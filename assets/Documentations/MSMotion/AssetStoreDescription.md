MaharajaStudio MSMotion — Animate. Simulate. React. All in One Place.
Create complex, FX-driven animations and synchronized multi-character choreography in minutes—without writing a single script.

Your game's attack has a sword trail. A footstep kicks up dust and plays a crunch. A leap follows a perfect arc and lands with a camera shake. A partner character catches the hero in mid-air and spins into a synchronized dance lift. MSMotion connects animations, visual effects, secondary physics, multi-character choreography, and gameplay logic on a single shared timeline.

No more jumping between an Animator window, Particle Systems, and scripts. MSMotion does it all in one editor with real-time Scene View preview — and zero performance cost at runtime.


🌟 Why MSMotion Is Different
Most animation tools stop at the clip. MSMotion starts there and goes much further:

🔹 Zero-Code Syncing: Drop Audio, particles, or surface decals on the exact impact frame.
🔹 Multi-Actor Choreography: Direct dance duets, martial arts grapples, co-op takedowns, and cinematics with 0ms frame drift.
🔹 Live Editor Preview: Everything previews live in the Scene View without entering Play Mode.
🔹 Interactive Physics & IK: Add Jiggle Physics, Foot IK, or IK Overrides with interactive handles.
🔹 Dynamic Summons: Spawn temporary weapons, familiars, dragons, or Stand avatars with automatic object pooling and 1-line playback.
🔹 Dynamic Motion Warping: Automatically scales approach locomotion and adapts to terrain so characters arrive at authored sync spots without foot sliding.
🔹 Custom Logic Triggers: Fire hitboxes, combo windows, and state changes directly from the timeline via typed C# events.
🔹 Scene-Independent: Build your sequence once and reuse it anywhere across your project.


🎛️ The Composition Editor
Your primary timeline workspace for character motion, layers, and gameplay events:

🔹 Unlimited Layers: Stack Override and Additive layers with AvatarMasks for seamless upper/lower body isolation.
🔹 Actor Roster & Routing: Manage participants in the Actor Roster (`👥 Actors`) and route timeline slots to designated characters with visual color badges and accent strips.
🔹 Non-Destructive Slot Editing: Drag, trim, split, duplicate, cut/copy/paste, and ripple-delete any slot.
🔹 6 Crossfade Transitions: Smoothly blend slots using Linear, Smooth, EaseIn, EaseOut, Cubic, or Bounce curves.
🔹 Markers & Loop Region: Annotate impact frames and loop sub-ranges for rapid iteration.
🔹 Viewport Controls: Real-time IK handle dragging, auto-keying, bone overlay, and breadcrumb navigation.


👥 Multi-Actor Choreography & Dynamic Summons (v2.0.0)
Direct multi-character choreography and companion summons right from the timeline:

🎭 Synchronized Duets & Grapples: Coordinate 2, 3+ characters with 0ms frame drift.
🐾 Humanoid & Generic Rigs: Mix Humanoids with Generic rigs (quadrupeds, monsters, robots, props) in the same sequence.
⚡ Motion Warping & Dynamic Alignment: Pre-interaction entry phase dynamically scales locomotion speed to match distance and terrain, eliminating foot sliding. Includes Auto Stride speed derivation and Scene View alignment discs.
🐉 Dynamic / Temporary Actors: Ephemeral summons (weapons, dragons, familiars) auto-spawn, track sockets, animate, and recycle back to the zero-allocation `MSMotionActorPool`.
🔄 Cross-Actor FX & Prop Handover: Seamlessly pass props, weapons, torches, or spell effects between characters (Instant, SmoothInterpolation, or FollowTrajectory). Transferred items can persist via `RetainOnEnd`.
🎯 Cross-Actor Partner Targeting: Hand/foot IK effectors and Look-At modifiers can directly target partner bones.
▶️ 1-Line Runtime API: `MSMotionInteraction.Play(duetConfig, leadActor, partnerActor)` coordinates independent PlayableGraphs without race conditions.
🚪 Dynamic Participant Departure: Characters can break away early via `session.StopActor()` using `ContinueRemaining` or `StopAll` cascade policies.


🧩 Modifier Nodes — The Power Behind the Animator
Stackable, timeline-driven procedural solvers:

🦾 IK Override: Multiple IK chains, effector/pole handles in Scene View, Squash & Stretch handles, Twist Distribution for limb rolls, FBIK solver, and Advanced IK Locks to pin multiple joints.
👣 Foot IK: Raycast terrain adaptation, pelvis drop, foot lock, toe rotation, and ground normal alignment. Auto-detects Humanoids and supports Generic rigs.
👀 Look-At: Head, spine, and eyes smoothly track targets. Includes biological saccade micro-jitter, soft angle limits, and partner bone targeting.
🌊 Jiggle Physics: Spring-mass chain simulation with stiffness, damping, mass, gravity, wind, turbulence, 4 collision shapes (Sphere, Capsule, Box, Plane), and volume preservation (Squash & Stretch).
🛤️ Spline Trajectory: Draw Bezier paths in Scene View for dashes, leaps, and cutscene motion with banking, ground snapping, and speed heatmaps.
🔒 IK Lock: Freeze a hand or foot to a surface contact point while the body continues animating.
🦴 Dynamic Bone Subdivision (DBS): Procedural multi-joint chain deformation with balanced weight distribution.


✨ FX & Gameplay Event Nodes — 8 Types + Summons
Trigger synchronized effects and logic directly from the timeline:

🔁 4-Tier Property Overrides: Customize prefab fields, light intensity, or material colors per slot, via global FXRegistry, or through runtime C# scripts.
🔊 Audio FX: Volume, pitch, stereo pan, 3D distance, and volume fade envelopes.
💥 Particle FX: Bone attachment, sustained/oneshot modes, and Bezier movement paths.
🎨 Decal FX: Project decals onto dynamic geometry with raycast slope angle limits, URP Decal Projector normal blending, non-uniform scaling, moving platform attachment, and pooling.
🎇 VFX Graph: Drive Unity VFX Graphs and exposed parameters from the timeline.
📷 Camera Shake: Cinemachine Impulse shakes triggered on specific impact frames.
📦 Spawn FX: Instantiate prefabs at bone sockets with zero runtime GC spikes.
🦴 Transform FX: Dynamic bone/socket offsets with 3D Bezier spline flight paths.
⚙️ Script Event: Dispatch typed callbacks via `MSMotionScriptEventBus` (float, int, bool, string, GameObject).
👥 Spawn & Destroy Actor: Control frame timing, sockets, scale curves, and pool recycling of dynamic summon entities.
🔄 Cross-Actor Handover: Smoothly transfer props and effects between characters.
🛣️ FX Path Tools HUD: Viewport overlay with preset path generators (Arcs, Helixes, Spirals, Waves).


🎬 Animation Editor
Inspect and refine raw animation clips directly inside Unity:

🔓 1-Click Extraction: Convert locked FBX model clips into editable local `.anim` assets.
✂️ Range Operations: Insert, Delete (with ripple), Scale, Reverse, Crop, and Remove with Transition.
📐 Keyframe Control: Edit time, value, tangents, and tangent modes (Auto, Linear, Manual).
🔁 Curve Tools: Mirror, curve smoothing (Median/Gaussian/Average), keyframe optimization, and root motion extraction.
🎯 Auto-Key: Move bones in Scene View to auto-write keyframes.
👻 Live Link & Ghost Preview: Evaluate full composition context (IK, layers, FX) live in Scene View while editing raw clips.


⚡ Runtime — Zero GC. Maximum Performance.
MSMotion runs on Unity's low-level PlayableGraph API — no Animator Controller overhead:

▶️ 1-Line Playback: `animator.Play(config)`, `CrossFade(config)`, and `PlayThenCrossFade(a, b)`.
👥 Multi-Actor Runner: `MSMotionInteraction.Play()` coordinates multiple characters with zero frame drift.
🎭 Dynamic Layers: Mixers allocated on-demand, keeping memory footprint minimal.
🎚️ Frame-Accurate FX: Audio, particles, decals, and camera shakes fire with automatic intensity scaling during crossfades.
🔗 Procedural Rigging: Activate/deactivate IK constraints per animation; retarget limbs at runtime.
♻️ Zero-Allocation Pooling: `MSMotionActorPool` and `MSMotionFXPool` eliminate runtime heap allocations.


🛠️ Compatibility

Engine: Unity 6 and above
Rig Support: Full support for both Humanoid and Generic rigs
Source Code: Full C# source included — no DLLs, no black boxes
Optional Integrations: Cinemachine · Unity VFX Graph · Unity Animation Rigging
Documentation: Full guides included in the Documentation folder and Website


📞 Support & Community
📧 Email: maharajastudiocustomerservice@gmail.com
🌐 Website: https://maharajastudiocustomerservice-cell.github.io/MaharajaStudioWeb/ms-motion.html
💬 Discord: https://discord.gg/GamF5bez3h
📖 Docs: https://maharajastudiocustomerservice-cell.github.io/MaharajaStudioWeb/ms-motion-docs.html
▶️ Tutorials: https://youtube.com/@king_of_games-l9e?si=EleZSFthz6ZBPPao
🎮 Demo : https://github.com/maharajastudiocustomerservice-cell/MSMotion-Demo-Build-win/releases/tag/Demo

🎮 Try the Interactive Windows Demo!
Want to see the system in action before you buy? We have put together a highly polished, high-fidelity cinematic demo showcasing exactly how the tool drives complex FX and animation paths at runtime with peak Burst-compiled performance.

👉 [Download the Free Windows Demo Build via GitHub](https://github.com/maharajastudiocustomerservice-cell/MSMotion-Demo-Build-win/releases/tag/Demo)

⚠️ Note on Windows SmartScreen: Because this is an unsigned indie executable demo distributed outside a major launcher, Windows Defender may show a "Windows protected your PC" popup when you launch it. This is completely normal! Simply click "More info" and then "Run anyway" to play.


MSMotion is built for developers who want AAA-quality animation pipelines without sacrificing performance, flexibility, or creative control.