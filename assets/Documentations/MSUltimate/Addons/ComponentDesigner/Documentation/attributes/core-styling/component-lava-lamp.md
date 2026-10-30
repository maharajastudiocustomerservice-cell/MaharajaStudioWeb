# [ComponentLavaLamp]

> Renders organic floating blob elements that drift and pulse in size across the component card, creating a mesmerizing vintage lava lamp ambient motion.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentLavaLamp]` introduces smooth, organic ambient motion into Unity inspector cards. Simulating viscous thermal convection fluid dynamics, it animates smooth floating circular blobs drifting across the card background. The blobs smoothly pulse between minimum and maximum diameters (`MinSize`, `MaxSize`) and interpolate across dual complementary colors (`Color1` and `Color2`). By default, it operates as a subtle backdrop (`Behind = true` $\to$ `ComponentSlot.ContentOverlay`) with low opacity (`Opacity = 0.15f`) and relaxing drift velocity (`Speed = 0.5f`), delivering visual life without drawing excessive attention away from work.

**The Problem:**
Static inspector forms for alchemy cauldrons, fluid simulators, organic biomass systems, or chill lo-fi ambient audio nodes feel rigid and artificial. Developers configuring viscous fluid logic lack tactile ambient feedback.

**The Solution:**
Decorating fluid and biological components with `[ComponentLavaLamp]`:
- **Organic Harmonic Convection:** Uses compound sinusoidal motion to simulate floating, colliding, and rising blobs that never move mechanically.
- **Dual-Hue Fluid Blending:** Interleaves two customizable colors (defaulting to coral pink `#FF6B6B` and soft turquoise `#4ECDC4`) for rich chromatic warmth.
- **Dynamic Size Breathing:** Blobs continually morph in size between `MinSize` and `MaxSize` as they drift.
- **Unobtrusive Background Default:** Defaults to `Behind = true` and `Opacity = 0.15f` with `PickingMode.Ignore`, ensuring zero interference with developer workflows.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentLavaLamp(Color1 = "#EC4899", Color2 = "#8B5CF6", Count = 8, MaxSize = 24f, Speed = 0.6f)]
public class AlchemicalCauldronBrew : MonoBehaviour
{
    public float fluidViscosity = 1.8f;
    public float brewingTemperatureCelsius = 92.5f;
    public int activeReagentCount = 5;
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
public ComponentLavaLampAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color1` | `string` | `"#FF6B6B"` | Hex color string for primary fluid blobs (warm coral). |
| `Color2` | `string` | `"#4ECDC4"` | Hex color string for secondary fluid blobs (turquoise). |
| `Count` | `int` | `6` | Total count of floating fluid blob elements. |
| `MaxSize` | `float` | `20f` | Maximum blob diameter in pixels during pulse peaks. |
| `MinSize` | `float` | `8f` | Minimum blob diameter in pixels during pulse troughs. |
| `Speed` | `float` | `0.5f` | Drift and breathing cycle velocity multiplier. |
| `Opacity` | `float` | `0.15f` | Transparency alpha of the fluid blobs (0.0 to 1.0). |
| `Behind` | `bool` | `true` | When true (default), renders behind inspector controls; when false, renders on top. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#14B8A6", Width = 1.5f, Radius = 8f)]
[ComponentBackground("#071D1B", BorderRadius = 8f, Padding = 10f)]
[ComponentHeader("SLIME REPLICATION CHAMBER", Subtitle = "Bio-Organic Growth & Fluid Dynamics", BackgroundColor = "#0B2E2A", TitleColor = "#CCFBF1")]
[ComponentLavaLamp(Color1 = "#2DD4BF", Color2 = "#A7F3D0", Count = 8, MaxSize = 26f, MinSize = 10f, Speed = 0.45f, Opacity = 0.2f, Behind = true)]
public class SlimeReplicationChamber : MonoBehaviour
{
    [Header("Organism Growth")]
    public float biomassMassKg = 14.8f;
    public float cellularMitosisRate = 0.08f;
    public bool isNutrientFeedActive = true;

    [Header("Chamber Conditions")]
    public float gelatinousDensity = 1.35f;
    public float phAcidityLevel = 6.8f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Deep obsidian or dark aquatic backgrounds create a glowing lantern aesthetic. |
| **`[ComponentHeader]`** | High | Floating blobs drift softly behind the fields below a structured header bar. |
| **Inspector Controls** | High | Defaults to `Behind = true` with `PickingMode.Ignore`, providing seamless click-through for all UI controls. |
