# Provider: Cover Nodes

**`CoverNodeProviderSO`** is a provider that uses a pre-defined set of hiding spots that have been manually placed in the scene by a designer.

## How It Works

This provider relies on a network of "Cover Nodes" that you place throughout your level. Each node is a simple GameObject with a specific component (`CoverNode`, which registers it to the `CoverNodeRegistry`) that marks it as a potential hiding spot.

When this provider is active, it doesn't search the environment dynamically. Instead, it gets a list of all registered `CoverNode` objects from the central `CoverNodeRegistry`. It then uses the position of each node as a candidate hiding spot.

Before adding a spot, it verifies that the node's position is on a valid NavMesh area, ensuring the AI can actually reach it.

This provider does **not** provide a cover normal, so scorers that rely on the direction of cover will not benefit from it, and the system's peeking logic will not be engaged for spots found by this provider.

## Setup

To use this provider, you must manually place `CoverNode` components in your scene.

1.  Create an empty GameObject in your scene.
2.  Place it where you want the AI to be able to hide (e.g., behind a crate, at the corner of a wall).
3.  Add the `CoverNode` component to this GameObject.
4.  Repeat for all desired hiding spots.

## Parameters

*   **NavMesh Area Mask** (from `HidingSettings`): Defines which NavMesh areas are considered valid. If a `CoverNode` is placed on an invalid area, it will be ignored.

## Use Cases

*   **Highly Controlled Level Design**: This is the perfect provider when you want exact, deliberate control over where your AI can hide. It removes the guesswork of dynamic systems.
*   **Performance Optimization**: This is one of the most performant providers. It avoids costly physics queries or complex calculations by relying on a simple, pre-computed list of points. It's an excellent choice for performance-critical scenarios or mobile platforms.
*   **Defining Tactical Positions**: Use it to mark specific strategic locations in your level that AI should use for cover, ambushes, or defensive positions.

## Performance

This provider has a very low performance overhead. Its main cost is iterating through the list of registered nodes. The performance impact is minimal, even with hundreds of nodes in a scene, making it significantly faster than dynamic providers like `BehindObstacleProviderSO` or `VoxelGridProviderSO`.