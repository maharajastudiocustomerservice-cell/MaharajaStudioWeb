# [HierarchyUnderlineText]

> Draws a styled colored underline, dotted line, dashed rule, or strikethrough stroke beneath or across the hierarchy label.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyUnderlineText]` draws customizable geometric stroke lines beneath or through the GameObject label in the Unity Hierarchy window. Supporting solid lines, dotted patterns, dashed strokes, and strikethrough styling (`LineStyle`), it enables technical artists and scene designers to emphasize critical scene anchors, mark deprecated or disabled entities with strikethroughs, or categorize systems with color-coded underlines.

**The Problem:**
In expansive scenes containing hundreds of GameObjects, standard Unity hierarchy rows offer uniform styling with no typographic weight or visual hierarchy. Identifying marked milestones, deprecation states, or primary game subsystem roots requires manual folder inspection or custom selection tags.

**The Solution:**
Decorating components or fields with `[HierarchyUnderlineText]`:
- **Visual Emphasis & Hierarchy:** Underline primary subsystem roots (e.g. `[GameDirector]`, `[PlayerSpawner]`) with sharp, vivid stroke accents.
- **Deprecation & Strikethrough States:** Mark outdated prefabs or legacy systems scheduled for decommissioning (`LineStyle = HierarchyLineStyle.Strikethrough`) without deleting them from source control.
- **Multiple Stroke Styles:** Choose between `Solid`, `Dotted`, `Dashed`, and `Strikethrough` rules with pixel-perfect stroke thickness (`LineThickness`).
- **Typographic Customization:** Independently style label color (`TextColor`), stroke color (`LineColor`), and font styles (`Bold`, `Italic`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyUnderlineText(
    TextColor = "#FFFFFF",
    LineColor = "#FF5E57",
    LineThickness = 2.0f,
    LineStyle = HierarchyLineStyle.Solid,
    Bold = true)]
public class ObjectiveManager : MonoBehaviour
{
    public string currentObjective = "Defend Core Gateway";
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
| **Render Engine** | `HierarchyUnderlineTextRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyUnderlineTextAttribute()
```

- Parameterless constructor allows flexible property initialization via named property syntax (`TextColor`, `LineColor`, `LineStyle`, `LineThickness`, `Bold`, `Italic`).

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `TextColor` | `string` | `"#E0E0E0"` | Hex color string applied to the GameObject label text. |
| `LineColor` | `string` | `"#FF5E57"` | Hex color string applied to the underline or strikethrough stroke. |
| `LineThickness` | `float` | `1.5f` | Thickness of the drawn stroke line in pixels. |
| `LineStyle` | `HierarchyLineStyle` | `HierarchyLineStyle.Solid` | Stroke geometry style: `Solid`, `Dotted`, `Dashed`, or `Strikethrough`. |
| `Bold` | `bool` | `false` | Whether to render the GameObject label text in bold font weight. |
| `Italic` | `bool` | `false` | Whether to render the GameObject label text in italic slant. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the underline and styling persist during active Play Mode. |
| `Order` | `int` | `0` | Drawing execution order relative to other hierarchy row renderers. |

### `HierarchyLineStyle` Enum Values
- **`Solid`**: Continuous single line beneath the text baseline.
- **`Dotted`**: Equidistant square dot sequence along the baseline.
- **`Dashed`**: Segmented dashes across the length of the label.
- **`Strikethrough`**: Centered horizontal line drawn across the midpoint of the text glyphs.

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

namespace ProjectZero.World
{
    // Deprecated spawner marked with a strikethrough line
    [HierarchyUnderlineText(
        TextColor = "#888888",
        LineColor = "#FF3838",
        LineThickness = 1.8f,
        LineStyle = HierarchyLineStyle.Strikethrough,
        Italic = true)]
    public class LegacyEnemySpawner : MonoBehaviour
    {
        [Tooltip("Deprecated spawner scheduled for removal in milestone v2.4.")]
        public string deprecationNotice = "Migrate to ModularEnemySpawner";
    }

    // Critical root hub emphasized with a golden solid underline
    [HierarchyUnderlineText(
        TextColor = "#FFF200",
        LineColor = "#FF9F1A",
        LineThickness = 2.5f,
        LineStyle = HierarchyLineStyle.Solid,
        Bold = true)]
    public class LevelHubController : MonoBehaviour
    {
        public int activeSector = 1;
        public bool isCheckpointActive = true;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyTooltip]`** | High | Pair underlines with rich hover documentation explaining deprecation or anchor importance. |
| **`[HierarchyIcon]`** | High | Icon is rendered alongside the underlined label without overlapping the underline stroke. |
| **`[HierarchyFolder]`** | High | Underline folder titles to designate master root category folders from subfolders. |
| **`[HierarchyBookmark]`** | High | Bookmark ribbon pairs on the right margin while the underline anchors the left title text. |
