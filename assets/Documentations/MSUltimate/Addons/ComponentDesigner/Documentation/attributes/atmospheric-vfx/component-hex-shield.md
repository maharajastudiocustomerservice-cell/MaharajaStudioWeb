# [ComponentHexShield]

> Renders an animated honeycomb hexagonal forcefield shield with pulsing energy ripples across the component background.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentHexShield]` injects an animated high-tech deflector barrier into the component inspector. Executed via UI Toolkit vector painters in `ComponentSlot.ContentOverlay`, it tessellates an energetic honeycomb hexagonal grid (`HexSize = 14f`) across the inspector card. Harmonic energy ripples propagate outward through the hexagonal cells at an adjustable frequency (`PulseSpeed = 1.2f`), radiating vibrant forcefield energy (`ShieldColor = "#00E5FF"`) at a subtle background alpha (`Opacity = 0.22f`).

**The Problem:**
Starship deflector arrays, energy barrier generators, mech kinetic shielding, and cyberpunk firewall subroutines feel static and inert when represented by basic gray Unity inspector forms. Designers miss the reactive energetic aura of an active defensive barrier during combat balance passes.

**The Solution:**
Decorating barrier and defensive shield systems with `[ComponentHexShield]`:
- **Procedural Honeycomb Tessellation:** Generates mathematical hexagonal forcefield geometry scaled smoothly across all inspector panel dimensions.
- **Dynamic Energy Ripple Propagation:** Sine-wave ripples cascade across the hex cells to evoke an active energy field absorbing micro-impacts.
- **Configurable Defensive Hue:** Customize hex wireframes for electric cyan deflector screens, solar amber kinetic shields, or crimson overload barriers.
- **Complete Click-Through:** Runs in `ContentOverlay` with `PickingMode.Ignore`, ensuring that text inputs, toggles, and dropdown menus remain 100% responsive.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentHexShield(shieldColor: "#00E5FF", hexSize: 14f, pulseSpeed: 1.2f)]
public class KineticBarrierGenerator : MonoBehaviour
{
    public float maximumShieldCapacityJoules = 5000f;
    public float rechargeRatePerSecond = 250f;
    public float deflectionDeflectionEfficiency = 0.88f;
    public bool isOvercharged = false;
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
public ComponentHexShieldAttribute()
public ComponentHexShieldAttribute(string shieldColor = "#00E5FF", float hexSize = 14f, float pulseSpeed = 1.2f)
```

- `shieldColor`: Hex color string representing the forcefield grid hue (e.g., `#00E5FF` for Cyan, `#F59E0B` for Amber).
- `hexSize`: Radius and side length in pixels of individual hexagonal cells.
- `pulseSpeed`: Rate multiplier governing the propagating energy ripple waves.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ShieldColor` | `string` | `"#00E5FF"` | Hex color string for the hexagonal honeycomb grid lines and glow. |
| `HexSize` | `float` | `14f` | Radius and dimensions in pixels for each individual honeycomb cell. |
| `PulseSpeed` | `float` | `1.2f` | Speed multiplier for propagating radial energy ripple waves. |
| `Opacity` | `float` | `0.22f` | Translucency alpha multiplier of the forcefield background layer. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#0284C7", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#03131F", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("TITAN DREADNOUGHT DEFLECTOR MATRIX", Subtitle = "Primary Bow Shield Harmonizer", BackgroundColor = "#062338", TitleColor = "#BAE6FD")]
[ComponentHexShield(ShieldColor = "#38BDF8", HexSize = 16f, PulseSpeed = 1.5f, Opacity = 0.25f)]
public class StarshipDeflectorMatrix : MonoBehaviour
{
    [Header("Field Dynamics")]
    public float shieldHitPoints = 12500f;
    public float plasmaAbsorptionRatio = 0.92f;
    public float phaseHarmonicFrequencyThz = 440.5f;

    [Header("Coolant & Overload")]
    [Range(0f, 100f)]
    public float capacitorHeatPercentage = 34.2f;
    public bool isEmergencyFluxDumpReady = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Deep navy or midnight black backgrounds (`#03131F`) make cyan and emerald hex lattices glow intensely. |
| **`[ComponentHeader]`** | High | Fits naturally underneath sci-fi military command and capital ship headers. |
| **Combat HUD Attributes** | High | Pairs seamlessly with animated shield gauges and recharge bars. |
| **Inspector Controls** | High | `PickingMode.Ignore` ensures zero disruption to numeric fields, sliders, and object references. |
