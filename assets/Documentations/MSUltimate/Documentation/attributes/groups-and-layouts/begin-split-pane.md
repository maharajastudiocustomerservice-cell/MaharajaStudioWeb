# [BeginSplitPane]

> Divides the Inspector into two resizable panes (left/right or top/bottom) with interactive dragging, custom headers, and minimum size constraints.

---

## 1. Overview & Value Proposition

**What it does:**
Opens a dual-pane resizable layout container in the Inspector. Divides controls into two distinct regions (Pane 1 and Pane 2) separated by a draggable splitter handle. Fields declared after the initial `[BeginSplitPane]` populate Pane 1. A second `[BeginSplitPane("GroupName")]` switches into Pane 2, and `[EndSplitPane]` seals the dual-pane container so subsequent members return to standard full-width layout flow.

**The Problem:**
Complex components—such as character setup workbenches, inventory managers, or dialogue editors—often benefit from master-detail workflows (e.g. list of items on the left, properties of the selected item on the right). Standard Unity inspectors only support one vertical column, forcing endless scrolling between lists and item details.

**The Solution:**
Add `[BeginSplitPane("GroupName")]` paired with a second `[BeginSplitPane("GroupName")]` and `[EndSplitPane]`:
- **Interactive Splitter:** Draggable separator handle with customizable hover effects, thickness, and margin.
- **Horizontal & Vertical Split:** Supports side-by-side (`UiOrientation.Horizontal`) or stacked dual panes (`UiOrientation.Vertical`).
- **Independent Scrolling & Minimum Sizes:** Protect panes from collapsing below readable limits via `PaneMinSize`, `Pane1ScrollMode`, and `Pane2ScrollMode`.
- **Custom Pane Titles & Cards:** Decorate each pane with its own title header, icon, background colors, and border styling.
- **Collapsible Panes:** Enable 1-click collapse arrows on either pane via `ShowCollapseButtons`, `Pane1Collapsible`, or `Pane2Collapsible`.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class MasterDetailInspector : MonoBehaviour
{
    // Pane 1: Master Overview
    [BeginSplitPane("CharacterSplit", InitialSplitterPosition = 180f)]
    public string characterName = "Knight";
    public int characterLevel = 10;

    // Pane 2: Detail Properties
    [BeginSplitPane("CharacterSplit")] // Switches to Pane 2
    public int healthPoints = 100;
    [EndSplitPane]
    public int manaPoints = 50;

    // Renders full-width below the split pane
    public bool isHeroic = true;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property | Method` |
| **Supported Types** | Any member placed within split layout scopes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Drawer Resolution** | Handled natively by MSUltimate Inspector layout engine |

---

## 4. Constructors & Parameters

```csharp
public BeginSplitPaneAttribute(string groupName)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `groupName` | `string` | *(Required)* | Unique identifier string for the split pane container. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `GroupName` | `string` | *(Set in constructor)* | Unique identifier for the split container. |
| `Direction` | `UiOrientation` | `UiOrientation.Horizontal` | Orientation of the split (`Horizontal` or `Vertical`). |
| `FixedPaneIndex` | `int` | `0` | Which pane retains fixed size during resizing (`0` = Pane 1, `1` = Pane 2, `-1` = proportional). |
| `InitialSplitterPosition` | `float` | `200f` | Default starting position of the splitter handle in pixels. |
| `PaneMinSize` | `float` | `100f` | Minimum pixel size allowed for either pane during resizing. |
| `Height` | `float` | `0f` | Explicit pixel height for the container (`0` = auto). |
| `MinHeight` | `float` | `0f` | Minimum height constraint for the container. |
| `MaxHeight` | `float` | `0f` | Maximum height constraint for the container. |
| `Width` | `float` | `0f` | Explicit pixel width for the container (`0` = auto 100%). |
| `MarginTop` | `float` | `5f` | Spacing above the container in pixels. |
| `MarginBottom` | `float` | `5f` | Spacing below the container in pixels. |
| `MarginLeft` | `float` | `0f` | Spacing to the left of the container in pixels. |
| `MarginRight` | `float` | `0f` | Spacing to the right of the container in pixels. |
| `BackgroundColor` | `string` | `null` | Hex fill color for the overall container background. |
| `BorderColor` | `string` | `null` | Hex outline border color for the overall container. |
| `BorderWidth` | `float` | `0f` | Border outline width for the overall container. |
| `BorderRadius` | `float` | `0f` | Corner radius for the overall container. |
| `SplitterColor` | `string` | `null` | Hex color code for the splitter handle. |
| `SplitterHoverColor` | `string` | `null` | Hex color code when hovering over the splitter handle. |
| `SplitterThickness` | `float` | `2f` | Width/thickness of the draggable separator handle in pixels. |
| `SplitterBorderRadius` | `float` | `0f` | Corner radius for the splitter handle. |
| `SplitterMargin` | `float` | `0f` | Margin around the splitter handle in pixels. |
| `Pane1Title` | `string` | `null` | Title text displayed at the top of Pane 1. |
| `Pane1TitleColor` | `string` | `null` | Hex color code for the first pane title text. |
| `Pane1TitleFontSize` | `int` | `0` | Font size for the first pane title text (`0` = default). |
| `Pane1TitleBold` | `bool` | `true` | Whether the first pane title is bold. |
| `Pane1TitleAlignment` | `UiAlignment` | `UiAlignment.Left` | Alignment of the first pane title header. |
| `Pane1TitleBackgroundColor` | `string` | `null` | Hex background color for the first pane header row. |
| `Pane1TitleIcon` | `string` | `null` | Built-in Unity icon name for the first pane title. |
| `Pane2Title` | `string` | `null` | Title text displayed at the top of Pane 2. |
| `Pane2TitleColor` | `string` | `null` | Hex color code for the second pane title text. |
| `Pane2TitleFontSize` | `int` | `0` | Font size for the second pane title text (`0` = default). |
| `Pane2TitleBold` | `bool` | `true` | Whether the second pane title is bold. |
| `Pane2TitleAlignment` | `UiAlignment` | `UiAlignment.Left` | Alignment of the second pane title header. |
| `Pane2TitleBackgroundColor` | `string` | `null` | Hex background color for the second pane header row. |
| `Pane2TitleIcon` | `string` | `null` | Built-in Unity icon name for the second pane title. |
| `Pane1BackgroundColor` | `string` | `null` | Hex fill color for Pane 1 body area. |
| `Pane1Padding` | `float` | `5f` | Internal padding inside Pane 1 in pixels. |
| `Pane1BorderColor` | `string` | `null` | Hex border color for Pane 1. |
| `Pane1BorderWidth` | `float` | `0f` | Border width for Pane 1 in pixels. |
| `Pane1BorderRadius` | `float` | `0f` | Corner radius for Pane 1 border in pixels. |
| `Pane1MinWidth` | `float` | `0f` | Minimum pixel width constraint for Pane 1. |
| `Pane1MinHeight` | `float` | `0f` | Minimum pixel height constraint for Pane 1. |
| `Pane2BackgroundColor` | `string` | `null` | Hex fill color for Pane 2 body area. |
| `Pane2Padding` | `float` | `5f` | Internal padding inside Pane 2 in pixels. |
| `Pane2BorderColor` | `string` | `null` | Hex border color for Pane 2. |
| `Pane2BorderWidth` | `float` | `0f` | Border width for Pane 2 in pixels. |
| `Pane2BorderRadius` | `float` | `0f` | Corner radius for Pane 2 border in pixels. |
| `Pane2MinWidth` | `float` | `0f` | Minimum pixel width constraint for Pane 2. |
| `Pane2MinHeight` | `float` | `0f` | Minimum pixel height constraint for Pane 2. |
| `Pane1ScrollMode` | `ScrollMode` | `ScrollMode.Vertical` | Scrolling behavior for Pane 1 (`Vertical`, `Horizontal`, `Both`, `None`). |
| `Pane2ScrollMode` | `ScrollMode` | `ScrollMode.Vertical` | Scrolling behavior for Pane 2 (`Vertical`, `Horizontal`, `Both`, `None`). |
| `ShowCollapseButtons` | `bool` | `false` | Renders 1-click collapse arrows on the panes. |
| `Pane1Collapsible` | `bool` | `false` | Allows Pane 1 to be collapsed via toggle. |
| `Pane2Collapsible` | `bool` | `false` | Allows Pane 2 to be collapsed via toggle. |
| `Pane1StartCollapsed` | `bool` | `false` | Whether Pane 1 starts collapsed by default. |
| `Pane2StartCollapsed` | `bool` | `false` | Whether Pane 2 starts collapsed by default. |
| `CollapseButtonColor` | `string` | `null` | Hex color code for the collapse/expand buttons. |
| `Order` | `int` | `0` | Execution priority in the inspector pipeline (inherited from `ModularAttribute`). |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class SkillTreeWorkbench : MonoBehaviour
{
    [Header("Master-Detail Skill Configuration")]
    // Pane 1: Skill Summary & Identity
    [BeginSplitPane("SkillSplit", 
        Direction = UiOrientation.Horizontal, 
        InitialSplitterPosition = 220f, 
        PaneMinSize = 120f,
        Pane1Title = "Skill Identification",
        Pane1TitleIcon = "d_FilterByLabel",
        Pane2Title = "Combat Attributes",
        Pane2TitleIcon = "d_SettingsIcon",
        SplitterThickness = 3f,
        SplitterColor = "#3498db"
    )]
    public string skillId = "SKL_METEOR_01";
    public string displayName = "Meteor Swarm";
    public Sprite skillIcon;

    // Pane 2: Combat Numerical Balancing
    [BeginSplitPane("SkillSplit")] // Transitions to Pane 2
    public int manaCost = 75;
    public float cooldownTime = 12.5f;
    public float areaOfEffectRadius = 8f;
    [EndSplitPane]
    public LayerMask targetLayers;

    // Full-width controls outside the split pane
    [Header("Global System Overrides (Full Width)")]
    public bool debugDrawTargetVolume = false;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BeginSplitPane]` (2nd Call) | Mandatory | To transition into Pane 2, apply `[BeginSplitPane("GroupName")]` to the first field of Pane 2. |
| `[EndSplitPane]` | Required | Must be closed with `[EndSplitPane]` on the final member of Pane 2. |
| `[TableList]` | Supported | Sits comfortably inside Pane 1 to act as a master selection list. |
| `[BoxGroup]` | Supported | Individual panes can host nested `[BoxGroup]` containers. |
| `[ShowIf]` | Supported | Members inside panes retain conditional visibility logic. |
