# Scorer: Rear Attack Bonus

**`RearAttackScorerSO`** is a positional scorer that evaluates the relative orientation of the candidate spot to the target. It heavily rewards positions located behind the target's back, facilitating stealth, backstabs, or flanking maneuvers.

## How It Works

This scorer uses vector mathematics (Dot Product) to determine the angle of approach.

1.  **Vector Calculation:** It calculates the direction vector from the **Target** to the **Candidate Spot**.
2.  **Facing Check:** It compares this direction against the **Target's Forward Vector**.
3.  **Dot Product Scoring:**
    * **In Front:** If the spot is directly in front of the target (Target is looking at it), the Dot Product is 1.0. This converts to a score of **0.0**.
    * **Behind:** If the spot is directly behind the target (Target is looking away), the Dot Product is -1.0. This converts to a score of **1.0**.
    * **Side:** Positions directly to the side receive a neutral score around **0.5**.

## Parameters

* This scorer relies purely on relative geometry and has no tweakable parameters.

## Use Cases

* **Stealth AI**: Ideal for "Spy" or "Assassin" classes that need to stay out of the player's cone of vision.
* **Surrounding**: Encourages a squad to fan out and wrap around a target, as spots behind the player become mathematically more valuable than spots in front.
* **Critical Hits**: If your game has a damage bonus for back attacks, this scorer aligns the AI behavior with that mechanic.

## Performance

**Very Fast.** Uses efficient vector math (`Vector3.Dot`). It is extremely lightweight.