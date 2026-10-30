# [ComponentParticles]

> Renders lightweight animated particle simulations across the component card with presets for rising embers, twinkling sparkles, falling snow, and floating bubbles.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentParticles]` injects ambient atmospheric particle effects across the component card. Operating via lightweight UI Toolkit vector rendering, it simulates active particles using four distinct physical movement presets (`Style` $\to$ `Embers`, `Sparkles`, `Snow`, `Bubbles`). It supports custom particle density (`Count`, defaulting to 12 for optimal performance), random diameter ranges (`SizeMin`, `SizeMax`), simulation velocity (`Speed`), global transparency (`Opacity`), optional custom tinting (`Color`), and front/back layer routing (`Behind = true` $\to$ `ContentOverlay`, `Behind = false` $\to$ `BodyOverlay`).

**The Problem:**
Elemental spells, frozen environments, underwater logic, and magical artifacts look identical in standard gray Unity inspector windows. Without environmental particle effects, configuring thematic gameplay elements lacks immersion and immediate mood.

**The Solution:**
Decorating themed components with `[ComponentParticles]`:
- **Four Atmospheric Simulation Presets:**
  - `Embers`: Rising warm sparks for fire, lava, and forge components.
  - `Sparkles`: Soft twinkling celestial dots for enchantments, magic, and cosmic modules.
  - `Snow`: Gently descending flakes for frost, blizzard, and cryo mechanics.
  - `Bubbles`: Soft floating circles for aquatic, chemistry, and liquid systems.
- **Controlled Lightweight Performance:** Tuned for editor performance with minimal CPU cycles (defaulting to 12 particles) without impacting editor framerates.
- **Custom Color Grading:** Override default style colors via `Color` (e.g. green poison bubbles or purple void sparkles).
- **Zero Input Interruption:** Absolutely positioned with `PickingMode.Ignore`, ensuring controls receive uninterrupted mouse input.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentParticles(Style = ParticleStyle.Snow, Count = 14, SizeMin = 2f, SizeMax = 4.5f, Speed = 0.8f)]
public class FrostbiteStatusEffect : MonoBehaviour
{
    public float freezeDurationSeconds = 4.5f;
    public float movementSlowPercentage = 40f;
    public bool applyShatterOnCrit = true;
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
public ComponentParticlesAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Style` | `ParticleStyle` | `ParticleStyle.Sparkles` | Preset physics style (`Embers`, `Sparkles`, `Snow`, `Bubbles`). |
| `Count` | `int` | `12` | Total particle count (recommended 8–20 for peak performance). |
| `SizeMin` | `float` | `2f` | Minimum particle diameter in pixels. |
| `SizeMax` | `float` | `5f` | Maximum particle diameter in pixels. |
| `Speed` | `float` | `1f` | Particle drift and simulation velocity multiplier. |
| `Opacity` | `float` | `0.6f` | Transparency alpha of the particle layer (0.0 to 1.0). |
| `Color` | `string` | `""` | Hex color override string. If empty, uses preset default color. |
| `Behind` | `bool` | `false` | When true, renders behind inspector controls; when false, renders on top. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#3B82F6", Width = 1.5f, Radius = 8f)]
[ComponentBackground("#0B1528", BorderRadius = 8f, Padding = 10f)]
[ComponentHeader("CRYSTALLINE ICE CITADEL", Subtitle = "Glacial Shard & Cryo Field Emitter", BackgroundColor = "#112240", TitleColor = "#E0F2FE")]
[ComponentParticles(Style = ParticleStyle.Snow, Count = 16, SizeMin = 2.5f, SizeMax = 5f, Speed = 0.9f, Opacity = 0.55f, Color = "#BAE6FD", Behind = true)]
public class CrystallineIceCitadel : MonoBehaviour
{
    [Header("Cryo Emitter Data")]
    public float frostRadiusMeters = 30f;
    public float temperatureCelsius = -45f;
    public int glacialSpikesActive = 12;

    [Header("Thermal Dissipation")]
    public float meltRatePerSecond = 0.05f;
    public bool enableAbsoluteZeroAura = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Dark backdrops dramatically elevate the visibility of glowing sparkles and snow particles. |
| **`[ComponentHeader]`** | High | Particles float gracefully behind or across fields below a themed header bar. |
| **Inspector Controls** | High | Fully click-through (`PickingMode.Ignore`) so all serialized fields, sliders, and toggles operate normally. |
