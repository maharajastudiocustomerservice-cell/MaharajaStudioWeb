# [HierarchyProgressBar]

> Renders an interactive horizontal progress bar directly on the hierarchy row for numeric fields with dynamic bounds and threshold alerts.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyProgressBar]` renders a sleek, miniature progress bar directly on the hierarchy row for numeric fields (`float`, `int`). Driven by `HierarchyProgressBarRenderer`, it dynamically visualizes fill ratios based on fixed or reflected bounds (`MaxValue`, `MaxValueField`, `MinValue`, `MinValueField`). It supports low and high threshold color transitions (e.g., turning red on low health or blue on high charge), inline numeric labels (`ShowValue = true`), custom tooltips, and interactive drag scrubbing (`IsEditable = true`).

**The Problem:**
Monitoring vital gauges (player health, boss stamina, battery charge, build progress, cooldown timers) during play testing requires switching focus between the Game View, custom UI overlays, and crowded Inspector panels. Without in-hierarchy bars, debugging multi-entity gameplay states (e.g. 20 spawned enemy health bars) is cumbersome.

**The Solution:**
Decorating numeric fields with `[HierarchyProgressBar]`:
- **At-a-Glance Telemetry:** Monitor health, mana, stamina, and cooldown bars for all active scene entities at once.
- **Dynamic Reflection Bounds:** Dynamically query component fields, properties, or methods for maximum and minimum values (e.g. `maxHealth`).
- **3-Phase Threshold Colors:** Transitions color automatically when entering critical low thresholds (`LowThresholdColor`) or peak high thresholds (`HighThresholdColor`).
- **Direct Interactive Scrubbing:** Click or drag directly on the hierarchy bar to modify the field value in real time.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class HealthComponent : MonoBehaviour
{
    [HierarchyProgressBar(100f, "#10B981", LowThreshold = 0.25f, LowThresholdColor = "#EF4444")]
    public float currentHealth = 75f;
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
| **Render Engine** | `HierarchyProgressBarRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyProgressBarAttribute()
```

- Parameterless constructor for full property-based setup.

```csharp
public HierarchyProgressBarAttribute(float maxValue, string fillColor = "#3A8FD5")
```

- `maxValue`: Fixed maximum numeric value representing 100% fill.
- `fillColor`: Normal hex color of the filled portion of the bar.

```csharp
public HierarchyProgressBarAttribute(string maxValueField, string fillColor = "#3A8FD5")
```

- `maxValueField`: Name of a field, property, or method on the component providing a dynamic maximum value.
- `fillColor`: Normal hex color of the filled portion of the bar.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MaxValue` | `float` | `100f` | Fixed maximum value used to compute the fill ratio. |
| `MaxValueField` | `string` | `""` | Name of a field, property, or parameterless method providing a dynamic maximum value. |
| `MinValue` | `float` | `0f` | Minimum value mapped to 0% fill. |
| `MinValueField` | `string` | `""` | Name of a field, property, or parameterless method providing a dynamic minimum value. |
| `FillColor` | `string` | `"#3A8FD5"` | Standard hex color of the active progress bar fill. |
| `LowThresholdColor` | `string` | `""` | Hex color used when fill ratio is at or below `LowThreshold`. |
| `LowThreshold` | `float` | `0.25f` | Fill ratio (0.0 to 1.0) triggering the low-threshold color switch. |
| `HighThresholdColor` | `string` | `""` | Hex color used when fill ratio is at or above `HighThreshold`. |
| `HighThreshold` | `float` | `0.85f` | Fill ratio (0.0 to 1.0) triggering the high-threshold color switch. |
| `BackgroundColor` | `string` | `"#222222"` | Hex background color of the unfilled bar portion. |
| `Width` | `float` | `50f` | Total width of the progress bar in pixels. |
| `Height` | `float` | `4f` | Height of the progress bar in pixels. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `ShowValue` | `bool` | `false` | Whether to render numeric text beside the bar. |
| `ValueFormat` | `string` | `"{0:F0}"` | C# format string for the numeric value text. |
| `ValueColor` | `string` | `"#CCCCCC"` | Hex color of the displayed numeric text. |
| `IsEditable` | `bool` | `false` | Enables click and drag scrubbing directly on the hierarchy row. |
| `Interactive` | `bool` | `false` | Alias property for `IsEditable`. |
| `Tooltip` | `string` | `""` | Custom hover tooltip text displayed over the bar. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the progress bar remains visible and active during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class BossEncounterController : MonoBehaviour
{
    public float maxHealth = 2500f;

    [Header("Live Boss Telemetry")]
    [HierarchyProgressBar(
        maxValueField: nameof(maxHealth), 
        fillColor: "#6366F1", 
        LowThreshold = 0.20f, 
        LowThresholdColor = "#EF4444", 
        HighThreshold = 0.80f, 
        HighThresholdColor = "#10B981", 
        Width = 70f, 
        Height = 6f, 
        ShowValue = true, 
        ValueFormat = "{0:F0} HP", 
        IsEditable = true, 
        Tooltip = "Click/drag to test boss phase transitions", 
        XOffset = 6f)]
    public float currentHealth = 2100f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyMinMaxTracker]`** | High | Place progress bars alongside min/max trackers to observe both current state and historic range. |
| **`[HierarchyConditionalHighlight]`** | High | Highlight the whole row in deep red when the progress bar enters low-threshold state. |
| **`[HierarchyStatusDot]`** | High | Use status dots for discrete boolean states and progress bars for continuous values. |
| **Numeric Member Types** | High | Works seamlessly with `float`, `int`, and `double` serialized fields. |
