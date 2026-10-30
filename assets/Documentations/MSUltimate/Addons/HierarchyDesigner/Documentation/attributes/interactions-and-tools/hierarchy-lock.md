# [HierarchyLock]

> Renders an interactive lock icon directly on the hierarchy row to toggle edit protection and scene picking locks.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyLock]` adds an interactive padlock icon button (`Size = 14f`) to the hierarchy row of GameObjects. Driven by `HierarchyLockRenderer`, clicking the lock icon toggles `HideFlags.NotEditable` on the GameObject. When locked, the icon illuminates in gold (`LockedColor = "#FFD700"`, `LockIcon-On`), preventing accidental transform moves, component deletion, or inspector edits. When unlocked, it renders in dim slate (`UnlockedColor = "#576574"`, `LockIcon`). It optionally cascades lock states recursively down through the entire child hierarchy (`AffectChildren = true`).

**The Problem:**
In production level design, finalized environmental assets, terrain chunks, cinematic cameras, and static lighting rigs should not be moved or edited accidentally. Unity's standard lock is hidden inside inspector menus or scene picking flags, making it easy for artists or designers to accidentally nudge or modify finalized props during selection.

**The Solution:**
Decorating components with `[HierarchyLock]`:
- **Single-Click Lock Protection:** Lock or unlock any entity with one click right in the hierarchy row.
- **Visual Padlock Feedback:** Vibrant gold padlock icon clearly distinguishes locked entities from editable objects.
- **Recursive Child Locking:** Protect entire prefab hierarchies and environment branches simultaneously (`AffectChildren = true`).
- **Complete Undo Integration:** Every lock/unlock action registers with Unity's undo manager (`Undo.RecordObject`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyLock(LockedColor = "#F59E0B", AffectChildren = true)]
public class StaticEnvironmentAsset : MonoBehaviour
{
    public string assetSignature = "ENVIRONMENT_TERRAIN_A";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyLockRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyLockAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `LockedColor` | `string` | `"#FFD700"` | Hex color of the lock icon when the object is locked (`HideFlags.NotEditable`). |
| `UnlockedColor` | `string` | `"#576574"` | Hex color of the lock icon when the object is unlocked. |
| `AffectChildren` | `bool` | `true` | Whether locking cascades recursively to child GameObjects in the transform tree. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the lock button remains visible during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyLock(
    LockedColor = "#EAB308", 
    UnlockedColor = "#475569", 
    AffectChildren = true, 
    XOffset = 6f)]
public class FinalizedCinematicRig : MonoBehaviour
{
    [Header("Cinematic Track")]
    public string cutsceneId = "PROLOGUE_CAMERA";
    public bool isFinalized = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchySeparator]`** | High | Lock separator header objects so child assets cannot be accidentally dragged or reorganized. |
| **`[HierarchyNote]`** | High | Pair with notes explaining why the object is locked (e.g., `"Locked: Baked lighting anchors"`). |
| **`[HierarchyActiveButton]`** | High | Keep the lock icon beside active buttons for comprehensive entity security and control. |
| **`HideFlags.NotEditable`** | High | Directly sets Unity's native `HideFlags.NotEditable` flag; works across all standard Unity editor tools. |
