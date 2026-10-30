# [OnFieldFocus]

> Invokes a C# callback method when a serialized field or property gains UI focus in the Inspector.

---

## 1. Overview & Value Proposition

**What it does:**
Triggers a method the moment you click on or tab into a specific field in the Inspector.

**The Problem:**
In standard Unity, there is no way to know when a developer is interacting with a specific property. If you want to highlight a relevant scene gizmo, open a contextual preview, or log the previous value before edits start, Unity gives you zero field-focus hooks.

**The Solution:**
Add `[OnFieldFocus]` next to any serialized field or method:
- **Instant Focus Detection:** Runs as soon as the user selects or clicks into the field.
- **Contextual Scene Feedback:** Show specific 3D gizmos or camera framing only when the relevant field is active.
- **Pre-Edit State Caching:** Cache the value before modification begins for custom undo or delta comparison.
- **UI Toolkit Native:** Plugs cleanly into UI Toolkit's native `FocusEvent` system.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CameraWaypoint : MonoBehaviour
{
    [OnFieldFocus(nameof(HighlightWaypoint))]
    public Transform targetNode;

    private void HighlightWaypoint()
    {
        Debug.Log($"Editing waypoint target: {targetNode?.name}");
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Field | AttributeTargets.Property | AttributeTargets.Method` |
| **Supported Types** | Any serializable field type; target method must be parameterless |
| **Allow Multiple** | `true` |
| **Inherited** | `true` |
| **Build Overhead** | Editor-only (Zero runtime build overhead / stripped in builds) |
| **Minimum Unity** | Unity 6 (6000.x)+ |

---

## 4. Constructors & Signatures

```csharp
public OnFieldFocusAttribute(string methodNameOrFieldName)
```
- **`methodNameOrFieldName`**: Name of callback method (when placed on field) or target field (when placed on method).

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MethodName` | `string` | *(Constructor)* | Name of the method to call when focus is gained. |
| `TargetFieldName` | `string` | *(Constructor)* | Target field name to listen for focus events. |
| `Order` | `int` | `0` | Execution priority relative to other attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class TurretZoneController : MonoBehaviour
{
    [Header("Patrol Area")]
    [OnFieldFocus(nameof(EnablePatrolGizmo))]
    [OnFieldBlur(nameof(DisablePatrolGizmo))]
    public float patrolRadius = 15f;

    private bool _showPatrolGizmo;

    private void EnablePatrolGizmo()
    {
        _showPatrolGizmo = true;
        Debug.Log("[Turret] Patrol radius focused: Showing area gizmo in Scene.");
    }

    private void DisablePatrolGizmo()
    {
        _showPatrolGizmo = false;
        Debug.Log("[Turret] Patrol radius blurred: Hiding area gizmo.");
    }

    private void OnDrawGizmosSelected()
    {
        if (_showPatrolGizmo)
        {
            Gizmos.color = Color.yellow;
            Gizmos.DrawWireSphere(transform.position, patrolRadius);
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

- **Pairing with `[OnFieldBlur]`:** Pair together for seamless enter/leave focus control.
- **Sliders & Inputs:** Works with numeric sliders, text inputs, curves, and object pickers.
- **Layouts:** Fully functional inside `[BoxGroup]`, `[TabGroup]`, and vertical stacks.
