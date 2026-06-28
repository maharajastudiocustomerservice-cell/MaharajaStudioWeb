# Transform FX Node

The **Transform FX Node** dynamically alters the position, rotation, or scale of a target bone or socket transform. It is commonly used for procedurally scaling weapon models, offsetting limb coordinates during climbs, or twisting attachments dynamically without modifying the underlying clip assets.

---

## Inspector Parameter Reference

Configure the Transform FX properties in the details panel:

### Drive Targets

You can selectively toggle which components of the target bone's transform are modified:
* **Drive Position**: Toggles modifying the bone position.
  * **Target Local Position**: A static offset vector.
  * **Position Curves (X, Y, Z)**: Keyframed curves to animate position coordinates over time.
* **Drive Rotation**: Toggles modifying the bone rotation.
  * **Target Local Euler**: A static rotation offset (Euler angles).
  * **Rotation Curves (X, Y, Z)**: Keyframed curves to animate rotation angles over time.
* **Drive Scale**: Toggles modifying the bone scale.
  * **Target Local Scale**: A static scale multiplier (default: `1, 1, 1`).
  * **Scale Curves (X, Y, Z)**: Keyframed curves to animate scale factors over time.

### Space & Mode Settings

* **Mode**:
  * **Snap**: Instantly overwrites the target bone's coordinates to match the defined offsets at the trigger start.
  * **Interpolate**: Blends coordinates over the node's duration.
* **World Space**: If checked, coordinates are processed in world space relative to the scene root. If unchecked, offsets are calculated relative to the parent bone's local coordinate system.
* **Preserve Previous Transform**: If checked, the target bone preserves its final overridden transform state when the timeline block ends (preventing the bone from snapping back to its original clip position).

---

## Transition Blending

To prevent sudden bone pops, you can automate easing transitions:

* **Use Position Transition In / Out**: Enables position blending curves.
* **Use Rotation Transition In / Out**: Enables rotation blending curves.
* **Use Scale Transition In / Out**: Enables scale blending curves.
  * *Curves:* Each enabled transition features a curve driving target weight (Y-axis = influence multiplier, X-axis = normalized time).
