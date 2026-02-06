# Scorer: Push Forward

**`PushForwardScorerSO`** is a movement-drive scorer that incentivizes the AI to close the distance to the target. It creates "Rusher" or "Aggressive" behaviors by rewarding spots that physically move the agent closer to the enemy.

## How It Works

This scorer measures the distance gain achieved by moving to a candidate spot.

1.  **Distance Comparison:** It calculates two distances:
    * **Current Distance:** From the Agent's current position to the Target.
    * **Candidate Distance:** From the Candidate spot to the Target.
2.  **Evaluation:**
    * **Gaining Ground:** If `Candidate Distance < Current Distance`, the spot is closer. The score starts at **0.5** and increases based on how much distance is closed (up to a max of ~5 meters for a full score).
    * **Retreating/Static:** If `Candidate Distance >= Current Distance`, the spot is further away or static. The scorer returns **0.0**.

This effectively filters out any "retreating" options and prioritizes the spots that offer the most forward progress.

## Parameters

* This scorer currently has no exposed parameters. It uses an internal constant (approx. 5 meters) to normalize the "distance gained" score.

## Use Cases

* **Melee Units**: Essential for zombies or sword-wielders to force them to constantly close the gap while still using cover (if combined with other scorers).
* **Shotgunners**: Drives units with short-range weapons to get into effective range.
* **Flanking**: When combined with a flank provider, this ensures the flank maneuver tightens the noose rather than drifting away.

## Performance

**Fast.** It relies on standard `Vector3.Distance` calculations.