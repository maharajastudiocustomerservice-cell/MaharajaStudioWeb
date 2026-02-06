# Providers Reference

This document contains a comprehensive reference for all Providers in the system.

## Standard Providers (V1)


---

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

---

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

---

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

---

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

---

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

---

# Provider: Hide Spot Provider (Base Class)
HideSpotProviderSO is not a functional provider itself. It is an abstract base class that serves as the template for all other provider assets.

## How It Works
The Hiding System is designed to be modular. Instead of having a single, monolithic way of finding hiding spots, it uses a collection of smaller, specialized `"providers."` Each provider is a ScriptableObject that knows one specific way to generate a list of potential hiding spots (candidates).

`The HideSpotProviderSO class defines the contract that every provider must follow. It contains a single abstract method:`
`public abstract void GenerateCandidates(in HidingContext ctx, List<CandidateInfo> results);`
*  **HidingContext ctx:** A struct containing all the information the provider might need, such as the agent's position, player locations, and system settings.
*  **List<CandidateInfo> results:** The list that the provider must add its generated candidate spots to.
By inheriting from this class, you can create your own custom logic for finding cover, which will seamlessly plug into the main hiding system alongside the built-in providers.

## Setup
`To create a new, custom provider:`
`Create a new C# script.`
`Make the class inherit from HideSpotProviderSO.`
Add the [CreateAssetMenu] attribute to allow you to create instances of it in the Unity Editor.
Implement the GenerateCandidates method with your custom logic for finding spots.
Create an instance of your new provider asset via the `Assets -> Create menu.`
Drag your new provider asset into the Providers array in your HidingSettingsSO.

## Use Cases
*  **System Extensibility:** The primary use is to allow developers to extend the hiding system with novel techniques for finding cover without modifying the core system code.
*  **Project-Specific Logic:** You can create providers tailored to the unique mechanics of your game. For example, a provider that finds hiding spots in magical portals, under brush, or in areas designated by a special trigger volume.

## Performance
As a base class, it has no performance impact. The performance of a provider is entirely dependent on the logic implemented in its GenerateCandidates method.

---

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

---

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

---

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

---

# Provider: Tactical Zone

`TacticalZoneProviderSO` is a provider that generates candidate hiding spots within specific, designer-placed volumes called `Tactical Zones.` This allows for a high degree of control over the AI's positioning, guiding it to use areas intended for specific tactical purposes.

## How It Works

This system requires designers to place TacticalZone components on GameObjects with colliders in the scene. Each zone is assigned a type (e.g., Overwatch, Ambush, Defensive).
The TacticalZoneProviderSO asset is configured to look for a specific TacticalZoneType. When it runs, it queries the central TacticalZoneRegistry to find all zones of that type within the agent's search radius.
For each matching zone, the provider generates a number of random points within the zone's collider bounds. It then finds the closest valid point on the NavMesh for each random sample. These valid NavMesh points become the candidate hiding spots.
This effectively lets a designer say, "When you are in a defensive state, find cover inside one of these designated defensive areas."

## Setup

1. `Create an empty GameObject in your scene to act as the zone.`
2. `Add a collider component (e.g., BoxCollider). Mark it as a Trigger.`
3. `Add the new TacticalZone component to this GameObject.`
4. `In the TacticalZone component, set the Zone Type to the desired tactical purpose (e.g., Defensive).`
5. `Adjust the size and position of the collider to cover the tactical area. A gizmo will show the zone's color and type in the Scene view.`
6. `Create an instance of the TacticalZoneProviderSO asset in your project files.`
7. `In the provider asset's Inspector, set the Target Zone Type to match the zones you want it to find.`
8. `Add this provider asset to the Providers list in your HidingSettingsSO.`

## Use Cases

*  **Designer-Controlled Encounters:** The primary use case. Force AI snipers to use sniper nests, or ensure ambushing enemies hide in designated ambush locations.
*  **Controlling Flow of Combat:** Guide the AI to fall back to specific, pre-defined defensive lines or to use flanking routes that you have explicitly laid out.

## Performance 

Since it only samples within a few known zones instead of the entire world, it can be more performant than wide-area environmental scanners if used correctly.

---

# Provider: Vertical Layer

**`VerticalLayerProviderSO`** generates candidate hiding spots on different vertical levels from the agent, making it ideal for multi-floor environments like buildings, canyons, or areas with catwalks.

## How It Works
This provider expands the search for cover into 3D space, allowing the AI to consider hiding spots above or below its current position.

*  **Define Layers:** It uses the agent's current position as a starting point and calculates the center points for layers above and below based on the Layer Height setting.
*  **Generate Points:** On each of these vertical layers, it generates a series of sample points in concentric rings, similar to the NavMeshRingProvider.
*  **NavMesh Validation:** For each sample point, it uses NavMesh.SamplePosition to find a valid, reachable location on the NavMesh. The search range for this check is limited to half the layer height to prevent it from finding spots on the wrong floor.
*  **Optional Cover Normal:** To add more intelligence, it performs a quick check for nearby cover by casting a ray from the valid NavMesh spot back towards the center of the layer. If it hits an occluder, it records the hit.normal as the coverNormal. If not, the spot is still added, but without cover information.

## Parameters
This provider's behavior is primarily controlled by its own settings.
*  **Layer Height:** The vertical distance between floors or layers. This should be set to match the typical floor height in your level architecture.
*  **Layers Above:** The number of floors to check above the agent's current position.
*  **Layers Below:** The number of floors to check below the agent's current position.
*  **Samples Per Ring:** The number of points to generate in each search ring on a given layer.
*  **Rings:** The number of concentric search rings to generate on each layer.
*  **Search Radius** (from HidingSettings): Controls the radius of the search rings on each layer.
*  **NavMesh Area Mask** (from HidingSettings): Ensures the spots are found on a valid NavMesh area.

## Use Cases
*  **Multi-Story Buildings:** The primary use case. It allows an AI on the ground floor to consider hiding on the second floor, and vice-versa.
*  **Environments with Verticality:** Excellent for levels with bridges, underpasses, catwalks, large staircases, or natural cliffs.
*  **Smarter Tactical Positioning:** Encourages AI to use height to its advantage, creating more dynamic and challenging combat or stealth encounters.

## Performance
The performance cost is directly related to the number of points it generates. The total number of candidates is (Layers Above + Layers Below) * Rings * Samples Per Ring. For each of these potential points, it performs a NavMesh.SamplePosition and a Physics.Raycast.

While very `effective`, it can become moderately expensive if the settings are high. It's recommended to balance the number of layers and samples with your performance budget. It can be a great addition to a high-quality LOD setting for when players are close.

---

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

## Advanced Providers (V2)


---

# Provider: Advance Cover

**`AdvanceCoverProviderSO`** is an offensive provider designed to generate hiding or cover points that facilitate forward movement towards a specific target or direction. It is the core component for "leapfrogging" or aggressive territory claiming behaviors.

## How It Works

This provider calculates a "Forward" vector using the following priority logic:
1.  **Direction to Last Known Enemy Position:** If the AI remembers where the player was, it prioritizes moving towards that memory.
2.  **Agent Forward:** If no target data exists, it uses the agent's current forward facing direction.

Once the direction is established, the provider generates candidate points within a defined cone (the `Search Angle`) along that vector. Unlike simple movement providers, this system explicitly checks for local cover availability:

1.  **Cone Sampling:** It casts random rays within the search angle.
2.  **Distance Randomization:** It selects a point between 50% and 100% of the `Advance Distance`. This ensures the AI makes significant progress and doesn't pick a spot just 1 meter away.
3.  **Obstacle Validation:** After sampling a valid NavMesh position, it performs a `Physics.CheckSphere` at that location. It only accepts the point if an obstacle is detected nearby (simulating "wall hugging" logic). This ensures the agent moves *to cover*, not just into the open.

## Parameters

* **Advance Distance**: The maximum distance forward the provider will search. The AI will try to move at least 50% of this distance.
* **Search Angle**: The width of the cone in degrees. A narrower angle forces a direct approach; a wider angle allows for diagonal advancement.

## Use Cases

* **Closing the Gap**: Ideal for melee units or shotgun wielders who need to move safely from cover to cover to get into effective range.
* **Leapfrogging**: When used by a squad, agents can take turns suppressing the enemy while others use this provider to advance to the next barricade.
* **Aggressive Patrols**: Allows an AI to push through a level while sticking to walls and obstacles rather than walking down the center of a corridor.

## Performance

**Moderate.** While the math for cone generation is cheap, this provider performs a `Physics.CheckSphere` for every generated candidate to ensure cover exists at the destination. While efficient for standard candidate counts (e.g., 10-20), setting the `Candidates Per Provider` count extremely high in your LOD settings may impact performance.

---

# Provider: Choke Point Finder

**`ChokePointProviderSO`** is a tactical provider designed to identify constricted areas in the environment, such as hallways, bridges, doorways, or narrow alleys. It is particularly useful for setting up ambushes or identifying defensible bottlenecks where enemy movement is restricted.

## How It Works

This provider scans the local environment to find points where the geometry constricts the NavMesh on opposing sides.

1.  **Random Sampling:** It first generates random points on the NavMesh within the `Search Radius`.
2.  **Constriction Check:** For each valid point, it performs a "star pattern" raycast check:
    * It casts rays to the Left and Right (X-axis relative to world).
    * It casts rays Forward and Backward (Z-axis relative to world).
3.  **Validation:** A point is considered a "Choke Point" if it detects obstacles on *both* opposing sides (e.g., Left AND Right or Forward AND Back) within the defined `Max Passage Width`.
4.  **Cover Normal:** If a choke point is found, the cover normal is set to `Vector3.up` (or generic), as the tactical value comes from the constriction itself rather than a specific cover face.

## Parameters

* **Max Passage Width**: The maximum width of a passage to be considered a choke point. Passages wider than this value will be ignored.
* **Wall Scan Range**: The distance rays are cast to detect walls, effectively derived from the passage width limit.

## Use Cases

* **Ambushes**: AI can identify choke points to place traps or wait for the player to pass through.
* **Defensive Holds**: A heavy unit might position itself in a narrow doorway to block player progress.
* **Grenade Targets**: AI can use this provider to find narrow areas to throw grenades into, knowing the player has limited movement options.

## Performance

**Moderate.** This provider performs 4 raycasts for every candidate point generated. While not as heavy as a full 360-degree scan, high `Candidates Per Provider` counts can add up. It is recommended to use this with a reasonable `Search Radius`.

---

# Provider: Corner Edges

**`CornerEdgeProviderSO`** is a high-fidelity "AAA" tactical provider that scans the environment to find the exact vertical edges of walls and obstacles. This allows AI agents to perform "Tactical Leaning" maneuvers, peeking around corners without fully exposing their bodies.

## How It Works

This provider performs a high-resolution angular sweep around the agent to detect geometric discontinuities.

1.  **Radial Scan:** It casts a series of rays in a 360-degree circle around the agent at chest height.
2.  **Edge Detection:** It identifies an edge when:
    * A ray hits an object, but the *next* ray does not (Transition from Hit -> Miss).
    * A ray does not hit, but the *next* ray does (Transition from Miss -> Hit).
    * The depth (distance) between two adjacent hits jumps significantly (e.g., a gap between two buildings or objects).
3.  **Corner Placement:** Once an edge is detected, it calculates a position slightly offset from the wall normal using the `Corner Offset` parameter. This places the candidate point just "behind" or "around" the corner.
4.  **Filtering:** It uses the NavMesh to ensure the point is walkable and applies a distance check to prevent stacking multiple points on the same corner.

## Parameters

* **Scan Resolution**: The number of rays to cast in the 360-degree circle (e.g., 64). Higher values provide more accurate corner detection but cost more performance.
* **Scan Range**: The maximum distance to check for walls.
* **Corner Offset**: How far the candidate point should be placed from the actual geometry corner (e.g., 0.6 meters behind the edge).
* **Edge Depth Sensitivity**: The distance difference required between two adjacent rays to consider them as hitting different objects.

## Use Cases

* **Tactical Peeking**: The primary use case. AI moves to the edge, leans out to shoot, and leans back in.
* **Urban Combat**: Essential for city environments with many building corners and alleyways.
* **Cover-to-Cover**: Allows AI to move from one building edge to another while minimizing exposure time.

## Performance

**Heavy.** This provider casts a large number of rays (`Scan Resolution`) every time it runs. It is recommended to use this provider selectively (e.g., only when near combat) or with a lower frequency/LOD setting compared to simpler providers.

---

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

---

# Provider: Pincer Formation

**`PincerFormationProviderSO`** is a cooperative squad provider. It generates candidate positions based on the location of *other* allies, naturally creating a surrounding "net" or pincer movement around the target without complex communication protocols.

## How It Works

This provider requires both a target and active allies (defined in the `TacticalAgent` component).

1.  **Ally Analysis:** It iterates through all known allies and calculates the vector from the **Target** to each **Ally**.
2.  **Average Direction:** It calculates the average direction from which the squad is currently engaging the target.
3.  **Inversion:** It inverts this average direction. This vector points to the "empty" side of the battlefield—the area least occupied by teammates.
4.  **Formation Generation:** It generates candidate points in a 60-degree arc around this "empty" vector at a specific `Engagement Distance`.

By picking points generated by this provider, the agent naturally fills the gaps in the squad's formation, leading to the target being surrounded.

## Parameters

* **Engagement Distance**: The distance from the target where the agent will attempt to hold formation.

## Use Cases

* **Boss Battles**: Ensures that minions or adds spread out evenly around the player rather than clustering in one spot (which makes them vulnerable to Area of Effect attacks).
* **Squad Tactics**: Useful for military AI to perform "Hammer and Anvil" tactics, where one group holds the front (using `OppositePlayersProvider` or `AdvanceCoverProvider`) and another group uses `PincerFormationProvider` to hit the exposed side.
* **Dynamic Spacing**: Automatically adjusts if allies die or move; the "average direction" shifts, causing the pincer point to rotate dynamically.

## Performance

**Good.** The cost is proportional to the number of active allies (linear complexity O(N)), followed by standard NavMesh sampling. For typical squad sizes (3-10 agents), the calculation overhead is negligible.

---

# Provider: Room Clearance (Pie Slicing)

**`RoomClearanceProviderSO`** is designed for Close Quarters Battle (CQB) scenarios. It generates a "fan" of points around a corner, allowing an AI to methodically "slice the pie"—gradually clearing a room from the outside before entering.

## How It Works

This provider combines edge detection with arc generation.

1.  **Corner Scan:** Similar to `CornerEdgeProvider`, it scans for depth discontinuities to identify corners within the `Scan Range` using a radial raycast sweep.
2.  **Arc Generation:** Once a corner is found, instead of placing a single point, it generates a series of points in a semi-circle (arc) around that corner.
3.  **Outward Facing:** The arc is oriented based on the corner's normal, ensuring the points fan out into the open space/room being cleared.
4.  **Visibility Check:** It performs a `Linecast` from the candidate point back to the corner to ensure the AI actually has a line of sight to the edge it is supposed to be clearing (prevents points spawning inside walls).

## Parameters

* **Scan Range**: The distance to scan for corners.
* **Ray Density**: The number of rays used to find the initial corners.
* **Stand Off Distance**: The distance from the corner where the AI will stand while clearing.
* **Points Per Corner**: How many points to generate in the "fan" for each detected corner.
* **Arc Angle**: The total angle of the fan (e.g., 90 degrees).

## Use Cases

* **Breach and Clear**: AI stacks up on a door, then uses these points to check the room's corners methodically.
* **Cautious Advance**: AI moves slowly around a blind corner, checking for threats at each step of the arc.
* **SWAT / Tactical Shooters**: Essential for realistic police or special forces behavior.

## Performance

**Heavy.** Like the Corner Edge provider, this relies on a radial scan plus additional calculations and linecasts for the arc generation. Use strictly for tactical phases (e.g., when `IsThreatened` is false but the AI is in "Search" mode).

---

# Provider: Squad Formation

**`SquadFormationProviderSO`** is a specialized provider that generates candidate points based on a strict tactical formation relative to a Squad Leader. It relies on the `SquadCoordinator` system to determine each agent's specific slot in the formation.

## How It Works

1.  **Leader Identification:** It queries the `SquadCoordinator` to find the leader of the agent's current squad. If the agent *is* the leader, or no leader exists, it runs the specified `Fallback Provider`.
2.  **Slot Calculation:** It determines the agent's index in the squad (e.g., Member 1, Member 2) and calculates the ideal local position offset based on the selected `Formation Shape` (Wedge, Line, File, etc.).
3.  **World Transformation:** It transforms this local offset into world space relative to the Leader's position and orientation.
    * *Note:* It can be configured to use either the Leader's body rotation or their velocity vector for orientation.
4.  **Jitter & Sampling:** It generates points around this ideal "slot" with a small amount of random jitter (Radius ~2.0f). This ensures that if the perfect formation spot is inside a wall, the AI can still find a valid NavMesh position nearby.

## Parameters

* **Shape**: The type of formation to use (`Wedge`, `Line`, `File`, `Diamond`, `Vee`).
* **Spacing**: The distance between agents in the formation.
* **Wedge Angle**: The angle of the formation (applicable for Wedge/Vee shapes).
* **Use Body Orientation**: If true, the formation rotates with the leader's body transform. If false, it rotates with their movement direction (velocity).
* **Fallback Provider**: The provider to use if the agent is the leader or not in a squad (usually a standard cover provider like `CoverProviderSO`).

## Use Cases

* **Military Squads**: Moving in a strict Wedge or File formation while patrolling.
* **Convoy Protection**: Agents moving in a Diamond formation around a VIP.
* **Organized Assault**: An entire squad advancing in a Line formation to maximize firepower.

## Performance

**Excellent.** The math for calculating formation offsets is trivial. The only cost is the standard NavMesh sampling for the candidate points. This is one of the cheapest providers available.

---

# Provider: Vantage Point

**`VantagePointProviderSO`** is designed to find positions that offer a height advantage, such as balconies, rooftops, or hilltops. It is essential for "Hunting" behaviors where the AI wants to acquire targets from a superior position.

## How It Works

This provider searches for NavMesh positions that are significantly higher than the agent's current location.

1.  **Biased Sampling:** It generates random search points but specifically biases the Y-coordinate upwards by adding a random value between `Min Height Advantage` and half the range.
2.  **Height Check:** It samples the NavMesh at these elevated coordinates. If a valid point is found, it verifies that the point's Y-position is indeed higher than the agent's current Y-position by the required amount.
3.  **View Check:** To ensure the high ground is actually useful (and not just a high shelf inside a closet), it casts a ray forward/down from the point. If the ray hits nothing for a short distance, it assumes the point has a clear view overlooking an area.

## Parameters

* **Min Height Advantage**: The minimum height difference required above the agent's current Y position for a point to be considered a vantage point.

## Use Cases

* **Snipers**: AI snipers will naturally seek out rooftops or towers using this provider.
* **Ambushers**: Melee units might wait on a ledge to drop down on the player.
* **Scouting**: A squad leader might move to high ground to get a better view of the battlefield.

## Performance

**Good.** It uses standard NavMesh sampling with a simple height check and one raycast per candidate. It is efficient enough for general use.


**➡️ Next: [Scorers Reference](Scorers-Reference.md)**
