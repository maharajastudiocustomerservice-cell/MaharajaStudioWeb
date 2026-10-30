# [RevealOnHover]

> Fades an inspector field to a reduced opacity until the mouse cursor hovers over it, minimizing visual clutter in data-dense components.

---

## 1. Overview & Value Proposition

**What it does:**
`[RevealOnHover]` keeps secondary, advanced, or auxiliary inspector fields at low opacity (`HiddenOpacity`) until the user hovers their mouse cursor over the control. Upon mouse entry, the field smoothly transitions to full opacity over `RevealDuration` milliseconds.

**The Problem:**
Extensive game entities often feature dozens of niche debug settings, technical tuning variables, and secondary overrides. When all fields are displayed at full prominence, inspectors become overwhelming and tedious to navigate.

**The Solution:**
Decorating secondary fields with `[RevealOnHover]`:
- **Reduces Cognitive Load:** Dimmed fields subtly fade into the background, allowing primary gameplay variables to stand out.
- **Fluid Transition Curves:** Smooth fade-in and fade-out animations provide a sleek, polished AAA interface experience.
- **Configurable Ghost Tinting:** Adjust the dormant opacity level (`HiddenOpacity`) or apply a custom resting tint (`HiddenColor`).
- **Interactive Accessibility:** The field remains fully interactive even when dimmed; hovering immediately restores full visual prominence.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class PlayerMovement : MonoBehaviour
{
    public float moveSpeed = 6.5f;

    [RevealOnHover(HiddenOpacity = 0.25f, RevealDuration = 200f)]
    public float internalSubstepTickInterval = 0.016f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public RevealOnHoverAttribute()
```

*Initializes a hover reveal effect with 20% resting opacity and smooth 300ms fade duration. Customize transitions via object initializers.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `HiddenOpacity` | `float` | `0.2f` | Resting opacity of the field when the mouse is not hovering (range `0.0` to `1.0`). |
| `RevealDuration` | `float` | `300f` | Transition duration in milliseconds when fading into full opacity on mouse enter. |
| `HideDuration` | `float` | `200f` | Transition duration in milliseconds when fading back to dormant opacity on mouse exit. |
| `HiddenColor` | `string` | `""` | Optional hex color tint applied to the field while resting in dimmed state. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class CameraController : MonoBehaviour
{
    [Header("Primary Controls")]
    public float followSpeed = 10f;
    public float lookSensitivity = 2.5f;

    [Header("Advanced Telemetry & Diagnostics")]
    [RevealOnHover(HiddenOpacity = 0.15f, RevealDuration = 150f, HideDuration = 250f)]
    public bool enableJitterDiagnostics = false;

    [RevealOnHover(HiddenOpacity = 0.2f, HiddenColor = "#64748B")]
    public float frustumCullingSafetyBuffer = 0.5f;

    [RevealOnHover(HiddenOpacity = 0.25f)]
    public Vector3 internalMatrixCorrectionOffset = Vector3.zero;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Functions cleanly inside groups; dims individual row elements without fading group header. |
| `[ReadOnly]` | Supported | Compatible with read-only fields for non-intrusive debug telemetries. |
| `[AnimatedHover]` | Stacking | Can be combined with `[AnimatedHover]` scale bumps for pronounced interactive reveal. |
