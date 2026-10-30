# [ComponentAuroraEffect]

> Renders a flowing Northern Lights aurora borealis color ribbon effect across the top or bottom of the component card.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentAuroraEffect]` generates an ethereal Northern Lights (Aurora Borealis) visual atmosphere across the header or footer of a component card. It projects multiple semi-transparent undulating color bands (`BandCount`, defaulting to 5) that cycle through three celestial colors (`Color1`, `Color2`, and `Color3`). Positioned along either the top or bottom edge (`Edge`), it can be rendered as a subtle foreground glow or tucked behind inspector controls (`Behind = true`). Operating with `PickingMode.Ignore`, it ensures that mouse selection and input fields remain fully responsive beneath the ambient effect.

**The Problem:**
Specialized gameplay systems—such as Arctic survival biomes, celestial spell schools, or cosmic inventory vaults—look identical to standard physics engines when viewed inside the default Unity Inspector. Without thematic environmental styling, tools fail to inspire technical artists and narrative designers.

**The Solution:**
Decorating themed components with `[ComponentAuroraEffect]`:
- **Multi-Band Atmospheric Ribbons:** Simulates layered atmospheric plasma curtains using graduated opacity and height stepping.
- **Three-Color Harmonic Palette:** Blends vibrant emerald, cyan, and violet wavelengths (`#00FF88`, `#4488FF`, `#AA44FF`) or custom hex palettes.
- **Top or Bottom Edge Anchoring:** Configurable via `WaveEdge` (`Top` or `Bottom`) to crown headers or illuminate footers.
- **Layer Stacking Flexibility:** Switch between foreground ambient haze (`Behind = false`, `BodyOverlay`) or soft background illumination (`Behind = true`, `ContentOverlay`).
- **Zero Input Interference:** Set to `PickingMode.Ignore`, allowing uninterrupted field clicks, slider drags, and text editing.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentAuroraEffect(Color1 = "#00FF88", Color2 = "#38BDF8", Color3 = "#A855F7", Height = 50f, Opacity = 0.25f)]
public class ArcticWeatherSystem : MonoBehaviour
{
    public float blizzardIntensity = 0.65f;
    public float ambientTemperatureCelsius = -18f;
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
public ComponentAuroraEffectAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color1` | `string` | `"#00FF88"` | Primary emerald/green aurora color stop. |
| `Color2` | `string` | `"#4488FF"` | Secondary blue/cyan aurora color stop. |
| `Color3` | `string` | `"#AA44FF"` | Tertiary purple/violet aurora color stop. |
| `BandCount` | `int` | `5` | Number of distinct ribbon layers rendered (clamped between 2 and 10). |
| `Height` | `float` | `40f` | Total vertical height in pixels allocated to the aurora wave. |
| `Speed` | `float` | `0.8f` | Animation flow speed multiplier. |
| `Opacity` | `float` | `0.2f` | Global transparency alpha of the aurora container (0.0 to 1.0). |
| `Edge` | `WaveEdge` | `WaveEdge.Top` | Screen edge where the ribbons originate (`WaveEdge.Top` or `WaveEdge.Bottom`). |
| `Behind` | `bool` | `false` | When true, renders behind inspector fields; when false, renders as a top overlay. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#38BDF8", Width = 1.5f, Radius = 8f)]
[ComponentBackground("#0B132B", BorderRadius = 8f, Padding = 10f)]
[ComponentAuroraEffect(Color1 = "#22D3EE", Color2 = "#818CF8", Color3 = "#C084FC", Height = 60f, Opacity = 0.3f, Behind = true)]
public class CelestialAstronomyDome : MonoBehaviour
{
    [Header("Observatory Instruments")]
    public float telescopeFocalLength = 1200f;
    public string celestialConstellationTarget = "Ursa Major";
    public bool isStarlightFilterActive = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Recommended pairing; dark backgrounds (`#0F172A`, `#0B132B`) make the translucent aurora bands stand out vividly. |
| **`[ComponentHeader]`** | High | Anchoring the aurora to `WaveEdge.Top` creates an ethereal halo effect directly behind or over the header bar. |
| **`[ComponentConstellations]`** | High | Stacks beautifully to create a full cosmic observatory card (aurora wave + twinkling starfield). |
| **Field Inputs & Sliders** | High | `PickingMode.Ignore` guarantees all underlying buttons, inputs, and toggles interact normally. |
