# Scorer: Muzzle Discipline

**`MuzzleDisciplineScorerSO`** is a tactical movement scorer that simulates professional firearm safety rules (specifically "do not cover anything you are not willing to destroy"). It ensures agents do not cross directly in front of a teammate's weapon barrel, regardless of whether that teammate is currently firing at a target.

## How It Works

Unlike the `LineOfFireScorer` (which cares about a specific target), `MuzzleDisciplineScorer` cares about the **direction the ally is facing**. It projects a "danger cylinder" extending forward from every ally.

The logic follows these steps:

1.  **Analyze Allies:** Iterate through all squad members.
2.  **Project Forward Vector:** Retrieve the ally's forward directional vector.
3.  **Cylinder Check:** The scorer calculates the position of the candidate spot relative to the ally. It checks two conditions:
    * **Depth:** Is the spot in front of the ally (positive dot product) and within the defined `Danger Distance`?
    * **Width:** Is the perpendicular distance from the spot to the ally's forward line less than the `Danger Radius`?
    * *Note:* This calculation flattens the Y-axis, treating the check as 2D (top-down) to ensure robustness on slopes.
4.  **Result:**
    * If **both** conditions are true, the agent is standing in front of the ally's gun. The scorer returns **0.0**.
    * Otherwise, it returns **1.0**.

## Parameters

* **Danger Distance**: How far forward (in meters) the "danger zone" extends from an ally. Beyond this distance, the scorer ignores the ally's facing direction.
* **Danger Radius**: The width (radius) of the cylinder extending from the ally.

## Key Differences: Line of Fire vs. Muzzle Discipline

| Feature | Line of Fire Scorer | Muzzle Discipline Scorer |
| :--- | :--- | :--- |
| **Reference** | Line from Ally to **Enemy** | Line from Ally to **Forward Direction** |
| **Purpose** | Prevent blocking active shooting | Prevent flagging/crossing lines during movement |
| **Context** | Best during active combat | Best during patrol, searching, or moving formations |

## Use Cases

* **Tactical Formations**: Keeps agents in a proper wedge or line formation while moving, preventing them from stepping on each other's toes.
* **CQB / Room Clearing**: Ensures that when a team stacks up or enters a room, the rear agents do not walk in front of the point man.
* **Non-Combat Movement**: Makes the AI look professional and trained by respecting personal space and weapon orientation even when no enemy is visible.

## Performance and Dependencies

* **Burst Compatible:** Yes. This scorer implements `IMultiThreadedScorer`, making it safe and highly efficient for use in the Asynchronous/Burst job system.
* **Cost:** Extremely Low. Uses simple vector math.
* **Requirement:** Requires the `allies` list in `HidingContext` to be populated.