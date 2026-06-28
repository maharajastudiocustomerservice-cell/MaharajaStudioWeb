# Export Options

The **Export Options** window is used to bake a multi-layer composition, including its procedural solvers, physics modifiers, and event triggers, into a single, optimized **Animation Clip** or **FBX** asset. 

To open the Export Options window, click the **Export (💾 Icon)** on the composition top toolbar.

---

## Window Structure

The window features a top header showing the active composition name, total duration, frame count, and baking frame rate. The bottom bar contains buttons to **Reset Defaults**, **View Queue** (for batch exports), **Cancel**, **Add to Queue** (for batch processing), and **Export Now**.

Settings are organized across five specialized tabs:

```
+-----------------------------------------------------------------+
| General | Timeline | Root Motion | Filtering | Output          |
+-----------------------------------------------------------------+
```

---

## 1. General Tab
Contains parameters for the core baking algorithms, formats, and post-export actions.

*   **Exporter**: Select the type of baking algorithm to execute:
    *   **Humanoid Pose Snapshot**: Recommended for humanoid characters. Captures poses in normalized muscle coordinates, maintaining full humanoid compatibility and body scale independence.
    *   **Generic Transform Snapshot**: Directly bakes the position, rotation, and scale of every individual bone transform. Required for non-humanoid rigs (animals, props, mechanical rigs).
*   **Frame Rate**: The sample rate in frames per second (FPS) for the baked clip (range: `1` to `240` FPS). Use `60` FPS for fluid gameplay animations or `30` FPS for cinematic assets.
*   **Format**: The output asset file type:
    *   **AnimClip**: Generates a native Unity `.anim` asset (always supported).
    *   **FBX**: Generates a standard `.fbx` model file containing the animation. This requires the Unity FBX Exporter package (`com.unity.formats.fbx`) to be installed in the project.
*   **After Export**: The post-export action performed when baking completes:
    *   **PingAsset**: Highlights the generated file in the Project window.
    *   **OpenInAnimationWindow**: Selects the new asset and opens it in the Unity Animation window.
    *   **ApplyToFirstAnimatorState**: Locates the character's active Animator Controller and assigns the baked clip to its first state.
*   **Tangent Mode**: Defines the slope interpolation tangent type for the output animation curves:
    *   **ClampedAuto**: Prevents curve overshoot and visual bounces. This is the recommended setting.
    *   **Auto**: Smoothly interpolates keyframes but may introduce subtle overshoots.
    *   **Linear**: Connects keyframes with straight lines, creating sharp transitions.

---

## 2. Timeline Tab
Allows you to bake a specific segment of the timeline rather than the full composition duration.

*   **Custom Range**: Enables or disables timeline range cropping.
*   **Start**: The starting boundary of the export range. Can be configured by entering either the exact frame count or time in seconds.
*   **End**: The ending boundary of the export range (in frames or seconds).
*   **Visual Range Bar**: Displays a horizontal bar representing the total duration of the composition. A highlighted blue segment indicates the cropped sub-range that will be exported.

---

## 3. Root Motion Tab
Configures how the character's overall movement and root coordinates are processed and baked.

*   **Export Mode (Base Mode)**:
    *   **Standard**: Bakes the character's root movement exactly as it is animated and solved on the timeline.
    *   **InPlaceXZ**: Strips horizontal forward/sideways (X and Z) movement. The character animations run in-place horizontally, while vertical root movement (Y) is preserved.
    *   **InPlaceFull**: Strips all root displacement (X, Y, and Z axes). This forces the root coordinates to remain completely locked to the starting origin.
*   **Per-Axis Strip**: Additive overrides to lock specific channels:
    *   **Strip Position X**: Locks the horizontal X-axis root position to the value of the first frame.
    *   **Strip Position Y**: Locks the vertical Y-axis root position (useful for jumping or climbing animations that should be forced in-place).
    *   **Strip Position Z**: Locks the forward Z-axis root position.
    *   **Strip Rotation Y (Yaw)**: Locks the Y-axis rotation (heading/direction) of the character root to prevent twisting during in-place animations.
*   **Root Driver**: Selects which GameObject drives the root motion coordinates:
    *   *Default (Empty)*: Uses the scene root transform for Generic rigs and the HumanPose body transform for Humanoid rigs.
    *   *Custom Assign*: Drag in a specific trajectory or motion bone transform to drive coordinates on rigs that use custom locomotion controllers.
*   **World Space Baking**: When enabled, bakes bone transform values in World Space coordinates rather than Local Space.
    > [!IMPORTANT]
    > World Space Baking is only available when using the **Generic Transform Snapshot** exporter. Humanoid exports always use normalized muscle coordinates.

---

## 4. Filtering Tab
Filters which bones and properties are written to the final output file to minimize file size.

*   **Mask Asset**: Restricts the export to a subset of character joints. Accepts a Unity AvatarMask asset:
    *   Supports humanoid body parts or generic transform path selections.
    *   Leave empty to export all bone transforms.
*   **Property Filter**: Toggle options to include or exclude animation curves:
    *   **Position (POS)**: Include local position coordinate curves.
    *   **Rotation (ROT)**: Include local rotation curves.
    *   **Scale (SCL)**: Include scale curves.
    *   > [!IMPORTANT]
    *   > Scale curves are only supported when using the **Generic Transform Snapshot** exporter.

---

## 5. Output Tab
Controls quality compression, event integration, and runtime manifest generation.

*   **Bake Events**: Embeds all custom animation events from the composition timeline into the exported clip.
*   **Baking Mode**:
    *   **AllCycles**: Bakes animation events across all loops in the range.
    *   **FirstCycleOnly**: Bakes events only during the first loop iteration to prevent duplicate triggers in looping clips.
*   **Bake Timeline Markers**: Embeds custom markers from the timeline ruler as standard animation events (invokes function name `'OnMarker'` with the marker's text label as a string parameter).
*   **Rotation Mode**: Defines how rotation curves are written:
    *   **Quaternion**: Recommended for game engines. Avoids gimbal lock and matches runtime interpolation.
    *   **Euler**: Best for exporting to external 3D modeling programs.
    *   > [!WARNING]
    *   > Humanoid rigs natively use Quaternions for root and muscle curves. Euler mode only applies to Generic rigs.
*   **Float Compression**: Quantizes floating-point values to clean precision noise. This reduces `.anim` file size in version control repositories.
*   **Decimal Places**: The precision depth (range: `1` to `6` decimal places, where `4` decimal places equates to a precision of `0.0001`).
*   **Keyframe Optimization**: Removes redundant keyframes that fall within tolerance limits:
    *   **Position Error**: Redundancy tolerance in meters.
    *   **Rotation Error**: Redundancy tolerance in rotation angles/muscles.
    *   **Scale Error**: Redundancy tolerance for scale parameters (Generic only).
*   **Runtime FX (MSMotion FX Layer)**:
    *   **Generate FX Manifest**: Automatically exports a custom FX manifest asset (`_fx.asset` ScriptableObject) alongside the clip. This file is read by runtime components to play spatial audio, spawn particles, trigger VFX, or call scripts.
    *   **Embed FX Trigger Events**: Embeds a single event wrapper (`OnFXTrigger`) per FX node on the clip. This allows runtime players to synchronize FX playback with animator states.

---

## Related Guides

*   **Main Workspace**: Get an overview of the editor in the [Composition Editor Index](index.md).
*   **Configuring Rigs**: Learn how to prepare skeletons for IK overlays in [IK Rig Configuration](ik-rig-configuration.md).
*   **Global Options**: Customize workspace defaults in [Editor Settings](editor-settings.md).
