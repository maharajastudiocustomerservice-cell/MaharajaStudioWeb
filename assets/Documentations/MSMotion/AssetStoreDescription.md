MaharajaStudio MSMotion — Animate. Simulate. React. All in One Place.

Your game's attack has a sword trail. A footstep kicks up dust and plays a crunch. A leap follows a perfect arc and lands with a camera shake. MSMotion is built around this reality — it is the only Unity tool that connects your animations, visual effects, physics, and gameplay logic on a single shared timeline.

No more jumping between an Animator window, a Particle System, and a script. MSMotion does it all, in one editor, with real-time preview — and zero performance cost at runtime.


🌟 Why MSMotion Is Different

Most animation tools stop at the clip. MSMotion starts there and goes much further.

✅  Place an IK Override on the same timeline as your attack animation — the arm reaches exactly where you want, exactly when you want.
✅  Drop an Audio event on the same frame as the impact — frame-perfect sync, every time.
✅  Add Jiggle Physics to a ponytail, a cape, or a chain — it reacts to movement automatically.
✅  Draw a Bezier path for a dash or a leap — the character follows it smoothly without touching root motion baking.
✅  Trigger your own gameplay code (hitboxes, combo windows, state changes) directly from the timeline — no polling, no guessing.

Everything previews live in the Scene View, inside the Unity Editor, without entering Play Mode.


🎛️ The Composition Editor

This is your main workspace. Think of it like a video editor, but for character animation and gameplay events.

🔹 Stack unlimited layers — blend full-body animations, upper-body overrides, and physics reactions all at once.
🔹 Mix Override and Additive layers with AvatarMasks — for perfect upper/lower body blending.
🔹 Every layer accepts Animation Clips, Pose Holds, IK Nodes, Physics Nodes, and FX Events as slots.
🔹 Drag, trim, split, duplicate, and ripple-delete any slot — a full non-destructive editing workflow.
🔹 Set crossfade curves per slot with 6 transition shapes.
🔹 Place color-coded Markers to annotate combo windows, impact frames, or cutscene beats.
🔹 Real-time IK handle dragging in the Scene View — keyframes write back automatically.


🧩 Modifier Nodes — The Power Behind the Animator

These are stackable, timeline-driven solvers that run live on top of your animation:

🦾  IK Override Node — Keyframe a hand or foot position in world space over time. Drag interactive handles in the Scene View. Add Squash & Stretch on impact frames — all without touching the base clip.

👣  Foot IK Node — Automatically plants feet on uneven terrain, stairs, and slopes. Handles pelvis drop, foot locking, and toe rotation. Works out-of-the-box on Humanoid rigs, and supports Generic rigs via manual bone mapping.

👀  Look-At Node — Makes a character's head, spine, and eyes smoothly track a target. Includes realistic eye micro-jitter (saccades) and soft angle limits. Reusable across any character.

🌊  Jiggle Physics Node — Secondary motion for hair, tails, capes, and chains. Add wind, turbulence, gravity, and collision bodies. Results feel physical and alive, not hand-keyed.

🛤️  Spline Trajectory Node — Draw a Bezier path in the Scene View and the character follows it during playback. Great for dashes, leaps, and cutscene movement — with ground snapping and banking.

🔒  IK Lock Node — Freeze a hand or foot to a surface contact point while the body continues to animate freely.


✨ FX & Gameplay Event Lanes

Place events directly on the composition timeline, in sync with your animation:

🔊  Audio — Trigger a sound at any frame, with volume, pitch, and 3D distance settings.
💥  Particle FX — Spawn particles attached to any bone, with movement paths and blend envelopes.
🎇  VFX Graph — Drive Unity VFX Graph effects and their parameters from the timeline.
📷  Camera Shake — Cinemachine Impulse shakes triggered on a specific frame.
📦  Spawn FX — Instantiate any prefab (sword trails, decals, muzzle flashes) from the timeline.
🦴  Transform FX — Animate any bone or object property from the timeline (great for eye blinks, wing folds, shield raises).
⚙️  Script Event — Notify your own C# code at any point in the animation, passing typed parameters (float, int, bool, string, or GameObject). Great for signalling gameplay systems, triggering sound managers, or driving UI — pair it with the runtime query API for critical logic.

Change the look of spawned effects per-character without making duplicate prefabs — just override the properties you need, per slot.


🎬 Animation Editor

For when you need to go deep into a clip:

🔓  Extract any locked FBX animation into a fully editable .anim asset in one click.
✂️  Trim, scale, reverse, insert, and crop time ranges directly.
📐  Edit individual keyframes — time, value, tangents, and tangent modes.
🔁  Mirror animations, smooth curves, remove redundant keys, and extract root motion.
🎯  Move bones in the Scene View and Auto-Key writes the keyframes for you.
👻  Ghost preview — edit a clip while seeing the full composition context blended behind it.


⚡ Runtime — Zero GC. Maximum Performance.

At runtime, MSMotion uses Unity's low-level PlayableGraph API. There are no Animator Controller state machines. No GC spikes. No string lookups.

▶️  Play, CrossFade, and sequence animations with a simple C# API.
🎭  Unlimited animation layers, allocated only when needed.
🎚️  FX events fire frame-accurately alongside the animation, with automatic intensity scaling during crossfades.
🔗  IK constraints activate and deactivate per animation — point a hand at a weapon target with one line of code.
♻️  All audio and particle effects are pooled — zero Instantiate/Destroy calls during gameplay.


🛠️ Compatibility

Engine: Unity 6 and above
Rig Support: Full support for both Humanoid and Generic rigs
Source Code: Full C# source included — no DLLs, no black boxes
Optional Integrations: Cinemachine · Unity VFX Graph · Unity Animation Rigging
Documentation: Full guides included in the Documentation~ folder


📞 Support & Community

📧 Email: [Insert Support Email Here]
🌐 Website: [Insert Website URL Here]
💬 Discord: [Insert Discord Invite Link Here]
📖 Docs: https://maharajastudiocustomerservice-cell.github.io/MaharajaStudioWeb/ms-motion-docs.html

MSMotion is built for developers who want AAA-quality animation pipelines without sacrificing performance, flexibility, or creative control.