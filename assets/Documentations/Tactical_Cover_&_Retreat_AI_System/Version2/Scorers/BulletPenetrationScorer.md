# Scorer: Material Thickness (Ballistics)

**`BulletPenetrationScorerSO`** is a high-fidelity "AAA" scorer that evaluates the physical thickness of the cover object protecting the agent. It penalizes thin cover (like plywood fences, sheet metal, or bushes) that bullets would likely penetrate, ensuring the AI seeks hard cover like concrete or thick walls.

## How It Works

This scorer performs a ballistics simulation using raycasts to approximate object volume.

1.  **Line of Fire Check:** It establishes a vector from the **Threat** (Player) to the **Candidate Spot**.
2.  **Entry & Exit Calculation:** It performs a `Physics.RaycastAll` along this vector to find all intersection points with the cover object.
3.  **Thickness Measurement:** It sorts the hits by distance to identify the "Entry" point (front of the wall) and the "Exit" point (back of the wall). It calculates the distance between these two points.
4.  **Scoring:**
    * If the calculated thickness is **less** than `Min Safe Thickness`, the spot is deemed unsafe and receives the `Thin Cover Penalty`.
    * If the thickness meets or exceeds the threshold, it returns a perfect score of **1.0**.

## Parameters

* **Min Safe Thickness**: The minimum thickness (in meters) required for an object to be considered "safe" (e.g., 0.5 for 50cm of concrete).
* **Thin Cover Penalty**: The score multiplier applied to thin cover (e.g., 0.1). A low value effectively rejects thin objects unless no other options exist.

## Use Cases

* **Destructible Environments**: In games where wood or thin metal can be shot through.
* **Realistic Shooters**: Ensures AI prefers engine blocks or brick walls over wooden fences.
* **Survival**: Prevents AI from hiding behind foliage or chain-link fences that block vision but not bullets.

## Performance

**Heavy.** This scorer uses `Physics.RaycastAll` and array sorting for every candidate check. It is computationally expensive and should be used judiciously, perhaps only when the AI is under active fire.