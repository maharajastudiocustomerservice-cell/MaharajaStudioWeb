# Scorer: Squad Separation

**`SquadSeparationScorerSO`** is a spatial scorer designed to maintain a minimum physical distance between squad members. While `TeamProximityScorer` pulls agents together to form a cohesive unit, `SquadSeparationScorer` pushes them apart locally to prevent overcrowding.

## How It Works

This scorer functions as a proximity filter.

1.  **Analyze Allies:** It iterates through all squad members in the `HidingContext`.
2.  **Distance Check:** It calculates the squared distance between the candidate spot and every ally's current position.
3.  **Score:**
    * **0.0 (Disqualified):** If *any* ally is closer than the defined `Min Separation`, the spot receives a 0 score. Note: Unlike Reservation (which checks *future* spots), this checks *current* positions.
    * **1.0 (Pass):** If all allies are outside the minimum separation radius.

## Parameters

* **Min Separation**: The minimum distance (in meters) allowed between agents. Default is **3.0f**.

## Use Cases

* **Explosive Safety**: Prevents the squad from clustering so tightly that a single grenade could kill everyone.
* **Pathfinding Clarity**: Keeping agents 3+ meters apart ensures their NavMeshAgents don't fight for the same small patch of navigation mesh.

## Performance and Dependencies

* **Burst Compatible:** Yes. Implements `IMultiThreadedScorer`.
* **Cost:** Extremely low. Uses simple distance-squared checks.