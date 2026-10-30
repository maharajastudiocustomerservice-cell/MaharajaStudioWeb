# [ColorWheel]

> Renders an interactive HSV Color Wheel directly inside the Unity Inspector, eliminating the need to open external floating color picker windows.

---

## 1. Overview & Value Proposition

**What it does:**
Embeds an interactive 360° HSV color wheel directly inside the Inspector, letting you tweak colors visually in real time without opening Unity's popup color window.

**The Problem:**
In standard Unity, changing a color requires clicking a tiny swatch, which pops open a floating Color Picker dialog. This popup blocks your Scene view, gets in the way of other inspector properties, and requires extra clicks just to make a quick adjustment.

**The Solution:**
Add `[ColorWheel]` to any `Color` or `Color32` field or property to render an embedded circular color wheel right on your component:
- **Fast Visual Tweaking:** Click and drag anywhere on the wheel to adjust hue and saturation instantly.
- **Dedicated Value & Alpha Sliders:** Easily fine-tune brightness and transparency right below the wheel.
- **Live Hex Readout:** View and edit exact Hex codes in real time without extra dialogs.
- **Zero Window Clutter:** Keeps your Scene view and Inspector completely unobstructed.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class SpotlightConfig : MonoBehaviour
{
    [ColorWheel(WheelSize = 140f, ShowAlpha = true)]
    public Color lightBeamColor = Color.cyan;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Field | AttributeTargets.Property` |
| **Supported Types** | `Color`, `Color32` |
| **Allow Multiple** | `false` |
| **Inherited** | `true` |
| **Interfaces** | `ICollectionElementAttribute` |
| **Build Overhead** | Editor-only (Zero runtime build overhead / stripped in builds) |
| **Minimum Unity** | Unity 6 (6000.x)+ |

---

## 4. Constructors & Signatures

```csharp
public ColorWheelAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `WheelSize` | `float` | `120f` | Diameter of the HSV color wheel in pixels. |
| `ShowAlpha` | `bool` | `true` | Displays dedicated alpha opacity slider below the wheel. |
| `ShowHex` | `bool` | `true` | Shows an editable Hex code string input box below the wheel. |
| `Alignment` | `UiAlignment` | `UiAlignment.Left` | Alignment of the wheel container (`Left`, `Center`, `Right`). |
| `BackgroundColor` | `string` | `""` | Background color behind the wheel frame (supports Hex). |
| `BorderRadius` | `float` | `8f` | Corner rounding radius for the wheel container panel. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class MagicSpellAura : MonoBehaviour
{
    [BoxGroup("Aura Particle Styling", Box = true)]
    [ColorWheel(
        WheelSize = 150f,
        ShowAlpha = true,
        ShowHex = true,
        Alignment = UiAlignment.Center,
        BorderRadius = 10f
    )]
    [Tooltip("Primary elemental tint applied to magical projectile emissions.")]
    public Color elementalTint = new Color(0.2f, 0.8f, 1f, 1f);

    [BoxGroup("Aura Particle Styling")]
    [Range(0.1f, 5f)]
    public float emissionIntensity = 2.5f;
}
```

---

## 7. Stacking & Compatibility Matrix

- **Grouping:** Pairs seamlessly with `[BoxGroup]` and `[FoldoutGroup]`. Center alignment (`UiAlignment.Center`) is recommended inside cards.
- **Conditionals:** Fully reactive with `[ShowIf]` and `[DisableIf]`.
- **Validation:** Defensively restricts inputs to valid `Color` or `Color32` serialized properties. If applied to unsupported types, provides safe non-destructive fallback.
