# Trajectory Override Node

The **Trajectory Override Node** replaces a character's root motion animation curves with a custom Bezier spline trajectory. This is ideal for steering characters along exact paths (such as combat rolls, leaps, wall runs, or scripted cinematics).

---

## Spline Editing in the Scene View

When you select a Trajectory Override Node, visual spline controls appear in the Scene View:

* **Bezier Nodes**: White boxes indicating spline points. Click and drag nodes to shift the pathway.
* **Tangents**: Pink handles protruding from each node. Drag these to define the curve's exit and entry angles.
* **Adding/Deleting Nodes**: Right-click on the spline to add a new Bezier node, or select a node and press **Delete** to remove it.
* **Tangent Modes**: Right-click a node to set its tangent calculations:
  * **Auto**: Calculates smooth curves automatically based on neighboring nodes.
  * **Split**: Allows left and right tangent handles to be rotated independently to create sharp corners.

---

## Inspector Parameter Reference

Configure the spline trajectory solver properties in the details panel:

### Space Configurations

* **Space**:
  * **Relative**: The spline coordinates are relative to the character's starting position at the node's start time. If the character is moving, the path shifts with them.
  * **Absolute**: The spline is locked to absolute world-space coordinates. The character will snap to the exact world coordinates regardless of their previous location.

### Speed & Easing

* **Easing Curve**: Drives timing along the spline. The X-axis represents normalized timeline time; the Y-axis represents progress along the spline length (0.0 = start, 1.0 = end). E.g. an S-curve creates gradual acceleration and deceleration.

### Rotation & Banking

* **Rotation Blend Weight**: Blends the character's orientation between the animation clip's original rotation (`0.0`) and the spline's direction vector (`1.0`).
* **Use Banking**: When enabled, the character procedurally leans/banks left or right into curves (like a motorcycle or skater).
* **Bank Multiplier**: Sets the intensity of the bank lean (higher values create deeper tilts in tight corners).

### Ground Snapping (Terrain Conformance)

* **Ground Layer Mask**: Physics layers representation representing walkable terrain.
* **Ground Snap Offset**: Vertical height offset applied above the hit terrain point.
* **Align to Ground Normal**: Automatically rotates the character to match the slope inclination of the ground beneath the spline nodes.

### Loop Options

* **Is Closed Loop**: Connects the final node back to the initial node, transforming the trajectory into a continuous loop track.

---

## Visual HUD & Debug Settings

Turn these options on in the Inspector to show overlays in the Scene View:

* **Show Speed Heatmap**: Colors the spline path (gradient from green to red) to visually display where the character will accelerate or decelerate based on the easing curve.
* **Show Path Length HUD**: Displays a text box indicating the total length of the spline in meters.
* **Show Per-Node Time**: Prints the execution time (in seconds) next to each Bezier node.
* **Show Preview Playhead**: Renders a silhouette of the character at the current scrubber time along the spline path.

---

## Workflow: Spline Sub-Path Extraction

If you need to crop the duration of a trajectory node without destroying the shape of the spline curve, click the **Extract Sub-Path** button in the details panel.

This uses a **de Casteljau subdivision** algorithm to:
1. Divide the spline at the new start and end timestamps.
2. Mathematically calculate new control points and tangents so the cropped segment preserves the exact visual shape of the original path.
3. Optionally translate/shift the new start point back to the local origin coordinate (`0, 0, 0`).

