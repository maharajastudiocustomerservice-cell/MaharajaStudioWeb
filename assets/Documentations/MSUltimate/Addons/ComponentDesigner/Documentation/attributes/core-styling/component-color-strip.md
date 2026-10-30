# [ComponentColorStrip]

> Adds a thin, colored accent edge strip along any side of the component inspector for instant category identification.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentColorStrip]` applies a crisp accent color rail along the left, top, right, or bottom edge (`Edge`) of the component inspector card. Operating via `ComponentSlot.BodyOverlay`, it renders a high-visibility stripe with configurable thickness (`Thickness`, defaulting to 4px), partial or full edge length (`LengthPercent`, defaulting to 100%), rounded endpoints (`BorderRadius`), and inward offset margins. It supports multiple instances (`AllowMultiple = true`), allowing dual-edge framing (e.g. left and right bars) or multi-color department coding.

**The Problem:**
Color-coding components by subsystem (e.g. Blue for Audio, Green for Gameplay, Red for Combat, Yellow for UI) usually requires full background coloring, which can create visual fatigue and clash with light/dark editor themes.

**The Solution:**
Decorating classes with `[ComponentColorStrip]`:
- **Subtle Accent Rail:** Delivers clear, non-intrusive subsystem identification without overwhelming the inspector canvas.
- **Four-Edge Flexibility:** Position on the left rail (`StripEdge.Left`), top accent bar, right edge, or bottom baseline.
- **Partial Edge Length:** Span full 100% edges or create sleek, centered accent dashes (`LengthPercent = 40f`).
- **Multiple Strips Allowed:** Combine multiple instances (e.g. Left green bar + Right gold bar) on a single component.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentColorStrip("#EF4444", Edge = StripEdge.Left, Thickness = 4f)]
public class CombatHitboxController : MonoBehaviour
{
    public float damageMultiplier = 2.0f;
    public bool isCriticalHitbox = true;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ComponentDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Component Slot** | `BodyOverlay` (`Order = 20`) |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentColorStripAttribute(string color)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `color` | `string` | *Required* | Hex color string for the accent stripe (e.g. `"#3B82F6"`). |

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color` | `string` | *Set via constructor* | Hex color code applied to the accent rail. |
| `Edge` | `StripEdge` | `StripEdge.Left` | Target edge where the strip is anchored (`Left`, `Top`, `Right`, `Bottom`). |
| `Thickness` | `float` | `4f` | Thickness of the strip in pixels. |
| `BorderRadius` | `float` | `0f` | Corner radius applied to the strip endpoints. |
| `LengthPercent` | `float` | `100f` | Length of the strip expressed as a percentage of the edge (0 to 100). |
| `Offset` | `float` | `0f` | Inward pixel offset from the selected edge boundary. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBackground("#1E293B", BorderRadius = 8f, Padding = 10f)]
[ComponentColorStrip("#10B981", Edge = StripEdge.Left, Thickness = 5f, BorderRadius = 3f)]
[ComponentColorStrip("#F59E0B", Edge = StripEdge.Top, Thickness = 2f, LengthPercent = 50f)]
public class EnvironmentalAudioEmitter : MonoBehaviour
{
    [Header("Acoustic Profile")]
    public string audioZoneName = "Ancient Whispering Cavern";
    public float reverbDecaySeconds = 3.5f;
    public float occlusionLowpassFrequency = 800f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Excellent pairing; anchors directly along the edges of the background container. |
| **`[ComponentBadge]`** | High | Badges and color strips complement each other for rapid visual triage. |
| **Multiple `[ComponentColorStrip]`** | High | Fully supported; use different edges (`Left`, `Right`, `Top`) to avoid overlap. |
| **Field-Level Attributes** | High | Leaves child field margins intact with zero horizontal layout distortion. |
