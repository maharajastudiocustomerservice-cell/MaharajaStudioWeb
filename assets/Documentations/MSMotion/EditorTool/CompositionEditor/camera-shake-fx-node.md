# Camera Shake FX Node

The **Camera Shake FX Node** triggers procedural screen shake events (for dramatic actions like ground stomps, heavy landing impacts, spell explosions, or boss roar screens).

---

## Cinemachine Integration

The Camera Shake node interfaces directly with Unity's **Cinemachine** package (using Cinemachine Impulse):

* **Impulse Source Prefab**: If Cinemachine is active, this field allows you to assign a Cinemachine Impulse Source prefab. The system will instantiate this prefab at the target socket bone to fire camera shake signals directly into Cinemachine cameras.

---

## Inspector Parameter Reference

Configure the Camera Shake properties in the details panel:

### Shake Core Properties

* **Amplitude**: The intensity scale of the shake (0.0 to 5.0). Higher values create larger screen displacements.
* **Frequency**: The speed of shake oscillations (0.1 to 10.0). Higher values create fast, jittery buzz shakes; lower values create slow, rolling sway movements.
* **Impulse Direction**: A direction vector (default: `0, 1, 0`) defining the primary axis of the shake impact.
* **Use Character Forward**: When checked, rotates the **Impulse Direction** vector to align with the character's forward direction at the trigger time.
  * *For example:* A recoil slide shake can be aligned to push the screen backward relative to whichever direction the character is facing.
* **Propagation Radius**: The distance (in meters) within which cameras are affected by this shake. Cameras sitting outside this radius will not shake (ideal for local explosion visual feedback).

---

## Amplitude & Frequency Transitions

You can automate shake intensity decay dynamically over the timeline duration:

* **Use Amplitude Transition In / Out**: Enables fading the shake volume strength using curves.
  * **Amplitude Transition In / Out Curve**: Easing curves (Y-axis = strength multiplier, X-axis = normalized time).
* **Use Frequency Transition In / Out**: Enables modulating the shake speed using curves.
  * **Frequency Transition In / Out Curve**: Easing curves (Y-axis = speed multiplier, X-axis = normalized time).
