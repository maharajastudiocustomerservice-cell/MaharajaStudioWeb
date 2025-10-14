# Scorer: Distance From Players

**`DistanceScorerSO`** is a fundamental scorer that evaluates hiding spots based on their distance from the nearest player. It encourages AI to move farther away from threats.

## How It Works

This scorer calculates the distance from the candidate hiding spot to every player currently known to the system. It finds the shortest of these distances and uses that value to calculate a score.

The score is normalized by the `Search Radius` from your `HidingSettings`. The formula is essentially:

`Score = (Distance to Nearest Player) / (Search Radius * normalizeByRadius)`

This means a spot right next to a player will have a score near 0, while a spot at the edge of the search radius will have a score near 1.0. In short, **farther away is better.**

### Negative Weight Trick

This scorer has a special interaction with negative weights. If you give it a negative weight in the `HidingSettings` (e.g., -1.0), you will invert its behavior. Instead of rewarding distance, it will **reward proximity**, encouraging the AI to find the closest possible (safe) hiding spot. This is useful for aggressive or hunter-style AI.

## Parameters

*   **Weight**: Determines how much the AI prioritizes distance. A high positive weight creates cowardly AI. A high negative weight creates aggressive AI.
*   **Normalize By Radius**: This multiplier on the scorer asset adjusts the normalization.
    *   `1.0` (default): The score scales linearly with the `Search Radius`. A spot at the search radius distance gets a score of 1.0.
    *   `< 1.0`: The score will reach 1.0 before hitting the full search radius. For example, at `0.5`, a spot at half the search radius already gets a score of 1.0.
    *   `> 1.0`: The score will only approach 1.0 for distances beyond the search radius.

## Use Cases

*   **Cowardly AI**: Use with a high positive weight. This is the primary scorer for AI that should run away from the player.
*   **Ranged Units**: Use with a moderate positive weight for archers or mages who need to maintain a safe distance.
*   **Stealthy Hunters**: Use with a high **negative weight** to make the AI try to sneak as close to the player as possible while remaining hidden.

## Performance

The performance of this scorer is **excellent**. For each candidate spot, it performs a simple `Vector3.Distance` calculation for each player. This is a very fast operation, and the scorer has a negligible impact on performance.