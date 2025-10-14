# Scorer: Visibility

**`VisibilityScorerSO`** is one of the most essential scorers in the system. It evaluates hiding spots with a simple binary question: "Can a player see this spot?" It heavily penalizes any spot that is not completely concealed from all players.

## How It Works

This scorer uses the `IVisibilityService` to determine if a candidate hiding spot is exposed. To make the check more robust and simulate the physical presence of an agent, it checks two separate points at the candidate location:

1.  A **high point** (simulating the agent's head).
2.  A **low point** (simulating the agent's center of mass).

It then asks the `IVisibilityService`, "Does any player have a direct, unobstructed line of sight to either of these points?"

The scoring is binary:

*   **If YES:** At least one player can see the spot. It is considered compromised and receives a score of **0.0**.
*   **If NO:** The spot is fully concealed from all players. It receives a perfect score of **1.0**.

This scorer does **not** care about the player's field of view (FOV). It only checks for physical line of sight. A spot directly behind a player is still considered "visible" by this scorer if there are no walls or obstacles in between. For FOV-based logic, see the `FOVScorerSO`.

## Parameters

*   **Weight**: Determines how much the AI prioritizes being physically hidden. For almost all hiding behaviors, this should have a very high weight. It's a core component of what it means "to hide."
*   **Player Eye Height** (from `HidingSettings`): This global setting is used to calculate the positions of the high and low points for the visibility check.

## Use Cases

*   **Core Hiding Mechanic**: This is a foundational scorer and should be included in nearly every `HidingSettings` configuration. It is the primary driver for making AI take cover behind walls, crates, and other obstacles.
*   **Breaking Line of Sight**: When an AI needs to escape, this scorer ensures it chooses a location that will actually break the player's line of sight.
*   **Working with Other Scorers**: It's often used as the primary "filter." Other scorers then rank the spots that this scorer has already deemed "safe." For example, you can combine it with the `DistanceScorerSO` to find a spot that is **both** hidden **and** far away.

## Performance and Dependencies

The performance of this scorer is entirely dependent on the implementation of the `IVisibilityService.AnyPlayerHasLineOfSight` method. This check almost always involves one or more `Physics.Raycast` calls.

*   The cost scales with the number of players and the number of candidate spots.
*   Because it performs at least two visibility checks per candidate, it is a moderately expensive scorer.
*   It has a hard dependency on a correctly configured **`IVisibilityService`**. Without it, this scorer cannot function.