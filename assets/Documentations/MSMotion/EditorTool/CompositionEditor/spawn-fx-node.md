# Spawn FX Node

The **Spawn FX Node** instantiates a custom GameObject prefab at a specified socket target. This is useful for temporary props (like drawing a sword, spawning a shield, dropping a footstep dust-cloud decal, or shooting a projectile model).

---

## Inspector Parameter Reference

Configure the Spawn FX properties in the details panel:

### Spawning & Pooling Settings

* **Prefab**: The Unity GameObject prefab asset spawned by this node.
* **Attach to Bone**: If checked, parents the spawned prefab GameObject directly under the target socket bone. If unchecked, the object spawns in the world at the bone's coordinates but does not follow its movements.
* **Destroy on End**: If checked, the spawned GameObject is automatically destroyed as soon as the timeline block ends. If unchecked, the object persists in the scene.
* **Use Pool**: When enabled, the runtime system utilizes an object pooling manager rather than performing expensive `Instantiate` and `Destroy` operations.
  * *Workflow Tip:* Always enable **Use Pool** for frequent visual effects (like weapon impact sparks or footprint decals) to maintain smooth frame rates.

---

## Scale Transitions

You can fade the spawned GameObject's scale in and out dynamically over the block's timeline range:

* **Use Scale Transition In / Out**: Enables animating scale using custom curves.
  * **Scale Transition In / Out Curve**: Easing curves driving scale (Y-axis = size scale factor, X-axis = normalized time).

---

## Trajectory Spline Path

* **Trajectory**: Expand this foldout to configure a Bezier spline path. You can define control points to make the spawned object travel along a specified vector path relative to the character (e.g. throwing a weapon prop that flies forward along a curved Bezier arc).
* For details on how to generate, edit, and manipulate these spline paths, see the [FX Path Tools Scene Panel](fx-nodes-overview.md#fx-path-tools-scene-panel) section of the FX Nodes Overview.

