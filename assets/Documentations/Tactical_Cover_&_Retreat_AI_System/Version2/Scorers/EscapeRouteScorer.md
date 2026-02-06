# Scorer: Escape Route

**`EscapeRouteScorerSO`** is a survival scorer that ensures the agent doesn't corner themselves. It evaluates whether a hiding spot offers a valid path for further retreat if the situation worsens.

## How It Works

This scorer tests the "navigability" of the terrain *behind* the cover.

1.  **Determine Threat:** Calculates the average position of all known players to determine the "Threat Direction."
2.  **NavMesh Raycast:** It casts a ray on the Navigation Mesh starting from the candidate spot and moving **away** from the threat.
3.  **Analyze Hit:**
    * **Edge Hit:** If the ray hits a NavMesh edge (a wall, a cliff, the map boundary), it means retreat is blocked.
    * **No Hit:** If the ray travels the full `Min Escape Distance` without hitting an edge, the path is clear.
4.  **Score:**
    * **1.0:** Full escape route available.
    * **0.0 - 0.9:** Scaled based on how far the agent can retreat before hitting a wall. If the distance is very short (<1m), it returns 0.0.

## Parameters

* **Min Escape Distance**: How far (in meters) the agent needs to be able to run backwards for the spot to be considered safe.
* **Escape Cone Angle**: (Internal logic) Defines the direction away from the enemy.

## Use Cases

* **Fluid Combat**: Encourages AI to pick "open" cover (like a tree in a field) over "closed" cover (like the corner of a dead-end alley).
* **Hit and Run**: Essential for skirmisher units that need to fire a few shots and then immediately fall back.

## Performance and Dependencies

* **Thread Safety:** **Main Thread Only**. Uses `UnityEngine.AI.NavMesh.Raycast`.
* **Cost:** Low to Moderate. NavMesh raycasts are generally cheaper than Physics raycasts but still require main thread access.