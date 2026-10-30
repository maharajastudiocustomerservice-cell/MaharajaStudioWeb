# [OnUndoRedo]

> Automatically executes a C# callback method whenever an Undo or Redo operation modifies the target object.

---

## 1. Overview & Value Proposition

**What it does:**
Triggers a method automatically whenever you press `Ctrl+Z` (Undo) or `Ctrl+Y` (Redo) in Unity.

**The Problem:**
In standard Unity, undoing an edit changes serialized field data in the background without notifying custom caching algorithms, mesh generators, or child component linkers. This leaves your scene out of sync with your internal data structures until someone manually modifies another property.

**The Solution:**
Add `[OnUndoRedo]` above your cache rebuild method:
- **Instant Desync Prevention:** Immediately recomputes matrices, procedurally generated meshes, or linked references after an undo.
- **Bi-Directional Safety:** Handles both Undo (`Ctrl+Z`) and Redo (`Ctrl+Y`) operations automatically.
- **Zero Static Listeners:** No need to manually subscribe to `Undo.undoRedoPerformed`.
- **Editor-Only Execution:** Completely excluded from player game builds.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class ProceduralPillar : MonoBehaviour
{
    public float pillarHeight = 3.5f;

    [OnUndoRedo]
    private void OnUndoRedoPerformed()
    {
        Debug.Log($"Undo/Redo detected. Recalculating pillar mesh for height: {pillarHeight}");
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Method | Field | Property` |
| **Supported Types** | Parameterless methods |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public OnUndoRedoAttribute()
public OnUndoRedoAttribute(string methodName)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `methodName` | `string` | `null` | Optional method name when placing the attribute on a field or property instead of directly on the method. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MethodName` | `string` | `null` | Target method name invoked when attribute decorates a field or property. |
| `Order` | `int` | `0` | Execution priority relative to other undo/redo callbacks. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

[ExecuteAlways]
public class GridSnapAligner : MonoBehaviour
{
    [Header("Grid Alignment")]
    [OnValueChanged(nameof(RecalculateSnap))]
    public float snapSize = 1.0f;

    public Vector3 snappedCoordinate;

    [OnUndoRedo]
    private void RecalculateSnap()
    {
        Vector3 currentPos = transform.position;
        snappedCoordinate = new Vector3(
            Mathf.Round(currentPos.x / snapSize) * snapSize,
            Mathf.Round(currentPos.y / snapSize) * snapSize,
            Mathf.Round(currentPos.z / snapSize) * snapSize
        );
        Debug.Log($"[GridSnapAligner] Synchronized snapped position: {snappedCoordinate}");
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[OnValueChanged]` | Supported | Pair together (OnValueChanged on field, OnUndoRedo on callback method) to guarantee synchronization on both user edits and undo operations. |
| `[ReadOnly]` | Supported | Safely display cached values recomputed on undo. |
| `[BoxGroup]` | Supported | Fully functional inside layout containers. |
