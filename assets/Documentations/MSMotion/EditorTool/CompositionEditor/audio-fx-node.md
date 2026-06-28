# Audio FX Node

The **Audio FX Node** triggers audio playback at a specific timeline mark. It is commonly used for sound effects like footstep rustles, sword slashes, impact thuds, or character vocalizations.

---

## Inspector Parameter Reference

Configure the Audio FX properties in the details panel:

### Audio Asset & Playback Properties

* **Clip**: The Unity AudioClip asset played by this node.
* **Volume**: The base volume slider (0.0 to 1.0).
* **Pitch**: The playback pitch speed (0.1 to 3.0). A value of `1.0` is normal pitch.
* **Pitch Variance**: Adds random pitch variance (0.0 to 1.0) to every trigger.
  * *Workflow Tip:* Set **Pitch Variance** to a low value (e.g. `0.05` to `0.10`) for repetitive sounds like footsteps or sword swings. This minor variation prevents the sound from feeling mechanical or repetitive.
* **Stereo Pan**: Constant panning between the left and right speakers (-1.0 to 1.0). Only active when **Spatial Blend** is set to 2D.

### Spatialization (3D vs. 2D)

* **Spatial Blend**: Smoothly interpolates the sound source type:
  * **0.0 (2D)**: Plays directly through the headphones/speakers with static panning (ideal for background music or global UI cues).
  * **1.0 (3D)**: Attenuates sound based on the distance between the camera listener and the character's target bone location (ideal for point-source sound effects).
* **Min Distance**: The distance (in meters) from the source where the volume remains at full strength.
* **Max Distance**: The distance (in meters) beyond which the sound is no longer audible.

---

## Volume & Pitch Automation

You can fade audio parameters dynamically over the node's timeline duration:

* **Use Volume Transition In / Out**: Enables fading the sound volume in or out using custom Animation Curves.
  * **Volume Transition In / Out Curve**: Easing curves driving volume. The Y-axis represents volume (0.0 to 1.0) and the X-axis is normalized time.
* **Use Pitch Transition In / Out**: Enables modulating the pitch over the node duration using curves.
  * **Pitch Transition In / Out Curve**: Easing curves driving pitch. The Y-axis represents pitch multiplier and the X-axis is normalized time.
