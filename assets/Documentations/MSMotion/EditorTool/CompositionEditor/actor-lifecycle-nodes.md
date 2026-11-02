# Dynamic Actor Lifecycle Nodes

**Dynamic Actor Lifecycle Nodes** control the precise moment, spatial placement, entry transitions, and pool recycling of temporary or summoned actors (such as weapons, familiars, dragons, or Stand avatars) directly on the composition timeline.

To add lifecycle nodes to the timeline:
*   Right-click on an FX or Actor track and choose **Actor > Add Spawn Actor Node Here** or **Actor > Add Destroy Actor Node Here**.
*   Or click **+ Add Spawn Node** / **+ Add Destroy Node** inside the [Actor Roster Window](actor-roster-window.md) when a dynamic actor's timing preset is set to `Custom`.

---

## 1. Spawn Actor Node

The **Spawn Actor Node** triggers the instantiation and visual entry of a dynamic actor.

```
+-------------------------------------------------------+
|  [Spawn Actor]  Duration: 0.20s                       |
+-------------------------------------------------------+
```

### Parameter Reference

*   **Attachment Mode**: Defines how the spawned entity connects to the scene:
    *   **World Sync Offset**: Spawns relative to the shared composition sync anchor.
    *   **Caster Root Relative**: Tracks the caster's root position while maintaining an authored offset.
    *   **Caster Bone Socket**: Attaches as a child of a specific bone on the caster character (e.g., `RightHand`, `Spine`, `Head`).
*   **Attach Socket Bone**: Name of the target socket bone when using socket attachment mode.
*   **Position Offset**: Local Vector3 spatial offset applied relative to the attachment target.
*   **Rotation Offset Euler**: Local rotation angles applied relative to the attachment target.
*   **Scale Offset**: Initial scale factor applied to the spawned entity (default: `1, 1, 1`).

### Entry Transitions & Blending

*   **Use Scale Transition In**: Enables an animated scale curve over the node's duration.
*   **Scale Transition Curve**: Custom animation curve defining scale growth from spawn time (e.g. popping up from 0 to 1, or overshooting for a dynamic impact).
*   **Fade In Duration**: Time (in seconds) over which material alpha or visual intensity ramps up smoothly.
*   **Show Gizmo**: Displays an interactive position/rotation handle in the Scene View to visually position the spawn location.

---

## 2. Destroy Actor Node

The **Destroy Actor Node** handles the graceful despawn, fade-out, and pool recycling of a dynamic actor when its action completes.

```
+-------------------------------------------------------+
|  [Destroy Actor]  Duration: 0.25s                     |
+-------------------------------------------------------+
```

### Parameter Reference

*   **Fade Out Duration**: Time (in seconds) over which the entity fades out or dissolves before removal.
*   **Use Scale Transition Out**: Enables an animated exit scale curve.
*   **Scale Transition Curve**: Custom animation curve controlling how the entity shrinks or collapses before recycling.
*   **Return to Pool**: When enabled, recycles the actor's GameObject back to the internal object pool rather than destroying it. Always keep this checked for smooth gameplay performance and zero runtime heap allocations.

---

## Workflow: Authoring a Familiar or Weapon Summon

1. Open the [Actor Roster Window](actor-roster-window.md) (**👥 Actors** on the top toolbar).
2. Click **+ Add Participant Character** and set its **Actor Type** to **Dynamic**.
3. Assign the entity's prefab and set its spawn and destroy timing to **Custom**.
4. In the timeline, move the playhead to where the character begins summoning and add a **Spawn Actor Node**.
5. Position the spawn handle in the Scene View (or choose a socket bone like `RightHand`).
6. Add animation clip blocks on the dynamic actor's track to drive its motion during the sequence.
7. Move the playhead to the end of the action and place a **Destroy Actor Node** with a `0.2s` fade-out and **Return to Pool** checked.
8. Scrub the timeline to preview the summon appearing, animating, and despawning smoothly!
