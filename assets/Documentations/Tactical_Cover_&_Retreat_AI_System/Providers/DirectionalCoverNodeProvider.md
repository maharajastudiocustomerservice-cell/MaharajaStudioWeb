# Provider: Directional Cover Nodes

**`DirectionalCoverNodeProviderSO`** is an intelligent version of the `CoverNodeProviderSO`. It selects pre-placed `CoverNode` objects only if they are oriented correctly, providing cover that faces away from the player's position.

## How It Works

Like the standard `CoverNodeProvider`, this provider uses the central `CoverNodeRegistry` to get a list of all manually placed cover points in the scene. However, it adds a crucial filtering step.

For each `CoverNode`, it checks the node's defined "cover direction." It then compares this direction to the direction from the AI agent to the player(s). The node is only considered a valid candidate if its cover direction is pointing generally away from the player.

This ensures that the AI doesn't try to take cover on the wrong side of an object, making for much more believable and effective tactical behavior.

This provider does not provide a cover normal for scorers or the peeking system to use.

## Setup

The setup is the same as the `CoverNodeProvider`, but with one extra step:

1.  Create an empty GameObject and add the `CoverNode` component.
2.  **Crucially, adjust the `Cover Direction` vector in the `CoverNode` component's settings.** This vector should point in the direction the cover is "facing." For example, for a chest-high wall, the direction should point straight up from the wall's top edge, away from the side the AI should stand on. A gizmo in the scene view will help you visualize this direction.

## Parameters

*   **Acceptance Angle**: This is a key setting on the provider asset itself. It defines how forgiving the directional check is. The value represents the total angle of the cone used for the check.
    *   A **small angle** (e.g., 30) means the cover must be almost perfectly oriented away from the player to be considered. This is strict but very precise.
    *   A **large angle** (e.g., 180) means the cover can be facing in any direction in the hemisphere away from the player. This is very lenient.
*   **NavMesh Area Mask** (from `HidingSettings`): Ensures the selected node is on a valid NavMesh area.

## Use Cases

*   **Smart Tactical Cover**: This is the primary use case. It allows you to design levels with clear tactical positions (e.g., L-shaped corners, barricades) and have the AI use them intelligently based on the threat direction.
*   **Flanking and Positioning**: By ensuring cover is used correctly, you can create more advanced behaviors where AI effectively suppresses the player from safe positions.

## Performance

The performance is excellent and very close to the standard `CoverNodeProvider`. It adds a simple vector math calculation (`Vector3.Angle`) for each node, but this is extremely fast. It remains one of the most performant providers and is a great choice for nearly any project that uses manually placed cover points.