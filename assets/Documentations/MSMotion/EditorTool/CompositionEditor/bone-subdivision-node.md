# Bone Subdivision Node (Exp)

> [!WARNING]
> The Bone Subdivision node is currently an experimental feature and is subject to change.

The **Bone Subdivision** node allows you to dynamically divide existing bones into multiple virtual segments. This is useful for creating flexible, bendy, or elongated motions (like a stretchy neck or tentacle) without requiring the original rig to be authored with dozens of bones. 

At export time, the mesh weights are automatically redistributed, and the virtual bones are baked into the resulting animation clip.

## Adding the Node

To add this node to your composition:
1. Open the **Composition Editor**.
2. Right-click on any layer track in the timeline.
3. Select **Constraints → Bone Subdivision (Exp)**.

Once added, select the node in the timeline to view and configure its settings in the Details panel.

## Node Settings

The Bone Subdivision node can be authored entirely inline (within the composition timeline) or via a reusable **Descriptor Asset** if you want to share the exact same configuration across multiple animations.

### General Configuration

- **Descriptor Asset:** (Optional) Drag a `MSMotionBoneSubdivisionDescriptor` ScriptableObject here. If assigned, the node will use the asset's settings and ignore the inline settings below. This is highly recommended for maintaining consistency across multiple animations.
- **Config Label:** A custom, human-readable name for this node's configuration (e.g., "Bendy Neck Setup").

### Chain Topology

- **Subdivision Mode:** Determines how the system decides how many virtual bones to create:
  - **Fixed Count:** Creates an exact, set number of virtual bones per source bone.
  - **Density:** Creates virtual bones dynamically based on the physical length of the source bone, ensuring a consistent spatial resolution regardless of how long the bone is stretched.
- **Subdivisions Per Bone:** (Only active if Mode is *Fixed Count*). The exact number of virtual bones to inject into each source bone.
- **Bone Spacing (cm):** (Only active if Mode is *Density*). The physical spacing between each virtual bone in centimetres.

### Deformation & Weighting

- **Weight Falloff Curve:** Defines how the original bone's skin weights are distributed across the newly created virtual bones. 
  - The **X-axis** represents the position along the virtual chain (0 = root of the chain, 1 = tip of the chain).
  - The **Y-axis** represents the relative influence or weight.
  - A linear curve (`0,1` to `1,1`) is typical for an even distribution.
- **Preserve Volume:** If enabled, the system automatically applies perpendicular scale compensation when the chain stretches, maintaining the character's volume and preventing unwanted "ballooning" or thinning artifacts.

### Source Bones

- **Source Bone Chain:** A list of bones to subdivide, ordered from Root to Tip (e.g., `Spine` → `Chest` → `Neck`).
  - **For Humanoid Rigs:** Use the dropdown to select the `HumanBodyBones` mapping (e.g., `Neck`).
  - **For Generic Rigs:** Leave the dropdown as `LastBone` and manually type the transform hierarchy path into the string field.
  
*Note: Do not include terminal bones you want to manually animate (like the `Head`) in this list. If you subdivide a bone, it becomes a dummy and loses its weights. Subdivide the `Neck` instead, and the `Head` will seamlessly ride on top of the bendy neck.*

### Advanced / Solver Settings

- **Propagated Tip Children:** Explicitly forces specific child bones to detach from the source bone and re-attach to the very tip of the subdivided chain. 
  - *Note: The system now features **Smart Auto-Propagation** which automatically measures distance and re-parents tip-based children (like the head or eyes) to the tip, and base-based children (like shoulder pads) to the base. This list is mostly retained for legacy support or highly specific manual overrides.*
- **FABRIK Iterations:** The maximum number of solver iterations allowed per frame. Higher values yield more accurate IK solving at the cost of performance. Default is usually sufficient.
- **FABRIK Tolerance:** The distance threshold (in metres) at which the solver stops iterating. Smaller values are more accurate but require more iterations.

