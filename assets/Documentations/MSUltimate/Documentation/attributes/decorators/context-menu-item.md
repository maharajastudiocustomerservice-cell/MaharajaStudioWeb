# [ContextMenuItem]

> Attaches custom right-click context menu actions directly to a serialized field for quick resets, calculations, or presets.

---

## 1. Overview & Value Proposition

**What it does:**
Adds custom right-click options to a specific field in the Inspector (e.g. right-click to "Randomize Seed" or "Reset to Default").

**The Problem:**
In standard Unity, adding custom contextual actions to a component puts them under the 3 dots menu at the very top of the component header. When an action is directly tied to a specific field (like generating a GUID or resetting an offset), scrolling up to the component header is clunky.

**The Solution:**
Add `[ContextMenuItem]` directly above the target field:
- **Direct Right-Click Menus:** Right-click the field label to open your custom action list.
- **Multiple Actions per Field:** Stack multiple attributes to attach several actions to the same field.
- **Cleaner Inspectors:** Keeps the Inspector uncluttered by hiding rare utility actions behind right-click menus instead of adding large buttons.
- **Full Undo Support:** Changes made by invoked context methods integrate smoothly into Unity's Undo history.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class PlayerProfile : MonoBehaviour
{
    [ContextMenuItem("Generate New Guid", nameof(GenerateGuid))]
    public string profileId = "DEFAULT_PROFILE";

    private void GenerateGuid()
    {
        profileId = System.Guid.NewGuid().ToString("N");
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field, property, array (`T[]`), list (`List<T>`), or dictionary value |
| **Collection Interface** | `ICollectionElementAttribute` (Automatic Element Cascading) |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ContextMenuItemAttribute()
public ContextMenuItemAttribute(string name, string methodName)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `name` | `string` | `null` | Display title of the context menu item in the right-click menu. |
| `methodName` | `string` | `null` | Name of the parameterless C# method to invoke when clicked. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Name` | `string` | `null` | Menu label text. |
| `MethodName` | `string` | `null` | Target method name. |
| `Order` | `int` | `0` | Execution or menu ordering priority. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class TransformPresetRig : MonoBehaviour
{
    [Header("Default Offsets")]
    [ContextMenuItem("Reset to Zero", nameof(ResetOffset))]
    [ContextMenuItem("Snap to Ground (Raycast)", nameof(SnapToGround))]
    public Vector3 spawnOffset = Vector3.up;

    [Header("Direct Collections Cascading")]
    [ContextMenuItem("Re-verify Waypoint", nameof(VerifyWaypoint))]
    public Vector3[] patrolWaypoints = new Vector3[] { Vector3.zero, new Vector3(10, 0, 0) };

    [ContextMenuItem("Refresh Endpoint", nameof(RefreshEndpoint))]
    public List<string> endpointUrls = new List<string> { "https://api.game.io/cluster1" };

    private void ResetOffset()
    {
        spawnOffset = Vector3.zero;
        Debug.Log("[PresetRig] Offset reset to zero.");
    }

    private void SnapToGround()
    {
        if (Physics.Raycast(transform.position, Vector3.down, out var hit, 50f))
        {
            spawnOffset = hit.point - transform.position;
            Debug.Log($"[PresetRig] Snapped offset to ground surface at {hit.point}.");
        }
    }

    private void VerifyWaypoint()
    {
        Debug.Log("[PresetRig] Waypoint verified!");
    }

    private void RefreshEndpoint()
    {
        Debug.Log("[PresetRig] Endpoint connection refreshed!");
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[IconButton]` | Alternative | Use `[IconButton]` for visible 1-click buttons; use `[ContextMenuItem]` to keep UI minimal. |
| `[ReadOnly]` | Supported | Right-click actions still function on read-only fields. |
| `[BoxGroup]` | Supported | Functions normally inside group containers. |

### Collection Cascading Matrix

| Collection / Container Type | Cascading Support | Render Target | Notes |
| :--- | :---: | :--- | :--- |
| `T[]` | ✅ Yes | Individual array elements | Right-clicking on any array element row reveals context menu actions. |
| `List<T>` | ✅ Yes | Individual list items | Each list item row supports right-click contextual actions. |
| `AdvancedList<T>` | ✅ Yes | Individual list rows | Works seamlessly across reorderable items. |
| `SerializableDictionary<K, V>` | ✅ Yes | Dictionary cells | Right-click on key or value cells invokes targeted actions. |
| `SerializableNullable<T>` | ✅ Yes | Inner value | Cascades to nullable payload. |
| `SerializableTuple<...>` | ✅ Yes | Tuple cells | Right-click within tuple cells surfaces context menu. |

