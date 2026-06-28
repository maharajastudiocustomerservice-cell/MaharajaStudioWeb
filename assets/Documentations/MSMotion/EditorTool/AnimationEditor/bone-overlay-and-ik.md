# Bone Overlay & IK/FK Solver

Posing characters by navigating hierarchical bone structures can be tedious. The Animation Editor features a visual **Bone Overlay** and an interactive **IK/FK Solver** to pose models directly in the Scene view.

---

## The Viewport Bone Overlay

The **Viewport** panel in the sidebar overlays a visual skeleton on top of your character in the Scene view, making it easy to see joint relationships and identify animated parts:

### Overlay Toggles
* **Show Bones**: Draws the character's skeleton in the Scene view.
* **Animated Bones Only**: Hides non-animated bones, drawing only the bone paths that have active keyframes in the loaded clip.
* **Bone Names**: Draws text labels next to the joints in the viewport.

### Visual Configurations (⚙ Settings Window)
You can customize the appearance of the bone wireframe:
* **Bone Shape**: Choose between wire **Lines**, **Diamonds**, or **Boxes**.
* **Bone Size & Width**: Scale sliders to match different character sizes (e.g. tiny creatures vs. giants).
* **Color Schemes**: Distinct colors for standard bones, animated bones, and currently selected bones.

### Viewport Action Buttons
* **Focus Root**: Frames the Scene view camera directly onto the character.
* **Use Selected Bone**: Select a bone transform in the Scene view, then click this button. The editor will automatically locate that bone's animation curves in the Curves panel and filter the timeline to show only that bone's tracks.

---

## IK / FK Solver Integration

The editor includes a real-time edit-mode Inverse Kinematics (IK) rig solver that runs inside the Scene view, allowing you to drag end-effectors (like hands or feet) and have the limb joints bend naturally:

### Visualizing IK Handles
When an IK rig is assigned in the **IK / FK Solver** sidebar panel, colored handle markers appear in the Scene view at the active IK targets:
* **Posing limbs**: Click and drag an IK target handle (e.g., a hand control circle) in the Scene view. The elbow and shoulder joints bend in real time to follow your hand.
* **Stable Pole Vectors**: Limbs bend consistently based on pole vector configurations.
* **Procedural Scales**: The solver supports stretch-and-scale calculations, automatically adjusting bone lengths if the target is pulled beyond the limb's reach.

---

## IK Auto-Keying Workflow

To prevent drag latency and handle loss, the editor handles pose calculations in two distinct steps:
1. **Interactive Dragging**: While dragging a handle, the character's limbs adjust visually in real time. The editor does **not** write keyframes mid-drag.
2. **Keyframe Baking**: When you release the mouse button, the solver calculates the final rotation and position values for all bones in the limb chain. If **Auto-Key** is enabled, it bakes these solved values as keys into the animation clip at the current playhead frame.

> [!TIP]
> Use **Offset Mode** in combination with IK dragging. If you drag the hand handle with Offset Mode active, the entire arm's animation path will shift by that offset across the entire clip length, allowing you to easily adjust weapon aiming heights or walking stances.
