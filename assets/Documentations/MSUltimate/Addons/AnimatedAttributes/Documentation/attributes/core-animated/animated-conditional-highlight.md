# [AnimatedConditionalHighlight]

> Triggers an attention-grabbing animated pulsing highlight background when a specified boolean condition method evaluates to true.

---

## 1. Overview & Value Proposition

**What it does:**
Monitors a custom boolean method callback at regular intervals (`CheckInterval`). When the condition returns `true`, it activates a rhythmic pulsing background glow (`HighlightColor`) behind the field, drawing the developer's immediate focus to critical states (e.g. low ammo, dangerous health thresholds, unsaved configs).

**The Problem:**
Static inspector warnings easily blend into busy components and get overlooked during rapid iteration or playtesting.

**The Solution:**
Add `[AnimatedConditionalHighlight]` to any field:
- **Dynamic Reactive Pulse:** Automatically pulses only when game state or field configuration warrants attention.
- **Configurable Speed & Color:** Fine-tune oscillation speed (`PulseSpeed`) and highlight hex color.
- **Interval Throttling:** Periodic evaluation (`CheckInterval = 500ms`) ensures negligible CPU overhead.
- **Clean Auto-Dismissal:** The pulsing animation stops cleanly the moment the condition returns `false`.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class TurretController : MonoBehaviour
{
    [AnimatedConditionalHighlight(nameof(IsAmmoDepleted), HighlightColor = "#FF000055", PulseSpeed = 2f)]
    public int currentAmmo = 0;

    private bool IsAmmoDepleted() => currentAmmo <= 0;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public AnimatedConditionalHighlightAttribute()
```

*Attribute initializes with default settings; configure properties via object initializer.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ConditionMethod` | `string` | `""` | Name of the boolean method invoked to trigger the highlight. |
| `HighlightColor` | `string` | `"#FF980044"` | Hex color string for the pulsing highlight background. |
| `PulseSpeed` | `float` | `1.5f` | Oscillation speed in cycles per second. |
| `CheckInterval` | `float` | `500f` | Evaluation interval in milliseconds between condition checks. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class ReactorCore : MonoBehaviour
{
    [Header("Core Temperature (Pulses Red on Overheat)")]
    [AnimatedConditionalHighlight(
        nameof(IsOverheating), 
        HighlightColor = "#e74c3c66", 
        PulseSpeed = 2.5f, 
        CheckInterval = 250f
    )]
    public float temperatureCelsius = 350f;

    public float criticalThreshold = 300f;

    private bool IsOverheating() => temperatureCelsius >= criticalThreshold;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Pulsing highlight renders smoothly inside group containers. |
| `[ShowIf]` | Supported | Condition checks pause automatically when the field is hidden. |
| Primary Drawers | Supported | Enhances primary drawers like sliders without interfering with input. |
