# [HierarchyToggle]

> Draws an interactive checkbox toggle directly on the hierarchy row bound to a boolean field.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyToggle]` binds an interactive toggle checkbox directly to a serialized boolean field on the hierarchy row. Driven by `HierarchyToggleRenderer`, clicking the checkbox flips the boolean value immediately. It supports optional inline text labels (`Label`), custom active state tinting (`ActiveTint`), custom tooltips, and complete Undo integration (`Undo.RecordObject`) in Edit Mode while executing seamlessly in Play Mode.

**The Problem:**
During level design, testing, and debugging, developers frequently need to flip boolean switches (e.g., `enableDebugGizmos`, `isInvulnerable`, `autoSpawn`, `muteSFX`, `drawNavMeshPath`). Opening each GameObject's Inspector to toggle a single boolean takes multiple clicks and breaks debugging focus.

**The Solution:**
Decorating boolean fields with `[HierarchyToggle]`:
- **Single-Click In-Hierarchy Toggling:** Toggle boolean fields on and off with a single click right in the hierarchy row.
- **Accompanying Label Support:** Display a short identifier label (e.g. `"AI"`, `"Debug"`, `"God"`) beside the checkbox.
- **Visual State Feedback:** Clearly see whether the flag is active without selecting the entity.
- **Undo Integration:** Records full Undo history in Edit Mode to ensure accidental toggles can be undone instantly.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class EnemyAI : MonoBehaviour
{
    [HierarchyToggle(Label = "AI Active", ActiveTint = "#10B981")]
    public bool isAiEnabled = true;
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
| **Render Engine** | `HierarchyToggleRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyToggleAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Label` | `string` | `""` | Optional short text label displayed beside the checkbox. |
| `LabelColor` | `string` | `"#AAAAAA"` | Hex color of the text label. |
| `ActiveTint` | `string` | `""` | Hex color tint applied to the checkbox when active/checked. |
| `Size` | `float` | `14f` | Size of the checkbox square in pixels. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `UndoLabel` | `string` | `"Toggle Field"` | Undo transaction description registered in Edit Mode. |
| `Tooltip` | `string` | `""` | Tooltip text displayed when hovering over the toggle checkbox. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the toggle remains visible and interactive in Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class GameplayCameraController : MonoBehaviour
{
    [Header("Debug Controls")]
    [HierarchyToggle(
        Label = "FreeCam", 
        LabelColor = "#38BDF8", 
        ActiveTint = "#06B6D4", 
        Size = 14f, 
        Tooltip = "Toggle free flight debug camera mode", 
        XOffset = 6f)]
    public bool enableFreeCameraMode = false;

    public float moveSpeed = 15f;
    public float lookSensitivity = 2f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyStatusDot]`** | High | Use `HierarchyStatusDot` for passive state feedback and `HierarchyToggle` for interactive boolean toggling. |
| **`[HierarchyActiveButton]`** | High | Use `HierarchyActiveButton` for GameObject active state and `HierarchyToggle` for component-level boolean logic. |
| **Hierarchy Selection** | High | Consumes mouse clicks directly to prevent accidental GameObject selection or name renaming. |
| **Field Types** | High | Specifically designed for `bool` member fields. |
