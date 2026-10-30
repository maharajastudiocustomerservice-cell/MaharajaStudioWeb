# [HierarchyMinMaxTracker]

> Tracks and displays the observed minimum and maximum runtime values for numeric fields directly on the hierarchy row.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyMinMaxTracker]` attaches to numeric fields (`float`, `int`, `double`) and records the historical minimum and maximum values encountered during runtime execution. Driven by `HierarchyMinMaxTrackerRenderer`, it displays a live range indicator (`Min ~ Max`, e.g. `12.4 ~ 89.1`) on the right side of the hierarchy row. It supports custom format strings, distinct color coding for min and max bounds, optional live value display, background boxes, and automatic state reset whenever entering Play Mode.

**The Problem:**
When balancing gameplay mechanics (character movement speeds, frame deltas, weapon recoil, network ping, AI decision weights), numeric values fluctuate continuously. Profiling these values usually requires setting up debug charts, checking Profiler counters, or cluttering the console with spammy `Debug.Log` statements, which can drop frame rates.

**The Solution:**
Decorating numeric fields with `[HierarchyMinMaxTracker]`:
- **Continuous Boundary Observation:** Tracks extremes seamlessly without requiring extra code or debug logging.
- **Glanceable Hierarchy Telemetry:** Inspect fluctuating gameplay metrics directly in the hierarchy while keeping focus on the Scene View.
- **Independent Per-Instance Caching:** Tracks each component instance separately via unique InstanceID keys.
- **Auto-Reset on Play:** Automatically clears previous session bounds on entering Play Mode (`ResetOnPlay = true`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class PlayerMovement : MonoBehaviour
{
    [HierarchyMinMaxTracker(ValueFormat = "{0:F1} m/s", MinColor = "#38BDF8", MaxColor = "#F43F5E")]
    public float currentSpeed;
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
| **Render Engine** | `HierarchyMinMaxTrackerRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyMinMaxTrackerAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Separator` | `string` | `"~"` | String placed between the observed minimum and maximum values. |
| `ValueFormat` | `string` | `"{0:F1}"` | C# format string applied to min and max values. |
| `ShowCurrentValue` | `bool` | `false` | Whether to display the live current value before the min and max range. |
| `MinColor` | `string` | `"#5599CC"` | Hex color of the minimum observed value text. |
| `MaxColor` | `string` | `"#CC5555"` | Hex color of the maximum observed value text. |
| `SeparatorColor` | `string` | `"#666666"` | Hex color of the separator string. |
| `LabelColor` | `string` | `"#DDDDDD"` | Hex color of the current value label when `ShowCurrentValue` is `true`. |
| `BackgroundColor` | `string` | `""` | Optional hex background color behind the tracker display. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `ResetOnPlay` | `bool` | `true` | Whether tracked min and max bounds reset upon entering Play Mode. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the tracker remains active and updating during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class NetworkLatencyMonitor : MonoBehaviour
{
    [Header("Network Telemetry")]
    [HierarchyMinMaxTracker(
        Separator = " → ", 
        ValueFormat = "{0:F0}ms", 
        ShowCurrentValue = true, 
        MinColor = "#10B981", 
        MaxColor = "#EF4444", 
        BackgroundColor = "#1E293B", 
        XOffset = 6f)]
    public float roundTripTimeMs;

    private void Update()
    {
        // Simulated network jitter
        roundTripTimeMs = 30f + Mathf.PingPong(Time.time * 25f, 60f) + Random.Range(-5f, 15f);
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyProgressBar]`** | High | Combine with a progress bar to show both current proportion and historical extremes. |
| **`[HierarchyStatusDot]`** | High | Use a status dot to flag critical connection states alongside numeric min/max bounds. |
| **`[HierarchyHighlight]`** | High | Tint the row when values exceed critical gameplay thresholds. |
| **Numeric Field Types** | High | Fully compatible with `int`, `float`, `double`, and numeric struct wrappers. |
