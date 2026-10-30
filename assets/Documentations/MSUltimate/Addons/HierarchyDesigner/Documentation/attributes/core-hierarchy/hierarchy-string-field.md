# [HierarchyStringField]

> Draws an inline editable text field directly on the hierarchy row for live string editing without selecting the GameObject.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyStringField]` binds an inline text input box directly onto the hierarchy row for string fields. Driven by `HierarchyStringFieldRenderer`, it uses a unique control ID per component instance to maintain keyboard focus, displays dimmed placeholder text when empty (`PlaceholderText = "..."`), enforces character length caps (`MaxLength`), and applies sleek dark container styling. In Edit Mode, edits register with Unity's Undo system (`Undo.RecordObject`) upon change detection; in Play Mode, string updates apply immediately to live component state.

**The Problem:**
Renaming character titles, dialogue identifiers, localization keys, waypoint handles, or notes typically requires clicking the GameObject, waiting for the Inspector to load, finding the string field, editing it, and deselecting. When modifying dozens of dialogue nodes or spawn waypoints, this back-and-forth disrupts creative flow.

**The Solution:**
Decorating string fields with `[HierarchyStringField]`:
- **Direct Inline Typing:** Edit names, tags, and identifiers right in the hierarchy row without selecting the GameObject.
- **Focus Management:** Keeps typing focus cleanly isolated per row, preventing accidental GameObject renaming.
- **Placeholder Styling:** Shows clean placeholder cues when values are empty.
- **Full Undo Registration:** Supports standard `Ctrl+Z` rollbacks during Edit Mode editing sessions.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class DialogueNode : MonoBehaviour
{
    [HierarchyStringField(PlaceholderText = "Node ID...", Width = 90f)]
    public string nodeId = "INTRO_01";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyStringFieldRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyStringFieldAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `PlaceholderText` | `string` | `"..."` | Placeholder text shown when the field is empty and unfocused. |
| `MaxLength` | `int` | `32` | Maximum character count allowed, or `0` for no limit. |
| `TextColor` | `string` | `"#DDDDDD"` | Hex color of the entered text. |
| `PlaceholderColor` | `string` | `"#666666"` | Hex color of the placeholder prompt text. |
| `BackgroundColor` | `string` | `"#1A1A2A"` | Hex background color of the input field container. |
| `BorderColor` | `string` | `"#334466"` | Hex outline border color around the text box. |
| `ItalicWhenIdle` | `bool` | `false` | Whether to render text in italic when displaying a non-empty value while unfocused. |
| `Width` | `float` | `80f` | Total width of the text input field in pixels. |
| `Height` | `float` | `0f` | Height of the field in pixels, or `0` for auto-sizing (capped at 16px). |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `UndoLabel` | `string` | `"Edit String Field"` | Undo transaction description registered in Edit Mode. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the text field remains visible and editable during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class QuestWaypoint : MonoBehaviour
{
    [Header("Waypoint Data")]
    [HierarchyStringField(
        PlaceholderText = "Objective Tag", 
        MaxLength = 24, 
        Width = 110f, 
        BackgroundColor = "#1E293B", 
        BorderColor = "#6366F1", 
        TextColor = "#F8FAFC", 
        PlaceholderColor = "#64748B", 
        XOffset = 6f)]
    public string objectiveTag = "REACH_CASTLE";

    public float triggerRadius = 3.5f;
    public bool isMandatory = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyToggle]`** | High | Combine string fields with toggles to edit identifiers and active states side-by-side. |
| **`[HierarchyLabel]`** | High | Use `HierarchyLabel` for read-only displays and `HierarchyStringField` for editable strings. |
| **Hierarchy Selection** | High | Consumes click events inside the input rect to prevent accidental GameObject selection or name renaming. |
| **Field Types** | High | Specifically engineered for `string` member fields. |
