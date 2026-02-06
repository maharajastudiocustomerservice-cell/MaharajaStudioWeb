# Scorer: Line of Fire Safety

**`LineOfFireScorerSO`** is a squad-coordination scorer designed to prevent friendly fire incidents. It ensures that an AI agent does not choose a hiding spot or position that blocks the firing line of a teammate engaging a target.

## How It Works

This scorer acts as a **Binary Disqualifier**. It does not grade spots on a curve; a spot is either safe (1.0) or obstructing fire (0.0).

The logic follows these steps for every candidate spot:

1.  **Identify the Target:** The system determines the focal point of the squad's attention. This is typically the `playerLastKnownPosition`. If that is unavailable, it defaults to the current position of the nearest player.
2.  **Analyze Allies:** The scorer iterates through all known allies (excluding the agent itself).
3.  **Project Fire Tunnel:** For each ally, it mathematically constructs a line segment starting from the ally's eye position and ending at the target's center.
4.  **Check Obstruction:** It calculates the shortest distance from the candidate spot to this line segment.
    * If the distance is **less than** the `Safety Radius`, the spot is considered to be "in the crossfire."
    * The scorer immediately returns **0.0**, effectively disqualifying the spot (depending on the scorer's weight).
5.  **Pass:** If the candidate spot is outside the safety radius of all ally fire lines, it returns **1.0**.

## Parameters

* **Safety Radius**: A float value that defines the thickness of the "fire tube." A larger radius ensures the agent gives teammates a wider berth, while a smaller radius allows for tighter formations but increases the risk of clipping.

## Use Cases

* **Corridor Combat**: Prevents agents from clustering in a single line of sight within narrow hallways.
* **Coordinated Flanking**: Ensures that while one unit suppresses the player, the flanking unit moves around the fire, not through it.
* **Heavy Weapons Support**: Essential when one unit (e.g., a machine gunner) has a fixed lane of fire that must remain clear.

## Performance and Dependencies

* **Complexity:** $O(N)$ where $N$ is the number of allies.
* **Cost:** Low. The calculation uses simple vector dot products to determine the distance to a line segment. It does not perform physics raycasts.
* **Requirement:** The `HidingContext` must have the `allies` list populated, and there must be a valid target (`playerLastKnownPosition` or valid `players` list).