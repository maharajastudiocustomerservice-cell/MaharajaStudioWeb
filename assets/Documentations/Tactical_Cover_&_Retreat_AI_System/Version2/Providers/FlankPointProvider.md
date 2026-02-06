# Provider: Flank Points

**`FlankPointProviderSO`** is a tactical provider that generates candidate positions specifically located at the sides (flanks) or rear of a target. It actively ignores positions directly in front of the target.

## How It Works

This provider requires a target (either a currently visible player or a `LastKnownPlayerPosition`). If no target is available, it generates no candidates.

1.  **Target Orientation:** It determines the forward vector of the target. If the target is only a memory (position), it estimates the orientation based on the vector from the AI to that position.
2.  **Arc Calculation:** It calculates an angle offset based on the `Min Flank Angle`. For example, if set to 90 degrees, the search starts directly to the target's right and left.
3.  **Spread:** It adds a random variation within the defined `Arc Width`.
4.  **Alternating Sides:** The provider alternates between generating a point on the Left Flank and the Right Flank to ensure a balanced set of options.
5.  **NavMesh Validation:** It projects these calculated points onto the NavMesh to ensure they are walkable.

## Parameters

* **Min Flank Angle**: The starting angle from the target's forward vector.
    * `90` = Starts at the immediate side (Perpendicular).
    * `135` = Starts at the rear-diagonal.
    * `180` = Directly behind the target.
* **Arc Width**: How much variation is allowed from the minimum angle.
* **Flank Distance**: The fixed distance from the target where the points will be generated.

## Use Cases

* **Ambushing**: Used to position stealth units behind a player.
* **Breaking Stalemates**: If a player is hunkered down behind cover, this provider forces the AI to move to a position where the player's cover is ineffective.
* **Encirclement**: When combined with other providers, this ensures that not all AI agents stack up in front of the player.

## Performance

**Very Good.** This provider relies on simple vector mathematics and standard `NavMesh.SamplePosition` calls. It is very lightweight and can be run frequently without performance concerns.