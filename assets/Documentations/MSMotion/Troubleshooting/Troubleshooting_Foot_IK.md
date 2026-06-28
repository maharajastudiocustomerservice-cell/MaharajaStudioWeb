# Troubleshooting: Foot IK Forced on All Animations

## The Issue
When using **MSMotionAnimator**, you might find that Unity's built-in Foot IK is being forcefully applied to every animation (like attacks, jumps, or rolls), **even if you explicitly set `ApplyFootIK = false` on their `MSMotionAnimationConfig`**. This can cause the character's feet to unexpectedly stick to the ground or snap into odd poses during mid-air animations.

## The Cause
Unity's PlayableGraph has a hard limitation when blending legacy Animator Controllers with Playables: **If your base layer (Layer 0) is driven by an Animator Controller, and the active state in that controller has "Foot IK" ticked, it will forcefully bubble up and evaluate Foot IK across the entire character.**

Because MSMotion uses complex layered overrides, the base layer (your idle/walk/run locomotion) remains active at Weight 1.0 underneath the higher layers to prevent the character from squashing. As long as that base layer is requesting Foot IK, Unity's built-in IK solver will run for the final pose, completely ignoring the `ApplyFootIK = false` setting on your overriding MSMotion layers.

## The Solutions

### Solution 1: Use Animation Rigging (Recommended for Realistic look)
Unity's built-in legacy Foot IK is very limited and cannot be smoothly disabled during crossfades without causing 1-frame popping artifacts. 
For an industry-standard setup:
1. **Uncheck "Foot IK"** on all states (Idle/Walk/Run) in your base Animator Controller.
2. Setup **Two Bone IK constraints** using Unity's Animation Rigging package.
3. Assign the `MSMotionRigController` to your character.
MSMotion natively supports Animation Rigging and can dynamically and smoothly fade the IK rig weights in and out based on the `MSMotionAnimationConfig` for each layer, resulting in perfectly smooth transitions!

### Solution 2: Disable Foot IK on the Base Layer
If you prefer not to use Animation Rigging and want to rely on the built-in Foot IK, you must accept a compromise:
1. Open your base legacy Animator Controller.
2. Select your **Idle** state (or whichever states you expect to transition out of when playing a full-body MSMotion override).
3. **Uncheck "Foot IK"** on those specific states.
*(Note: This means you will lose Foot IK during those idle animations, but it will allow your higher-layer MSMotion animations to correctly disable Foot IK when needed.)*
