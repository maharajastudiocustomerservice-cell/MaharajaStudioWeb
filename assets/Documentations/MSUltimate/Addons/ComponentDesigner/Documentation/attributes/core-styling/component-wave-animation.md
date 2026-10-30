# [ComponentWaveAnimation]

> Renders animated undulating sinusoidal color wave bands along the top or bottom edge of the component card with dual-tone gradient blending.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentWaveAnimation]` brings fluid undulating wave ribbon motion to component borders. Docked to either the bottom or top boundary (`Edge = WaveEdge.Bottom` or `WaveEdge.Top`), it animates smooth sine wave curves traveling along the border edge. Composed of multiple curve segments (`Segments = 16`), it oscillates smoothly between vertical peaks (`Height = 6f`) at a configurable speed (`Speed`). Featuring dual-color gradient transitions (`Color` and `SecondaryColor`, defaulting to vibrant cyan `#4FC3F7` and deep azure `#0288D1`), transparency controls (`Opacity = 0.6f`), and layer ordering (`Behind = false` $\to$ `BodyOverlay`), it imparts fluid energy to ocean, fluid, and audio components.

**The Problem:**
Standard component borders are rigid and static rectangles. Marine systems, liquid dispensers, sound frequency filters, and coastal environments appear flat without organic undulating wave motion along card margins.

**The Solution:**
Decorating liquid and wave systems with `[ComponentWaveAnimation]`:
- **Continuous Undulating Sine Wave:** Animates harmonic sinusoidal wave crests traveling continuously along the border edge.
- **Dual-Hue Color Gradient:** Blends between primary crest highlights (`Color`) and deep trough accents (`SecondaryColor`).
- **Configurable Wave Geometry:** Tune wave peak height (`Height = 6f`), curve subdivision smoothness (`Segments = 16`), and motion tempo (`Speed`).
- **Input Transparency:** Absolutely positioned with `PickingMode.Ignore`, preserving full mouse responsiveness for all inspector fields.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentWaveAnimation(Color = "#38BDF8", SecondaryColor = "#0369A1", Height = 8f, Speed = 1.4f, Edge = WaveEdge.Bottom)]
public class OceanTideSimulationManager : MonoBehaviour
{
    public float highTideHeightMeters = 3.2f;
    public float tidalPeriodHours = 12.4f;
    public bool isLunarGravityApplied = true;
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
public ComponentWaveAnimationAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color` | `string` | `"#4FC3F7"` | Hex color string for wave crest highlights. |
| `SecondaryColor` | `string` | `"#0288D1"` | Hex color string for wave trough accents. |
| `Height` | `float` | `6f` | Peak vertical wave amplitude displacement in pixels. |
| `Segments` | `int` | `16` | Number of polygonal subdivisions used to render smooth curve waves. |
| `Speed` | `float` | `1f` | Wave crest propagation velocity multiplier. |
| `Opacity` | `float` | `0.6f` | Transparency alpha of the wave animation (0.0 to 1.0). |
| `Edge` | `WaveEdge` | `WaveEdge.Bottom` | Edge placement (`WaveEdge.Bottom` or `WaveEdge.Top`). |
| `Behind` | `bool` | `false` | When true, renders behind inspector controls; when false, renders on top. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#0284C7", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#071926", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("COASTAL HYDRAULICS CORE", Subtitle = "Fluid SPH Solver & Shoreline Breaker", BackgroundColor = "#0B2B40", TitleColor = "#E0F2FE")]
[ComponentWaveAnimation(Color = "#38BDF8", SecondaryColor = "#0284C7", Height = 8f, Segments = 20, Speed = 1.5f, Opacity = 0.65f, Edge = WaveEdge.Bottom, Behind = true)]
public class CoastalHydraulicsCore : MonoBehaviour
{
    [Header("Fluid Particle Dynamics")]
    public int sphParticleCount = 8000;
    public float fluidRestDensity = 998.2f;
    public float surfaceTensionCoefficient = 0.072f;

    [Header("Shoreline Dissipation")]
    public float seabedFrictionFactor = 0.45f;
    public bool enableWhitewaterFoamPass = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Deep aquatic blue backdrops provide strong visual contrast for rolling wave crests. |
| **`[ComponentHeader]`** | High | Anchoring the wave to `WaveEdge.Top` creates an animated liquid underline beneath header cards. |
| **Inspector Controls** | High | `PickingMode.Ignore` ensures complete click-through transparency for all inspector controls. |
