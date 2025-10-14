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