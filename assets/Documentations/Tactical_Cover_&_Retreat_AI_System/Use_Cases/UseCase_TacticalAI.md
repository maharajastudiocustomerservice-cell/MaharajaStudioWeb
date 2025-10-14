# Use Case: The Tactical AI

This guide explains how to configure the Hide-And-Stealth-System to create a "Tactical" AI. This AI behaves like a trained soldier, prioritizing good cover, safe movement, and smart positioning over simply running away.

## Behavior Goal

*   The AI should prefer to hide behind solid objects.
*   It must avoid running through open areas where the player can see it.
*   It should be able to use pre-defined tactical positions in the level.
*   It should be "sticky" to good cover and not abandon it unless necessary.

---

## Setup

1.  Add the `EnemyHider` component to your AI GameObject. Make sure **Allow Desperate Retreat** is checked.
2.  Create a new `HidingSettingsSO` asset and name it `TacticalAI_Settings`.
3.  Assign this asset to the `Settings` field on the `EnemyHider` component.
4.  In your AI controller script, call `hider.RetreatToHide()` when the AI needs to find cover.

## `HidingSettings` Configuration

This configuration focuses on providers that find high-quality cover and scorers that evaluate safety and tactical advantage.

### Providers

The providers should focus on finding well-defined cover locations.

1.  **`BehindObstacleProviderSO`**: This is a core provider for this use case. It dynamically finds spots behind walls and other obstacles.
2.  **`DirectionalCoverNodeProviderSO`**: Use this if you have manually placed `CoverNode` objects in your scene. This allows the AI to use your pre-defined tactical points intelligently.
3.  **`CurrentPositionProviderSO`**: Absolutely essential for a tactical AI. It prevents the AI from abandoning good cover for a spot that isn't significantly better.

### Scorers

The scorers are balanced to reward safety and tactical awareness. The weights are critical.

| Scorer                       | Weight | Reason                                                                                                                                                              |
| ---------------------------- | :----: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`PathSafetyScorerSO`**     | **1.0**  | **CRITICAL.** A tactical AI must not run through the open. This heavily penalizes unsafe paths, forcing the AI to move from cover to cover. Max weight is recommended. |
| **`VisibilityScorerSO`**     | **1.0**  | **CRITICAL.** The entire point of cover is to be hidden. This ensures the destination is concealed. Max weight is recommended.                                        |
| **`DefensivePositionScorerSO`** |  0.1   | **CRITICAL.** This makes the AI "sticky." It will stay in its safe cover spot unless it's compromised. The `NegativeInfinity` penalty for being visible is key. |
| **`FOVScorerSO`**            |  0.7   | **Highly Recommended.** This makes the AI smarter by encouraging it to move to the player's flank or rear, outside their direct vision cone.                           |
| **`AmbushScorerSO`**         |  0.5   | **Optional, but powerful.** Add this to give your AI the ability to lie in wait and ambush the player. Creates very intelligent-seeming behavior. |
| **`ReachabilityScorerSO`**   |  0.5   | **Recommended.** Filters out spots that are too far away, keeping the AI engaged in the fight.      |
| **`DistanceScorerSO`**       |  0.2   | **Use with low weight.** A small weight here gives a gentle nudge for the AI to prefer farther cover spots, but it won't override the need for safety.  |

---

## How It Works Together

1.  When your script calls `RetreatToHide()`, the `BehindObstacleProvider` and `DirectionalCoverNodeProvider` find a list of high-quality cover positions.
2.  The `PathSafetyScorer` and `VisibilityScorer` act as hard filters. They ensure that any chosen spot **must** have a safe path and **must** be concealed.
3.  The `DefensivePositionScorer` is the next most important. If the AI is already in a good, safe spot, it gets a high score, making it very unlikely to move. If its cover is blown, this scorer returns negative infinity, forcing it to find a new spot.
4.  The remaining scorers (`FOV`, `Ambush`, `Distance`) then rank the handful of "safe" spots that are left, helping the AI pick the most tactically advantageous one.

This layered approach creates a robust and intelligent AI. It follows a clear hierarchy of needs: first **be safe**, then **stay safe**, and only then worry about finding a *tactically better* position.