# Feature Guide: EnemyHider Component

The EnemyHider component is the central brain and primary interface for the Tactical Cover & Retreat AI System. You attach this component directly to your AI agent's GameObject. It acts as a "facade," simplifying the complex process of finding cover into a set of easy-to-use commands and events.

## Why Use It?

The EnemyHider is the bridge between your AI's decision-making logic (like a Behavior Tree or State Machine) and the hiding system's core functionality. It manages the search process, handles asynchronous operations, and translates the final result into movement for your AI.

*  **Centralized Control:** Manages all settings, targets, and state for a single AI agent.
*  **Performance Options:** Choose between a high-performance, multi-threaded Asynchronous mode or a simple, easy-to-debug Synchronous mode.
*  **Event-Driven:** Provides UnityEvents to easily hook up animations, sound effects, or other gameplay logic without needing to write extra code.
*  **Extensible:** Can be linked with custom ICombatAction scripts to execute complex tactical maneuvers after finding cover, instead of just moving.

## Setup Guide

1. Select your AI agent's GameObject in the scene.
2. Click Add Component and search for EnemyHider. Add the script.
3. Drag your HidingSettingsSO asset into the Settings field. This asset acts as the "rulebook" for the AI's decisions.
4. Drag the NavMeshAgent component from your AI into the Agent field. The system will use this to move the AI.
5. `(Optional)` If you have a custom script that implements the ICombatAction interface, assign its GameObject to the Combat Action Game Object field.

## Inspector Parameters

### System Settings
*  **Execution Mode:**
**Asynchronous:** The recommended mode for best performance. It uses the Unity Job System and Burst Compiler to perform searches on background threads, preventing game freezes.
**Synchronous:** A simpler mode where the search happens on the main thread. Useful for debugging as the code flow is easier to follow, but may cause performance hitches with many agents or complex searches.

### Fallback Settings
*  **Allow Desperate Retreat:** If checked, the AI will perform a second, less strict search if the first one fails to find a perfectly safe path. This is crucial for preventing the AI from getting "stuck" and doing nothing when it's surrounded or in a very open area.

### Component References
*  **Settings:** The HidingSettingsSO asset that defines the AI's behavior. This is the most critical reference.
*  **Agent:** The NavMeshAgent component on this AI, used for pathfinding and movement.
*  **Combat Action Game Object:** An optional field for advanced users. Assign a GameObject that has a component implementing the ICombatAction interface to override the default movement behavior with your own custom logic (e.g., peek-and-shoot, suppressive fire).
*  **Players / Allies:** Lists for Transform components. These are primarily for quick testing in the editor. In a real game, you will likely set these lists at runtime using the public API.

## Events
*  **On Search Started:** A UnityEvent that fires the moment RetreatToHide() is called. Useful for triggering "taking cover!" voice lines or changing the AI's state to "retreating."
*  **On Search Success:** A UnityEvent<HidingSpot> that fires when a valid hiding spot is found. It passes the HidingSpot data, which you can use for custom logic.
*  **On Search Failed:** A UnityEvent that fires if no suitable hiding spot could be found, even after a desperate retreat. Useful for triggering a fallback behavior, like a last-stand fight.

## Public API for Programmers
The `EnemyHider` is controlled from your own AI scripts.

```CSharp
// In your AI's main controller script (e.g., EnemyFSM.cs)

using MaharajaStudio.HidingSystem;

public class MyAIController : MonoBehaviour
{
    private EnemyHider hider;
    public Transform player;

    void Start()
    {
        hider = GetComponent<EnemyHider>();
    }

    void Update()
    {
        // Your logic decides WHEN to hide.
        if (IsUnderFire() && !hider.IsSearching)
        {
            // Tell the hider who to hide from.
            hider.SetSinglePlayerTarget(player);

            // Command the hider to find a spot and move.
            hider.RetreatToHide();
        }
    }

    bool IsUnderFire() { /* ... your custom logic ... */ return true; }
}
```
*  **RetreatToHide():** The main function. Initiates the search for a hiding spot based on the current settings and targets.
*  **CancelSearch():** Immediately stops an ongoing Asynchronous search.
*  **SetPlayers(IReadOnlyList<Transform> playerList):** Sets the list of enemies to hide from.
*  **SetAllies(IReadOnlyList<Transform> allyList):** Sets the list of teammates for coordinated tactics.
*  **IsSearching (property):** A read-only boolean that is true while a search is in progress.