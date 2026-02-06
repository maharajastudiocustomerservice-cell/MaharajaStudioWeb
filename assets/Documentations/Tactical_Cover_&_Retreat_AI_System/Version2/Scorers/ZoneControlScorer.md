# Scorer: Zone Control (LOS)

**`ZoneControlScorerSO`** is a strategic scorer designed for defensive or "Overwatch" roles. Unlike `ObjectiveProximityScorer` (which simply pulls the agent *physically close* to an objective), this scorer rewards positions that maintain a clear **Line of Sight (LOS)** to the objective, allowing the AI to guard it effectively from a distance.

## How It Works

This scorer evaluates the tactical value of a spot based on its ability to "see" a key location.

1.  **Identify Target:** It searches the `ObjectiveService` for a valid objective. (Currently, it defaults to the first active objective found, but supports ID filtering).
2.  **Distance Check:** It first verifies if the candidate spot is within the `Max Control Distance` of the objective. If the spot is too far away to effectively guard the point, it is disqualified (Score 0.0).
3.  **Visibility Check:** It performs a Physics Raycast from the candidate spot's eye position to the center of the objective.
4.  **Score:**
    * **1.0 (High Value):** If the raycast has a clear line of sight to the objective.
    * **0.0 (Disqualified):** If the view is blocked by a wall or obstacle.

## Parameters

* **Target Objective ID**: An integer ID used to filter which specific objective to watch (matching your `ObjectiveService` IDs).
* **Max Control Distance**: The maximum range (in meters) from which the AI is allowed to guard the point.

## Use Cases

* **King of the Hill**: AI defenders will find spots like balconies or windows that overlook the capture point, rather than standing directly inside the capture zone where they are vulnerable to grenades.
* **Sniper Overwatch**: Forces sniper units to find high-visibility lines of sight on key choke points.

## Performance and Dependencies

* **Thread Safety:** **Main Thread Only**. It relies on the `ObjectiveService`, which is likely not thread-safe.
* **Cost:** Moderate. Performs one Physics Raycast per candidate spot within range.