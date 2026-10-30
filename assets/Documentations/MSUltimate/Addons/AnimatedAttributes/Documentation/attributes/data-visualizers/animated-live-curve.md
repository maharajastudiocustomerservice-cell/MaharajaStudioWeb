# [AnimatedLiveCurve]

> Renders an animated glowing point tracer traveling continuously along an AnimationCurve preview with luminous comet trails.

---

## 1. Overview & Value Proposition

**What it does:**
`[AnimatedLiveCurve]` turns standard Unity `AnimationCurve` fields into an animated live trajectory preview. A luminous point tracer (`TracerColor`) glides continuously along the evaluated curve shape at an adjustable speed (`TracerSpeed`), leaving a glowing decay trail (`TrailLength`) behind it.

**The Problem:**
Designing ease-in/ease-out curves, camera recoil paths, bounce curves, or weapon velocity envelopes in the standard static curve field provides no sense of speed, easing acceleration, or temporal cadence without repeatedly entering Play Mode.

**The Solution:**
Decorating `AnimationCurve` properties with `[AnimatedLiveCurve]`:
- **Real-Time Temporal Preview:** Immediately visualizes where the curve accelerates, slows down, or loops over time.
- **Luminous Particle Tracer:** Renders a glowing point tracer accompanied by a decaying comet tail (`TrailLength`).
- **Fully Preserved Curve Editing:** The built-in Unity AnimationCurve drawer remains fully accessible and interactive right above or alongside the preview.
- **Collection Cascading:** Implements `ICollectionElementAttribute` for multi-stage curve sequences or serialized animation blend profiles.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class CameraShakeProfile : MonoBehaviour
{
    [AnimatedLiveCurve(height: 52f, tracerColor: "#F43F5E")]
    public AnimationCurve traumaDecayCurve = AnimationCurve.EaseInOut(0f, 1f, 1f, 0f);
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `UnityEngine.AnimationCurve` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Collection Element Support** | Yes (`ICollectionElementAttribute`) |

---

## 4. Constructors & Parameters

```csharp
public AnimatedLiveCurveAttribute(float height = 48f, string tracerColor = "#F43F5E")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `height` | `float` | `48f` | Vertical display height in pixels of the live curve preview area. |
| `tracerColor` | `string` | `"#F43F5E"` | Hex color string for the traveling glowing point tracer. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `PreviewHeight` | `float` | `48f` | Height of the curve preview canvas in pixels. |
| `CurveColor` | `string` | `"#38BDF8"` | Hex color string for the evaluated spline curve path. |
| `TracerColor` | `string` | `"#F43F5E"` | Hex color string for the leading point tracer. |
| `TracerSpeed` | `float` | `1.0f` | Speed multiplier controlling how fast the tracer traverses normalized time `0` to `1`. |
| `TrailLength` | `float` | `0.2f` | Normalized length of the luminous fading comet tail behind the tracer. |
| `DrawInputField` | `bool` | `true` | Whether to draw the standard Unity AnimationCurve field above the preview. |
| `ShowInputField` | `bool` | `true` | Alias for `DrawInputField`. |
| `CustomLabel` | `string` | `null` | Optional custom label rendered above the live curve preview. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class WeaponRecoilController : MonoBehaviour
{
    [Header("Recoil Recovery Spline")]
    [AnimatedLiveCurve(
        height: 60f, 
        tracerColor: "#E11D48", 
        CurveColor = "#0284C7", 
        TracerSpeed = 1.4f, 
        TrailLength = 0.25f,
        CustomLabel = "Vertical Recoil Spring"
    )]
    public AnimationCurve verticalKickCurve = new AnimationCurve(
        new Keyframe(0f, 0f),
        new Keyframe(0.1f, 1.2f),
        new Keyframe(0.35f, 0.2f),
        new Keyframe(1.0f, 0.0f)
    );
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Live curve view fits cleanly into weapon tuning or motion tween panels. |
| `[ShowIf]` | Supported | Halts animation scheduling when hidden to prevent unnecessary UI renders. |
| Arrays & Lists | Supported | Implements `ICollectionElementAttribute` for lists of AnimationCurves. |
