# Stretch & Scale System

MSMotion includes a high-performance procedural scaling solver managed by the `MSMotionStretchApplicator` component. It applies Squash & Stretch scale transformations directly to skeletal bone transforms at runtime based on curves baked into animation metadata.

---

## Standalone vs. Driver Execution Modes

The applicator adapts automatically to your character's setup, running in one of two modes:

### 1. Standalone (Vanilla) Mode
If no `MSMotionAnimator` is present on the GameObject, the applicator runs in standalone mode:
*   Every frame, it polls `Animator.GetCurrentAnimatorClipInfo(0)` to detect active animation clips.
*   Upon clip change, it searches for an embedded `MSMotionClipMetadata` sub-asset.
*   If metadata is found, the applicator evaluates scale curves and applies them to matching bones in sync with the state's normalized playback time.

### 2. Driver Mode
When bound to an `MSMotionAnimator` driver component, the applicator bypasses Animator polling:
*   The animator actively updates the applicator via `UpdateLayerState(layer, metadata, weight, normalizedTime, isAdditive, mask)`.
*   The applicator blends scale curves across **multiple layers** simultaneously, respecting active layer weights, additive blending modes, and isolated bone `AvatarMask` boundaries.

---

## Cross-Layer Scale Suppression

To maintain visual consistency during multi-layer blending (for example, blending a throwing animation on top of a running animation), lower-layer scale curves must not distort bone segments actively driven by higher-priority actions.

If `_enableCrossLayerSuppression` is enabled:
*   The applicator evaluates bones layer-by-layer in ascending order.
*   If a higher layer is active, non-additive, and its `AvatarMask` includes a bone that is also targeted by a lower layer's stretch chain, the lower layer's scale curve weight is dynamically suppressed by the higher layer's weight:
    $$\text{Effective Weight} = \text{Layer Weight} \times (1 - \text{Higher Layer Weight})$$
*   This prevents conflicts between overlapping stretch systems.

---

## Level-of-Detail (LOD) & Distance Culling

Procedurally modifying bone scales every frame across dozens of characters can quickly exhaust CPU resources. To prevent this, `MSMotionStretchApplicator` implements a distance-based Level-of-Detail (LOD) optimization system that dynamically adjusts evaluation intervals:

```
[Camera] ===== Near =====> [ Near LOD: Tick Every Frame ]
         ===== Mid ======> [ Mid LOD: Tick Every N Frames ]
         ===== Far ======> [ Far LOD: Capped / Restored Bind Scale ]
```

### LOD States & Intervals

The applicator measures the distance between the character's transform and the main camera (`Camera.main`), selecting one of three evaluation intervals:

| LOD Zone | Distance Condition | Evaluation Interval | Behavior |
| :--- | :--- | :--- | :--- |
| **Near Zone** | $\text{Distance} \leq \text{Near Threshold}$ | Every frame (`Interval = 1`) | Full-frequency evaluation for close-up animations. |
| **Mid Zone** | $\text{Near Threshold} < \text{Distance} \leq \text{Far Threshold}$ | Every $N$ frames (`Interval = MidInterval`) | Evaluates scale curves every $N$ frames (e.g., every 2nd or 3rd frame), skipping updates in-between to reduce CPU overhead. |
| **Far Zone** | $\text{Distance} > \text{Far Threshold}$ | Disabled (`Interval = 0`) | Evaluation is completely suspended. Bones are instantly restored to their default bind-pose scales (`localScale = Vector3.one`) to eliminate culling artifacts. |

---

## MSMotionStretchApplicator API Reference

`MaharajaStudio.MSMotion.Runtime.MSMotionStretchApplicator` : `MonoBehaviour`

### Methods

#### PauseStretch
```csharp
public void PauseStretch();
```
Freezes real-time scale calculations, locking current bone scales in place.

#### ResumeStretch
```csharp
public void ResumeStretch();
```
Resumes dynamic scale curve evaluations.

#### ClearVanillaStretch
```csharp
public void ClearVanillaStretch();
```
Instantly restores all affected bones to their original bind-pose local scales when running in Standalone (Vanilla) mode.

#### SetLODSettings
```csharp
public void SetLODSettings(float nearDistance, float farDistance, int midLODInterval);
```
Configures LOD thresholds and frame-skipping intervals at runtime.

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `nearDistance` | `float` | Distance threshold for full-frequency updates (every frame). |
| `farDistance` | `float` | Distance threshold beyond which stretch application is disabled. |
| `midLODInterval` | `int` | Number of frames to skip during mid-distance updates (e.g. `2` = evaluate every other frame). |

#### GetCurrentLODInterval
```csharp
public int GetCurrentLODInterval();
```
Returns the currently active LOD update interval (e.g. `1` for every frame, `2` for every second frame, `0` for disabled/culled).

#### SetCrossLayerSuppression
```csharp
public void SetCrossLayerSuppression(bool enable);
```
Toggles whether higher-layer Avatar Masks dynamically suppress lower-layer bone scale curves.

#### GetActiveStretchLayerCount
```csharp
public int GetActiveStretchLayerCount();
```
Returns the number of layers actively contributing to stretch calculations (always returns `0` in Standalone mode).

#### SetMetadata
```csharp
public void SetMetadata(MSMotionClipMetadata metadata);
```
Manually assigns a metadata asset. Only applicable when running in Standalone (Vanilla) mode.

---

## LOD Configuration C# Example

This example demonstrates how to adjust culling thresholds dynamically based on graphics quality settings:

```csharp
using UnityEngine;
using MaharajaStudio.MSMotion.Runtime;

public class PerformanceManager : MonoBehaviour
{
    [SerializeField] private MSMotionStretchApplicator[] _applicators;

    public void ApplyGraphicsSettings(bool highPerformanceMode)
    {
        foreach (var applicator in _applicators)
        {
            if (highPerformanceMode)
            {
                // Strict performance: cull early, skip frames frequently in mid-range
                applicator.SetLODSettings(5f, 25f, 4);
            }
            else
            {
                // High visual quality: extend full-rate evaluation distance
                applicator.SetLODSettings(15f, 60f, 2);
            }
        }
        
        Debug.Log($"[Performance] Adjusted {_applicators.Length} stretch applicators.");
    }
}
```

> **Next Guide**: Review overall performance design, garbage collection mitigation, and best practices in [Optimization & Best Practices](optimization-and-best-practices.md).
