# [HierarchyTextColor]

> Customizes hierarchy label text color, font style, size, affixes, and optional background pill box.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyTextColor]` is the primary workhorse attribute for colorizing and formatting GameObject names in the Unity Hierarchy window. It provides direct hex color tinting (`ColorHex = "#FFD700"`), font weight controls (`Bold`, `Italic`, `FontSize`), optional text affixes (`Prefix`, `Suffix`), and an optional background pill box with customizable padding (`BackgroundColor`, `BackgroundPadding`).

**The Problem:**
By default, Unity renders all hierarchy labels in a single monochromatic gray/white font. In complex scenes, finding essential landmark objects—such as main cameras, player rigs, game managers, or level exit triggers—requires reading through hundreds of identical rows.

**The Solution:**
Decorating components with `[HierarchyTextColor]`:
- **Instant Color Identification:** Tint critical objects with distinct color codes (e.g. gold for managers, cyan for lighting, emerald for checkpoints).
- **Flexible Overload Constructors:** Accepts hex color strings directly in the constructor (`[HierarchyTextColor("#38BDF8")]`) or parameterless for default gold (`"#FFD700"`).
- **Typography Sizing & Weights:** Fine-tune font sizes and weights for visual hierarchy.
- **Background Pill Box:** Draw an optional colored pill behind the text for prominent header badges.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyTextColor("#38BDF8", Bold = true)]
public class PlayerRig : MonoBehaviour
{
    public float movementSpeed = 6.0f;
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
| **Render Engine** | `HierarchyTextColorRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyTextColorAttribute()
public HierarchyTextColorAttribute(string colorHex)
```

- **`colorHex`** (`string`): Hex color string formatted as `"#RRGGBB"` or `"#RRGGBBAA"`. Defaults to gold (`"#FFD700"`).

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ColorHex` | `string` | `"#FFD700"` | Hex color code for the label text. |
| `Bold` | `bool` | `false` | Whether to render the characters with bold font weight. |
| `Italic` | `bool` | `false` | Whether to render the characters in italics. |
| `FontSize` | `int` | `0` | Custom font size in pixels (0 uses default 12px size). |
| `Prefix` | `string` | `""` | Optional string prepended to the displayed name. |
| `Suffix` | `string` | `""` | Optional string appended to the displayed name. |
| `BackgroundColor` | `string` | `""` | Optional hex background color for a pill box behind text. |
| `BackgroundPadding` | `float` | `2f` | Horizontal padding in pixels for the background pill box. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether color customization remains active during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row decorations. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyTextColor(
    "#10B981", 
    Bold = true, 
    FontSize = 13, 
    Prefix = "★ ", 
    BackgroundColor = "#064E3B", 
    BackgroundPadding = 4f)]
public class LevelExitPortal : MonoBehaviour
{
    [Header("Portal Mechanics")]
    public string destinationSceneName = "Level_02_Forest";
    public bool requiresBossKey = true;
    public ParticleSystem portalVFX;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyTooltip]`** | High | Display portal requirements, destination scenes, or status notes on hover. |
| **`[HierarchyIcon]`** | High | Pair custom color text with high-visibility component icons. |
| **`[HierarchyBookmark]`** | High | Stacks smoothly with bookmark ribbons on priority landmark entities. |
| **`[HierarchyFolder]`** | High | Apply color labels to virtual folders to categorize scene hierarchy sections. |
