# [HeartbeatAlert]

> Animates a double-pulse heartbeat scale and red warning glow when vital numeric resources drop below critical safety thresholds.

---

## 1. Overview & Value Proposition

**What it does:**
`[HeartbeatAlert]` provides an urgent, physical warning cadence whenever a numeric resource (health, battery, oxygen, shield) drops below `CriticalThreshold`. It simulates a biological double-pulse cardiac heartbeat (`lub-dub`) through rapid micro-scale contractions (`ScaleBump`) and synchronized crimson vascular glow pulses (`GlowColor`), cycling at an authentic beats-per-minute cadence (`BPM`).

**The Problem:**
When balancing survival mechanics, roguelikes, or horror games, designers easily miss that initial health setups or enemy damage tuning leaves the player in immediate danger upon spawning. Static warning labels fail to deliver visceral urgency.

**The Solution:**
Decorating vital resource properties with `[HeartbeatAlert]`:
- **Biological Double-Pulse Rhythm:** Renders a realistic anatomical heartbeat rhythm that instantly triggers urgency.
- **Dynamic Threshold Trigger:** Dormant during healthy states; automatically awakens the instant values dip below `CriticalThreshold`.
- **Configurable Cadence & Color:** Fine-tune tempo via `BPM`, accent color via `GlowColor`, and scale pulse strength via `ScaleBump`.
- **Low-Overhead UI Toolkit Scheduling:** Automatically deschedules ticking timers when above threshold or hidden, consuming zero overhead during normal operation.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class PlayerVitality : MonoBehaviour
{
    [HeartbeatAlert(criticalThreshold: 20f, bpm: 80f)]
    public float currentHealth = 15f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any numeric serializable field or property (`float`, `int`, etc.), numeric collections (`float[]`, `int[]`, `List<float>`) |
| **Collection Cascading** | Yes (`ICollectionElementAttribute`) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public HeartbeatAlertAttribute(float criticalThreshold = 25f, float bpm = 75f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `criticalThreshold` | `float` | `25f` | Numeric value threshold below which the heartbeat animation activates. |
| `bpm` | `float` | `75f` | Beats per minute controlling pulse frequency and cardiac cadence. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `CriticalThreshold` | `float` | `25f` | Value threshold below which the heartbeat alert triggers. |
| `BPM` | `float` | `75f` | Heartbeat pulse cadence in beats per minute. |
| `GlowColor` | `string` | `"#EF4444"` | Hex color string for the pulsing vascular warning glow. |
| `ScaleBump` | `float` | `1.08f` | Peak scale multiplier reached during the cardiac contraction pulse. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class SurvivalSuitTelemetry : MonoBehaviour
{
    [Header("Life Support Systems")]
    [HeartbeatAlert(
        criticalThreshold: 25f, 
        bpm: 90f, 
        GlowColor = "#DC2626", 
        ScaleBump = 1.10f
    )]
    public float oxygenReservePercentage = 18f;

    [Header("Reactor Coolant Fluid")]
    [HeartbeatAlert(criticalThreshold: 15f, bpm: 110f, GlowColor = "#EA580C")]
    public float emergencyCoolantLevel = 10f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Pulsing container scales gently without overlapping outer layout borders. |
| `[AnimatedProgressBar]` | Supported | Pairs with progress bars to turn standard bars into emergency distress gauges. |
| `[EditorSoundEffect]` | Stacking | Triggers synchronized warning tones or heartbeat audio pulses on critical threshold entry. |
| Direct Collections | Supported | Cascades heartbeat pulse and warning glow onto individual element slots dropping below threshold across `float[]`, `int[]`, and `List<float>` via `ICollectionElementAttribute`. |
