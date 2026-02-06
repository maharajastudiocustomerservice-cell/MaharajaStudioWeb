# Scorers Reference

This document contains a comprehensive reference for all Scorers in the system.

## Standard Scorers (V1)


---

# Scorer: Ambush Potential

**`AmbushScorerSO`** is a sophisticated scorer that evaluates hiding spots based on their tactical potential for an ambush. It rewards spots that are concealed from the player's current position but maintain a clear line of sight to a strategic location.

## How It Works

This scorer operates on a simple but powerful principle for setting up an ambush: **hide from where the player IS, but watch where the player WAS.**

It checks three conditions in order:

1.  **Is the spot hidden?** It first uses the `IVisibilityService` to check if the candidate spot is visible to any player from their **current, real-time position**. If the AI can be seen, the spot is immediately disqualified and gets a score of 0.
2.  **Can the spot see the target?** If the spot is hidden, it then determines an "ambush target." This is the player's **last known position (LKP)** if available, otherwise it falls back to the closest player's current position. It then performs a raycast to see if there is a clear line of sight from the candidate spot to this ambush target. If the view is obstructed, the spot is disqualified with a score of 0.
3.  **Is it at the right distance?** If the spot is both hidden and has a clear view of the target, it receives a score based on how close it is to the `Optimal Ambush Distance`. The closer to this ideal distance, the higher the score (maxing out at 1.0).

This logic creates an intelligent behavior where the AI will try to find a flanking position or overlook that allows it to surprise the player.

## Parameters

*   **Weight**: As with all scorers, this determines how much influence the `AmbushScorer` has on the final decision. A high weight means the AI will strongly prioritize setting up ambushes.
*   **Optimal Ambush Distance**: This float value, set on the scorer asset, defines the ideal range in meters for the AI to be from the ambush target point.

## Use Cases

*   **Lying in Wait**: The primary use case. Create AI that hides around a corner and waits for the player to walk past the location where they were last seen.
*   **Tactical Overwatch**: Excellent for snipers or other ranged AI. They will find concealed positions that have a good vantage point over key areas where the player is likely to be.
*   **Smart Repositioning**: When an AI loses sight of the player, this scorer helps it choose a new hiding spot that anticipates the player's movements, rather than just running away.

## Performance and Dependencies

This is a moderately expensive scorer. For each candidate spot, it performs:
*   A visibility check via the `IVisibilityService` (which often involves its own raycasts).
*   An additional `Physics.Raycast` to check the line of sight to the ambush target.

Because of this, its performance cost is higher than simple scorers like `DistanceScorerSO`. It's highly effective but should be used when its specific tactical behavior is desired. It also requires the `EnemyHider` to have seen a player to generate a `playerLastKnownPosition` to be maximally effective.

---

# Scorer: Cover Height

`CoverHeightScorerSO` evaluates a candidate spot based on the height of the cover in front of it, ensuring the AI does not try to hide behind objects that are too short to conceal it properly.

## How It Works
This scorer adds a layer of intelligence to cover selection by checking not just if there is cover, but if that cover is tall enough. It operates only on candidates that have a coverNormal provided by their generator (like AutomaticCoverProviderSO or BehindObstacleProviderSO).

For a given `candidate spot`, the scorer simulates the agent's head position. It then casts a short ray from just in front of the agent's head directly towards the primary threat (`the player's last known position or current position`).
* If the ray hits an `occluder`, it means there is a solid object at head-level between the agent and the threat. The spot receives a high score (1.0), indicating good, tall cover.
* If the ray does not hit anything, it implies the cover is too low (e.g., a waist-high crate), and the agent's head would be exposed. The spot receives a low score (0.0).
* If a candidate has no coverNormal, the scorer returns a neutral score (0.5) so as not to penalize providers that don't generate this data.

## Parameters
*  **Check Offset:** How far in front of the agent's head to start the raycast. This should be a small value to ensure the check is close to the agent.
*  **Check Distance:** The maximum length of the raycast. This should be short, as it's only meant to verify the immediate cover, not see across the map.

## Use Cases
Realistic Cover Selection: This is a crucial scorer for preventing silly AI behavior, like crouching behind a small rock or a low railing while thinking it's completely hidden.
Enhancing Tactical Realism: In shooters or tactical games, this ensures that AI agents prioritize cover that offers full protection, leading to more believable and challenging encounters.

## Performance
The performance impact of this scorer is very low. It performs a single, very short Physics.Raycast for each candidate that has cover information. In most scenarios, its cost is negligible.

---

# Scorer: Crossfire

`CrossfireScorerSO` evaluates hiding spots based on their potential to create a tactical crossfire with allied units. It rewards spots that provide a flanking angle on the player's position relative to the positions of other AI agents.

## How It Works

This scorer promotes intelligent squad behavior by moving beyond simple grouping. Instead of just huddling together, it encourages agents to spread out and attack from multiple angles.
For a given candidate spot, the scorer does the following:

1. It identifies the primary threat location (the player's last known or current position).
2. It iterates through all of the agent's allies.
3. For each ally, it calculates the angle formed at the player's position between the ally and the candidate spot (ally -> player -> candidate).
4. The scorer finds the maximum angle created among all allies.
5. The final score is based on how close this maximum angle is to the Optimal Angle defined in the asset. An angle of 90 degrees (a perfect "L" shape flank) would receive the highest score, while positions that are directly in line with an ally receive a low score.

## Setup

* Ensure your EnemyHider components have their allies list populated correctly.
* Create an instance of the CrossfireScorerSO asset.
* In the asset's Inspector, configure the Optimal Angle (90 is a good default) and Minimum Angle (e.g., 20, to ignore insignificant angles).
* Add this scorer asset to the Scorers list in your HidingSettingsSO and give it a moderate weight (e.g., 1.0 to 2.0). Its influence should be a significant factor in repositioning decisions.

Use Cases

*  **Advanced Squad Tactics:** The primary use case. Transform a group of AI from a simple mob into a coordinated squad that actively tries to flank and suppress the player.
*  **Making Combat More Challenging:** A crossfire is a difficult situation for a player to deal with. This scorer directly increases the tactical challenge of combat encounters.
*  **Dynamic Encounters:** The AI will dynamically create flanking maneuvers based on the current positions of all units, leading to less predictable and more engaging fights.

---

# Scorer: Darkness

**`DarknessScorerSO`** is a very simple scorer that evaluates hiding spots based on the overall ambient light level of the scene. It rewards spots in environments that are generally darker.

## How It Works

This scorer operates on a very simple principle: it reads the scene's global ambient light intensity value from `RenderSettings.ambientIntensity`.

*   If the ambient intensity is high (a bright scene), it returns a low score.
*   If the ambient intensity is low (a dark scene), it returns a high score.

The score is calculated as `1.0f - ambientIntensity`, clamped between 0 and 1.

**Important Note:** This is a **global** scorer. At any given moment, it will return the exact same score for **every single candidate spot** regardless of their position. It does not check for dynamic lights or shadows cast by objects. Its purpose is to give a general "bias" towards darkness for the AI's decision-making process.

## Parameters

*   **Weight**: Determines how much the AI should care about the overall darkness of the scene when choosing a spot. If you want AI to strongly prefer hiding when the level is dark, give this a high weight.

## Use Cases

*   **Time of Day Behavior**: This scorer is perfect for influencing AI behavior based on a day/night cycle. If you change the ambient intensity at runtime to simulate the transition from day to night, this scorer will automatically make your AI more likely to hide during the night.
*   **General "Creature of the Dark" AI**: For AI that should be more active or more likely to take cover in dark levels (e.g., caves, nighttime scenes), this scorer provides a simple and extremely performant way to achieve that.

## Performance

The performance of this scorer is **excellent**. It is one of the fastest scorers available because it only involves reading a single float value from the render settings. Its impact on performance is negligible, making it safe to use in any configuration.

---

# Scorer: Defensive Position Bonus

**`DefensivePositionScorerSO`** is a powerful scorer that provides "inertia" or a defensive bonus. It evaluates the agent's **current position** to determine if it's safe, making the AI less likely to abandon a good spot and more likely to flee a compromised one.

## How It Works

This scorer is unique because it only cares about one specific candidate: the one that represents the agent's current location. For all other candidate spots, it returns a score of 0.

When it evaluates the agent's current position, it performs a critical check:

1.  **Is the agent currently visible to any player?** It uses the `IVisibilityService` to check if the agent can be seen from its current spot.

2.  The result of this check leads to one of two extreme outcomes:
    *   **If VISIBLE:** The agent's cover is blown. The scorer returns `float.NegativeInfinity`. This is a powerful penalty that effectively disqualifies the current position, forcing the AI to choose a different hiding spot. It creates a strong "get to cover!" instinct.
    *   **If NOT VISIBLE:** The agent is safe. The scorer returns the small, positive `inertiaBonus`. This gives a slight advantage to staying put, ensuring the AI won't move to a new spot unless it's significantly better than the one it's already in. This prevents fidgety, unnecessary movement.

## Parameters

*   **Weight**: Determines the influence of this scorer. Because it can return `NegativeInfinity`, its penalty effect is absolute regardless of weight. The weight primarily affects how influential the `inertiaBonus` is when compared to scores from other active scorers.
*   **Acceptance Radius**: A small radius to determine if a candidate point is close enough to be considered the agent's current position.
*   **Inertia Bonus**: The small score bonus (e.g., 0.1 or 0.2) applied if the agent is currently safe. This value should be kept relatively low.

## Use Cases

*   **Creating Stable AI**: This is the primary solution for preventing AI from constantly shuffling between two or more hiding spots that have very similar scores. The inertia bonus makes them "prefer" to stay still.
*   **Intelligent Cover Response**: This scorer is essential for creating AI that reacts believably to being discovered. The moment it becomes visible, its top priority will be to move to a new, safer location.
*   **Establishing a Defensive Baseline**: It should be included in most configurations to create a base level of intelligent self-preservation.

## Note

* Chose the parameters value and weight in the HidingSetting for this scorer very carefully because it's very sencitive one and a wrong weight for this scorer may cause the agent will never move. so try to give it's weight as low as possible like 0.1 or less than 0.1


## Performance and Dependencies

This scorer's performance is excellent. It only performs its main logic (the visibility check) for a single candidate spot per evaluation cycle.

*   It is highly dependent on a correctly configured **`IVisibilityService`**.
*   It is designed to be used with the **`CurrentPositionProviderSO`**, which ensures that the agent's current position is always included in the list of candidates to be evaluated. Without this provider, the `DefensivePositionScorer` will do nothing.

---

# Scorer: Distance From Players

**`DistanceScorerSO`** is a fundamental scorer that evaluates hiding spots based on their distance from the nearest player. It encourages AI to move farther away from threats.

## How It Works

This scorer calculates the distance from the candidate hiding spot to every player currently known to the system. It finds the shortest of these distances and uses that value to calculate a score.

The score is normalized by the `Search Radius` from your `HidingSettings`. The formula is essentially:

`Score = (Distance to Nearest Player) / (Search Radius * normalizeByRadius)`

This means a spot right next to a player will have a score near 0, while a spot at the edge of the search radius will have a score near 1.0. In short, **farther away is better.**

### Negative Weight Trick

This scorer has a special interaction with negative weights. If you give it a negative weight in the `HidingSettings` (e.g., -1.0), you will invert its behavior. Instead of rewarding distance, it will **reward proximity**, encouraging the AI to find the closest possible (safe) hiding spot. This is useful for aggressive or hunter-style AI.

## Parameters

*   **Weight**: Determines how much the AI prioritizes distance. A high positive weight creates cowardly AI. A high negative weight creates aggressive AI.
*   **Normalize By Radius**: This multiplier on the scorer asset adjusts the normalization.
    *   `1.0` (default): The score scales linearly with the `Search Radius`. A spot at the search radius distance gets a score of 1.0.
    *   `< 1.0`: The score will reach 1.0 before hitting the full search radius. For example, at `0.5`, a spot at half the search radius already gets a score of 1.0.
    *   `> 1.0`: The score will only approach 1.0 for distances beyond the search radius.

## Use Cases

*   **Cowardly AI**: Use with a high positive weight. This is the primary scorer for AI that should run away from the player.
*   **Ranged Units**: Use with a moderate positive weight for archers or mages who need to maintain a safe distance.
*   **Stealthy Hunters**: Use with a high **negative weight** to make the AI try to sneak as close to the player as possible while remaining hidden.

## Performance

The performance of this scorer is **excellent**. For each candidate spot, it performs a simple `Vector3.Distance` calculation for each player. This is a very fast operation, and the scorer has a negligible impact on performance.

---

# Scorer: FOV Avoidance

**`FOVScorerSO`** is a critical scorer for stealth gameplay. It evaluates spots based on whether they fall within any player's field of view (FOV). It heavily penalizes spots that the player is actively looking towards.

## How It Works

This scorer performs a simple but crucial binary check using the `IVisibilityService`:

1.  It asks the `IVisibilityService`: "Is this candidate spot inside any player's viewing cone AND visible from their eyes?"
2.  Based on the answer, it returns a score:
    *   **If YES:** The spot is in the player's direct field of view. The scorer returns **0.0**.
    *   **If NO:** The spot is outside the player's direct field of view (either behind them, to the side, or obscured by an object). The scorer returns **1.0**.

This creates a strong incentive for the AI to stay out of the player's forward-facing view cone, encouraging flanking and sneaking behaviors.

## Distinguishing from `VisibilityScorer`

It's important to understand the difference between this scorer and the general `VisibilityScorer`:

*   **`VisibilityScorer`**: Checks for a clear line of sight from the player's eyes to the spot, regardless of which direction the player is facing. A spot directly behind the player would be considered "visible" if there are no walls in the way.
*   **`FOVScorer`**: *Also* checks for line of sight, but *only* if the spot is within the player's view cone angle. A spot directly behind the player will always get a perfect score of 1.0 from this scorer, because it's not in the FOV.

For true stealth gameplay, you typically use **both** scorers together. This tells the AI to:
1.  Strongly prefer spots outside the player's FOV (`FOVScorer`).
2.  Of those spots, prefer the ones that are also physically hidden behind objects (`VisibilityScorer`).

## Parameters

*   **Weight**: Determines how strongly the AI will prioritize staying out of the player's view cone. For stealthy AI, this should usually have a very high weight.

## Use Cases

*   **Classic Stealth Mechanics**: This is the cornerstone of any system where AI needs to avoid a player's vision cone (like in *Metal Gear Solid* or *Dishonored*).
*   **Flanking Behavior**: By heavily penalizing spots in front of the player, this scorer naturally encourages AI to move to the player's sides or back.
*   **Creating "Blind Spots"**: This scorer is what makes hiding behind a player a valid and rewarding tactic for the AI.

## Performance and Dependencies

The performance of this scorer is entirely dependent on the underlying implementation of `IVisibilityService.InAnyPlayerFOVAndVisible`. This check typically involves fast vector math (a dot product to check the angle) and potentially a `Physics.Raycast` to check for obstructions.

It is moderately expensive, more so than simple math-based scorers, but essential for this type of gameplay. It has a hard dependency on a correctly configured **`IVisibilityService`**.

---

# Scorer: Hazard Avoidance

`HazardAvoidanceScorerSO` prevents the AI from choosing hiding spots inside known environmental dangers, such as fires, poison clouds, or the blast radius of a grenade.

## How It Works

This system relies on Hazard components being placed on objects that represent a threat. Any GameObject with a Hazard component will register itself with a central HazardRegistry when it becomes active.
The HazardAvoidanceScorer queries this registry to get a list of all active hazards. For each candidate hiding spot, it checks the distance to every hazard.
If the candidate's position is within the defined radius of any Hazard object, the scorer returns float.NegativeInfinity. This instantly and absolutely disqualifies the spot, forcing the AI to look for cover elsewhere. This is a critical self-preservation behavior.

## Setup

On any GameObject that represents a danger (e.g., a fire particle system, a grenade prefab), add the new Hazard component.
Adjust the Radius property on the Hazard component to match the area of effect of the danger. A red gizmo in the Scene view will help you visualize this area.
Create an instance of the HazardAvoidanceScorerSO asset in your project files.
Add this scorer asset to the Scorers list in your HidingSettingsSO. It is highly recommended to give this scorer a high weight (e.g., 5.0) to ensure its decisions are always prioritized.

## Use Cases

*  **Dynamic Dangers:** Essential for making AI react to dynamic events like grenades, molotovs, or artillery strikes.
*  **Persistent Hazards:** Prevents AI from unintelligently pathing through fires, acid pools, or other static level hazards when looking for cover.
*  **Enhanced Believability:** Stops the AI from making immersion-breaking mistakes, making them feel more aware and intelligent.

---

# Scorer: Hide Spot Scorer (Base Class)

`HideSpotScorerSO` is not a functional scorer itself. It is an abstract base class that serves as the template for all other scorer assets.

## How It Works

The `Hiding System's` evaluation process is modular. It doesn't use a single, hard-coded method for judging hiding spots. Instead, it uses a list of specialized "scorers." Each scorer is a ScriptableObject that implements one specific way of evaluating a candidate spot and returning a numerical score.
The HideSpotScorerSO class defines the contract that every scorer must follow. It contains a single abstract method:
`public abstract float Score(in HidingContext ctx, in CandidateInfo candidate);`

*  **HidingContext ctx:** A struct containing all the information the scorer might need, such as player locations, the agent's own position, system settings, etc.
*  **CandidateInfo candidate:** The potential hiding spot being evaluated.
return float: The scorer must return a floating-point number. By convention, higher scores are better. A score of float.NegativeInfinity will instantly disqualify the candidate. Scores are typically normalized between 0.0 and 1.0.
By inheriting from this class, you can create your own custom logic for evaluating cover, which will then be seamlessly integrated into the main system by adding it to the Scorers list in your HidingSettingsSO.

## Setup

`To create a new, custom scorer:`
`Create a new C# script.`
`Make the class inherit from HideSpotScorerSO.`
`Add the [CreateAssetMenu] attribute to allow you to create instances of it in the Unity Editor.`
`Implement the Score method with your custom logic.`
`Create an instance of your new scorer asset via the Assets -> Create menu.`
`Drag your new scorer asset into the Scorers list in your HidingSettingsSO and assign it a weight.`

## Use Cases

System Extensibility: The primary purpose is to allow developers to easily extend the AI's decision-making logic without altering the core system code.
Project-Specific AI Behavior: You can create scorers tailored to your game's unique mechanics. For example:
* A scorer that prefers spots near health packs.
* A scorer that avoids areas with hazardous materials.
* A scorer that gives a bonus to spots with a view of a mission objective.

## Performance

As a base class, it has no performance impact. The performance of any given scorer is entirely dependent on the complexity of the logic implemented within its Score method.

---

# Scorer: Height Difference

`HeightDifferenceScorerSO` scores a candidate based on its vertical distance from the agent, discouraging movement to different floors or extreme heights unless the spot is significantly better in other ways.

## How It Works

This scorer introduces a preference for the AI to stay on its current vertical plane. It calculates the absolute difference in the `Y-axis` value between the agent's current position and the candidate spot's position.
The scoring is inversely proportional to this height difference:
A spot on the same level (height difference is zero) receives a perfect score of 1.0.
As the vertical distance increases, the score decreases linearly.
If the height difference exceeds the maxAcceptableHeightDifference, the score becomes 0.0.
This acts as a penalty for vertical movement, meaning a spot on another floor must be significantly better in other aspects (like visibility, safety, etc.) to overcome this penalty and be chosen.

## Parameters

*  **Max Acceptable Height Difference:** The maximum vertical distance the AI will consider before the score drops to zero. This should typically be set to a value slightly greater than the height of a single floor in your level (e.g., 4-5 meters).

## Use Cases

*  **Controlling Vertical Movement:** Its primary use is to prevent AI from erratically running up and down stairs or jumping off ledges just because a spot is slightly better. It promotes more deliberate and logical movement.
*  **Improving Performance:** By penalizing distant vertical spots, it can indirectly favor closer, more relevant hiding locations, potentially reducing the need for long and complex pathfinding calculations.
*  **Defining Agent Behavior:** You could give different AI types different settings. A nimble, spider-like robot might have a high maxAcceptableHeightDifference, while a heavy ground soldier would have a very low one.

## Performance
This scorer is extremely fast. It only involves a few floating-point subtractions and divisions (Mathf.Abs). Its performance impact is virtually zero, making it a safe and effective scorer to add to any configuration.

---

# Scorer: Objective Proximity

`ObjectiveProximityScorerSO` scores candidate spots based on their distance and relevance to a mission objective. This makes the AI "mission-aware," preventing it from abandoning a critical location it's supposed to be defending.

## How It Works

This scorer relies on a new static service called ObjectiveService. Your game's own mission scripts are responsible for registering and unregistering objective locations with this service.
The ObjectiveProximityScorerSO asset is configured to care about a specific ObjectiveType (e.g., Defend, Attack).
When scoring a candidate, it finds the nearest objective of the matching type. The scoring logic then rewards proximity:
A spot very close to the objective receives a high score (1.0).
As the distance to the objective increases, the score decreases linearly.
If the distance exceeds the Max Distance setting on the scorer, the score becomes 0.0.
This creates a powerful incentive for the AI to choose cover that keeps it relevant to the mission, adding a crucial layer of tactical intelligence.

## Setup

From your game logic scripts (e.g., a "King of the Hill" manager, a "Bomb Defusal" script), get a reference to the objective's position.
When the objective becomes active, call `ObjectiveService.RegisterObjective(...)`, passing in its position and type.
When the objective is completed or moves, call `ObjectiveService.UnregisterObjective(...)` or `ClearObjectives()`.
Create an instance of the `ObjectiveProximityScorerSO` asset.
Configure its Target Type, Optimal Distance, and Max Distance in the Inspector.
Add this scorer asset to the Scorers list in your HidingSettingsSO and give it an appropriate weight.

## Use Cases

Defensive Scenarios: Essential for AI that needs to guard a flag, control point, or VIP. This scorer will force them to hide near the objective instead of running away.
Offensive Scenarios: By setting the type to Attack, you can encourage AI to select hiding spots that move them progressively closer to their target.
Dynamic Objectives: Works perfectly for objectives that move, as long as your game logic continually updates the objective's position in the ObjectiveService.

---

## Scorer: Partial Visibility

`PartialVisibilityScorerSO` provides a more thorough visibility check than the standard VisibilityScorerSO. It ensures the agent's entire body is concealed by checking multiple points against player line of sight.

## How It Works

While the basic VisibilityScorerSO might only check one or two points, PartialVisibilityScorerSO checks three distinct points on the agent's body relative to the candidate position:
*  **Head Point:** At the agent's full eye height.
*  **Chest Point:** At the agent's center of mass (e.g., 60% of eye height).
*  **Feet Point:** Near the ground (e.g., 0.2 meters up).
It then uses the IVisibilityService to check if any player has a direct, unobstructed line of sight to any of these three points.
If all three points are hidden from all players, the spot is considered fully concealed and receives a perfect score of 1.0.
If even one point is visible to any player, the spot is considered compromised and receives a score of 0.0.
This creates a strict, all-or-nothing evaluation of cover.

## Use Cases

*  **Creating Cautious AI:** This is the ideal scorer for stealth games or for AI archetypes (like snipers or scouts) that prioritize complete concealment above all else.
*  **Eliminating Exploits:** It prevents situations where a player can see and shoot an AI's feet or head poking out from cover, even though the AI's center point is hidden.
*  **High-Difficulty Settings:** This can be used to make AI on higher difficulty levels much harder to spot and engage, as they will only choose locations that offer total body cover.

## Performance

The performance cost is slightly higher than the basic `VisibilityScorerSO` because it makes up to three calls to AnyPlayerHasLineOfSight per candidate instead of one or two. However, because the underlying visibility checks are often optimized (especially in the asynchronous system), the impact is still relatively low and is a worthwhile trade-off for the increased fidelity.

---

# Scorer: Path Safety

**`PathSafetyScorerSO`** is one of the most intelligent and important scorers for creating believable stealth AI. It evaluates the safety of the **path** an agent would take to reach a hiding spot, not just the destination itself. It heavily penalizes paths that would expose the agent to player view.

## How It Works

For each candidate hiding spot, this scorer performs a detailed analysis of the journey from the agent's current position to that spot.

1.  **Calculate Path**: It first calculates the `NavMeshPath` to the candidate spot. If no complete path exists, the spot is unreachable and is disqualified with a score of `NegativeInfinity`.
2.  **Sample Path Points**: It gathers all the corners of the path. To ensure safety on long, straight sections, it also adds extra sample points in the middle of any path segment longer than the `Long Segment Threshold`.
3.  **Check Visibility**: It then iterates through all these sample points along the path. For each point, it uses the `IVisibilityService` to check if that point is visible to any player.
4.  **Calculate Exposure**: It determines the `visibilityRatio`—the percentage of sample points that were visible to a player.
5.  **Apply Penalties**: The scoring logic is applied in two stages for maximum control:
    *   **Hard Disqualification**: If the `visibilityRatio` is greater than the `Visibility Threshold`, the path is considered too dangerous. The scorer returns `NegativeInfinity`, completely disqualifying it. This acts as a hard "do not cross" rule. (This threshold can be dynamically overridden per agent via the `HidingContext` for the "desperate retreat" feature).
    *   **Exponential Penalty**: If the path is not disqualified, its score is calculated based on its safety (`1.0 - visibilityRatio`). This value is then raised to the power of the `Penalty Exponent`. Using an exponent greater than 1 means that even small amounts of exposure are heavily penalized, making the AI extremely cautious.

## Parameters

*   **Weight**: Determines how much the AI prioritizes a safe path. For stealthy characters, this should have a very high weight.
*   **Visibility Threshold**: A hard limit (0.0 to 1.0) for how much of the path can be exposed. If the visible portion exceeds this, the path is invalid.
*   **Penalty Exponent**: Controls the scoring curve for paths that pass the threshold check. A value of `1` is a linear penalty. A value of `2` or higher makes the AI extremely averse to even minimal exposure.
*   **Long Segment Threshold**: The length of a straight path segment that will trigger an extra visibility check at its midpoint. This prevents AI from feeling safe running down a long, open hallway just because its corners are hidden.

## Use Cases

*   **Essential Stealth Behavior**: This is a cornerstone scorer for any AI that needs to be sneaky. It's the difference between an AI that intelligently skirts cover and one that foolishly runs across an open room.
*   **Creating Cautious AI**: By tuning the exponent, you can create AI personalities ranging from slightly cautious to extremely risk-averse.
*   **Preventing "Suicidal" Traverses**: It stops the AI from choosing a theoretically perfect hiding spot if the only way to get there is through a field of fire.

## Performance and Dependencies

**This is one of the most performance-intensive scorers in the system.** Its cost is significant and should be considered carefully. For every candidate spot, it must:
1.  Calculate a NavMesh path.
2.  Perform multiple visibility checks (which often involve raycasts) along the path's length.

The total cost scales with the number of candidate spots, the number of players, and the complexity (number of corners) of the potential paths.

*   **Recommendation**: Use this scorer when high-quality stealth is required, but be mindful of the performance cost. Consider reducing the number of candidate spots if this scorer is active.
*   **Dependencies**: It has hard dependencies on a valid **`NavMesh`** in the scene and a correctly configured **`IVisibilityService`**.

---

# Scorer: Player Path Prediction

PlayerPathPredictionScorerSO is a highly intelligent scorer that allows an AI to ambush the player by predicting their future position based on their current movement velocity.

## How It Works

This scorer elevates the AmbushScorer from reacting to the player's past position to anticipating their future actions. It leverages a new PlayerTrackerService to get the player's current velocity.
The scoring logic follows two critical ambush principles:
* Stay Hidden Now: The candidate spot must be hidden from the player's current position. If the AI can be seen while moving into its ambush spot, the ambush fails. This check receives a score of 0.
* See Them Later: The candidate spot must have a clear line of sight to the player's predicted future position. This position is calculated by projecting the player's current velocity forward in time by a set amount (Prediction Time).
* If both conditions are met, the candidate is a perfect ambush spot and receives a high score (1.0). Otherwise, it receives a score of 0.0.

## Setup

* Crucial Step: In the EnemyHider.cs script, you must add one line to the CreateHidingContext method: PlayerTrackerService.Update(players);. This is required to feed the tracker the data it needs. The updated script is provided below.
1. Create an instance of the PlayerPathPredictionScorerSO asset.
2. In the asset's Inspector, set the Prediction Time (e.g., 1.0 to 2.0 seconds, depending on how fast your players move).
3. Add this scorer asset to the Scorers list in your HidingSettingsSO. It works well with a moderate to high weight.

## Use Cases

*  **Creating "Smart" AI:** This is a hallmark of intelligent-feeling AI. It gives the impression that the AI is thinking ahead and outsmarting the player.
*  **Effective Ambushes:** Perfect for stealth games or for AI archetypes like assassins or trappers. The AI will correctly lead its target, hiding behind a corner and preparing to engage as the player sprints past.
*  **Punishing Predictable Player Behavior:** This scorer naturally punishes players who run in straight lines without checking corners, as the AI will be waiting for them.

---

# Scorer: Proximity Penalty

ProximityPenaltyScorerSO scores a candidate based on its raw proximity to the nearest player. It creates a "danger zone" around players, heavily penalizing or disqualifying spots that are too close, regardless of visibility.

## How It Works

This scorer enforces a critical self-preservation behavior by ensuring the AI maintains a safe distance from threats. It doesn't care about cover or line of sight; its only concern is raw distance.
*  **Finds Nearest Threat:** It first calculates the distance from the candidate hiding spot to every player. It only considers the distance to the closest player for its evaluation.
*  **Disqualification Check:** It checks if this distance is within the disqualificationRadius. If it is, the spot is considered suicidally close. The scorer returns float.NegativeInfinity, which instantly removes the spot from consideration, no matter how good other scorers think it is.
*  **Penalty Calculation:** If the spot is outside the disqualification zone but inside the larger dangerRadius, it is considered hazardous. The scorer calculates a penalty that scales linearly.
A spot right on the edge of the dangerRadius will get a score of 1.0 (no penalty).
A spot right on the edge of the disqualificationRadius will get a score of 0.0 (maximum penalty).
*  **Safe Zone:** If the spot is outside of the dangerRadius, this scorer considers it perfectly safe and gives it a full score of 1.0.

## Parameters

*  **Disqualification Radius:** The absolute "no-go" zone. Any candidate spot within this distance of a player will be instantly rejected. This should be a small value representing the agent's immediate personal space (e.g., 2-3 meters).
*  **Danger Radius:** A larger warning zone. Spots within this radius will be penalized. This should be a larger value representing the distance at which the agent starts to feel threatened (e.g., 7-10 meters).

## Use Cases

*  **Essential Self-Preservation:** This is a highly recommended scorer for nearly every configuration. It prevents the AI from making the naive mistake of hiding right next to an enemy.
*  **Enforcing Engagement Ranges:** It stops the AI from retreating to a "hidden" spot that is still within melee or shotgun range of a player.
*  **Creating Skittish AI:** By using a large dangerRadius, you can create AI characters that are more cautious and prefer to keep their distance.

## Performance

This scorer is extremely high-performance. It involves a simple loop and distance calculations (Vector3.SqrMagnitude). Its impact on performance is negligible, and the behavioral improvement it provides is immense.


---

# Scorer: Reachability

**`ReachabilityScorerSO`** is a fundamental utility scorer that evaluates spots based on whether they are reachable by the agent on the NavMesh and within a maximum travel distance.

## How It Works

This scorer acts as a critical filter to ensure the AI only considers valid, reachable hiding spots. For each candidate spot, it performs the following checks:

1.  **Path Calculation**: It attempts to calculate a complete `NavMeshPath` from the agent's current position to the candidate spot.
2.  **Path Validity**: It checks the status of the calculated path. If the status is not `PathComplete` (meaning the spot is on a separate NavMesh island or is blocked), the spot is considered unreachable.
3.  **Path Distance**: If the path is valid, it calculates the total length of the path by summing the distances between all its corners. It then compares this length to the `Path Max Distance` defined in the `HidingSettings`.

The scoring logic is as follows:

*   **If the path is invalid, incomplete, or longer than `Path Max Distance`:** The scorer returns `float.NegativeInfinity`. This is a hard penalty that completely disqualifies the candidate spot, preventing the AI from ever choosing it.
*   **If the path is valid and within the distance limit:** It returns a score between 0 and 1. The score is higher for **shorter paths**, calculated as `1.0 - (pathLength / pathMaxDistance)`. This gives a natural preference for closer spots.

## Parameters

*   **Weight**: Determines how much the AI should prioritize spots with shorter path distances.
*   **Path Max Distance** (from `HidingSettings`): This is the crucial setting for this scorer. It defines the maximum travel distance (in meters) that the AI is allowed to consider. Any spot requiring a longer path will be disqualified.
*   **NavMesh Area Mask** (from `HidingSettings`): Used to constrain the path calculation to specific NavMesh area types.

## Use Cases

*   **Filtering for "Dumb" Providers**: This scorer is **essential** when using providers that don't perform their own NavMesh checks, such as `VoxelGridProviderSO`. It acts as the filter that removes all the unreachable points generated by such providers.
*   **Enforcing a "Leash" on AI**: By setting `Path Max Distance`, you can effectively "leash" your AI, preventing it from choosing a hiding spot that is technically within its search radius but would require a very long and winding path to reach. This keeps the AI's movement tactically relevant.
*   **Performance Optimization**: By running this scorer early (by placing it high in the scorer list), you can quickly disqualify many invalid or distant spots. This saves more performance-intensive scorers (like `PathSafetyScorerSO`) from having to run their complex logic on spots the AI could never reach anyway.

## Performance and Dependencies

This scorer is moderately expensive. `NavMesh.CalculatePath` is a non-trivial operation and its cost will add up when run on many candidate spots. It is more expensive than simple math-based scorers but generally cheaper than those involving multiple physics raycasts.

*   **Dependencies**: It has a hard dependency on a valid **`NavMesh`** being present and correctly baked in the scene. Without a NavMesh, it will fail to find any valid paths.

---

# Scorer: Team Proximity

**`TeamProximityScorerSO`** is a scorer that encourages agents to hide near their allies, promoting group cohesion and squad-based behavior.

## How It Works

This scorer evaluates a candidate hiding spot based on its distance to the nearest friendly unit.

1.  **Find Nearest Ally**: It iterates through the list of allies provided in the `HidingContext` (sourced from the `EnemyHider`'s `allies` list) and finds the one closest to the candidate spot.
2.  **Compare to Optimal Distance**: It then compares this closest distance to the `Optimal Ally Distance` defined on the scorer asset.
3.  **Calculate Score**: The score is highest (1.0) when the spot is exactly the optimal distance from the nearest ally. The score decreases as the spot gets either closer to or farther away from the ally than this ideal distance.

If the agent has no allies, this scorer returns a neutral score of 0.5, having no effect on the decision. This logic encourages agents to "stick together" but not "stand on top of each other."

## Parameters

*   **Weight**: Determines how strongly the AI will prioritize staying near its teammates. A high weight will cause agents to form tight groups.
*   **Optimal Ally Distance**: This float value on the scorer asset defines the ideal distance (in meters) the agent should maintain from its closest ally.

## Use Cases

*   **Squad Behavior**: This is the primary use case. It makes soldier AI maintain formations and hide as a unit, rather than scattering across the map.
*   **Pack Animals**: Perfect for creating pack-based AI like wolves or raptors that hunt and move together.
*   **Support Roles**: Can be used to make support units (like medics or officers) stay close to the combat units they are supposed to be assisting.
*   **Discouraging Isolation**: Prevents a single AI from wandering off on its own, which can make the overall group feel more intelligent and coordinated.

## Performance and Dependencies

The performance of this scorer is **excellent**. For each candidate spot, it performs a series of fast distance calculations. Its impact on performance is negligible.

*   **Dependency**: This scorer's functionality is entirely dependent on the **`allies` list** on the `EnemyHider` component being correctly populated by your own controller scripts. If the list is empty, it will have no effect.

---

# Scorer: Threat Avoidance

**`ThreatScorerSO`** is an advanced scorer that makes AI aware of and avoid areas of known danger. It evaluates spots based on their proximity to a dynamic, global "threat map."

## How It Works

This scorer relies on an external system, the **`ThreatMapService`**, which is assumed to hold a list of active "threat points." These points could represent locations where a player was recently seen, where an explosion just occurred, or an area under suppressive fire.

For each candidate hiding spot, the scorer:

1.  **Finds the Closest Threat**: It iterates through all active points in the `ThreatMapService` and finds the one closest to the candidate spot.
2.  **Calculates Score Based on Distance**: The score is determined by how far the candidate spot is from this closest threat point.
    *   A spot right on top of a threat point gets a score of **0.0**.
    *   A spot that is farther away than the `Safe Distance` gets a score of **1.0**.
    *   The score scales linearly in between.

In short, this scorer makes AI want to move as far away from known danger zones as possible. If there are no active threats on the map, it returns a perfect score of 1.0.

## Parameters

*   **Weight**: Determines how strongly the AI will avoid known threats. For most AI, this should have a high weight to encourage self-preservation.
*   **Safe Distance**: A float value on the scorer asset that defines the radius of influence for a threat point. Once a spot is farther than this distance from a threat, the threat no longer affects its score.

## Use Cases

*   **Creating Persistent Awareness**: This is the primary use case. It allows AI to "remember" that a certain area is dangerous, even after the player has left. If a player shoots from a window, you can add a threat point there, and AI will avoid that window for a period of time.
*   **Responding to Grenades and Explosions**: When a grenade is thrown, you can add a temporary threat point at its location. This scorer will then naturally make all nearby AI flee from the blast radius.
*   **Suppressing Fire**: An AI under fire can add a threat point at the source of the shots, encouraging it and its allies to find cover that is not exposed to that direction or location.

## Performance and Dependencies

The performance of this scorer is very good. Its cost is proportional to the number of active threat points in the `ThreatMapService`, as it involves a series of distance calculations.

*   **Crucial Dependency**: This scorer is **completely dependent on the `ThreatMapService`**. It does nothing on its own. The service is automatically updated by the `EnemyHider` when it creates a `HidingContext`, but you can also add your own threats to it from other game systems (e.g., an explosion manager).

---

# Scorer: Visibility

**`VisibilityScorerSO`** is one of the most essential scorers in the system. It evaluates hiding spots with a simple binary question: "Can a player see this spot?" It heavily penalizes any spot that is not completely concealed from all players.

## How It Works

This scorer uses the `IVisibilityService` to determine if a candidate hiding spot is exposed. To make the check more robust and simulate the physical presence of an agent, it checks two separate points at the candidate location:

1.  A **high point** (simulating the agent's head).
2.  A **low point** (simulating the agent's center of mass).

It then asks the `IVisibilityService`, "Does any player have a direct, unobstructed line of sight to either of these points?"

The scoring is binary:

*   **If YES:** At least one player can see the spot. It is considered compromised and receives a score of **0.0**.
*   **If NO:** The spot is fully concealed from all players. It receives a perfect score of **1.0**.

This scorer does **not** care about the player's field of view (FOV). It only checks for physical line of sight. A spot directly behind a player is still considered "visible" by this scorer if there are no walls or obstacles in between. For FOV-based logic, see the `FOVScorerSO`.

## Parameters

*   **Weight**: Determines how much the AI prioritizes being physically hidden. For almost all hiding behaviors, this should have a very high weight. It's a core component of what it means "to hide."
*   **Player Eye Height** (from `HidingSettings`): This global setting is used to calculate the positions of the high and low points for the visibility check.

## Use Cases

*   **Core Hiding Mechanic**: This is a foundational scorer and should be included in nearly every `HidingSettings` configuration. It is the primary driver for making AI take cover behind walls, crates, and other obstacles.
*   **Breaking Line of Sight**: When an AI needs to escape, this scorer ensures it chooses a location that will actually break the player's line of sight.
*   **Working with Other Scorers**: It's often used as the primary "filter." Other scorers then rank the spots that this scorer has already deemed "safe." For example, you can combine it with the `DistanceScorerSO` to find a spot that is **both** hidden **and** far away.

## Performance and Dependencies

The performance of this scorer is entirely dependent on the implementation of the `IVisibilityService.AnyPlayerHasLineOfSight` method. This check almost always involves one or more `Physics.Raycast` calls.

*   The cost scales with the number of players and the number of candidate spots.
*   Because it performs at least two visibility checks per candidate, it is a moderately expensive scorer.
*   It has a hard dependency on a correctly configured **`IVisibilityService`**. Without it, this scorer cannot function.

---

# Scorer: Volumetric Cover

VolumetricCoverScorerSO scores candidate spots based on their concealment inside "soft cover" volumes like smoke clouds, dense fog, or magical darkness. This teaches the AI to use visual obstruction to its advantage.

## How It Works

This system is designed to complement the standard visibility system, which only understands solid objects. It uses a VolumetricCover component, which should be placed on objects like smoke cloud prefabs. These components register themselves with a VolumetricCoverRegistry.
The VolumetricCoverScorer evaluates a candidate spot that the normal visibility system considers "exposed." For each such spot, it performs its own line-of-sight check. It casts a ray from the player's eyes to the candidate spot. Then, it checks if that ray intersects with any active VolumetricCover collider.

* If the spot is exposed to the normal system, but the line of sight is blocked by a volumetric cover, it means the AI can use that smoke cloud to hide. The spot receives a high score (1.0).
* If the spot is exposed and not blocked by any soft cover, it is truly a bad spot and receives a low score (0.0).
* If the spot is already hidden behind a solid wall (according to the normal system), this scorer returns a neutral score (0.5), as it doesn't need to add its own input.

## Setup

* On your smoke grenade prefab, fog effect, etc., add a collider (e.g., SphereCollider or BoxCollider) that approximates its volume. Mark it as a Trigger.
* Add the new VolumetricCover component to this GameObject.
* Create an instance of the VolumetricCoverScorerSO asset.
* Add this scorer asset to the Scorers list in your HidingSettingsSO and give it a positive weight (e.g., 1.0 - 1.5).

## Use Cases

*  **Tactical Gameplay:** Allows AI to intelligently use smoke grenades (either its own or the player's) to break line of sight and maneuver.
*  **Environmental Storytelling:** You can fill a swamp with VolumetricCover fog volumes, and the AI will naturally understand that it can use the fog to hide and ambush the player.
*  **Magic Systems:** Perfect for spells that create fields of magical darkness or obscuring mist.

## Advanced Scorers (V2)


---

# Scorer: Aggressive Line of Sight

**`AggressiveLOSScorerSO`** is an offensive scorer designed for units that need to engage the enemy. Unlike standard hiding scorers that punish visibility, this scorer strictly rewards spots that have a clear line of fire to the target.

## How It Works

This scorer performs a raycast to determine if a shot is possible from the candidate position.

1.  **Target Acquisition:** It identifies the target position using the AI's memory (`playerLastKnownPosition`). If no memory exists, it defaults to the current position of the first available player.
2.  **Origin & Aim Point:** * **Origin:** The ray starts at the candidate position raised by the `enemyEyeHeight`.
    * **Aim Point:** The ray aims at the target's position. Depending on the settings, it aims either at the **Head** (full eye height) or the **Center Mass** (half eye height).
3.  **Raycast Check:** It casts a physics ray using the `OccluderMask` defined in the settings.
    * **Clear Path:** If the ray hits nothing, the path is clear. The scorer returns **1.0**.
    * **Blocked:** If the ray hits an obstacle, the scorer returns **0.0**.

This binary scoring (All or Nothing) ensures that "Attacker" roles strictly filter out spots where they would be staring at a wall.

## Parameters

* **Require Head Visibility**: 
    * **True**: The AI checks for line of sight specifically to the target's head (at `playerEyeHeight`). Useful for Snipers or units that need a perfect shot.
    * **False**: The AI checks for line of sight to the target's center/chest. Useful for general infantry or units with splash damage.

## Use Cases

* **Snipers / Turrets**: Use this with a high weight to ensure the AI only picks spots where it can shoot the player immediately.
* **"Stand and Fight"**: Use this on a profile where the AI decides to stop retreating and start engaging.
* **Support Units**: Ensures machine gunners move to positions where they can suppress the enemy.

## Performance

**Moderate.** This scorer performs one `Physics.Raycast` for every candidate spot generated. While not overly expensive, it is heavier than simple distance checks.

---

# Scorer: Audio Stimulus

**`AudioStimulusScorerSO`** is a strategic scorer that influences the AI to investigate or move toward interesting events (Stimuli) in the world, such as gunshots, explosions, or footsteps.

## How It Works

This scorer connects the hiding system to a global event system (`StimulusRegistry`).

1.  **Fetch Stimuli:** It retrieves a list of recent events from the `StimulusRegistry`.
2.  **Filter:** It ignores any stimuli that are "stale" (older than 5 seconds) or outside the agent's `Hearing Range`.
3.  **Evaluate:** For the candidate spot, it calculates the distance to the relevant sound.
4.  **Score:**
    * It calculates a score based on proximity: `1.0 - (Distance / HearingRange)`.
    * Closer spots get higher scores, effectively pulling the agent toward the source of the noise.
    * It returns the highest score found among all valid stimuli.

## Parameters

* **Hearing Range**: The maximum distance (in meters) at which the agent can "hear" or care about a stimulus.

## Use Cases

* **"Third Partying"**: In a battle royale or free-for-all scenario, this draws AI agents toward ongoing firefights.
* **Investigating**: If a player knocks over a physics object, this scorer can override standard cover logic to make the AI move toward the noise source to investigate.

## Performance and Dependencies

* **Thread Safety:** **Main Thread Only**. It accesses the static `StimulusRegistry` and `Time.time`, which are generally not safe or accessible within Burst jobs.
* **Requirement:** Requires an external system populating `StimulusRegistry.RecentStimuli`.

---

# Scorer: Material Thickness (Ballistics)

**`BulletPenetrationScorerSO`** is a high-fidelity "AAA" scorer that evaluates the physical thickness of the cover object protecting the agent. It penalizes thin cover (like plywood fences, sheet metal, or bushes) that bullets would likely penetrate, ensuring the AI seeks hard cover like concrete or thick walls.

## How It Works

This scorer performs a ballistics simulation using raycasts to approximate object volume.

1.  **Line of Fire Check:** It establishes a vector from the **Threat** (Player) to the **Candidate Spot**.
2.  **Entry & Exit Calculation:** It performs a `Physics.RaycastAll` along this vector to find all intersection points with the cover object.
3.  **Thickness Measurement:** It sorts the hits by distance to identify the "Entry" point (front of the wall) and the "Exit" point (back of the wall). It calculates the distance between these two points.
4.  **Scoring:**
    * If the calculated thickness is **less** than `Min Safe Thickness`, the spot is deemed unsafe and receives the `Thin Cover Penalty`.
    * If the thickness meets or exceeds the threshold, it returns a perfect score of **1.0**.

## Parameters

* **Min Safe Thickness**: The minimum thickness (in meters) required for an object to be considered "safe" (e.g., 0.5 for 50cm of concrete).
* **Thin Cover Penalty**: The score multiplier applied to thin cover (e.g., 0.1). A low value effectively rejects thin objects unless no other options exist.

## Use Cases

* **Destructible Environments**: In games where wood or thin metal can be shot through.
* **Realistic Shooters**: Ensures AI prefers engine blocks or brick walls over wooden fences.
* **Survival**: Prevents AI from hiding behind foliage or chain-link fences that block vision but not bullets.

## Performance

**Heavy.** This scorer uses `Physics.RaycastAll` and array sorting for every candidate check. It is computationally expensive and should be used judiciously, perhaps only when the AI is under active fire.

---

# Scorer: Casualty Aversion

**`CasualtyAversionScorerSO`** is a high-level survival scorer that allows the AI to "learn" from the battlefield. It penalizes hiding spots that are near locations where allies have recently died, simulating the realization that an area is "zeroed-in" or compromised.

## How It Works

This scorer acts as a dynamic "Fear Map" generator.

1.  **Fetch Data:** It retrieves a list of recent death locations from the global `CasualtyRegistry`.
2.  **Distance Check:** For every candidate spot, it checks the distance to the nearest known casualty.
3.  **Score:**
    * **1.0 (Safe):** If the spot is outside the `Fear Radius` of all dead bodies.
    * **Gradient Penalty:** If the spot is inside the radius, the score drops linearly.
    * **0.0 (Dangerous):** If the spot is exactly where an ally died.

## Parameters

* **Fear Radius**: The radius (in meters) around a corpse that is considered "cursed" or dangerous.

## Use Cases

* **Anti-Lemming Behavior**: Prevents a line of AI agents from running to the exact same cover point one by one and getting shot by the same sniper.
* **Dynamic Flanking**: As direct approaches become littered with casualties, the "negative score" pushes the AI naturally toward flanking routes that haven't been tried yet.

## Performance and Dependencies

* **Thread Safety:** **Main Thread Only**. Accesses the `CasualtyRegistry`.
* **Cost:** Low. Uses simple distance-squared checks against a usually small list of recent deaths.

---

# Scorer: Cover Cluster (Density)

**`CoverClusterScorerSO`** evaluates the immediate environment around a candidate spot to determine "Cover Density." It prefers areas rich in obstacles (junkyards, forests, urban debris) over isolated cover (a single rock in an open field). This gives the AI backup options if their primary spot is compromised.

## How It Works

1.  **Proximity Scan:** It performs a `Physics.OverlapSphere` check around the candidate position using the defined `Check Radius`.
2.  **Object Counting:** It counts how many valid occluders (walls, crates, trees) are found in this radius.
3.  **Density Evaluation:**
    * If the count is **<= 1** (implying only the cover itself or the floor is detected), it returns a score of **0.0** (Isolated).
    * It scales the score linearly based on `Ideal Cover Count`. If the count meets or exceeds this ideal, it returns **1.0**.

## Parameters

* **Check Radius**: The radius in meters to scan for additional cover objects.
* **Ideal Cover Count**: The number of nearby objects required to achieve a maximum score.

## Use Cases

* **Tactical Flexibility**: Ensures the AI doesn't trap itself behind a "Lonely Rock" where it can be easily flanked with no escape.
* **Urban Combat**: Draws AI towards piles of rubble or vehicle graveyards.
* **Forest Encounters**: Encourages AI to move deeper into the treeline rather than staying at the edge.

## Performance

**Moderate.** It relies on `Physics.OverlapSphereNonAlloc`, which is relatively efficient but involves checking all colliders in a small radius.

---

# Scorer: Escape Route

**`EscapeRouteScorerSO`** is a survival scorer that ensures the agent doesn't corner themselves. It evaluates whether a hiding spot offers a valid path for further retreat if the situation worsens.

## How It Works

This scorer tests the "navigability" of the terrain *behind* the cover.

1.  **Determine Threat:** Calculates the average position of all known players to determine the "Threat Direction."
2.  **NavMesh Raycast:** It casts a ray on the Navigation Mesh starting from the candidate spot and moving **away** from the threat.
3.  **Analyze Hit:**
    * **Edge Hit:** If the ray hits a NavMesh edge (a wall, a cliff, the map boundary), it means retreat is blocked.
    * **No Hit:** If the ray travels the full `Min Escape Distance` without hitting an edge, the path is clear.
4.  **Score:**
    * **1.0:** Full escape route available.
    * **0.0 - 0.9:** Scaled based on how far the agent can retreat before hitting a wall. If the distance is very short (<1m), it returns 0.0.

## Parameters

* **Min Escape Distance**: How far (in meters) the agent needs to be able to run backwards for the spot to be considered safe.
* **Escape Cone Angle**: (Internal logic) Defines the direction away from the enemy.

## Use Cases

* **Fluid Combat**: Encourages AI to pick "open" cover (like a tree in a field) over "closed" cover (like the corner of a dead-end alley).
* **Hit and Run**: Essential for skirmisher units that need to fire a few shots and then immediately fall back.

## Performance and Dependencies

* **Thread Safety:** **Main Thread Only**. Uses `UnityEngine.AI.NavMesh.Raycast`.
* **Cost:** Low to Moderate. NavMesh raycasts are generally cheaper than Physics raycasts but still require main thread access.

---

# Scorer: Exposure Volume

**`ExposureVolumeScorerSO`** calculates how "exposed" a candidate spot is to the open world. Unlike visibility checks (which check against specific enemies), this checks against empty space. It prevents the AI from choosing spots that are technically hidden from the current enemy but are otherwise wide open (e.g., the middle of a courtyard).

## How It Works

This scorer creates a 360-degree "safety profile" of the spot.

1.  **Radial Sampling:** It casts a specified number of rays (`Samples`) in a circle around the candidate spot at waist height.
2.  **Open Space Detection:** For each ray, it checks if it hits any geometry within `Check Distance`.
    * **Hit:** The direction is "Closed/Safe."
    * **No Hit:** The direction is "Open/Exposed."
3.  **Ratio Calculation:** It calculates the ratio of Open rays to Total rays.
    * A spot in an open field (0 hits) gets a high exposure ratio -> **Low Score**.
    * A spot in a tight alley (many hits) gets a low exposure ratio -> **High Score**.

## Parameters

* **Samples**: The number of rays to cast (e.g., 8 or 16). Higher values are more accurate but more expensive.
* **Check Distance**: How far the ray must travel without hitting anything to be considered "Open."

## Use Cases

* **General Survival**: The most robust "default" behavior for avoiding open areas.
* **Corridors vs. Halls**: Biases the AI towards tighter spaces where they are less likely to be sniped from unknown angles.
* **Avoiding "Skylining"**: Prevents AI from standing on top of ridges or hills where they are visible against the sky.

## Performance

**Scalable.** The cost is directly proportional to the `Samples` parameter. 8 samples is usually sufficient for good results without heavy performance impact.

---

# Scorer: Fatal Funnel (Doorway Avoidance)

**`FatalFunnelScorerSO`** is a tactical survival scorer designed to identify and penalize choke points. It detects if a candidate spot is located in a narrow corridor, doorway, or bridge—areas often referred to as "Fatal Funnels" in tactical doctrine.

## How It Works

This scorer measures the lateral (side-to-side) space available at the candidate position.

1.  **Orientation:** It determines the "Right" vector relative to the cover normal (or the agent's facing direction).
2.  **Width Scan:** It casts two Physics Raycasts: one Left and one Right from the candidate spot.
3.  **Measure:** It sums the distance to the nearest obstacle on both sides.
4.  **Score:**
    * **1.0 (Safe):** If the total width is greater than `Min Corridor Width`.
    * **Penalty:** If the total width is less than the minimum, it returns the `Choke Point Penalty` (default 0.0).

## Parameters

* **Min Corridor Width**: The minimum width (in meters) required for a space to be considered safe/maneuverable.
* **Choke Point Penalty**: The score assigned to a narrow spot (0.0 = Reject, 1.0 = Ignore).

## Use Cases

* **Doorway Safety**: Stops AI from taking cover *inside* a door frame where they have no room to dodge or strafe.
* **Hallway Awareness**: Discourages stopping in the middle of narrow bridges or catwalks.

## Performance and Dependencies

* **Thread Safety:** **Main Thread Only**. Uses Physics Raycasts.
* **Cost:** Moderate. Two raycasts per candidate.

---

# Scorer: High Ground

**`HighGroundScorerSO`** is a tactical scorer that evaluates the verticality of a hiding spot relative to the target. It creates a behavior where the AI naturally seeks elevation advantages, adhering to the "High Ground" tactical doctrine.

## How It Works

The scorer compares the Y-coordinate (height) of the candidate spot against the target's Y-coordinate.

1.  **Elevation Calculation:** It calculates `Difference = Candidate.y - Target.y`.
2.  **Above Target:** If the difference is positive (AI is higher), the score scales linearly from **0.5 to 1.0**.
    * A difference of 0 meters gives a score of 0.5.
    * A difference equal to or greater than `Ideal Height Advantage` gives a score of 1.0.
3.  **Below Target:** If the difference is negative or zero (AI is lower):
    * If **Penalize Low Ground** is true: The score scales down from **0.5 to 0.0** based on how deep below the target the spot is.
    * If false: It returns a neutral score of 0.5.

## Parameters

* **Ideal Height Advantage**: The height difference (in meters) required to achieve a perfect score. For example, if set to `4.0`, a spot 4 meters above the player gets the maximum bonus.
* **Penalize Low Ground**: If checked, positions significantly lower than the player will be actively discouraged (receiving low scores). If unchecked, low ground is treated as neutral.

## Use Cases

* **King of the Hill**: AI will fight to reach the top of a structure or hill.
* **Grenadiers**: Units with lobbed projectiles benefit from height; this scorer guides them to balconies or rooftops.
* **Snipers**: Gives snipers a strong preference for towers and upper-story windows.

## Performance

**Very Fast.** This scorer uses simple arithmetic comparisons. It has negligible performance cost.

---

# Scorer: Light Probe (Shadows)

**`LightProbeScorerSO`** is a stealth-oriented scorer that leverages Unity's baked or dynamic Global Illumination (GI) data. It allows agents to detect and prioritize dark areas, such as shadows cast by static geometry.

## How It Works

This scorer queries the scene's lighting data directly.

1.  **Probe Query:** It calls `LightProbes.GetInterpolatedProbe` at the candidate position. This returns the lighting information (Spherical Harmonics) for that specific point in space.
2.  **Luminance Calculation:** It estimates the average brightness (Luminance) from the probe data.
3.  **Score:**
    * **1.0 (Stealthy):** If the brightness is 0 (Pitch Black).
    * **0.0 (Exposed):** If the brightness exceeds the `Darkness Threshold`.
    * **Gradient:** Scores linearly between 0 and the threshold.

## Parameters

* **Darkness Threshold**: The brightness value (approx 0.0 to 1.0+) above which a spot is considered "too bright" and receives 0 score.

## Use Cases

* **Stealth Games**: AI can hide in the shadows of buildings or trees.
* **Night Missions**: AI will stick to unlit alleyways rather than walking under streetlights.

## Performance and Dependencies

* **Thread Safety:** **Main Thread Only**. `LightProbes` API is not thread-safe.
* **Cost:** Low. Interpolating a light probe is very fast compared to raycasting.

---

# Scorer: Line of Fire Safety

**`LineOfFireScorerSO`** is a squad-coordination scorer designed to prevent friendly fire incidents. It ensures that an AI agent does not choose a hiding spot or position that blocks the firing line of a teammate engaging a target.

## How It Works

This scorer acts as a **Binary Disqualifier**. It does not grade spots on a curve; a spot is either safe (1.0) or obstructing fire (0.0).

The logic follows these steps for every candidate spot:

1.  **Identify the Target:** The system determines the focal point of the squad's attention. This is typically the `playerLastKnownPosition`. If that is unavailable, it defaults to the current position of the nearest player.
2.  **Analyze Allies:** The scorer iterates through all known allies (excluding the agent itself).
3.  **Project Fire Tunnel:** For each ally, it mathematically constructs a line segment starting from the ally's eye position and ending at the target's center.
4.  **Check Obstruction:** It calculates the shortest distance from the candidate spot to this line segment.
    * If the distance is **less than** the `Safety Radius`, the spot is considered to be "in the crossfire."
    * The scorer immediately returns **0.0**, effectively disqualifying the spot (depending on the scorer's weight).
5.  **Pass:** If the candidate spot is outside the safety radius of all ally fire lines, it returns **1.0**.

## Parameters

* **Safety Radius**: A float value that defines the thickness of the "fire tube." A larger radius ensures the agent gives teammates a wider berth, while a smaller radius allows for tighter formations but increases the risk of clipping.

## Use Cases

* **Corridor Combat**: Prevents agents from clustering in a single line of sight within narrow hallways.
* **Coordinated Flanking**: Ensures that while one unit suppresses the player, the flanking unit moves around the fire, not through it.
* **Heavy Weapons Support**: Essential when one unit (e.g., a machine gunner) has a fixed lane of fire that must remain clear.

## Performance and Dependencies

* **Complexity:** $O(N)$ where $N$ is the number of allies.
* **Cost:** Low. The calculation uses simple vector dot products to determine the distance to a line segment. It does not perform physics raycasts.
* **Requirement:** The `HidingContext` must have the `allies` list populated, and there must be a valid target (`playerLastKnownPosition` or valid `players` list).

---

# Scorer: Muzzle Discipline

**`MuzzleDisciplineScorerSO`** is a tactical movement scorer that simulates professional firearm safety rules (specifically "do not cover anything you are not willing to destroy"). It ensures agents do not cross directly in front of a teammate's weapon barrel, regardless of whether that teammate is currently firing at a target.

## How It Works

Unlike the `LineOfFireScorer` (which cares about a specific target), `MuzzleDisciplineScorer` cares about the **direction the ally is facing**. It projects a "danger cylinder" extending forward from every ally.

The logic follows these steps:

1.  **Analyze Allies:** Iterate through all squad members.
2.  **Project Forward Vector:** Retrieve the ally's forward directional vector.
3.  **Cylinder Check:** The scorer calculates the position of the candidate spot relative to the ally. It checks two conditions:
    * **Depth:** Is the spot in front of the ally (positive dot product) and within the defined `Danger Distance`?
    * **Width:** Is the perpendicular distance from the spot to the ally's forward line less than the `Danger Radius`?
    * *Note:* This calculation flattens the Y-axis, treating the check as 2D (top-down) to ensure robustness on slopes.
4.  **Result:**
    * If **both** conditions are true, the agent is standing in front of the ally's gun. The scorer returns **0.0**.
    * Otherwise, it returns **1.0**.

## Parameters

* **Danger Distance**: How far forward (in meters) the "danger zone" extends from an ally. Beyond this distance, the scorer ignores the ally's facing direction.
* **Danger Radius**: The width (radius) of the cylinder extending from the ally.

## Key Differences: Line of Fire vs. Muzzle Discipline

| Feature | Line of Fire Scorer | Muzzle Discipline Scorer |
| :--- | :--- | :--- |
| **Reference** | Line from Ally to **Enemy** | Line from Ally to **Forward Direction** |
| **Purpose** | Prevent blocking active shooting | Prevent flagging/crossing lines during movement |
| **Context** | Best during active combat | Best during patrol, searching, or moving formations |

## Use Cases

* **Tactical Formations**: Keeps agents in a proper wedge or line formation while moving, preventing them from stepping on each other's toes.
* **CQB / Room Clearing**: Ensures that when a team stacks up or enters a room, the rear agents do not walk in front of the point man.
* **Non-Combat Movement**: Makes the AI look professional and trained by respecting personal space and weapon orientation even when no enemy is visible.

## Performance and Dependencies

* **Burst Compatible:** Yes. This scorer implements `IMultiThreadedScorer`, making it safe and highly efficient for use in the Asynchronous/Burst job system.
* **Cost:** Extremely Low. Uses simple vector math.
* **Requirement:** Requires the `allies` list in `HidingContext` to be populated.

---

# Scorer: Player Gaze

**`PlayerGazeScorerSO`** is a visibility scorer that specifically avoids the player's direct focus. While standard visibility checks determines if the player *can* see the agent, this scorer determines if the player is *currently looking* at the spot.

## How It Works

This scorer performs a vector analysis of the player's orientation.

1.  **Vector Calculation:** It calculates the vector from the player's eyes to the candidate spot.
2.  **Angle Check:** It compares this vector with the player's `Transform.forward` vector (their gaze).
3.  **Score:**
    * **Penalty:** If the angle is smaller than `Gaze Cone Angle` (meaning the player is looking directly at the spot).
    * **1.0:** If the spot is in the player's peripheral vision or behind them.

## Parameters

* **Gaze Cone Angle**: The angle (in degrees) representing the player's foveal (focused) vision. Usually narrow (e.g., 15 degrees).
* **Penalty Strength**: How strictly to avoid the gaze. 1.0 means avoid completely; 0.5 means it's a soft preference.

## Use Cases

* **Sniper Avoidance**: If the player is aiming down a hallway, the AI will refuse to step into that hallway.
* **Sneaking**: Encourages AI to move only when the player looks away.

## Performance and Dependencies

* **Thread Safety:** **Main Thread Only**.
* **Cost:** Very Low. Simple vector math.

---

# Scorer: Push Forward

**`PushForwardScorerSO`** is a movement-drive scorer that incentivizes the AI to close the distance to the target. It creates "Rusher" or "Aggressive" behaviors by rewarding spots that physically move the agent closer to the enemy.

## How It Works

This scorer measures the distance gain achieved by moving to a candidate spot.

1.  **Distance Comparison:** It calculates two distances:
    * **Current Distance:** From the Agent's current position to the Target.
    * **Candidate Distance:** From the Candidate spot to the Target.
2.  **Evaluation:**
    * **Gaining Ground:** If `Candidate Distance < Current Distance`, the spot is closer. The score starts at **0.5** and increases based on how much distance is closed (up to a max of ~5 meters for a full score).
    * **Retreating/Static:** If `Candidate Distance >= Current Distance`, the spot is further away or static. The scorer returns **0.0**.

This effectively filters out any "retreating" options and prioritizes the spots that offer the most forward progress.

## Parameters

* This scorer currently has no exposed parameters. It uses an internal constant (approx. 5 meters) to normalize the "distance gained" score.

## Use Cases

* **Melee Units**: Essential for zombies or sword-wielders to force them to constantly close the gap while still using cover (if combined with other scorers).
* **Shotgunners**: Drives units with short-range weapons to get into effective range.
* **Flanking**: When combined with a flank provider, this ensures the flank maneuver tightens the noose rather than drifting away.

## Performance

**Fast.** It relies on standard `Vector3.Distance` calculations.

---

# Scorer: Rear Attack Bonus

**`RearAttackScorerSO`** is a positional scorer that evaluates the relative orientation of the candidate spot to the target. It heavily rewards positions located behind the target's back, facilitating stealth, backstabs, or flanking maneuvers.

## How It Works

This scorer uses vector mathematics (Dot Product) to determine the angle of approach.

1.  **Vector Calculation:** It calculates the direction vector from the **Target** to the **Candidate Spot**.
2.  **Facing Check:** It compares this direction against the **Target's Forward Vector**.
3.  **Dot Product Scoring:**
    * **In Front:** If the spot is directly in front of the target (Target is looking at it), the Dot Product is 1.0. This converts to a score of **0.0**.
    * **Behind:** If the spot is directly behind the target (Target is looking away), the Dot Product is -1.0. This converts to a score of **1.0**.
    * **Side:** Positions directly to the side receive a neutral score around **0.5**.

## Parameters

* This scorer relies purely on relative geometry and has no tweakable parameters.

## Use Cases

* **Stealth AI**: Ideal for "Spy" or "Assassin" classes that need to stay out of the player's cone of vision.
* **Surrounding**: Encourages a squad to fan out and wrap around a target, as spots behind the player become mathematically more valuable than spots in front.
* **Critical Hits**: If your game has a damage bonus for back attacks, this scorer aligns the AI behavior with that mechanic.

## Performance

**Very Fast.** Uses efficient vector math (`Vector3.Dot`). It is extremely lightweight.

---

# Scorer: Repetition Penalty

**`RepetitionPenaltyScorerSO`** is a utility scorer that forces the AI to "rotate" positions. It penalizes candidate spots that are geographically close to where the agent has hidden recently.

## How It Works

This scorer accesses the agent's short-term memory.

1.  **Fetch History:** It retrieves the `PositionHistory` queue from the `TacticalAgent`.
2.  **Comparison:** It compares the candidate spot's position against every position in the history.
3.  **Score:**
    * **0.0 (Reject):** If the candidate is within `Memory Radius` of *any* previous spot.
    * **1.0 (Accept):** If the spot is fresh territory.

## Parameters

* **Memory Radius**: The radius (in meters) around previous spots that is considered "used ground."

## Use Cases

* **Whac-A-Mole**: Prevents the AI from popping up at the exact same corner over and over again.
* **Evasive Tactics**: Forces the AI to constantly relocate after firing, making them a harder target.

## Performance and Dependencies

* **Thread Safety:** **Main Thread Only**. Accesses the `TacticalAgent` instance.
* **Cost:** Very Low. Simple distance checks against a small history queue (usually size 3-5).

---

# Scorer: Sector Watch (Flank Security)

**`SectorWatchScorerSO`** is a squad-coordination scorer designed to maximize the team's situational awareness. It encourages individual agents to face directions (sectors) that are not currently being watched by their teammates, effectively automating "Rear Security" or "Flank Watch" behaviors.

## How It Works

This scorer operates by analyzing the "eyes" of the entire squad to find blind spots.

1.  **Divide the View:** It conceptually divides the 360-degree view around the squad into a specific number of slices or "sectors" (defined by the `sectors` parameter).
2.  **Analyze Allies:** It iterates through all teammates and calculates which sector they are currently facing based on their forward direction. It builds a "histogram" of coverage (e.g., "Sector 1 has 2 watchers, Sector 2 has 0 watchers").
3.  **Evaluate Candidate:** For the candidate hiding spot, it determines the direction the agent *would* face if they took that spot.
    * *Primary Check:* If the spot has a cover normal (e.g., a wall), it assumes the agent will look outward away from the wall.
    * *Fallback:* If no cover normal exists, it assumes the agent will look outward away from the center of the squad's formation.
4.  **Score:**
    * **1.0 (High Reward):** If the candidate spot faces a "Blind Spot" (a sector with 0 allies watching it).
    * **0.5 (Neutral):** If the sector is already watched by exactly one ally.
    * **0.0 (Penalty):** If the sector is crowded (watched by 2 or more allies), the spot is considered redundant.

## Parameters

* **Sectors**: The integer number of slices to divide the 360-degree view into. A value of **8** (default) creates 45-degree sectors, which is standard for tactical games.

## Use Cases

* **Perimeter Defense**: When a squad holds a room, this ensures they spread out to watch all doors and windows rather than all staring at the same entrance.
* **Rear Security**: If the whole squad is moving North, this scorer will highly reward a spot that allows an agent to look South (Rear), protecting the team's back.

## Performance and Dependencies

* **Burst Compatible:** Yes. Implements `IMultiThreadedScorer`.
* **Complexity:** $O(N)$ where $N$ is the number of allies.
* **Cost:** Low. Uses basic trigonometry (`Vector3.SignedAngle`) and array lookups.

---

# Scorer: Skylining (Silhouette)

**`SkyliningScorerSO`** is a visual camouflage scorer. It detects "Skylining"—a tactical error where a soldier stands on a ridge or roof and is silhouetted against the bright sky, making them an easy target.

## How It Works

This scorer checks the *background* of the candidate spot from the enemy's perspective.

1.  **Reverse Raycast:** It calculates the direction from the Enemy -> Candidate Spot.
2.  **Background Check:** It casts a ray starting *from* the candidate spot and continuing along that direction (away from the enemy).
3.  **Analyze Hit:**
    * **Hit:** If the ray hits geometry (a wall, a mountain, a tree), it means the agent has a "Backstop." They will blend in with the background. (Score 1.0).
    * **No Hit:** If the ray hits nothing, it means the background is the Skybox. The agent is skylined. (Score = `Skylining Penalty`).

## Parameters

* **Background Check Distance**: How far behind the agent to check for geometry (e.g., 20m).
* **Skylining Penalty**: The score received if skylined (0.0 = Reject, 1.0 = Ignore).

## Use Cases

* **Ridge Safety**: Prevents AI from standing on the very top of a hill; encourages them to move slightly down the reverse slope (Military Crest).
* **Rooftops**: AI will avoid standing on the very edge of a roof where they stick out against the sky.

## Performance and Dependencies

* **Thread Safety:** **Main Thread Only**. Uses Physics Raycasts.
* **Cost:** Moderate. One raycast per candidate.

---

# Scorer: Smart Path Safety (Detour Aware)

**`SmartPathSafetyScorerSO`** is a highly advanced pathfinding scorer. Unlike basic path checks that simply reject unsafe paths, this scorer actively tries to find a "Detour" or "Flank" route to the destination if the direct path is dangerous.

## How It Works

This is a multi-stage path analyzer:

1.  **Direct Check:** It calculates a NavMesh path to the candidate spot. It samples points along the path and checks visibility to the player.
    * If safe, it returns the score immediately.
2.  **Detour Calculation:** If the direct path is exposed, it calculates a heuristic "Via Point" to the side (flank) of the danger vector.
3.  **Two-Leg Validation:** It calculates two separate paths:
    * **Leg 1:** Agent -> Detour Point.
    * **Leg 2:** Detour Point -> Candidate Spot.
4.  **Score:**
    * If *both* legs are safe, it returns a passing score (slightly penalized to account for the longer travel time).
    * If either leg is unsafe, the spot is disqualified.

## Parameters

* **Visibility Threshold**: The percentage of path samples (0.0 to 1.0) allowed to be visible before the path is deemed unsafe.
* **Flank Offset Distance**: How far sideways (in meters) to plot the detour point.
* **Penalty Exponent**: Controls the curve of the safety penalty.

## Use Cases

* **Smarter Movement**: Allows AI to cross a dangerous street by running *down* the block and crossing at a safe point, rather than running straight across and getting shot.
* **Flanking**: Naturally produces flanking behaviors as the AI seeks safe routes around the player's line of fire.

## Performance and Dependencies

* **Thread Safety:** **Main Thread Only**. Heavily reliant on `NavMesh.CalculatePath` and `IVisibilityService`.
* **Cost:** **High**. This is an expensive scorer. It may perform multiple path calculations and dozens of visibility checks per candidate. Use sparingly or with lower candidate counts.

---

# Scorer: Squad Reservation

**`SquadReservationScorerSO`** is a critical coordination scorer that prevents multiple agents from trying to claim the exact same hiding spot. It acts as the bridge between the individual agent's search and the central `SquadCoordinator`.

## How It Works

This is a **Binary Disqualifier**. It does not output a gradient score; it either accepts a spot or strictly forbids it.

1.  **Check Coordinator:** It first verifies that a `SquadCoordinator` is assigned and accessible.
2.  **Query Reservation:** It asks the coordinator: *"Is this specific position already reserved by someone else in my squad?"*.
3.  **Result:**
    * **Negative Infinity:** If the spot is reserved, it returns `float.NegativeInfinity`. This creates an immediate "Veto," ensuring this spot is removed from the candidate list regardless of how good its other scores are.
    * **1.0:** If the spot is free, it returns a passing score.

## Parameters

* *None.* This scorer relies entirely on the external logic of the `SquadCoordinator` system.

## Use Cases

* **Stacking Prevention**: Essential for any game with multiple AI agents. Without this, the "best" cover point (e.g., the only concrete wall) would attract every single AI unit, causing them to clip inside each other.

## Performance and Dependencies

* **Thread Safety:** **Main Thread Only**. This scorer is **not** Burst compatible because it must access the `SquadCoordinator` class (a standard C# class) to check dynamic dictionaries and lists.
* **Requirement:** The `HidingContext` must have a valid reference to `squadCoordinator` and `requestingAgent`.

---

# Scorer: Squad Separation

**`SquadSeparationScorerSO`** is a spatial scorer designed to maintain a minimum physical distance between squad members. While `TeamProximityScorer` pulls agents together to form a cohesive unit, `SquadSeparationScorer` pushes them apart locally to prevent overcrowding.

## How It Works

This scorer functions as a proximity filter.

1.  **Analyze Allies:** It iterates through all squad members in the `HidingContext`.
2.  **Distance Check:** It calculates the squared distance between the candidate spot and every ally's current position.
3.  **Score:**
    * **0.0 (Disqualified):** If *any* ally is closer than the defined `Min Separation`, the spot receives a 0 score. Note: Unlike Reservation (which checks *future* spots), this checks *current* positions.
    * **1.0 (Pass):** If all allies are outside the minimum separation radius.

## Parameters

* **Min Separation**: The minimum distance (in meters) allowed between agents. Default is **3.0f**.

## Use Cases

* **Explosive Safety**: Prevents the squad from clustering so tightly that a single grenade could kill everyone.
* **Pathfinding Clarity**: Keeping agents 3+ meters apart ensures their NavMeshAgents don't fight for the same small patch of navigation mesh.

## Performance and Dependencies

* **Burst Compatible:** Yes. Implements `IMultiThreadedScorer`.
* **Cost:** Extremely low. Uses simple distance-squared checks.

---

# Scorer: Stalemate Breaker

**`StalemateBreakerScorerSO`** is a behavioral scorer designed to prevent "camping." It detects if an agent has been sitting in one spot for too long and dynamically increases the value of flanking positions to force movement.

## How It Works

This scorer introduces the concept of "Boredom" to the AI.

1.  **Check Boredom:** It checks the `TimeInCover` property of the agent.
    * If the time is less than `Boredom Threshold`, the agent is "content," and the scorer returns a neutral **0.5**.
2.  **Calculate Flank Urgency:** If the agent is "bored" (time > threshold), the scorer aggressively seeks movement.
3.  **Geometric Analysis:** It compares the direction to the Enemy vs. the direction to the Candidate Spot.
    * It uses the **Dot Product** to determine the angle.
    * **High Reward:** Lateral movements (moving sideways relative to the enemy). This is a "Flank".
    * **Low Reward:** Moving directly forward (aggressive) or backward (retreat) is rewarded less than flanking in this specific scorer.
4.  **Scaling:** The score is multiplied by a `Boredom Factor`. The longer the agent sits, the higher the score for flanking becomes, eventually overriding safety concerns to force a move.

## Parameters

* **Boredom Threshold**: The time (in seconds) the agent must sit in cover before this scorer activates.
* **Flank Urgency**: A multiplier that determines how desperately the agent wants to flank once bored. Higher values create more aggressive, restless AI.

## Use Cases

* **Anti-Camping**: Prevents AI from finding one "perfect" spot and staying there forever, which is boring for the player.
* **Dynamic Flow**: Creates a rhythm to combat where AI takes cover, shoots for a while, and then naturally decides to rotate to a new angle.

## Performance and Dependencies

* **Thread Safety:** **Main Thread Only**. It relies on accessing the `TimeInCover` property from the `TacticalAgent` instance provided in the context.

---

# Scorer: Wall Hugging

**`WallHuggingScorerSO`** is a survival-focused scorer that strongly encourages the agent to stay physically close to geometry (walls, large obstacles). It combats "Open Field Syndrome," where an AI might hide in a technically valid spot that feels unnatural because it's floating in the middle of a room.

## How It Works

1.  **Geometry Search:** It performs an `OverlapSphere` check to find any colliders on the `Wall Mask` layers within the `Scan Radius`.
2.  **Nearest Point Calculation:** If colliders are found, it calculates the `ClosestPoint` on the collider's surface to the candidate spot.
3.  **Distance Scoring:**
    * **Touching Wall:** If the distance is near 0, the score is **1.0**.
    * **Far from Wall:** As the distance approaches `Scan Radius`, the score drops to **0.0**.
    * **No Wall:** If no walls are found within the radius, the score is **0.0**.

## Parameters

* **Scan Radius**: The maximum distance from a wall the agent is allowed to be to receive any score.
* **Wall Mask**: The LayerMask defining what counts as a "Wall" (usually Default, Static, or a specific Cover layer).

## Use Cases

* **Indoor Movement**: Keeps AI moving along the edges of corridors rather than the center.
* **Stealth**: Spies/Assassins look smarter when sticking to the shadows at the edge of a room.
* **Cover Readiness**: An agent hugging a wall is always closer to breaking line of sight than one standing 2 meters away from it.

## Performance

**Moderate.** Uses `OverlapSphere` followed by `ClosestPoint` calculations. It is generally efficient enough for standard usage.

---

# Scorer: Zone Control (LOS)

**`ZoneControlScorerSO`** is a strategic scorer designed for defensive or "Overwatch" roles. Unlike `ObjectiveProximityScorer` (which simply pulls the agent *physically close* to an objective), this scorer rewards positions that maintain a clear **Line of Sight (LOS)** to the objective, allowing the AI to guard it effectively from a distance.

## How It Works

This scorer evaluates the tactical value of a spot based on its ability to "see" a key location.

1.  **Identify Target:** It searches the `ObjectiveService` for a valid objective. (Currently, it defaults to the first active objective found, but supports ID filtering).
2.  **Distance Check:** It first verifies if the candidate spot is within the `Max Control Distance` of the objective. If the spot is too far away to effectively guard the point, it is disqualified (Score 0.0).
3.  **Visibility Check:** It performs a Physics Raycast from the candidate spot's eye position to the center of the objective.
4.  **Score:**
    * **1.0 (High Value):** If the raycast has a clear line of sight to the objective.
    * **0.0 (Disqualified):** If the view is blocked by a wall or obstacle.

## Parameters

* **Target Objective ID**: An integer ID used to filter which specific objective to watch (matching your `ObjectiveService` IDs).
* **Max Control Distance**: The maximum range (in meters) from which the AI is allowed to guard the point.

## Use Cases

* **King of the Hill**: AI defenders will find spots like balconies or windows that overlook the capture point, rather than standing directly inside the capture zone where they are vulnerable to grenades.
* **Sniper Overwatch**: Forces sniper units to find high-visibility lines of sight on key choke points.

## Performance and Dependencies

* **Thread Safety:** **Main Thread Only**. It relies on the `ObjectiveService`, which is likely not thread-safe.
* **Cost:** Moderate. Performs one Physics Raycast per candidate spot within range.
