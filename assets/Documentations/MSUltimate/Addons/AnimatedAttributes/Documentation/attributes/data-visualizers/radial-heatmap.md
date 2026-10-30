# [RadialHeatmap]

> Renders a circular gauge that dynamically shifts color from cool blue to pulsing hot red as values rise toward critical thresholds.

---

## 1. Overview & Value Proposition

**What it does:**
`[RadialHeatmap]` provides a thermal visual indicator for temperature, danger levels, resource stress, or engine heat. As values rise from `MinValue` to `MaxValue`, the circular arc smoothly interpolates across three distinct thermal tiers: `CoolColor` (blue), `WarmColor` (amber), and `HotColor` (red). When the value exceeds `CriticalThreshold`, the gauge engages an urgent pulsing heartbeat glow.

**The Problem:**
Heat buildup, radiation exposure, core temperature, and weapon overheating mechanics become dangerous only near extreme limits. Flat numerical fields provide no peripheral sense of thermal escalation or impending crisis.

**The Solution:**
Decorating thermal properties with `[RadialHeatmap]`:
- **Dynamic 3-Tone Thermal Palette:** Automatically blends between `CoolColor`, `WarmColor`, and `HotColor`.
- **Urgent Critical Warning Pulse:** Activates a rhythmic warning pulse as soon as values exceed `CriticalThreshold`.
- **Circular Interactive Scrubbing:** Drag directly along the circular ring (`IsEditable = true`) to modulate thermal levels.
- **Dynamic Upper & Lower Bounds:** Bind `DynamicMaxValueMember` and `DynamicMinValueMember` for contextual limits.
- **Collection Cascading:** Implements `ICollectionElementAttribute` for multi-core reactors or thruster clusters.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class ReactorCore : MonoBehaviour
{
    [RadialHeatmap(min: 0f, max: 100f, CriticalThreshold = 85f)]
    public float coreTemperature = 45f;
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
public RadialHeatmapAttribute(float min = 0f, float max = 100f)

public RadialHeatmapAttribute(string dynamicMaxValueMember)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `min` | `float` | `0f` | Minimum value mapped to arc start and cool thermal baseline. |
| `max` | `float` | `100f` | Maximum value mapped to arc end and maximum heat capacity. |
| `dynamicMaxValueMember` | `string` | — | Name of a member returning dynamic max thermal capacity. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MinValue` | `float` | `0f` | Minimum thermal threshold. |
| `MaxValue` | `float` | `100f` | Maximum thermal capacity. |
| `DynamicMaxValueMember` | `string` | `null` | Name of a member returning dynamic max heat limit. |
| `DynamicMinValueMember` | `string` | `null` | Name of a member returning dynamic min heat limit. |
| `CoolColor` | `string` | `"#3B82F6"` | Hex color string for low/nominal resting values. |
| `WarmColor` | `string` | `"#F59E0B"` | Hex color string for intermediate elevated values. |
| `HotColor` | `string` | `"#EF4444"` | Hex color string for critical danger values. |
| `CriticalThreshold` | `float` | `80f` | Value threshold at which hot color pulsing engages. |
| `Radius` | `float` | `30f` | Radius in pixels of the circular heatmap gauge. |
| `DrawInputField` | `bool` | `true` | Whether to draw the standard serialized property field beside the gauge. |
| `ShowInputField` | `bool` | `true` | Alias for `DrawInputField`. |
| `IsEditable` | `bool` | `true` | Whether dragging along the ring face scrubs the heat value. |
| `Interactive` | `bool` | `true` | Alias for `IsEditable`. |
| `CustomLabel` | `string` | `null` | Optional label displayed above or beside the gauge. |
| `ShowValue` | `bool` | `true` | Whether to display numeric text readout. |
| `ShowPercentage` | `bool` | `false` | Whether to display percentage text readout. |
| `ValueFormat` | `string` | `"{0:F1}"` | Format string for the numeric readout text. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class PlasmaCannon : MonoBehaviour
{
    [Header("Heat Tolerances")]
    public float thermalShutdownLimit = 200f;

    [Header("Current Barrel Heat")]
    [RadialHeatmap(
        nameof(thermalShutdownLimit), 
        CriticalThreshold = 160f, 
        Radius = 36f,
        CoolColor = "#06B6D4",
        WarmColor = "#EAB308",
        HotColor = "#DC2626",
        CustomLabel = "BARREL HEAT",
        ValueFormat = "{0:N0} °C"
    )]
    public float barrelHeat = 125f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Frames neatly within telemetry dashboards or weapon stat modules. |
| `[HeartbeatAlert]` | Stacking | Can be paired to reinforce critical alert states when approaching thresholds. |
| Arrays & Lists | Supported | Implements `ICollectionElementAttribute` for multiple engine cores in arrays. |
