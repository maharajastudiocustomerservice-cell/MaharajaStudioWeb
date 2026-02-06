# Provider: Squad Formation

**`SquadFormationProviderSO`** is a specialized provider that generates candidate points based on a strict tactical formation relative to a Squad Leader. It relies on the `SquadCoordinator` system to determine each agent's specific slot in the formation.

## How It Works

1.  **Leader Identification:** It queries the `SquadCoordinator` to find the leader of the agent's current squad. If the agent *is* the leader, or no leader exists, it runs the specified `Fallback Provider`.
2.  **Slot Calculation:** It determines the agent's index in the squad (e.g., Member 1, Member 2) and calculates the ideal local position offset based on the selected `Formation Shape` (Wedge, Line, File, etc.).
3.  **World Transformation:** It transforms this local offset into world space relative to the Leader's position and orientation.
    * *Note:* It can be configured to use either the Leader's body rotation or their velocity vector for orientation.
4.  **Jitter & Sampling:** It generates points around this ideal "slot" with a small amount of random jitter (Radius ~2.0f). This ensures that if the perfect formation spot is inside a wall, the AI can still find a valid NavMesh position nearby.

## Parameters

* **Shape**: The type of formation to use (`Wedge`, `Line`, `File`, `Diamond`, `Vee`).
* **Spacing**: The distance between agents in the formation.
* **Wedge Angle**: The angle of the formation (applicable for Wedge/Vee shapes).
* **Use Body Orientation**: If true, the formation rotates with the leader's body transform. If false, it rotates with their movement direction (velocity).
* **Fallback Provider**: The provider to use if the agent is the leader or not in a squad (usually a standard cover provider like `CoverProviderSO`).

## Use Cases

* **Military Squads**: Moving in a strict Wedge or File formation while patrolling.
* **Convoy Protection**: Agents moving in a Diamond formation around a VIP.
* **Organized Assault**: An entire squad advancing in a Line formation to maximize firepower.

## Performance

**Excellent.** The math for calculating formation offsets is trivial. The only cost is the standard NavMesh sampling for the candidate points. This is one of the cheapest providers available.