# [ComponentSciFiHUD]

> Encases the component in a futuristic holographic heads-up display with neon targeting reticles, corner telemetry brackets, and coordinates.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentSciFiHUD]` wraps component controls inside an advanced holographic fighter cockpit or tactical visor interface. Injected into `ComponentSlot.BodyWrapper`, it frames the inspector with illuminated corner targeting reticles (`ShowReticles = true`), a live telemetry system tag (`TelemetryId = "HUD // SYS-01"`), and simulated navigational coordinates (`ShowCoordinates = true`). The entire shell radiates in customizable high-tech neon hues (`HudColor = "#00FFAA"`) over a subtle translucent cockpit backdrop (`BackgroundOpacity = 0.12f`).

**The Problem:**
Starship cockpits, combat mech telemetry hubs, sniper targeting sensors, and robotic visual subsystems lose their futuristic military atmosphere when edited in default gray inspector boxes. Developers tuning targeting offsets or heat dissipations miss the immersion of looking through an active helmet HUD.

**The Solution:**
Decorating tactical and futuristic entities with `[ComponentSciFiHUD]`:
- **Four-Corner Optical Reticles:** Precision angled corner brackets simulate holographic targeting visors and fighter flight displays.
- **Dynamic Telemetry Readouts:** Stamped system designations and coordinate lines impart an authentic military sci-fi aesthetic.
- **Vibrant Neon Laser Hues:** Tailor HUD lines to electric cyan, hazard amber, laser crimson, or tactical emerald.
- **Transparent Wrapper Mechanics:** Operates seamlessly as a `BodyWrapper`, wrapping fields cleanly without blocking clicks, sliders, or keyboard navigation.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentSciFiHUD(hudColor: "#00E5FF", telemetryId: "FIGHTER // AVIONICS-09")]
public class StarfighterTargetingComputer : MonoBehaviour
{
    public float targetLockRangeMeters = 4500f;
    public float missileSeekerConeDegrees = 35f;
    public int simultaneousTrackedTargets = 8;
    public bool isIFFInterrogatorActive = true;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ComponentDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Component Slot** | `BodyWrapper` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentSciFiHUDAttribute()
public ComponentSciFiHUDAttribute(string hudColor = "#00FFAA", string telemetryId = "HUD // SYS-01")
```

- `hudColor`: Hex color string representing the neon HUD wireframe, reticles, and text.
- `telemetryId`: Alphanumeric subsystem identifier displayed in the HUD frame header.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `HudColor` | `string` | `"#00FFAA"` | Hex color string for the holographic HUD line accents and reticles. |
| `TelemetryId` | `string` | `"HUD // SYS-01"` | System identification code string displayed in the HUD frame. |
| `ShowReticles` | `bool` | `true` | Whether to display four-corner targeting reticle brackets. |
| `ShowCoordinates` | `bool` | `true` | Whether to render simulated coordinate readouts along the frame border. |
| `BackgroundOpacity` | `float` | `0.12f` | Background container opacity for the holographic HUD tinted backing. |
| `Order` | `int` | `0` | Sequence sorting order within the target component slot. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentSciFiHUD(
    HudColor = "#38BDF8", 
    TelemetryId = "MECH // TITAN-CORE-V2", 
    ShowReticles = true, 
    ShowCoordinates = true, 
    BackgroundOpacity = 0.15f)]
public class TitanMechAvionicsController : MonoBehaviour
{
    [Header("Reactor & Core Temp")]
    [Range(0f, 1000f)] public float reactorCoreTemperatureK = 650f;
    public float plasmaExhaustFlowRate = 120.4f;

    [Header("Targeting & Ballistics")]
    public float railgunCapacitorChargePercent = 94.2f;
    public int remainingDepletedUraniumRounds = 450;
    public bool isAutoTargetingEngaged = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeaderButton]`** | High | Buttons integrate cleanly onto the HUD perimeter for quick diagnostic sweeps. |
| **`[ComponentHexShield]`** | High | Combine HUD reticles with defensive hexagonal forcefields for armored combat shields. |
| **Combat HUD Attributes** | High | Complements shield meters and animated radar displays from AnimatedAttributes. |
| **Inspector Controls** | High | Encapsulates all serialized properties without blocking clicks, drags, or scroll views. |
