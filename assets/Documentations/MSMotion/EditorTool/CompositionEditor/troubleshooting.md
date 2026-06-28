# Troubleshooting Compositions

This guide covers common issues and questions when working with the **Composition Editor** in MSMotion.

---

## 1. Character "Jumps" or Snaps When Pressing Play

### Issue
When scrubbing the timeline, the character is in one position, but the moment you press **Play** in the toolbar, the character jumps or shifts to another position in the scene.

### Cause
This occurs due to a coordinate origin mismatch. When scrubbing, the editor uses the character's *current scene position* as the origin path for relative trajectories. When you press Play, if the coordinates haven't been locked, the preview graph may reset to a default origin, causing a sudden snap.

### Solution
1. Position your preview character in the scene where you want it.
2. In the Composition Editor's top toolbar, click the **Set Origin** button.
3. This locks the current coordinates as the explicit origin for the Composition asset, ensuring scrubbing and playback align.

---

## 2. Character Gaps (Slipping into a T-Pose)

### Issue
At certain times along the timeline, the character suddenly slips or blends into a static T-pose.

### Cause
This happens when there is a timeline gap where no active animation is playing. If you fade out one clip block and have a gap before the next block begins, the layer's total weight drops to 0. If there is no active animation on lower layers either, the character falls back to their default binding T-pose.

### Solution
* **Use Hold Extrapolation**: Select the preceding clip block and set its **Extrapolation Mode** to **Hold**. This freezes the final frame of the clip across the timeline gap until the next block starts playing.
* **Add a Base Layer Loop**: Ensure you have a bottom base layer (e.g. Layer 0) containing a looping idle animation block that plays continuously, acting as a fallback pose.

---

## 3. Script Events or Custom FX Do Not Fire in Editor Preview

### Issue
You have placed Audio, Particle, or Script FX nodes on the timeline, but you cannot hear or see them when scrubbing the timeline in the editor.

### Cause
* **Mute Events Toggle**: The global speaker icon on the toolbar is active.
* **Safety Toggle Active**: The safety toggle (FX indicator) is active, blocking script execution.
* **Missing Target Bone**: The target bone path is incorrect, or the character's hierarchy has changed.

### Solution
1. In the top toolbar, ensure the **Mute Events (Speaker)** toggle is unclicked (not highlighted).
2. Ensure the **Safety Toggle (FX)** is clicked to allow editor execution of custom script overrides.
3. Verify the **Target Human Bone** or **Target Bone** path exists on the preview character. Use the **Try Rebind FX Nodes to Humanoid** utility if you switched character meshes.

---

## 4. Performance Spikes or Lag During Editor Playback

### Issue
The Unity Editor suffers frame rate drops or lagging when playing or scrubbing a composition.

### Cause
Procedural physics (Jiggle) or leg grounding solvers (Foot IK) are executing heavy physics calculations (like raycasts or mesh collisions) every frame in edit mode.

### Solution
* **Optimize Jiggle Colliders**: If using Jiggle Physics, avoid enabling **Enable Self Collision** unless necessary. Self-collision on long bone chains (e.g. 15+ tail bones) is expensive.
* **Restrict Raycast Masks**: For **Foot IK**, ensure the **Raycast Mask** is set specifically to a simplified Terrain layer. Do not let Raycasts query complex character mesh colliders.
* **Simplify Target Bone Paths**: Reduce the number of targeted bones inside the Jiggle bone lists.

---

## 5. Visual Quality Discrepancies in Baked Clips (Clip Comparer)

### Issue
After exporting a composition, you notice that the character's movement in the baked animation clip has subtle offset differences, or is missing specific motion curves compared to the live preview window.

### Cause
This can happen due to curve optimization thresholds removing required keyframes, or due to channel filters (e.g. scale curves ignored on Generic exports or rotation modes not matching).

### Solution
Use the **Clip Comparer** utility to run a direct comparison:
1.  Open the Clip Comparer by choosing **Tools > Maharaja Studio > MsMotion > Debug > Compare Animation Clips** from the menu.
2.  Assign the original source clip (or composition preview clip) to the **Original Clip (A)** slot.
3.  Assign the newly baked output clip to the **Exported Clip (B)** slot.
4.  Click **Compare Clips**.
5.  The comparer will compare curves at keyframes (`t=0`) and write a detailed log mapping:
    *   Missing curves in the exported clip.
    *   Extra curves in the exported clip.
    *   Floating-point value differences.
6.  The comparison log will be saved to your project folder at `Assets/ClipComparisonLog.txt`. Review this file to pinpoint which bones or properties were optimized out or misaligned, and adjust your **Tangent Modes**, **Precision decimal places**, or **Keyframe Optimization Tolerances** in the [Export Options](export-options.md) window accordingly.

