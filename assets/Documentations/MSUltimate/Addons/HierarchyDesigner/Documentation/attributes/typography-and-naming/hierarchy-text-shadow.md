# [HierarchyTextShadow]

> Renders a directional drop shadow or omnidirectional glowing halo behind hierarchy label characters.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyTextShadow]` adds depth and contrast to the GameObject's hierarchy row label. It draws a directional drop shadow (`ShadowOffsetX`, `ShadowOffsetY`) or an 8-way omnidirectional glowing halo (`GlowHalo = true`) behind the foreground characters, significantly improving text readability against alternating hierarchy background strips.

**The Problem:**
In custom Editor themes, selected rows, or when multiple background colors and zebra-striping plugins are in use, hierarchy text can lose contrast and become difficult to read. Furthermore, flat text lacks visual punch.

**The Solution:**
Decorating components with `[HierarchyTextShadow]`:
- **Directional Drop Shadows:** Offsets a crisp shadow silhouette (`ShadowOffsetX = 1.0f`, `ShadowOffsetY = 1.0f`) beneath the label for elevated contrast.
- **8-Way Halo Glow:** Enabling `GlowHalo = true` renders an omnidirectional outline around each glyph, creating a neon or radiant outline effect.
- **Independent Color Control:** Configure foreground text (`TextColor = "#FFFFFF"`) and shadow/glow tint (`ShadowColor = "#000000"`) separately.
- **Typography Weights:** Full support for bold and italic font variations.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyTextShadow(TextColor = "#FFFFFF", ShadowColor = "#000000", ShadowOffsetX = 1.5f, ShadowOffsetY = 1.5f)]
public class HighContrastHeader : MonoBehaviour
{
    public string categoryName;
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
| **Render Engine** | `HierarchyTextShadowRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyTextShadowAttribute()
```

- Standard parameterless constructor. Shadow offsets, colors, and halo options are configured via object initializers.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `TextColor` | `string` | `"#FFFFFF"` | Hex color string for the foreground text characters. |
| `ShadowColor` | `string` | `"#000000"` | Hex color string for the shadow or glowing halo silhouette. |
| `ShadowOffsetX` | `float` | `1.0f` | Horizontal shadow pixel displacement offset. |
| `ShadowOffsetY` | `float` | `1.0f` | Vertical shadow pixel displacement offset. |
| `GlowHalo` | `bool` | `false` | Whether to render an 8-directional surrounding halo instead of a single directional drop shadow. |
| `Bold` | `bool` | `true` | Whether to render characters with bold font weight. |
| `Italic` | `bool` | `false` | Whether to render characters in italics. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether shadow rendering remains active during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row decorations. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyTextShadow(
    TextColor = "#38BDF8", 
    ShadowColor = "#0369A1", 
    GlowHalo = true, 
    Bold = true)]
public class RadiantBeaconNode : MonoBehaviour
{
    [Header("Beacon Settings")]
    public float signalStrength = 100f;
    public bool isBroadcasting = true;
    public Color beaconAuraColor = Color.cyan;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyFolder]`** | High | Apply drop shadows to virtual folder headers for pronounced visual separation. |
| **`[HierarchyTooltip]`** | High | Pair shadowed headers with rich documentation notes on hover. |
| **`[HierarchyBookmark]`** | High | Sits cleanly alongside bookmark ribbon tabs. |
| **`[HierarchyTextColor]`** | Incompatible | Do not stack with standard text color attributes as `[HierarchyTextShadow]` manages foreground and background passes. |
