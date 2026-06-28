# Transition & Bridging

When editing motion capture or cleaning up sequences, you often need to remove a bad segment (such as a glitch, pop, or idle gap) and blend the remaining ends together. The **Remove + Bridge** tool handles this process automatically.

---

## How Bridging Works

Bridging performs two operations in sequence:
1. It deletes all keyframes within your selected time range.
2. It calculates the pose of the character immediately *before* the deleted range and the pose immediately *after* it.
3. It generates new transition keyframes across the gap to blend smoothly between those two boundary poses over a designated duration.

```
Original:    [--- Pose A ---] [======= Glitchy Segment =======] [--- Pose B ---]
Cut:         [--- Pose A ---]                                   [--- Pose B ---]
Bridged:     [--- Pose A ---] \____ Transition Blend (Bridge) _/ [--- Pose B ---]
```

---

## Bridging Controls

Configure these controls in the sidebar's **Range** section before running the operation:

### Transition Duration
Set the blend length in seconds in the **Transition** field. 
* A short duration (e.g., `0.1s`) creates a fast, sudden snap.
* A long duration (e.g., `0.5s`) creates a slow, soft blend.
* The duration cannot exceed the total length of the removed segment.

### Transition Mode
Choose how the editor interpolates values between the boundary poses:

| Mode | Interpolation Style | Best Used For |
|:---|:---|:---|
| **Linear** | Steady, constant speed from start to end. | Quick shifts, mechanical parts, or linear camera movements. |
| **Smooth** | Eases out of Pose A and eases into Pose B (using a smooth curve). | Human and creature body motions, walk cycle stitching, and natural posture shifts. |

---

## Step-by-Step Workflows

### Method 1: Bridge and Edit the Loaded Clip Directly
Use this method to modify your active animation in place:
1. Scrub to locate the segment you want to remove.
2. Drag on the ruler to highlight the range, or type the boundary times in the **Start** and **End** fields.
3. In the sidebar, set your desired blend length in the **Transition** field.
4. Choose **Smooth** or **Linear** from the **Transition Mode** dropdown.
5. Click **Remove + Bridge**.
6. The editor deletes the segment, ripples subsequent keys leftward, and inserts smooth blending keyframes across the transition window.

### Method 2: Export a Bridged Copy
Use this method to generate a new file, leaving your source animation untouched:
1. Define the range, set the **Transition** duration, and choose the **Transition Mode** as described above.
2. Click **Export Bridged** in the sidebar.
3. A standard Unity save file dialog will open. Name the new asset (e.g. `walk_cycle_bridged.anim`) and choose a location.
4. The editor generates and saves the new, bridged clip without altering the loaded asset.
