# [ComponentMuteSound]

> Mutes all inspector audio feedback effects for the annotated component with an optional visual muted badge indicator.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentMuteSound]` provides acoustic comfort during intensive parameter tuning. Positioned in `ComponentSlot.BodyOverlay`, it intercepts and silences all tactile UI sounds (such as mouseover clicks, slider ticks, and button thuds provided by `ComponentSound` or suite themes) specifically for this component. When enabled, it optionally renders a subtle muted speaker icon badge (`ShowBadge = true`) in the component card to notify developers that audio feedback is suppressed.

**The Problem:**
While tactile acoustic feedback enriches high-level inspector interactions, developers performing rapid numerical iteration—such as scrubbing animation curves, dragging physics values, or continuously adjusting color sliders—can find repetitive sound effects jarring and fatigue-inducing during prolonged editing sessions.

**The Solution:**
Applying `[ComponentMuteSound]` to rapid-iteration components:
- **Targeted Acoustic Silencing:** Silences UI sounds for a single component without disabling audio feedback across the entire project.
- **Visual Mute Indicator:** A clean speaker badge (`🔇`) confirms that sensory audio triggers are muted by design.
- **Combats Developer Fatigue:** Keeps the editor whisper-quiet during long balance passes that involve hundreds of slider adjustments.
- **Zero Configuration Boilerplate:** A single attribute call on the class declaration instantly silences all child interactions.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentMuteSound(showBadge: true)]
public class RapidSliderTuner : MonoBehaviour
{
    [Range(0f, 100f)] public float blendWeightA = 50f;
    [Range(0f, 100f)] public float blendWeightB = 50f;
    [Range(0.01f, 10f)] public float cycleFrequency = 1.25f;
    public Color tintColor = Color.white;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ComponentDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Component Slot** | `BodyOverlay` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentMuteSoundAttribute(bool showBadge = true)
```

- `showBadge`: Whether to display a subtle muted speaker badge indicator in the component header or card border.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ShowBadge` | `bool` | `true` | When true, renders a subtle mute icon badge in the inspector. |
| `Order` | `int` | `0` | Sequence sorting order within the target component slot. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#64748B", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#0F172A", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("PROCEDURAL IK CALIBRATION", Subtitle = "High-Frequency Joint Tuning Matrix", BackgroundColor = "#1E293B", TitleColor = "#E2E8F0")]
[ComponentMuteSound(ShowBadge = true)]
public class ProceduralIKJointCalibrator : MonoBehaviour
{
    [Header("Spine Angles & Limits")]
    [Range(-90f, 90f)] public float spinePitchDegrees = 12f;
    [Range(-90f, 90f)] public float spineYawDegrees = 0f;
    [Range(-90f, 90f)] public float spineRollDegrees = 5f;

    [Header("Damping & Springs")]
    [Range(0f, 1f)] public float jointFrictionDamping = 0.45f;
    [Range(10f, 500f)] public float jointSpringStiffness = 180f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentSound]`** | High | Cleanly overrides and mutes sensory sound effects that would otherwise trigger on this component. |
| **`[ComponentHeader]`** | High | Places the mute badge neatly alongside header elements and title tags. |
| **Numeric & Slider Fields** | High | Recommended for components with numerous continuous sliders where repetitive audio ticks become irritating. |
| **Inspector Controls** | High | Zero impact on event propagation; buttons, dropdowns, and text fields continue to operate normally. |
