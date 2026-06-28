# Troubleshooting

This guide addresses common issues encountered when using the Animation Editor and provides steps to resolve them.

---

## Common Issues & Solutions

### 1. "Cannot edit keys: The clip is read-only..."
* **Symptoms**: Red error warning in the status area; keyframe fields are locked; transforms in the Scene view snap back instantly.
* **Cause**: The loaded animation clip is embedded inside an imported 3D model file (such as `.fbx`), which Unity treats as write-protected.
* **Solution**: In the sidebar's **Clip** panel, click **Extract Editable Copy**. This will duplicate the animation into a writeable `.anim` file and load it automatically.

### 2. Character does not update when dragging the playhead
* **Symptoms**: Scrubbing the timeline ruler has no visual effect on your model in the Scene view.
* **Cause**: The **Preview Root** field is empty, or the character model's bones do not match the animation curve paths.
* **Solution**: 
  1. Verify that your character GameObject is assigned to the **Preview Root** field in the top toolbar.
  2. Ensure the character has an active **Animator** component.
  3. If using Generic (non-humanoid) animations, check that the bone names and hierarchy paths in the clip match your character's bone names exactly.

### 3. Skeletons and bone lines do not render in the Scene view
* **Symptoms**: The character model is visible, but the colored bone lines, shapes, and name tags do not draw.
* **Cause**: The bone overlay toggle is disabled, or Unity's scene gizmos are turned off.
* **Solution**:
  1. In the sidebar's **Viewport** panel, check that **Show Bones** is toggled on.
  2. If **Animated Bones Only** is enabled, check that your loaded animation clip actually contains keyframes for the model's joints.
  3. Ensure that **Gizmos** are enabled in the top toolbar of the Unity Scene view.

### 4. IK target handles do not appear in the Scene view
* **Symptoms**: You cannot see the circle or line handles to grab and pose limbs, even though you have a character loaded.
* **Cause**: No IK rig config is assigned, or the IK Solver panel is disabled.
* **Solution**:
  1. Expand the **IK / FK Solver** section in the sidebar.
  2. Verify that your character has a valid IK rig configuration assigned.
  3. Make sure you are in a perspective or orthographic Scene view (not the Game view).

### 5. Transforming bones does not record keyframes
* **Symptoms**: You rotate or move bones in the Scene view, but no keyframe markers appear on the timeline.
* **Cause**: **Auto-Key** is disabled, or the modified bone is outside the Preview Root hierarchy.
* **Solution**:
  1. Check that the **Auto-Key** toggle is active (highlighted) in the top toolbar.
  2. Verify that the bone transform you are modifying is a child of the GameObject assigned to the **Preview Root** field.
  3. Make sure the playhead is sitting on the frame where you want to record the key before you move the bone.

### 6. Posing a bone on one frame shifts the animation across all frames
* **Symptoms**: When you rotate a bone, instead of writing a keyframe on the active frame, the entire animation path for that bone shifts by that offset.
* **Cause**: **Offset Mode** is enabled in the top toolbar.
* **Solution**: Toggle **Offset Mode** off to return to standard single-frame keyframe recording.
