# Core Animation System

At the center of MSMotion's execution pipeline is the core animation playback system. Driven by Unity's low-level **PlayableGraph API**, this system replaces standard Animator Controllers with code-directed blending, dynamic layer allocation, and strict allocation-free runtime updates.

---

## PlayableGraph Architecture

`MSMotionAnimator` constructs a custom `PlayableGraph` at runtime. The root of this graph is an `AnimationLayerMixerPlayable`. 

*   **Layer 0 (Base Layer)**: Dedicated to locomotion. It can evaluate a standard Unity `RuntimeAnimatorController` or fallback to a default idle clip.
*   **Layer 1+ (Override/Action Layers)**: Created on demand. As you play animations on higher indexes, the graph dynamically grows to accommodate new mixer inputs, ensuring zero overhead for unused layers.

```
       [AnimationPlayableOutput]
                  |
    [AnimationLayerMixerPlayable] (Root)
       /          |          \
   [Layer 0]   [Layer 1]   [Layer 2] ...
    (Locomotion) (Attack)    (Emote)
```

---

## The 2-Input Layer Mixer Pattern

To prevent skeletal popping and zero-transform squashing (where an empty or uninitialized track evaluates transforms to `0,0,0` and crushes the model), MSMotion implements two runtime layer configurations:

### 1. Mixer Mode (Idle Fallback)
If a layer has a default idle clip assigned (via `_defaultIdleClips` in the Inspector), the allocator binds an `AnimationMixerPlayable` sub-mixer to that layer slot. 
*   **Input 0**: The looping default/idle clip.
*   **Input 1**: The active overriding action clip.
*   The root layer weight is kept at `1.0`, and crossfading transitions interpolate the weights inside this sub-mixer (e.g. fading Input 1 from `0` to `1` while fading Input 0 from `1` to `0`).

### 2. Direct Mode (No Idle Fallback)
If no idle clip is declared for a layer, creating a sub-mixer would squash the character when no clip is playing. 
*   Instead, the `AnimationClipPlayable` is connected **directly** to the root `AnimationLayerMixerPlayable`.
*   The root layer's weight starts at `0.0` and is faded up dynamically by `MSMotionAnimator`.

---

## MSMotionAnimator API Reference

`MaharajaStudio.MSMotion.Runtime.MSMotionAnimator` : `MonoBehaviour`

The primary playback driver component. Must reside on the same GameObject as the Unity `Animator`.

### Inspector Configuration Fields

The component properties are configured in the Unity Inspector:
*   `RuntimeAnimatorController _legacyController` (locomotion): Locomotion blend controller assigned to Layer 0.
*   `AnimationClip[] _defaultIdleClips` (per layer): Default clip played on each layer when no animation is active (e.g. index 0 = Layer 0 fallback, index 1 = Layer 1 fallback).
*   `MSMotionFXPlayer _fxPlayer`: References the FX player. Automatically retrieved from the same GameObject if left unassigned.
*   `MSMotionStretchApplicator _stretchApplicator`: References the stretch applicator. Automatically retrieved if left unassigned.
*   `MSMotionRigController _rigController`: References the rig controller. Automatically retrieved if left unassigned.
*   `bool _applyRootMotionDirectly`: If true, MSMotionAnimator applies root motion delta translations and rotations directly to the character's Transform.
*   `bool _applyFootIKOnIdle`: If true, applies Unity's built-in Foot IK to default idle clips.

### Events

*   `public event Action<MSMotionAnimationConfig> OnAnimationStarted;`
    *   Fires when an animation begins playing (at the start of its fade-in).
*   `public event Action<MSMotionAnimationConfig> OnAnimationCompleted;`
    *   Fires when a non-looping animation naturally finishes (after its fade-out completes).
*   `public event Action<MSMotionAnimationConfig> OnAnimationStopped;`
    *   Fires when an animation is explicitly stopped via code.
*   `public event Action<Vector3, Quaternion> OnRootMotionDelta;`
    *   Fires every frame inside `OnAnimatorMove` with the translation vector and rotation delta for the current frame. Use this to manually apply root motion in custom controllers.

### Methods

#### Play
```csharp
public void Play(MSMotionAnimationConfig config);
```
Plays the animation configuration immediately with a hard cut (no fade-in). Any active animation on the same layer is stopped instantly.

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `config` | `MSMotionAnimationConfig` | The data asset defining the clip and parameters. |

#### CrossFade
```csharp
public void CrossFade(MSMotionAnimationConfig config, float fadeOverride = -1f);
```
Smoothly transitions to the new animation configuration.
*   `fadeOverride`: If greater than `0f`, overrides both the fade-in and fade-out durations. If `≤ 0f`, uses the values calculated by the config asset.

#### PlayThenCrossFade
```csharp
public async Awaitable PlayThenCrossFade(MSMotionAnimationConfig current, MSMotionAnimationConfig next);
```
Plays the `current` config, waits for its active duration to reach its fade-out threshold, and then smoothly crossfades into `next`.

#### Stop
```csharp
public void Stop(MSMotionAnimationConfig config);
```
Immediately stops the animation configuration if it is currently active on its layer, snapping the layer weight back to `0` (or returning the layer to idle).

#### StopSmoothly
```csharp
public void StopSmoothly(MSMotionAnimationConfig config);
```
Smoothly fades out the active animation configuration over its configured fade-out duration before stopping it.

#### StopAll
```csharp
public void StopAll();
```
Instantly halts playback across all layers, returning all layers to idle or bind poses, and terminates all active sustained FX.

#### Playback Control Methods
*   `public void Pause(int layer)` / `public void Pause(MSMotionAnimationConfig config)`
    *   Pauses playback on the layer (sets play speed to `0`).
*   `public void Resume(int layer)` / `public void Resume(MSMotionAnimationConfig config)`
    *   Resumes playback, restoring the speed defined in the active config.
*   `public void PauseAll()` / `public void ResumeAll()`
    *   Pauses or resumes all active animation playables.

#### Layer Weight Methods
*   `public void SetLayerWeight(int layer, float weight)`
    *   Instantly sets the root layer mixer weight (clamped `[0,1]`).
*   `public void FadeLayerWeight(int layer, float targetWeight, float duration)`
    *   Asynchronously interpolates the root layer weight to `targetWeight` over `duration` seconds.
*   `public void SetPlaybackSpeed(int layer, float speed)` / `public void SetPlaybackSpeed(MSMotionAnimationConfig config, float speed)`
    *   Overrides the active animation's speed multiplier at runtime.

### Query Methods

*   `public bool IsPlaying(MSMotionAnimationConfig config)`: True if the config is active on its layer.
*   `public bool IsPlaying(int layer)`: True if any action is playing on the layer index.
*   `public float GetNormalizedTime(int layer)`: Returns playback progress `[0, 1]` on the layer.
*   `public float GetNormalizedTime(MSMotionAnimationConfig config)`: Returns playback progress `[0, 1]` of the specific config.
*   `public float GetCurrentTime(int layer)`: Returns the absolute playback head position in seconds.
*   `public MSMotionAnimationConfig GetActiveConfig(int layer)`: Returns the active config asset on the layer.
*   `public float GetActiveWeight(int layer)`: Returns the current layer blend weight.
*   `public int GetAllocatedLayerCount()`: Returns total layers currently allocated in the graph.
*   `public AnimationClip GetCurrentClip(int layer)`: Retrieves the currently active `AnimationClip` on the layer.
*   `public float GetClipLength(int layer)`: Returns active clip length in seconds.
*   `public float GetTimeRemaining(int layer)`: Returns remaining play duration (factors loop iterations).
*   `public float GetPlaybackSpeedMultiplier(int layer)`: Returns the custom speed multiplier currently applied to the layer.
*   `public float GetEffectivePlaybackSpeed(int layer)`: Returns the true real-world playback speed (combining clip base speed, layer multiplier, and global `Animator.speed`).
*   `public bool IsPaused(int layer)`: Returns true if the animation on the given layer is actively paused.
*   `public bool IsFading(int layer)`: Returns true if the layer is currently crossfading or transitioning weights.
*   `public UnityEngine.Playables.Playable GetActivePlayable(int layer)`: Returns the generic active `Playable` struct for advanced graph modifications.
*   `public UnityEngine.Animations.AnimationClipPlayable GetActiveAnimationClipPlayable(int layer)`: Returns the underlying `AnimationClipPlayable` if present.
*   `public UnityEngine.Animations.AnimatorControllerPlayable GetAnimatorControllerPlayable()`: Returns the legacy controller playable running on Layer 0, if assigned.

---

## MSMotionAnimationConfig Reference

`MaharajaStudio.MSMotion.Runtime.MSMotionAnimationConfig` : `ScriptableObject`

Drag-and-drop asset declaring playback settings. Create via: **Assets > Create > Maharaja Studio > MsMotion > Animation Config**.

### Properties & Serialized Fields

| Property | Type | Description |
| :--- | :--- | :--- |
| `Clip` | `AnimationClip` | The native animation clip. *Required.* |
| `Manifest` | `MSMotionFXManifest` | The FX event markers asset generated by the exporter. |
| `Metadata` | `MSMotionClipMetadata` | Baked scale and stretch curve metadata. |
| `Layer` | `int` | Layer index (`0` is base, `1+` are overrides). Default is `1`. |
| `Mask` | `AvatarMask` | Limits the animation to specific bones. *Null = Full Body.* |
| `IsAdditive` | `bool` | Blends additively on top of lower layers. |
| `IsLoop` | `bool` | Loops the animation clip. |
| `ApplyFootIK` | `bool` | Applies Unity's built-in Foot IK to the playable. |
| `ScaleFXWithLayerWeight` | `bool` | Scales volume/emission of spawned FX by the layer weight. |
| `FXWeightMultiplier` | `float` | Additional volume/emission multiplier. Default: `1.0`. |
| `PlaybackSpeed` | `float` | Playback speed multiplier. Default: `1.0`. |
| `FXRegistryOverride` | `MSMotionFXRegistry` | Overrides the global FX registry while this animation plays. |
| `IKOverrides` | `IReadOnlyList<MSMotionIKEntry>` | Dynamic constraint mappings evaluated by `MSMotionRigController`. |
| `ResolvedFadeInTime` | `float` | Computed fade-in time (returns customized time, or defaults to 10% of clip duration clamped to `[0.05, 0.3]` seconds). |
| `ResolvedFadeOutTime` | `float` | Computed fade-out time. |

---

## Custom Sequences & Blending Example

Below is an advanced implementation utilizing custom weighting and sequencing:

```csharp
using UnityEngine;
using MaharajaStudio.MSMotion.Runtime;

public class AdvancedAnimatorController : MonoBehaviour
{
    [SerializeField] private MSMotionAnimator _animator;
    [SerializeField] private MSMotionAnimationConfig _heavyAttack;
    [SerializeField] private MSMotionAnimationConfig _recoveryIdle;

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.Alpha1))
        {
            // Trigger heavy attack and transition to recovery once complete
            _ = PlayCombatChain();
        }
        
        if (Input.GetKeyDown(KeyCode.Alpha2))
        {
            // Dynamically slow down playback speed
            _animator.SetPlaybackSpeed(_heavyAttack, 0.5f);
        }
    }

    private async Awaitable PlayCombatChain()
    {
        Debug.Log("Starting Attack Chain...");
        
        // Play attack and automatically crossfade to recovery
        await _animator.PlayThenCrossFade(_heavyAttack, _recoveryIdle);
        
        Debug.Log("Combat Chain Completed and Returned to Recovery Idle.");
    }
}
```

> **Next Guide**: Learn how to configure and trigger custom event tracks in [FX & Event System](fx-event-system.md).
