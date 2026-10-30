# [ComponentBioluminescence]

> Renders drifting and pulsing bioluminescent deep-sea organisms across the component card background with fluid organic motion.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentBioluminescence]` immerses the component inspector in an ethereal deep-sea ambiance. Operating via UI Toolkit vector painters in `ComponentSlot.ContentOverlay`, it renders an animated colony of floating luminous plankton organisms (`OrganismCount = 18`, clamped between 8 and 30 for performance). Organisms drift gracefully across the card surface with fluid noise (`DriftSpeed = 0.5f`), while pulsing their luminescence with harmonic breathing rhythms (`PulseRate = 1.2f`). Developers can customize organism glow hue (`GlowColor`, defaulting to cyan `#06B6D4`), colony density, and motion tempo.

**The Problem:**
Deep-sea creatures, alien flora, fungal spore ecosystems, and enchanted oceanic artifacts look lifeless in standard flat gray Unity inspector panels. Developers miss the mysterious underwater atmosphere during script tuning.

**The Solution:**
Decorating biological and oceanic systems with `[ComponentBioluminescence]`:
- **Fluid Organic Drift:** Simulates underwater micro-currents with organic drifting velocities across all organism nodes.
- **Harmonic Luminescence Breathing:** Each organism pulses independently in luminance and radius based on individual phase offsets.
- **Configurable Colony Density:** Scale organism count between 8 and 30 nodes with high editor performance.
- **Background Layer Default:** Placed in `ContentOverlay` with `PickingMode.Ignore`, ensuring all standard Unity controls remain fully interactable.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBioluminescence(glowColor: "#22D3EE", organismCount: 22, driftSpeed: 0.6f)]
public class AbyssalFloraSporeGenerator : MonoBehaviour
{
    public float sporeEmissionRate = 15f;
    public float illuminationRadiusMeters = 8.5f;
    public bool isPhosphorescentFloraMature = true;
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
public ComponentBioluminescenceAttribute()
public ComponentBioluminescenceAttribute(string glowColor = "#06B6D4", int organismCount = 18, float driftSpeed = 0.5f)
```

- `glowColor`: Hex color string for the bioluminescent emission glow.
- `organismCount`: Total count of drifting organisms (clamped between 8 and 30).
- `driftSpeed`: Fluid velocity multiplier governing organic drift.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `GlowColor` | `string` | `"#06B6D4"` | Hex color string for organism luminescent glow. |
| `OrganismCount` | `int` | `18` | Total count of animated organisms (clamped 8–30 for editor performance). |
| `DriftSpeed` | `float` | `0.5f` | Fluid drift velocity multiplier. |
| `PulseRate` | `float` | `1.2f` | Pulsing luminance oscillation rate multiplier. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#0891B2", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#04131A", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("DEEP TRENCH BIOMASS HARVESTER", Subtitle = "Abyssal Extraction & Symbiosis Matrix", BackgroundColor = "#07202B", TitleColor = "#CFFAFE")]
[ComponentBioluminescence(GlowColor = "#06B6D4", OrganismCount = 20, DriftSpeed = 0.45f, PulseRate = 1.3f)]
public class DeepTrenchBiomassHarvester : MonoBehaviour
{
    [Header("Organism Extraction")]
    public float extractionPressureAtm = 450f;
    public float biomassFilterEfficiency = 0.94f;
    public int currentColonySpecimens = 1420;

    [Header("Symbiotic Tank")]
    public float dissolvedOxygenPpm = 6.8f;
    public bool isNutrientCirculationActive = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Dark midnight or deep trench backdrops make cyan and teal glowing organisms pop vibrantly. |
| **`[ComponentHeader]`** | High | Organisms drift softly behind fields below deep-sea title cards. |
| **Inspector Controls** | High | `PickingMode.Ignore` ensures complete click-through transparency for all inspector controls. |
