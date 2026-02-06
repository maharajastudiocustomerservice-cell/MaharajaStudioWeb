# Scorer: Wall Hugging

**`WallHuggingScorerSO`** is a survival-focused scorer that strongly encourages the agent to stay physically close to geometry (walls, large obstacles). It combats "Open Field Syndrome," where an AI might hide in a technically valid spot that feels unnatural because it's floating in the middle of a room.

## How It Works

1.  **Geometry Search:** It performs an `OverlapSphere` check to find any colliders on the `Wall Mask` layers within the `Scan Radius`.
2.  **Nearest Point Calculation:** If colliders are found, it calculates the `ClosestPoint` on the collider's surface to the candidate spot.
3.  **Distance Scoring:**
    * **Touching Wall:** If the distance is near 0, the score is **1.0**.
    * **Far from Wall:** As the distance approaches `Scan Radius`, the score drops to **0.0**.
    * **No Wall:** If no walls are found within the radius, the score is **0.0**.

## Parameters

* **Scan Radius**: The maximum distance from a wall the agent is allowed to be to receive any score.
* **Wall Mask**: The LayerMask defining what counts as a "Wall" (usually Default, Static, or a specific Cover layer).

## Use Cases

* **Indoor Movement**: Keeps AI moving along the edges of corridors rather than the center.
* **Stealth**: Spies/Assassins look smarter when sticking to the shadows at the edge of a room.
* **Cover Readiness**: An agent hugging a wall is always closer to breaking line of sight than one standing 2 meters away from it.

## Performance

**Moderate.** Uses `OverlapSphere` followed by `ClosestPoint` calculations. It is generally efficient enough for standard usage.