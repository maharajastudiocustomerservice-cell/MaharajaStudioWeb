# Animation Clip Node

An **Animation Clip Node** is the fundamental building block of a composition layer. It represents a specific segment of time on the timeline during which a native Unity Animation Clip (`.anim`) plays back on the preview character.

---

## Visual Timeline Blocks

Animation Clip Nodes are shown as colored horizontal blocks on the timeline tracks. 

### Waveform Visualization
To help you align motion, each block can visualize the underlying animation curves directly on the timeline track. You can customize this globally in the composition settings (**Waveform Mode**):
* **First Curve**: Draws the first animated float curve of the clip as a thin wave line across the node block.
* **Energy Bars**: Computes the root-mean-square (RMS) velocity energy of the curves and draws them as vertical volume bars across the block.

---

## Positioning and Resizing

You can interact with clip blocks directly in the timeline:
* **Move**: Click and drag the middle of a block to shift its start time.
* **Resize**: Click and drag the left or right edges of the block to change its duration.

### Resize Modes
How a clip behaves when you stretch or shrink its block bounds is determined by the **Resize Mode** setting in the block's Inspector:

| Resize Mode | Action on Resizing |
|:---|:---|
| **Trim** | The playback speed of the animation remains constant. Stretching the block makes the clip play longer (revealing more of the source clip or applying extrapolation). Shrinking the block clips the end of the animation. |
| **Scale** | The entire duration of the source animation is stretched or compressed to fit the visual block bounds exactly. Stretching the block slows the playback speed down, while shrinking it speeds it up. |

---

## Inspector Parameter Reference

When you select an Animation Clip Node, the following parameters are available in the Inspector/Details panel:

### Clip Settings

* **Clip**: The Unity Animation Clip asset loaded into this slot.
* **Is Embedded**: A checkbox indicating whether the clip asset is physically saved inside this Composition asset (like layers in a PSD file) or referenced as an external standalone file.
  * *Workflow Tip:* Embedded clips are fully portable—copying the composition asset copies the clips inside it. You can extract them at any time to standalone files.
* **Clip Offset**: The start offset (in seconds) from the beginning of the source clip. Playback will begin from this timestamp.
* **Playback Speed**: A static playback speed multiplier. A value of `1.0` is normal speed. Negative values (e.g. `-1.0`) play the animation backward.
* **Use Speed Curve**: Enables using an Animation Curve to modulate playback speed dynamically over the node's duration instead of a static speed multiplier.
* **Speed Curve**: The keyframed speed curve. The Y-axis represents the speed multiplier, while the X-axis is the normalized duration (0.0 to 1.0) of the block.
* **Extrapolation Mode**: Determines how the animation behaves if the node duration is longer than the source animation clip:
  * **Hold**: Freezes the character at the final frame of the animation clip for the remainder of the block.
  * **Loop**: Continuously restarts the animation clip from its beginning.
  * **PingPong**: Plays the animation forward, then backward, then forward, in a continuous yoyo loop.
  * **None**: Stops playing the animation altogether (bone transforms bleed through entirely from lower layers).

---

## Advanced Event Rules

Unity Animation Clips often contain **Animation Events** (functions triggered at specific times in the clip). When an animation clip is looped or stretched in a composition, triggering these events can become chaotic. The **Advanced Event Rules** panel lets you control this behavior:

* **Mute Events**: A checkbox that completely silences/blocks all events inside this specific block from executing.
* **Event Max Loop Count**: Restricts event triggers to a specific number of loop iterations.
  * For example, if set to `1`, events will only trigger during the first loop of the animation, remaining silent during subsequent loops. Set to `-1` for infinite triggers.
* **Event Start Loop Index**: Delay event triggers until the clip has looped a certain number of times.
  * For example, if set to `2`, events will remain silent during the initial play and the first loop, only starting to fire on the second loop.
* **Event Time Offset**: Shifts the execution of all events in this slot by a constant time offset (in seconds) relative to their original position in the clip.
* **Event Loop Interval Delay**: Inserts a custom pause delay (in seconds) between loops before the animation events are allowed to repeat.
