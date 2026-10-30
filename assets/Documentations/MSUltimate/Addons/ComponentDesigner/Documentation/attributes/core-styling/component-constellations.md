# [ComponentConstellations]

> Renders an animated background pattern of twinkling celestial stars with connecting geometric constellation lines.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentConstellations]` introduces a celestial stargazing aesthetic into the component inspector. Injected as an ambient background or overlay layer (`Behind = true` $\to$ `ContentOverlay`, `Behind = false` $\to$ `BodyOverlay`), it procedurally scatters twinkling star nodes across the card container. Using deterministic seed coordinates (RNG 313), each star point oscillates in luminosity according to independent twinkle speeds. Optional geometric vectors (`ShowLines = true`) bridge neighboring stellar coordinates in a subtle celestial mesh (`LineColor`). Operating with `PickingMode.Ignore`, it gives space simulators, astrology spellbooks, and sci-fi nav-computers a cosmic atmosphere without interrupting user input.

**The Problem:**
Astrological systems, space navigation consoles, skill galaxy trees, and fantasy astronomy managers feel lifeless when decorated with plain flat gray backdrops.

**The Solution:**
Decorating cosmic components with `[ComponentConstellations]`:
- **Twinkling Star Field:** Renders procedural stellar nodes (`Stars`, clamped between 3 and 15) with independent sinusoidal brightness oscillation.
- **Connecting Constellation Vectors:** Renders geometric lines linking neighboring star clusters (`ShowLines = true`).
- **Configurable Ambient Opacity:** Tune star/line transparency (`Opacity`) so content remains crisp and legible.
- **Behind Content Placement:** Renders smoothly behind fields (`Behind = true`) so text, dropdowns, and toggles remain primary.
- **Zero Click Interception:** Configured with `PickingMode.Ignore`, allowing uninterrupted slider dragging and button clicks.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentConstellations(Stars = 10, Size = 3.5f, Speed = 1.2f, Opacity = 0.35f)]
public class SpaceNavigationComputer : MonoBehaviour
{
    public Vector3 warpCoordinates = new Vector3(1420f, -850f, 9200f);
    public float hyperdriveFuelLevel = 0.88f;
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
public ComponentConstellationsAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color` | `string` | `"#FFFFFF"` | Hex color string for twinkling star dots. |
| `Stars` | `int` | `8` | Number of procedural stars generated (clamped between 3 and 15). |
| `Size` | `float` | `3f` | Diameter in pixels for each individual circular star dot. |
| `Speed` | `float` | `1f` | Twinkle oscillation cycle speed multiplier. |
| `Opacity` | `float` | `0.3f` | Global transparency alpha of the constellation layer (0.0 to 1.0). |
| `ShowLines` | `bool` | `true` | When true, draws connecting vector lines between neighboring star coordinates. |
| `LineColor` | `string` | `"#444466"` | Hex color code applied to connecting constellation lines. |
| `Behind` | `bool` | `true` | When true, renders behind inspector controls; when false, renders on top. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#818CF8", Width = 1.5f, Radius = 8f)]
[ComponentBackground("#090D16", BorderRadius = 8f, Padding = 12f)]
[ComponentConstellations(Stars = 12, Size = 3f, Speed = 1.5f, Opacity = 0.4f, LineColor = "#4338CA", Behind = true)]
public class CelestialSkillTreeEngine : MonoBehaviour
{
    [Header("Constellation Mastery")]
    public string activeZodiacSign = "Sagittarius";
    public int unlockedCelestialNodes = 14;
    public float astralEnergyResonance = 78.4f;
    public bool isAlignmentBonusActive = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Highly recommended; deep midnight blues or obsidian blacks (`#090D16`, `#0B132B`) showcase the twinkling stars best. |
| **`[ComponentAuroraEffect]`** | High | Combines naturally to produce a complete cosmic aurora sky across the component card. |
| **`[ComponentHeader]`** | High | Headers stay positioned cleanly above the constellation background plane. |
| **Field Inputs & Buttons** | High | `PickingMode.Ignore` ensures zero conflict with mouse events or input fields. |
