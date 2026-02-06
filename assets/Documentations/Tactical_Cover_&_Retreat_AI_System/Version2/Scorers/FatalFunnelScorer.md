# Scorer: Fatal Funnel (Doorway Avoidance)

**`FatalFunnelScorerSO`** is a tactical survival scorer designed to identify and penalize choke points. It detects if a candidate spot is located in a narrow corridor, doorway, or bridge—areas often referred to as "Fatal Funnels" in tactical doctrine.

## How It Works

This scorer measures the lateral (side-to-side) space available at the candidate position.

1.  **Orientation:** It determines the "Right" vector relative to the cover normal (or the agent's facing direction).
2.  **Width Scan:** It casts two Physics Raycasts: one Left and one Right from the candidate spot.
3.  **Measure:** It sums the distance to the nearest obstacle on both sides.
4.  **Score:**
    * **1.0 (Safe):** If the total width is greater than `Min Corridor Width`.
    * **Penalty:** If the total width is less than the minimum, it returns the `Choke Point Penalty` (default 0.0).

## Parameters

* **Min Corridor Width**: The minimum width (in meters) required for a space to be considered safe/maneuverable.
* **Choke Point Penalty**: The score assigned to a narrow spot (0.0 = Reject, 1.0 = Ignore).

## Use Cases

* **Doorway Safety**: Stops AI from taking cover *inside* a door frame where they have no room to dodge or strafe.
* **Hallway Awareness**: Discourages stopping in the middle of narrow bridges or catwalks.

## Performance and Dependencies

* **Thread Safety:** **Main Thread Only**. Uses Physics Raycasts.
* **Cost:** Moderate. Two raycasts per candidate.