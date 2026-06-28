# FX Nodes Overview

**FX Nodes** are timeline blocks dedicated to triggering runtime events (such as playing sound effects, spawning particles, instantiating prefabs, animating attachments, or firing custom scripts) rather than animating skeletal bones. 

Unlike motion nodes, FX nodes do not bake curve data into the exported Animation Clip. Instead, they are compiled into a companion **FX Manifest** asset which is read by runtime playback components.

---

## Shared Parameter Reference

Every FX Node type inherits a common set of properties for timing, positioning, and socket attachment:

### Timing & Loop Settings

* **Event Name**: A user-friendly label to organize this event.
* **Loop**: If checked, the FX continues to play or repeat for the duration of the timeline block.
* **Blend In**: Time (in seconds) over which the FX fades in (e.g., volume ramp-up or particle size growth).
* **Blend Out**: Time (in seconds) over which the FX fades out (e.g., volume decay or particle opacity fade).

### Socket Target & Attachment

You can attach the spawned effect to a specific part of the character's skeleton:

* **Target Human Bone**: A dropdown list of standard Humanoid bones (e.g., **RightHand**, **Head**, **LeftFoot**). 
* **Target Bone**: A text field to enter a manual bone name if the character is generic (non-humanoid).
* **Transform Space**: Controls how the spawned FX tracks character movement:
  * **Follow Target**: The FX attaches as a child of the bone, translating and rotating along with it.
  * **Spawn and Stand**: The FX spawns at the bone's coordinates at the trigger time, but remains stationary at those world coordinates as the character moves away.
  * **World Space**: The FX spawns at absolute world coordinates, independent of the character's bone position.

### Transform Overrides

Offsets applied relative to the socket bone coordinate system:
* **Override Position**: Custom Vector3 offset coordinates (**Local Position**).
* **Override Rotation**: Custom Euler angle offsets (**Local Rotation Euler**).
* **Override Scale**: Custom Vector3 scale factors (**Local Scale**).

---

## Workflow: Property Overrides

The **Property Overrides** workflow allows you to dynamically customize public variables, fields, or component properties of the spawned effect prefab or the character's bone hierarchy directly from the composition timeline. This is ideal for altering effects per event without duplicating prefabs (e.g., changing a particle system's material color, modifying a spawned light component's intensity, or triggering custom component methods on a specific skeletal joint).

To manage overrides, open the fourth tab in the FX node editor details panel.

### Adding and Managing Overrides
* **Add Override**: Click the **+ Add Override** button to append a new property override card to the list.
* **Enable/Disable Toggle**: Click the checkbox next to the override card header to temporarily disable/enable the modification without deleting its configuration.
* **Remove Override (✕)**: Click the delete icon at the right of the header to remove the override from the event node.

### Target Selection
Select where the property modification should be applied using the **Target Mode** dropdown:
* **Root**: Targets the character's main root GameObject.
* **SpawnedObject**: Targets the instantiated FX prefab GameObject itself.
* **CustomTargetBone**: Targets a specific named bone in the character's skeleton. When selected, displays the standard humanoid bone picker dropdown and a manual bone name field.

### Trigger Time Configuration
You can define the exact timestamp within the FX slot's range at which the override is executed:
* **Trigger Time Slider**: Drag the slider to set the normalized time (0.0 to 1.0) along the event duration.
* **Time Inputs**: Read or enter numerical values using the **Normalized Time** field (0.0 to 1.0) or the **Composition Time** field (in seconds).

### Action Types & Method Invocation
Toggle the **Action Type** switch to configure the modification behavior:
* **Set Property**: Directly modifies the value of a public field, variable, or property on the target component.
* **Invoke Method**: Executes a public parameterless method or a method accepting a single argument on the target component.

### Target Component & Member Mappings
Map the override to a specific component on the target GameObject:
* **Component Field**: Enter the type name of the component class to modify (e.g., `Light`, `ParticleSystem`, `AudioSource`, `MeshRenderer`, or custom scripts).
* **Target Name**: Enter the exact name of the public property or field (e.g. `intensity`, `range`, `volume`) or the method name to invoke.
* **Auto-Picker (▼)**: Click the dropdown arrow to scan the active target GameObject and display a list of all detected components, properties, and methods for quick one-click assignment.
* **Refresh Type (↻)**: Click the refresh icon to force the UI to parse the entered component/target name and rebuild the value editor.

### Dynamic Value & Argument Editors
The **Value/Arg** field automatically displays a specialized input type matching the data type of the mapped property or method parameter:
* **Text Field**: Displayed for string parameters.
* **Integer Field / Float Field**: Displayed for numerical properties, using culture-invariant parsing.
* **Toggle**: Displayed for boolean flags.
* **Vector3 Field**: Displays 3D input slots for positions, rotations, or scaling factors.
* **Color Field**: Renders an interactive RGBA color picker.
* **Enum Field**: Displays a dropdown listing all valid names for enum properties.
* **Object Field**: Displays an asset slot to assign external project files, prefabs, or materials.

---


## Editor Preview Safety

By default, some dynamic effects (like custom scripts or scene property overrides) are blocked in edit mode:

> [!WARNING]
> Enabling **Allow Editor Preview Overrides** allows custom scripts and overrides to execute in the Scene View while scrubbing the timeline. Use caution: poorly written scripts can permanently alter scene objects, modify assets, or throw errors in edit mode. 

To test preview-safe actions, ensure the top toolbar's **Safety Toggle (FX Indicator)** is enabled.

---

## Node Types Reference

Each FX node has specific parameters tailored to its trigger target. Read the details in the following guides:

* **Audio**: [Audio FX Node](audio-fx-node.md)
* **Particles**: [Particle FX Node](particle-fx-node.md)
* **Spawning**: [Spawn FX Node](spawn-fx-node.md)
* **Transform**: [Transform FX Node](transform-fx-node.md)
* **VFX Graph**: [VFX Graph FX Node](vfx-graph-fx-node.md)
* **Custom Scripts**: [Script Event FX Node](script-event-fx-node.md)
* **Camera Shake**: [Camera Shake FX Node](camera-shake-fx-node.md)

---

## FX Path Tools Scene Panel

When editing a spline trajectory on an FX node (such as Particle FX, VFX Graph, or Spawn FX nodes), a floating overlay panel titled **FX Path Tools** appears in the Scene View. This context-aware panel provides tabs and controls to quickly edit nodes, generate path presets, and perform coordinate manipulation directly in the viewport.

### Node Tab
The **Node** tab displays context-sensitive properties based on your viewport selection:
* **No selection**: Shows a help message prompting you to click a node handle in the viewport. Includes an **Add Node at End** button to append a new Bezier control node to the end of the spline.
* **Single Node Selected**:
  * Displays the selected node's name (e.g. `● Node_X`).
  * **Local Time**: Adjusts the node's normalized time (0.0 to 1.0) along the duration of the FX slot.
  * **Global Time**: Adjusts the node's absolute position on the playback timeline (in seconds), automatically updating its local normalized time relative to the slot's start time and duration.
  * **Tangent Mode**: Sets the node's Bezier tangent calculation mode (`Auto`, `Split`, etc.) to control curve blending.
  * **Add Node After**: Inserts a new node immediately after the selected node, positioned forward along the path.
  * **Remove Node**: Deletes the selected node (requires at least 2 nodes to remain on the spline).
  * **Stop Editing Tangents**: Hides tangent editing handles in the Scene View.
* **Multiple Nodes Selected**:
  * Displays the number of selected nodes.
  * Dragging any selected node in the viewport moves all of them collectively.
  * **Remove Selected Nodes**: Deletes all currently selected nodes (requires at least 2 nodes to remain on the spline).

### Presets Tab
The **Presets** tab allows you to generate complex motion paths in one click. Customize the general **Target Distance** (in meters) to define the forward scale of the generated path, then apply any of the following presets:

#### Projectile / Travel
* **Parabolic Arc**: Generates a classic projectile arc. Configure **Peak Height** (maximum height of the arc) and **Nodes** count (4 to 20).
* **Straight Line**: Generates a direct linear trajectory from the start point to the target distance.
* **Bounce**: Generates a repeating bouncing pattern along the ground. Configure **Peak Height** (bounce height) and **Bounces** count (1 to 6).
* **Zig-Zag / Lightning**: Generates a jagged zig-zag pathway. Configure lateral **Amplitude** and the number of **Segments** (2 to 14).
* **Ribbon / Trail**: Generates a smooth horizontally waving path. Configure the lateral **Swing** width.
* **Lasso / Hook**: Generates a straight flight path that loops back at the end. Configure the **Loop Radius**.

#### Orbital / Looping
* **Circle / Orbit**: Generates a circular loop. Configure the circle's **Radius**, **Nodes** count (4 to 32), and toggle **Full Loop** to close the shape.
* **Ellipse**: Generates an oval orbital path. Uses the circle radius as the major axis and a minor axis scaled to 60%.
* **Helix / Coil**: Generates a vertical corkscrew pattern. Configure the coil **Radius**, **Height**, total **Turns** (1 to 8), and **Nodes/Turn** (4 to 16).
* **Figure-8 / Infinity**: Generates a horizontal figure-8 pattern using the circle radius.
* **Spiral — Inward**: Generates a spiral contracting towards the center. Configure **Start Radius**, total **Turns**, **Nodes** (8 to 48), and **Height** (vertical travel).
* **Spiral — Outward**: Generates an expanding spiral starting from the center and scaling outwards.

#### Wave / Organic
* **Sine Wave**: Generates a smooth, wavy sine path. Configure wave **Amplitude**, **Frequency**, and **Nodes** count (4 to 32).
* **Spring / Energy Beam**: Generates a tight spiral beam pattern using the Helix configuration parameters (**Radius**, **Turns**, and **Nodes/Turn**).

### Edit Tab
The **Edit** tab provides utilities to clean up, reverse, or transform the active spline path:
* **Reverse Path**: Swaps the direction of the spline nodes, reversing the path starting and ending points.
* **Smooth Tangents**: Recalculates and smooths all node tangents to eliminate sharp corners.
* **Normalize Timing (E)**: Distributes control node timestamps evenly across the duration of the timeline slot.
* **Normalize Timing (D)**: Adjusts node timestamps based on physical distance, ensuring constant travel speed along the spline.
* **Subdivide Path**: Inserts a new Bezier node in the middle of each existing spline segment, doubling detail while preserving the curve's shape.
* **Mirror (X, Y, Z)**: Viewport mirror buttons that flip the spline coordinates along the chosen local axis.
* **Reset to Default**: Restores the spline to a simple 2-node straight line extending 2 meters forward.

