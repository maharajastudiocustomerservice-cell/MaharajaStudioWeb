# Animation Editor

The **Animation Editor** is the central interface in MSMotion for authoring and editing character animations in edit mode. It provides a visual timeline-based environment for directly modifying native Unity Animation Clips (`.anim` files) with complete Undo/Redo support, real-time Scene view previews, and advanced keyframe manipulation tools.

Unlike Unity's built-in Animation window, which is object-centric and requires setting up Animators and recording states, the MSMotion Animation Editor is **asset-first**. You load and edit the animation asset directly, previewing the results against any compatible character model in the scene.

---

## Editor Interface Layout

When you open the Animation Editor (**Tools > Maharaja Studio > MsMotion > Animation Editor**), the interface is divided into three main functional zones:

```
+-----------------------------------------------------------------------------+
|                               Top Toolbar                                   |
+-----------------------------------------------------------------------------+
|                     |                                                       |
|                     |                                                       |
|                     |                   Timeline Ruler                      |
|                     +-------------------------------------------------------+
|    Left Sidebar     |                                                       |
|       Panels        |                   Scrubber & Tracks                   |
|                     |                                                       |
|                     |                                                       |
|                     |                                                       |
+-----------------------------------------------------------------------------+
```

### 1. Top Toolbar
The top toolbar contains global controls for preview setup, play/pause clock manipulation, and undo/redo functions:
* **Preview Root**: A field to assign a character GameObject from the Scene. This character is used to preview the animation changes in real time.
* **Play / Stop / Loop**: Playback controls to run or halt the animation in edit mode.
* **Reset Root**: A toggle that forces the character to snap back to its original coordinate origin when the animation loop starts over.
* **Auto-Key**: Toggles automatic recording of keyframes when character bones are transformed in the Scene view.
* **Offset Mode**: When active alongside Auto-Key, transforming a bone shifts the *entire* animation curve by that amount as a constant offset, rather than overwriting only the current frame.
* **Undo / Redo**: Quick buttons to step backward or forward through your edits.
* **Export Pose**: Bakes the current pose of the preview character into a new, single-frame Animation Clip asset.
* **Settings (⚙)**: Opens the settings window to customize colors, row heights, and layout scales.

### 2. Left Sidebar Panels
An accordion-style container of collapsible sections containing settings and action buttons:
* **Clip**: Load assets, extract editable copies of read-only clips, and manage the clipboard.
* **Range**: Perform crop, delete, shift, stretch, snap, and bake operations across selected time regions.
* **Curves**: Search, filter, select, and delete animated property bindings.
* **Key Editor**: Detailed numerical control over a single selected keyframe's time, frame, value, and mathematical tangents.
* **Advanced Tools**: Panels for **Mirror Pose**, **Tween Machine**, **Keyframe Optimizer**, **Keyframe Smoothing**, and **Extract Root Motion**.
* **Viewport**: Toggle bone overlay shapes, colors, and name tags.
* **IK / FK Solver**: Controls for locking IK targets and blending procedural IK chains with base skeletal poses.
* **Animation Events**: Visual list of runtime event markers triggered by the clip.

### 3. Timeline Scrubber & Tracks
The main workspace where keyframes are visualized and manipulated:
* **Timeline Ruler**: Shows time in seconds or frames, and hosts event markers.
* **Scrubber**: The red vertical line indicating the current preview time. Drag the scrubber handle to scrub time.
* **Tracks**: Horizontal rows displaying keyframes for selected curves. Keys are colored by curve type (blue for floats, orange for object references).

---

> [!TIP]
> You can navigate the timeline zoom by holding **Ctrl** (or **Alt**) while using your mouse scroll wheel over the track area. This makes it easy to switch between coarse range selections and precise, frame-level keyframe adjustments.

---

## Keyboard Shortcuts

The Animation Editor supports the following hotkeys to speed up your editing workflow. Make sure the editor window is in focus when using these shortcuts:

### Playback & Navigation

| Hotkey | Action |
|:---|:---|
| **Space** | Play or pause animation playback. |
| **Left Arrow** | Step the playhead backward by 1 frame. |
| **Right Arrow** | Step the playhead forward by 1 frame. |
| **Shift + Left Arrow** | Step the playhead backward by 10 frames. |
| **Shift + Right Arrow** | Step the playhead forward by 10 frames. |
| **Home** | Jump the playhead to the beginning of the animation (0.0s). |
| **L** | Toggle playback loop option (**Loop**). |

### Editing Actions

| Hotkey | Action |
|:---|:---|
| **Delete** / **Backspace** | Deletes elements based on selection context: <br> • If keyframes are selected on the timeline, deletes those keys. <br> • If a single key is active in the Key Editor list, deletes that key. <br> • If property curves are highlighted in the Curves panel, deletes those curves. |
| **Ctrl + Z** | Undo the last action. |
| **Ctrl + Y** / **Ctrl + Shift + Z** | Redo the last undone action. |
| **Ctrl + C** | Copy selected keyframes to the clipboard (or copy the active time range selection if no keys are highlighted). |
| **Ctrl + X** | Cut selected keyframes to the clipboard (or cut the active time range selection if no keys are highlighted). |
| **Ctrl + V** | Paste clipboard keyframes at the playhead time (or paste the copied time range). |

### Viewport & Tools

| Hotkey | Action |
|:---|:---|
| **K** | Toggle **Auto-Key** recording mode. |
| **B** | Toggle **Show Bones** overlay in the Scene view. |

