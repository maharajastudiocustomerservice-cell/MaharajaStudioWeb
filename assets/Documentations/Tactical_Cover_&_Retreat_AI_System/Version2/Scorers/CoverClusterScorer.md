# Scorer: Cover Cluster (Density)

**`CoverClusterScorerSO`** evaluates the immediate environment around a candidate spot to determine "Cover Density." It prefers areas rich in obstacles (junkyards, forests, urban debris) over isolated cover (a single rock in an open field). This gives the AI backup options if their primary spot is compromised.

## How It Works

1.  **Proximity Scan:** It performs a `Physics.OverlapSphere` check around the candidate position using the defined `Check Radius`.
2.  **Object Counting:** It counts how many valid occluders (walls, crates, trees) are found in this radius.
3.  **Density Evaluation:**
    * If the count is **<= 1** (implying only the cover itself or the floor is detected), it returns a score of **0.0** (Isolated).
    * It scales the score linearly based on `Ideal Cover Count`. If the count meets or exceeds this ideal, it returns **1.0**.

## Parameters

* **Check Radius**: The radius in meters to scan for additional cover objects.
* **Ideal Cover Count**: The number of nearby objects required to achieve a maximum score.

## Use Cases

* **Tactical Flexibility**: Ensures the AI doesn't trap itself behind a "Lonely Rock" where it can be easily flanked with no escape.
* **Urban Combat**: Draws AI towards piles of rubble or vehicle graveyards.
* **Forest Encounters**: Encourages AI to move deeper into the treeline rather than staying at the edge.

## Performance

**Moderate.** It relies on `Physics.OverlapSphereNonAlloc`, which is relatively efficient but involves checking all colliders in a small radius.