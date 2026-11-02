# Multi-Actor Interaction & Choreography System

**MSMotion 2.0.0** introduces the **Multi-Actor Interaction & Choreography System**, enabling creators to author and execute complex synchronized multi-character animations — such as dance duets, martial arts grapples/takedowns, shared lifts, co-op puzzle interactions, and 3+ character cinematics — with **one line of code** and full runtime control.

---

## Key Capabilities

*   **Synchronized Multi-Character Choreography**: Coordinate 2, 3, or more characters playing interdependent animations with 0ms frame drift.
*   **Humanoid & Generic (Non-Humanoid) Support**: Seamlessly mix Humanoids with Generic rigs (quadrupeds, monsters, robots, props) in the exact same choreography.
*   **Independent PlayableGraph Isolation**: Every character maintains its own independent `MSMotionAnimator` and `PlayableGraph`. The system orchestrates them without graph conflicts, evaluation order glitches, or race conditions.
*   **Dynamic Participant Departure**: Characters can break away or leave early (e.g. taking damage, hit reaction, interrupted) while remaining characters smoothly continue or cancel the choreography.
*   **Cross-Actor Partner Targeting**: Hand/foot IK effectors and head look-at modifiers can directly target bones on partner characters.

---

## 1-Line-of-Code Runtime API

Playing a synchronized multi-character interaction requires just one line of C#:

```csharp
using System.Collections.Generic;
using MaharajaStudio.MSMotion.Runtime;
using UnityEngine;

public class InteractionTrigger : MonoBehaviour
{
    [SerializeField] private MSMotionInteractionConfig salsaDuetConfig;
    [SerializeField] private MSMotionInteractionOverrides trollTakedownOverrides;
    [SerializeField] private MSMotionFXRegistry darkFlameRegistry;
    [SerializeField] private Transform movingStageAnchor;
    [SerializeField] private MSMotionAnimator leadDancer;
    [SerializeField] private MSMotionAnimator partnerDancer;

    public void PlayStandard()
    {
        // 1. Plays synchronized at lead character's position
        MSMotionInteraction.Play(salsaDuetConfig, leadDancer, partnerDancer);
    }

    public void PlayOnMovingTransform()
    {
        // 2. Dynamically anchored to a moving platform, elevator, or vehicle
        MSMotionInteraction.Play(salsaDuetConfig, movingStageAnchor, leadDancer, partnerDancer);
    }

    public void PlayWithDirectFXRegistry()
    {
        // 3. Direct FX Registry injection (replaces audio/particles without extra animation configs)
        MSMotionInteraction.Play(salsaDuetConfig, darkFlameRegistry, leadDancer, partnerDancer);
    }

    public void PlayWithPerRoleFX()
    {
        // 4. Per-role FX Registry dictionary (e.g. fire partner vs ice victim)
        var roleRegistries = new Dictionary<string, MSMotionFXRegistry>
        {
            { "lead", fireRegistry },
            { "partner", iceRegistry }
        };
        MSMotionInteraction.Play(salsaDuetConfig, roleRegistries, leadDancer, partnerDancer);
    }

    public void PlayWithOverrides()
    {
        // 5. Designer-authored ScriptableObject overrides preset
        MSMotionInteraction.Play(salsaDuetConfig, trollTakedownOverrides, leadDancer, partnerDancer);
    }
}
```

---

## Native Unity 6 Async Execution (`PlayAsync`)

When sequencing game choreography, cutscenes, combat finishers, or dialogue interactions, you can use Unity 6's native `Awaitable` to await completion asynchronously:

```csharp
public async Awaitable ExecuteCinematicDuet()
{
    // Plays and suspends execution until the interaction finishes naturally or is stopped
    var session = await MSMotionInteraction.PlayAsync(salsaDuetConfig, leadDancer, partnerDancer);
    
    Debug.Log($"Interaction {session.Config.name} finished! Continuing cutscene...");
}

public async Awaitable ExecuteWithCancellation(CancellationToken ct)
{
    // Awaits with full cancellation token support (e.g. player skipped cutscene)
    await MSMotionInteraction.PlayAsync(salsaDuetConfig, movingStageAnchor, ct, leadDancer, partnerDancer);
}
```

---

## Query, Introspection & Session Lifecycle

MSMotion provides zero-allocation static utilities to query, pause, and control active interaction sessions from gameplay systems or combat managers:

```csharp
// Query status
bool isBusy = MSMotionInteraction.IsInInteraction(character);
bool isSequenceRunning = MSMotionInteraction.IsInteractionActive(salsaDuetConfig);

// Introspection
if (MSMotionInteraction.TryGetSession(character, out var session))
{
    Debug.Log($"Playing interaction elapsed: {session.ElapsedTime}s (Progress: {session.NormalizedTime * 100f}%)");
}

// Global pause / resume (e.g. during game pause menu or dialogue popups)
MSMotionInteraction.PauseAllInteractions();
MSMotionInteraction.ResumeAllInteractions();

// Stop specific actor with cascade policy
MSMotionInteraction.StopInteractionFor(character, fadeOutTime: 0.2f, InteractionCascadePolicy.ContinueRemaining);

// Stop all interactions
MSMotionInteraction.StopAllInteractions(fadeOutTime: 0.25f);
```

---

## Fluent Builder & Runtime Control

`MSMotionInteraction.Play` or `MSMotionInteraction.Prepare` returns an `MSMotionInteractionSession` instance that exposes fluent chaining controls:

```csharp
MSMotionInteraction.Prepare(salsaDuetConfig, leadDancer, partnerDancer)
    // Dynamic Transform anchor or static world position
    .SetSyncPoint(movingStageAnchor)
    
    // Direct FX Registry overrides without extra animation configs
    .OverrideFXRegistry(darkFlameRegistry)
    .OverrideActorFXRegistry("partner", holyAuraRegistry)
    
    // Custom crossfade durations
    .SetFadeIn(0.3f)
    .SetFadeOut(0.25f)
    
    // Lifecycle callbacks
    .OnComplete(() =>
    {
        Debug.Log("Dance duet completed successfully!");
    })
    .OnActorStopped(actor =>
    {
        Debug.Log($"{actor.name} left the interaction.");
    })
    .OnTick(currentTime =>
    {
        // Monitor live playhead progress
    })
    .Play();
```

---

## Dynamic Participant Departure (`StopActor`)

In games, characters often need to break away from an interaction early — for example, if **Character C** takes damage, is interrupted by combat, or triggers a ragdoll.

The system provides `StopActor` with an `InteractionCascadePolicy`:

```csharp
// Character B gets hit by an arrow and must react immediately
session.StopActor(characterB, fadeOutTime: 0.15f, InteractionCascadePolicy.ContinueRemaining);
```

### Cascade Policies

| Policy | Behavior | Typical Use Case |
| :--- | :--- | :--- |
| `ContinueRemaining` *(Default)* | The specified actor blends out to idle or hit reaction. Remaining participants continue their choreography uninterrupted to completion. | Group combat finishers, 3+ dancer choreography, co-op interactions where one character breaks off. |
| `StopAll` | If any critical actor leaves, the entire interaction is terminated smoothly for all participants. | Partner lifts, acrobatic stunts, or intimate dance holds where the absence of one character invalidates the scene. |

---

## Authoring Multi-Actor Interactions in the Editor

1. Open the **Composition Editor** (`Tools > Maharaja Studio > MsMotion`).
2. Click the **👥 Actors** button on the top toolbar to open the **Actor Roster Window**.
3. Click **+ Add Participant Character** to add Actor B, Actor C, etc.
4. For each character:
   * Assign their role name (e.g. `Lead`, `Partner`, `Monster`).
   * Select their **Rig Type** (`Humanoid` or `Generic`).
   * Assign their scene preview `GameObject`.
5. On any timeline slot or layer, use the **Target Character Dropdown** to assign which actor the clip or solver drives.
6. Scrub the playhead to preview all characters animating simultaneously in the Scene View!
7. Click **Export** to generate the baked `MSMotionInteractionConfig` asset.

---

## Cross-Actor IK & Look-At Targeting

When authoring physical contact (e.g., holding hands, waist grabs, takedowns) or eye contact:

*   **IK Chain Modifier**: Set `PartnerActorId` to target a partner character, and specify either `PartnerHumanBone` (for Humanoids) or `PartnerBonePath` (for Generic rigs). The effector pins directly to the partner's bone in world space.
*   **Look-At Modifier**: Set `PartnerActorId` to make a character dynamically turn their head, spine, and eyes toward the partner's head or chest during the sequence.

---

## Dynamic / Temporary Actors (Summons & Ephemeral Entities)

In addition to persistent scene characters, MSMotion supports **Dynamic / Temporary Actors** — ephemeral entities like summoned dragons, phantom weapons, Stand avatars, spectral beasts, or familiars that:
- Spawn automatically at a precise moment in the animation.
- Attach to the caster's root, a specific bone/socket (e.g. right hand, spine), or the world sync point.
- Play their companion animation in full synchronization.
- Automatically despawn, dissolve/fade out, and recycle back to the zero-allocation `MSMotionActorPool`.
- **Zero Gameplay Code Required**: The gameplay programmer merely calls `animator.Play(attackConfig)`. The companion interaction engine manages the dynamic actor's lifecycle under the hood.

### Lifecycle Timing Presets & Custom Nodes

In the **Actor Roster Window** (`👥 Actors`), set the actor's **Actor Type** to `Dynamic`:
1. **Dynamic Prefab**: Assign the prefab asset to spawn.
2. **Spawn Time**: Choose from `0`, `0.25`, `0.5`, `0.75`, `1.0`, or `Custom`.
3. **Destroy Time**: Choose from `0`, `0.25`, `0.5`, `0.75`, `1.0`, or `Custom`.
4. **Attachment**: Choose `CasterBoneSocket` (e.g. `RightHand`), `CasterRootRelative`, or `WorldSyncOffset`.

When set to `Custom`:
- Click **+ Add Spawn Node** or add via timeline context menu (`Actor > Add Spawn Actor Node Here`) to place a `SpawnActorSlot` at any frame.
- Click **+ Add Destroy Node** or add via timeline context menu (`Actor > Add Destroy Actor Node Here`) to place a `DestroyActorSlot` at any frame.
- Custom nodes provide granular control over spatial offsets, entry scale curves, fade durations, and pool recycling policies.

---

## Motion Warping & Dynamic Alignment System

In gameplay scenarios, characters rarely stand at the exact millimetric coordinate authored for a synchronized duet or grapple. For example, a partner might be standing 1.5 meters away on flat ground, while in another instance they are 4 meters away on a staircase.

The **Motion Warping & Dynamic Alignment System** bridges arbitrary starting distances dynamically:
- Secondary actors travel smoothly toward their authored sync spots using their designated locomotion clip (e.g. walk, run).
- Animation playback speed dynamically scales to match their travel distance and duration without foot sliding.
- Characters arriving early enter a **Waiting / Idle** state until all participants reach their spots.
- Once all participants arrive, all actors seamlessly crossfade into the main synchronized choreography together.

### Pre-Interaction Entry Phase Architecture

Because approach duration is dynamic and dependent on real-time distance, Dynamic Alignment operates as an **asynchronous Pre-Interaction Entry Phase** rather than a fixed timeline block:
- **Clean Choreography Timeline**: The timeline strictly represents the authored synchronized choreography starting at $t = 0$.
- **Actor Roster & Alignment Window**: Configured directly in the **Actor Roster Window** (`👥 Actors > ⚡ Dynamic Alignment` tab or `⚡ Alignment` toolbar button).
- **Zero Timeline Clutter**: Eliminates artificial fixed-duration blocks, timeline dead space, and desync risks.

### Configurable Bounds & Fields

| Field | Description | Default |
| :--- | :--- | :--- |
| **Approach Locomotion Clip** | Walk, jog, or run animation played while traveling to the sync point. | *(AnimationClip)* |
| **Waiting / Idle Clip** | Animation played when this character arrives early or is waiting for others. | *(AnimationClip)* |
| **Primary Actor Waiting Clip** | Animation played by Actor 0 while waiting stationary at the sync origin. | *(AnimationClip)* |
| **Min / Max Time** | Allowed approach duration window in seconds (e.g. 0.5s to 4.0s). | `0.5s - 4.0s` |
| **Min / Max Speed** | Playback speed multiplier bounds (e.g. 0.5x to 2.0x) preventing unrealistic fast-forwarding or foot sliding. | `0.5x - 2.0x` |
| **Natural Stride Speed** | Locomotion speed in m/s. Click **Auto Stride** to derive directly from clip root motion curves. | `1.4 m/s` (or Auto) |
| **Arrival Threshold** | Distance in meters considered "arrived" at the sync spot. | `0.1 m` |
| **Adapt to Terrain** | Raycasts terrain downward during approach to keep feet planted on stairs or slopes. | `true` |

### Scene View Visualizer & Manipulator

When Dynamic Alignment is enabled on the composition:
- **Sync Spot Targets**: Cyan arrival boundary discs mark each character's target spot with authored facing arrows.
- **Lead Sync Origin**: Gold marker highlighting Actor 0's synchronization anchor.
- **Live Trajectory Lines**: Dynamic dotted lines connect each character's current scene position to their sync spot.
- **Real-Time Readouts**: Displays live distance, estimated duration, and calculated animation playback speed (e.g. `➤ Actor 1: 3.2m | 2.1s @ 1.07x speed`).
- **Scene HUD**: Bottom-left HUD includes quick actions to **Snap to Sync Spots** or **Test Approach Offsets** (scatters actors back by 3m to visually test approach speeds).

---

## Overriding Multi-Actor Interaction Animations

While single-actor animations can easily be overridden via `animator.Play(config, overrides)`, multi-actor choreography involves interdependent participant graphs and synchronization constraints. MSMotion provides **3 seamless approaches** to override multi-actor animations post-export without modifying assets or re-exporting.

### 1. Safe Pre-Flight Preparation (`MSMotionInteraction.Prepare(...)`)
When configuring runtime overrides, calling `Play()` immediately starts PlayableGraphs at frame 0. If you chained overrides after `Play()`, the graph had already evaluated. The `Prepare()` workflow decouples initialization from playback:

```csharp
// 1. Prepare session without starting playback immediately
var session = MSMotionInteraction.Prepare(grappleConfig, attackerAnim, victimAnim);

// 2. Chain pre-flight overrides safely before frame 0
session.OverrideActorClip("victim", heavyArmorReactionClip)
       .OverrideRoleOffset("victim", new Vector3(0f, 0f, 2.2f), Quaternion.identity)
       .SetActorSpeedMultiplier("victim", 0.8f);

// 3. Initiate synchronized playback
session.Play();
```

### 2. Direct Role Animation Swapping (`OverrideActorClip` / `OverrideActorConfig`)
You can dynamically swap an actor's core animation clip or entire config at runtime based on gameplay state (e.g. character class, armor tier, or injury level):

```csharp
// Swap with a simple AnimationClip (auto-generates transient config inheriting track layer & rules):
session.OverrideActorClip("victim", femaleReactionClip);

// Or swap with a complete MSMotionAnimationConfig asset with customized blend curves & FX manifests:
session.OverrideActorConfig("victim", armoredReactionConfig);
```

### 3. Designer-Facing Asset Overrides (`MSMotionInteractionOverrides` Asset & Custom Inspector)
For non-technical designers and technical artists, overrides can be authored entirely in the Unity Inspector as reusable ScriptableObject data assets:

1. In the Project window, right-click and choose **Create > Maharaja Studio > MsMotion > Interaction Overrides**.
2. Assign the **Target Interaction Config** (e.g. `Takedown_Config`).
3. Use the responsive toolbar to **Add Override** for a selected role, click **Populate All** to auto-generate cards for all participant and dynamic roles, or click **Sync from Config** to refresh values with authored baseline tracks.
4. Customize with **granular field-level checkboxes**:
   * **Full Baseline Pre-Filling**: Fields are populated automatically from the interaction config (just like FX Registry), so you can see existing values before overriding.
   * **Animation & Clip Variants**: Swap clips or configs per role.
   * **Spatial Spacing (Body Size Compensation)**: Adjust local position/rotation offsets to eliminate mesh clipping between giants, rogues, or monsters (with dedicated `[Copy]` / `[Paste]` buttons).
   * **Speed Multipliers**: Configure independent hit-stop or impact lag multipliers per character.
   * **4 Dynamic Alignment Foldout Categories**:
     * **🎬 Locomotion & Gaits**: Gait modes, walk/run clips, threshold speeds, crossfade durations, and arrival downshifting.
     * **🧭 Pathfinding & Navigation**: Obstacle avoidance radii, corner smoothing, moving target tracking, and terrain raycasting.
     * **🔄 Steering & Arrival Rotation**: Angular turn speeds, arrival alignment radii, and pivot-in-place thresholds.
     * **⏱ Timing, Stride & Speed Bounds**: Root-motion extraction (**⚡ Auto Stride**), min/max playback speeds, and custom velocity curves.
   * **Foldouts & Quick Actions**: Category headers collapse to save vertical space, display active override counters (e.g. `(4/8)`), support right-click **Enable/Disable All**, and feature category-level `[Copy]` and `[Paste]` buttons.
   * **Dynamic Actor Overrides**: Swap summoned weapon/prop prefabs, bone attachment sockets, scales, and spawn timings.
   * **Handover Redirects**: Redirect prop/weapon handover to alternative teammates or target sockets.
   * **Live Runtime PlayMode Tools**: Detects active scene sessions with a 1-click **Apply Overrides to Active Session** button for live testing.
5. Apply in C# with a single line:

```csharp
[SerializeField] private MSMotionInteractionOverrides trollTakedownOverrides;

public void TriggerInteraction()
{
    // 1-line execution with designer-authored overrides:
    MSMotionInteraction.Play(takedownConfig, trollTakedownOverrides, playerAnim, enemyAnim);
}
```

> [!TIP]
> **Complete Reference:** For full property breakdowns, data models, recipes, and API reference, see the dedicated **[Interaction Overrides System Guide](interaction-overrides.md)**.

---

## Cross-Actor FX & Prop Handover

Multi-actor choreography often features physical objects or effects moving between characters — such as handing a torch to a partner, disarming an opponent's sword, passing a potion flask, or throwing a shared energy orb.

MSMotion provides **Cross-Actor Handover** integrated directly into the runtime FX pipeline via `FXHandoverData` and `FXHandoverEvaluator`:

```csharp
// Example: Querying or dynamically enabling handover on an event
fxEvent.Handover.Enabled = true;
fxEvent.Handover.ReceiverActorId = "partner";
fxEvent.Handover.ReceiverHumanBone = HumanBodyBones.RightHand;
fxEvent.Handover.HandoverTime = 0.5f;          // Transfer starts at 50% normalized clip time
fxEvent.Handover.TransitionDuration = 0.15f;    // 15% window to glide across
fxEvent.Handover.TransitionMode = FXHandoverTransitionMode.SmoothInterpolation;
fxEvent.Handover.RetainOnEnd = true;           // Keep attached to partner after dance ends
```

### Supported FX Node Types

Cross-Actor Handover is supported across all visual, audio, and physical effect nodes that instantiate or control independent scene objects/components:

| FX Handler | Handover Capabilities |
| :--- | :--- |
| **Spawn FX** (`SpawnFXHandler`) | Instantiated weapon/prop prefabs transfer sockets between participants seamlessly. |
| **Particle FX** (`ParticleFXHandler`) | Particle systems (auras, torches, trail emitters) re-anchor and transition to partner bones. |
| **VFX Graph FX** (`VFXGraphFXHandler`) | Visual Effect Graph instances glide or snap to partner attachment sockets. |
| **Decal FX** (`DecalFXHandler`) | Projected surface decals or decal projector objects re-parent across participants. |
| **Audio FX** (`AudioFXHandler`) | 3D spatialized audio emitters travel between characters (e.g. humming magical artifacts). |
| **Camera Shake FX** (`CameraShakeFXHandler`) | Dedicated Cinemachine impulse origins travel between actors during physical interactions. |

> [!NOTE]
> **Why Transform FX Does Not Use Handover:**  
> `TransformFXHandler` is explicitly designed for procedural animation of an actor's own skeleton bones (e.g., driving local/world rotation, translation curves, or Bezier flight trajectories on Spine, Head, or Hand joints). Because reparenting an internal skeleton bone to a foreign character would destroy the character rig's bone hierarchy, Transform FX does not support cross-actor handover. Use **Spawn FX** when passing physical props or held objects between characters.

### Post-Export & Runtime Overrides (`ResolvedHandover`)

To preserve asset purity and avoid mutating ScriptableObjects at runtime, all handover-capable FX handlers maintain a runtime `ResolvedHandover` field:

```csharp
// Evaluated internally during event trigger:
state.ResolvedHandover = (ov != null && ov.OverrideHandover && ov.HandoverOverride != null && ev.Handover != null)
    ? ev.Handover.ApplyOverride(ov.HandoverOverride)
    : ev.Handover;
```

Overrides take effect in the following order of precedence:
1. **Interactive Session Dynamic Overrides** (`session.OverrideHandoverReceiver(...)`): Runtime session-level rerouting.
2. **FX Registry Overrides** (`MSMotionBaseFXOverride.HandoverOverride`): Custom configuration passed via an `MSMotionFXOverrides` asset or builder.
3. **Base Composition Settings** (`ev.Handover`): Authored handover parameters configured in the Composition Editor.

### Handover Transition Modes

| Transition Mode | Runtime Behavior |
| :--- | :--- |
| `Instant` | Object snaps immediately from the source actor's socket to the receiver's socket at `HandoverTime`. |
| `SmoothInterpolation` | Smoothly spherical-linearly interpolates (lerp/slerp) world position and rotation between the two sockets over `TransitionDuration`. |
| `FollowTrajectory` | Drives the object along an authored Bezier spline trajectory toward the receiver socket before snapping and parenting. |

When `RetainOnEnd` is set to `true`, the object remains permanently parented to the receiver character when the interaction ends, preserving weapon disarms and prop exchanges into subsequent gameplay.

---

## Backward Compatibility Guarantee

All existing single-character compositions and animations automatically map to **Actor 0 (Default)** with zero migration steps required. Existing single-character runtime methods (`animator.Play(config)`) remain 100% compatible.

