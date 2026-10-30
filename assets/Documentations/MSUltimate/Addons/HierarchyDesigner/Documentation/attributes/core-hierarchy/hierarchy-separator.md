# [HierarchySeparator]

> Transforms a hierarchy row into a styled visual section header with background banner, icon, and accent lines.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchySeparator]` turns empty organizational GameObjects into full-width section headers, category banners, and dividers in the Unity Hierarchy window. Driven by `HierarchySeparatorRenderer`, it paints a full-width background color (`BackgroundColor = "#1A1A2E"`), an optional bottom accent line (`AccentColor = "#7B61FF"`), a left edge vertical accent stripe, and built-in icons. It supports customizable text alignment (Left, Center, Right), text overrides, bold/italic typography, and custom font sizes.

**The Problem:**
Large Unity scenes inevitably end up with hundreds of objects. To create visual structure, developers traditionally create dummy GameObjects named `--- LIGHTING ---` or `// ENVIRONMENT //`. These pseudo-dividers look messy, blend into the background, and provide no true visual contrast or organization.

**The Solution:**
Decorating header GameObjects with `[HierarchySeparator]`:
- **Full-Width Section Banners:** Renders vibrant, themed background banners across the entire hierarchy row.
- **Accents & Edge Stripes:** Features customizable bottom underline borders and left-edge color bars for crisp category delineation.
- **Flexible Text Alignment:** Center, left-align, or right-align section labels (`HierarchySeparatorTextAlignment`).
- **Icon Support:** Display native Unity icons or symbols beside the header text.
- **Zero Runtime Overhead:** Operates purely in the editor GUI without requiring heavy MonoBehaviour logic or performance penalties.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchySeparator(BackgroundColor = "#0F172A", AccentColor = "#38BDF8", Bold = true)]
public class LightingSectionHeader : MonoBehaviour
{
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchySeparatorRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchySeparatorAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `OverrideText` | `string` | `""` | Custom header text, or empty to use the GameObject's current name. |
| `Icon` | `string` | `""` | Built-in Unity icon name drawn beside the header text. |
| `IconSize` | `float` | `14f` | Size of the icon in pixels. |
| `BackgroundColor` | `string` | `"#1A1A2E"` | Hex background color spanning the entire hierarchy row. |
| `AccentColor` | `string` | `"#7B61FF"` | Hex color of the bottom accent border line. |
| `AccentHeight` | `float` | `2f` | Height of the bottom accent line in pixels. |
| `TextColor` | `string` | `"#FFFFFF"` | Hex color of the header label text. |
| `Bold` | `bool` | `true` | Whether to render the header text in bold font. |
| `Italic` | `bool` | `false` | Whether to render the header text in italic font. |
| `FontSize` | `int` | `0` | Font size override in pixels, or `0` for default editor font size. |
| `TextAlignment` | `HierarchySeparatorTextAlignment` | `Left` | Horizontal text alignment (`Left`, `Center`, or `Right`). |
| `LeftStripeColor` | `string` | `""` | Hex color of the left edge vertical accent stripe, or empty for none. |
| `LeftStripeWidth` | `float` | `3f` | Width of the left vertical edge stripe in pixels. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the separator styling remains visible during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchySeparator(
    OverrideText = "=== AUDIO & AMBIENCE ===", 
    Icon = "AudioSource Icon", 
    BackgroundColor = "#1E1B4B", 
    AccentColor = "#818CF8", 
    AccentHeight = 2.5f, 
    TextColor = "#E0E7FF", 
    LeftStripeColor = "#4F46E5", 
    LeftStripeWidth = 4f, 
    TextAlignment = HierarchySeparatorTextAlignment.Center, 
    Bold = true)]
public class AudioHierarchyDivider : MonoBehaviour
{
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **Empty GameObjects** | High | Best used on empty divider objects to segment major scene branches. |
| **`[HierarchyLock]`** | High | Lock separator GameObjects so team members don't accidentally drag child entities under them. |
| **`[HierarchyNote]`** | High | Add notes to separators to outline organizational policies for that scene section. |
| **Hierarchy Folders** | High | Works alongside hierarchy folder tools to create clean visual chapters in scene hierarchies. |
