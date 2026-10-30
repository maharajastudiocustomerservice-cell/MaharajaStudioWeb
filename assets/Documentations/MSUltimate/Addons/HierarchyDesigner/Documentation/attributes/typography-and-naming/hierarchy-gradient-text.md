# [HierarchyGradientText]

> Renders a character-by-character color gradient or dynamic rainbow effect across the hierarchy label.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyGradientText]` interpolates colors across each individual glyph in the GameObject name, supporting 2-stop linear gradients (`StartColor` $\rightarrow$ `EndColor`), 3-stop multi-color ramps (`MiddleColor`), and dynamic cycling chromatic spectrums (`RainbowMode = true`).

**The Problem:**
Standard Unity text color customization is strictly uniform and monolithic across the entire name. In complex project architectures, differentiating high-level tiers (e.g. Legendary items, Epic boss rigs, or special engine subsystems) with single solid colors lacks visual prestige.

**The Solution:**
Decorating classes with `[HierarchyGradientText]`:
- **Smooth Character Gradient Interpolation:** Calculates precise per-character t-values from start to finish, rendering a luxury gradient banner across the text.
- **3-Stop Color Ramps:** Supports intermediate midpoint hues (`MiddleColor = "#E67E22"`) for fire, sunset, or galaxy color blends.
- **Dynamic Rainbow Spectrum Mode:** Toggle `RainbowMode = true` to animate the entire visible character sequence through the full HSV spectrum continuously.
- **Weight and Style Options:** Fully supports bold weight, italic slant, and custom pixel font sizes.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyGradientText(StartColor = "#38BDF8", EndColor = "#A855F7", Bold = true)]
public class MythicItemChest : MonoBehaviour
{
    public int tierLevel = 5;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class` \| `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyGradientTextRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyGradientTextAttribute()
```

- Standard parameterless constructor. Gradients, midpoints, and styling parameters are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `StartColor` | `string` | `"#00D2FF"` | Hex color code of the gradient starting glyphs. |
| `EndColor` | `string` | `"#9B59B6"` | Hex color code of the gradient terminating glyphs. |
| `MiddleColor` | `string` | `""` | Optional hex color code for a 3-stop midpoint transition hue. |
| `RainbowMode` | `bool` | `false` | Whether to cycle dynamic chromatic rainbow spectrum colors across characters. |
| `Bold` | `bool` | `true` | Whether to render characters with bold font weight. |
| `Italic` | `bool` | `false` | Whether to render characters in italics. |
| `FontSize` | `int` | `0` | Custom font size in pixels (0 uses default hierarchy size). |
| `IsActiveInPlayMode` | `bool` | `true` | Whether gradient rendering remains active during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row decorations. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyGradientText(
    StartColor = "#F59E0B", 
    MiddleColor = "#EF4444", 
    EndColor = "#8B5CF6", 
    Bold = true, 
    FontSize = 13)]
public class LegendaryArtifactSpawner : MonoBehaviour
{
    [Header("Artifact Spawning")]
    public string artifactId = "AURA_BLADE_01";
    public float respawnCooldown = 300f;
    public bool isAvailable = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyTextShadow]`** | High | Pair gradient text with subtle black shadows or halo glows for enhanced readability. |
| **`[HierarchyTooltip]`** | High | Display item stats, rarity multipliers, and lore notes on hover. |
| **`[HierarchyTextColor]`** | Incompatible | Do not stack with solid color attributes since gradient rendering supersedes single-color fills. |
| **`[HierarchyFolder]`** | High | Can be applied to virtual folder categories to create luxury gradient category headers. |
