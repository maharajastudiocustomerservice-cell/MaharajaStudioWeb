# Scorer: Sector Watch (Flank Security)

**`SectorWatchScorerSO`** is a squad-coordination scorer designed to maximize the team's situational awareness. It encourages individual agents to face directions (sectors) that are not currently being watched by their teammates, effectively automating "Rear Security" or "Flank Watch" behaviors.

## How It Works

This scorer operates by analyzing the "eyes" of the entire squad to find blind spots.

1.  **Divide the View:** It conceptually divides the 360-degree view around the squad into a specific number of slices or "sectors" (defined by the `sectors` parameter).
2.  **Analyze Allies:** It iterates through all teammates and calculates which sector they are currently facing based on their forward direction. It builds a "histogram" of coverage (e.g., "Sector 1 has 2 watchers, Sector 2 has 0 watchers").
3.  **Evaluate Candidate:** For the candidate hiding spot, it determines the direction the agent *would* face if they took that spot.
    * *Primary Check:* If the spot has a cover normal (e.g., a wall), it assumes the agent will look outward away from the wall.
    * *Fallback:* If no cover normal exists, it assumes the agent will look outward away from the center of the squad's formation.
4.  **Score:**
    * **1.0 (High Reward):** If the candidate spot faces a "Blind Spot" (a sector with 0 allies watching it).
    * **0.5 (Neutral):** If the sector is already watched by exactly one ally.
    * **0.0 (Penalty):** If the sector is crowded (watched by 2 or more allies), the spot is considered redundant.

## Parameters

* **Sectors**: The integer number of slices to divide the 360-degree view into. A value of **8** (default) creates 45-degree sectors, which is standard for tactical games.

## Use Cases

* **Perimeter Defense**: When a squad holds a room, this ensures they spread out to watch all doors and windows rather than all staring at the same entrance.
* **Rear Security**: If the whole squad is moving North, this scorer will highly reward a spot that allows an agent to look South (Rear), protecting the team's back.

## Performance and Dependencies

* **Burst Compatible:** Yes. Implements `IMultiThreadedScorer`.
* **Complexity:** $O(N)$ where $N$ is the number of allies.
* **Cost:** Low. Uses basic trigonometry (`Vector3.SignedAngle`) and array lookups.