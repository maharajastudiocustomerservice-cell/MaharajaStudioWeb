# Use Case: The Cowardly AI

This guide explains how to configure the Hide-And-Stealth-System to create a "Cowardly" or "Skittish" AI. This type of AI's primary goal is to run away from threats and maximize its distance from players.

## Behavior Goal

*   When a threat appears, the AI should flee.
*   It should always try to find a hiding spot that is as far away as possible.
*   It doesn't need to be clever; its main instinct is self-preservation through distance.

---

## Setup

1.  Add the `EnemyHider` component to your AI GameObject.
2.  Create a new `HidingSettingsSO` asset and name it something like `CowardlyAI_Settings`.
3.  Assign this asset to the `Settings` field on the `EnemyHider` component.
4.  In your AI controller script, call `hider.RetreatToHide()` when the AI should flee.

## `HidingSettings` Configuration

This configuration will heavily reward distance and penalize proximity.

### Providers

The providers should generate a wide variety of potential points for the AI to run to.

1.  **`OppositePlayersProviderSO`**: This is the most important provider for this use case. It generates points in the direction *away* from the player, which is the core of the fleeing behavior.
2.  **`NavMeshRingProviderSO`**: This finds many reachable points around the AI at various distances. It ensures that even if there's no clear "away" direction, the AI still has plenty of places to run to.
3.  **`CurrentPositionProviderSO`**: Essential for stability. This prevents the AI from moving if it's already in a good, distant location.

### Scorers

The scorers are configured to overwhelmingly prioritize being far from the player.

| Scorer                       | Weight | Reason                                                                                                                              |
| ---------------------------- | :----: | ----------------------------------------------------------------------------------------------------------------------------------- |
| **`DistanceScorerSO`**       | **1.0**  | **CRITICAL.** This is the main driver of the cowardly behavior. A maximum weight ensures the AI will always choose the farthest spot. |
| **`ReachabilityScorerSO`**   |  0.8   | **CRITICAL.** This filters out any spots that are too far to reach, preventing the AI from getting stuck trying to run to an impossible location. |
| **`VisibilityScorerSO`**     |  0.5   | **Recommended.** The AI isn't a brilliant tactician, but it should still prefer a spot behind a wall over one in the open. This gives it a basic sense of cover. |
| **`DefensivePositionScorerSO`** |  0.05   | **Good for stability.** This gives a small bonus for staying put if the AI is already safe and far away, preventing it from fidgeting unnecessarily. |

---

## How It Works Together

1.  When your script calls `RetreatToHide()`, the `EnemyHider` kicks into action.
2.  The `OppositePlayersProvider` and `NavMeshRingProvider` generate a large number of potential "escape points".
3.  The `ReachabilityScorer` immediately disqualifies any points that are unreachable or too far away.
4.  The `DistanceScorer`, with its maximum weight, dominates the decision, finding the reachable spot that is farthest from the player.
5.  The `VisibilityScorer` acts as a tie-breaker, making the AI prefer a distant spot that is also behind cover.
6.  The `DefensivePositionScorer` ensures that if the AI is already far away and safe, it won't move unless it finds a spot that is significantly farther away.

This configuration creates a simple but very effective fleeing behavior. The AI will consistently try to create as much space as possible between itself and any threats.