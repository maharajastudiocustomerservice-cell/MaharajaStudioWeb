# [AnimatedGradientBackground]

> Renders a continuous cycling two-color animated gradient background with customizable colors, cycle speeds, and corner rounding.

---

## 1. Overview & Value Proposition

**What it does:**
Renders an eye-catching, smoothly cycling two-color linear gradient directly behind the field. The gradient oscillates smoothly between `Color1` and `Color2` at a customizable speed (`AnimationSpeed`), perfect for highlighting premium features, legendary items, or critical mechanics.

**The Problem:**
Static background colors in the Inspector look dull and fail to convey the special status of legendary items, boss phases, or VIP features.

**The Solution:**
Add `[AnimatedGradientBackground]` to any field:
- **Liquid Motion Backdrop:** Creates a modern, flowing animated backdrop behind any property.
- **Dual-Color Blending:** Choose two distinct hex colors with alpha transparency.
- **Custom Oscillation Speed:** Control the rate of the color cycle.
- **Rounded Aesthetics:** Clean corner rounding (`Rounding = 4f`) keeps borders modern and sleek.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class LegendaryLoot : MonoBehaviour
{
    [AnimatedGradientBackground(Color1 = "#FFD70066", Color2 = "#FF450066", AnimationSpeed = 1.5f)]
    public string legendarySwordName = "Excalibur";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public AnimatedGradientBackgroundAttribute()
```

*Attribute initializes with a cyberpunk neon gradient; customize colors via object initializers.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color1` | `string` | `"#FF007F55"` | Starting hex color string of the gradient. |
| `Color2` | `string` | `"#7F00FF55"` | Ending hex color string of the gradient. |
| `AnimationSpeed` | `float` | `2f` | Speed multiplier for the gradient color oscillation. |
| `Rounding` | `float` | `4f` | Corner radius in pixels for the gradient background. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class BossPhaseConfig : MonoBehaviour
{
    [Header("Enrage Phase Attributes")]
    [AnimatedGradientBackground(
        Color1 = "#e74c3c77", 
        Color2 = "#8e44ad77", 
        AnimationSpeed = 3f, 
        Rounding = 6f
    )]
    public float enrageDamageMultiplier = 2.5f;

    [Header("Divine Protection Mode")]
    [AnimatedGradientBackground(Color1 = "#f1c40f66", Color2 = "#2ecc7166")]
    public bool isInvulnerable = false;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Gradient background sits cleanly within group containers. |
| `[AnimatedHover]` | Supported | Can be combined with hover scale for a complete VIP card feel. |
| Primary Drawers | Supported | Operates strictly on the background layer, leaving controls fully accessible. |
