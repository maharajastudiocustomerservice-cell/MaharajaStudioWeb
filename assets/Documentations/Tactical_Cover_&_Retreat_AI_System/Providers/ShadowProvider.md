# Provider: Shadow Provider

**`ShadowProviderSO`** is a specialized provider that finds potential hiding spots by locating areas on the NavMesh that are currently in shadow.

## How It Works

This provider simulates how light and shadow work in the environment. It requires a reference to a dominant `Light` source in the scene (typically a Directional Light representing the sun).

For a number of sample points around the agent, it performs the following check:
1.  It finds a random, reachable point on the NavMesh within the `Search Radius`.
2.  It casts a ray from a position high above this point, aiming downwards along the direction of the dominant light.
3.  If this ray hits an object (on a layer specified by the `Occluder Mask`) before it reaches the ground point, it means the point is in shadow.
4.  Shadowed points that are on the NavMesh are added to the list of candidate hiding spots.

This provider does not generate a cover normal.

## Parameters

*   **Dominant Light**: A direct reference to the `Light` component that should be treated as the primary shadow-casting light source in the scene. If this is not assigned, the provider will try to find the first available `Light` component, but it is highly recommended to assign this manually for predictable behavior.
*   **Raycast Height Offset**: Determines how far above the sample point the shadow-checking raycast begins. This value should be large enough to ensure the ray starts above any potential geometry that could cast a shadow.
*   **Search Radius** (from `HidingSettings`): The radius around the agent in which to search for shadowed spots.
*   **Occluder Mask** (from `HidingSettings`): A physics layer mask that determines which objects are capable of casting shadows.
*   **Candidates Per Provider** (from LOD Settings): The number of random points to test for shadow coverage.

## Use Cases

*   **Light-and-Shadow Stealth**: This is the core provider for any game where stealth is based on hiding in the dark (e.g., *Thief*, *Splinter Cell*).
*   **Nocturnal or Light-Sensitive AI**: Perfect for creating creatures of the night, vampires, or other AI that are harmed by or actively avoid light.
*   **Ambiance and Believability**: Can be used subtly to make AI seem more intelligent, as they will appear to naturally use shadows to their advantage when approaching or hiding from the player.

## Performance

The performance cost of this provider is directly related to the **`Candidates Per Provider`** setting. Each candidate requires a `NavMesh.SamplePosition` call followed by a `Physics.Raycast`. This makes it one of the more computationally intensive providers, with a cost similar to `BehindObstacleProviderSO`.

For best performance:
*   Keep the `Candidates Per Provider` value as low as you can while still getting good results.
*   **Always** assign the `Dominant Light` reference manually to avoid the overhead of the system having to search for it.