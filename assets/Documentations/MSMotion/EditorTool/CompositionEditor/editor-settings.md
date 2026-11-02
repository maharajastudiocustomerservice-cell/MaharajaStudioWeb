# Editor Settings

The **MSMotion Settings** window acts as a central hub for configuring your workspace preferences, timeline rendering options, snapping mechanics, viewport overlays, and undo buffers.

To open the Settings window, click the **Settings (Gear Icon)** on the composition top toolbar or choose **Tools > Maharaja Studio > MsMotion > Setting** from the Unity menu bar.

---

## Window Structure

The window features a sidebar list on the left to select categories, and a main vertical scrolling content panel on the right:

```
+------------------------+-----------------------------------------+
|      Left Sidebar      |            Right Content Area           |
| (Settings Categories)  |  (Scrollable panels and configuration)  |
+------------------------+-----------------------------------------+
```

---

## 1. General Category
Controls defaults for composition creation and editing behavior in the timeline.

### Composition Defaults Panel
*   **Default Frame Rate**: The frame rate applied to newly created compositions (presets: `24`, `30`, `60`, `120` FPS).
*   **Default Layer Blend Mode**: The default mixing mode assigned when adding a new layer:
    *   *Override*: Replaces motion from lower layers.
    *   *Additive*: Adds delta motion on top of lower layers.

### Editing Behaviour Panel
*   **Ripple Delete**: When enabled, deleting a timeline block automatically shifts all subsequent blocks on that same layer to the left, closing the gap. When disabled, deleting a block leaves an empty gap.

---

## 2. Timeline & Playback Category
Fine-tunes the timeline view layout, playback speed, and horizontal scroll mechanics.

### View Panel
*   **Default Zoom (px/s)**: Pixels-per-second zoom scale applied when opening a composition (range: `20` to `800` px/s).
*   **Default Waveform Display**: The visual waveform drawn on clip nodes:
    *   *First Curve*: Draws a line matching the first float track of the animation clip.
    *   *Energy Bars*: Renders vertical RMS energy level bars.
*   **Time Display Format**: The format of the timeline ruler and time fields:
    *   *Seconds*: (e.g., `1.25s`)
    *   *Frames*: (e.g., `F75`, based on composition frame rate)
    *   *SMPTE*: (e.g., `00:00:01:15` timecode)
*   **Enable Loop Region by Default**: Automatically activates a loop region across the entire duration when a composition is first opened.

### Playback Panel
*   **Default Preview Time Scale**: The starting playback speed (range: `0.1×` to `4.0×`). Only affects editor previews and does not affect the exported clip.

### Navigation Panel
*   **Horizontal Scroll Sensitivity**: Mouse wheel multiplier when scrolling horizontally through tracks (range: `5` to `120`).
*   **Playhead Auto-Scroll Margin (px)**: How close the playhead can get to the track boundary before the view automatically pans to follow it.

---

## 3. Interaction & Workflow Category
Configures snapping constraints and duration parameters for placing nodes.

### Workflow Options Panel
*   **Slot Snap Mode**: Snapping behavior when dragging clips:
    *   *None*: Free movement.
    *   *Frame*: Snaps to ruler frame increments.
    *   *SlotBoundaries*: Snaps to the start and end borders of adjacent clips.
    *   *Markers*: Snaps to custom timeline ruler markers.
    *   *All*: Snaps to frames, adjacent borders, and markers.
*   **Snap Tolerance (px)**: Distance threshold in pixels where snapping occurs (range: `1` to `50` px).
*   **Trim Handle Width (px)**: Size of the interactive edge drag handles on timeline blocks (range: `4` to `20` px).
*   **Auto-Select New Slots**: Automatically selects a timeline node in the inspector as soon as it is created.
*   **Default New Slot Duration (s)**: Duration in seconds for newly created blank or override slots (range: `0.1s` to `10.0s`).

---

## 4. Clip Editor Category
Default values applied when using the standalone Animation Clip Editor window.

### Clip Editor Defaults Panel
*   **Default Frame Rate**: FPS assigned to new clips inside the editor (range: `1` to `120`).
*   **Default Transition (s)**: The default crossfade duration for transition curves (range: `0.0s` to `5.0s`).
*   **Default Paste Mode**: Keyframe pasting behavior (e.g., insert, overwrite).
*   **Auto-Key Enabled by Default**: Toggles whether Auto-Keying is active when opening the clip editor.
*   **Optimize Position Tolerance**: Position curve compression threshold.
*   **Optimize Rotation Tolerance**: Rotation curve compression threshold.

---

## 5. Undo / Redo Category
Manages editing memory and transaction grouping constraints.

### Undo Stack Panel
*   **Max History Count**: The maximum number of undo steps stored in memory per composition.
*   **Grouping Window (s)**: Microsecond threshold where continuous adjustments (like dragging a slider or rotating a bone in the scene view) are merged into a single undo command instead of creating individual entries.

### Danger Zone Panel
*   **Clear All Undo History**: Erases the active session undo/redo stack for all open compositions. Use this to free system memory during long editing sessions.

---

## 6. Visuals & Viewport Category
Customizes Scene View bone renderings, timeline colors, and visual overlays.

### Bone Overlay Panel
*   **Show Bone Overlay by Default**: Automatically activates skeleton drawing when opening a composition.
*   **Animated Bones Only**: Restricts skeletal outlines to bones that contain active animation curves.
*   **X-Ray (Draw Over Mesh)**: Renders the skeletal bone overlays on top of the character's geometry.
*   **Show Local Axes**: Renders three-axis coordinate gizmos (red X, green Y, blue Z) on each bone.
*   **Show Bone Names**: Draws text label tags next to each joint.
*   **Joint Size**: The size of the joint nodes (range: `0.006` to `0.08`).
*   **Bone Shape**: The visual segment geometry:
    *   *Pyramid*: Renders standard volumetric bones.
    *   *Line*: Renders simple single lines.
*   **Bone Width**: Thickness scale for volumetric pyramid bones (range: `0.01` to `0.2`).
*   **Bone Colors**: Customize colors for:
    *   *Normal Bone Color*
    *   *Animated Bone Color*
    *   *Selected Bone Color*
    *   *Masked Bone Color*

### Timeline Visuals Panel
*   **Timeline Row Height**: Vertical height of layer rows (range: `20` to `80` px).
*   **Row Background (Even / Odd)**: Solid row stripe colors.
*   **Layer Auto-Color Style**: The style style applied to new layers.
*   **Selection & Playhead Colors**: Custom colors for selection boxes, loop regions, and playhead lines.

### Key Colours Panel
*   **Key Colors**: Customize timeline keyframe colors for *Float Keys*, *Object Keys*, *Selected Keys*, and *Edited Keys*.

### Onion Skinning Panel
Renders semi-transparent ghost poses of past and future frames to help visualize the motion curve:
*   **Enable Onion Skinning**: Toggles ghost rendering on or off.
*   **Frame Step**: Inter-frame spacing count for drawing ghost steps.
*   **Past Frames / Future Frames**: Count of past and future frames to display.
*   **Opacity Decay**: Fade coefficient for distant frames.
*   **Show In Playback**: Displays ghost frames during active timeline playback.

---

## 7. Export Workflow Category
Configures default paths, one-click bypass behaviors, companion asset packaging, and global multi-actor export rules.

### Export Path & Behaviors Panel
*   **Default Export Directory**: The default folder where baked Animation Clips, FBX files, and companion assets are created. Use the **Browse...** button to select an in-project directory.
*   **Bypass Save Prompt**: When enabled, clicking one-click export immediately writes to the Default Export Directory without displaying an OS file save dialog.

### Companion Assets (Config, Manifest & Interaction)
Controls where auto-generated companion assets are saved relative to the exported animation clip:
*   **Config Save Behavior**: Where to store auto-generated `MSMotionAnimationConfig` (`_config.asset`) files:
    *   *NextToClip*: In the same folder as the baked animation clip.
    *   *Subfolder*: Inside a `Configs/` subfolder.
    *   *CustomDirectory*: In a designated custom project path.
*   **Config Custom Path**: Folder path used when Config Save Behavior is set to *CustomDirectory*.
*   **Manifest Save Behavior**: Where to store auto-generated `MSMotionFXManifest` (`_fx.asset`) files:
    *   *NextToClip*: In the same folder as the baked animation clip.
    *   *Subfolder*: Inside a `Manifests/` subfolder.
    *   *CustomDirectory*: In a designated custom project path.
*   **Manifest Custom Path**: Folder path used when Manifest Save Behavior is set to *CustomDirectory*.
*   **Interaction Save Behavior**: Where to store auto-generated `MSMotionInteractionConfig` (`_interaction.asset`) files for multi-actor compositions:
    *   *NextToClip*: In the same folder as the baked animation clips.
    *   *Subfolder*: Inside an `Interactions/` subfolder.
    *   *CustomDirectory*: In a designated custom project path.
*   **Interaction Custom Path**: Folder path used when Interaction Save Behavior is set to *CustomDirectory*.

### Multi-Actor Export Defaults Panel
Provides default settings applied when exporting compositions that contain multiple participant actors:
*   **Default Export Scope**: Pre-selected actor export scope:
    *   *AllActorsSeparateClips*: Bakes each participant actor into an individual animation clip.
    *   *ActiveActorOnly*: Bakes only the currently active/lead actor.
    *   *CustomSelection*: Opens the export window with user-defined actor selection checkboxes.
*   **Filename Suffix Style**: How secondary actor output animation and companion files are named:
    *   *ActorDisplayName*: Appends the sanitized actor role name (e.g., `Walk_Hero.anim`, `Walk_Partner.anim`).
    *   *ActorId*: Appends the internal actor identifier (e.g., `Walk_actor_0.anim`, `Walk_actor_1.anim`).
*   **Auto-Generate Interaction Config**: Automatically generates and links an `MSMotionInteractionConfig` asset binding all participant tracks, relative frame-0 offsets, dynamic alignment data, and companion animation configs.
*   **Isolate FX Manifest Per Actor**: Filters companion FX manifest events so each participant actor's manifest only contains FX nodes assigned to that specific actor rather than duplicating all scene events.
*   **Reset Actors To Origin On Export**: Automatically restores all participant preview actors to their canonical scene origins before and after each bake pass to prevent spatial coordinate drift.

### Humanoid Root Motion Defaults Panel
Default settings applied to exported humanoid animation clips (these can be further customized per-export in the Export Options window):
*   **Loop Time**: Enables animation looping on the exported clip.
*   **Loop Pose**: Smoothly blends the loop boundary frames.
*   **Cycle Offset**: Loop cycle offset (range: `0.0` to `1.0`).
*   **Root Transform Rotation**:
    *   *Bake Into Pose (Rot)*: Bakes orientation into the character's pose.
    *   *Based Upon (Rot)*: Reference orientation (`Original`, `BodyOrientation`).
    *   *Offset (Rot)*: Angular rotation offset in degrees.
*   **Root Transform Position (Y)**:
    *   *Bake Into Pose (Y)*: Bakes vertical motion into the pose.
    *   *Based Upon (Y)*: Reference vertical level (`Original`, `CenterOfMass`, `Feet`).
    *   *Offset (Y)*: Height offset in meters.
*   **Root Transform Position (XZ)**:
    *   *Bake Into Pose (XZ)*: Bakes horizontal position into the pose.
    *   *Based Upon (XZ)*: Reference horizontal coordinates (`Original`, `CenterOfMass`).
*   **Mirror**: Flips the exported animation horizontally left-to-right.

---

## Related Guides

*   **Main Workspace**: Get an overview of the editor in the [Composition Editor Index](index.md).
*   **Baking Clips**: Bake animations with [Export Options](export-options.md).
*   **Configuring Rigs**: Learn how to prepare skeletons for IK overlays in [IK Rig Configuration](ik-rig-configuration.md).
