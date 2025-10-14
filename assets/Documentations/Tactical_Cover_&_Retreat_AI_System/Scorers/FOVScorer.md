# Scorer: FOV Avoidance

**`FOVScorerSO`** is a critical scorer for stealth gameplay. It evaluates spots based on whether they fall within any player's field of view (FOV). It heavily penalizes spots that the player is actively looking towards.

## How It Works

This scorer performs a simple but crucial binary check using the `IVisibilityService`:

1.  It asks the `IVisibilityService`: "Is this candidate spot inside any player's viewing cone AND visible from their eyes?"
2.  Based on the answer, it returns a score:
    *   **If YES:** The spot is in the player's direct field of view. The scorer returns **0.0**.
    *   **If NO:** The spot is outside the player's direct field of view (either behind them, to the side, or obscured by an object). The scorer returns **1.0**.

This creates a strong incentive for the AI to stay out of the player's forward-facing view cone, encouraging flanking and sneaking behaviors.

## Distinguishing from `VisibilityScorer`

It's important to understand the difference between this scorer and the general `VisibilityScorer`:

*   **`VisibilityScorer`**: Checks for a clear line of sight from the player's eyes to the spot, regardless of which direction the player is facing. A spot directly behind the player would be considered "visible" if there are no walls in the way.
*   **`FOVScorer`**: *Also* checks for line of sight, but *only* if the spot is within the player's view cone angle. A spot directly behind the player will always get a perfect score of 1.0 from this scorer, because it's not in the FOV.

For true stealth gameplay, you typically use **both** scorers together. This tells the AI to:
1.  Strongly prefer spots outside the player's FOV (`FOVScorer`).
2.  Of those spots, prefer the ones that are also physically hidden behind objects (`VisibilityScorer`).

## Parameters

*   **Weight**: Determines how strongly the AI will prioritize staying out of the player's view cone. For stealthy AI, this should usually have a very high weight.

## Use Cases

*   **Classic Stealth Mechanics**: This is the cornerstone of any system where AI needs to avoid a player's vision cone (like in *Metal Gear Solid* or *Dishonored*).
*   **Flanking Behavior**: By heavily penalizing spots in front of the player, this scorer naturally encourages AI to move to the player's sides or back.
*   **Creating "Blind Spots"**: This scorer is what makes hiding behind a player a valid and rewarding tactic for the AI.

## Performance and Dependencies

The performance of this scorer is entirely dependent on the underlying implementation of `IVisibilityService.InAnyPlayerFOVAndVisible`. This check typically involves fast vector math (a dot product to check the angle) and potentially a `Physics.Raycast` to check for obstructions.

It is moderately expensive, more so than simple math-based scorers, but essential for this type of gameplay. It has a hard dependency on a correctly configured **`IVisibilityService`**.