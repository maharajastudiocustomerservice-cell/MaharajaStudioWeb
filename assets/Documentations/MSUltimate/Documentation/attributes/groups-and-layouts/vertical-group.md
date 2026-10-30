# [VerticalGroup]

> Groups fields, properties, or methods into a named vertical stack container, perfect for multi-column dashboards when nested in horizontal rows.

---

## 1. Overview & Value Proposition

**What it does:**
Declaratively collects multiple members into a distinct vertical column container based on a shared `groupName`. When combined inside a `[HorizontalGroup]`, it enables developers to build complex, multi-column dashboard layouts with scrolling, custom borders, titles, separators, and indentation.

**The Problem:**
Creating balanced multi-column layouts (such as Column 1: Equipment, Column 2: Stats, Column 3: Actions) in Unity inspectors is nearly impossible with standard tools. Fields either stack linearly or get squished across unorganized horizontal rows.

**The Solution:**
Add `[VerticalGroup("ColumnName")]` across your class:
- **Multi-Column Workbenches:** Nest multiple vertical groups inside a horizontal container to produce clean multi-column layouts using nested paths (`Dashboard/Column`).
- **Card Framing & Titles:** Frame columns in border boxes (`Box = true`), give each column a title, and customize corner radii.
- **Collapsible Columns:** Collapse individual vertical panels on demand (`Collapsible = true`).
- **Flexible Spacing, Separators & Scrolling:** Add horizontal separator lines between child items, enable vertical scrolling with `Scrollable = true`, or indent sub-blocks via `IndentLevel`.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class MultiColumnInspector : MonoBehaviour
{
    [HorizontalGroup("SplitLayout")]
    [VerticalGroup("SplitLayout/LeftCol")]
    public string playerName = "Hero";

    [VerticalGroup("SplitLayout/LeftCol")]
    public int playerLevel = 1;

    [VerticalGroup("SplitLayout/RightCol")]
    public float currentHealth = 100f;

    [VerticalGroup("SplitLayout/RightCol")]
    public float currentMana = 50f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Method | Property` |
| **Supported Types** | Any serializable field, property, or method |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Drawer Resolution** | `VerticalGroupDrawer` (registered in `DrawerDatabase`) |

---

## 4. Constructors & Parameters

```csharp
public VerticalGroupAttribute(string groupName, float height = 0f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `groupName` | `string` | *(Required)* | Unique name uniting members into this vertical column. |
| `height` | `float` | `0f` | Explicit height constraint in pixels (`0` = auto). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `GroupName` | `string` | *(Set in constructor)* | Identifying key uniting members in the vertical column. |
| `Height` | `float` | `0f` | Height constraint in pixels (`0` = auto). |
| `Gap` | `float` | `2f` | Vertical gap between child elements in pixels. |
| `Padding` | `float` | `0f` | Uniform padding inside the group container. |
| `PaddingTop` | `float` | `-1f` | Top padding override (`-1` = use `Padding`). |
| `PaddingBottom` | `float` | `-1f` | Bottom padding override (`-1` = use `Padding`). |
| `PaddingLeft` | `float` | `-1f` | Left padding override (`-1` = use `Padding`). |
| `PaddingRight` | `float` | `-1f` | Right padding override (`-1` = use `Padding`). |
| `AlignItems` | `FlexAlign` | `FlexAlign.Stretch` | Cross-axis alignment of children (`Stretch`, `FlexStart`, `Center`, `FlexEnd`). |
| `JustifyContent` | `FlexJustify` | `FlexJustify.FlexStart` | Main-axis alignment of children (`FlexStart`, `Center`, `SpaceBetween`, etc.). |
| `FlexGrow` | `bool` | `false` | Whether the group container expands to fill available space. |
| `FlexShrink` | `bool` | `true` | Whether the group container can shrink below its natural size. |
| `NoWrap` | `bool` | `false` | If true, content will not wrap to a new column. |
| `Width` | `float` | `0f` | Fixed width constraint in pixels (`0` = auto 100%). |
| `MinWidth` | `float` | `0f` | Minimum width constraint in pixels (`0` = none). |
| `MaxWidth` | `float` | `0f` | Maximum width constraint in pixels (`0` = none). |
| `MinHeight` | `float` | `0f` | Minimum height constraint in pixels (`0` = none). |
| `MaxHeight` | `float` | `0f` | Maximum height constraint in pixels (`0` = none). |
| `Box` | `bool` | `false` | Renders a styled background box around the group. |
| `BackgroundColor` | `string` | `null` | Hex fill color when `Box` is enabled. |
| `BorderColor` | `string` | `null` | Hex outline border color. |
| `BorderWidth` | `float` | `0f` | Border outline thickness in pixels. |
| `BorderRadius` | `float` | `0f` | Corner radius for the column card. |
| `HideLabel` | `bool` | `false` | Suppresses field labels for members in this group. |
| `LabelWidth` | `float` | `0f` | Fixed width for field labels in pixels (`0` = auto). |
| `LabelColor` | `string` | `null` | Hex text color override for labels in this group. |
| `LabelFontSize` | `int` | `0` | Font size override for labels in this group (`0` = default). |
| `MarginTop` | `float` | `2f` | Spacing above the group in pixels. |
| `MarginBottom` | `float` | `2f` | Spacing below the group in pixels. |
| `MarginLeft` | `float` | `0f` | Spacing to the left of the group in pixels. |
| `MarginRight` | `float` | `0f` | Spacing to the right of the group in pixels. |
| `Title` | `string` | `null` | Header title displayed at the top of the column. |
| `TitleColor` | `string` | `null` | Hex color code for the title text. |
| `TitleFontSize` | `int` | `0` | Font size for the title text (`0` = default). |
| `TitleBold` | `bool` | `true` | Whether the title text is bold. |
| `TitleAlignment` | `UiAlignment` | `UiAlignment.Left` | Title text alignment (`Left`, `Center`, `Right`). |
| `TitleBackgroundColor`| `string`| `null` | Background color for the title header bar. |
| `TitleIcon` | `string` | `null` | Built-in Unity icon name displayed in the title header. |
| `TitleBorderColor`| `string` | `null` | Border color for the title header bottom edge. |
| `TitleBorderWidth`| `float` | `0f` | Border width for the title header bottom edge. |
| `ShowSeparator` | `bool` | `false` | Draws horizontal separator lines between child items. |
| `SeparatorColor` | `string` | `null` | Hex color code for the separator lines. |
| `SeparatorHeight`| `float` | `1f` | Height/thickness of the separator lines in pixels. |
| `SeparatorMargin`| `float` | `0f` | Horizontal margin (left/right) for the separator line. |
| `Collapsible` | `bool` | `false` | Allows collapsing the entire vertical stack. |
| `StartCollapsed` | `bool` | `false` | Whether the group starts in a collapsed state. |
| `CollapseButtonColor`| `string` | `null` | Hex color code for the collapse toggle button. |
| `Scrollable` | `bool` | `false` | Wraps group content in a scrollable view container. |
| `ScrollDirection`| `ScrollMode` | `ScrollMode.Vertical`| Scroll orientation (`Vertical`, `Horizontal`, `Both`). |
| `IndentLevel` | `int` | `0` | Indent level for child elements (each level = 15px). |
| `Order` | `int` | `0` | Execution priority in the inspector pipeline (inherited from `ModularAttribute`). |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class RPGCharacterSheet : MonoBehaviour
{
    [HorizontalGroup("Dashboard", Gap = 8f)]
    [VerticalGroup("Dashboard/Attributes", Box = true, Title = "Attributes", TitleIcon = "d_SettingsIcon", Padding = 6f)]
    public int strength = 18;

    [VerticalGroup("Dashboard/Attributes")]
    public int dexterity = 14;

    [VerticalGroup("Dashboard/Attributes")]
    public int intelligence = 22;

    [VerticalGroup("Dashboard/Vitals", Box = true, Title = "Vitals", TitleIcon = "d_Favorite", Padding = 6f, ShowSeparator = true)]
    public float healthPoints = 120f;

    [VerticalGroup("Dashboard/Vitals")]
    public float staminaPoints = 80f;

    [VerticalGroup("Dashboard/Vitals")]
    public float manaPoints = 200f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[HorizontalGroup]`| Recommended | Pairs together to form multi-column layouts using nested paths (`Group/Col`). |
| `[Button]` | Supported | Methods marked with `[Button]` stack cleanly within vertical columns. |
| `[ShowIf]` | Supported | Evaluates conditional visibility on individual members or the entire column. |
