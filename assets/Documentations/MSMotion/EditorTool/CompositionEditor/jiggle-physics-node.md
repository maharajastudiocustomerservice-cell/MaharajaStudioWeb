# Jiggle Physics Node

The **Jiggle Physics Node** applies secondary spring-mass physics to chains of bones (such as hair, capes, tails, ears, or loose accessories). The physics simulation reacts dynamically to the character's primary animations and movement.

---

## Spring-Mass Core Mechanics

The physics simulation is driven by a spring-mass solver configured in the Inspector:

* **Stiffness**: How strongly the bones try to return to their original animated poses (0.01 to 1.00). High stiffness makes bones spring back quickly; low stiffness makes them loose and floppy.
* **Damping**: How much energy is lost per frame (0.00 to 1.00). Higher values cause the jiggle to settle faster, preventing endless oscillations.
* **Mass**: The resistance of the bones to motion (0.1 to 5.0). Higher mass creates more inertia, causing larger lag and dramatic overshoot during movements.
* **Simulate in Local Space**: When enabled, the simulation is computed within the character's local coordinates rather than world space.
  * *Workflow Tip:* Enable local space simulation for extremely fast-moving characters (such as characters teleporting or riding mounts) to prevent the physics from stretching or breaking during sudden displacements.

### Falloff Curves (Root-to-Tip Modulation)
Physically, the root of a tail or hair braid is usually stiffer than the floppy tip. You can model this using the falloff curves:
* **Stiffness Falloff / Damping Falloff**: Standard curves where the X-axis is the index along the bone chain (0.0 = root bone, 1.0 = tip bone) and the Y-axis is the property multiplier.
* **Stiffness/Damping Time Curves**: Modulates stiffness and damping over the absolute duration of the timeline slot (X-axis = normalized duration).

---

## Environment & External Forces

* **Gravity**: A direction vector (default: `0, -9.81, 0` representing world gravity).
* **Gravity Multiplier**: Scale multiplier for gravity strength (0.0 to 5.0).
* **Use Local Gravity**: When active, gravity is calculated relative to the character's rotation, bending tail/cape assets in a fixed direction relative to the spine.
* **Centrifugal Multiplier**: Multiplies the outward centrifugal force applied to jiggle chains when the character performs sharp rotations.
* **Wind Strength**: The base pressure force of constant wind blowing on the bone chain.
* **Wind Direction**: The direction vector of the wind.
* **Turbulence Speed / Frequency**: Generates noise in the wind force to create organic, fluttering motions.

---

## Volume Preservation (Squash & Stretch)

To prevent jiggling chains from looking like rigid rods when stretched, you can enable volume preservation:

* **Enable Squash & Stretch**: Toggles procedural scale deformation on the jiggle transforms.
* **Max Stretch**: The maximum elongation factor allowed.
* **Squash Multiplier**: Determines how much the bones shrink along their perpendicular axes when stretched along their length, maintaining visual volume.

---

## Colliders & Collision Shapes

To prevent jiggle bones from clipping through the character's body or the environment, you can define custom collider shapes inside the **Colliders** panel:

### 1. Collision Properties
* **Enable Colliders**: Globally enables or disables collider interactions.
* **Enable Self Collision**: When active, bones in the jiggle chain are blocked from passing through each other.
* **Self Collision Radius**: The spherical thickness around each jiggle bone used for self-collision detection.

### 2. Custom Collider Shapes
You can add shapes directly within the modifiers interface:

| Shape | Dimensional Properties | Setup |
|:---|:---|:---|
| **Sphere** | **Radius** | Best for head, shoulders, or hands. |
| **Capsule** | **Radius**, **Height**, **Capsule Axis** (X, Y, Z) | Best for limbs, torso, or long neck structures. |
| **Box** | **Box Size** (Width, Height, Depth) | Best for furniture, shield objects, or steps. |
| **Plane** | **Plane Normal** (Direction vector) | Creates an infinite ground boundary below which bones cannot fall. |

Each custom collider is attached to a **Parent Bone Path** and positioned using a **Local Offset** offset matrix.
