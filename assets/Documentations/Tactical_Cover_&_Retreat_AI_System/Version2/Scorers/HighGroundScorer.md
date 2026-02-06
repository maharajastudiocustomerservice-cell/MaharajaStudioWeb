# Scorer: High Ground

**`HighGroundScorerSO`** is a tactical scorer that evaluates the verticality of a hiding spot relative to the target. It creates a behavior where the AI naturally seeks elevation advantages, adhering to the "High Ground" tactical doctrine.

## How It Works

The scorer compares the Y-coordinate (height) of the candidate spot against the target's Y-coordinate.

1.  **Elevation Calculation:** It calculates `Difference = Candidate.y - Target.y`.
2.  **Above Target:** If the difference is positive (AI is higher), the score scales linearly from **0.5 to 1.0**.
    * A difference of 0 meters gives a score of 0.5.
    * A difference equal to or greater than `Ideal Height Advantage` gives a score of 1.0.
3.  **Below Target:** If the difference is negative or zero (AI is lower):
    * If **Penalize Low Ground** is true: The score scales down from **0.5 to 0.0** based on how deep below the target the spot is.
    * If false: It returns a neutral score of 0.5.

## Parameters

* **Ideal Height Advantage**: The height difference (in meters) required to achieve a perfect score. For example, if set to `4.0`, a spot 4 meters above the player gets the maximum bonus.
* **Penalize Low Ground**: If checked, positions significantly lower than the player will be actively discouraged (receiving low scores). If unchecked, low ground is treated as neutral.

## Use Cases

* **King of the Hill**: AI will fight to reach the top of a structure or hill.
* **Grenadiers**: Units with lobbed projectiles benefit from height; this scorer guides them to balconies or rooftops.
* **Snipers**: Gives snipers a strong preference for towers and upper-story windows.

## Performance

**Very Fast.** This scorer uses simple arithmetic comparisons. It has negligible performance cost.