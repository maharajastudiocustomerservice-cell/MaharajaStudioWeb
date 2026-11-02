# MaharajaStudio MSMotion

**MaharajaStudio MSMotion** is an advanced edit-mode animation authoring workspace, multi-actor choreography director, and high-performance runtime framework for Unity. It allows creators to edit native `.anim` clips, choreograph multi-character interactions with 0ms frame drift, dynamically summon entities, adapt pre-interaction approach locomotion with motion warping, overlay Inverse Kinematics (IK) solvers, and trigger 8 types of audio, particle, decal, and script events on a visual timeline.

Open the editor workspace from the Unity menu bar: `Tools > Maharaja Studio > MsMotion`.

---

## Key Capabilities

### 1. Edit-Mode Animation Clip Editor (UI Toolkit)
* **Direct Asset Modification**: Edit native Unity `.anim` assets directly inside the Editor.
* **Extraction Utility**: Extract read-only, imported model clips (from FBX or OBJ models) into fully editable local `.anim` assets with one click.
* **Timeline Operations**: Scrub, insert, delete (with ripple), duplicate, scale, reverse, crop, and trim timeline ranges.
* **Fine-Tuning Curve Editor**: Keyframe single-value or curve bindings with custom tangent modes (`Auto`, `Linear`, `Manual`).
* **Curve Optimization & Smoothing**: Median, Gaussian, and Average curve smoothing filters, keyframe reduction, and root motion extraction.
* **Skeletal Overlay**: Inspect bone paths and animation poses directly inside the Scene View.

### 2. Multi-Layer Composition Mixer & Choreography Director
* **PSD-Like Layering**: Blend multiple animation clips and procedural solvers together using override or additive modes.
* **Multi-Actor Choreography**: Direct synchronized 2, 3+ character choreography (dance duets, grapples, shared lifts, combat finishers) with 0ms frame drift and Humanoid/Generic rig mixing.
* **Actor Roster & Alignment Window**: Manage character roles, accent swatches, dynamic summon entities, and configure pre-interaction dynamic approach warping.
* **Dynamic Alignment (Motion Warping)**: Secondary characters travel smoothly to authored sync spots with automated locomotion scaling and terrain raycasting.
* **Dynamic Summons & Lifecycles**: Spawn weapons, dragons, Stand avatars, or familiars with automatic timeline lifecycle nodes (`SpawnActor`, `DestroyActor`) and object pooling.
* **Top Toolbar System**: Controls for play/loop, safety overrides, rig bindings, actor roster, dynamic alignment, and asset cleanup.

### 3. Procedural Solvers & Constraints
* **IK Override Node**: Blends Inverse Kinematics targets over time, featuring interactive scale handles in the viewport to apply Squash & Stretch.
* **Gait-Adaptive Foot IK**: Automatically aligns character feet to terrain normals, handles pelvic drops, and prevents joint popping. Works out-of-the-box on Humanoid rigs, and supports Generic rigs via manual bone mapping.
* **Look-At Solver**: Procedural head, spine, and eye targeting with biological eye jitter (saccades) and soft-angle limiting.
* **Jiggle Physics Node**: Spring-mass chain simulation for secondary motion (hair, chains, cloth) with built-in wind, turbulence, and collision bodies.
* **Trajectory Overrides**: Replaces standard character root motion with custom Bezier spline paths, supporting ground snaps and de Casteljau subdivisions.
* **Dynamic Bone Subdivision (Exp)**: Injects virtual bone chains into existing skeletons with auto-propagation.

### 4. FX Event Triggering & Cross-Actor Handover
* **8 Dedicated Event Lanes**: Place trigger blocks to spawn Audio, Particles, Decals, VFX Graphs, Custom Prefabs, Camera Shakes, Transforms, or Script Callbacks.
* **Decal FX**: Projects surface decals (blood, dirt, runes, skid marks) onto floors and walls via directional raycasts with normal angle filtering.
* **Cross-Actor Handover**: Seamlessly transfer weapons, torches, and spell effects between characters with phase-aware Scene View gizmos, HUD bars, and auto-keying.
* **Property Overrides**: Customize public variables or component fields (e.g. Light intensity, Material color) of spawned prefabs directly from the event timeline without duplicate assets.
* **FX Path Tools (Scene View HUD)**: Author complex Bezier spline movement paths for particle systems and visual effects using interactive node and preset tabs.

### 5. Designer-Friendly Interaction Overrides
* **`MSMotionInteractionOverrides` Asset**: Non-destructive post-export customization preset system.
* **Granular Field Toggles**: Independent checkboxes per field—only explicitly enabled values override the baseline.
* **Body Spacing Compensation**: Eliminate mesh clipping between differing creature sizes (e.g. giant monsters vs rogues) with frame-0 spatial offsets.
* **4-Category Dynamic Alignment Foldouts**: Locomotion & Gaits, Pathfinding & Navigation, Steering & Arrival Rotation, and Timing, Stride & Speed Bounds (with **⚡ Auto Stride** root-motion extraction).

---

## Runtime Framework Architecture

MSMotion's runtime framework is designed for low-overhead, high-efficiency playback inside games and builds.

### 1. PlayableGraph API Core
At the center of the runtime is `MSMotionAnimator`, which bypasses rigid, bloated Animator Controllers in favor of Unity's low-level **PlayableGraph API**. This provides:
* **Zero Runtime GC**: Eliminates garbage collection allocation spikes during animation playback.
* **On-The-Fly Layer Allocation**: Graph inputs and mixers are dynamically created and allocated when played, keeping memory use minimal.
* **Dynamic Rebinding**: Dynamic avatar and modular character rebinding via `Rebind(...)` and external graph attachment via `AttachToExternalGraph(...)`.

### 2. Multi-Actor Orchestration
* **`MSMotionInteraction`**: Orchestrates multi-character choreography playback with 1 line of C#, native Unity 6 `Awaitable` async execution, and dynamic participant departure (`StopActor` with `ContinueRemaining` / `StopAll` policies).
* **`MSMotionActorPool`**: Zero-allocation runtime pooling for ephemeral summons, companion entities, and decals.

### 3. Procedural Rig Controllers & Scaling
* **`MSMotionRigController`**: Evaluates custom rig chains, applying active IK solvers, pole vector constraints, and joint limits at runtime.
* **`MSMotionStretchApplicator`**: Inspects baked keyframe metadata and applies Squash & Stretch scale transformations to bone transforms at runtime with LOD distance culling.

### 4. Event and Trajectory Execution
* **`MSMotionFXPlayer`**: Monitors the playback playhead and triggers 8 types of timeline events (audio, particles, decals, Cinemachine camera shakes).
* **`MSMotionFXPool`**: Leverages object pooling for spawned prefabs and events, avoiding expensive `Instantiate` and `Destroy` calls.
* **`FXTrajectoryEvaluator`**: A stateless spline solver that dynamically moves spawned GameObjects along Bezier paths over their lifetime.

---

## Documentation

For a comprehensive guide on all features, refer to the local documentation directories:

### 1. Editor Tooling Guides
📂 [EditorTool/CompositionEditor/](EditorTool/CompositionEditor/)
*   `index.md`: Global composition mixer settings, top toolbar, and hotkeys.
*   `actor-roster-window.md`: Character roster management, dynamic summons, and motion warping.
*   `actor-lifecycle-nodes.md`: Spawn Actor and Destroy Actor timeline nodes.
*   `interaction-overrides-inspector.md`: Post-export preset authoring and dynamic alignment foldouts.
*   `animation-clip-node.md`: Speed curves and timeline operations.
*   `ik-override-node.md` & `ik-rig-configuration.md`: IK solver and rig configurations.
*   `jiggle-physics-node.md`: Physics setups and colliders.
*   `decal-fx-node.md`: Surface decal projection and pooling.
*   `fx-nodes-overview.md` & `batch-export.md`: Handover, property overrides, and queue managers.

### 2. Runtime Framework Guides
📂 [RuntimeSystem/](RuntimeSystem/)
*   `index.md`: System architecture and component interactions.
*   `quick-start.md`: Setting up characters and scripting playback in 5 minutes.
*   `core-animation-system.md`: PlayableGraph, layers, transition APIs, and dynamic avatar rebinding.
*   `multi-actor-interaction.md`: Synchronized choreography, dynamic departure, summons, and prop handovers.
*   `interaction-overrides.md`: Post-export preset authoring, 4 alignment foldouts, and C# API.
*   `fx-event-system.md`: Player timing, trajectories, overrides, and script event buses.
*   `rigging-and-ik-system.md`: Rig controllers, target matching, and joint stabilization.
*   `stretch-and-scale-system.md`: Squash & Stretch applicator, and LOD culling ranges.
*   `optimization-and-best-practices.md`: Allocation culling, caches, and layer organization.

---

## 🎮 Interactive Windows Demo Build

Try MSMotion before you integrate! A standalone, high-fidelity cinematic demo build is available for Windows showcasing runtime PlayableGraph evaluation, Burst compilation, 8 FX event lanes, and synchronized multi-actor choreography.

👉 **[Download the Free Windows Demo Build via GitHub](https://github.com/maharajastudiocustomerservice-cell/MSMotion-Demo-Build-win/releases/tag/Demo)**

---

## Support & Community

* 📧 **Email**: [maharajastudiocustomerservice@gmail.com](mailto:maharajastudiocustomerservice@gmail.com)
* 🌐 **Website**: [Maharaja Studio MSMotion](https://maharajastudiocustomerservice-cell.github.io/MaharajaStudioWeb/ms-motion.html)
* 💬 **Discord**: [Join Discord](https://discord.gg/GamF5bez3h)
* 📖 **Online Docs**: [MSMotion Online Documentation](https://maharajastudiocustomerservice-cell.github.io/MaharajaStudioWeb/ms-motion-docs.html)
* ▶️ **YouTube Tutorials**: [Maharaja Studio Tutorials](https://youtube.com/@king_of_games-l9e?si=EleZSFthz6ZBPPao)
