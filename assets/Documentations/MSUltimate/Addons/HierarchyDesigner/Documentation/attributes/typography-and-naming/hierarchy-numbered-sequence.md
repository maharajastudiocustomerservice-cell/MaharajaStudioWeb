# [HierarchyNumberedSequence]

> Formats sibling GameObject hierarchy names with automatic sequential indices or Roman numerals.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyNumberedSequence]` automatically prepends or formats the GameObject name with its sibling order index, supporting standard numbers (`1, 2, 3`), zero-padded indices (`01, 02, 03`), Roman numerals (`I, II, III`), or hexadecimal notation (`0x01, 0x02`), using a flexible format template like `"[{num}] {name}"`.

**The Problem:**
When designing ordered sequences (such as checkpoint sequences, patrol waypoints, dialogue beat triggers, or inventory slots), developers often have to manually rename GameObjects to maintain order (e.g. `Waypoint_01`, `Waypoint_02`). When re-ordering or inserting a new waypoint, all subsequent items must be laboriously renumbered by hand.

**The Solution:**
Decorating sequential components with `[HierarchyNumberedSequence]`:
- **Dynamic Sibling Indexing:** Queries `transform.GetSiblingIndex() + 1` dynamically at repaint time, meaning reordering objects in the hierarchy immediately updates their displayed sequence number automatically.
- **Multiple Numbering Styles:** Choose from `Standard`, `ZeroPadded`, `RomanNumeral`, or `Hex` formats.
- **Custom Display Templates:** Use placeholders `{num}`, `{roman}`, and `{name}` in custom format strings (e.g. `"STAGE {roman} : {name}"`).
- **Two-Tone Color Highlighting:** Distinguish the sequence number (`NumberColor = "#F39C12"`) from the object name (`TextColor = "#E0E0E0"`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyNumberedSequence(Format = HierarchyNumberFormat.ZeroPadded, Template = "[{num}] {name}")]
public class PatrolWaypoint : MonoBehaviour
{
    public float waitDuration = 2.0f;
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
| **Render Engine** | `HierarchyNumberedSequenceRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyNumberedSequenceAttribute()
```

- Standard parameterless constructor. Numbering format, template, and color parameters are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Format` | `HierarchyNumberFormat` | `ZeroPadded` | Index style: `Standard` (1, 2), `ZeroPadded` (01, 02), `RomanNumeral` (I, II), `Hex` (0x01, 0x02). |
| `Template` | `string` | `"[{num}] {name}"` | Display format template supporting `{num}`, `{roman}`, and `{name}` tokens. |
| `NumberColor` | `string` | `"#F39C12"` | Hex color string applied to index numbers. |
| `TextColor` | `string` | `"#E0E0E0"` | Hex color string applied to the GameObject name. |
| `Bold` | `bool` | `true` | Whether to render the formatted characters with bold font weight. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether dynamic numbering remains visible during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row decorations. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyNumberedSequence(
    Format = HierarchyNumberFormat.RomanNumeral, 
    Template = "ACT {roman} — {name}", 
    NumberColor = "#EAB308", 
    TextColor = "#F8FAFC", 
    Bold = true)]
public class StoryQuestChapterNode : MonoBehaviour
{
    [Header("Quest Progression")]
    public string chapterTitle = "The Forgotten Citadel";
    public bool isCompleted = false;
    public int requiredLevel = 15;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyTreeBranch]`** | High | Excellent synergy: visual tree branches link consecutive numbered waypoints neatly under a parent path. |
| **`[HierarchyTooltip]`** | High | Pair with hover tooltips showing waypoint transit times or trigger conditions. |
| **`[HierarchyBookmark]`** | High | Slot bookmark ribbons on critical chapters/checkpoints without numbering conflicts. |
| **`[HierarchyTextColor]`** | Incompatible | Do not stack with static text color attributes as `[HierarchyNumberedSequence]` renders the full label pass. |
