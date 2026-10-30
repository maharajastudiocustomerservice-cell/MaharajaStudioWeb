# [FloatUpDeltaNumber]

> Spawns floating RPG combat-style delta text (+/- change) that drifts upward and fades out whenever a numeric property mutates.

---

## 1. Overview & Value Proposition

**What it does:**
`[FloatUpDeltaNumber]` introduces floating damage and healing numbers directly into the Unity Inspector. Whenever the monitored numeric field or property changes, the attribute calculates the mathematical difference ($\Delta$), creates an animated floating number badge formatted as `+N` or `-N`, and floats it upward (`FloatDistance`) while fading over a smooth curve (`Duration`).

**The Problem:**
While adjusting combat damage, experience point gains, gold economies, or stamina curves in the inspector, it is difficult to perceive the exact delta between the old value and the newly entered or modified value. Designers frequently lose track of how much an attribute was bumped.

**The Solution:**
Decorating numeric fields with `[FloatUpDeltaNumber]`:
- **Instant Delta Readout:** Automatically displays the signed arithmetic difference (`+15`, `-500`) the microsecond a change occurs.
- **Color-Coded Semantic Polarity:** Distinguishes gains and losses with distinct customizable tints (`PositiveColor` and `NegativeColor`).
- **Smooth RPG Drift Animation:** Floats upward smoothly by a configurable pixel distance (`FloatDistance`) before dissolving.
- **Zero Editor Latency:** Built on top of UI Toolkit transient visual elements, bypassing IMGUI layout recalculations and garbage generation.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class CharacterEconomy : MonoBehaviour
{
    [FloatUpDeltaNumber(positiveColor: "#10B981", negativeColor: "#EF4444")]
    public int goldCoins = 1500;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any numeric serializable field or property (`int`, `float`, `double`, `long`, etc.), numeric collections (`int[]`, `List<float>`) |
| **Collection Cascading** | Yes (`ICollectionElementAttribute`) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public FloatUpDeltaNumberAttribute(string positiveColor = "#10B981", string negativeColor = "#EF4444")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `positiveColor` | `string` | `"#10B981"` | Hex color string for positive numeric increases (`+Delta`). |
| `negativeColor` | `string` | `"#EF4444"` | Hex color string for negative numeric decreases (`-Delta`). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `PositiveColor` | `string` | `"#10B981"` | Hex color string used when the value increases. |
| `NegativeColor` | `string` | `"#EF4444"` | Hex color string used when the value decreases. |
| `FloatDistance` | `float` | `25f` | Upward vertical drift distance in pixels before full fade. |
| `Duration` | `float` | `700f` | Total lifetime in milliseconds of the floating number animation. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class RPGCombatStats : MonoBehaviour
{
    [Header("Health Pool")]
    [FloatUpDeltaNumber(
        positiveColor: "#22C55E", 
        negativeColor: "#DC2626", 
        FloatDistance = 32f, 
        Duration = 850f
    )]
    public float currentHealth = 450f;

    [Header("Mana Points")]
    [FloatUpDeltaNumber(positiveColor: "#38BDF8", negativeColor: "#64748B")]
    public float currentMana = 120f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[ImpactRecoil]` | Stacking | Pairs with impact recoil to deliver both kinetic recoil kicks and numerical floating deltas. |
| `[AnimatedProgressBar]` | Supported | Floats change deltas directly above animated progress gauges. |
| `[BoxGroup]` | Supported | Drifting text renders above group containers without clipping boundaries. |
| Direct Collections | Supported | Cascades floating +/- delta indicators to individual element rows across `int[]`, `float[]`, and `List<T>` via `ICollectionElementAttribute`. |
