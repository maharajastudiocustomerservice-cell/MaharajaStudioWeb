# Scorer: Repetition Penalty

**`RepetitionPenaltyScorerSO`** is a utility scorer that forces the AI to "rotate" positions. It penalizes candidate spots that are geographically close to where the agent has hidden recently.

## How It Works

This scorer accesses the agent's short-term memory.

1.  **Fetch History:** It retrieves the `PositionHistory` queue from the `TacticalAgent`.
2.  **Comparison:** It compares the candidate spot's position against every position in the history.
3.  **Score:**
    * **0.0 (Reject):** If the candidate is within `Memory Radius` of *any* previous spot.
    * **1.0 (Accept):** If the spot is fresh territory.

## Parameters

* **Memory Radius**: The radius (in meters) around previous spots that is considered "used ground."

## Use Cases

* **Whac-A-Mole**: Prevents the AI from popping up at the exact same corner over and over again.
* **Evasive Tactics**: Forces the AI to constantly relocate after firing, making them a harder target.

## Performance and Dependencies

* **Thread Safety:** **Main Thread Only**. Accesses the `TacticalAgent` instance.
* **Cost:** Very Low. Simple distance checks against a small history queue (usually size 3-5).