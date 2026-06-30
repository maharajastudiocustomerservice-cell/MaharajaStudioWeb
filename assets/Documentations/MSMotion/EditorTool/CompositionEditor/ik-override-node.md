# IK Override Node

An **IK Override Node** is a timeline block that modulates limb positioning using Inverse Kinematics (IK) over a set time range. It allows you to overlay custom hand/foot placements, joint targets, and posture adjustments on top of base animation clips.

Unlike motion nodes that contain actual clip curves, the IK Override Node is a timing envelope that blends active IK solvers on and off the preview character.

---

## Capabilities and Visual Handles

When you place an IK Override Node on a layer and select it, it interfaces with the character's IK rig. 

* **Scene View Handles**: Visual manipulators appear in the Scene view at the positions of the configured IK targets (e.g. left hand, right hand, left foot, right foot). You can drag these handles directly to pose the character.
* **Transition Blending**: Timing sliders allow you to fade the IK solver influence in and out, smoothly capturing the limbs from the animation state, locking them to your target coordinates, and then releasing them back to the animation curves.

---

## Inspector Parameter Reference

When you select an IK Override Node, the following parameters are available in the Inspector/Details panel:

### Timing & Transitions

* **Start Time**: The timestamp (in seconds) on the timeline when the IK override begins blending in.
* **Duration**: The length of time the IK solver remains active.
* **Transition In Duration**: The duration (in seconds) over which the limbs transition from their animated positions to the IK target positions.
* **Transition Out Duration**: The duration (in seconds) over which the limbs transition from the IK target positions back to their animated coordinates.
* **Transition Curve**: The mathematical easing curve (**Linear**, **EaseIn**, **EaseOut**, **EaseInOut**, or **Smooth**) driving the fade.

### Weights & Automations

* **Use Weight Curve**: Enables using an Animation Curve to drive the IK solver's global influence dynamically over the node's duration.
* **Weight Curve**: A keyframed curve where the Y-axis represents influence (0.0 to 1.0) and the X-axis represents normalized duration. Use this to create complex pulsing, fading, or scaling IK strengths.

### Masking & Blending Options

* **Apply Root Motion**: A toggle to project the solver's root modifications back onto the character's root trajectory.
* **Preserve Transform**: A toggle to lock the limb's world-space position relative to the moving root, keeping the limb locked in place relative to the character's body coordinates.
* **Slot Mask**: A specific AvatarMask that restricts which parts of the skeleton are affected by this node. Leaving this blank defaults to the parent layer's mask.

---

## Timeline Keyframe Authoring & Path Tools

An IK Override Node functions as a path modifier. You can author multi-point trajectories for effectors directly in the Scene View using the floating **MSMotion IK Tools** HUD overlay. 

When you select a keyframe node in the Scene View, the HUD panel displays the **Node Details & Tools** foldout with the following controls:

### Timing & Operations
* **Local Time**: Sets the selected keyframe's normalized time (0.0 to 1.0) relative to the start and end of the timeline block.
* **Global Time**: Adjusts the keyframe's location on the main timeline ruler (in seconds).
* **Add Node**: Inserts a new keyframe node immediately following the selected node, or appends a new node at the end of the trajectory.
* **Remove Node**: Deletes the selected keyframes (the spline requires at least two nodes to remain valid).

### Snapping Tools
* **Align Rotation to Normal**: Toggles whether rotation snapping aligns the effector orientation to match the slope angles of terrain/meshes.
* **Effector to Ground**: Raycasts downwards from the effector coordinates and snaps the target position directly to the ground surface.
* **Pole to Ground**: Snaps the knee/elbow pole-vector target directly to the ground surface.
* **Effector to Cursor (Mesh)**: Performs a viewport raycast and places the selected effector at the exact mesh surface point directly under your mouse pointer.
* **Snap to Transform (Path Tools)**: Assign a Scene transform target and click **Snap** to shift the keyframe node coordinates to that object's bounding center.
* **Reset Nodes to FK Pose**: Rebinds all keyframe coordinates to match the underlying base Forward Kinematics (FK) animation values.

### Path Transformations
* **Mirror X (World)**: Flips the coordinates of the selected nodes along the world origin X-axis.
* **Mirror X (Root)**: Flips the selected nodes along the character's root position, ideal for mirroring hand/foot paths from left to right.
* **Reverse Path Time**: Flips the normalized timeline coordinates of the path nodes, reversing the execution order.
* **Bake FK to IK Path**: Samples the base animation over the node's duration and records the joint paths into a series of keyframe nodes. Adjust the **Nodes** slider to increase or decrease the sample resolution.

---

## Advanced IK Locks

IK Locks allow you to pin multiple joints (e.g., both hands or feet) to specific world-space coordinates while the rest of the body continues to animate dynamically. 

Under the **IK Locks** tab in the IK Override Node:
* Click **+ Add IK Lock** to attach a new lock modifier.
* **Target Bone**: Choose the bone to freeze in place.
* **Lock Position/Rotation**: Check to freeze translation, rotation, or both.
* **World Space Constraints**: You can provide a specific transform target to stick the limb to an object during the override duration.

---


## Squash & Stretch and Joint Scale Overrides

For advanced stylized animations, character rigs can utilize squash and stretch behaviors dynamically. The IK Override Node allows you to configure scale multipliers visually or customize joints per keyframe:

### Interactive Scale Handles
If a selected chain is configured to allow stretching (see [IK Rig Configuration](ik-rig-configuration.md)), selecting a single keyframe node in the Scene View displays a **light-blue cone scale handle** at the effector position. 
* Drag this handle in the viewport to scale the **Stretch Scale** multiplier of that keyframe.
* Dragging outwards stretches the bone joints (values >1.0), while pushing inwards squashes them (values <1.0).

### Squash & Stretch Overrides
Under the **Squash & Stretch Overrides** section in the Scene View HUD, enable the **Override Structural Settings** checkbox to override the global rig defaults for the selected keyframe:
* **Allow Stretch**: Enables or disables the joint scaling calculations.
* **Stretch Limit**: Sets the maximum length multiplier the joints can extend (e.g. `1.5` caps elongation at 150%).
* **Stretch Axis**: Sets the scaling direction (choose between **Uniform**, **X**, **Y**, or **Z** axes).
* **Preserve Volume**: When enabled, automatically thins or widens the joint geometry as it stretches/squashes to maintain a constant physical mass volume.
* **Compensate Parent Scale**: Negates parent bone scaling factors so that child bones do not inherit unwanted skewing.

### Joint Scale Overrides
Under the **Override Joint Scales** checkbox in the HUD, you can configure manual scaling factors for each individual joint in the IK chain (e.g., shoulder, elbow, wrist):
* Select **Override Joint Scales** to display a list of the chain's bones.
* Edit the **Vector3 Fields** (X, Y, Z scale factors) for each bone to customize their dimensions at the selected keyframe. The solver automatically interpolates scale transitions smoothly between keyframes.

