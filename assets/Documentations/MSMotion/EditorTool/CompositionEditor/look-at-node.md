# Look-At Constraint Node

The **Look-At Constraint Node** forces a character's spine, head, and eyes to track and look at one or more targets in 3D space. This is essential for character focus, conversation behaviors, and combat aiming.

---

## Visual Scene View Handles

When you select a Look-At node, a visual crosshair handle representing the look-at target appears in the Scene View. Dragging this handle moves the target position dynamically, causing the character to twist their spine and head to follow in real time.

---

## Inspector Parameter Reference

The Look-At Constraint properties are configured via the details panel:

### Target Selection

You can configure targets in the **Targets** list. If multiple targets are active, the look-at direction is computed as a weighted average.

* **Target Mode**:
  * **Transform**: Follows a specific Unity Transform GameObject assigned from the scene.
  * **FX Event**: Dynamic tracking that locks onto a temporary object spawned by an FX node (such as a launched projectile or a spawned prop).
  * **Local Offset**: Follows a coordinate offset relative to the character (e.g. looking straight ahead by 5 meters).
* **Weight**: Individual target weights (0.0 to 1.0) to mix influences.
* **Local Offset**: Offset coordinates added to the target transform.

### Bones & Weights

* **Use Humanoid Bones**: When enabled, the system automatically detects head, spine, and eye bones from the character's Humanoid Animator, making the node reusable across different skeletons.
* **Head Bone Path / Spine Base Bone Path**: Fields to manually assign bone paths if not using humanoid structures.
* **Head Weight**: Sets how much of the rotation is applied to the neck and head (0.0 = none, 1.0 = full focus).
* **Spine Weight**: Sets how much of the rotation is absorbed by the spine (0.0 = rigid spine, 1.0 = deep body twist).

### Eye Tracking & Biological Jitter

* **Left Eye Bone Path / Right Eye Bone Path**: Fields to assign eye bones.
* **Eyes Weight**: Controls the focus strength of the eye bones (0.0 = dead gaze, 1.0 = direct focus).
* **Saccade Jitter**: Simulates biological eye movement by injecting minor, high-frequency micro-jitter into the eyes' tracking vector (0.0 = static gaze, 1.0 = high biological eye activity).

### Limits & Easing Speed

* **Max Angle**: The absolute rotation boundary (0 to 180 degrees) the character is allowed to twist. If the target exceeds this angle, the constraint will clamp.
* **Soft Limit Angle**: Eases and slows down head turning as the target approaches the **Max Angle**, preventing visual popping. Set to 0 to disable.
* **Smooth Speed**: The tracking acceleration. Lower values create sluggish, heavy-head rotations, while higher values create snap reactions.
* **Forward Axis / Up Axis**: Coordinate mapping dropdowns (**Z**, **Y**, **X**, or negative options) to match the head bone's local forward alignment. Typically, this is **Z** forward and **Y** up.
