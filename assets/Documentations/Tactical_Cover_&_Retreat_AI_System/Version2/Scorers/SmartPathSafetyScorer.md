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