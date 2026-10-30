# [AnimatedDialGauge]

> Displays a circular dial gauge with a damped animated needle, glowing arc fill, dynamic bounds, and interactive needle scrubbing.

---

## 1. Overview & Value Proposition

**What it does:**
`[AnimatedDialGauge]` replaces conventional numeric textboxes or linear sliders with an analog circular dial gauge. A smooth spring-damped needle (`NeedleDamping`) points along a glowing circular arc (`ArcColor`) representing current numeric progress between `MinValue` and `MaxValue`. Users can click and drag angularly along the dial face to interactively scrub values.

**The Problem:**
Speedometers, tachometers, steering angles, power gauges, and pressure meters are fundamentally circular in nature. Linear horizontal progress bars fail to convey the tactile feel of rotary automotive or aviation meters.

**The Solution:**
Decorating numeric fields with `[AnimatedDialGauge]`:
- **Analog Spring-Damped Needle:** Smoothly interpolates toward target values with authentic mechanical inertia.
- **Interactive Angular Dragging:** Click and scrub anywhere on the dial face (`IsEditable = true`) to rotate the needle.
- **Dynamic Upper & Lower Bounds:** Bind `DynamicMaxValueMember` and `DynamicMinValueMember` for contextual dial ranges.
- **Value & Percentage Overlays:** Formatted numeric readout (`ValueFormat`) or percentage text displayed cleanly below the dial.
- **Collection Cascading:** Implements `ICollectionElementAttribute` for multi-dial motor arrays or engine cylinder telemetries.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class VehicleSpeedometer : MonoBehaviour
{
    [AnimatedDialGauge(min: 0f, max: 240f, size: 90f, NeedleColor = "#EF4444")]
    public float currentSpeedKmh = 120f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `int`, `float`, `double`, `long`, `short`, `byte` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Collection Element Support** | Yes (`ICollectionElementAttribute`) |

---

## 4. Constructors & Parameters

```csharp
public AnimatedDialGaugeAttribute(float min = 0f, float max = 100f, float size = 80f)

public AnimatedDialGaugeAttribute(string dynamicMaxValueMember, float size = 80f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `min` | `float` | `0f` | Minimum value mapped to the start of the dial arc. |
| `max` | `float` | `100f` | Maximum value mapped to the end of the dial arc. |
| `size` | `float` | `80f` | Diameter in pixels of the circular dial gauge. |
| `dynamicMaxValueMember` | `string` | — | Name of a member returning dynamic max dial capacity. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MinValue` | `float` | `0f` | Minimum value at arc start. |
| `MaxValue` | `float` | `100f` | Maximum value at arc termination. |
| `DynamicMaxValueMember` | `string` | `null` | Member name returning dynamic upper bound. |
| `DynamicMinValueMember` | `string` | `null` | Member name returning dynamic lower bound. |
| `GaugeSize` | `float` | `80f` | Gauge diameter in pixels. |
| `NeedleColor` | `string` | `"#EF4444"` | Hex color string for the indicator pointer needle. |
| `ArcColor` | `string` | `"#3B82F6"` | Hex color string for the active illuminated value arc. |
| `TrackColor` | `string` | `"#1E293B"` | Hex color string for the background unfilled dial track. |
| `NeedleDamping` | `float` | `8f` | Spring damping coefficient controlling needle settling time. |
| `DrawInputField` | `bool` | `true` | Whether to draw the standard serialized property field alongside the dial. |
| `ShowInputField` | `bool` | `true` | Alias for `DrawInputField`. |
| `IsEditable` | `bool` | `true` | Whether angular dragging on the dial adjusts the field value. |
| `Interactive` | `bool` | `true` | Alias for `IsEditable`. |
| `CustomLabel` | `string` | `null` | Optional label displayed above or beside the dial. |
| `ShowValue` | `bool` | `true` | Whether to display the numeric value readout below the dial. |
| `ShowPercentage` | `bool` | `false` | Whether to display percentage readout below the dial. |
| `ValueFormat` | `string` | `"{0:F1}"` | Format string applied to numeric value text. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class TurboEngineDiagnostics : MonoBehaviour
{
    [Header("Engine RPM")]
    public float redlineRpm = 8500f;

    [AnimatedDialGauge(
        nameof(redlineRpm), 
        size: 100f, 
        NeedleColor = "#DC2626", 
        ArcColor = "#F59E0B", 
        TrackColor = "#0F172A",
        NeedleDamping = 12f,
        CustomLabel = "TACHOMETER",
        ValueFormat = "{0:N0} RPM"
    )]
    public float currentRpm = 4200f;

    [Header("Boost Pressure (PSI)")]
    [AnimatedDialGauge(min: 0f, max: 35f, size: 75f, NeedleColor = "#06B6D4", ArcColor = "#0284C7")]
    public float manifoldBoostPsi = 18.5f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Aligns centered or inline within custom group frames. |
| `[ReadOnly]` | Supported | Disables interactive needle scrubbing while preserving smooth needle animation. |
| Arrays & Lists | Supported | Implements `ICollectionElementAttribute` for multiple engine dials in arrays. |
