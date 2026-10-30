# [HierarchyObjectField]

> Draws an interactive object reference field directly on the hierarchy row supporting click-to-ping and drag-and-drop assignment.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyObjectField]` exposes any `UnityEngine.Object`-derived field (`GameObject`, `Component`, `ScriptableObject`, `Material`, `AudioClip`, etc.) as an interactive reference slot embedded directly in the hierarchy row. Driven by `HierarchyObjectFieldRenderer`, it wraps `EditorGUI.ObjectField` inside a sleek, custom-styled container. It renders missing references with alert backgrounds (`MissingColor = "#2A1A1A"`), highlights populated slots, allows drag-and-drop asset assignment, and lets developers click the field to immediately ping the referenced asset in the Project window or Scene.

**The Problem:**
Connecting key assets (prefabs to spawners, target transforms to cameras, sound banks to audio triggers) often requires selecting an object, pinning the Inspector, and dragging assets across distant windows. When references go missing (null reference bugs), scanning dozens of game objects in the hierarchy to find which slot is empty is tedious.

**The Solution:**
Decorating reference fields with `[HierarchyObjectField]`:
- **Direct Hierarchy Assignment:** Drag prefabs or scene objects straight into the hierarchy row without selecting the target GameObject.
- **Instant Click-to-Ping:** Click the slot name to ping and highlight the referenced object in the Project window or Scene hierarchy.
- **Visual Null Alerting:** Highlights unassigned slots in deep red/alert tints so missing references can never be overlooked.
- **Full Undo Support:** Records standard Unity `Undo` transactions in Edit Mode so changes can be reverted with `Ctrl+Z`.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class TargetFollowCamera : MonoBehaviour
{
    [HierarchyObjectField(Width = 110f)]
    public Transform followTarget;
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
| **Render Engine** | `HierarchyObjectFieldRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyObjectFieldAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `BackgroundColor` | `string` | `"#1A1A2A"` | Hex background color of the field when an object reference is assigned. |
| `MissingColor` | `string` | `"#2A1A1A"` | Hex background color of the field when the reference is null. |
| `BorderColor` | `string` | `"#334466"` | Hex outline border color surrounding the slot. |
| `TextColor` | `string` | `"#AACCEE"` | Hex text color for the object name label. |
| `ShowTypeIcon` | `bool` | `true` | Whether to display the object type icon inside the field. |
| `Width` | `float` | `100f` | Width of the object field in pixels. |
| `Height` | `float` | `0f` | Height of the object field in pixels, or `0` for row-adjusted height (capped at 16px). |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `UndoLabel` | `string` | `"Assign Object Reference"` | Undo transaction description registered in Edit Mode. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the object field remains visible and interactive in Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class BossSpawnPortal : MonoBehaviour
{
    [Header("Portal Linking")]
    [HierarchyObjectField(
        Width = 120f, 
        BackgroundColor = "#1E293B", 
        MissingColor = "#450A0A", 
        BorderColor = "#38BDF8", 
        TextColor = "#F1F5F9", 
        XOffset = 6f)]
    public GameObject bossPrefab;

    [Header("Portal Properties")]
    public float activationDelay = 3.5f;
    public bool autoActivateOnStart = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyFieldAlert]`** | High | Combine with field alerts to display a warning icon if the reference remains unassigned. |
| **`[HierarchyAssetThumbnail]`** | High | Use thumbnail previews for texture/sprite fields and object fields for prefabs/components. |
| **`[HierarchyStatusDot]`** | High | Place status dots on the row to reflect overall system readiness alongside reference slots. |
| **Supported Types** | High | Works with any type deriving from `UnityEngine.Object` (`GameObject`, `ScriptableObject`, `MonoBehaviour`, etc.). |
