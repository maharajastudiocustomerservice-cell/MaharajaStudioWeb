# Composition Editor

The **Composition Editor** is the most advanced feature in MSMotion. It provides a multi-layer, timeline-based animation mixer and solver environment for combining standard animations, procedural constraints (such as Look-At and Foot IK), secondary physics (Jiggle), and runtime FX events into a single, cohesive playback sequence.

Unlike the Animation Editor which works on a single, isolated animation clip, a **Composition** acts like a Photoshop document (PSD) for character motion. You stack clips, override poses, and inject physics solvers across separate layers, blending them together to author complex character behaviors.

Compositions are saved as self-contained `.asset` files in your project. You can create a new Composition by right-clicking in the Project window and choosing **Create > MaharajaStudio > MSMotion Composition**.

---

## Editor Window Layout

To open the Composition Editor, choose **Tools > Maharaja Studio > MsMotion > Composition Editor** from the Unity menu bar. The window is divided into several main sections:

```
+-----------------------------------------------------------------------------+
|                               Top Toolbar                                   |
+-----------------------------------------------------------------------------+
|                     |                                                       |
|  Left Sidebar       |                     Timeline View                     |
|  Layers Panel       |           (Tracks, Scrubber, Loop Region)            |
|                     |                                                       |
+---------------------+-------------------------------------------------------+
|                                                                             |
|                           Inspector / Details Panel                         |
|                                                                             |
+-----------------------------------------------------------------------------+
```

### 1. Top Toolbar
Provides global controls for active preview, playback, asset actions, and utility windows:

*   **Preview Root**: An object picker field to assign a character GameObject from the active Scene. Once assigned, this character is bound to the playable graph to preview the blended animation layers, IK solvers, physics simulation, and FX triggers in real time.
*   **Refresh Bones (Refresh Icon)**: Re-binds bone hierarchies and updates the context for all active FX slots and scene overlays, forcing a Scene View redraw to align bone alignments.
*   **Set Origin (Avatar Pivot Icon)**: Locks the character preview's current position, rotation, and scale as the composition's permanent starting origin. When playback loops or resets, the character snaps back to these exact coordinates, preventing position drift or starting displacement.
*   **Height Clamp (↕ Icon)**: Opens the Height Clamp configuration panel.
    *   **Enable Height Clamp**: Toggles vertical constraint enforcement on the preview character's root.
    *   **Min Height / Max Height**: Float fields to define a vertical movement corridor.
    *   **Viewport Interaction**: Displays a green horizontal plane for the minimum height boundary and a red plane for the maximum height boundary in the Scene View. You can drag these planes using standard position handles to adjust the vertical bounds.
*   **Play/Pause (► / ❚❚)**: Plays or pauses composition playback in edit mode.
*   **Loop Playback (Loop Icon)**: Cycles playback automatically back to the beginning when reaching the end of the loop region.
*   **Reset Root (📍 Pin Icon)**: When active, resets the character to the captured starting origin coordinates whenever the playback loops back to the start.
*   **Auto-Key (🔑 Key Icon)**: When toggled on, rotating or moving bones inside the Scene View automatically inserts keyframe values into the active clip or pose node at the playhead's current frame.
*   **Mute Events (Speaker Icon)**: Globally silences all animation events and FX slot triggers during playback and scrubber sweeps.
*   **Allow Editor FX (Safety Icon)**: Permits Script Events and Property Overrides to execute in the Editor Preview. 
    > [!WARNING]
    > Enabling this option allows script event triggers to modify active scene components. Use with care to avoid permanent modifications to non-playback scene assets.
*   **Bone Rendering (🦴 Bone Icon)**: Shows or hides a solid overlay skeleton of the character in the Scene View for easy joint selection and visual troubleshooting.
*   **Undo / Redo (↩ / ↪)**: Undoes the last edit action or redoes the last undone action.
*   **New Composition (📄 Page Icon)**: Creates a new, blank Composition asset (.asset) in the project folders.
*   **Open Composition (📂 Folder Icon)**: Displays a file finder to select and open an existing Composition asset.
*   **Rig Config (🦴 Bone Icon)**: Opens the **IK Rig Config Editor Window** to set up custom inverse kinematics chains, solvers, presets, and joint constraints. See [IK Rig Configuration](ik-rig-configuration.md) for more details.
*   **Export (💾 Disk Icon)**: Opens the **Export Options Window** to bake the multi-layer timeline composition into a single, clean Animation Clip or FBX asset. See [Export Options](export-options.md) for details.
*   **Cleanup Sub-Assets (🧹 Broom Icon)**: Scans the composition asset for orphaned or unused sub-clip assets and permanently deletes them to optimize project asset sizes.
    > [!CAUTION]
    > Running this cleanup clears the editor's undo history for the session.
*   **Settings (Gear Icon)**: Opens the **MSMotion Settings Window** to adjust general editor options, timeline rows, visuals, snapping defaults, and undo boundaries. See [Editor Settings](editor-settings.md) for details.

### 2. Breadcrumb Bar
Located directly below the global Top Toolbar. It displays the folder path and asset hierarchy of the currently loaded Composition asset:
*   **Interactive Paths**: Each folder name and asset in the breadcrumb path is clickable.
*   **Asset Locating**: Clicking a path element pings that specific folder or the active composition asset inside the Project window, allowing fast navigation within large directories.


### 3. Left Sidebar (Layers Panel)
Manages the stacking and blending behavior of your animation layers. See the [The PSD Layer Model](#the-psd-layer-model) section below for detailed workflows.

### 4. Timeline View
Displays horizontal tracks corresponding to each layer. Timeline blocks (Nodes) can be dragged, resized, split, and duplicated here.
* **Timeline Ruler**: Shows time in seconds or frames, and hosts custom event markers.
* **Scrubber**: The red vertical playhead. Drag to scrub through composition playback.
* **Loop Region**: A highlighted region on the ruler. Drag the handles to constrain playback preview to a specific sub-range.
* **Markers**: Text tags placed on the timeline ruler for reference or transition anchors.

### 5. Inspector / Details Panel
Surfaces the options and properties of the currently selected layer or timeline block.

---

## The PSD Layer Model

Compositions evaluate layers from **bottom to top** (higher layers in the list draw on top of lower ones, blending according to their weights and masks).

```
+----------------------------------------+
| [Layer 3] Override (Upper Body Mask)   | -> Overwrites Layer 2 & 1 (Chest up)
+----------------------------------------+
| [Layer 2] Additive (Jiggle Physics)    | -> Adds jiggle on top of Layer 1
+----------------------------------------+
| [Layer 1] Base (Full Body Walk Clip)   | -> Drives primary motion
+----------------------------------------+
```

Each layer in the sidebar contains the following user-facing controls:

| Control | Function |
|:---|:---|
| **Enable (Mute)** | A toggle (checkbox/eye icon) to include or exclude the layer from playback and baking previews. |
| **Solo** | Mutes all other layers in the composition so you can audit this layer in isolation. |
| **Lock** | Prevents editing, moving, or resizing of any timeline blocks on this layer. |
| **Blending Mode** | Defines how the layer mixes with layers below it:<br> • **Override**: Fully replaces motion from lower layers (restricted only by the Avatar Mask).<br> • **Additive**: Calculates the relative pose difference and adds it on top of the combined lower layers (ideal for secondary breathing, recoil, or physics). |
| **Weight** | A slider from `0.0` (no influence) to `1.0` (full strength) representing how much of this layer is blended in. |
| **Use Curve** | Enables automating the layer weight using an Animation Curve instead of a static slider, letting you fade layers in and out at exact timeline coordinates. |
| **Layer Mask** | Accepts a Unity AvatarMask asset. Only bone hierarchies checked in this mask are animated by this layer. Unmasked bones bleed through from lower layers. |

---

## Keyboard Shortcuts

Use these hotkeys to navigate the timeline and perform edits inside the Composition Editor. Ensure the window is focused:

### Playback & Navigation

| Hotkey | Action |
|:---|:---|
| **Space** | Play or pause composition playback. |
| **Right Arrow** | Step playhead forward by 1 frame. |
| **Left Arrow** | Step playhead backward by 1 frame. |
| **Shift + Right Arrow** | Step playhead forward by 10 frames. |
| **Shift + Left Arrow** | Step playhead backward by 10 frames. |
| **Home** | Jump playhead back to the beginning (0.0s). |
| **L** | Toggle playback loop option. |
| **M** | Toggle Mute Events globally. |

### Editing Actions

| Hotkey | Action |
|:---|:---|
| **Delete** / **Backspace** | Deletes all currently selected timeline blocks. |
| **Ctrl + Z** | Undo the last action. |
| **Ctrl + Y** / **Ctrl + Shift + Z** | Redo the last undone action. |
| **Ctrl + C** | Copy the first selected block to the clipboard. |
| **Ctrl + X** | Cut the first selected block to the clipboard. |
| **Ctrl + V** | Paste clipboard block onto the active layer at the playhead time. |
| **Ctrl + D** | Duplicate all selected timeline blocks. |
| **S** | Split selected timeline blocks at the current playhead time. |

### Viewport & View Toggles

| Hotkey | Action |
|:---|:---|
| **K** | Toggle **Auto-Key** recording mode. |
| **B** | Toggle **Show Bones** overlay in the Scene View. |

---

## Related Guides

* **Core Nodes**: Learn about the primary timeline blocks in [Animation Clip Nodes](animation-clip-node.md) and [Pose Nodes](pose-node.md).
* **Solvers & Constraints**: Configure limb targets in [IK Override Nodes](ik-override-node.md), face-tracking in [Look-At Nodes](look-at-node.md), and grounding in [Foot IK Nodes](foot-ik-node.md).
* **Procedural Modifiers**: Add simulation behaviors in [Jiggle Physics Nodes](jiggle-physics-node.md) and drive pathways in [Trajectory Override Nodes](trajectory-override-node.md).
* **FX Triggers**: Attach runtime triggers, audio, or particle events using the [FX Nodes Overview](fx-nodes-overview.md).
* **Baking & Pipelines**: Configure [Export Options](export-options.md), manage [Batch Export Queue](batch-export.md), and adjust preferences in [Editor Settings](editor-settings.md).
* **Project Maintenance**: Purge and manage embedded clip data in the [Metadata Manager](metadata-manager.md) or resolve layout errors in [Troubleshooting](troubleshooting.md).

