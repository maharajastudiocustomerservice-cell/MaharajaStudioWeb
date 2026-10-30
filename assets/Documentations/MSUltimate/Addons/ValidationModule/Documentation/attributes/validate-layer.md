# [ValidateLayer]

> Validates that an integer or string field represents a valid, defined Unity Layer in the project settings.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateLayer]` inspects integer (`int`) or string fields representing Unity Layers. It verifies against Unity's `LayerMask.LayerToName` and `LayerMask.NameToLayer` tables that the integer index (0–31) or string name corresponds to an actual defined Layer in `Project Settings > Tags and Layers`. If an undefined layer index or string is entered, an immediate error banner is displayed.

**The Problem:**
In physics raycasts, camera culling masks, and collision detection systems, developers often store layer indices as raw integers (e.g. `public int collisionLayer = 8;`) or strings. If someone deletes a custom layer in Project Settings, renames it, or types a layer index that does not exist, physics raycasts and layer masks fail silently, causing gameplay triggers and collision detections to stop firing.

**The Solution:**
Decorating layer fields with `[ValidateLayer]`:
- **Project Settings Synchronization:** Verifies that the layer exists in the active project's layer table.
- **Supports Integers and Strings:** Validates both numeric layer indices (`0..31`) and string layer names (`"Player"`, `"Water"`).
- **Catches Renamed/Deleted Layers:** Immediately warns developers if an asset references a layer that was removed in project settings.
- **Clear Error Reporting:** Informs the developer that the specified layer index or name is invalid.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class BulletPhysics : MonoBehaviour
{
    [ValidateLayer("Configured impact layer is not defined in Project Settings.")]
    public int impactLayer = 8;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ValidationModule Addon |
| **Attribute Target** | `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Inspector & Validation Engine Window |
| **Validation Interface** | `IValidationAttribute`, `ICollectionElementAttribute` |

---

## 4. Constructors & Parameters

```csharp
public ValidateLayerAttribute(string message = "Invalid Unity Layer.")
```

- **`message`** (`string`, optional): Custom error message displayed if the layer is not defined in Project Settings.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Message` | `string` | `"Invalid Unity Layer."` | Failure explanation displayed in the validation message banner. |
| `MessageType` | `InspectorMessageType` | `InspectorMessageType.Error` | Visual severity badge (`None`, `Info`, `Warning`, `Error`). |
| `ErrorColor` | `string` | `null` | Hex text color override for the validation error banner. |
| `ErrorBackgroundColor` | `string` | `null` | Hex background color override for the alert box. |
| `FontSize` | `int` | `0` | Font size override in pixels (0 uses default inspector font size). |
| `Padding` | `float` | `0f` | Internal padding around the validation banner. |
| `Margin` | `float` | `5f` | Outer margin spacing separating the banner from neighboring controls. |

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.ValidationModule;

namespace ProjectZero.Physics
{
    public class GroundSensor : MonoBehaviour
    {
        [Header("Ground Detection Layer")]
        [ValidateLayer("Ground layer index must be a defined layer in Tags & Layers settings.",
            MessageType = InspectorMessageType.Error)]
        public int groundLayer = 0;

        [Header("Obstacle Layer Tag")]
        [ValidateLayer("Obstacle layer name is undefined.")]
        public string obstacleLayerName = "Default";

        public bool CheckGroundContact()
        {
            return Physics.Raycast(transform.position, Vector3.down, 1.2f, 1 << groundLayer);
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[Layer]` / `[LayerSelector]`**| High | Pair standard visual layer dropdown drawers with backend layer validation. |
| **`[ValidateTag]`** | High | Validate Unity Tags and Unity Layers side-by-side on gameplay filters. |
| **`[ValidateIf]`** | High | Conditionally validate layer indices based on active physics detection mode. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans. |

### Collection Cascading & Serializer Matrix

| Collection / Container Type | Supported | Behavior |
| :--- | :---: | :--- |
| **`List<int>` / `List<string>`** | Yes | Cascades to validate every layer index or layer name in the list. |
| **`int[]` / `string[]`** | Yes | Cascades to validate each array item exists in project LayerMask. |
| **`AdvancedList<int>`** | Yes | Full element-level validation support with dynamic item reordering. |
| **`SerializableDictionary<K, int>`** | Yes | Validates layer indices when applied to value elements. |
| **`SerializableNullable<int>`** | Yes | Validates wrapped layer index when populated. |
| **`SerializableTuple<...>`** | Yes | Validates layer fields within tuple members. |
