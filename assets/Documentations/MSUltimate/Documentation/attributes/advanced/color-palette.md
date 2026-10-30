# [ColorPalette]

> Enhances Color and Color32 fields with clickable swatch presets from predefined project palettes ("Material", "Pastel", "GrayScale") or custom hex arrays.

---

## 1. Overview & Value Proposition

**What it does:**
Attaches clickable color swatch buttons next to your Color fields, allowing artists and designers to pick approved project colors with a single click.

**The Problem:**
In standard Unity, keeping colors consistent across UI, lighting, and materials is painful. Designers have to remember Hex codes, copy-paste color values between objects, or use the eyedropper tool over and over. A single wrong shade can make your game UI look inconsistent and unpolished.

**The Solution:**
Add `[ColorPalette]` to any `Color` or `Color32` field to display a curated swatch palette directly in the Inspector:
- **Predefined Palettes:** Built-in support for `"Material"` (19 modern UI hues), `"Pastel"` (soft pastel tones), and `"GrayScale"` (monochrome values). If no palette or custom array is specified, automatically defaults to `"Material"`.
- **1-Click Selection:** Click any swatch to immediately set the field's serialized color and apply changes.
- **Custom Swatch Arrays:** Define bespoke brand or faction palettes using arrays of hex strings.
- **Custom Swatch Grids:** Control swatch size, spacing, borders, hover highlights, and wrapping.
- **Dual Representation:** The standard Unity color picker field remains optionally accessible alongside swatches.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class UIThemeController : MonoBehaviour
{
    // Uses predefined "Pastel" palette
    [ColorPalette("Pastel")]
    public Color accentColor = Color.white;

    // Uses custom hex colors
    [ColorPalette(CustomColors = new string[] { "#FF5733", "#33FF57", "#3357FF", "#F1C40F" })]
    public Color primaryAccent = Color.yellow;
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
public ColorPaletteAttribute(string paletteName = null)
```
- **`paletteName`**: Optional name of a predefined palette: `"Material"`, `"Pastel"`, or `"GrayScale"`. When `null` and `CustomColors` is empty, defaults to `"Material"`.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `PaletteName` | `string` | `null` | Predefined palette key (`"Material"`, `"Pastel"`, `"GrayScale"`). Read-only; set via constructor. |
| `CustomColors` | `string[]` | `null` | Array of hex color strings (e.g. `"#E74C3C"`) to render as swatches. |
| `SwatchSize` | `float` | `24f` | Width and height of each color swatch button in pixels. |
| `SwatchesPerRow` | `int` | `0` | Maximum swatches per row (`0` auto-wraps based on Inspector width). |
| `ShowAlpha` | `bool` | `true` | Whether the default color field and swatches support alpha transparency. |
| `DrawDefaultColorField` | `bool` | `true` | Renders the standard Unity color picker field above the swatches. |
| `SwatchMargin` | `float` | `2f` | Spacing in pixels between adjacent color swatches. |
| `BorderWidth` | `float` | `1f` | Border line thickness in pixels for each swatch box. |
| `BorderRadius` | `float` | `3f` | Corner rounding radius for each swatch box in pixels. |
| `BorderColor` | `string` | `"#000000"` | Hex border outline color around swatches. |
| `HoverBorderColor` | `string` | `"#FFFFFF"` | Accent border color when hovering over a swatch. |
| `ShowLabel` | `bool` | `true` | Toggles whether the property name label is displayed. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class MinimapBlipManager : MonoBehaviour
{
    [BoxGroup("Faction Styling", Box = true)]
    [ColorPalette(
        CustomColors = new string[] { 
            "#2ECC71", // Friendly Green
            "#E74C3C", // Hostile Red
            "#3498DB", // Neutral Blue
            "#9B59B6", // Objective Purple
            "#F39C12"  // Alert Orange
        },
        SwatchSize = 22f,
        BorderRadius = 4f,
        BorderColor = "#222222",
        HoverBorderColor = "#00FFFF"
    )]
    [Tooltip("Color tint representing player allegiance on the radar.")]
    public Color allegianceColor = Color.green;

    [BoxGroup("Faction Styling")]
    [Range(0.5f, 2f)]
    public float blipScale = 1.0f;
}
```

---

## 7. Stacking & Compatibility Matrix

- **Layout Compatibility:** Works cleanly inside `[BoxGroup]`, `[VerticalGroup]`, and `[CardGroup]`. Swatches wrap cleanly if parent width narrows.
- **Conditionals:** Compatible with `[ShowIf]` and `[EnableIf]`. Disabled states grey out both the color field and swatch buttons.
- **Callbacks:** Dispatches standard `SerializedObject.ApplyModifiedProperties()`, triggering any `[OnValueChanged]` callbacks when swatches are clicked.
- **Defensive Fallback:** If applied to non-color fields, logs a safe inspector warning without throwing GUI exceptions.
