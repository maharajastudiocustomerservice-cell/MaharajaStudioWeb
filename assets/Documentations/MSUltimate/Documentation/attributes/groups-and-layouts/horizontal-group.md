# [HorizontalGroup]

> Declaratively groups fields, properties, or buttons side-by-side into a named horizontal row with explicit column widths and flexbox alignment.

---

## 1. Overview & Value Proposition

**What it does:**
Declaratively aligns multiple serialized members side-by-side into a horizontal row. Unlike imperative `[BeginHorizontal]` / `[EndHorizontal]` pairs, `[HorizontalGroup]` works declaratively by clustering all members sharing the same `groupName`, with optional per-field column widths (`Width`).

**The Problem:**
Placing multiple related properties on the same line (such as X/Y offsets, Min/Max thresholds, or paired health and mana bars) using standard Unity requires custom property drawers or awkward GUI code.

**The Solution:**
Add `[HorizontalGroup("GroupName")]` to any member:
- **Declarative Grouping:** Simply assign the same group name; MSUltimate automatically forms the row without requiring ending tags.
- **Explicit Column Widths:** Pass pixel widths (e.g. `120f`) or proportional flex fractions (`0.5f`) per column.
- **Flexbox Alignment:** Control cross-axis alignment (`AlignItems`) and horizontal distribution (`JustifyContent`).
- **Responsive Label Control:** Hide labels (`HideLabel = true`), set fixed label widths (`LabelWidth`), or configure responsive vertical stacking (`LayoutMode`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class BoundsConfig : MonoBehaviour
{
    [HorizontalGroup("BoundsRow", 100f)]
    public float minLimit = 0f;

    [HorizontalGroup("BoundsRow", 100f)]
    public float maxLimit = 100f;
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
| **Drawer Resolution** | `HorizontalGroupDrawer` (registered in `DrawerDatabase`) |

---

## 4. Constructors & Parameters

```csharp
public HorizontalGroupAttribute(string groupName, float width = 0f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `groupName` | `string` | *(Required)* | Unique name uniting members into this horizontal row. |
| `width` | `float` | `0f` | Explicit column width in pixels, or flex ratio (`0` = auto). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `GroupName` | `string` | *(Set in constructor)* | Unique identifier uniting members in the row. |
| `Width` | `float` | `0f` | Column width in pixels or flex fraction. |
| `Gap` | `float` | `5f` | Spacing in pixels between items in the row. |
| `Align` | `UiAlignment` | `UiAlignment.Center` | Alignment of items within the row. |
| `Box` | `bool` | `false` | Renders a styled background box around the group. |
| `BackgroundColor` | `string` | `null` | Hex fill color when `Box` is enabled. |
| `Padding` | `float` | `0f` | Internal padding inside the group container. |
| `NoWrap` | `bool` | `false` | Prevents items from wrapping if row width is exceeded. |
| `HideLabel` | `bool` | `false` | Suppresses field labels to maximize control input width. |
| `LabelWidth` | `float` | `0f` | Explicit width allocated for item labels. |
| `LayoutMode` | `LabelLayoutMode`| `LabelLayoutMode.Default`| Label layout mode (`AdaptiveInline`, `ResponsiveStack`, `AlwaysStacked`, `StandardUnity`). |
| `StackBreakpoint` | `float` | `0f` | Slot width below which items stack vertically when `ResponsiveStack` is active. |
| `Height` | `float` | `0f` | Fixed height for the horizontal group container (`0` = auto). |
| `MinHeight` | `float` | `0f` | Minimum height constraint in pixels. |
| `MaxHeight` | `float` | `0f` | Maximum height constraint in pixels. |
| `MinWidth` | `float` | `0f` | Minimum width constraint in pixels. |
| `MaxWidth` | `float` | `0f` | Maximum width constraint in pixels. |
| `AlignItems` | `FlexAlign` | `FlexAlign.Center` | Cross-axis alignment (`Center`, `FlexStart`, `FlexEnd`, `Stretch`). |
| `JustifyContent` | `FlexJustify` | `FlexJustify.FlexStart` | Main-axis distribution (`FlexStart`, `Center`, `SpaceBetween`, etc.). |
| `MarginTop` | `float` | `0f` | Spacing above the group in pixels. |
| `MarginBottom` | `float` | `2f` | Spacing below the group in pixels. |
| `MarginLeft` | `float` | `0f` | Spacing to the left of the group in pixels. |
| `MarginRight` | `float` | `0f` | Spacing to the right of the group in pixels. |
| `BorderColor` | `string` | `null` | Hex border outline color. |
| `BorderWidth` | `float` | `0f` | Border outline thickness in pixels. |
| `BorderRadius` | `float` | `0f` | Border corner radius in pixels. |
| `Title` | `string` | `null` | Optional header title rendered above the row. |
| `TitleColor` | `string` | `null` | Hex text color for the group title. |
| `TitleFontSize` | `int` | `0` | Font size for the group title (`0` = default). |
| `TitleBold` | `bool` | `true` | Whether the group title text is bold. |
| `TitleAlignment` | `UiAlignment` | `UiAlignment.Left` | Text alignment of the group title. |
| `TitleBackgroundColor`| `string`| `null` | Hex background color for the title header bar. |
| `TitleIcon` | `string` | `null` | Built-in Unity icon name displayed beside the title. |
| `Collapsible` | `bool` | `false` | Enables a toggle button to collapse/expand the entire row. |
| `StartCollapsed` | `bool` | `false` | Whether the group starts collapsed by default. |
| `CollapseButtonColor`| `string` | `null` | Hex color code for the collapse toggle button. |
| `Order` | `int` | `0` | Execution priority in the inspector pipeline (inherited from `ModularAttribute`). |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class PlayerMovementRig : MonoBehaviour
{
    [HorizontalGroup("SpeedConfig", Title = "Locomotion Speeds", Box = true, Padding = 6f)]
    public float walkSpeed = 4.5f;

    [HorizontalGroup("SpeedConfig")]
    public float runSpeed = 8.0f;

    [HorizontalGroup("SpeedConfig")]
    public float sprintSpeed = 12.5f;

    [Header("Quick Preset Buttons")]
    [HorizontalGroup("PresetButtons", Gap = 8f)]
    [Button("Set Stealth")]
    public void SetStealth() => walkSpeed = 2f;

    [HorizontalGroup("PresetButtons")]
    [Button("Set Combat")]
    public void SetCombat() => walkSpeed = 5f;

    [HorizontalGroup("PresetButtons")]
    [Button("Set Sprint")]
    public void SetSprint() => walkSpeed = 10f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Button]` | Supported | Methods marked with `[Button]` can share rows with fields or form button toolbars. |
| `[VerticalGroup]` | Supported | Pairs with `[VerticalGroup]` to build sophisticated multi-column layouts. |
| `[ShowIf]` | Supported | Conditionally hides individual columns without breaking adjacent columns. |
