# [ThresholdSpikeFlash]

> Emits an instantaneous shockwave ripple and flash when a numeric field crosses defined threshold milestone boundaries.

---

## 1. Overview & Value Proposition

**What it does:**
`[ThresholdSpikeFlash]` attaches dynamic boundary monitoring to numeric properties in the Unity Inspector. As soon as a serialized field or property crosses one of the predefined threshold boundaries (`Thresholds`), the attribute triggers a radiating shockwave ripple and chromatic flash (`FlashColor`) across the property row for the specified duration (`FlashDuration`).

**The Problem:**
Numeric balancing frequently involves non-linear milestones—such as engine overheating past 100°C, speed barrier crossings, armor degradation phases, or boss enrage trigger percentages. Without visual feedback, developers and level designers must constantly reference documentation spreadsheets to know when a tuned variable has triggered critical gameplay phase gates.

**The Solution:**
Decorating milestone variables with `[ThresholdSpikeFlash]`:
- **Instant Milestone Shockwaves:** Dispatches an immediate visual ripple effect when the field value crosses from below to above (or vice-versa) any threshold milestone.
- **Multiple Arbitrary Thresholds:** Configure single or multiple boundary checkpoints (e.g., `25f, 50f, 75f, 100f`) via `params float[]` in the constructor.
- **Vibrant Alert Customization:** Tailor the shockwave hue (`FlashColor`) and transition duration (`FlashDuration`) to represent warnings, level gates, or danger thresholds.
- **Efficient Transition Polling:** Utilizes lightweight property change subscriptions within UI Toolkit, executing zero tick loops when the inspector field is idle.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class ReactorCore : MonoBehaviour
{
    [ThresholdSpikeFlash(50f, 80f, 100f)]
    public float temperatureCelsius = 45f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any numeric serializable field or property (`float`, `int`, `double`, `long`, etc.) |
| **Collection Cascading** | Supported via `ICollectionElementAttribute` (arrays, lists, advanced lists) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ThresholdSpikeFlashAttribute(params float[] thresholds)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `thresholds` | `params float[]` | `new float[] { 50f, 100f }` | Array of boundary values that trigger shockwave ripples when crossed. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Thresholds` | `float[]` | `{ 50f, 100f }` | Array of milestone boundaries that trigger the shockwave flash. |
| `FlashColor` | `string` | `"#F59E0B"` | Hex color string for the radiating ripple shockwave. |
| `FlashDuration` | `float` | `400f` | Duration in milliseconds of the ripple flash effect. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class ReactorCoreTelemetry : ModularMonoBehaviour
{
    [System.Serializable]
    public class AuxiliaryGeneratorCell
    {
        public string generatorName = "Sub-Level Fusion Cell 03";

        [ThresholdSpikeFlash(50f, 100f, 150f, FlashColor = "#EC4899", FlashDuration = 400f)]
        public float powerOutputMw = 85f;
    }

    [BoxGroup("1. Standalone Shockwaves")]
    [ThresholdSpikeFlash(25f, 50f, 75f, 100f, FlashColor = "#10B981", FlashDuration = 500f)]
    public float capacitorChargeLevel = 45f;

    [ThresholdSpikeFlash(80f, 100f, FlashColor = "#EF4444", FlashDuration = 600f)]
    public float turbineLoadTemperature = 65f;

    [BoxGroup("2. Nested Class Showcase")]
    public AuxiliaryGeneratorCell backupCell = new AuxiliaryGeneratorCell();

    [BoxGroup("3. Direct Collections Cascading")]
    [InfoBox("Milestone shockwaves radiate across individual collection rows as each element crosses defined boundaries.")]
    [ThresholdSpikeFlash(50f, 100f, 150f, FlashColor = "#EF4444", FlashDuration = 500f)]
    public float[] reactorZoneTemperatures = new float[] { 45f, 95f, 140f };

    [ThresholdSpikeFlash(25f, 50f, 75f, FlashColor = "#10B981", FlashDuration = 450f)]
    public List<int> subsystemBatteryPercentages = new List<int> { 20, 48, 70 };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Shockwave ripples fit seamlessly inside card and box grouping containers. |
| `[AnimatedProgressBar]` | Supported | Pairs with animated progress bars to emphasize milestone threshold crossings. |
| `[WarningStrobe]` | Stacking | Can be combined with warning strobes for escalating emergency alert sequences. |

### Collection Cascading Matrix

| Collection Type | Cascading Behavior | Presentation Mode |
| :--- | :---: | :--- |
| `float[]`, `int[]` | **Supported** | Individual element fields radiate flash ripples as their respective values cross milestone thresholds. |
| `List<float>`, `List<int>` | **Supported** | Dynamically attaches value tracking to list rows in reorderable UI Toolkit lists. |
| `AdvancedList<T>` | **Supported** | Full support with pagination, item insertion, and reordering. |
| `SerializableDictionary<K, V>` | **Supported** | Cascades to numeric values within key-value pair rows. |
| Nested `[Serializable]` Classes | **Supported** | Tracks nested member boundaries cleanly across serializable class instances. |

