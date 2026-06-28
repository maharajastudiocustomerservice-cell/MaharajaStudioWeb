# Timeline & Range Operations

The timeline is where you navigate your animation, select time regions, and execute structural edits across ranges of keyframes.

---

## Timeline Navigation

Navigating the timeline is simple and fluid:
* **Scrubbing**: Click and drag the red playhead line left or right across the ruler to scrub through time.
* **Playback Shortcuts**: Use the navigation buttons in the timeline toolbar:
  * **First Frame (⏮)**: Snaps the playhead to the beginning (0.0s).
  * **Previous Frame (⏪)**: Steps backward by one frame.
  * **Play / Pause (⏯)**: Starts or pauses playhead movement.
  * **Next Frame (⏩)**: Steps forward by one frame.
  * **Last Frame (⏭)**: Snaps the playhead to the end of the clip.
* **Zooming**: Hover your mouse over the track area and hold **Ctrl** (or **Alt**) while scrolling the wheel. Zooming allows you to expand the timeline horizontally to see individual frame markings or contract it to see the entire clip.

---

## Time and Frame Formats

You can view and enter time in two formats:
* **Seconds**: Entered numerically (e.g., `0.75` seconds).
* **Frames**: Entered as integers (e.g., Frame `45`). The editor converts time using the clip's frame rate. For example, at a frame rate of `60 FPS`, Frame 30 corresponds to `0.5` seconds.
* **FPS Setting**: Located in the sidebar's Range section. Change this value to adjust the grid density for snapping and baking actions.

---

## Creating Selection Ranges

To select a specific segment of the animation:
1. Hover your cursor over the ruler track area.
2. Click and drag horizontally. A blue highlighted box will cover the selected time region.
3. To adjust the boundaries, hover over the left or right edges of the blue selection box until the cursor changes, then drag the handle.
4. The numerical boundaries will update in the **Start** and **End** fields in the sidebar. You can also type frame numbers directly in the **Start Frame** and **End Frame** fields to set an exact range.

---

## Range Editing Actions

Once you have set a selection range, you can perform structural actions from the sidebar:

### Copy, Cut, Paste, and Delete
* **Copy Range**: Copies only the keyframes within the selected range into the clipboard.
* **Cut Range**: Copies the keyframes in the selection and deletes them from the clip.
* **Paste Range**: Pastes the clipboard keyframes at the current playhead time.
* **Delete Range**: Clears all keyframes within the selection range.
* **Ripple delete/cut**: A toggle in the Range sidebar. When enabled, deleting or cutting a range automatically shifts all keyframes to the right of the selection leftward, closing the gap. When disabled, the space is left empty (holding the last pose).

### Paste Modes
Select a mode from the **Paste Mode** dropdown before pasting:
* **Overwrite**: Clears any existing keyframes in the target time region and drops in the clipboard keys.
* **Merge**: Keeps existing keys and overlays the clipboard keys on top of them.
* **Insert**: Moves all subsequent keyframes to the right by the duration of the clipboard data to make room, then inserts the copied range.

---

## Advanced Range Transformations

* **Crop Clip**: Destructive action that discards all animation before the selection start and after the selection end, keeping only the selected range.
* **Trim Head**: Instantly deletes all keyframes before the selection start.
* **Trim Tail**: Instantly deletes all keyframes after the selection end.
* **Extract Range**: Saves the selected segment as a brand-new standalone `.anim` file.
* **Reverse**: Flips the keyframe sequence in the selection backwards in time (great for reversing loops or walkcycles).
* **Scale**: Multiplies the timing of keys in the range by the value in the **Scale** field. For example, a scale of `2.0` doubles the duration (slowing it down), while `0.5` cuts the duration in half (speeding it up). Subsequent keys are shifted (rippled) to match.
* **Snap**: Aligns all keyframes in the range to the nearest frame grid interval defined by your **FPS** setting, removing sub-frame jitter.
* **Bake**: Samples the curves and generates a keyframe on every single frame grid line within the selection. Useful for freezing procedural overlays or preparing data for export.

---

> [!TIP]
> You can speed up your timeline editing using built-in keyboard shortcuts like **Space** to toggle playback, **Arrow Keys** (with **Shift**) to step frames, and **Ctrl + C / X / V** to copy, cut, and paste. See [the main index page](index.md#keyboard-shortcuts) for the full hotkey reference.

