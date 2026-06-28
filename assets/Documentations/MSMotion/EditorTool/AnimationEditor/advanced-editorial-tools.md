# Advanced Editorial Tools

The Animation Editor includes five advanced tools located in the **Advanced Tools** sidebar foldout. These tools streamline editing tasks like mirroring poses, blending keys, cleaning up noise, and extracting root motion.

---

## 1. Mirror Pose

The **Mirror Pose** tool flips the animation data across the character's center axis. This is useful for copying poses from the left arm to the right, or mirroring entire walk cycles.

### Settings
* **Target Options**:
  * **Current Frame Only**: Mirrors only the pose at the current playhead time.
  * **Selected Time Range**: Mirrors animation keys falling within your active selection range.
  * **Selected Keys**: Mirrors only the specific keyframes highlighted in the timeline.
  * **Entire Clip**: Mirrors the animation across the full length of the clip.
* **Limit to Selected Curves**: When enabled, the mirror action only affects the curves highlighted in the Curves list (e.g. mirroring only the arm curves while leaving the legs untouched).

### How it Works
* **Humanoid Characters**: The editor uses Unity's humanoid joint mapping to swap muscle values (e.g., Left Shoulder Twist to Right Shoulder Twist) and automatically inverts values to maintain visual symmetry.
* **Generic Characters**: The editor uses naming rules to swap curve paths (e.g., swapping paths containing `Left`, ` L `, or `_L_` with `Right`, ` R `, or `_R_`). Numeric translation and rotation coordinates are inverted on the appropriate axes.

---

## 2. Tween Machine

The **Tween Machine** allows you to interactively blend the pose at the current frame using the preceding and succeeding keyframes as anchors.

### How to Use
1. Select one or more property curves in the Curves list.
2. Move the playhead to a frame between two keyframes.
3. Drag the **Blend** slider left or right:
   * Dragging **Left (0.0)** blends the pose toward the previous keyframe's value.
   * Dragging **Right (1.0)** blends the pose toward the next keyframe's value.
   * Leaving it in the **Center (0.5)** creates an equal blend.
4. Release the slider to bake the interpolated value as a keyframe at the playhead time.

---

## 3. Keyframe Optimizer

Raw animations (especially motion capture or baked animations) often contain keys on every single frame, resulting in large asset file sizes. The **Keyframe Optimizer** removes redundant keys without changing the overall shape of the motion.

### Settings
* **Position Tol.**: The threshold (in units) for discarding translation keyframes.
* **Rotation Tol.**: The threshold (in degrees) for discarding rotation keyframes.
* **Algorithm**: The editor analyzes each curve. If a keyframe's value deviates less than the tolerance from a straight line drawn between the preceding and succeeding keys, it is deleted.

---

## 4. Keyframe Smoothing

The **Keyframe Smoothing** tool filters jitter, noise, and abrupt spikes from animation curves.

### Settings
* **Target Bone**: Choose a specific bone curve path to smooth, or select **All Bones** to filter the entire clip.
* **Filter Type**:
  * **Median**: Removes isolated spikes and sudden noise pops while preserving sharp motion transitions.
  * **Average**: Smooths general noise by calculating a flat average of neighboring frames.
  * **Gaussian**: Applies a weighted average to create smooth, organic motion profiles.
* **Window Size**: The frame range (3 to 51 frames) used for the smoothing calculations. Larger windows create smoother, slower motion.
* **Iterations**: The number of filtering passes (1 to 5) to run.
* **Auto Tangents**: Automatically adjusts tangent slopes for the modified keyframes to maintain smooth curves.
* **Limit Range**: Confines the smoothing filter to the time window specified in the **Range (s)** fields.

---

## 5. Extract Root Motion

Root motion moves the character's physical coordinate origin in the game world based on the animations. The **Extract Root Motion** tool isolates movement from a character bone and transfers it to the animation's Root Node.

### Typical Workflow
1. Select the bone that contains the forward motion (typically the `Hips`, `Pelvis`, or the root-most moving bone).
2. Configure extraction settings:
   * **Target is Humanoid**: Enable this if working on a humanoid character.
   * **Pos (X/Y/Z)** / **Rot (X/Y/Z)**: Choose which motion axes to extract. For standard locomotion, position X and Z (horizontal movement) and rotation Y (turning direction) are typically extracted, leaving position Y (jumping height) on the hips.
3. Click **Extract Root Motion**. The editor strips translation and rotation from the hips bone and writes it directly onto the clip's root transform curves.
