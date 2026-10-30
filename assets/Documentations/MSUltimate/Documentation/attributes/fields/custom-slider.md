# [CustomSlider]

> Renders a numeric field with a custom styled slider track, optional numeric field, and dynamic member bounds.

---

## 1. Overview & Value Proposition

**What it does:**
Renders numeric values as stylish, theme-colored sliders with optional number inputs and dynamic member bounds.

**The Problem:**
Standard Unity sliders are visually rigid and grey. When building custom tools, level editors, or branded component dashboards, default sliders look outdated and do not support dynamic runtime bounds derived from other fields or methods.

**The Solution:**
Add `[CustomSlider]` to any numeric field:
- **Custom Accent Coloring:** Tint slider tracks with custom hex colors (e.g. green for health, blue for mana).
- **Dynamic Member Bounds:** Bind `MinMember` and `MaxMember` to properties, fields, or methods.
- **Toggleable Number Input:** Show or hide the companion numeric input field with `ShowField`.
- **Discrete Step Snapping:** Configure stepping increments (e.g. `Step = 5f`) for stepped tuning.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class AudioSettings : MonoBehaviour
{
    [CustomSlider(0f, 1f, colorHex: "#2ecc71")]
    public float masterVolume = 0.8f;

    [CustomSlider(20f, 120f, Step = 5f)]
    public float targetFrameRate = 60f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `float`, `int`, `double`, `long`, `short`, `byte` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public CustomSliderAttribute()
public CustomSliderAttribute(float min, float max)
public CustomSliderAttribute(float min, float max, string colorHex)
public CustomSliderAttribute(string minMember, string maxMember, string colorHex = null)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `min` | `float` | `0f` | Static minimum slider value. |
| `max` | `float` | `100f` | Static maximum slider value. |
| `colorHex` | `string` | `null` | Accent color hex string for the slider track. |
| `minMember` | `string` | `null` | Member name returning dynamic min bound. |
| `maxMember` | `string` | `null` | Member name returning dynamic max bound. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Min` | `float` | `0f` | Static minimum slider bound. |
| `Max` | `float` | `100f` | Static maximum slider bound. |
| `ColorHex` | `string` | `null` | Accent color hex string. |
| `ShowField` | `bool` | `true` | Shows numeric input box next to slider. |
| `Step` | `float` | `0f` | Stepping increment (`0` for continuous). |
| `CustomLabel` | `string` | `null` | Custom display label override. |
| `MinMember` | `string` | `null` | Member name for dynamic minimum bound. |
| `MaxMember` | `string` | `null` | Member name for dynamic maximum bound. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class VehicleEngineTuning : MonoBehaviour
{
    public float peakRpmLimit = 7500f;

    [Header("Engine Throttle")]
    [CustomSlider(0f, 100f, colorHex: "#e74c3c", Step = 1f)]
    public float throttleInput = 25f;

    [Header("Idle & Redline")]
    [CustomSlider("GetIdleRpm", nameof(peakRpmLimit), colorHex: "#f39c12")]
    public float cruiseRpm = 2200f;

    private float GetIdleRpm() => 800f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[CustomRange]` | Alternative | Use `[CustomRange]` for detailed decimal control; use `[CustomSlider]` for theme styling. |
| `[SuffixLabel]` | Supported | Suffix measurement unit docks cleanly to the right. |
| `[BoxGroup]` | Supported | Integrates cleanly inside grouped containers and tabs. |
