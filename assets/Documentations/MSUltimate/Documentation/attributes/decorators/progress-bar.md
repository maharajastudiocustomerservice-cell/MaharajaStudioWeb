# [ProgressBar]

> Renders a numeric field as an interactive, styled visual progress bar with dynamic limits and threshold colors.

---

## 1. Overview & Value Proposition

**What it does:**
Converts numbers into animated, colored fill bars with custom heights, percentage displays, dynamic limits, and click-drag editing.

**The Problem:**
Sliders in standard Unity are plain, single-line track bars with no visual fill color, no threshold warnings (e.g. turning red below 20% health), and no support for dynamic max limits read from other properties.

**The Solution:**
Add `[ProgressBar]` to any numeric field:
- **Interactive Click & Drag:** Scrub values dynamically by dragging directly across the colored progress bar.
- **Dynamic Limits:** Bind `MaxValue` and `MinValue` to properties or methods on the object (e.g. `maxHealth`).
- **Low / High Threshold Colors:** Automatically change colors when ratios dip below or exceed thresholds (e.g. green $\rightarrow$ yellow $\rightarrow$ red).
- **Flexible Overlays:** Overlay percentages (`75%`), raw values (`150 / 200`), or custom formatted labels.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class HealthSystem : MonoBehaviour
{
    public float maxHealth = 100f;

    [ProgressBar(nameof(maxHealth), colorHex: "#2ecc71")]
    public float currentHealth = 85f;

    [ProgressBar(0, 100, colorHex: "#3498db")]
    public float experienceProgress = 42f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `float`, `int`, `double`, `short`, `byte`, `long` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ProgressBarAttribute()
public ProgressBarAttribute(float maxValue, string colorHex = null)
public ProgressBarAttribute(float minValue, float maxValue, string colorHex = null)
public ProgressBarAttribute(string dynamicMaxValueMember, string colorHex = null)
public ProgressBarAttribute(string dynamicMinValueMember, string dynamicMaxValueMember, string colorHex = null)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `maxValue` | `float` | `100f` | Maximum upper limit for the progress bar. |
| `minValue` | `float` | `0f` | Minimum lower limit for the progress bar. |
| `colorHex` | `string` | `null` | Hex color string for the active fill bar. |
| `dynamicMaxValueMember` | `string` | `null` | Name of field, property, or method returning dynamic maximum limit. |
| `dynamicMinValueMember` | `string` | `null` | Name of field, property, or method returning dynamic minimum limit. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MinValue` | `float` | `0f` | Static minimum limit value. |
| `MaxValue` | `float` | `100f` | Static maximum limit value. |
| `DynamicMinValueMember` | `string` | `null` | Member name providing dynamic minimum value. |
| `DynamicMaxValueMember` | `string` | `null` | Member name providing dynamic maximum value. |
| `CustomLabel` | `string` | `null` | Custom text label overlaid on the progress bar. |
| `LabelFormat` | `string` | `null` | Custom format string (tokens: `{label}`, `{value}`, `{min}`, `{max}`, `{percent}`). |
| `ColorHex` | `string` | `null` | Primary fill bar hex color. |
| `BackgroundColor` | `string` | `null` | Hex background track color behind the fill bar. |
| `Height` | `float` | `15f` | Bar height in pixels. |
| `BorderColor` | `string` | `null` | Hex color of the progress bar border. |
| `BorderWidth` | `float` | `0f` | Thickness of the border in pixels. |
| `BorderRadius` | `float` | `0f` | Corner rounding radius in pixels. |
| `LabelColor` | `string` | `null` | Hex color of the overlaid label text. |
| `LabelFontSize` | `int` | `0` | Font size of overlaid label text (0 uses default). |
| `Alignment` | `UiAlignment` | `UiAlignment.Center` | Text alignment within the progress bar. |
| `DrawInputField` / `ShowInputField` | `bool` | `true` | Draws standard numeric input field above the bar. |
| `IsEditable` / `Interactive` | `bool` | `true` | Allows dragging directly on the bar to scrub values. |
| `ShowValue` | `bool` | `true` | Displays numeric values in the overlay text. |
| `ShowPercentage` | `bool` | `false` | Displays percentage formatted text in the overlay. |
| `LowThreshold` | `float` | `-1f` | Ratio (0–1) at/below which bar switches to `LowThresholdColor`. |
| `LowThresholdColor` | `string` | `null` | Hex color applied when below low threshold. |
| `HighThreshold` | `float` | `-1f` | Ratio (0–1) at/above which bar switches to `HighThresholdColor`. |
| `HighThresholdColor` | `string` | `null` | Hex color applied when above high threshold. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class MechEnergyCore : MonoBehaviour
{
    public float maxCapacitorJoules = 2500f;

    [Header("Reactor Capacitor")]
    [ProgressBar(nameof(maxCapacitorJoules), colorHex: "#3498db", Height = 22f, ShowPercentage = true, 
                 LowThreshold = 0.2f, LowThresholdColor = "#e74c3c")]
    public float currentJoules = 1850f;

    [Header("Heat Dissipation")]
    [ProgressBar(0, 100, colorHex: "#f39c12", Height = 18f, 
                 HighThreshold = 0.85f, HighThresholdColor = "#c0392b")]
    public float internalCoreHeat = 35f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[HideLabel]` | Supported | Progress bar stretches edge-to-edge across the card. |
| `[BoxGroup]` | Supported | Integrates cleanly inside groups and tabs. |
| `[ReadOnly]` | Supported | Interactive dragging is disabled; functions strictly as a live gauge. |
