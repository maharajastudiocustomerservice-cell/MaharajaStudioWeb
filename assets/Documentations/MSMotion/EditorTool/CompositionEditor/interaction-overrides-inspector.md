# Interaction Overrides Preset Inspector

The **Interaction Overrides Preset Inspector** is a dedicated editor workspace for configuring post-export customization presets (`MSMotionInteractionOverrides` assets). It allows animators and designers to tailor multi-character choreographies for diverse gameplay situations—such as adapting body spacing for differing creature sizes, swapping character reaction clips, fine-tuning approach locomotion and pathfinding bounds, and redirecting prop handovers—**without altering baked interaction configs or writing code**.

---

## Accessing & Creating Overrides Presets

1. In the Unity Project window, right-click and choose **Create > Maharaja Studio > MsMotion > Interaction Overrides**.
2. Select the created asset to inspect it in the Inspector window.
3. In the **Target Interaction Config** field, assign the baked choreography config asset (e.g. `Takedown_Config` or `SalsaDuet_Config`).

---

## Interface Layout & Sections

```
+-----------------------------------------------------------------------------------+
| MSMotion Interaction Overrides (Banner)                                           |
| Target Interaction Config: [ S_Duet_Exported_Config                     (⊙) ]     |
+-----------------------------------------------------------------------------------+
| Detected Roles in Config                                                          |
| Participants: 2 | Dynamic Entities: 1 | Handovers: 2 | Duration: 4.37s | Loop: False |
| [ [Participant] partner (Actor_1) ▼ ]  [ Add Override ]                           |
| [               Populate All               ]  [             Sync from Config             ] |
+-----------------------------------------------------------------------------------+
| ▼ Interaction FX Registry (Global)                                                |
|   [✓] Global FX Registry Override: [ FXRegistry_DarkFlame                 (⊙) ]   |
+-----------------------------------------------------------------------------------+
| ▼ Participant Role Overrides (2)                                                  |
|   ...                                                                             |
| ▼ Dynamic Actor Overrides (1)                                                     |
|   ...                                                                             |
| ▼ Terrain Raycast Ground LayerMask                                                |
|   ...                                                                             |
| ▼ Live Runtime PlayMode Tools                                                     |
|   ...                                                                             |
+-----------------------------------------------------------------------------------+
```

### 1. Detected Roles in Config (Toolbar)
Scans the assigned **Target Interaction Config** and provides batch creation tools:
*   **Summary Readout**: Displays the total count of detected participant roles, dynamic summons, cross-actor handovers, total sequence duration, and looping state.
*   **Role Dropdown**: Lists all unassigned and assigned roles in the config (e.g. `[Participant] actor_0 (Actor_0)`, `[Dynamic] sword_summon`).
*   **Add Override**: Adds a custom override card for the role currently selected in the dropdown.
*   **Populate All**: One-click generation. Automatically inspects the interaction config and creates override cards for every participant character and dynamic summon.
*   **Sync from Config**: Refreshes all existing override cards with authored baseline values from the target config. Preserves all your active override checkbox states.

---

## 2. Interaction FX Registry (Global)

Located directly beneath the detected roles deck, the **Interaction FX Registry Card** allows designers to override all sound, visual particle, decal, and summon effects across the entire interaction session in one place:
*   **Global FX Registry Override**: Toggle checkbox + object picker (`MSMotionFXRegistry`). When enabled, this registry overrides FX events for all participating characters across the choreography unless an actor has a role-specific registry override assigned.
*   **Zero Asset Duplication**: Swaps entire audio/visual themes (e.g. fire vs ice, holy vs demonic) across all actors without authoring extra `MSMotionAnimationConfig` assets.

---

## 3. Participant Role Overrides

Each participant role card provides granular control over that specific character's animation, spacing, and approach locomotion:

### Card Header Controls
*   **Foldout Arrow (`▶` / `▼`) & Title**: Expands or collapses the role card. Displays the role identifier and active override counter (e.g. `Participant Role: 'actor_1' (4 active overrides)`).
*   **Track Sync Button (`🔄`)**: Re-syncs only this specific character's fields with their authored baseline values in the interaction track.
*   **Card Copy & Paste (`[Copy]` / `[Paste]`)**: Duplicates the entire role configuration to the clipboard, allowing you to paste settings onto other participant roles.

### Core Overrides
*   **Role Identifier**: Name of the character track (e.g. `actor_0`, `lead`, `partner`). Includes dedicated copy and paste buttons.
*   **Animation Config**: Toggle checkbox + object picker. Overrides the character's entire animation package, including blend curves and FX manifests.
*   **Animation Clip**: Toggle checkbox + clip picker. Swaps out the character's core performance clip while automatically inheriting the layer's authored parameters.
*   **FX Registry (Direct Role Override)**: Toggle checkbox + object picker (`MSMotionFXRegistry`). Directly overrides FX events (audio, particles, decals, transforms) specifically for this character without creating an intermediate `MSMotionAnimationConfig` asset. Takes precedence over the global interaction FX registry.
*   **Spatial Spacing (Offset)**: Always visible position ($X, Y, Z$) and rotation ($X, Y, Z$) fields with an override toggle. Offsets the character relative to the interaction sync point at frame 0. Includes dedicated `[Copy]` and `[Paste]` buttons to easily transfer spacing setups between assets.
    > [!TIP]
    > **Monster & Scale Compensation:** When executing a human grapple on a large Orc or Troll, enable **Spatial Spacing** and adjust the $Z$-offset to separate the characters and eliminate body clipping.
*   **Speed Multiplier**: Slider ($0.0 - 5.0\times$) to scale playback speed independently (useful for hit-stop pauses or heavy monster reaction delays).

---

## 3. Dynamic Alignment Approach Foldouts

When characters start an interaction from arbitrary scene locations, the **Dynamic Alignment System** moves them smoothly to their target sync spots. The 4 section headers are collapsible foldouts with **individual field toggles** and **active counter badges**:

### 🎬 Locomotion & Gaits
*   **Gait Mode**: `AutomaticWalkRun`, `WalkOnly`, `RunOnly`, or `TeleportSnap`.
*   **Walk Locomotion Clip**: The walking animation used during the approach.
*   **Run / Sprint Clip**: The running animation used when the character must travel a greater distance.
*   **Run Spd Min / Run Dist Min**: Velocity and distance thresholds required to trigger the run gait.
*   **Crossfade (s)**: Blending duration when switching between walking and running.
*   **Downshift on Arrival**: Decelerates from a run to a walk when approaching the arrival boundary.
*   **Waiting / Idle Clip**: Animation played if this character arrives early at their sync spot and waits for others.

### 🧭 Pathfinding & Navigation
*   **Navigation Mode**: `NoneLinear`, `SimpleObstacleAvoidance`, `NavMeshAgent`, or `NavMeshPathfinding`.
*   **Clearance (m)**: Capsule obstacle avoidance radius.
*   **Obstacle Mask**: Layer mask evaluated by obstacle detection raycasts.
*   **Corner Smoothing (m)**: Bezier corner fillet radius along waypoints.
*   **Track Moving Target**: Real-time recalculation if the partner is moving during the approach.
*   **Dynamic Lookahead & Lookahead Distance**: Projects forward raycasts to detect incoming dynamic obstacles.
*   **Adapt to Terrain (Raycast Snapping)**: Snaps character feet to uneven ground, ramps, and stairs.

### 🔄 Steering & Arrival Rotation
*   **Turn Speed (°/s)**: Angular turning velocity toward the approach path.
*   **Align Radius (m)**: Distance threshold where the character starts aligning with the final authored facing direction.
*   **Align Arrival Rotation**: Toggles orientation matching at the destination.
*   **Pivot In Place First & Pivot Angle Threshold**: Rotates on the spot before moving forward if the starting angle is wide.

### ⏱ Timing, Stride & Speed Bounds
*   **Natural Stride Speed (m/s)**: Locomotion velocity corresponding to a $1.0\times$ playback speed.
*   **⚡ Auto Stride Button**: Automatically analyzes the assigned Walk Locomotion Clip's root motion curves and extracts the exact stride velocity!
*   **Stop Dist (m)**: Arrival radius considered "at the destination".
*   **Min / Max Duration (s)**: Hard clamps on total allowed approach duration.
*   **Min / Max Playback (x)**: Playback speed bounds preventing sliding or unnatural fast-forwarding.
*   **Accel / Decel (m/s²)**: Physical acceleration and braking rates.
*   **Velocity Profiling & Custom Velocity Curve**: User-defined curve driving non-linear approach speed.
*   **Transition Override (s)**: Crossfade length from arrival into the main choreography.

### Foldout Productivity Features
*   **Right-Click Context Menu**: Right-click any category header to open a menu with **Enable All Overrides in Section** or **Disable All Overrides in Section**.
*   **Section Copy & Paste**: Every category header has dedicated `[Copy]` and `[Paste]` buttons. Pasting settings into a section automatically unfolds it to reveal the pasted values.

---

## 4. Dynamic Actor Overrides (Summons & Props)

Overrides the appearance, placement, scale, and timing of temporary entities spawned during the choreography:
*   **Prefab Override**: Swaps the summoned object's prefab (e.g. skin variants or elemental swords).
*   **Socket Override**: Retargets the attachment bone on the caster character (e.g. `RightHand`, `Spine2`).
*   **Local Position & Euler Rotation**: Offsets relative to the attachment socket.
*   **Scale Override**: Multiplies the object's 3D scale (e.g. giant summoning variants).
*   **Spawn & Destroy Timing**: Overrides normalized timeline moments ($0.0 - 1.0$) for appearance and despawn.

---

## 5. Terrain Ground LayerMask

*   **Override Ground LayerMask**: Overrides the raycast LayerMask used across the entire interaction for downward ground snapping. Ensures feet plant correctly on custom environment layers.

---

## 6. Live Runtime PlayMode Tools

When entering Unity Play Mode with an interaction running in the scene:
*   The inspector automatically detects matching active interaction sessions.
*   Displays real-time session feedback: playing status and elapsed duration.
*   **Apply Overrides to Active Session Button**: Hot-reloads all inspector modifications directly into the running scene session without restarting playback!
