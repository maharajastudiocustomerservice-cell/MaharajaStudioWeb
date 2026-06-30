# MaharajaStudio MSMotion

**MaharajaStudio MSMotion** is an advanced edit-mode animation authoring workspace and a high-performance runtime blending framework for Unity. It allows creators to edit, trim, crop, retime, and preview native `.anim` clips, overlay Inverse Kinematics (IK) solvers, and trigger complex audio, particle, and script events on a visual timeline.

Open the editor workspace from the Unity menu bar: `Tools > Maharaja Studio > MsMotion`.

---

## Key Capabilities

### 1. Edit-Mode Animation Clip Editor (UI Toolkit)
* **Direct Asset Modification**: Edit native Unity `.anim` assets directly inside the Editor.
* **Extraction Utility**: Extract read-only, imported model clips (from FBX or OBJ models) into fully editable local `.anim` assets with one click.
* **Timeline Operations**: Scrub, insert, delete, duplicate, scale, reverse, and trim timeline ranges.
* **Fine-Tuning Curve Editor**: Keyframe single-value or curve bindings with custom tangent modes (`Auto`, `Linear`, `Manual`).
* **Skeletal Overlay**: Inspect bone paths and animation poses directly inside the Scene View.

### 2. Multi-Layer Composition Mixer
* **PSD-Like Layering**: Blend multiple animation clips and procedural solvers together using override or additive modes.
* **Layer Constraints**: Fine-tune layer weights using custom curves and isolate bones using Unity `AvatarMask` assets.
* **Timeline Utilities**: Set loop regions, place sync markers, and utilize a Breadcrumb Bar to navigate parent assets easily.
* **Top Toolbar System**: A unified interface of **19 control elements** managing play/loop, safety overrides, rig bindings, and asset cleanup.

### 3. Procedural Solvers & Constraints
* **IK Override Node**: Blends Inverse Kinematics targets over time, featuring interactive scale handles in the viewport to apply Squash & Stretch.
* **Gait-Adaptive Foot IK**: Automatically aligns character feet to terrain normals, handles pelvic drops, and prevents joint popping. Works out-of-the-box on Humanoid rigs, and supports Generic rigs via manual bone mapping.
* **Look-At Solver**: Procedural head, spine, and eye targeting with biological eye jitter (saccades) and soft-angle limiting.
* **Jiggle Physics Node**: Spring-mass chain simulation for secondary motion (hair, chains, cloth) with built-in wind, turbulence, and collision bodies.
* **Trajectory Overrides**: Replaces standard character root motion with custom Bezier spline paths, supporting ground snaps and de Casteljau subdivisions.

### 4. FX Event Triggering & Property Overrides
* **Dedicated Event Lanes**: Place trigger blocks to spawn audio, particles, custom prefabs, camera shakes, or trigger custom scripting callbacks.
* **Property Overrides**: Customize public variables or component fields (e.g. Light intensity, Material color) of spawned prefabs directly from the event timeline without duplicate assets.
* **FX Path Tools (Scene View HUD)**: Author complex Bezier spline movement paths for particle systems and visual effects using interactive node and preset tabs.

---

## Runtime Framework Architecture

MSMotion's runtime framework is designed for low-overhead, high-efficiency playback inside games and builds.

### 1. PlayableGraph API Core
At the center of the runtime is `MSMotionAnimator`, which bypasses rigid, bloated Animator Controllers in favor of Unity's low-level **PlayableGraph API**. This provides:
* **Zero Runtime GC**: Eliminates garbage collection allocation spikes during animation playback.
* **On-The-Fly Layer Allocation**: Graph inputs and mixers are dynamically created and allocated when played, keeping memory use minimal.
* **2-Input Layer Mixer Pattern**: Every override layer blends between a constant default/idle fallback playable and the active action playable to ensure click-free crossfades.

### 2. Procedural Rig Controllers
* **`MSMotionRigController`**: Evaluates custom rig chains, applying active IK solvers, pole vector constraints, and joint limits at runtime.
* **`MSMotionStretchApplicator`**: Inspects baked keyframe metadata and applies Squash & Stretch scale transformations to bone transforms at runtime.

### 3. Event and Trajectory Execution
* **`MSMotionFXPlayer`**: Monitors the playback playhead and triggers timeline events (audio, particles, Cinemachine camera shake).
* **`MSMotionFXPool`**: Leverages object pooling for spawned prefabs and events, avoiding expensive `Instantiate` and `Destroy` calls.
* **`FXTrajectoryEvaluator`**: A stateless spline solver that dynamically moves spawned GameObjects along Bezier paths over their lifetime.

---

## Documentation

For a comprehensive guide on all features, refer to the local documentation directories:

### 1. Editor Tooling Guides
📂 [EditorTool/CompositionEditor/](file:///c:/Users/Soutick/ToolTester2_Unity6/Assets/com.maharajastudio.animation-editor/Documentation~/EditorTool/CompositionEditor/)
This folder contains detailed guides covering:
*   `index.md`: Global composition mixer settings and hotkeys.
*   `animation-clip-node.md`: Speed curves and timeline operations.
*   `ik-override-node.md` & `ik-rig-configuration.md`: IK solver and rig configurations.
*   `jiggle-physics-node.md`: Physics setups and colliders.
*   `fx-nodes-overview.md` & `batch-export.md`: Property overrides and queue managers.

### 2. Runtime Framework Guides
📂 [RuntimeSystem/](file:///c:/Users/Soutick/ToolTester2_Unity6/Assets/com.maharajastudio.animation-editor/Documentation~/RuntimeSystem/)
This folder contains detailed API references and integration guides:
*   [index.md](file:///c:/Users/Soutick/ToolTester2_Unity6/Assets/com.maharajastudio.animation-editor/Documentation~/RuntimeSystem/index.md): System architecture and component interactions.
*   [quick-start.md](file:///c:/Users/Soutick/ToolTester2_Unity6/Assets/com.maharajastudio.animation-editor/Documentation~/RuntimeSystem/quick-start.md): Setting up characters and scripting playback.
*   [core-animation-system.md](file:///c:/Users/Soutick/ToolTester2_Unity6/Assets/com.maharajastudio.animation-editor/Documentation~/RuntimeSystem/core-animation-system.md): PlayableGraph, layers, and transition APIs.
*   [fx-event-system.md](file:///c:/Users/Soutick/ToolTester2_Unity6/Assets/com.maharajastudio.animation-editor/Documentation~/RuntimeSystem/fx-event-system.md): Player timing, trajectories, overrides, and script event buses.
*   [rigging-and-ik-system.md](file:///c:/Users/Soutick/ToolTester2_Unity6/Assets/com.maharajastudio.animation-editor/Documentation~/RuntimeSystem/rigging-and-ik-system.md): Rig controllers, target matching, and joint stabilization.
*   [stretch-and-scale-system.md](file:///c:/Users/Soutick/ToolTester2_Unity6/Assets/com.maharajastudio.animation-editor/Documentation~/RuntimeSystem/stretch-and-scale-system.md): Squash & Stretch applicator, and LOD culling ranges.
*   [optimization-and-best-practices.md](file:///c:/Users/Soutick/ToolTester2_Unity6/Assets/com.maharajastudio.animation-editor/Documentation~/RuntimeSystem/optimization-and-best-practices.md): Allocation culling, caches, and layer organization.
