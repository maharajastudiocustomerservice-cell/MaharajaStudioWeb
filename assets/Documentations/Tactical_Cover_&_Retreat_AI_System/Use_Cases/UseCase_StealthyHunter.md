# Use Case: The Stealthy Hunter

This guide explains how to configure the Hide-And-Stealth-System to create a "Stealthy Hunter" or "Assassin" AI. This AI's goal is to get as close as possible to the player while remaining completely undetected.

## Behavior Goal

*   Prioritize remaining unseen above all else.
*   Actively try to get closer to the player, not farther away.
*   Use shadows, bushes, and other forms of concealment, not just hard cover.
*   Move with extreme caution, never breaking stealth.

---

## Setup

1.  Add the `EnemyHider` component to your AI GameObject.
2.  Create a new `HidingSettingsSO` asset and name it `StealthyHunter_Settings`.
3.  Assign this asset to the `Settings` field on the `EnemyHider` component.
4.  In your AI controller script, call `hider.RetreatToHide()` when the AI should reposition or advance on the player.

## `HidingSettings` Configuration

This advanced configuration uses specialized providers and a **negative weight** on the `DistanceScorer` to make the AI actively seek proximity while staying hidden.

### Providers

The providers should focus on finding non-obvious hiding spots that a stealthy character would use.

1.  **`ShadowProviderSO`**: Excellent for AI that can use darkness. This will make them find and stick to shadows.
2.  **`VoxelGridProviderSO`**: The perfect provider for finding spots inside "soft" cover like tall grass or thick bushes. This is a key part of the "hunter" feel.
3.  **`BehindObstacleProviderSO`**: A good fallback for finding standard hard cover spots.
4.  **`CurrentPositionProviderSO`**: Essential for stability, ensuring the AI doesn't abandon a great hiding spot.

### Scorers

The scorers are weighted to create an AI that is obsessed with stealth and proximity.

| Scorer                       | Weight | Reason                                                                                                                                                                                                   |
| ---------------------------- | :----: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`VisibilityScorerSO`**     | **1.0**  | **CRITICAL.** The AI must be physically concealed. This is non-negotiable for a stealth character.                                                                                                        |
| **`FOVScorerSO`**            | **1.0**  | **CRITICAL.** The AI must stay out of the player's direct vision cone. This is the essence of sneaking.                                                                                                    |
| **`PathSafetyScorerSO`**     | **1.0**  | **CRITICAL.** The path taken must be as concealed as the destination. The hunter cannot afford to be seen while moving into position.                                                                       |
| **`DistanceScorerSO`**       | **-1.0** | **CRITICAL (NEGATIVE WEIGHT).** This is the key to the "hunter" behavior. `DistanceScorer` normally rewards being far away. By giving it a *negative* weight, you penalize distance, which effectively **rewards proximity**. The AI will now actively seek out the closest safe hiding spot. |
| **`ReachabilityScorerSO`**   |  0.8   | **CRITICAL.** Because `VoxelGridProvider` can generate points inside walls, this scorer is essential to filter out all the spots the AI cannot physically reach.                                           |
| **`DefensivePositionScorerSO`** |  0.05   | **Recommended.** This provides stability. If the AI has found an excellent, hidden spot right next to the player, this encourages it to stay there and wait.                                            |

---

## How It Works Together

1.  When you call `RetreatToHide()`, the `ShadowProvider` and `VoxelGridProvider` find a unique set of hiding spots suitable for a stealthy character (shadows, bushes), supplemented by standard cover from `BehindObstacleProvider`.
2.  The three critical safety scorers (`Visibility`, `FOV`, and `PathSafety`) act as a hard filter. They ensure the AI will **only** consider spots that are completely hidden and have a safe path.
3.  The `ReachabilityScorer` provides another essential filter, throwing out any unreachable points found by the `VoxelGridProvider`.
4.  Now, the magic happens. From the remaining list of perfectly safe spots, the negatively weighted `DistanceScorer` takes over. Instead of choosing the farthest spot, it chooses the **closest** one.
5.  This results in an AI that relentlessly pushes forward, always trying to close the distance to the player, but only by moving from one perfectly concealed location to another. It will feel like a predator stalking its prey.