# VFX Graph FX Node

The **VFX Graph FX Node** triggers visual effects authored with Unity's Visual Effect Graph (VFX Graph). It provides controls for parameter bindings and spawning offsets.

---

## Inspector Parameter Reference

Configure the VFX Graph FX properties in the details panel:

### Asset & Attachment Settings

* **VFX Asset**: The Unity Visual Effect Graph asset to trigger.
* **Attach to Bone**: If checked, parents the instantiated VFX GameObject directly under the target socket bone.
* **Stop at Duration End**: If checked, halts the VFX system or destroys its instance as soon as the timeline block ends. If unchecked, the effect plays until its natural system completion (even if it exceeds the block bounds).

### Parameter Bindings & Overrides

* **Parameter Overrides**: A list of property bindings. You can target specific properties inside the visual effect asset (such as float parameters, integers, or color variables) and override their values directly from this slot without modifying the master asset.

---

## Property and Scale Transitions

To fade or scale effects dynamically, you can automate values using curves:

### Easing a VFX Property
You can bind a float property inside the VFX Graph to be driven by timeline transition times:
* **Transition Property Name**: Enter the exact string name of the float parameter inside the VFX Graph (e.g. `SpawnRate` or `Intensity`).
* **Use Property Transition In / Out**: Enables driving the named property using custom Animation Curves.
  * **Property Transition In / Out Curve**: Easing curves (Y-axis = parameter value, X-axis = normalized time).

### Easing VFX Local Scale
* **Use Scale Transition In / Out**: Enables automating the visual effect's transform size.
  * **Scale Transition In / Out Curve**: Easing curves driving local scale size (Y-axis = size scale factor, X-axis = normalized time).

---

## Trajectory Spline Path

* **Trajectory**: Expand this foldout to configure a Bezier spline path. You can define control points to make the VFX Graph system travel along a specified vector path relative to the character (e.g. firing a plasma projectile that flies forward along a curved Bezier arc).
* For details on how to generate, edit, and manipulate these spline paths, see the [FX Path Tools Scene Panel](fx-nodes-overview.md#fx-path-tools-scene-panel) section of the FX Nodes Overview.

