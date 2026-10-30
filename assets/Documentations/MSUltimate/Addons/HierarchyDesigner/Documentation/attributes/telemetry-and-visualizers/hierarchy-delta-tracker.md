# [HierarchyDeltaTracker]

> Observes and displays real-time rate of change indicators for numeric fields directly on the hierarchy row.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyDeltaTracker]` measures frame-to-frame numeric fluctuations and displays a live directional rate-of-change indicator on the hierarchy row. Driven by `HierarchyDeltaTrackerRenderer`, it compares the current value with the previous frame's reading:
- **Increasing Values:** Displays an upward arrow in green (`PositiveColor = "#2ECC71"`, e.g. `"▲ +1.5"`).
- **Decreasing Values:** Displays a downward arrow in red (`NegativeColor = "#E74C3C"`, e.g. `"▼ -0.8"`).
- **Stable Values:** Displays a neutral dot in slate (`NeutralColor = "#95A5A6"`, e.g. `"● 0.0"`).
- **Format Flexibility:** Supports custom C# numeric formatting strings (`Format = "{0:+0.0;-0.0;0.0}"`).

**The Problem:**
When balancing dynamic gameplay systems (player acceleration, physics velocities, health regeneration, resource drain rates, heat buildup), watching the absolute value alone does not tell you if the value is currently rising or dropping, or how fast the change is occurring.

**The Solution:**
Decorating numeric fields or properties with `[HierarchyDeltaTracker]`:
- **Instant Directional Rate Feedback:** Immediately see whether values are rising, dropping, or plateauing.
- **Color-Coded Status Symbols:** Intuitive green `▲`, red `▼`, and gray `●` cues provide instant visual clarity.
- **Custom Numeric Precision:** Control floating-point precision to filter out micro-jitter or display high-precision rates.
- **Per-Component History:** Tracks each component instance independently in editor session memory.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class PlayerMovement : MonoBehaviour
{
    [HierarchyDeltaTracker(PositiveColor = "#10B981", NegativeColor = "#EF4444")]
    public float currentSpeed;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Field`, `Property` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyDeltaTrackerRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyDeltaTrackerAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `PositiveColor` | `string` | `"#2ECC71"` | Hex color when the numeric value is increasing (`▲`). |
| `NegativeColor` | `string` | `"#E74C3C"` | Hex color when the numeric value is decreasing (`▼`). |
| `NeutralColor` | `string` | `"#95A5A6"` | Hex color when the numeric value is unchanged (`●`). |
| `Format` | `string` | `"{0:+0.0;-0.0;0.0}"` | String format for displaying the delta change number. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the delta tracker remains visible and updating during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class ReactorCoreTelemetry : MonoBehaviour
{
    [Header("Core Heat Balance")]
    [HierarchyDeltaTracker(
        PositiveColor = "#F97316", 
        NegativeColor = "#06B6D4", 
        NeutralColor = "#64748B", 
        Format = "{0:+0.00;-0.00;0.00} °C/s", 
        XOffset = 6f)]
    public float temperatureCelsius = 350f;

    public bool coolingPumpActive = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyMinMaxTracker]`** | High | Use delta tracking for instant velocity of change and min/max tracking for historical extremes. |
| **`[HierarchyProgressBar]`** | High | Place progress bars alongside delta trackers for complete gauge + rate telemetry. |
| **Numeric Member Types** | High | Compatible with `float`, `int`, `double`, and custom numeric struct wrappers. |
| **Editor Repaint** | High | Updates diff calculation exclusively on repaint ticks; zero garbage collection or runtime CPU cost. |
