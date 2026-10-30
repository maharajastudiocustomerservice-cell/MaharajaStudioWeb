# [ButtonGroup]

> Clusters multiple method buttons into a coordinated horizontal toolbar or vertical stack with uniform button sizing and styling.

---

## 1. Overview & Value Proposition

**What it does:**
Gathers multiple methods marked as inspector buttons into a unified, aligned button group. Methods sharing the same `groupName` are placed together in a horizontal button strip or vertical stack, ensuring equal button widths, uniform heights, and shared headers.

**The Problem:**
In standard inspector tools, adding multiple buttons to a MonoBehaviour creates large, bulky full-width buttons stacked vertically on top of one another. For complementary actions (like "Play / Pause / Stop", "Load / Save / Reset", or "Next / Previous"), this wastes space and looks unpolished.

**The Solution:**
Add `[ButtonGroup("GroupName")]` to multiple methods:
- **Unified Toolbar Rows:** Places related buttons side-by-side in a sleek, compact toolbar.
- **Equal Width Distribution:** Automatically distributes available inspector width evenly (`EqualWidth = true`).
- **Flexible Orientations:** Supports horizontal toolbars (`UiOrientation.Horizontal`) or vertical column clusters (`UiOrientation.Vertical`).
- **Card Framing & Titles:** Optional surrounding border box (`Box = true`) and group title header with icons.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class TransportControls : MonoBehaviour
{
    [ButtonGroup("Transport")]
    public void PreviousTrack() => Debug.Log("Previous");

    [ButtonGroup("Transport")]
    public void PlayPause() => Debug.Log("Play/Pause");

    [ButtonGroup("Transport")]
    public void NextTrack() => Debug.Log("Next");
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Method` |
| **Supported Types** | Any parameterless or invokable method |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Drawer Resolution** | `ButtonGroupDrawer` (registered in `DrawerDatabase`) |

---

## 4. Constructors & Parameters

```csharp
public ButtonGroupAttribute(string groupName)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `groupName` | `string` | *(Required)* | Shared identifier uniting methods into this button cluster. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `GroupName` | `string` | *(Set in constructor)* | Unique identifier for the button group. |
| `Orientation` | `UiOrientation` | `UiOrientation.Horizontal`| Layout direction (`Horizontal` or `Vertical`). |
| `Gap` | `float` | `4f` | Spacing in pixels between adjacent buttons. |
| `AlignItems` | `FlexAlign` | `FlexAlign.Stretch` | Cross-axis alignment for the group. |
| `JustifyContent` | `FlexJustify` | `FlexJustify.FlexStart` | Main-axis distribution for the group. |
| `EqualWidth` | `bool` | `true` | Forces all buttons in the group to share the same width. |
| `ButtonHeight` | `float` | `0f` | Height override for buttons (`0` = default). |
| `ButtonMinWidth` | `float` | `0f` | Minimum width constraint for individual buttons. |
| `Box` | `bool` | `false` | Renders a styled border card around the button group. |
| `BackgroundColor` | `string` | `null` | Hex fill color for the surrounding container. |
| `BorderColor` | `string` | `null` | Hex border color for the surrounding container. |
| `BorderWidth` | `float` | `0f` | Width of the group container's border in pixels. |
| `BorderRadius` | `float` | `0f` | Corner radius for the container card. |
| `Padding` | `float` | `0f` | Internal padding for the group container in pixels. |
| `MarginTop` | `float` | `0f` | Spacing above the group in pixels. |
| `MarginBottom` | `float` | `2f` | Spacing below the group in pixels. |
| `MarginLeft` | `float` | `0f` | Spacing to the left of the group in pixels. |
| `MarginRight` | `float` | `0f` | Spacing to the right of the group in pixels. |
| `Title` | `string` | `null` | Optional header title text displayed above the group. |
| `TitleColor` | `string` | `null` | Hex color code for the group title text. |
| `TitleFontSize` | `int` | `0` | Font size for the group title (`0` = default). |
| `TitleBold` | `bool` | `true` | Whether the title should be displayed in bold. |
| `TitleIcon` | `string` | `null` | Built-in Unity icon name to display next to the title. |
| `ButtonBackgroundColor`| `string`| `null`| Hex background color applied to every button in this group. |
| `ButtonTextColor` | `string` | `null` | Hex text color applied to every button in this group. |
| `ButtonBorderRadius`| `float` | `0f` | Corner radius applied to every button in this group. |
| `Order` | `int` | `0` | Execution priority in the inspector pipeline (inherited from `ModularAttribute`). |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class GameStateDirector : MonoBehaviour
{
    [ButtonGroup("SaveLoad", 
        Title = "Game State Operations", 
        TitleIcon = "d_SaveAs", 
        Box = true, 
        Padding = 6f, 
        Gap = 6f, 
        ButtonBackgroundColor = "#2c3e50", 
        ButtonTextColor = "#ffffff", 
        ButtonBorderRadius = 4f
    )]
    public void QuickSave()
    {
        Debug.Log("Game state saved to slot 0.");
    }

    [ButtonGroup("SaveLoad")]
    public void QuickLoad()
    {
        Debug.Log("Game state loaded from slot 0.");
    }

    [ButtonGroup("SaveLoad")]
    public void DeleteSave()
    {
        Debug.Log("Save file deleted.");
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[ShowIf]` | Supported | Individual buttons can be conditionally displayed based on game state. |
| `[ReadOnly]` | Supported | Disables specific buttons while keeping others in the group active. |
| `[BoxGroup]` | Supported | Button groups can be embedded directly inside outer `[BoxGroup]` containers. |
| `[BeginTabGroup]` | Supported | Button groups can live within tabbed navigation views. |
