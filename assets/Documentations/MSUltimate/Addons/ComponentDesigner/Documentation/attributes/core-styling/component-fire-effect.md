# [ComponentFireEffect]

> Renders an animated fire flame effect with rising embers and three-tier color gradients along the edge of the component card.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentFireEffect]` brings fiery elemental aesthetics to component inspector windows. It simulates living fire along either the bottom or top boundary of a component card (`Edge = WaveEdge.Bottom` or `WaveEdge.Top`), animating flickering flame tongues that leap upward with fluid noise. The attribute features tri-color grading—incorporating hot ember red (`CoreColor`), fiery orange (`BaseColor`), and radiant tip yellow (`TipColor`). Users can adjust flame density (`FlameCount`), maximum height (`MaxHeight`), turbulence speed (`Speed`), transparency (`Opacity`), and layer depth (`Behind = false` $\to$ `BodyOverlay`, `Behind = true` $\to$ `ContentOverlay`).

**The Problem:**
Pyromancy spells, combustion engines, flamethrower controllers, and heat dissipation systems in games get buried in mundane inspector forms. Without distinctive visual cues, it's easy for developers to mistake fire hazard configurations for ordinary physics or combat scripts.

**The Solution:**
Decorating burning modules with `[ComponentFireEffect]`:
- **Three-Tier Thermal Grading:** Layers hot core embers (`#FF0000`), mid-level fire body (`#FF6600`), and flickering tips (`#FFCC00`) for genuine combustion visuals.
- **Turbulent Organic Flicker:** Uses harmonic sine waves and noise-driven heights to ensure flame tongues rise, curl, and dissipate without repetitive loops.
- **Top or Bottom Placement:** Position flames dancing along the card footer or crowning the card header via `WaveEdge`.
- **Transparent Click-Through:** Runs with `PickingMode.Ignore`, preserving immediate mouse responsiveness for all inspector fields.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentFireEffect(FlameCount = 24, MaxHeight = 30f, Speed = 2f, Opacity = 0.7f)]
public class PyromancerSpellbook : MonoBehaviour
{
    public float burnDamagePerSecond = 45f;
    public float igniteRadiusMeters = 6.5f;
    public float fuelConsumptionRate = 12f;
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
| **Component Slot** | `ContentOverlay` (if `Behind = true`) or `BodyOverlay` (if `Behind = false`) |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentFireEffectAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `FlameCount` | `int` | `20` | Number of animated flame tongue elements rendered along the border. |
| `MaxHeight` | `float` | `25f` | Maximum vertical flame leap height in pixels. |
| `BaseColor` | `string` | `"#FF6600"` | Hex color string for the mid flame body (warm orange). |
| `TipColor` | `string` | `"#FFCC00"` | Hex color string for the hottest flame tips (radiant yellow). |
| `CoreColor` | `string` | `"#FF0000"` | Hex color string for base ember coals (hot red). |
| `Speed` | `float` | `1.5f` | Animation flicker and leap velocity multiplier. |
| `Opacity` | `float` | `0.6f` | Transparency alpha of the flame layer (0.0 to 1.0). |
| `Edge` | `WaveEdge` | `WaveEdge.Bottom` | Edge placement (`WaveEdge.Bottom` or `WaveEdge.Top`). |
| `Behind` | `bool` | `false` | When true, renders behind inspector controls; when false, renders on top. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#EF4444", Width = 2f, Radius = 8f)]
[ComponentBackground("#1A0B0B", BorderRadius = 8f, Padding = 10f)]
[ComponentHeader("INFERNAL CRUCIBLE", Subtitle = "Molten Core Temperature Controller", BackgroundColor = "#2A0E0E", TitleColor = "#FEE2E2")]
[ComponentFireEffect(FlameCount = 28, MaxHeight = 28f, BaseColor = "#F97316", TipColor = "#FDE047", CoreColor = "#DC2626", Speed = 1.8f, Opacity = 0.65f, Edge = WaveEdge.Bottom, Behind = true)]
public class InfernalCrucible : MonoBehaviour
{
    [Header("Thermal State")]
    public float coreTemperatureKelvin = 1850f;
    public float heatExchangeEfficiency = 0.92f;
    public bool isEmergencyVentOpen = false;

    [Header("Combustion Settings")]
    public float oxygenInjectionRate = 34.5f;
    public float plasmaContainmentPsi = 420f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Deep soot black or obsidian red backgrounds dramatically heighten the radiance of orange-red fire. |
| **`[ComponentHeader]`** | High | Positioning flames along `WaveEdge.Bottom` forms an aesthetic furnace base underneath top headers. |
| **Inspector Controls** | High | `PickingMode.Ignore` ensures fire visualizers never obstruct numerical inputs or buttons. |
