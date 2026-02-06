# Provider: Room Clearance (Pie Slicing)

**`RoomClearanceProviderSO`** is designed for Close Quarters Battle (CQB) scenarios. It generates a "fan" of points around a corner, allowing an AI to methodically "slice the pie"—gradually clearing a room from the outside before entering.

## How It Works

This provider combines edge detection with arc generation.

1.  **Corner Scan:** Similar to `CornerEdgeProvider`, it scans for depth discontinuities to identify corners within the `Scan Range` using a radial raycast sweep.
2.  **Arc Generation:** Once a corner is found, instead of placing a single point, it generates a series of points in a semi-circle (arc) around that corner.
3.  **Outward Facing:** The arc is oriented based on the corner's normal, ensuring the points fan out into the open space/room being cleared.
4.  **Visibility Check:** It performs a `Linecast` from the candidate point back to the corner to ensure the AI actually has a line of sight to the edge it is supposed to be clearing (prevents points spawning inside walls).

## Parameters

* **Scan Range**: The distance to scan for corners.
* **Ray Density**: The number of rays used to find the initial corners.
* **Stand Off Distance**: The distance from the corner where the AI will stand while clearing.
* **Points Per Corner**: How many points to generate in the "fan" for each detected corner.
* **Arc Angle**: The total angle of the fan (e.g., 90 degrees).

## Use Cases

* **Breach and Clear**: AI stacks up on a door, then uses these points to check the room's corners methodically.
* **Cautious Advance**: AI moves slowly around a blind corner, checking for threats at each step of the arc.
* **SWAT / Tactical Shooters**: Essential for realistic police or special forces behavior.

## Performance

**Heavy.** Like the Corner Edge provider, this relies on a radial scan plus additional calculations and linecasts for the arc generation. Use strictly for tactical phases (e.g., when `IsThreatened` is false but the AI is in "Search" mode).