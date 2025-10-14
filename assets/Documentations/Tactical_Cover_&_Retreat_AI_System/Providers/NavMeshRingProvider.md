# Provider: NavMesh Ring

**`NavMeshRingProviderSO`** is a versatile provider that generates potential hiding spots by sampling points on the NavMesh in concentric circles around the agent.

## How It Works

This provider creates a series of rings around the agent's current position, up to the maximum `Search Radius` defined in the `HidingSettings`. It then generates a number of sample points along the circumference of each ring.

For each sample point, it checks if there is a valid NavMesh location nearby. If a valid point is found on the NavMesh, it is added to the list of candidates. This method effectively "probes" the walkable area around the agent at different distances.

A small amount of random jitter is added to the points to prevent all the samples from lining up perfectly, which helps in more complex or irregular environments. This provider does not generate a cover normal.

## Parameters

*   **Rings**: This is a setting on the provider asset itself. It determines how many concentric rings are generated.
    *   `1` ring will only sample points at the maximum `Search Radius`.
    *   `3` rings will sample points at 1/3, 2/3, and the full `Search Radius`.
*   **Search Radius** (from `HidingSettings`): Defines the radius of the largest, outermost ring.
*   **Candidates Per Provider** (from LOD Settings): This global setting is divided among the number of rings to determine how many sample points are generated for each circle. For example, if this is set to 30 and you have 3 rings, each ring will have 10 sample points.
*   **NavMesh Area Mask** (from `HidingSettings`): Restricts the search to specific types of NavMesh areas.

## Use Cases

*   **General Exploration**: This is an excellent general-purpose provider for when you want an AI to simply find *any* valid position, not necessarily one behind cover. It's great for AI that needs to reposition, flank, or just move around the environment.
*   **Combining with Other Providers**: This provider works very well when combined with more specific ones like `BehindObstacleProviderSO`. The `NavMeshRingProvider` can find open positions, while the other provider finds tight cover spots, giving the AI a good variety of choices.
*   **Finding "Fallback" Positions**: If no specific cover is found, this provider ensures the AI can still find a valid place to move to.

## Performance

The performance of this provider is directly tied to the number of sample points it generates. The total number of points is roughly equal to **`Rings` * (`Candidates Per Provider` / `Rings`)**, which simplifies to `Candidates Per Provider`.

Each sample point performs a `NavMesh.SamplePosition` call, which is generally efficient. However, a very high number of candidates can still add up. It is more expensive than the `CoverNodeProvider` but generally cheaper than physics-based providers like `BehindObstacleProviderSO`. Adjust the `Candidates Per Provider` setting to balance search density with performance.