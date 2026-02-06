# Provider: Choke Point Finder

**`ChokePointProviderSO`** is a tactical provider designed to identify constricted areas in the environment, such as hallways, bridges, doorways, or narrow alleys. It is particularly useful for setting up ambushes or identifying defensible bottlenecks where enemy movement is restricted.

## How It Works

This provider scans the local environment to find points where the geometry constricts the NavMesh on opposing sides.

1.  **Random Sampling:** It first generates random points on the NavMesh within the `Search Radius`.
2.  **Constriction Check:** For each valid point, it performs a "star pattern" raycast check:
    * It casts rays to the Left and Right (X-axis relative to world).
    * It casts rays Forward and Backward (Z-axis relative to world).
3.  **Validation:** A point is considered a "Choke Point" if it detects obstacles on *both* opposing sides (e.g., Left AND Right or Forward AND Back) within the defined `Max Passage Width`.
4.  **Cover Normal:** If a choke point is found, the cover normal is set to `Vector3.up` (or generic), as the tactical value comes from the constriction itself rather than a specific cover face.

## Parameters

* **Max Passage Width**: The maximum width of a passage to be considered a choke point. Passages wider than this value will be ignored.
* **Wall Scan Range**: The distance rays are cast to detect walls, effectively derived from the passage width limit.

## Use Cases

* **Ambushes**: AI can identify choke points to place traps or wait for the player to pass through.
* **Defensive Holds**: A heavy unit might position itself in a narrow doorway to block player progress.
* **Grenade Targets**: AI can use this provider to find narrow areas to throw grenades into, knowing the player has limited movement options.

## Performance

**Moderate.** This provider performs 4 raycasts for every candidate point generated. While not as heavy as a full 360-degree scan, high `Candidates Per Provider` counts can add up. It is recommended to use this with a reasonable `Search Radius`.