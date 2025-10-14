# Provider: Opposite Players Direction

**`OppositePlayersProviderSO`** is a provider designed to find hiding spots that are located in the general direction *away* from the player or players.

## How It Works

This provider first determines the average direction from the AI agent to all known player positions. It then inverts this vector to get a primary direction that points directly away from the threat.

It then generates a number of candidate points along this "away" vector, at various distances up to the `Search Radius`. A small amount of random jitter is added to each point to spread the candidates out and prevent them from all falling on a single line, allowing for more flexible positioning.

Finally, each candidate point is checked to ensure it's on a valid NavMesh area before being added to the list of potential spots. This provider does not generate a cover normal.

## Parameters

This provider's behavior is controlled by the global settings in your `HidingSettings` asset.

*   **Search Radius**: Defines the maximum distance the provider will look for spots along the "away" vector.
*   **Candidates Per Provider** (from LOD Settings): Controls how many sample points are generated. More candidates will create a denser search pattern in the "away" direction.
*   **NavMesh Area Mask**: Restricts the search to specific types of NavMesh areas.

## Use Cases

*   **Retreating and Kiting**: This is the ideal provider for AI that needs to create distance from a threat. It's perfect for ranged characters who want to kite their enemies, or for "cowardly" AI that tries to flee from combat.
*   **Strategic Repositioning**: When an AI is in a bad spot, this provider can help it find a safer location that is generally farther away from the player, forcing the player to close the distance again.
*   **Breaking Line of Sight**: While it doesn't explicitly check for line of sight, by moving in the opposite direction of a player, the AI naturally increases its chances of putting obstacles between itself and the player.

## Performance

The performance of this provider is very good. Its cost is directly proportional to the **`Candidates Per Provider`** setting, as each candidate requires a `NavMesh.SamplePosition` call. It does not perform any expensive physics raycasts, making it significantly cheaper than providers like `BehindObstacleProviderSO`. It is a lightweight and effective way to generate directional movement.