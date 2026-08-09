# Dynamic Bone Subdivision (DBS) (Exp)

> [!WARNING]
> The DBS system is currently an experimental feature and its API or behavior is subject to change in future releases.

The **Dynamic Bone Subdivision (DBS)** system allows you to create fluid, snake-like, or elongated movements for existing bones without requiring the source rig to have those extra bones authored.

This is a powerful tool for generating stylized animations like a "long neck" horror character, a stretchy arm, or a flowing tail, while fully preserving the mesh integrity of the character.

## How it Works

The system operates in two phases: **Authoring/Baking** (in the Editor) and **Playback** (at Runtime).

### 1. Editor / Baking (Composition Window)

1. Open a composition and add a **Bone Subdivision** slot to any layer.
2. Define the source bones (e.g., `Spine` -> `Chest` -> `Neck`).
3. Set the subdivision density (either fixed count or spatial density).
4. Configure the weight falloff curve (how skin influence distributes across the virtual bones).

During preview, the system dynamically inserts **virtual bones** into the scene and solves their positions using a high-performance FABRIK algorithm. When you **export** the composition, the virtual bone positions and rotations are baked directly into the output `.anim` clip, and a lightweight `SubdividedChainMetadata` sub-asset is embedded alongside it.

#### Dummy Bones and Smart Child Propagation
When a bone is subdivided, its mesh weights are completely transferred to the newly created virtual bones. The original bone becomes a "dummy" bone (temporarily renamed with a `[DUMMY]` prefix in the editor).
- **Smart Re-parenting:** The system automatically analyzes any children of the subdivided bones. 
  - If a child (like a `Head` attached to a `Neck`) is physically located at the tip of the bone, it is automatically re-parented to the end of the virtual chain.
  - If a child (like a `ShoulderPad`) is located at the base of the bone, it remains attached to the base of the virtual chain.
- **Tip Rotation Preservation:** The solver uses a minimal-arc `FromToRotation` to orient the virtual bones, guaranteeing that children at the tip maintain their exact local axes and do not twist unexpectedly.

*Note: If you want to manually animate a bone (e.g., rotating the head), do **not** include it in the source bone list. Subdivide the bones leading up to it (e.g., the Neck), and the Head will seamlessly ride on the tip of the subdivided chain while retaining its original weights and animatability.*

### 2. Runtime Playback

The runtime playback is extremely lightweight because it does **not** run the IK/FABRIK solver.

1. Add the `SubdividedChainApplicator` component to your character (next to the `Animator`).
2. The component automatically detects the active `SubdividedChainMetadata` from the playing clip.
3. It reconstructs the virtual bone hierarchy and seamlessly restores the smart child propagation.
4. In `LateUpdate`, it samples the baked curves from the animation clip and drives the virtual bones.

#### Additive Blending

The `SubdividedChainApplicator` includes a `BlendWeight` property (0.0 to 1.0). 
- At `1.0`, the virtual bones follow the baked DBS curves perfectly.
- At `0.0`, they revert to their original bind pose (matching the non-DBS animation).
- You can cross-fade this value (using `FadeIn()` and `FadeOut()` coroutines) to smoothly transition a character into or out of a subdivided state.

## Mesh Preservation (Skin Weight Redistribution)

To ensure the mesh doesn't distort or tear, the `SkinWeightRedistributor` dynamically creates a copy of your `SkinnedMeshRenderer`'s `sharedMesh` at export time. It intelligently extracts the top 4 most significant bone influences after redistribution to bypass Unity's strict vertex buffer format limitations, ensuring perfect stability. 

This happens entirely automatically during the bake process and does not permanently modify your original mesh assets.
