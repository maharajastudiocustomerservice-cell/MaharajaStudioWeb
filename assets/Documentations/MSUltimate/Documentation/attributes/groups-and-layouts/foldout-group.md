# [FoldoutGroup]

> Groups multiple fields, properties, or methods into a shared collapsible foldout section with persistent state, custom headers, and borders.

---

## 1. Overview & Value Proposition

**What it does:**
Collects multiple fields, properties, or buttons sharing the same `groupName` into a single collapsible foldout container. Features a sleek header bar with an animated foldout toggle arrow, persistent open/closed memory, custom icons, and borders.

**The Problem:**
While `[BoxGroup]` clusters fields into visual cards, those cards remain permanently expanded. For massive configuration screens (like 40+ sound effects or complex AI state trees), having every section permanently open overwhelms the inspector and requires excessive scrolling.

**The Solution:**
Add `[FoldoutGroup("GroupName")]` to multiple members:
- **Shared Collapsible Container:** All members with the same group name collapse and expand together.
- **Persistent State:** Saves the open/closed state so the inspector remains exactly as you left it across selections and domain reloads.
- **Header Customization:** Custom colors, icons, bold text, arrow styles, alignments, and padding.
- **Inner Nesting:** Fields within the foldout group support all MSUltimate drawers (`[MinMaxSlider]`, `[AutoFill]`, `[TagSelector]`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class EnemyAI : MonoBehaviour
{
    [FoldoutGroup("Patrol Behavior")]
    public float patrolSpeed = 3.5f;

    [FoldoutGroup("Patrol Behavior")]
    public float waypointWaitTime = 2.0f;

    [FoldoutGroup("Patrol Behavior")]
    public bool loopWaypoints = true;
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
| **Drawer Resolution** | `FoldoutGroupDrawer` (registered in `DrawerDatabase`) |

---

## 4. Constructors & Parameters

```csharp
public FoldoutGroupAttribute(string groupName)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `groupName` | `string` | *(Required)* | Unique identifier uniting members into this foldout section. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `GroupName` | `string` | *(Set in constructor)* | Unique identifier for the foldout group. |
| `StartOpen` | `bool` | `true` | Whether the foldout begins expanded by default. |
| `HeaderColor` | `string` | `null` | Hex text color for the foldout header. |
| `HeaderBackgroundColor`| `string`| `null`| Hex fill color for the foldout header row. |
| `HeaderBold` | `bool` | `true` | Renders the foldout title in bold text. |
| `HeaderFontSize` | `int` | `0` | Header font size in pixels (`0` = default). |
| `HeaderIcon` | `string` | `null` | Built-in Unity icon name displayed in the header. |
| `HeaderAlignment` | `UiAlignment` | `UiAlignment.Left` | Alignment of the header title text. |
| `HeaderPadding` | `float` | `6f` | Padding on all sides of the header row in pixels. |
| `HeaderBorderWidth` | `float` | `1f` | Header bottom border width in pixels. |
| `HeaderBorderColor` | `string` | `null` | Hex color code for the header bottom border. |
| `ArrowColor` | `string` | `null` | Hex color code for the collapse/expand arrow icon. |
| `ArrowSize` | `int` | `0` | Font size for the arrow indicator (`0` = default 12). |
| `BackgroundColor` | `string` | `null` | Content area background color (hex string). |
| `Padding` | `float` | `5f` | Padding for all sides of the content area in pixels. |
| `PaddingTop` | `float` | `-1f` | Top padding override (`-1` = use `Padding`). |
| `PaddingBottom` | `float` | `-1f` | Bottom padding override (`-1` = use `Padding`). |
| `PaddingLeft` | `float` | `-1f` | Left padding override (`-1` = use `Padding`). |
| `PaddingRight` | `float` | `-1f` | Right padding override (`-1` = use `Padding`). |
| `IndentContent` | `bool` | `true` | Indents child fields inside the foldout body. |
| `IndentAmount` | `float` | `15f` | Indent offset in pixels when `IndentContent` is true. |
| `Gap` | `float` | `2f` | Vertical spacing between child items in pixels. |
| `BorderColor` | `string` | `null` | Hex outline border color. |
| `BorderWidth` | `float` | `1f` | Outer border outline thickness in pixels. |
| `BorderRadius` | `float` | `4f` | Corner radius for the foldout card in pixels. |
| `MarginTop` | `float` | `2f` | Spacing above the foldout group in pixels. |
| `MarginBottom` | `float` | `2f` | Spacing below the foldout group in pixels. |
| `MarginLeft` | `float` | `0f` | Spacing to the left of the foldout group in pixels. |
| `MarginRight` | `float` | `0f` | Spacing to the right of the foldout group in pixels. |
| `Animated` | `bool` | `false` | If true, open/close transitions animate smoothly. |
| `Order` | `int` | `0` | Execution priority in the inspector pipeline (inherited from `ModularAttribute`). |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class BossAIBrain : MonoBehaviour
{
    [FoldoutGroup("Aggro & Perception", HeaderIcon = "d_ViewToolOrbit", HeaderBackgroundColor = "#2c3e50", BorderRadius = 6f)]
    public float sightRadius = 30f;

    [FoldoutGroup("Aggro & Perception")]
    public float fieldOfViewAngle = 120f;

    [FoldoutGroup("Aggro & Perception")]
    public LayerMask obstructionMask;

    [FoldoutGroup("Combat Abilities", HeaderIcon = "d_CustomTool", HeaderBackgroundColor = "#c0392b", StartOpen = false, BorderRadius = 6f)]
    public float meleeAttackDamage = 45f;

    [FoldoutGroup("Combat Abilities")]
    public float enrageHealthThreshold = 0.3f;

    [FoldoutGroup("Combat Abilities")]
    [Button("Force Enrage State")]
    public void ForceEnrage()
    {
        Debug.Log("Boss enrage state triggered manually.");
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Button]` | Supported | Methods marked with `[Button]` can be grouped seamlessly alongside fields. |
| `[ShowIf]` | Supported | Dynamically hides individual fields or the entire foldout group. |
| `[ReadOnly]` | Supported | Individual fields inside the foldout can be locked against edits. |
| Nested Drawers | Supported | Full support for `[MinMaxSlider]`, `[AutoFill]`, and `[TagSelector]` within the group. |
