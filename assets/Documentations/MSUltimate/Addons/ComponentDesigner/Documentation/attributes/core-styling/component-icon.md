# [ComponentIcon]

> Renders a prominent visual icon emblem card above the component inspector with support for built-in Unity editor icons, color tinting, and descriptive sub-labels.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentIcon]` anchors an eye-catching emblem banner at the top of the component card (`ComponentSlot.BeforeContent`, `Order = 25`). Centering a large graphic icon (`Icon`, `IconSize` defaulting to 48px), it visually brands key game systems. It supports Unity built-in editor icons, custom icon color tinting (`TintColor`), an optional centered descriptive label (`Label`, `LabelColor`, `LabelFontSize`, `LabelFontStyle`), customizable background plate styling (`BackgroundColor`), rounded top corners (`BorderRadius`), and internal padding (`Padding`).

**The Problem:**
Text-heavy component inspectors can blur together during intense level design and balancing passes. Level designers and technical artists scanning inspector hierarchies often waste time reading class names rather than immediately recognizing components by iconic visual symbols.

**The Solution:**
Decorating core systems with `[ComponentIcon]`:
- **Large Emblem Presentation:** Features large 48px emblem icons that establish immediate visual category recognition across inspectors.
- **Built-In Icon Catalog:** References any Unity editor icon (e.g. `"Camera Icon"`, `"AudioSource Icon"`, `"d_FilterByType"`, `"d_SceneAsset Icon"`).
- **Sub-Label Support:** Accompanies emblems with concise role descriptions (e.g. `"PLAYER WEAPON ARSENAL"`).
- **Custom Tinting:** Colorizes icons to harmonize with specific gameplay factions or UI color palettes.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentIcon("d_SceneViewCamera", IconSize = 40f, Label = "Virtual Cinemachine Rig")]
public class OrbitCameraRig : MonoBehaviour
{
    public Transform targetFocus;
    public float fieldOfView = 60f;
    public float dampingSpeed = 5f;
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
| **Component Slot** | `BeforeContent` (`Order = 25`) |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentIconAttribute(string icon)
```

- `icon`: The Unity built-in icon identifier string (e.g. `"d_Settings Icon"`).

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Icon` | `string` | *(Constructor)* | Unity built-in editor icon name. |
| `IconSize` | `float` | `48f` | Dimension (width and height) of the rendered icon in pixels. |
| `Label` | `string` | `""` | Optional caption label text displayed below the icon. |
| `BackgroundColor` | `string` | `"#1A1A2E"` | Hex background color string for the emblem card area. |
| `TintColor` | `string` | `""` | Hex tint color string applied to the icon image. If empty, uses original icon color. |
| `LabelColor` | `string` | `"#8888AA"` | Hex color string for the caption label text. |
| `LabelFontSize` | `int` | `11` | Font size in points for the caption label. |
| `LabelFontStyle` | `FontStyle` | `FontStyle.Normal` | Font style for caption text (`Normal`, `Bold`, `Italic`). |
| `Padding` | `float` | `12f` | Internal padding in pixels around the emblem. |
| `BorderRadius` | `float` | `6f` | Top-left and top-right corner rounding in pixels. |
| `MarginBottom` | `float` | `4f` | Bottom margin spacing below the icon banner. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#6366F1", Width = 1.5f, Radius = 8f)]
[ComponentBackground("#0E0E24", BorderRadius = 8f, Padding = 10f)]
[ComponentIcon("d_Favorite", IconSize = 44f, Label = "HERO TALENT MATRIX", BackgroundColor = "#161638", TintColor = "#818CF8", LabelColor = "#C7D2FE", LabelFontSize = 12, LabelFontStyle = FontStyle.Bold, BorderRadius = 8f)]
public class HeroTalentMatrix : MonoBehaviour
{
    [Header("Hero Specialization")]
    public string primaryTalentTree = "Aether Vanguard";
    public int allocatedSkillPoints = 28;
    public int unspentTalentPoints = 4;

    [Header("Perk Modifiers")]
    public float critDamageBonusMultiplier = 1.45f;
    public bool enableUltimateCooldownRefund = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBorder]`** | High | Matches corner radius with `BorderRadius` for clean outer containment. |
| **`[ComponentFooter]`** | High | Creates a bookended inspector with an icon emblem at top and metadata at the bottom. |
| **Inspector Controls** | High | Injected cleanly into `BeforeContent`, leaving all serialized inspector elements fully accessible below. |
