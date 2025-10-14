# Scorer: Team Proximity

**`TeamProximityScorerSO`** is a scorer that encourages agents to hide near their allies, promoting group cohesion and squad-based behavior.

## How It Works

This scorer evaluates a candidate hiding spot based on its distance to the nearest friendly unit.

1.  **Find Nearest Ally**: It iterates through the list of allies provided in the `HidingContext` (sourced from the `EnemyHider`'s `allies` list) and finds the one closest to the candidate spot.
2.  **Compare to Optimal Distance**: It then compares this closest distance to the `Optimal Ally Distance` defined on the scorer asset.
3.  **Calculate Score**: The score is highest (1.0) when the spot is exactly the optimal distance from the nearest ally. The score decreases as the spot gets either closer to or farther away from the ally than this ideal distance.

If the agent has no allies, this scorer returns a neutral score of 0.5, having no effect on the decision. This logic encourages agents to "stick together" but not "stand on top of each other."

## Parameters

*   **Weight**: Determines how strongly the AI will prioritize staying near its teammates. A high weight will cause agents to form tight groups.
*   **Optimal Ally Distance**: This float value on the scorer asset defines the ideal distance (in meters) the agent should maintain from its closest ally.

## Use Cases

*   **Squad Behavior**: This is the primary use case. It makes soldier AI maintain formations and hide as a unit, rather than scattering across the map.
*   **Pack Animals**: Perfect for creating pack-based AI like wolves or raptors that hunt and move together.
*   **Support Roles**: Can be used to make support units (like medics or officers) stay close to the combat units they are supposed to be assisting.
*   **Discouraging Isolation**: Prevents a single AI from wandering off on its own, which can make the overall group feel more intelligent and coordinated.

## Performance and Dependencies

The performance of this scorer is **excellent**. For each candidate spot, it performs a series of fast distance calculations. Its impact on performance is negligible.

*   **Dependency**: This scorer's functionality is entirely dependent on the **`allies` list** on the `EnemyHider` component being correctly populated by your own controller scripts. If the list is empty, it will have no effect.