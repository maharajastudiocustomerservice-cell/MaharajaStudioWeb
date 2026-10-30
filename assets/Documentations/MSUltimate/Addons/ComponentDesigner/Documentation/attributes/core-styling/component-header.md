# [ComponentHeader]

> Renders a premium header bar above the component card with support for title, subtitle, built-in Unity icons, horizontal gradient backgrounds, and separator dividers.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentHeader]` transforms ordinary component headers into branded, AAA-grade control headers. Injected into `ComponentSlot.BeforeContent` (`Order = 10`), it anchors a styled title bar across the top of the inspector card. It features high-visibility title typography (`Title`, `TitleColor`, `TitleFontSize`, `TitleFontStyle`), an optional contextual subtitle (`Subtitle`, `SubtitleColor`, `SubtitleFontSize`, `SubtitleFontStyle`), built-in Unity editor icon integration (`Icon`, `IconSize`), solid or dual-color horizontal gradient backdrops (`BackgroundColor`, `GradientEndColor`), and an integrated bottom divider stroke (`ShowDivider`, `DividerColor`, `DividerHeight`).

**The Problem:**
Standard Unity inspectors display only the C# script class name in faint, standard text. In complex scenes packed with dozens of MonoBehaviours, team members struggle to quickly identify which component controls which subsystem, leading to configuration mistakes and wasted navigation time.

**The Solution:**
Decorating components with `[ComponentHeader]`:
- **Immediate Visual Recognition:** Prominent bold titles and italic subtitles instantly communicate component authority and purpose.
- **Built-In Icon Integration:** Supports any Unity editor icon or custom texture string directly beside the title.
- **Dynamic Gradient Banners:** Set `GradientEndColor` to create smooth horizontal two-tone gradient banners without complex CSS.
- **Unified Card Architecture:** Rounded top corners (`BorderRadius`) snap flush with `[ComponentBorder]` and `[ComponentBackground]`.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentHeader("PLAYER HEALTH CONTROLLER", Subtitle = "Vital Stats, Armor & Damage Mitigation", Icon = "d_Favorite", BackgroundColor = "#1E1E38")]
public class PlayerHealthController : MonoBehaviour
{
    public float maximumHitPoints = 100f;
    public float armorDamageReduction = 0.25f;
    public bool isInvulnerable = false;
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
| **Component Slot** | `BeforeContent` (`Order = 10`) |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentHeaderAttribute(string title)
```

- `title`: The primary header title string (e.g. `"COMBAT SYSTEM"`).

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Title` | `string` | *(Constructor)* | Primary title text string. |
| `Subtitle` | `string` | `""` | Secondary subtitle displayed underneath the title. |
| `Icon` | `string` | `""` | Unity built-in icon identifier (e.g. `"d_Settings Icon"`, `"d_Favorite"`). |
| `IconSize` | `float` | `24f` | Icon display dimensions in pixels. |
| `BackgroundColor` | `string` | `"#1A1A2E"` | Hex background color string for the header bar. |
| `GradientEndColor` | `string` | `""` | Optional second hex color for horizontal background gradient. |
| `TitleColor` | `string` | `"#E0E0FF"` | Hex color string for the primary title text. |
| `SubtitleColor` | `string` | `"#8888AA"` | Hex color string for the subtitle text. |
| `TitleFontSize` | `int` | `14` | Font size in points for the primary title. |
| `TitleFontStyle` | `FontStyle` | `FontStyle.Bold` | Font style for title text (`Normal`, `Bold`, `Italic`, `BoldAndItalic`). |
| `SubtitleFontSize` | `int` | `11` | Font size in points for the subtitle. |
| `SubtitleFontStyle` | `FontStyle` | `FontStyle.Italic` | Font style for subtitle text. |
| `ShowDivider` | `bool` | `true` | When true, renders a separator divider below the header bar. |
| `DividerColor` | `string` | `"#3A3A5E"` | Hex color string for the separator divider line. |
| `DividerHeight` | `float` | `1f` | Height/thickness in pixels of the separator line. |
| `BorderRadius` | `float` | `6f` | Top-left and top-right corner rounding in pixels. |
| `Padding` | `float` | `10f` | Internal padding in pixels surrounding header content. |
| `MarginBottom` | `float` | `4f` | Vertical margin spacing below the header bar. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#059669", Width = 2f, Radius = 8f)]
[ComponentBackground("#062319", BorderRadius = 8f, Padding = 10f)]
[ComponentHeader("TERRAIN GENERATION ENGINE", Subtitle = "Voxel Meshing & Biome Distribution", Icon = "d_Terrain Icon", IconSize = 26f, BackgroundColor = "#0A3D2C", GradientEndColor = "#047857", TitleColor = "#ECFDF5", SubtitleColor = "#A7F3D0", ShowDivider = true, DividerColor = "#10B981", DividerHeight = 1.5f, BorderRadius = 8f)]
[ComponentFooter("Voxel Framework Engine", Version = "v4.1.0", BackgroundColor = "#082F22", TextColor = "#6EE7B7", BorderRadius = 8f)]
public class TerrainGenerationEngine : MonoBehaviour
{
    [Header("Chunk Settings")]
    public int chunkWidth = 32;
    public int chunkHeight = 128;
    public int worldSeed = 94821;

    [Header("Noise Generators")]
    public float surfacePerlinScale = 0.02f;
    public float caveDensityThreshold = 0.45f;
    public bool enableErosionPass = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentFooter]`** | High | Header and footer enclose the serialized inspector into a complete studio card. |
| **`[ComponentBorder]`** | High | Match `BorderRadius` with border framing to align header rounded corners. |
| **`[ComponentNotification]`** | High | System notifications render cleanly directly below or above the header. |
