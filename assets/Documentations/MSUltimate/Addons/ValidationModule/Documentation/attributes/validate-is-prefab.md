# [ValidateIsPrefab]

> Validates that an assigned object reference is a persistent project Prefab asset, rejecting temporary scene instances.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateIsPrefab]` inspects assigned `GameObject` or `Component` fields that are intended to be instantiated at runtime (such as bullet templates, enemy spawn prefabs, particle FX templates, or UI popup prefabs). It verifies using `PrefabUtility` that the reference is a genuine source Prefab asset located in the Project window (`PrefabAssetType.Regular`, `Model`, or `Variant`), displaying an error banner if a user drags a temporary scene instance into the slot.

**The Problem:**
In spawner and factory patterns, developers intend to instantiate a persistent Prefab asset. However, Unity's inspector allows dragging GameObjects directly from the active Hierarchy window into the prefab field. If a level designer accidentally assigns a scene instance instead of the project prefab, runtime instantiation clones the scene object (which may be destroyed, mutated, or missing in other scenes), causing catastrophic cross-scene reference corruption and missing prefab links.

**The Solution:**
Decorating template fields with `[ValidateIsPrefab]`:
- **Prefab Asset Enforcement:** Guarantees that only persistent project Prefab assets can be assigned.
- **Rejects Scene Instances:** Catches accidental drag-and-drops from the Hierarchy window immediately.
- **Prevents Cross-Scene Leaks:** Ensures spawners and pool managers always instantiate immutable asset sources.
- **Clear Error Messaging:** Distinct error banner explaining that project assets are required.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class EnemySpawner : MonoBehaviour
{
    [ValidateIsPrefab("Enemy spawn template must be a Prefab asset from the Project window.")]
    public GameObject enemyPrefab;
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
public ValidateIsPrefabAttribute(string message = "Reference must be a Prefab Asset from the Project, not a Scene instance.")
```

- **`message`** (`string`, optional): Custom error message displayed if a scene instance or invalid object is assigned.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Message` | `string` | `"Reference must be a Prefab Asset..."` | Failure explanation displayed in the validation message banner. |
| `MessageType` | `InspectorMessageType` | `InspectorMessageType.Error` | Visual severity badge (`None`, `Info`, `Warning`, `Error`). |
| `ErrorColor` | `string` | `null` | Hex text color override for the validation error banner. |
| `ErrorBackgroundColor` | `string` | `null` | Hex background color override for the alert box. |
| `FontSize` | `int` | `0` | Font size override in pixels (0 uses default inspector font size). |
| `Padding` | `float` | `0f` | Internal padding around the validation banner. |
| `Margin` | `float` | `5f` | Outer margin spacing separating the banner from neighboring controls. |

---

## 6. Real-World Production Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.ValidationModule;

namespace ProjectZero.Combat
{
    public class WeaponMuzzleFlash : MonoBehaviour
    {
        [Header("Spawn Templates")]
        [ValidateIsPrefab("Muzzle FX template must be a persistent project Prefab.", 
            MessageType = InspectorMessageType.Error)]
        public GameObject muzzleFlashFxPrefab;

        [ValidateIsPrefab("Shell casing template must be a project Prefab.")]
        public GameObject spentCasingPrefab;

        [Header("Direct Collection Cascading")]
        [ValidateIsPrefab]
        [Tooltip("Cascades prefab assertion to each GameObject spawn template in the array.")]
        public GameObject[] enemySpawnPrefabs;

        [ValidateIsPrefab]
        [Tooltip("Cascades prefab asset validation to each entry in the prop prefab list.")]
        public List<GameObject> environmentalPropPrefabs = new List<GameObject>();

        public void SpawnMuzzleEffect(Vector3 socketPosition, Quaternion socketRotation)
        {
            if (muzzleFlashFxPrefab != null)
                Instantiate(muzzleFlashFxPrefab, socketPosition, socketRotation);
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

### 7.1 Layout & Conditional Stacking

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateIsSceneObject]`** | Inverse | Exact complement: use `[ValidateIsSceneObject]` when scene instances are required. |
| **`[ValidateInFolder]`** | High | Guarantee the assigned prefab is located inside designated prefab folders. |
| **`[Required]` / `[NotNull]`** | High | Ensure reference is assigned before validating prefab asset status. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans via `ValidateIsPrefabRule`. |

### 7.2 Collection Cascading & Serializer Behavior Matrix

| Target Context | Support Status | Architecture Notes |
| :--- | :---: | :--- |
| **Direct Arrays (`T[]`)** | Supported | Implements `ICollectionElementAttribute`; cascades prefab status checks to every slot in GameObject or Component arrays. |
| **Generic Lists (`List<T>`)** | Supported | Validates dynamic list entries individually; displays error banners if a temporary scene instance is added. |
| **Custom `[Serializable]` Classes** | Supported | Operates seamlessly on nested class fields when rendered inline or within collections. |
| **Validation Engine Iteration** | Supported | `ValidateIsPrefabRule` iterates `IEnumerable` collections during static project validation audits. |
