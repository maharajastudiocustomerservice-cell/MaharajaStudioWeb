# EnemyHider Class API Documentation

The `EnemyHider` is the central component of the AI Hiding System. Attach it to your AI agent to enable intelligent cover-finding and retreat behaviors. This documentation covers all public properties, methods, and events you can use to control and query the AI's state.

## 1. Core Properties (Status & State)

These properties provide real-time information about the AI's current state. They are read-only and are perfect for driving animations, behavior trees, or UI debugging.

---

### IsSearching

Returns `true` if the AI is currently in the process of finding a hiding spot.

*   **Use Case:** Prevent the AI from performing other actions (like attacking or reloading) while it's busy thinking about where to hide. It's an essential flag for state management in a Behavior Tree or State Machine.
*   **How to Use:**
    ```csharp
    EnemyHider hider = GetComponent<EnemyHider>();

    void Update()
    {
        // Example: Don't allow the AI to shoot while it's looking for cover.
        if (hider.IsSearching)
        {
            myWeaponController.HoldFire();
        }
    }
    ```

---

### IsInCover

Returns `true` if the agent has successfully reached its destination and is stationary.

*   **Use Case:** Use this to trigger "in cover" behaviors, such as crouching, peeking, or starting a timer before re-engaging. It confirms that the AI is not only safe but also in position.
*   **How to Use:**
    ```csharp
    EnemyHider hider = GetComponent<EnemyHider>();

    void Update()
    {
        // If the AI is in cover, make it crouch.
        if (hider.IsInCover)
        {
            animator.SetBool("IsCrouching", true);
        }
        else
        {
            animator.SetBool("IsCrouching", false);
        }
    }
    ```

---

### IsThreatened

A convenient alias for `IsNeedToHide()`. Returns `true` if the agent is currently visible to any player.

*   **Use Case:** This is the primary trigger for deciding *when* to start a search. It's a lightweight check that can be called every frame in an `Update` loop or as a condition in a Behavior Tree to initiate a retreat.
*   **How to Use:**
    ```csharp
    EnemyHider hider = GetComponent<EnemyHider>();

    void Update()
    {
        // If the AI is threatened and not already moving to cover, tell it to hide.
        if (hider.IsThreatened && !hider.IsMoving)
        {
            hider.RetreatToHide();
        }
    }
    ```

---

### IsMoving

Returns `true` if the NavMeshAgent is actively following a path to a destination.

*   **Use Case:** Useful for controlling animations (e.g., switching between idle/run) and for preventing the AI from starting a new search while it's already on its way to cover.
*   **How to Use:**
    ```csharp
    EnemyHider hider = GetComponent<EnemyHider>();

    void Update()
    {
        // Control the "IsRunning" parameter in the animator.
        animator.SetBool("IsRunning", hider.IsMoving);
    }
    ```

---

### HasValidHidingSpot

Returns `true` if the agent has a valid `CurrentHidingSpot`, even if it hasn't reached it yet.

*   **Use Case:** Differentiate between an AI that has no plan (`HasValidHidingSpot` is false) and an AI that has a plan but is still executing it (`HasValidHidingSpot` is true, but `IsInCover` is false).
*   **How to Use:**
    ```csharp
    // In a Behavior Tree, this could be a condition:
    // "Does the AI have a valid destination?"
    if (hider.HasValidHidingSpot)
    {
        // Proceed with movement task.
    }
    else
    {
        // Trigger a search task.
    }
    ```

---

### CurrentHidingSpot

The `HidingSpot` struct the agent is currently moving to or located at. It's `HidingSpot.Invalid` if no spot has been found.

*   **Use Case:** Access detailed information about the AI's destination, such as its position, the direction of cover (`coverNormal`), and whether it can peek left or right.
*   **How to Use:**
    ```csharp
    if (hider.IsInCover && hider.CurrentHidingSpot.canPeekRight)
    {
        // The AI is in cover and can peek right, so trigger a peek-and-shoot action.
        myCombatLogic.PerformPeek(hider.CurrentHidingSpot.peekRightPosition);
    }
    ```

---

### LastKnownPlayerPosition

The position where the AI last had a line of sight to a player. This acts as the AI's short-term memory.

*   **Use Case:** This is crucial for tactical decisions. When the AI gets into cover, it should aim or throw grenades towards this position, not the player's new, unseen location.
*   **How to Use:**
    ```csharp
    // When the AI decides to throw a grenade from cover:
    if (hider.IsInCover && hider.LastKnownPlayerPosition.HasValue)
    {
        Vector3 target = hider.LastKnownPlayerPosition.Value;
        myGrenadeController.ThrowAt(target);
    }
    ```

---

### TimeInCover

Returns the number of seconds the agent has been stationary in its current valid cover spot.

*   **Use Case:** Make the AI's behavior more dynamic. For example, an aggressive AI might decide to pop out of cover after 2 seconds, while a cautious one might wait for 5 seconds.
*   **How to Use:**
    ```csharp
    // A cautious AI might only re-engage after being in cover for a while.
    if (hider.IsInCover && hider.TimeInCover > 5.0f)
    {
        // It's been 5 seconds, time to look for an opportunity to attack.
        myCombatLogic.SeekAttackOpportunity();
    }
    ```

---

## 2. Core Methods (Actions)

These methods instruct the `EnemyHider` to perform an action, such as starting a search or stopping its current behavior.

---

### RetreatToHide()

Initiates a search for the best hiding spot using the default settings. This is the primary and most common way to make the AI find cover.

*   **Use Case:** This is your go-to method. Call it when the AI is exposed and needs to find safety.
*   **How to Use:**
    ```csharp
    EnemyHider hider = GetComponent<EnemyHider>();

    void OnTookDamage()
    {
        // When the AI takes damage, it should immediately try to find cover.
        hider.RetreatToHide();
    }
    ```

---

### RetreatToHide(SearchProfile profile)

Initiates a search using a temporary `SearchProfile` to override the default settings for a single search.

*   **Use Case:** This is powerful for creating dynamic, context-aware AI. An AI might use a "cautious" profile (preferring distant cover) when its health is low, or an "aggressive" profile (preferring ambush spots) when it has a shotgun.
*   **How to Use:**
    ```csharp
    // Create a profile for an aggressive flank.
    var flankProfile = new SearchProfile
    {
        // Create a dictionary to override scorer weights.
        ScorerWeightOverrides = new Dictionary<HideSpotScorerSO, float>
        {
            { crossfireScorerAsset, 5.0f }, // Heavily prioritize crossfire angles
            { distanceScorerAsset, 0.5f }   // Care less about being far away
        }
    };

    // Tell the AI to find a flanking position using this custom profile.
    hider.RetreatToHide(flankProfile);
    ```

---

### RetreatToHideInArea(Vector3 areaCenter, float areaRadius)

A convenient wrapper that tells the AI to find cover, but only within a specific circular area in the world.

*   **Use Case:** Perfect for mission objectives or squad tactics. For example, "Defend this control point" means the AI should find cover *inside* the control point's radius, not run across the map.
*   **How to Use:**
    ```csharp
    Vector3 controlPointCenter = new Vector3(10, 0, 50);
    float controlPointRadius = 15f;

    // The AI must find cover within the designated objective area.
    hider.RetreatToHideInArea(controlPointCenter, controlPointRadius);
    ```

---

### StopAndClear()

Immediately cancels any ongoing search, stops all movement, and clears the current hiding spot.

*   **Use Case:** Use this to interrupt the AI's current action. For example, if a player gets too close, you might want the AI to stop retreating and switch to close-quarters combat, regardless of its previous plan.
*   **How to Use:**
    ```csharp
    float distanceToPlayer = Vector3.Distance(transform.position, player.position);

    if (distanceToPlayer < 5.0f)
    {
        // The player is too close! Stop running and fight back.
        hider.StopAndClear();
        myCombatLogic.EngageInMelee();
    }
    ```

---

### CancelSearch()

Cancels an ongoing *asynchronous* search. It does not stop the agent if it's already moving.

*   **Use Case:** This is a more subtle interruption than `StopAndClear()`. Use it if you want to abort the *thinking* process (which can take a few frames) without necessarily stopping the AI's current movement.
*   **How to Use:**
    ```csharp
    // The AI started a search, but the player suddenly died.
    void OnPlayerDied()
    {
        // Cancel the search since the threat is gone. The AI might continue to its last spot.
        hider.CancelSearch();
    }
    ```

---

## 3. Query Methods (Checks & Information)

These methods allow you to ask questions and get information from the system without changing the AI's state. They are ideal for decision-making logic.

---

### IsNeedToHide()

Performs a lightweight line-of-sight check to see if the agent is currently visible to any player.

*   **Use Case:** This is the most common query. Use it in `Update` or a Behavior Tree to decide if a retreat is necessary. It's much cheaper than running a full `RetreatToHide()` every frame.
*   **How to Use:**
    ```csharp
    // A classic "tick" for a Behavior Tree node.
    public NodeStatus CheckThreatStatus()
    {
        if (hider.IsNeedToHide())
        {
            return NodeStatus.FAILURE; // We are exposed, the "Stay Safe" check fails.
        }
        return NodeStatus.SUCCESS; // We are hidden, the check passes.
    }
    ```

---

### CanFindHidingSpot(out HidingSpot potentialSpot)

Performs a quick, synchronous search to see if *any* valid hiding spot exists from the current position. It does **not** make the AI move.

*   **Use Case:** A crucial "look before you leap" check. Before deciding to retreat, you can use this to see if there's anywhere *to* retreat to. If not, the AI might choose to stand and fight instead of running into a dead end.
*   **How to Use:**
    ```csharp
    // Before committing to a retreat, check if it's even possible.
    if (hider.IsThreatened)
    {
        if (hider.CanFindHidingSpot(out HidingSpot spot))
        {
            // A safe spot exists, so let's go!
            hider.RetreatToHide();
        }
        else
        {
            // There's nowhere to hide. Stand and fight!
            myCombatLogic.HoldPositionAndFight();
        }
    }
    ```

---

### GetTopNHidingSpotsSync / GetTopNHidingSpotsAsync

Performs a full search and returns a list of the best hiding spots found, sorted by score. The `Sync` version blocks the main thread for a frame, while the `Async` version is non-blocking.

*   **Use Case:** Advanced usage for squad tactics or complex behaviors. A squad leader could call this to find the top 3 spots and then assign each squad member to one of them, ensuring they don't all run to the same piece of cover.
*   **How to Use (Async):**
    ```csharp
    private async void AssignSquadPositions()
    {
        // Find the 3 best cover spots near the squad leader.
        List<HidingSpot> bestSpots = await squadLeader.hider.GetTopNHidingSpotsAsync(3);

        if (bestSpots.Count >= 3)
        {
            squadMember1.hider.MoveToSpot(bestSpots[0]);
            squadMember2.hider.MoveToSpot(bestSpots[1]);
            squadMember3.hider.MoveToSpot(bestSpots[2]);
        }
    }
    ```

---

### ReEvaluateCurrentSpot()

Checks if the agent's `CurrentHidingSpot` is still safe from all players. This is much cheaper than a full new search.

*   **Use Case:** Periodically check if the AI's cover has been flanked. If a player moves and gets a new angle, this method will return `false`, signaling that the AI needs to find a new, better spot.
*   **How to Use:**
    ```csharp
    // Run this check every couple of seconds while in cover.
    IEnumerator CheckCoverValidity()
    {
        while(true)
        {
            yield return new WaitForSeconds(2.0f);
            if (hider.IsInCover && !hider.ReEvaluateCurrentSpot())
            {
                // Our cover is blown! Find a new spot.
                hider.RetreatToHide();
            }
        }
    }
    ```

---

## 4. Configuration Methods

These methods are used to set up and change the `EnemyHider`'s behavior and context at runtime.

---

### SetPlayers(IReadOnlyList<Transform> playerList) / SetAllies(IReadOnlyList<Transform> allyList)

Updates the list of player targets and allies that the AI should be aware of.

*   **Use Case:** This is fundamental for setup. Your game manager or AI spawner should call this to tell each AI who its enemies and friends are. It should be updated if players or allies enter or leave the AI's awareness range.
*   **How to Use:**
    ```csharp
    EnemyHider myAI = GetMyAI();
    List<Transform> allPlayers = FindAllPlayerTransforms();
    List<Transform> nearbyAllies = FindNearbyAllies();

    myAI.SetPlayers(allPlayers);
    myAI.SetAllies(nearbyAllies);
    ```

---

### UpdateHidingSettings(HidingSettingsSO newSettings)

Swaps the currently used `HidingSettingsSO` asset at runtime.

*   **Use Case:** Allows for profound changes in AI behavior. You could have different settings assets for different enemy types (e.g., "GruntSettings", "SniperSettings") or for different game states (e.g., "StealthSettings", "CombatSettings").
*   **How to Use:**
    ```csharp
    public HidingSettingsSO cautiousSettings;
    public HidingSettingsSO aggressiveSettings;

    void OnHealthLow()
    {
        // When health is low, switch to the cautious behavior set.
        hider.UpdateHidingSettings(cautiousSettings);
    }
    ```

---

### SetCurrentEyeHight(float eyeHeight)

Updates the AI's eye height, which is used for all visibility calculations.

*   **Use Case:** Make the AI's visibility checks more accurate based on its stance. If the AI is crouching, its eye height should be lower, which might make shorter objects valid cover.
*   **How to Use:**
    ```csharp
    void Crouch()
    {
        animator.SetBool("IsCrouching", true);
        hider.SetCurrentEyeHight(0.8f); // Set eye height for crouching.
    }

    void StandUp()
    {
        animator.SetBool("IsCrouching", false);
        hider.SetCurrentEyeHight(1.7f); // Reset to default standing height.
    }
    ```

---

### ForgetPlayerLocation()

Manually clears the AI's memory of the `LastKnownPlayerPosition`.

*   **Use Case:** Useful in stealth scenarios. If the player successfully hides for a certain amount of time, you can call this to make the AI "give up" the search and return to its patrol, making it seem less omniscient.
*   **How to Use:**
    ```csharp
    // Called by a stealth manager after the player has been hidden for 10 seconds.
    public void OnPlayerLost()
    {
        aiHider.ForgetPlayerLocation();
        aiHider.ReturnToPatrol();
    }
    ```