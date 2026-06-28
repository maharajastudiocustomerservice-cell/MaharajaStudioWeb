# FX & Event System

MSMotion includes a robust, frame-accurate runtime FX execution engine managed by the `MSMotionFXPlayer` component. This system schedules, pools, and blends audio clips, particle bursts, visual effect graphs, camera shakes, procedural transform adjustments, and custom game logic callbacks in sync with character animation frames.

---

## Dispatch Mechanisms

The FX Player supports two high-performance execution modes, which are mutually exclusive and transition automatically:

### 1. Animation Event Mode (OnFXTrigger)
For standalone or legacy projects, the exported `.anim` clip embeds exactly **one** `AnimationEvent` per FX node at its designated trigger timestamp. 
*   This event calls `OnFXTrigger(string eventId)`.
*   The player performs a fast dictionary lookup on the active manifest and immediately fires the matching effect. This minimizes overhead, avoiding per-frame timeline scrubbing or update-loop polling.

### 2. Driver Mode (TickByDriver)
When an `MSMotionFXPlayer` resides alongside an `MSMotionAnimator`, the animator binds the player into **Driver Mode**.
*   The playback dispatcher completely ignores `OnFXTrigger` animation events.
*   Instead, the `MSMotionAnimator` calls `TickByDriver(layer, compositionTime)` every `LateUpdate` frame.
*   This gives the engine precise sub-frame scrubbing capability and ensures that effects stay in sync with custom crossfades, pauses, speed alterations, and playback directions.

---

## The Three-Level Priority Override System

MSMotion utilizes an override structure designed to allow artists and programmers to swap assets (e.g., footstep sounds on sand vs. concrete) without needing to re-author or re-export animation clips:

```
+---------------------------------------------+
|  3. Runtime Overrides (Highest Priority)    | -> Set via SetRuntimeOverride() in C#
+---------------------------------------------+
                       |
+---------------------------------------------+
|  2. Global Registry Overrides               | -> Assigned via MSMotionFXRegistry asset
+---------------------------------------------+
                       |
+---------------------------------------------+
|  1. Manifest Defaults (Lowest Priority)      | -> Authored in the visual timeline editor
+---------------------------------------------+
```

1.  **Manifest Defaults**: The fallback assets and timing configurations baked into the exported `MSMotionFXManifest`.
2.  **Global Registry Overrides**: An `MSMotionFXRegistry` ScriptableObject mapping stable `EventId` keys to customized assets. If an entry is found, it overrides the manifest default.
3.  **Runtime Overrides**: Dynamic override containers (`MSMotionAudioFXOverride`, etc.) set programmatically via C# on a specific character instance. These take absolute priority and never modify assets on disk.

---

## Detailed FX Event Reference

All events inherit from the base `MSMotionFXEvent` class, which declares:
*   `EventId` (string): Stable GUID mapping the event to registry overrides.
*   `TriggerTime` / `Duration` (float): Absolute timings in seconds.
*   `Loop` (bool): Whether the effect loops for the duration.
*   `BlendIn` / `BlendOut` (float): Volume/emission fade durations.
*   `TargetBone` (string) / `TargetHumanBone` (HumanBodyBones): Binding socket.
*   `TransformSpace` (FXTransformSpace): `FollowTarget` or `FixedAtSpawnLocation`.

### 1. AudioFXEvent
Plays an `AudioClip` at the target bone.
*   `Clip` (AudioClip): The audio clip asset.
*   `Volume` / `Pitch` (float): Base parameters.
*   `PitchVariance` (float): Adds random pitch variations per play: `Pitch +/- Random(-Variance, +Variance)`.
*   `SpatialBlend` (float): `0` = 2D (stereo UI/music), `1` = 3D (world-space spatial).
*   `MinDistance` / `MaxDistance` (float): 3D roll-off bounds.
*   `VolumeTransitionInCurve` / `VolumeTransitionOutCurve` (AnimationCurve): Volume ramps.

### 2. ParticleFXEvent
Spawns a legacy Particle System prefab.
*   `Prefab` (GameObject): Prefab to instantiate.
*   `PlayMode` (ParticlePlayMode): `OneShot` (single burst), `Sustained` (loops over duration), or `ManualEmit` (triggers `Emit(EmitCount)`).
*   `EmitCount` (int): Number of manual particles to emit.
*   `ScaleMultiplier` (float): Uniform local scale adjustment.
*   `AttachToBone` (bool): Parent the instance under the target bone.
*   `WaitForCompletion` (bool): Restores the instance to the pool only after all particles have decayed.

### 3. VFXGraphFXEvent
Spawns a Visual Effect Graph asset.
*   `VFXAsset` (VisualEffectAsset): The graph to run.
*   `ParameterOverrides` (List<VFXParameterOverride>): Unions of types (float, int, bool, Vector4, Texture, Mesh) mapped to exposed graph parameters.
*   `StopAtDurationEnd` (bool): Sends a "Stop" event to the graph at the end of the duration.
*   `TransitionPropertyName` (string): Exposed property name (e.g. `SpawnRate`) scaled by the event weight transitions.

### 4. CameraShakeFXEvent
Triggers a Cinemachine impulse shake.
*   `ImpulseSourcePrefab` (GameObject): Cinemachine impulse source component host.
*   `Amplitude` / `Frequency` (float): Intensity and speed multipliers.
*   `ImpulseDirection` (Vector3): Force vector direction.
*   `UseCharacterForward` (bool): Rotates the direction relative to the character's facing direction.
*   `PropagationRadius` (float): Distance limit for cameras to feel the impulse.

### 5. SpawnFXEvent
Instantiates a generic GameObject prefab.
*   `Prefab` (GameObject): Prefab to spawn.
*   `DestroyOnEnd` (bool): If true, destroys (or returns to pool) the instance when the event duration expires.
*   `UsePool` (bool): Uses `MSMotionFXPool` to prevent instantiation garbage collection.
*   `AttachToBone` (bool): Parent the spawned object to the target socket.

### 6. TransformFXEvent
Drives bone or target transform offsets over time.
*   `Mode` (TransformFXMode): `Snap` (immediate), `Lerp` (linear blend), `SmoothStep` (slow-fast-slow), or `Curve` (evaluates custom animation curves).
*   `DrivePosition` / `DriveRotation` / `DriveScale` (bool): Property switches.
*   `TargetLocalPosition` / `TargetLocalEuler` / `TargetLocalScale` (Vector3): Goal properties.
*   `PreservePreviousTransform` (bool): Blends smoothly starting from the bone's pre-event transform instead of cutting.

### 7. ScriptFXEvent
Triggers developer-defined logic callbacks.
*   `ScriptEventTag` (string): Identifier passed to listeners (e.g., `FootstepRight`, `ApplyDamage`).
*   `ContextTargetMode` (FXOverrideTargetMode): Target resolution (`Root`, `NodeTargetBone`, `SpawnedObject`).
*   `Parameters` (List<ScriptFXParameter>): Key-value pairs containing floats, strings, ints, colors, and asset references.
*   `UseSendMessage` (bool): Automatically executes `GameObject.SendMessage` on the target.
*   `SendMessageMethod` (string): The script method name to invoke.

---

## Spline Trajectory System

Both `ParticleFXEvent` and `VFXGraphFXEvent` support **Bezier Trajectories** (`FXTrajectoryData`). When enabled, the FX Player hands evaluation to `FXTrajectoryEvaluator` to move the effect along a bezier spline path over its active duration:

*   **Coordinate Space**: Can evaluate in `AbsoluteWorld` space or `RelativeToAnchor` (relative to the target bone at the moment of spawning).
*   **Align to Path**: If true, rotates the spawned object to face the forward tangent of the path (useful for projectiles or trailing vfx).
*   **Easing Curve**: An `AnimationCurve` remapping time `[0,1]` to accelerate, decelerate, or loop travel along the spline.

---

## Global Script Event Bus

When a `ScriptFXEvent` is fired, it triggers the player's local `OnScriptEvent` event. If a global `MSMotionScriptEventBus` asset is assigned to the active `MSMotionFXRegistry`, the player also forwards the event globally:

```csharp
using UnityEngine;
using MaharajaStudio.MSMotion.Runtime;

public class GameSoundManager : MonoBehaviour
{
    // Assign the same ScriptEventBus asset here as in your FXRegistry
    [SerializeField] private MSMotionScriptEventBus _globalEventBus;

    private void OnEnable()
    {
        _globalEventBus.OnEvent += HandleGlobalFXEvent;
    }

    private void OnDisable()
    {
        _globalEventBus.OnEvent -= HandleGlobalFXEvent;
    }

    private void HandleGlobalFXEvent(ScriptFXEvent ev)
    {
        if (ev.ScriptEventTag == "Footstep")
        {
            string material = ev.GetString("Material", "Grass");
            Vector3 worldPos = ev.ContextTarget != null ? ev.ContextTarget.transform.position : Vector3.zero;
            
            PlayFootstepSFX(material, worldPos);
        }
    }

    private void PlayFootstepSFX(string material, Vector3 position)
    {
        // Integration code...
        Debug.Log($"Playing footstep sound for: {material} at {position}");
    }
}
```

---

## FX Overrides in Detail

To support highly dynamic environments and gameplay states, MSMotion exposes detailed overrides at both design-time (Registry level) and runtime (C# container level).

### 1. Asset-Based Overrides (MSMotionBaseFXOverride)
Exposed in the `MSMotionFXRegistry` ScriptableObject. Each override class corresponds to an event type and contains a series of boolean switches (`OverrideX`) and override value fields. At trigger time, the player evaluates these overrides:

*   **MSMotionAudioFXOverride**: `OverrideClip` (AudioClip), `OverrideVolume` (float), `OverridePitch` (float), `OverrideSpatialBlend` (float), `OverrideMinDistance` (float), `OverrideMaxDistance` (float), `OverrideStereoPan` (float), `OverrideLoop` (bool).
*   **MSMotionParticleFXOverride**: `OverridePrefab` (GameObject), `OverrideScaleMultiplier` (float), `OverridePlayMode` (ParticlePlayMode), `OverrideEmitCount` (int), `OverrideAttachToBone` (bool), `OverrideWaitForCompletion` (bool).
*   **MSMotionVFXGraphFXOverride**: `OverrideAsset` (VisualEffectAsset), `OverrideStopAtDurationEnd` (bool), `OverrideAttachToBone` (bool).
*   **MSMotionTransformFXOverride**: `OverridePrefab` (GameObject), `OverrideMode` (TransformFXMode), `OverrideDrivePosition` (bool), `OverrideTargetLocalPosition` (Vector3), `OverrideDriveRotation` (bool), `OverrideTargetLocalEuler` (Vector3), `OverrideDriveScale` (bool), `OverrideTargetLocalScale` (Vector3).
*   **MSMotionScriptFXOverride**: `OverrideMethodName` (string), `OverrideContextTargetMode` (FXOverrideTargetMode), `OverrideCustomContextBoneName` (string), `OverrideCustomContextHumanBone` (HumanBodyBones), `OverrideUseSendMessage` (bool).
*   **MSMotionCameraShakeFXOverride**: `OverrideImpulseSourcePrefab` (GameObject), `OverrideAmplitude` (float), `OverrideFrequency` (float), `OverrideImpulseDirection` (Vector3), `OverrideUseCharacterForward` (bool).
*   **MSMotionSpawnFXOverride**: `OverridePrefab` (GameObject), `OverrideDestroyOnEnd` (bool), `OverrideUsePool` (bool), `OverrideAttachToBone` (bool).

---

### 2. Runtime Overrides (MSMotionBaseFXOverride)
For high-performance, dynamic overrides at runtime, subclass one of the `MSMotionBaseFXOverride` classes. These act as value containers that bypass Registry searches. Assign them using `MSMotionFXPlayer.SetRuntimeOverride(overrideContainer)`.

#### Common Base Fields
All runtime override containers inherit from `MSMotionBaseFXOverride` and expose the following overrides:
*   `string EventId` (Matches the authoring key)
*   `bool OverrideDuration` / `float Duration`
*   `bool OverrideLoop` / `bool Loop`
*   `bool OverrideBlendIn` / `float BlendIn`
*   `bool OverrideBlendOut` / `float BlendOut`
*   `bool OverrideTransformSpace` / `FXTransformSpace TransformSpace`
*   `bool OverrideTargetBone` / `string TargetBone`
*   `bool OverrideTargetHumanBone` / `HumanBodyBones TargetHumanBone`
*   `bool OverrideLocalPosition` / `Vector3 LocalPosition`
*   `bool OverrideLocalRotationEuler` / `Vector3 LocalRotationEuler`
*   `bool OverrideLocalScale` / `Vector3 LocalScale`
*   `List<FXPropertyOverrideDelta> PropertyDeltas` (Allows granular overriding of specific dynamically targeted properties, methods, or fields defined in the original event)

#### Specialized Classes & Fields
*   **MSMotionAudioFXOverride**: `OverrideClip` (AudioClip), `OverrideVolume` (float), `OverridePitch` (float), `OverrideSpatialBlend` (float), `OverrideMinDistance` (float), `OverrideMaxDistance` (float), `OverrideStereoPan` (float).
*   **MSMotionParticleFXOverride**: `OverridePrefab` (GameObject), `OverrideScaleMultiplier` (float), `OverridePlayMode` (ParticlePlayMode), `OverrideEmitCount` (int), `OverrideAttachToBone` (bool), `OverrideWaitForCompletion` (bool).
*   **MSMotionVFXGraphFXOverride**: `OverrideAsset` (VisualEffectAsset), `OverrideStopAtDurationEnd` (bool), `OverrideAttachToBone` (bool).
*   **MSMotionTransformFXOverride**: `OverridePrefab` (GameObject), `OverrideMode` (TransformFXMode), `OverrideDrivePosition` (bool), `OverrideTargetLocalPosition` (Vector3), `OverrideDriveRotation` (bool), `OverrideTargetLocalEuler` (Vector3), `OverrideDriveScale` (bool), `OverrideTargetLocalScale` (Vector3).
*   **MSMotionScriptFXOverride**: `OverrideMethodName` (string), `OverrideContextTargetMode` (FXOverrideTargetMode), `OverrideCustomContextBoneName` (string), `OverrideCustomContextHumanBone` (HumanBodyBones), `OverrideUseSendMessage` (bool).
*   **MSMotionCameraShakeFXOverride**: `OverrideImpulseSourcePrefab` (GameObject), `OverrideAmplitude` (float), `OverrideFrequency` (float), `OverrideImpulseDirection` (Vector3), `OverrideUseCharacterForward` (bool).
*   **MSMotionSpawnFXOverride**: `OverridePrefab` (GameObject), `OverrideDestroyOnEnd` (bool), `OverrideUsePool` (bool), `OverrideAttachToBone` (bool).

#### Programmatic Override Example

```csharp
using UnityEngine;
using MaharajaStudio.MSMotion.Runtime;

public class DynamicEnvironmentFX : MonoBehaviour
{
    [SerializeField] private MSMotionFXPlayer _fxPlayer;
    [SerializeField] private AudioClip _underwaterFootstepAudio;

    public void EnterWaterVolume()
    {
        // Smoothly adjust all footstep SFX to play an underwater clip at a lower pitch
        var footstepOverride = new MSMotionAudioFXOverride
        {
            EventId = "Footstep_SFX",
            
            // Override base properties
            OverrideBlendOut = true,
            BlendOut = 0.5f, // longer fade-out in water

            // Override audio properties
            OverrideClip = true,
            Clip = _underwaterFootstepAudio,
            OverrideVolume = true,
            Volume = 0.8f,
            OverridePitch = true,
            Pitch = 0.7f, // deep, muffled sound
            
            // Override dynamic property (e.g., if the original event modifies a ReverbFilter's dryLevel)
            PropertyDeltas = new System.Collections.Generic.List<FXPropertyOverrideDelta>
            {
                new FXPropertyOverrideDelta
                {
                    TargetComponentTypeName = "AudioReverbFilter",
                    TargetPropertyName = "dryLevel",
                    OverrideSerializedValue = true,
                    SerializedValue = "-2000" // Lower dry level in water
                }
            }
        };

        _fxPlayer.SetRuntimeOverride(footstepOverride);
    }

    public void ExitWaterVolume()
    {
        _fxPlayer.ClearRuntimeOverride("Footstep_SFX");
    }
}
```

---

## Speed Compensation & Speed Tracking

When a character's animation is slowed down (for example, in bullet-time or slow-motion), sustained effects like audio loops or particle emissions must adjust their lifetimes to match.

The FX Player supports two timing compensation modes:
1.  **Automatic speed tracking**: Call `_fxPlayer.SetAnimatorSpeedTracking(true)`. The component automatically reads the standard `Animator.speed` scale each LateUpdate and scales internal delta times accordingly.
2.  **Manual speed setting**: Call `_fxPlayer.SetPlaybackSpeed(float speed)`. Useful if you want the visual effects to run at a different speed than the skeletal animation.

---

## MSMotionFXPlayer API Reference

`MaharajaStudio.MSMotion.Runtime.MSMotionFXPlayer` : `MonoBehaviour`

The runtime manager component that instantiates and schedules audio, visual, and script effects. Must reside on the same GameObject as the Unity `Animator`.

### Events

*   `public event Action<ScriptFXEvent> OnScriptEvent;`
    *   Fired whenever a `ScriptFXEvent` is triggered on any active animation layer. Use this to bind gameplay logic handlers.

### Dispatching & Controls

*   `public void SwitchManifest(MSMotionFXManifest manifest);`
    *   Switches the active default manifest. Stops all currently active sustained effects from the previous manifest and resets evaluation markers.
*   `public void PauseFX();`
    *   Suspends the dispatching of *new* FX events. Currently active sustained effects continue playing.
*   `public void ResumeFX();`
    *   Resumes scheduling and triggering new events.
*   `public void PauseActiveFX();`
    *   Pauses playback of all currently active sustained effects (pauses audio sources, visual effect graphs, and halts particle systems).
*   `public void ResumeActiveFX();`
    *   Resumes playback of all paused active sustained effects.
*   `public void StopAllFX();`
    *   Immediately terminates all active sustained effects, destroys temporary spawned objects, and returns pooled emitters/audio sources back to the `MSMotionFXPool`.

### Active Status & Query API

*   `public bool IsFXPlaying(string eventId);`
    *   Returns true if any active sustained effect matching the specified `eventId` is currently playing.
*   `public int GetActiveFXCount();`
    *   Returns the total count of all active sustained effects currently playing on the character.
*   `public int GetActiveFXCount(string eventId);`
    *   Returns the count of active sustained effects specifically matching the given `eventId`.
*   `public void StopFX(string eventId);`
    *   Immediately halts all active sustained effects matching the specified `eventId`.
*   `public AudioSource GetActiveAudioSource(string eventId);`
    *   Retrieves the active `AudioSource` instance for the given event ID, or null if not playing.
*   `public ParticleSystem GetActiveParticleSystem(string eventId);`
    *   Retrieves the active `ParticleSystem` instance for the given event ID, or null if not playing.
*   `public UnityEngine.VFX.VisualEffect GetActiveVFX(string eventId);`
    *   Retrieves the active `VisualEffect` component for the given event ID (if VFX Graph is supported), or null if not playing.
*   `public Transform GetSpawnedObjectTransform(string eventId);`
    *   Retrieves the `Transform` of an active spawned object (VFX Graph, Particle, or spawned Prefab) matching the `eventId`. Useful for look-at targets or physical attachments.
*   `public GameObject GetSpawnedGameObject(string eventId);`
    *   Retrieves the exact spawned `GameObject` matching the `eventId`. Only applies to SpawnFX.
*   `public float GetFXElapsedTime(string eventId);`
    *   Returns the elapsed composition time in seconds for a specific sustained FX.
*   `public float GetFXRemainingTime(string eventId);`
    *   Returns the remaining time in seconds before a specific sustained FX automatically ends.
*   `public float GetLayerSpeed(int layerIndex);`
    *   Returns the exact playback speed configured for the specified layer (useful for custom speed synchronization).
*   `public void RebindBones();`
    *   Clears the internal cached bone lookups and layer avatar mask checks. Call this if the character's skeletal hierarchy is structurally modified at runtime.

### Playback Speed controls

*   `public void SetPlaybackSpeed(float speed);`
    *   Sets a manual speed scale multiplier applied to all sustained FX delta calculations. Disables automatic Animator speed tracking.
*   `public void SetAnimatorSpeedTracking(bool enable);`
    *   If true, the FX player automatically polls `Animator.speed` every frame and compensates sustained transitions, loops, and particle speeds accordingly.
*   `public float GetPlaybackSpeed();`
    *   Returns the current active speed multiplier applied to sustained effects.

### Runtime Overrides API

You can apply runtime overrides globally (for the entire lifetime of the `MSMotionFXPlayer`), or transiently (scoped specifically to the playback of a single animation).

#### 1. Transient Playback Overrides (Recommended)
You can pass custom overrides directly into the Animator's playback methods. These overrides will apply exclusively to the exact animation triggered, and will **automatically be cleared** when the animation finishes or is interrupted. This is the safest and cleanest way to alter FX without mutating your `ScriptableObject` configurations.

```csharp
// Example: Play an animation but override its Footstep sound
var footstepOverride = new MSMotionAudioFXOverride {
    EventId = "Footstep", OverrideClip = true, Clip = waterStepClip 
};
_animator.Play(attackConfig, transientRuntimeOverrides: new[] { footstepOverride });
```

#### 2. Global Programmatic Overrides
If you want an override to persist across *multiple* different animations (e.g., a permanent "low health" filter), use the `MSMotionFXPlayer` methods directly:

*   `public void SetRuntimeOverride(MSMotionBaseFXOverride runtimeOverride);`
    *   Applies a dynamic, instance-specific runtime override container. This takes immediate precedence over global registries and manifest settings without mutating disk assets.
*   `public MSMotionBaseFXOverride GetRuntimeOverride(string eventId);`
    *   Retrieves the active runtime override container matching the `eventId`, if one is set.
*   `public void ClearRuntimeOverride(string eventId);`
    *   Removes the runtime override container for the specified event ID.
*   `public void ClearAllOverrides();`
    *   Removes all per-instance runtime overrides.

#### Override Priority Hierarchy
Because there are multiple ways to override FX events, MSMotion evaluates them in a strict top-down priority. The first override found in this list completely replaces all lower levels:

1. **Transient Runtime Override:** (`MSMotionBaseFXOverride` passed into `Play()`) - Highest priority, scopes to exact playback instance.
2. **Global Runtime Override:** (Set via `FXPlayer.SetRuntimeOverride()`) - Applies to all animations until manually cleared.
3. **Transient Registry:** (`MSMotionFXRegistry` passed into `Play()`)
4. **Config Registry:** (`FXRegistryOverride` baked into the `MSMotionAnimationConfig` ScriptableObject)
5. **Global Registry:** (The `MSMotionFXRegistry` assigned directly to the `MSMotionFXPlayer` Inspector).
6. **Manifest Default:** (The base values authored in the Animation Window) - Lowest priority.

> **Next Guide**: Learn how to apply dynamic skeletal constraints in the [Rigging & IK System](rigging-and-ik-system.md).
