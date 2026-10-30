# 9. Scene Debug Overlay

The Scene Debug Overlay system allows developers to visualize and interactively manipulate spatial values (positions, directions, rotations, scales, radii, bounds, labels, lines, sliders, grids, and buttons) directly in the Unity Scene view using straightforward field and method attributes with full live Undo/Redo support.

It deeply intersects with the `Scene Debug Overlay` Editor Window (`Tools > Maharaja Studio > MSUltimate > Windows > Scene Debug Overlay`), where overlays can be forcefully re-scanned, filtered, or toggled on/off at a component-level or globally.

---

## ── Upgraded Interactive Visual Attributes ──

### `[ShowInScene]`
Draws a targeted shape representing a position, with optional interactive 3D translation handles.
**Supports:** `Vector3`, `Vector2`, `Transform`, `GameObject`, `Component`
- `Label`: (string) Text drawn next to the gizmo.
- `ColorHex`: (string) Shape color.
- `Size`: (float) Diameter of the shape.
- `Shape`: (SceneGizmoShape) Options: Sphere, Cube, Cross, Diamond.
- `ShowLabel`: (bool) Toggles drawing the world-space label.
- `OffsetX` / `OffsetY` / `OffsetZ`: (float) Shift factor for the text label.
- `ShowDistanceToCamera`: (bool) Live-calculates and renders distance to scene view camera.
- `OnlyWhenSelected`: (bool) Hides drawing unless the parent GameObject is actively selected in Hierarchy.
- **`Editable`**: (bool) When `true`, displays an interactive `Handles.PositionHandle` allowing you to drag and reposition the value directly in the Scene view with Undo!
- **`LocalSpace`**: (bool) Treats the coordinate as local relative to the GameObject.
- **`Snap`**: (float) Grid snapping increment when dragging in Scene view.

### `[SceneRadius]`
Draws a wireframe or semi-solid radial projection marking operational distances or areas of effect.
**Supports:** `float`, `int`, `double`
- `ColorHex`: (string) Area color.
- `FillAlpha`: (float) Opacity of the solid internal fill (0 for purely wireframe).
- `Segments`: (int) Detail configuration for circular arcs.
- `DrawMode`: (SceneRadiusMode) Sphere, Circle (flat XZ), Hemisphere.
- `ShowValue`: (bool) Appends the current float value to the label.
- `Label`: (string) Optional tag prepended to the radius measurement.
- `OnlyWhenSelected`: (bool) Visibility binding.
- **`Editable`**: (bool) When `true`, displays an interactive radial slider handle in the Scene View to resize the radius with mouse drag.
- **`MinRadius`** / **`MaxRadius`**: (float) Clamps interactive resizing.

### `[SceneBounds]`
Visualizes rigid spatial cages, hitboxes, or spawn regions.
**Supports:** `Bounds`, `Rect`, `Vector3` (cubic extents), `BoxCollider`, `Collider`
- `ColorHex`: (string) Outline color.
- `FillAlpha`: (float) Box internal tint intensity.
- `ShowDimensions`: (bool) Overlays width/height/depth numerical measurements.
- `ShowCenter`: (bool) Renders a crosshair at the structural center.
- `WireframeOnly`: (bool) Overrides alpha fills.
- `Label`: (string) Optional descriptor label.
- `OnlyWhenSelected`: (bool) Visibility binding.
- **`Editable`**: (bool) When `true`, activates interactive 6-face handles (`BoxBoundsHandle`) allowing you to drag box faces to resize boundaries directly in the Scene view.
- **`HandleColorHex`**: (string) Color of the draggable face handles.

### `[SceneArrow]`
Displays strongly directional impulses, velocities, lines of sight, or applied forces.
**Supports:** `Vector3` (Direction/Velocity), `Transform` (Forward relative vector), `Quaternion`, `Rigidbody`
- `ColorHex`: (string) Arrow tint.
- `ArrowHeadSize`: (float) Triangulation cap length.
- `Thickness`: (float) Handle weight.
- `Length`: (float) Fixed multiplier.
- `Normalize`: (bool) Forces arrow cap at exactly 1 unit regardless of input magnitude.
- `ShowMagnitude`: (bool) Overlays raw magnitude scalar data as text.
- `ArrowStyle`: (SceneArrowStyle) Solid, Dashed, Double.
- `Label`: (string) Descriptive tag.
- `OnlyWhenSelected`: (bool) Visibility binding.
- **`Editable`**: (bool) When `true`, adds an interactive move handle at the tip of the arrow. Dragging aims and scales the vector live.
- **`LockLength`**: (bool) When `true` during interactive aiming, preserves the original magnitude while re-aiming the direction.

### `[SceneLine]`
Draws continuous lines or paths between arrays/lists of positional data.
**Supports:** `Vector3[]`, `List<Vector3>`, `Vector2[]`, `List<Vector2>`, `Transform[]`, `List<Transform>`
- `ColorHex`: (string) Line color.
- `Thickness`: (float) Thickness of the Handles drawing line.
- `DashLength`: (float) Converts the solid line into a dotted line (0 for solid).
- `ClosedLoop`: (bool) Automatically draws an attaching line from the last index back to the first.
- `ShowVertexDots`: (bool) Draws spherical handles at every distinct point index.
- `VertexDotSize`: (float) Scale calculation for individual vertex spheres.
- `ShowDistances`: (bool) Displays individual segment lengths at segment midpoints.
- `Label`: (string) Descriptive label.
- `OnlyWhenSelected`: (bool) Visibility binding.
- **`Editable`**: (bool) When `true`, each waypoint vertex becomes an interactive draggable handle in the Scene View to reshape paths on the fly.

### `[SceneGrid]`
Projects a local construction or navigation grid array onto the floor or wall relative to the parent object.
**Supports:** `Vector2` (Grid Size), `float` (Cell Size uniform), `int` (Cell Count uniform)
- `ColorHex`: (string) Internal lines.
- `CellSize`: (float) Spatial distance separating grid markers.
- `GridWidth` / `GridDepth`: (int) Expansions.
- `ShowAxes`: (bool) Highlights primary central perpendicular axes.
- `AxesColorHex`: (string) Color of the center axes.
- `Plane`: (SceneGridPlane) `XZ` (Floor), `XY` (2D Wall), `YZ` (Side Wall).
- `CenterOnObject`: (bool) Drifts grid logic from 0,0,0 to the parent component position.
- `Label`: (string) Title label.

### `[SceneLabel]`
Highly customizable, floating text billboards in the Scene View strictly tied to component parameters.
**Supports:** `string`, `float`, `int`, `Vector3`, or any `.ToString()` supported object.
- `ColorHex`: (string) Primary text paint.
- `FontSize`: (int) Typography scale.
- `BackgroundColorHex`: (string) Floating container background.
- `OffsetX` / `OffsetY` / `OffsetZ`: (float) World-space drifting from object origin.
- `Prefix` / `Suffix`: (string) Appended context tags.
- `ShowFieldName`: (bool) Automatically prepends structural logic names.
- `BillboardMode`: (bool) Forces the text block to perpetually stare at the Scene Camera.

---

## ── NEW Interactive Scene Manipulation Attributes ──

### `[ScenePositionHandle]`
Renders a dedicated 3D translation gizmo (`Handles.PositionHandle`) for direct positional authoring.
**Supports:** `Vector3`, `Vector2`
- `Label`: (string) Text displayed above the position gizmo.
- `ColorHex`: (string) Accent color for handle guides and caps.
- `LocalSpace`: (bool) If `true`, edits coordinates relative to the GameObject's local transform.
- `Snap`: (float) Grid snapping increment (e.g. `0.5f`, `1.0f`).
- `DrawLineToOrigin`: (bool) Draws a dotted line connecting the position back to the GameObject origin.
- `CapSize`: (float) Size of the origin point handle.

### `[SceneRotationHandle]`
Renders a 3D rotation disc gizmo (`Handles.RotationHandle`) in the Scene View to interactively orient directions, turrets, or spawn rotations.
**Supports:** `Quaternion`, `Vector3` (Euler angles)
- `Label`: (string) Descriptive text.
- `ColorHex`: (string) Ring tint.
- `OffsetX` / `OffsetY` / `OffsetZ`: (float) Offset from object origin.
- `LocalSpace`: (bool) Whether rotation aligns with parent or world.

### `[SceneScaleHandle]`
Renders a 3D scale gizmo (`Handles.ScaleHandle`) directly in the Scene View.
**Supports:** `Vector3` (3-axis scale extents), `float` (Uniform scale factor)
- `Label`: (string) Title.
- `ColorHex`: (string) Handle accent color.
- `MinScale`: (float) Minimum clamp limit.

### `[SceneSlider]`
Renders a constrained 1D linear slider handle along an axis (`Handles.Slider`) with live distance readout.
**Supports:** `float`, `int`
- `Axis`: (SceneSliderAxis) `X`, `Y`, `Z`, `Forward`, `Up`, `Right`.
- `Min` / `Max`: (float) Numerical limits of the slider.
- `ColorHex`: (string) Slider line and handle color.
- `HandleSize`: (float) Size of the draggable slider handle.
- `Label`: (string) Tag displayed with current live value.

### `[SceneButton]`
Renders an interactive, clickable 3D button in the Scene View that executes a method on click with live Undo support.
**Supports:** Methods (`void MethodName()`), Fields, Properties
- `Text`: (string) Label text on the 3D button.
- `OffsetX` / `OffsetY` / `OffsetZ`: (float) 3D position offset relative to object.
- `ColorHex`: (string) Button text and outline color.
- `Size`: (float) Button scale.

---

## ── Dedicated Sample Scripts ──

Every Scene Debug attribute features its own standalone, realistic sample component located in `Assets/MSUltimate/Sample/Scripts/Runtime/Attributes/Debugging/SceneDebugOverlay/`:

| Attribute | Dedicated Example Script | Key Interactive Features Demonstrated |
| :--- | :--- | :--- |
| `[ScenePositionHandle]` | [`ScenePositionHandleExample.cs`](../../Sample/Scripts/Runtime/Attributes/Debugging/SceneDebugOverlay/ScenePositionHandleExample.cs) | 3D Position handles for strike coordinates, local space offsets, 2D planar nodes. |
| `[SceneRotationHandle]` | [`SceneRotationHandleExample.cs`](../../Sample/Scripts/Runtime/Attributes/Debugging/SceneDebugOverlay/SceneRotationHandleExample.cs) | 3D rotation discs for Quaternion turret aiming and Euler Vector3 camera angles. |
| `[SceneScaleHandle]` | [`SceneScaleHandleExample.cs`](../../Sample/Scripts/Runtime/Attributes/Debugging/SceneDebugOverlay/SceneScaleHandleExample.cs) | 3D non-uniform Vector3 zone scaling and uniform float multiplier scaling. |
| `[SceneSlider]` | [`SceneSliderExample.cs`](../../Sample/Scripts/Runtime/Attributes/Debugging/SceneDebugOverlay/SceneSliderExample.cs) | 1D linear sliders along Y (jump height), Forward (combat range), and X (lane offset). |
| `[SceneButton]` | [`SceneButtonExample.cs`](../../Sample/Scripts/Runtime/Attributes/Debugging/SceneDebugOverlay/SceneButtonExample.cs) | Clickable 3D buttons in Scene view to trigger blast waves, reset position, and toggle shields. |
| `[ShowInScene]` | [`ShowInSceneExample.cs`](../../Sample/Scripts/Runtime/Attributes/Debugging/SceneDebugOverlay/ShowInSceneExample.cs) | Interactive patrol points with `Editable = true` and `Snap = 0.5f`. |
| `[SceneRadius]` | [`SceneRadiusExample.cs`](../../Sample/Scripts/Runtime/Attributes/Debugging/SceneDebugOverlay/SceneRadiusExample.cs) | Interactive radial resizing slider with `Editable = true`, `MinRadius`, and `MaxRadius`. |
| `[SceneBounds]` | [`SceneBoundsExample.cs`](../../Sample/Scripts/Runtime/Attributes/Debugging/SceneDebugOverlay/SceneBoundsExample.cs) | Interactive 6-face `BoxBoundsHandle` with `Editable = true`. |
| `[SceneArrow]` | [`SceneArrowExample.cs`](../../Sample/Scripts/Runtime/Attributes/Debugging/SceneDebugOverlay/SceneArrowExample.cs) | Interactive vector tip handle for re-aiming wind velocity and forces. |
| `[SceneLine]` | [`SceneLineExample.cs`](../../Sample/Scripts/Runtime/Attributes/Debugging/SceneDebugOverlay/SceneLineExample.cs) | Interactive waypoint vertices for reshaping paths directly in the Scene View. |
| `[SceneLabel]` | [`SceneLabelExample.cs`](../../Sample/Scripts/Runtime/Attributes/Debugging/SceneDebugOverlay/SceneLabelExample.cs) | Informational floating badges, health readouts, and state billboards. |
| `[SceneGrid]` | [`SceneGridExample.cs`](../../Sample/Scripts/Runtime/Attributes/Debugging/SceneDebugOverlay/SceneGridExample.cs) | Construction and navigation planar grid lines (XZ, XY, YZ). |
| *All-In-One* | [`InteractiveSceneDebugExample.cs`](../../Sample/Scripts/Runtime/Attributes/Debugging/SceneDebugOverlay/InteractiveSceneDebugExample.cs) | Comprehensive master sandbox containing all 12 attributes simultaneously. |

---

## ── Inspector Field Toggle Button & Persistent Memory ──

Every field and method decorated with any Scene Debug attribute automatically receives an interactive, AAA-styled toggle button (eye icon) embedded directly on its Inspector row.

### Key Capabilities

1. **Direct In-Inspector Toggling:**
   - **Left-Click:** Instantly toggles whether that specific member's gizmo is rendered in the Scene View.
   - **Visual State:** Active gizmos display a bright cyan-accented eye icon (`👁`). Hidden gizmos display a dimmed eye-slash icon (`⊘`) with a muted border.
   - **Multi-Selection Support:** Works seamlessly across multiple selected GameObjects in the Inspector.

2. **Zero-Pollution Persistent Memory:**
   - Gizmo visibility is automatically persisted per-object and per-member using the high-performance `MSDrawerStateStorage` system.
   - **Zero Scene Asterisks:** Does not modify or serialize into MonoBehaviour fields, preventing unwanted scene or prefab dirtying.
   - **Reload Resilient:** Automatically restores your preferred visibility states across Unity restarts, assembly reloads, and scene transitions.

3. **Rich Context Menu (Right-Click):**
   - **Show/Hide Scene Gizmo:** Inverts current visibility.
   - **Show All Gizmos on Target:** Turns on every debug gizmo on the inspected component.
   - **Hide All Gizmos on Target:** Turns off all debug gizmos on the inspected component.
   - **Reset to Default (Visible):** Clears overrides and restores default visibility.
   - **Open Scene Debug Overlay Window...:** Quick-access shortcut to the master overlay management window.

4. **Live Bidirectional Synchronization:**
   - Toggling visibility via the Inspector button immediately synchronizes with the `Scene Debug Overlay` window and vice versa.

5. **Opt-Out Per Attribute:**
   - If you prefer not to display the toggle button on a particular field or method, simply set `ShowToggleInInspector = false`:
     ```csharp
     [SceneRadius(5f, ShowToggleInInspector = false)]
     public float detectionRadius = 5f;
     ```

