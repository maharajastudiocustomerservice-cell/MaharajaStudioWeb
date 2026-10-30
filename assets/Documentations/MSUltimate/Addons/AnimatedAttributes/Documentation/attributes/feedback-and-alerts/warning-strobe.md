# [WarningStrobe]

> Renders alternating high-visibility emergency hazard warning stripes that pulse rhythmically across invalid or critical inspector fields.

---

## 1. Overview & Value Proposition

**What it does:**
`[WarningStrobe]` overlays high-contrast, industrial hazard hazard stripes behind or around inspector controls. The stripes oscillate rhythmically between two customizable hex colors (`StrobeColor1`, `StrobeColor2`) at a designated frequency (`StrobeSpeed` in Hertz). It can be configured to pulse permanently (`AlwaysActive = true`) or activate upon critical error conditions.

**The Problem:**
In expansive projects with hundreds of configurable fields, missing an essential reference, setting an unsafe multiplier, or overlooking an uncalibrated threshold can cause runtime failure. Subdued text warnings and subtle error icons frequently blend into the surrounding dark grey editor background.

**The Solution:**
Decorating critical or hazardous fields with `[WarningStrobe]`:
- **Industrial Hazard Aesthetic:** Instantly demands developer attention with alternating diagonal hazard warning bars.
- **Dynamic Frequency Tuning:** Regulate pulse oscillation tempo via `StrobeSpeed` (Hz) for subtle reminders or frantic emergency strobes.
- **Dual-Color Customization:** Configure contrasting warning duotones (e.g., hazard amber/black, radioactive yellow/charcoal, or emergency crimson/white).
- **Persistent or Conditional Modes:** Toggle between unconditional always-on display (`AlwaysActive`) and event-triggered alerting.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class SecurityConsole : MonoBehaviour
{
    [WarningStrobe(color1: "#EF4444", strobeSpeed: 3.5f)]
    public bool lockdownProtocolActive = true;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property, `T[]`, `List<T>`, `AdvancedList<T>`, `SerializableDictionary<K, V>` |
| **Collection Interface** | `ICollectionElementAttribute` (Automatic Element Cascading) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public WarningStrobeAttribute(string color1 = "#F59E0B", float strobeSpeed = 4f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `color1` | `string` | `"#F59E0B"` | Primary hex color for the alternating hazard stripes. |
| `strobeSpeed` | `float` | `4f` | Strobe oscillation speed in Hertz (cycles per second). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `StrobeColor1` | `string` | `"#F59E0B"` | Primary hex color for alternating hazard warning stripes. |
| `StrobeColor2` | `string` | `"#000000"` | Secondary contrasting hex color for alternating hazard stripes. |
| `StrobeSpeed` | `float` | `4f` | Oscillation frequency in Hertz controlling the flashing tempo. |
| `AlwaysActive` | `bool` | `false` | Whether the hazard strobe effect remains active unconditionally. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class NuclearReactorCore : MonoBehaviour
{
    [BoxGroup("Containment Safety Gate", Box = true)]
    [WarningStrobe(
        color1: "#DC2626", 
        strobeSpeed: 5f, 
        StrobeColor2 = "#FFFFFF", 
        AlwaysActive = true
    )]
    public bool emergencyScramArmed = false;

    [BoxGroup("Radiation Threshold", Box = true)]
    [WarningStrobe(color1: "#F59E0B", strobeSpeed: 2.5f, StrobeColor2 = "#18181B", AlwaysActive = true)]
    public float curieRadiationDose = 1250f;

    [BoxGroup("Critical System Alarms", Box = true)]
    [InfoBox("Direct collection cascading via ICollectionElementAttribute.")]
    [WarningStrobe(color1: "#EF4444", strobeSpeed: 4.5f, AlwaysActive = true)]
    public string[] criticalAlarmCodes = new string[]
    {
        "ALARM-901: COOLANT VENT VALVE STUCK OPEN",
        "ALARM-904: CORE TEMPERATURE EXCEEDING 1200C"
    };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Hazard stripes respect outer box container radii and padding. |
| `[ThresholdSpikeFlash]` | Stacking | Combines instantaneous boundary ripples with sustained hazard warning stripes. |
| `[HelpBox]` | Supported | Pairs with help boxes to clearly explain the hazard condition behind the strobe. |

### Collection Cascading Matrix

| Collection / Container Type | Cascading Support | Render Target | Notes |
| :--- | :---: | :--- | :--- |
| `string[]` | ✅ Yes | Individual array items | Renders animated hazard stripes on each string alarm row. |
| `List<float>` | ✅ Yes | Individual list items | Each numeric entry displays animated warning stripes. |
| `AdvancedList<T>` | ✅ Yes | Individual list items | Cascades stripes to items; outer container is cleanly preserved. |
| `SerializableDictionary<K, V>` | ✅ Yes | Dictionary value column | Value column rows display hazard warning stripes. |
| `SerializableNullable<T>` | ✅ Yes | Inner value element | Active state displays hazard stripes. |
| `SerializableTuple<...>` | ✅ Yes | Tuple member fields | Displays stripes within tuple columns. |

