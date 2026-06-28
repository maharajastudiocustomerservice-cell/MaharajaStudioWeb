# Troubleshooting: 1-3 Frame Rotation Glitches in Roll & Flip Animations

## The Problem
When using extreme acrobatic animations where a Humanoid character goes completely upside down (e.g., forward rolls, backflips), you may notice the character's body visually spin backward or glitch for exactly 1 to 3 frames at the very apex of the flip. 

This typically happens in the Composition Editor when **Apply Root Motion is disabled** for that clip, or when the clip is attached to a **Trajectory**.

## The Cause
This is a known, fundamental limitation within Unity's core `PlayableGraph` and Humanoid Retargeting engine, not a bug within the MSMotion Animation Editor itself.

When a Humanoid character flips upside down (Pitch reaches 180 degrees), Unity's internal Center of Mass (CoM) extractor hits a mathematical singularity (Gimbal lock). To try and resolve it, Unity generates a massive sudden spike in the internal Root Motion curves and bakes the inverse of that spike into the character's hips. 

If Root Motion is enabled, these two spikes cancel each other out perfectly. However, if Root Motion is disabled or redirected via a Trajectory, the character's root is locked in place, and the inverse spike baked into the hips is visually exposed—causing the sudden 3-frame flip glitch.

## The Solution
Because this is a native Unity evaluation behavior, the MSMotion Editor cannot mathematically fix the curves at runtime without breaking other features. 

To solve this, you must tell Unity to permanently bake the singularity into the animation asset's pose itself, bypassing the buggy Center of Mass extractor.

### Step-by-Step Fix
Whenever you drag an animation into the MSMotion Composition Editor, the tool automatically creates a duplicate of that animation and stores it as a **sub-asset** inside your Composition Asset. You must modify this specific sub-asset.

1. **Locate your Composition Asset** in the Unity Project Window.
2. Click the small **expand arrow** next to the Composition Asset to reveal its sub-assets.
3. Find and select the problematic **roll/flip animation clip** sub-asset.
4. With the clip selected, look at the **Inspector Window**.
5. Adjust the following settings:
   - Check **"Bake Into Pose"** for **Root Transform Rotation** (This prevents the rotation glitch).
   - Check **"Bake Into Pose"** for **Root Transform Position (Y)** (This prevents the vertical position spike).
   - *Optional:* Leave **Root Transform Position (XZ)** UNCHECKED if the roll moves the character forward and you want to preserve that forward root motion.

Once these settings are applied, the animation will play and scrub flawlessly inside the Composition Editor, regardless of whether Root Motion is on, off, or following a Trajectory!
