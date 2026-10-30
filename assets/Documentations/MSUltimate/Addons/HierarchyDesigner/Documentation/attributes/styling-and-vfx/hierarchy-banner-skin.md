# [HierarchyBannerSkin]

> Renders a themed skinned header banner row across the hierarchy for styled visual grouping.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyBannerSkin]` transforms GameObjects into themed section headers and dividers directly in the Unity Hierarchy window. Driven by `HierarchyBannerSkinRenderer`, it paints a full-width themed background rect, custom accent border stripes on the left and bottom edges, and theme-specific icon prefixes (e.g. `"◈ "`, `"⚔ "`, `"⚠ "`, `"◼ "`, `"● "`). It features 5 built-in aesthetic presets via the `HierarchyBannerTheme` enum (`SciFiCyber`, `FantasyParchment`, `CarbonDark`, `MinimalistClean`, `HazardIndustrial`), with full support for custom title strings and accent color overrides.

**The Problem:**
Standard Unity hierarchies lack visual personality and aesthetic organization. Game developers often create plain divider objects with text like `--- CAMERAS ---`, which blend into standard scene objects and provide no distinctive styling or theme cohesion.

**The Solution:**
Decorating header GameObjects with `[HierarchyBannerSkin]`:
- **Themed Visual Headers:** Choose from 5 curated design aesthetics matching your game's genre (Sci-Fi, Fantasy, Industrial, Minimal, Carbon).
- **Edge Accent Stripes:** Renders crisp vertical accent bars on the left margin and thin underlines on the bottom edge.
- **Custom Accent Tinting:** Override accent colors (`AccentColor = "#00FFAA"`) to match project color palettes.
- **Title Override Support:** Specify a custom title or let it automatically format the GameObject's name in uppercase.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyBannerSkin(Theme = HierarchyBannerTheme.SciFiCyber, Title = "AI DIRECTORS", AccentColor = "#00E5FF")]
public class AiSectionBanner : MonoBehaviour
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
| **Render Engine** | `HierarchyBannerSkinRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyBannerSkinAttribute()
```

- Standard parameterless constructor. Theme, title, and accents are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Theme` | `HierarchyBannerTheme` | `SciFiCyber` | Visual theme preset (`SciFiCyber`, `FantasyParchment`, `CarbonDark`, `MinimalistClean`, `HazardIndustrial`). |
| `Title` | `string` | `""` | Title text displayed in the header banner. If empty, uses the GameObject's name in uppercase. |
| `AccentColor` | `string` | `"#00FFAA"` | Hex accent color for the left border bar, bottom underline, and title text. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the banner styling remains visible during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

### Supported Theme Presets

| Theme | Prefix Icon | Default Background | Default Aesthetic |
| :--- | :---: | :--- | :--- |
| `SciFiCyber` | `◈ ` | Deep Navy (`#141F29`) | Cyberpunk, sci-fi HUDs, futuristic telemetry |
| `FantasyParchment` | `⚔ ` | Warm Leather/Brown (`#3D3326`) | RPGs, medieval fantasy, parchment maps |
| `CarbonDark` | `◼ ` | Dark Matte Carbon (`#1A1A1E`) | Sleek dark mode, pro studio tools, audio racks |
| `HazardIndustrial` | `⚠ ` | Dark Amber/Ochre (`#2E240D`) | Industrial zones, hazard traps, sci-fi facilities |
| `MinimalistClean` | `● ` | Neutral Charcoal (`#26262E`) | Minimalist modern layouts, clean studio pipelines |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyBannerSkin(
    Theme = HierarchyBannerTheme.FantasyParchment, 
    Title = "DUNGEON BOSS RIGS", 
    AccentColor = "#F59E0B")]
public class BossSectionDivider : MonoBehaviour
{
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchySeparator]`** | Alternative | Use `HierarchySeparator` for custom underline geometry, and `HierarchyBannerSkin` for themed game-genre skins. |
| **`[HierarchyLock]`** | High | Lock banner headers to prevent accidental dragging or reparenting of child entities. |
| **Empty GameObjects** | High | Best placed on empty GameObject dividers to organize large scene branches. |
| **Hierarchy Selection** | High | Full row styling renders during repaint; clicking the row still selects the GameObject normally. |
