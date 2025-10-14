# Scorer: Threat Avoidance

**`ThreatScorerSO`** is an advanced scorer that makes AI aware of and avoid areas of known danger. It evaluates spots based on their proximity to a dynamic, global "threat map."

## How It Works

This scorer relies on an external system, the **`ThreatMapService`**, which is assumed to hold a list of active "threat points." These points could represent locations where a player was recently seen, where an explosion just occurred, or an area under suppressive fire.

For each candidate hiding spot, the scorer:

1.  **Finds the Closest Threat**: It iterates through all active points in the `ThreatMapService` and finds the one closest to the candidate spot.
2.  **Calculates Score Based on Distance**: The score is determined by how far the candidate spot is from this closest threat point.
    *   A spot right on top of a threat point gets a score of **0.0**.
    *   A spot that is farther away than the `Safe Distance` gets a score of **1.0**.
    *   The score scales linearly in between.

In short, this scorer makes AI want to move as far away from known danger zones as possible. If there are no active threats on the map, it returns a perfect score of 1.0.

## Parameters

*   **Weight**: Determines how strongly the AI will avoid known threats. For most AI, this should have a high weight to encourage self-preservation.
*   **Safe Distance**: A float value on the scorer asset that defines the radius of influence for a threat point. Once a spot is farther than this distance from a threat, the threat no longer affects its score.

## Use Cases

*   **Creating Persistent Awareness**: This is the primary use case. It allows AI to "remember" that a certain area is dangerous, even after the player has left. If a player shoots from a window, you can add a threat point there, and AI will avoid that window for a period of time.
*   **Responding to Grenades and Explosions**: When a grenade is thrown, you can add a temporary threat point at its location. This scorer will then naturally make all nearby AI flee from the blast radius.
*   **Suppressing Fire**: An AI under fire can add a threat point at the source of the shots, encouraging it and its allies to find cover that is not exposed to that direction or location.

## Performance and Dependencies

The performance of this scorer is very good. Its cost is proportional to the number of active threat points in the `ThreatMapService`, as it involves a series of distance calculations.

*   **Crucial Dependency**: This scorer is **completely dependent on the `ThreatMapService`**. It does nothing on its own. The service is automatically updated by the `EnemyHider` when it creates a `HidingContext`, but you can also add your own threats to it from other game systems (e.g., an explosion manager).