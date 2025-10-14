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