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