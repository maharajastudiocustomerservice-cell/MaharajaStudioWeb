# [ComponentQuantumTunnel]

> Renders an animated hyperspace quantum star-tunnel with perspective light streaks radiating outward across the component card.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentQuantumTunnel]` transports the component inspector into a high-velocity hyperspace jump. Driven by UI Toolkit vector rendering in `ComponentSlot.ContentOverlay`, it projects radiating perspective light streaks (`StreakCount = 36`) streaming outward from a central vanishing point at adjustable warp velocities (`WarpSpeed = 1.8f`). The streaks radiate in luminous indigo, cyan, or violet spectrums (`Color = "#818CF8"`) with delicate background translucency (`Opacity = 0.25f`).

**The Problem:**
FTL hyperdrives, warp fold engines, quantum entanglers, and wormhole transit stabilizers lack cosmic dynamism when viewed on flat gray Unity inspector panels. Developers lose the visual thrill of relativistic spacetime travel while tweaking jump calculations and fuel expenditure curves.

**The Solution:**
Decorating interstellar and relativistic travel modules with `[ComponentQuantumTunnel]`:
- **Radiating Perspective Warp Streaks:** Simulates 3D relativistic motion with accelerating light filaments expanding outward towards inspector margins.
- **Dynamic Warp Velocities:** Scale travel speed from gentle interstellar drift to maximum FTL hyperspace velocity.
- **Cosmic Indigo Spectrum:** Vibrant indigo and ultraviolet light rays evoke quantum sub-space tunneling and dimension hopping.
- **Complete Interaction Transparency:** Injected into `ContentOverlay` with `PickingMode.Ignore`, ensuring that text inputs, toggles, and buttons remain 100% responsive.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentQuantumTunnel(color: "#818CF8", streakCount: 36, warpSpeed: 1.8f)]
public class HyperspaceFoldDrive : MonoBehaviour
{
    public float warpFactor = 8.4f;
    public float antimatterInjectionRate = 42.5f;
    public float tachyonFieldCoherence = 0.99f;
    public bool isWarpBubbleStable = true;
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
| **Component Slot** | `ContentOverlay` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentQuantumTunnelAttribute()
public ComponentQuantumTunnelAttribute(string color = "#818CF8", int streakCount = 36, float warpSpeed = 1.8f)
```

- `color`: Hex color string representing the radiating star-streak light beam emission.
- `streakCount`: Total number of perspective hyperspace light filaments to simulate.
- `warpSpeed`: Velocity multiplier governing how quickly streaks travel outward from the center.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color` | `string` | `"#818CF8"` | Hex color string for the perspective star streaks and energy rays. |
| `StreakCount` | `int` | `36` | Total count of radiating hyperspace light filaments. |
| `WarpSpeed` | `float` | `1.8f` | Outward radial velocity multiplier for warp acceleration. |
| `Opacity` | `float` | `0.25f` | Overall background opacity multiplier of the tunnel effect. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#4F46E5", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#0A0B1E", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("TACHYON SUB-SPACE ENTANGLER", Subtitle = "Trans-Dimensional Gateway Coordinates", BackgroundColor = "#141538", TitleColor = "#C7D2FE")]
[ComponentQuantumTunnel(Color = "#6366F1", StreakCount = 42, WarpSpeed = 2.2f, Opacity = 0.28f)]
public class TachyonGatewayController : MonoBehaviour
{
    [Header("Wormhole Telemetry")]
    public string targetGalacticSector = "SECTOR-EPSILON-9";
    public double eventHorizonRadiusMeters = 840.5;
    public float gravitationalLensingArcSec = 14.8f;

    [Header("Quantum Containment")]
    [Range(0f, 100f)]
    public float exoticMatterStabilityPercent = 97.4f;
    public bool isSingularityGateOnline = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Deep void black or cosmic navy cards (`#0A0B1E`) provide deep contrast for high-speed light streaks. |
| **`[ComponentHeader]`** | High | Complements sci-fi warp console titles and starship navigation headers. |
| **`[ComponentBadge]`** | High | Pair with status badges like "FTL READY" or "WARP 9.2" for maximum sci-fi immersion. |
| **Inspector Controls** | High | `PickingMode.Ignore` ensures complete click-through capability for all inspector fields. |
