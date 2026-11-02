MSMotion — Technical Details & Feature Reference
📖 Full Documentation: https://maharajastudiocustomerservice-cell.github.io/MaharajaStudioWeb/ms-motion-docs.html
📦 Package Contents
✔ Full C# source code — no DLLs, no black boxes
✔ UI Toolkit editor scripts and USS stylesheets
✔ High-performance runtime API (PlayableGraph-based, Zero-GC)
✔ Comprehensive local documentation (Documentation folder)
✔ Example scenes and starter guides

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

→ Layers: Unlimited named layers · Override or Additive blend modes · Curve-driven weights · AvatarMask isolation · Solo · Lock · Mute · Drag-to-reorder · Duplicate
→ Slot Operations: Move across layers · Edge trimming · Split at playhead · Duplicate clip copy · Cut / Copy / Paste · Ripple-delete · Custom tint · Speed easing curve · 6 transition curve shapes (Linear, Smooth, EaseIn, EaseOut, Cubic, Bounce)
→ Slot Types: AnimationClip · Pose Hold · IK Override · Foot IK · Look-At · Jiggle Physics · Spline Trajectory · IK Lock · Dynamic Bone Subdivision (DBS) · AudioFX · ParticleFX · DecalFX · VFXGraphFX · SpawnFX · TransformFX · CameraShakeFX · ScriptEventFX · SpawnActor · DestroyActor
→ Editor Features: Actor Roster Window (`MSMotionActorRosterWindow`) · Dynamic Alignment (Motion Warping) · Color-coded Markers · Loop Region · Real-time Scene Preview (PlayableGraph inside AnimationMode) · IK Scene View Handles · Breadcrumb Navigation · Bone Scene Overlay


👥 Multi-Actor Choreography & Dynamic Summons (v2.0.0)
Direct multi-character choreography and companion summons right from the timeline:

→ Choreography & Rigs: Synchronized 2, 3+ character choreography with 0ms frame drift · Humanoid & Generic rig mixing (creatures, quadrupeds, robots, props) in the same sequence · Actor Roster Window role assignments, accent swatches, and bound scene objects · Visual actor badge pills & tinted strips on timeline blocks · Details Panel & context menu slot routing · Independent root motion evaluation per actor channel (prevents sliding) · Multi-output PlayableGraph preview & synchronized scrubbing · Target actor event dispatching · Cross-actor partner bone pinning (`IKChainModifier`) and look-at tracking (`MSMotionLookAtModifier`)
→ Dynamic / Temporary Actors: Author ephemeral summons (weapons, dragons, Stand avatars, familiars) in Actor Roster · Timing presets (`0`, `0.25`, `0.5`, `0.75`, `1.0`, `Custom`) · `SpawnActorSlot` & `DestroyActorSlot` timeline blocks (socket parenting, spatial offsets, entry/exit scale curves) · Zero-allocation pooling (`MSMotionActorPool`) · 1-line playback (`animator.Play`) auto-spawns, transforms, animates, and recycles
→ Motion Warping & Dynamic Alignment: Pre-interaction entry phase bridges gameplay starting distances without timeline padding · Dynamic speed scaling eliminates foot sliding · Early arrival waiting idles · Auto Stride derivation from root motion curves · Downward terrain raycasting for slopes/stairs · Scene View visualizer (arrival discs, lead sync origin, live trajectory readouts, Snap & Test tools)
→ Cross-Actor FX & Prop Handover: Dynamically pass props, weapons, torches, or visual spell effects between characters (`Instant`, `SmoothInterpolation`, `FollowTrajectory`) · `RetainOnEnd` setting persists transferred items on the receiver actor


🧩 Modifier Nodes
Stackable, timeline-driven procedural solvers:

→ 🦾 IK Override: Multiple IK chains · Effector + pole keyframes in Scene View · Squash & Stretch scale handles · Twist Distribution for limb rolls · Advanced IK Locks to freeze multiple joints · FBIK solver
→ 👣 Foot IK: Standard, RootRelative, SimpleSnap algorithms · Raycast terrain adaptation · Pelvis drop · Foot lock · Toe rotation · Normal alignment · Humanoid & Generic support
→ 👀 Look-At: Head, spine, and eyes track targets · Biological saccade micro-jitter · Soft angle limits · Partner bone targeting · Humanoid & Generic support
→ 🌊 Jiggle Physics: Spring-mass chain simulation · Stiffness, damping, mass, gravity, wind, turbulence · 4 colliders (Sphere, Capsule, Box, Plane) · Volume preservation (Squash & Stretch)
→ 🛤️ Spline Trajectory: Bezier root motion paths in Scene View · Procedural banking · Ground-snap raycasting · Speed heatmap HUD · Closed-loop paths
→ 🔒 IK Lock: Freeze limb at world-space contact while body continues animating
→ 🦴 Dynamic Bone Subdivision (DBS): Procedural multi-joint chain deformation with balanced weight distribution


✨ FX Event Nodes — 8 Types + Dynamic Actor Nodes

→ 🔊 AudioFX: Volume, pitch, spatial blend, stereo pan, 3D distance, volume fade envelope
→ 💥 ParticleFX: OneShot or sustained, bone attachment, detach mode, Bezier movement paths
→ 🎨 DecalFX: Raycast surface projection (slope normal angle limits, distance, layers) · Prefab or Material mode · URP Decal Projector normal blending · Uniform & non-uniform scaling · Moving platform attachment · Fade in/out · Fully pooled
→ 🎇 VFXGraphFX: Drive all VFX Graph parameter types (float, Color, Texture, Gradient, Mesh)
→ 📷 CameraShakeFX: Cinemachine Impulse trigger on a specific frame
→ 📦 SpawnFX: Instantiate prefabs at bone-relative sockets with zero runtime GC spikes
→ 🦴 TransformFX: Bone override (Local/World/Bone-Relative) · Blend envelope · Bezier spline flight paths
→ ⚙️ ScriptEventFX: Typed C# callbacks via `MSMotionScriptEventBus` (float, int, bool, string, GameObject)
→ 👥 SpawnActorFX / DestroyActorFX: Spawns and recycles dynamic actors (summons, familiars, props) · Socket attachment · Scale curves · Pool integration
→ Shared FX Features: Cross-Actor Handover · 4-tier Property Overrides (Manifest → Global FXRegistry → Per-Slot Overrides → Dynamic Runtime Overrides API) · FX Path Tools HUD overlay with preset generators · AvatarMask-aware dispatch · Layer-weight-scaled intensity


🎬 Animation Editor

→ 1-Click FBX Extraction: Convert model clips to editable local `.anim` assets
→ Range Operations: Insert, Delete (with ripple), Scale, Reverse, Crop, Remove with Transition
→ 3 Paste Modes: Merge, Overwrite, Insert
→ Keyframe Control: Time, value, in/out tangents, tangent modes (Auto, Linear, Manual)
→ Optimization & Smoothing: Median/Gaussian/Average curve smoothing, keyframe reduction, root motion extractor
→ Live Link & Ghost Preview: Evaluate full composition context (IK, layers, FX) live in Scene View while editing raw clips


⚠️ Known Limitation — FX Event Dispatch
FX events are triggered via Unity's AnimationEvent system embedded in exported clips. Animation events can skip during fast time jumps or non-linear crossfades.
✔ Use FX events for visual/audio effects (particles, sounds, camera shakes, decals).
✘ Do NOT rely on FX events for critical gameplay logic (hitbox activation, damage, state transitions).
For gameplay-critical timing, use `MSMotionAnimator` state queries (`GetNormalizedTime`, `GetCurrentTime`, `IsPlaying`) from your Update loop, or use ScriptEventFX with a gameplay fallback.

🔜 Upcoming: An event-free FX cursor driven directly by PlayableGraph time will eliminate skipped events entirely.


⚡ Runtime API Summary
MSMotionAnimator

→ Play(config) · CrossFade(config) · PlayThenCrossFade(a, b) — async-await sequencing
→ Stop · StopSmoothly · StopAll · Pause · Resume
→ Delay-start-during-crossfade — preserves frame-0 root motion during crossfade blend-in
→ Query: IsPlaying · IsFading · GetNormalizedTime · GetTimeRemaining · GetActiveWeight
MSMotionInteraction *(Multi-Actor Choreography)*
→ Play(config, lead, partner...) — 1-line synchronized multi-character playback
→ StopActor(actor, fade, policy) — dynamic departure (`ContinueRemaining` or `StopAll`)
→ Builder: SetSyncPoint · SetFadeIn · SetFadeOut · OnComplete · OnActorStopped · OnTick
MSMotionActorPool
→ Zero-allocation runtime pooling for ephemeral summons, companion entities, and decals
MSMotionFXPlayer
→ Fires all 8 FX types frame-accurately · Fully pooled (AudioSource + ParticleSystem + Decals)
→ Layer-weight-scaled intensity · AvatarMask-aware per-layer FX dispatch
MSMotionRigController *(requires Unity Animation Rigging)*
→ Named IK constraint registry · SetTarget(id, transform) · Cross-layer suppression via AvatarMask
MSMotionStretchApplicator
→ Applies Squash & Stretch scale transformations at runtime · Built-in LOD distance culling
MSMotionAnimationConfig & MSMotionInteractionConfig
→ ScriptableObject assets storing clips, masks, layers, IK entries, and multi-actor sync alignments


🎮 Interactive Windows Demo Build
👉 Download: https://github.com/maharajastudiocustomerservice-cell/MSMotion-Demo-Build-win/releases/tag/Demo


📞 Support
📧 Email: maharajastudiocustomerservice@gmail.com
🌐 Website: https://maharajastudiocustomerservice-cell.github.io/MaharajaStudioWeb/ms-motion.html
💬 Discord: https://discord.gg/GamF5bez3h
📖 Full Docs: https://maharajastudiocustomerservice-cell.github.io/MaharajaStudioWeb/ms-motion-docs.html