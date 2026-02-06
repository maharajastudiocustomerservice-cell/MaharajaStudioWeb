# Scorer: Player Gaze

**`PlayerGazeScorerSO`** is a visibility scorer that specifically avoids the player's direct focus. While standard visibility checks determines if the player *can* see the agent, this scorer determines if the player is *currently looking* at the spot.

## How It Works

This scorer performs a vector analysis of the player's orientation.

1.  **Vector Calculation:** It calculates the vector from the player's eyes to the candidate spot.
2.  **Angle Check:** It compares this vector with the player's `Transform.forward` vector (their gaze).
3.  **Score:**
    * **Penalty:** If the angle is smaller than `Gaze Cone Angle` (meaning the player is looking directly at the spot).
    * **1.0:** If the spot is in the player's peripheral vision or behind them.

## Parameters

* **Gaze Cone Angle**: The angle (in degrees) representing the player's foveal (focused) vision. Usually narrow (e.g., 15 degrees).
* **Penalty Strength**: How strictly to avoid the gaze. 1.0 means avoid completely; 0.5 means it's a soft preference.

## Use Cases

* **Sniper Avoidance**: If the player is aiming down a hallway, the AI will refuse to step into that hallway.
* **Sneaking**: Encourages AI to move only when the player looks away.

## Performance and Dependencies

* **Thread Safety:** **Main Thread Only**.
* **Cost:** Very Low. Simple vector math.