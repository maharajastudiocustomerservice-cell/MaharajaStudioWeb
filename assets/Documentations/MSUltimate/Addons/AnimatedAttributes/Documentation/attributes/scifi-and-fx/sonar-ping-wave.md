# [SonarPingWave]

> Emits periodic expanding circular sonar rings across the inspector field with a fading phosphor trail to visualize radar pulses.

---

## 1. Overview & Value Proposition

**What it does:**
`[SonarPingWave]` overlays active acoustic sonar pulses over inspector properties. Using UI Toolkit's 2D vector painter (`MeshGenerationContext.painter2D`), it emits expanding circular wavefronts (`painter.Arc`) from the center of the element that expand outward to 60% of the container's width. As the wave propagates, its stroke alpha fades gracefully from 0.6 down to zero over `PingDuration` ms, recurring periodically at every `PingInterval` seconds in an acoustic phosphor hue (`SonarColor`).

**The Problem:**
Underwater exploration games, acoustic stealth mechanics, deep-sea submarine games, or medical ultrasound devices often require tuning pulse frequencies, echo delays, and detection radii. In the editor, adjusting these values feels detached from the wave-propagation physics they represent.

**The Solution:**
Decorating acoustic, sonar, or echolocation variables with `[SonarPingWave]`:
- **Expanding Circular Wavefront:** Generates continuous radial sonar ripples centered across the field.
- **Organic Phosphor Decay:** Smoothly fades the stroke intensity as the wave reaches maximum expansion radius.
- **Configurable Pulse Tempo:** Fine-tune interval cadence (`PingInterval`) and wave travel duration (`PingDuration`).
- **Non-Obtrusive Background Overlay:** Rendered with `PickingMode.Ignore` over an overflow-hidden canvas, ensuring text input remains completely unaffected.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class SubmarineSonar : MonoBehaviour
{
    [SonarPingWave(interval: 2.5f, sonarColor: "#10B981")]
    public float acousticPulseFrequencyHz = 440f;
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
public SonarPingWaveAttribute(float interval = 3.0f, string sonarColor = "#10B981")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `interval` | `float` | `3.0f` | Interval between consecutive sonar ping wave emissions in seconds. |
| `sonarColor` | `string` | `"#10B981"` | Hex color string for the expanding circular sonar wave rings. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `PingInterval` | `float` | `3.0f` | Time between sonar ping emissions in seconds. |
| `SonarColor` | `string` | `"#10B981"` | Hex color string of the expanding sonar wave rings (defaults to Emerald). |
| `PingDuration` | `float` | `1200f` | Wave expansion and fadeout duration in milliseconds. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class DeepSeaExplorerTelemetry : MonoBehaviour
{
    [Header("Active Echolocation")]
    [SonarPingWave(
        interval: 2.0f, 
        sonarColor: "#06B6D4", 
        PingDuration = 1400f
    )]
    public float sonarBathymetryDepthMeters = 3800f;

    [Header("Passive Hydrophone Listening")]
    [SonarPingWave(interval: 4.5f, sonarColor: "#F59E0B")]
    public float ambientHydrophoneDecibels = 62.5f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Expanding sonar rings clip cleanly to group layout edges without leaking. |
| `[ScanningRadar]` | Stacking | Pairs with circular scanning radar scopes for complete maritime detection consoles. |
| `[ReadOnly]` | Supported | Accentuates read-only depth gauges and hydrophone sensors with rhythmic pulses. |
