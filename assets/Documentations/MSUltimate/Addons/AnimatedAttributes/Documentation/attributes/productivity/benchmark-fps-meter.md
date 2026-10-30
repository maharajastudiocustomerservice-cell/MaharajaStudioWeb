# [BenchmarkFPSMeter]

> Renders a live micro-speedometer gauge and rolling graph displaying real-time FPS and frame time directly inside the inspector.

---

## 1. Overview & Value Proposition

**What it does:**
`[BenchmarkFPSMeter]` embeds an active performance telemetry gauge into the inspector. It renders a circular analog speedometer needle alongside real-time framerate and frame-time measurements (ms), calibrated against a customizable baseline target framerate (`TargetFPS`). The gauge size (`GaugeSize`) can be scaled, and the target baseline can be interactively scrubbed (`IsEditable = true`). It also implements `ICollectionElementAttribute` for multi-metric profiling collections.

**The Problem:**
Profiling scene optimizations, physics load, procedural meshing scripts, or particle bottlenecks usually forces developers to juggle external Profiler windows or Game view statistics overlays. This breaks workflow focus when tweaking performance-heavy numbers in the Inspector.

**The Solution:**
Decorating performance-critical fields or profile targets with `[BenchmarkFPSMeter]`:
- **Integrated Live FPS Readout:** Continuously samples rendering framerate and draws a dynamic analog speedometer gauge directly above or beside the property.
- **Dynamic Threshold Coloration:** Changes color automatically from green (above target) to amber (marginal) to red (dropping below `TargetFPS`).
- **Configurable Gauge Dimensions:** Scale the speedometer diameter (`GaugeSize`) from a compact 40px chip to a prominent 80px instrument.
- **Direct Input Companion Support:** Keeps the underlying serialized property editable (`DrawInputField = true`) for manual input adjustments.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class PerformanceProfile : MonoBehaviour
{
    [BenchmarkFPSMeter(targetFps: 60f)]
    public float targetFrameRate = 60f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `float`, `double`, `int`, `long` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Collection Element Support** | Yes (`ICollectionElementAttribute`) |

---

## 4. Constructors & Parameters

```csharp
public BenchmarkFPSMeterAttribute(float targetFps = 60f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `targetFps` | `float` | `60f` | Target framerate baseline in FPS used for needle scaling and color thresholds. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `TargetFPS` | `float` | `60f` | Target baseline framerate for speedometer thresholds. |
| `GaugeSize` | `float` | `60f` | Visual diameter of the speedometer gauge in pixels. |
| `DrawInputField` | `bool` | `true` | Whether to draw the standard serialized property input field beside the gauge. |
| `ShowInputField` | `bool` | `true` | Alias for `DrawInputField`. |
| `IsEditable` | `bool` | `true` | Whether the meter target rate can be interactively scrubbed. |
| `Interactive` | `bool` | `true` | Alias for `IsEditable`. |
| `CustomLabel` | `string` | `null` | Custom label prefix displayed beside the FPS meter. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class GraphicsEngineSettings : MonoBehaviour
{
    [Header("Simulation Performance Benchmark")]
    [BenchmarkFPSMeter(
        targetFps: 120f, 
        GaugeSize = 75f, 
        CustomLabel = "Physics Tick Target"
    )]
    public float targetPhysicsFPS = 120f;

    [Header("Per-Platform Frame Budget")]
    [BenchmarkFPSMeter(targetFps: 60f)]
    public List<float> platformTargetFrameRates = new List<float> { 30f, 60f, 120f };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Sits cleanly inside diagnostic panels, graphics setups, and debug monitors. |
| Collections (`List<float>`) | Supported | Implements `ICollectionElementAttribute` for multiple framerate profiling targets. |
| `[ReadOnly]` | Supported | Locks the underlying property while keeping live FPS meter updates active. |
