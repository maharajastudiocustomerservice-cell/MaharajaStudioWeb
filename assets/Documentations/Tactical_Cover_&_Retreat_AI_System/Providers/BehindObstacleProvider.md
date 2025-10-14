# Provider: Behind Obstacle

**`BehindObstacleProviderSO`** is a provider that finds potential hiding spots by looking for locations directly behind environmental obstacles, relative to the agent's position.

## How It Works

This provider operates by casting a series of rays outward from the agent's current position in a 360-degree circle. When a ray hits an object on a layer specified by the `Occluder Mask` (in your `HidingSettings`), the provider then calculates a point a short distance behind that obstacle.

It then checks if this calculated point is on a valid NavMesh area. If it is, the point is added to the list of potential hiding spots.

A key feature of this provider is that it also stores the **normal** of the surface it hit. This information can be used by certain scorers (like the `DefensivePositionScorerSO`) and by the system's built-in peeking logic to evaluate not just the position, but also the quality and direction of the cover.

## Parameters

This provider's behavior is controlled by the global settings in your `HidingSettings` asset.

*   **Search Radius**: Defines how far the rays are cast from the agent to look for obstacles. A larger radius means the AI will consider cover that is farther away.
*   **Occluder Mask**: A physics layer mask that determines which objects are considered valid obstacles (e.g., walls, large props).
*   **NavMesh Area Mask**: Defines which NavMesh areas are considered valid for hiding spots.
*   **Candidates Per Provider** (from LOD Settings): Controls the number of rays cast in the 360-degree circle. A higher number increases the search density and the likelihood of finding small pieces of cover, but it also increases the performance cost.

## Use Cases

*   **Classic Stealth**: This is a fundamental provider for any stealth scenario where you want AI to hide behind walls, crates, pillars, or other large objects.
*   **Dynamic Cover Finding**: Excellent for situations where the environment is not explicitly marked up with cover points. The AI will dynamically find cover based on the physical geometry of the level.

## Performance

The performance cost of this provider is directly related to the **Candidates Per Provider** setting. Each candidate results in a `Physics.Raycast` call. While generally efficient, using a very high number of candidates on many agents simultaneously could impact performance. Adjust this setting based on your target platform and game's needs.