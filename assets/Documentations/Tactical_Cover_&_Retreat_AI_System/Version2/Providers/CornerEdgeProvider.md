# Provider: Corner Edges

**`CornerEdgeProviderSO`** is a high-fidelity "AAA" tactical provider that scans the environment to find the exact vertical edges of walls and obstacles. This allows AI agents to perform "Tactical Leaning" maneuvers, peeking around corners without fully exposing their bodies.

## How It Works

This provider performs a high-resolution angular sweep around the agent to detect geometric discontinuities.

1.  **Radial Scan:** It casts a series of rays in a 360-degree circle around the agent at chest height.
2.  **Edge Detection:** It identifies an edge when:
    * A ray hits an object, but the *next* ray does not (Transition from Hit -> Miss).
    * A ray does not hit, but the *next* ray does (Transition from Miss -> Hit).
    * The depth (distance) between two adjacent hits jumps significantly (e.g., a gap between two buildings or objects).
3.  **Corner Placement:** Once an edge is detected, it calculates a position slightly offset from the wall normal using the `Corner Offset` parameter. This places the candidate point just "behind" or "around" the corner.
4.  **Filtering:** It uses the NavMesh to ensure the point is walkable and applies a distance check to prevent stacking multiple points on the same corner.

## Parameters

* **Scan Resolution**: The number of rays to cast in the 360-degree circle (e.g., 64). Higher values provide more accurate corner detection but cost more performance.
* **Scan Range**: The maximum distance to check for walls.
* **Corner Offset**: How far the candidate point should be placed from the actual geometry corner (e.g., 0.6 meters behind the edge).
* **Edge Depth Sensitivity**: The distance difference required between two adjacent rays to consider them as hitting different objects.

## Use Cases

* **Tactical Peeking**: The primary use case. AI moves to the edge, leans out to shoot, and leans back in.
* **Urban Combat**: Essential for city environments with many building corners and alleyways.
* **Cover-to-Cover**: Allows AI to move from one building edge to another while minimizing exposure time.

## Performance

**Heavy.** This provider casts a large number of rays (`Scan Resolution`) every time it runs. It is recommended to use this provider selectively (e.g., only when near combat) or with a lower frequency/LOD setting compared to simpler providers.