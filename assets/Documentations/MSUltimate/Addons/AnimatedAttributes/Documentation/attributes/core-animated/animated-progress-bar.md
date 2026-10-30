# [AnimatedProgressBar]

> Renders a smoothly animating progress fill bar directly underneath a numeric field with interactive scrubbing, dynamic limits, threshold alerts, and text format tokens.

---

## 1. Overview & Value Proposition

**What it does:**
Enhances numeric float and integer fields with a hardware-accelerated animated progress meter. Features smooth tweening transitions upon value changes, click-and-drag mouse scrub editing directly on the bar, dynamic min/max limits linked to class members, custom label formatting tokens, and automatic threshold warning color shifts (e.g. low health alert).

**The Problem:**
Standard numeric inspector fields (or static IMGUI `EditorGUI.ProgressBar`) provide zero tactile feedback, do not support dragging to scrub values, cannot smoothly animate value transitions, and require hardcoded static min/max bounds.

**The Solution:**
Add `[AnimatedProgressBar]` to any numeric field:
- **Smooth Fill Transitions:** Animated tween fills (`AnimationDuration = 300ms`) respond gracefully to changes.
- **Interactive Mouse Scrubbing:** Click or drag directly across the bar to adjust values (`IsEditable = true`).
- **Dynamic Limits:** Bind `MaxValue` to another property (e.g. `[AnimatedProgressBar(nameof(maxHealth))]`).
- **Low Threshold Alarm:** Shifts to warning red (`LowThresholdColor`) when ratio drops below `LowThreshold`.
- **Rich Text Tokens:** Custom label formatting supports `{value}`, `{min}`, `{max}`, and `{percent}` tokens.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class PlayerHealth : MonoBehaviour
{
    [AnimatedProgressBar(0f, 100f, FillColor = "#2ecc71", ShowValue = true, ShowPercentage = true)]
    public float currentHealth = 85f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `float`, `int`, `double`, `long`, `short`, `byte` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public AnimatedProgressBarAttribute()
public AnimatedProgressBarAttribute(float maxValue)
public AnimatedProgressBarAttribute(float minValue, float maxValue)
public AnimatedProgressBarAttribute(string dynamicMaxValueMember)
public AnimatedProgressBarAttribute(string dynamicMinValueMember, string dynamicMaxValueMember)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `minValue` | `float` | `0f` | Static minimum boundary limit. |
| `maxValue` | `float` | `100f` | Static maximum boundary limit. |
| `dynamicMaxValueMember` | `string` | `null` | Name of field or property supplying dynamic max value. |
| `dynamicMinValueMember` | `string` | `null` | Name of field or property supplying dynamic min value. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MinValue` | `float` | `0f` | Minimum value represented by the progress bar. |
| `MaxValue` | `float` | `100f` | Maximum value represented by the progress bar. |
| `DynamicMaxValueMember` | `string` | `null` | Name of a member providing a dynamic maximum value. |
| `DynamicMinValueMember` | `string` | `null` | Name of a member providing a dynamic minimum value. |
| `FillColor` | `string` | `"#589DF6"` | Hex color string for the progress fill bar. |
| `BackgroundColor` | `string` | `"#222222"` | Hex color string for the progress bar background track. |
| `BarHeight` | `float` | `8f` | Height of the progress bar in pixels. |
| `AnimationDuration` | `float` | `300f` | Duration in milliseconds for the bar fill transition. |
| `DrawInputField` | `bool` | `true` | Whether to draw standard numeric input box above the bar. |
| `IsEditable` | `bool` | `true` | Whether the progress bar can be edited by dragging on the bar. |
| `CustomLabel` | `string` | `null` | Custom text label overlaid on the progress bar. |
| `ShowValue` | `bool` | `false` | Displays numeric current value in label. |
| `ShowPercentage` | `bool` | `false` | Displays percentage in label. |
| `LabelFormat` | `string` | `null` | Format string tokens: `{label}`, `{value}`, `{min}`, `{max}`, `{percent}`. |
| `LabelColor` | `string` | `"#FFFFFF"` | Hex color of the overlaid label text. |
| `LabelFontSize` | `int` | `10` | Font size of overlaid label text. |
| `LowThreshold` | `float` | `-1f` | Ratio (0–1) at which bar shifts to `LowThresholdColor` (`-1` disables). |
| `LowThresholdColor` | `string` | `null` | Hex color when ratio falls at or below `LowThreshold`. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class BossCharacterStats : MonoBehaviour
{
    public float maximumBossHealth = 5000f;

    [Header("Dynamic Boss Health Gauge")]
    [AnimatedProgressBar(
        nameof(maximumBossHealth), 
        FillColor = "#9b59b6", 
        BarHeight = 14f, 
        AnimationDuration = 400f,
        LabelFormat = "HP: {value} / {max} ({percent}%)",
        LowThreshold = 0.25f,
        LowThresholdColor = "#e74c3c"
    )]
    public float currentBossHealth = 3750f;

    [Header("Interactive Stamina Meter")]
    [AnimatedProgressBar(0f, 100f, FillColor = "#f1c40f", BarHeight = 10f, IsEditable = true)]
    public float stamina = 60f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Sits cleanly inside layout cards and foldouts. |
| `ICollectionElement` | Supported | Renders progress meters for elements in numeric arrays or lists. |
| Category | PrimaryDrawer | Manages both interactive input and visual progress rendering. |
