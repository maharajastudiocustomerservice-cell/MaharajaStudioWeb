# Provider: Automatic Cover Finder
AutomaticCoverProviderSO is an intelligent provider that automatically finds cover spots without manual tagging by sampling the environment and verifying that hidden locations are actually concealed by a nearby obstacle.

## How It Works
This provider intelligently searches the area around the agent to find tactically sound cover positions. It operates in several steps:

*  **Sample Generation:** It generates sample points in a series of concentric rings around the agent's current position.
*  **NavMesh Validation:** For each sample point, it finds the closest valid location on the NavMesh to ensure the agent can reach it.
*  **Visibility Check:** It then performs a critical check to see if the NavMesh point is visible to any player. If it has a clear line of sight to a player, the point is discarded as it is not "`in cover.`"
*  **Cover Verification:** If the point is hidden, the provider performs a final, crucial verification. It casts a ray from the hidden spot towards the nearest player. If this ray hits a nearby object (on the `Occluder Mask layer`), it confirms that there is a physical obstacle providing the cover.
*  **Candidate Creation:** If all checks pass, the point is added as a valid candidate. Importantly, it also records the normal of the obstacle's surface that was hit. This `coverNormal` (the direction pointing away from the cover) is invaluable information for advanced scoring and the peeking system.

## Parameters
This provider has its own specific settings and also uses global settings from your HidingSettings asset.
*  **Rings:** The number of concentric rings to sample around the agent. More rings mean a wider and more thorough search.
*  **Max Cover Distance:** The maximum distance from the hidden sample point that the provider will check for a wall or obstacle. This prevents the AI from thinking it's in cover when it's just hidden in an open field far from any object.
*  **Search Radius (from HidingSettings):** Defines the maximum radius of the outermost search ring.
*  **Occluder Mask (from HidingSettings):** A layer mask that determines which objects are considered valid cover obstacles.
*  **Candidates Per Provider** `(from LOD Settings)`: Determines how many sample points are generated per ring.

## Use Cases
*  **Dynamic Environments:** Perfect for levels where cover positions can change or are not known in advance, such as procedural worlds or maps with destructible environments.
*  **Reducing Design Workload:** A powerful "set it and forget it" provider that removes the need for designers to manually place hundreds of cover nodes.
*  **High-Fidelity AI:** Because it verifies cover and provides a surface normal, it enables more advanced behaviors like peeking and directional cover scoring, leading to more believable AI.

## Performance
This is one of the more computationally intensive providers due to its multi-step verification process. For each potential candidate, it performs:
`NavMesh.SamplePosition`
`IVisibilityService.AnyPlayerHasLineOfSight` (which involves raycasts)
An additional Physics.Raycast to verify the cover
The total performance cost scales with the `Rings` and `Candidates` Per Provider settings. While extremely effective, it should be used with care, especially if you have many AI agents searching `simultaneously`. Consider lowering the candidate count in higher-level `LOD settings`.