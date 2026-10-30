# [ComponentNebula]

> Renders layered cosmic nebula clouds that drift smoothly across the component background with multi-color blending and parallax depth.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentNebula]` washes the component card in an atmospheric deep-space interstellar nebula. It simulates soft, drifting gaseous clouds across multiple parallax depth planes (`Layers`). Featuring a cosmic tri-color palette (`Color1`, `Color2`, `Color3`—defaulting to deep purple `#6A0DAD`, vivid pink `#FF1493`, and celestial blue `#1E90FF`), clouds slowly drift across the card canvas with gentle undulating scale variance (`MaxSize`, `Speed`). It defaults to a soft background layer (`Behind = true` $\to$ `ComponentSlot.ContentOverlay`) with subtle ambient opacity (`Opacity = 0.12f`), giving components a rich celestial vibe without compromising field visibility.

**The Problem:**
Astrophysics systems, galaxy map generators, void sorcery spellbooks, and space exploration components look flat and uninspired in standard Unity gray inspector boxes. Static text fails to capture the grandeur of the cosmos.

**The Solution:**
Decorating cosmic and sci-fi systems with `[ComponentNebula]`:
- **Multi-Layered Parallax Depth:** Stacks up to 8+ semi-transparent gaseous cloud puffs moving at independent drift vectors and rates.
- **Tri-Color Celestial Palette:** Smoothly blends between violet, magenta, and stellar blue for authentic cosmic photography visuals.
- **Subtle Drift Speed:** Drifts at a relaxing velocity (`Speed = 0.3f`), preventing distracting visual clutter during editing.
- **Background Default Layering:** Defaults to `Behind = true` with `PickingMode.Ignore`, guaranteeing completely unobscured mouse control.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentNebula(Color1 = "#7928CA", Color2 = "#FF0080", Color3 = "#0070F3", Layers = 10, MaxSize = 70f)]
public class GalacticWarpGateHandler : MonoBehaviour
{
    public string destinationGalaxySector = "Orion-Cygnus Arm";
    public float wormholeStability = 0.94f;
    public bool isHyperspaceTransitReady = true;
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
public ComponentNebulaAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color1` | `string` | `"#6A0DAD"` | Hex color string for primary nebula clouds (deep purple). |
| `Color2` | `string` | `"#FF1493"` | Hex color string for secondary cosmic clouds (deep magenta/pink). |
| `Color3` | `string` | `"#1E90FF"` | Hex color string for tertiary star clouds (celestial blue). |
| `Layers` | `int` | `8` | Total count of semi-transparent drifting cloud layers. |
| `MaxSize` | `float` | `60f` | Maximum cloud puff radius in pixels. |
| `Speed` | `float` | `0.3f` | Cloud drift and deformation velocity multiplier. |
| `Opacity` | `float` | `0.12f` | Global transparency alpha of the nebula effect (0.0 to 1.0). |
| `Behind` | `bool` | `true` | When true (default), renders behind inspector controls; when false, renders on top. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#8B5CF6", Width = 1.5f, Radius = 8f)]
[ComponentBackground("#0B0817", BorderRadius = 8f, Padding = 10f)]
[ComponentHeader("STAR SYSTEM ORCHESTRATOR", Subtitle = "Procedural Stellar Classification & Orbits", BackgroundColor = "#140E2A", TitleColor = "#EDE9FE")]
[ComponentNebula(Color1 = "#7C3AED", Color2 = "#DB2777", Color3 = "#2563EB", Layers = 10, MaxSize = 75f, Speed = 0.25f, Opacity = 0.16f, Behind = true)]
public class StarSystemOrchestrator : MonoBehaviour
{
    [Header("Host Star Data")]
    public string starCatalogDesignation = "HD-189733";
    public float stellarLuminositySolarUnits = 1.25f;
    public int orbitingPlanetaryBodies = 7;

    [Header("Cosmic Dust & Asteroids")]
    public float asteroidBeltDensity = 0.45f;
    public bool hasKuiperBeltRing = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Deep void black or cosmic navy backdrops enhance the ethereal glow of nebula gas. |
| **`[ComponentConstellations]`** | High | Layering constellation star lines over a nebula backdrop creates an authentic deep-space astrolabe aesthetic. |
| **Inspector Controls** | High | Defaults to `Behind = true` with `PickingMode.Ignore`, ensuring all standard Unity input controls remain completely responsive. |
