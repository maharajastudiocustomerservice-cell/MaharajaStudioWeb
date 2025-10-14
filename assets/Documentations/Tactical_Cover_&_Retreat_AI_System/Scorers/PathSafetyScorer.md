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