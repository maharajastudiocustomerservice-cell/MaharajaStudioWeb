MSMotion — Technical Details & Feature Reference

📖 Full Documentation: https://maharajastudiocustomerservice-cell.github.io/MaharajaStudioWeb/ms-motion-docs.html


📦 Package Contents

✔  Full C# source code — no DLLs, no black boxes
✔  UI Toolkit editor scripts and USS stylesheets
✔  High-performance runtime API (PlayableGraph-based, Zero-GC)
✔  Comprehensive local documentation (Documentation~ folder)
✔  Example scenes and starter guides


🛠️ Compatibility

| Property              | Detail                                               |
|-----------------------|------------------------------------------------------|
| Unity Version         | Unity 6+                                             |
| Runtime Architecture  | PlayableGraph API — no AnimatorController at runtime |
| Editor Architecture   | Unity UI Toolkit                                     |
| Cinemachine           | Optional — for CameraShakeFX nodes                   |
| Unity VFX Graph       | Optional — for VFXGraphFX nodes                      |
| Unity Anim. Rigging   | Optional — for MSMotionRigController                 |


🎛️ Composition Editor

Multi-layer, non-destructive character timeline.

Layers
→ Unlimited named layers · Override or Additive blend mode
→ Per-layer weight: static or AnimationCurve-driven over time
→ Per-layer AvatarMask (upper/lower body isolation)
→ Enable · Disable · Solo · Lock · Drag-to-reorder · Duplicate

Slot Operations
→ Move across layers · Trim from either edge · Split at playhead
→ Duplicate (independent embedded clip copy) · Cut / Copy / Paste
→ Ripple-delete · Custom tint color · Speed override with easing curve
→ Per-slot Blend-In/Out with 6 curve shapes (Linear, Smooth, EaseIn, EaseOut, Cubic, Bounce)

Slot Types
🎞  AnimationClip · Pose Hold · IK Override · Foot IK · Look-At
🌊  Jiggle Physics · Spline Trajectory · IK Lock
🔊  AudioFX · ParticleFX · VFXGraphFX · SpawnFX · TransformFX · CameraShakeFX · ScriptEventFX

Other Features
→ Color-coded Composition Markers with drag-to-reposition
→ Configurable Loop Region for rapid authoring iteration
→ Real-time Scene Preview — live PlayableGraph inside AnimationMode, no Play Mode needed
→ IK Scene Controller — drag effector/pole handles in Scene View; keyframes auto-write back
→ Breadcrumb Navigation — drill into any slot's clip and return with one click
→ Bone Scene Overlay — all bones visible, animated bones highlighted


🧩 Modifier Nodes

All nodes are stackable, timed, and blend in/out on the composition timeline.

🦾  IK Override Node
Multiple IK chains · Animated effector + pole keyframes in Scene View
Per-chain Squash & Stretch scale handles · FBIK solver

👣  Gait-Adaptive Foot IK Node
Algorithms: Standard, RootRelative, SimpleSnap, Legacy
Swing/plant phase from animated foot velocity · Raycast terrain adaptation
Pelvis drop · Foot lock · Toe rotation · Ground normal alignment · Humanoid auto-detect / Generic support

👀  Look-At Node
Head · Spine chain · Left/Right eye — independently weighted
Biological saccade micro-jitter · Soft angle limits · Humanoid auto-detect / Generic support

🌊  Jiggle Physics Node
Spring-mass chain simulation · Stiffness, Damping, Mass, Gravity, Centrifugal force
Per-bone falloff curves · Wind + Turbulence · Self-collision
4 collider shapes: Sphere, Capsule, Box, Plane · Volume preservation (Squash & Stretch)

🛤️  Spline Trajectory Node
Bezier root motion path in Scene View · Relative or Absolute space
Procedural rotation + banking · Easing curve · Ground-snap raycasting
Speed heatmap HUD · Closed-loop paths

🔒  IK Lock Node
Freeze a limb at world-space contact while the body continues animating


✨ FX Event Nodes — 7 Types

🔊  AudioFX — Volume, Pitch, SpatialBlend, StereoPan, 3D distance · Blend envelope
💥  ParticleFX — OneShot or Sustained · Bone attachment · Detach mode · Trajectory path
🎇  VFXGraphFX — Drive all VFX Graph parameter types (float, Color, Texture, Gradient, Mesh, etc.)
📷  CameraShakeFX — Cinemachine Impulse trigger on a specific frame
📦  SpawnFX — Instantiate any prefab at a bone-relative position · Zero Instantiate/Destroy
🦴  TransformFX — Bone override (Local/World/Bone-Relative space) · Blend-In/Out envelope
⚙️  ScriptEventFX — Typed C# callbacks via MSMotionScriptEventBus · Passes float/int/bool/string/GameObject

Shared FX Features
→ Property Overrides — override any spawned prefab field (Light intensity, Material color, etc.) per slot
→ FX Trajectory Paths — Bezier movement paths for Particle/VFX effects in Scene View
→ Three-tier Override System: Manifest → Global FXRegistry → per-instance runtime API
→ AvatarMask-aware dispatch — lower-body layers don't fire upper-body FX events
→ Layer-weight-scaled intensity — FX volume/emission scales with blend weight during crossfades


🎬 Animation Editor

→ 1-click FBX clip extraction to editable standalone .anim assets
→ Range operations: Insert, Delete (with ripple), Scale, Reverse, Crop, Remove with Transition
→ Three paste modes: Merge · Overwrite · Insert
→ Keyframe edit: time, value, in/out tangent, tangent mode (Auto, Linear, Manual)
→ Snap to frame · Bake curves to target frame rate
→ Keyframe Optimizer — remove redundant keys within position/rotation tolerances
→ Curve Smoother — Median, Gaussian, or Average filter · configurable window and iteration
→ Root Motion Extractor — per-axis (X/Y/Z) extraction to Humanoid RootT/RootQ or Generic root
→ Mirror · Tween slider · Auto-Key in Scene View
→ Sync-to-Composition Ghost Preview — author a clip with the full composition context behind it


⚠️ Known Limitation — FX Event Dispatch (Current Version)

FX events are currently triggered via Unity's AnimationEvent system embedded in the exported
animation clip. While this works reliably in most cases, Unity's AnimationEvent mechanism can
skip events under certain conditions — for example, during fast time jumps, large frame rate
drops, or when a CrossFade causes the clip time to advance non-linearly.

Because of this, we strongly recommend the following:

✔  Use FX events for visual and audio effects (particles, sounds, camera shakes, VFX).
✘  Do NOT rely on FX events for critical gameplay logic such as hitbox activation,
    damage dealing, collision triggers, or state machine transitions.

For gameplay-critical timing, use the MSMotionAnimator state query API (GetNormalizedTime,
GetCurrentTime, IsPlaying) to drive logic from your own Update loop, or use the ScriptEventFX
node as a signal — but always guard it with a fallback in your gameplay code.

🔜 Upcoming: A future update will replace the AnimationEvent dispatch system with an
event-free FX cursor driven directly by MSMotionAnimator's PlayableGraph time. This will
eliminate skipped events entirely and make FX dispatch 100% reliable regardless of crossfade,
time scale, or frame rate. Existing authored compositions will migrate automatically.


⚡ Runtime API Summary

MSMotionAnimator
→ Play(config) · CrossFade(config) · PlayThenCrossFade(a, b) — async-await sequencing
→ Stop · StopSmoothly · StopAll · Pause · Resume
→ Delay-start-during-crossfade — holds clip at frame 0 during blend-in to preserve root motion
→ Query: IsPlaying · IsFading · GetNormalizedTime · GetTimeRemaining · GetActiveWeight

MSMotionFXPlayer
→ Fires all 7 FX types frame-accurately · Fully pooled (AudioSource + ParticleSystem)
→ Layer-weight-scaled intensity · AvatarMask-aware per-layer FX dispatch

MSMotionRigController  *(requires Unity Animation Rigging)*
→ Named IK constraint registry — activate/deactivate per animation config
→ SetTarget(id, transform) — point IK at any runtime target (enemy, ledge, weapon)
→ Cross-layer IK suppression via AvatarMask

MSMotionAnimationConfig *(ScriptableObject per animation)*
Clip · FX Manifest · Layer · AvatarMask · Additive flag · Loop flag
Fade-In/Out · Playback Speed · IK Override entries · FX Registry override · Delay-start flag


📞 Support

📧  Email: [Insert Support Email]
🌐  Website: [Insert Website URL]
💬  Discord: [Insert Discord Link]
📖  Full Docs: https://maharajastudiocustomerservice-cell.github.io/MaharajaStudioWeb/ms-motion-docs.html