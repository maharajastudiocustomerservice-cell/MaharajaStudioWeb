# [HierarchyCurveVisualizer]

> Renders a live mini waveform curve in the hierarchy row for AnimationCurve fields with playhead evaluation.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyCurveVisualizer]` renders an anti-aliased micro-waveform curve graph directly on the hierarchy row for serialized `AnimationCurve` fields. Driven by `HierarchyCurveVisualizerRenderer`, it samples the curve across 16 anti-aliased points, normalizes min/max amplitudes, and paints the wave within a sleek dark container card (`BackgroundColor = "#121A24"`, `BorderColor = "#1E3A50"`). During Play Mode, it can evaluate and plot a live moving playhead dot along the curve (`TrackPlayhead = true`), optionally querying a reflected time field (`PlayheadTimeField`).

**The Problem:**
AnimationCurves govern vital gameplay mechanics (weapon recoil profiles, easing transitions, light falloffs, jump trajectory parabolas, damage curves). Inspecting or comparing curves across different weapon prefabs or character rigs currently requires opening the Inspector and double-clicking each curve into Unity's popup Curve Editor window.

**The Solution:**
Decorating `AnimationCurve` fields with `[HierarchyCurveVisualizer]`:
- **Miniature Curve Waveform:** See the curve's profile (ease-in, ease-out, parabola, s-curve) at a glance in the hierarchy.
- **Live Playhead Tracking:** Watch real-time evaluation dot movement along the waveform during gameplay.
- **Reflected Time Synchronization:** Bind to float time/progress variables via `PlayheadTimeField` to evaluate actual curve playback.
- **Custom Visual Styling:** Customize line color (`LineColor = "#55DDFF"`), container borders, and width.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class JumpController : MonoBehaviour
{
    [HierarchyCurveVisualizer(LineColor = "#38BDF8", Width = 45f)]
    public AnimationCurve jumpTrajectory = AnimationCurve.EaseInOut(0f, 0f, 1f, 1f);
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyCurveVisualizerRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyCurveVisualizerAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Width` | `float` | `42f` | Width of the micro curve graph in pixels. |
| `Height` | `float` | `0f` | Height of the curve graph in pixels, or `0` for row-adjusted height (capped at 14px). |
| `LineColor` | `string` | `"#55DDFF"` | Hex line color of the waveform curve plot. |
| `BackgroundColor` | `string` | `"#121A24"` | Hex background fill color behind the curve. |
| `BorderColor` | `string` | `"#1E3A50"` | Hex border outline color around the graph container. |
| `TrackPlayhead` | `bool` | `true` | Whether to evaluate and render a live playhead dot during Play Mode. |
| `PlayheadTimeField` | `string` | `""` | Optional field name on the component to read live evaluation time from. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the waveform graph remains visible and updates during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class WeaponRecoilRig : MonoBehaviour
{
    [Header("Recoil Curve")]
    [HierarchyCurveVisualizer(
        Width = 50f, 
        LineColor = "#F43F5E", 
        BackgroundColor = "#1E293B", 
        BorderColor = "#475569", 
        TrackPlayhead = true, 
        PlayheadTimeField = nameof(recoilProgress), 
        XOffset = 6f)]
    public AnimationCurve recoilImpulse = AnimationCurve.Linear(0f, 0f, 0.2f, 1f);

    [HideInInspector]
    public float recoilProgress = 0f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchySparkline]`** | Complementary | Use `HierarchyCurveVisualizer` for static evaluation curves, and `HierarchySparkline` for live rolling historical numbers. |
| **`[HierarchyMiniSlider]`** | High | Place mini sliders next to curve graphs to tweak evaluation speed or multipliers directly. |
| **Field Types** | Required | Target field must be an `AnimationCurve`. Safely ignores any other field types. |
| **Anti-Aliasing** | Built-in | Renders smoothed micro-segments within an IMGUI clipped rect for crisp display at high DPIs. |
