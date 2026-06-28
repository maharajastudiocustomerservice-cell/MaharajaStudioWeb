# Animation Events

**Animation Events** allow you to trigger runtime visual effects, audio clips, camera shakes, or custom scripts at precise moments during an animation clip's playback (e.g., spawning dust particles on a footstep or playing a weapon swing sound).

---

## Visualizing Events on the Timeline

Events are represented visually on the timeline ruler:
* **Event Markers**: Small gold-colored diamond markers appearing along the bottom edge of the **Timeline Ruler**.
* **Selection**: Click a gold marker to highlight the event. The playhead snaps to the event's trigger time, and the **Animation Events** panel in the sidebar updates to display the event's settings.
* **Dragging**: Click and drag an event marker horizontally along the ruler to adjust its trigger time.

---

## The Event Editor Panel

When you select an event, you can configure its parameters in the **Animation Events** panel at the bottom of the sidebar:

### 1. Identity & Timing
* **Display Name**: The human-readable label shown in the editor (e.g. `FootstepLeft` or `Slash`).
* **Trigger Time**: The precise time in seconds when the event fires.
* **Duration**: Set to `0.0` for one-shot events (like playing a sound once). Set to a value greater than `0.0` for sustained events (like keeping a particle emitter active or looping a sound over a range).
* **Loop / Blend**: Set fade-in and fade-out times to smoothly blend effects (such as audio volume or light brightness).

### 2. Socket Targets
* **Target Bone**: Enter the name of a character joint to attach the spawned effect to (e.g. `Foot_L` or `Hand_R`). Leave this empty to spawn the effect at the character's root position.

### 3. Transform Overrides
Specify local offset coordinates relative to the target bone:
* **Position Offset**: Shifts the effect's starting coordinates (e.g. offsetting a dust particle slightly below the foot joint).
* **Rotation Override**: Rotates the effect relative to the bone's orientation.
* **Scale Override**: Scales the size of the spawned effect.

### 4. Property Overrides
The editor allows you to dynamically set component parameters on the spawned effect at runtime (such as changing a Light component's intensity or calling custom script variables):
* Click the Property Override fields to target specific components and write value changes.
* **Allow Editor Preview Overrides**: Toggles whether these property overrides run inside the Unity Editor preview. Enable this with caution, as previewing scripts can modify scene assets.

---

## Event Workflows

### How to Create an Event
1. Move the timeline playhead to the frame where the event should occur.
2. Right-click on the timeline ruler.
3. Select **Add Event** (or click the Add Event button in the sidebar panel).
4. A new gold marker will appear, and you can customize its function and parameters in the sidebar.

### How to Adjust Event Timing
* Click and drag the gold event marker on the ruler.
* Alternatively, enter the exact value in the **Trigger Time** field in the sidebar.

### How to Delete an Event
1. Click the gold marker to select it.
2. Click the Delete button in the sidebar panel.
