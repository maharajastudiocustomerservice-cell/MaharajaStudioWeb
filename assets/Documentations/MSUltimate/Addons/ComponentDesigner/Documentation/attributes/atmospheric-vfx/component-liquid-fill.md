# [ComponentLiquidFill]

> Renders an animated fluid liquid fill with sloshing wave ripples and adjustable container volume behind component fields.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentLiquidFill]` simulates a glass flask, chemical vat, or fuel reservoir directly behind inspector controls. Powered by UI Toolkit vector mathematics in `ComponentSlot.ContentOverlay`, it renders an animated fluid level filled to a specified percentage (`FillPercentage = 0.35f`, ranging from 0.1 to 0.9). Harmonic sine waves gently roll and slosh along the liquid surface meniscus (`SloshSpeed = 1.4f`, `WaveHeight = 6f`) with translucent fluid tints (`LiquidColor = "#3B82F655"`).

**The Problem:**
Potion brewing cauldrons, alchemical vats, spaceship fuel reserves, and hazardous acid conduits look sterile in default inspector windows. Developers lack an intuitive, visual sense of tank capacity, fluid viscosity, and reservoir volume during parameter balancing.

**The Solution:**
Decorating liquid container and alchemy systems with `[ComponentLiquidFill]`:
- **Animated Meniscus Waves:** Multi-frequency sine ripples simulate realistic sloshing and hydrodynamic surface tension.
- **Configurable Tank Fill Level:** Adjust fill percentages from 10% to 90% to match reservoir capacity or low-fluid danger thresholds.
- **Vibrant Fluid Coloration:** Supports translucent hex colors (with alpha channel) for healing elixirs, toxic sludge, mana water, or rocket propellant.
- **Non-Obtrusive Overlay:** Anchored to `ContentOverlay` with `PickingMode.Ignore`, ensuring that text inputs and numeric sliders remain fully interactable without interference.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentLiquidFill(liquidColor: "#10B98155", fillPercentage: 0.5f, sloshSpeed: 1.2f)]
public class AlchemicalCauldronTank : MonoBehaviour
{
    public float fluidCapacityLiters = 250f;
    public float boilTemperatureCelsius = 98.4f;
    public string primaryReagent = "Nightshade Belladonna";
    public bool isStirringPaddleActive = true;
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
public ComponentLiquidFillAttribute()
public ComponentLiquidFillAttribute(string liquidColor = "#3B82F655", float fillPercentage = 0.35f, float sloshSpeed = 1.4f)
```

- `liquidColor`: Hex color string with alpha channel defining the fluid color and translucency.
- `fillPercentage`: Vertical fill ratio of the component card (clamped between `0.1f` and `0.9f`).
- `sloshSpeed`: Frequency multiplier governing the animated surface ripple oscillations.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `LiquidColor` | `string` | `"#3B82F655"` | Hex color string (with 8-digit alpha) defining fluid hue and transparency. |
| `FillPercentage` | `float` | `0.35f` | Height percentage of the component card occupied by liquid (0.1f to 0.9f). |
| `SloshSpeed` | `float` | `1.4f` | Sloshing wave speed multiplier across the liquid meniscus. |
| `WaveHeight` | `float` | `6f` | Peak-to-trough wave amplitude in pixels along the surface. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#7C3AED", Width = 1.5f, Radius = 8f)]
[ComponentBackground("#160E2A", BorderRadius = 8f, Padding = 10f)]
[ComponentHeader("ARCANE MANA CONDENSER", Subtitle = "Etheric Reservoir Stabilization Matrix", BackgroundColor = "#251644", TitleColor = "#E9D5FF")]
[ComponentLiquidFill(LiquidColor = "#8B5CF666", FillPercentage = 0.65f, SloshSpeed = 1.6f, WaveHeight = 8f)]
public class ArcaneManaCondenser : MonoBehaviour
{
    [Header("Reservoir Metrics")]
    public float currentManaVolumeUnits = 6500f;
    public float maxManaCapacityUnits = 10000f;
    public float condensationFluxPerSec = 45f;

    [Header("Safety Valves")]
    [Range(0f, 1f)]
    public float etherPurityIndex = 0.98f;
    public bool isEmergencyOverflowVenting = false;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Dark backdrops allow translucent fluids to simulate glowing radioactive, magical, or chemical solutions. |
| **`[ComponentHeader]`** | High | Displays container names and status indicators above the sloshing fluid level. |
| **`[ComponentParticles]`** | High | Stacking rising bubbles or vapor particles above the liquid line creates an authentic boiling vat effect. |
| **Inspector Controls** | High | `PickingMode.Ignore` ensures complete click transparency for all inspector controls. |
