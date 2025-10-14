# Provider: Voxel Grid

**`VoxelGridProviderSO`** is a unique provider that finds potential hiding spots by sampling points in a 3D grid (a "voxel grid") around the agent and checking if these points are located *inside* solid geometry.

## How It Works

This provider creates a uniform 3D grid of points centered on the agent's position. The size of this grid is determined by the `Search Radius`. For each point in the grid, it performs a `Physics.OverlapBox` check.

If this check returns any colliders on the `Occluder Mask` layer, it means the point is inside or touching a piece of geometry. That point is then added to the list of candidate hiding spots.

Unlike other providers that find spots *behind* or *near* objects, this one is specifically designed to find spots *within* them. This provider does not generate a cover normal.

**Important Note:** This provider does not check for NavMesh reachability. It is intended to be used with scorers like the `ReachabilityScorerSO` to filter out any points that the AI cannot actually get to.

## Parameters

*   **Resolution**: This is a key setting on the provider asset. It defines the number of points to sample along each of the three axes (X, Y, Z). The total number of sample points is `resolution * resolution * resolution`. **Be careful with this value, as it has a major impact on performance.**
*   **Collision Check Size**: The size of the small box used for the `OverlapBox` check at each grid point. A larger value is more likely to detect nearby geometry but is less precise.
*   **Search Radius** (from `HidingSettings`): Defines the overall size of the 3D grid. The grid will be a cube with sides of length `Search Radius * 2`.
*   **Occluder Mask** (from `HidingSettings`): The physics layer mask that determines which objects are considered valid geometry to hide inside.

## Use Cases

*   **Hiding in "Soft" Cover**: This is the perfect provider for finding spots inside non-solid or semi-solid objects like thick bushes, tall grass, or magical concealment zones.
*   **Complex Geometry**: Can be useful for finding spots inside unusual or complex meshes that don't have a clear "behind," such as a hollowed-out log or a small cave opening.

## Performance

**This is potentially the most performance-intensive provider in the entire system.** The number of physics checks it performs is `resolution³`.

*   `resolution = 8` (default) -> `8 * 8 * 8 = 512` physics checks.
*   `resolution = 10` -> `10 * 10 * 10 = 1000` physics checks.
*   `resolution = 16` -> `16 * 16 * 16 = 4096` physics checks.

It is **critical** to keep the `resolution` as low as possible. This provider should be used sparingly and only when its specific functionality is required. For general-purpose cover finding, providers like `BehindObstacleProviderSO` or `CoverNodeProviderSO` are far more performant. Always profile your game when using this provider.