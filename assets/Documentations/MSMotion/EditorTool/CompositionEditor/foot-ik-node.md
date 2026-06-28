# Foot IK Node

The **Foot IK Node** is a procedural constraint that aligns a character's feet to the terrain slope and height in real time, preventing hovering, clipping, and foot sliding. 

By analyzing the character's movement phase, the system automatically transitions limbs between free swing animation and locked ground contact.

---

## Capabilities and Real-Time Calibration

When active, the Foot IK solver performs several tasks:
* **Terrain Alignment**: Casts rays downward from the ankles and toes to detect slope normal orientations.
* **Auto-Calibration**: Automatically measures bone distances (e.g. ankle height from ground) in the character's rest pose to prevent floating feet.
* **Pelvis Drop**: Automatically pulls the hips down if the ground is too low, keeping the character grounded without popping joints.

---

## Inspector Parameter Reference

Configure the Foot IK properties in the details panel:

### Leg Configuration & Bones

* **Use Humanoid Bones**: Automatically identifies thigh, calf, ankle, and toe bones from the Animator, making the solver instantly compatible across humanoid characters.
* **Left/Right Leg Config**: If **Use Humanoid Bones** is disabled, manually specify the bone paths for:
  * **Hip Bone Path** (Thigh)
  * **Knee Bone Path** (Calf)
  * **Foot Bone Path** (Ankle)
  * **Toe Bone Path** (Foot tip)
  * **Knee Hint** (Transform target defining the leg's bending direction)

### Raycasting & Step Limits

* **Raycast Mask**: Selects which Physics layers represent the walkable ground.
* **Max Step Up / Max Step Down**: Height boundaries (in meters) representing the maximum terrain steps or drops the legs are allowed to resolve.
* **Foot Height Offset**: Fine-tune offset added to the auto-measured ankle height (positive values raise the foot).

### Pelvis Drop

* **Enable Pelvis Drop**: When active, pulls the character's hips down if a foot needs to stretch to reach the ground.
* **Pelvis Drop Weight**: Strength slider (0.0 to 1.0) governing hip adjustments.

### Settings & Limits

* **Foot Rotation Weight**: Controls how strongly the ankle rotates to match the terrain normal. A value of `1.0` matches the slope perfectly; `0.0` keeps the foot aligned to the animation curve.
* **Smooth Speed**: Controls the transition speed of height changes. Higher values make the feet snap quickly to steps; lower values smooth the vertical motion.
* **Soft IK Ratio**: Sets the ratio (0.80 to 1.00) at which the solver softens leg stretching to prevent knee "popping" near full extension. Recommended: `0.98`.

---

## Gait Phase & Foot Locking

The Foot IK solver uses state-of-the-art algorithms to separate stepping from standing:

### Gait Phase (Swing Control)
To prevent the solver from fighting walking or running animations while a leg is off the ground:
* **Enable Gait Phase**: Automatically dampens the IK weight while a foot is swinging forward.
* **Swing Velocity Threshold**: The vertical speed (meters per second) at which the system considers the foot to be airborne. Lower values make the swing detection engage sooner.
* **Gait Phase Blend Speed**: Speed at which swing damping engages and disengages.

### Foot Locking (Anti-Slide)
To eliminate foot sliding when a foot makes contact with the ground:
* **Enable Foot Locking**: When engaged, captures the foot's world coordinates at the moment of landing and freezes the ankle position in place. As the root body passes over, the foot remains locked to the coordinates.
* **Lock IK Threshold**: The minimum weight required before the foot lock can engage (prevents locking while airborne).
* **Unlock Velocity Threshold**: The upward velocity at which a locked foot is released to swing.
* **Lock Blend Speed**: Easing speed for engaging/disengaging the world coordinates lock.
