# [VisualDataChart]

> Renders high-performance interactive visual charts (Bar, Line, Area, Sparkline, Stepped) directly above numeric arrays and lists.

---

## 1. Overview & Value Proposition

**What it does:**
Renders beautiful Bar, Line, Area, and Sparkline graphs directly above your number arrays and lists.

**The Problem:**
Balancing numerical progression curves—like weapon recoil over 10 shots, player XP across 20 levels, or damage falloff over distance—is really difficult when looking at a long vertical list of float values. You can't see the curve shape or spot sudden spikes without mentally graphing the numbers.

**The Solution:**
Add `[VisualDataChart]` above any array or list of numbers:
- **Instant Visual Graph:** Immediately visualizes your numbers as an Area, Line, Bar, Sparkline, or Stepped chart.
- **Multiple Chart Styles:** Choose the right visual style for your data (e.g. Area charts for XP curves, Bar charts for audio spectrums).
- **Min/Max Guides:** Shows clear scale markers so you always know the data bounds.
- **Real-Time Updates:** As you edit numbers in the list, the chart geometry redraws smoothly in real time.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class LevelProgression : MonoBehaviour
{
    [VisualDataChart(ChartType.Area, 75f, "#2ECC71")]
    public float[] experiencePerLevel = new float[] { 100, 250, 500, 900, 1500, 2400 };
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Field | AttributeTargets.Property` |
| **Supported Types** | `float[]`, `int[]`, `List<float>`, `List<int>`, `double[]`, `long[]` |
| **Collection Interface** | `ICollectionPresentationAttribute` (Alternate Collection View Mode) |
| **Allow Multiple** | `false` |
| **Inherited** | `true` |
| **Build Overhead** | Editor-only (Zero runtime build overhead / stripped in builds) |
| **Minimum Unity** | Unity 6 (6000.x)+ |

---

## 4. Constructors & Signatures

```csharp
public VisualDataChartAttribute()
public VisualDataChartAttribute(ChartType type)
public VisualDataChartAttribute(ChartType type, float height)
public VisualDataChartAttribute(ChartType type, float height, string colorHex)
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `EnableCustomPresentation` | `bool` | `true` | Whether custom collection presentation mode (📊 toggle) is enabled. |
| `Type` | `ChartType` | `ChartType.Bar` | Visualization style (`Bar`, `Line`, `Area`, `Sparkline`, `Stepped`). |
| `Height` | `float` | `60f` | Vertical pixel height of the chart canvas. |
| `ColorHex` | `string` | `"#3498db"` | Primary line or bar fill accent color in hex format. |
| `BackgroundColorHex`| `string`| `"#1a1a1acc"` | Dark viewport background color behind the chart data. |
| `ShowValues` | `bool` | `false` | Whether to display numeric labels directly on data points or bars. |
| `ShowMinMaxLabels` | `bool` | `true` | Displays floating min/max numeric scale labels along the Y-axis. |
| `ShowPoints` | `bool` | `true` | Draws circular dot vertices at each data point on line/area charts. |
| `LineThickness` | `float` | `2f` | Stroke width in pixels for line, area, and sparkline graphs. |
| `MinValue` | `float` | `float.NaN` | Explicit minimum scale floor (auto-scales if NaN). |
| `MaxValue` | `float` | `float.NaN` | Explicit maximum scale ceiling (auto-scales if NaN). |
| `CustomLabel` | `string` | `null` | Optional custom title displayed above the chart. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

[CreateAssetMenu(fileName = "WeaponRecoilCurve", menuName = "Game/Weapons/Recoil Profile")]
public class WeaponRecoilCurve : ScriptableObject
{
    [BoxGroup("Recoil Simulation", Box = true)]
    [VisualDataChart(
        type: ChartType.Line, 
        height: 90f, 
        colorHex: "#E74C3C",
        ShowMinMaxLabels = true,
        ShowPoints = true,
        LineThickness = 2.5f,
        CustomLabel = "Recoil Rise Per Shot"
    )]
    [Tooltip("Vertical kick degrees per consecutive bullet fired.")]
    public List<float> bulletRecoilSteps = new List<float>() { 0.5f, 1.2f, 2.1f, 3.4f, 4.0f, 4.2f };

    [BoxGroup("Performance Telemetry", Box = true)]
    [InfoBox("Collection presentation mode enabled via ICollectionPresentationAttribute. Use 📊 header toggle.")]
    [VisualDataChart(ChartType.Area, 75f, "#10B981", CustomLabel = "Network Latency History (ms)")]
    public float[] frameLatencyHistory = new float[] { 16.2f, 16.8f, 17.5f, 16.4f, 33.1f, 18.2f };
}
```

---

## 7. Stacking & Compatibility Matrix

- **Grouping:** Pairs seamlessly inside `[BoxGroup]` and `[CardGroup]`.
- **Dynamic Resizing:** Renders responsively across narrow and wide Inspector window layouts.
- **Immediate Repaint:** Automatically updates chart geometry in real-time as values are typed into array slots or modified via script.

### Collection Presentation Matrix

| Collection / Container Type | Presentation Support | Render Mode | Notes |
| :--- | :---: | :--- | :--- |
| `float[]` | ✅ Yes | Alternate View (📊) | Toggles between list view and interactive vector chart canvas. |
| `List<float>` | ✅ Yes | Alternate View (📊) | Seamlessly embedded into collection header view modes. |
| `int[]` | ✅ Yes | Alternate View (📊) | Renders discrete integer steps and bars. |
| `List<int>` | ✅ Yes | Alternate View (📊) | Ideal for level curves, wave counts, and stat tiers. |
| `AdvancedList<float>` | ✅ Yes | Alternate View (📊) | Full pagination and reordering integration. |

