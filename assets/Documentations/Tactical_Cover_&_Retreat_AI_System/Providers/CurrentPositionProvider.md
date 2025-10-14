# Provider: Current Position

**`CurrentPositionProviderSO`** is a simple but essential provider that adds the agent's own current position to the list of candidate hiding spots.

## How It Works

This provider does not search the environment. Its only job is to take the agent's current position (`enemyPosition` from the `HidingContext`), check that it's on a valid NavMesh, and add it to the list of potential spots to be evaluated by the scorers.

The purpose of this is to establish a **baseline**. By including its current location in the evaluation, the AI can compare all other potential hiding spots to the one it's already in. If no other spot offers a significant advantage, the agent's current position might receive the highest score, causing the AI to "choose" to stay put.

This provider does not generate a cover normal.

## Parameters

*   **NavMesh Area Mask** (from `HidingSettings`): Ensures the agent's current position is on a valid NavMesh area.

## Use Cases

*   **Preventing Unnecessary Movement**: This is a crucial provider for almost every configuration. It prevents the AI from "fidgeting" or abandoning a perfectly good hiding spot for another that isn't substantially better. It adds stability to the AI's decision-making.
*   **Establishing a "Cost of Moving"**: By forcing new spots to be better than the current one, you implicitly create a cost for moving. The AI will only move if it finds a spot that is demonstrably superior according to the active scorers.

## Performance

This is one of the highest-performance providers available. It adds only a single candidate to the list and performs just one `NavMesh.SamplePosition` call. Its performance impact is negligible, and it is highly recommended to include it in most `HidingSettings` configurations.