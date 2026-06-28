# Particle FX Node

The **Particle FX Node** spawns particle systems (like dust clouds, sparks, magical bursts, or fire trails) at specific socket targets.

---

## Inspector Parameter Reference

Configure the Particle FX properties in the details panel:

### Particle Spawn & Playback Settings

* **Prefab**: The particle system prefab asset instantiated by this node.
* **Play Mode**:
  * **OneShot**: Spawns the prefab and fires a single burst of particles before stopping.
  * **Continuous**: Instantiates the particle system and keeps it emitting particles for the entire duration of the timeline slot.
* **Emit Count**: The number of particles emitted during a **OneShot** burst trigger.
* **Scale Multiplier**: A scale multiplier (0.01 to 10.00) to adjust the particle size without altering the base prefab asset.
* **Attach to Bone**: If checked, parents the instantiated particle GameObject directly to the socket bone. If unchecked, the particle is spawned in the world at the bone's trigger position but remains there.
* **Wait for Completion**: When checked, delays the destruction of the spawned particle GameObject until all active particles have naturally decayed/died out, preventing ugly particle pops.

---

## Emission & Scale Transitions

You can automate particle intensity and dimensions dynamically over the timeline block:

* **Use Emission Transition In / Out**: Automates the emission rate using custom curves.
  * **Emission Transition In / Out Curve**: Easing curves driving emission scaling (Y-axis = rate multiplier, X-axis = normalized time).
* **Use Scale Transition In / Out**: Automates the physical transform size of the spawned system over time.
  * **Scale Transition In / Out Curve**: Easing curves driving scale (Y-axis = size multiplier, X-axis = normalized time).

---

## Spline Trajectory Path

You can configure particles to travel along custom spline paths relative to the character:
* Expand the **Trajectory** foldout to enable a local Bezier spline path. You can edit control points to make particles (e.g. magic projectiles, floating bubbles, or smoke trails) travel along exact paths away from the character's hands or feet.
* For details on how to generate, edit, and manipulate these spline paths, see the [FX Path Tools Scene Panel](fx-nodes-overview.md#fx-path-tools-scene-panel) section of the FX Nodes Overview.

