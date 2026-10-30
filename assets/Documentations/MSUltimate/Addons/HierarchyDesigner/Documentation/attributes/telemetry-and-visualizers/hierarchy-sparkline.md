# [HierarchySparkline]

> Renders a live rolling mini sparkline graph of historic numeric values directly on the hierarchy row.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchySparkline]` records recent numeric values across consecutive editor frames and draws a live, rolling micro-sparkline graph on the hierarchy row. Driven by `HierarchySparklineRenderer`, it maintains a sliding window of historical points (`HistoryLength = 24`), normalizes points between `MinValue` and `MaxValue`, and plots a smoothed line graph (`HierarchyDrawUtilities.DrawSparkline`) within a sleek dark box (`BackgroundColor = "#1E272E"`, `LineColor = "#00FFAA"`).

**The Problem:**
Diagnosing performance spikes, frame time hiccups, fluctuating network ping, or erratic physics velocities cannot be done with instantaneous numbers alone. A single number like `42ms` doesn't reveal whether latency is holding steady or oscillating erratically. Opening Unity's Profiler or external graphing tools can be overkill for quick balance passes.

**The Solution:**
Decorating numeric fields or properties with `[HierarchySparkline]`:
- **Live Historical Trendline:** Watch a continuous rolling plot of the last 24+ data points directly beside the GameObject.
- **Immediate Anomaly Detection:** Easily spot erratic oscillations, periodic spikes, or sudden drops.
- **Configurable Normalization:** Set fixed expected min/max boundaries or let values scale within range.
- **Compact Card Container:** Embedded cleanly in the row (`Width = 50f`, `Height = 12f`) with rounded corners.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class PerformanceMonitor : MonoBehaviour
{
    [HierarchySparkline(MinValue = 0f, MaxValue = 60f, LineColor = "#10B981")]
    public float frameTimeMs;
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
| **Render Engine** | `HierarchySparklineRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchySparklineAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `HistoryLength` | `int` | `24` | Number of historic data points to retain and plot in the sliding window. |
| `MinValue` | `float` | `0f` | Expected minimum value for graph normalization. |
| `MaxValue` | `float` | `100f` | Expected maximum value for graph normalization. |
| `LineColor` | `string` | `"#00FFAA"` | Hex line color of the sparkline plot. |
| `BackgroundColor` | `string` | `"#1E272E"` | Hex background fill color of the sparkline graph card. |
| `Width` | `float` | `50f` | Width of the sparkline graph in pixels. |
| `Height` | `float` | `12f` | Height of the sparkline graph in pixels. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the sparkline graph remains visible and updates during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class NetworkHealthProbe : MonoBehaviour
{
    [Header("Network Latency Telemetry")]
    [HierarchySparkline(
        HistoryLength = 32, 
        MinValue = 10f, 
        MaxValue = 120f, 
        LineColor = "#38BDF8", 
        BackgroundColor = "#0F172A", 
        Width = 55f, 
        Height = 12f, 
        XOffset = 6f)]
    public float pingLatencyMs = 35f;

    public int packetsLost = 0;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyDeltaTracker]`** | High | Combine sparklines with delta rate indicators for simultaneous trendline and directional change telemetry. |
| **`[HierarchyMinMaxTracker]`** | High | Use min/max trackers for extreme bounds and sparklines for recent wave shapes. |
| **History Buffer** | Session Only | History buffers reside in static editor session dictionaries; cleared cleanly on scene reload. |
| **Numeric Member Types** | High | Works directly with `float`, `int`, and `double` fields and properties. |
