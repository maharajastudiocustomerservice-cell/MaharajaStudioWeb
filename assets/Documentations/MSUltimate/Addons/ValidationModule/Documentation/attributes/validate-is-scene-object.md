# [ValidateIsSceneObject]

> Validates that an assigned object reference is an active instance in the scene hierarchy, completely rejecting project Prefab assets.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateIsSceneObject]` inspects assigned `GameObject` or `Component` fields that are designed to reference active scene entities (such as camera targets, player transforms, waypoint anchors, or scene lighting rigs). It uses `EditorUtility.IsPersistent` to verify that the assigned object is a living instance in an open Scene, completely rejecting persistent Project Prefab assets.

**The Problem:**
Certain gameplay mechanics require interacting with a live scene instance (e.g. `cinematicCamera.LookAt = targetPlayer`). If a developer accidentally drags the `PlayerPrefab` asset from the Project window instead of the `Player` GameObject in the active Hierarchy, the script references an un-instantiated disk asset. At runtime, the script attempts to read the position or invoke methods on an inert prefab, producing zero movement or failing with bizarre transform errors.

**The Solution:**
Decorating scene reference fields with `[ValidateIsSceneObject]`:
- **Scene Instance Enforcement:** Guarantees that only live GameObjects currently in an active scene can be assigned.
- **Rejects Disk Prefabs:** Flags an immediate error banner if an un-instantiated Project window prefab is dragged into the slot.
- **Prevents Inert Reference Bugs:** Eliminates elusive bugs where scripts attempt to manipulate transform coordinates on project assets.
- **Clear Studio Diagnostic Feedback:** Informs designers that an active scene instance must be linked.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class CameraFollow : MonoBehaviour
{
    [ValidateIsSceneObject("Follow target must be an active GameObject in the scene.")]
    public Transform followTarget;
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
public ValidateIsSceneObjectAttribute(
    string message = "Reference must be an instance within a Scene, completely rejecting Project Prefab Assets.")
```

- **`message`** (`string`, optional): Custom error message displayed if a Project asset or prefab is assigned.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Message` | `string` | `"Reference must be an instance..."` | Failure explanation displayed in the validation message banner. |
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

namespace ProjectZero.Cameras
{
    public class CinematicTrackingRig : MonoBehaviour
    {
        [Header("Scene Track Targets")]
        [ValidateIsSceneObject("Primary tracking focus must be a live GameObject in the scene.",
            MessageType = InspectorMessageType.Error)]
        public Transform primaryActorTransform;

        [ValidateIsSceneObject("Secondary tracking focus must be a live scene object.")]
        public Transform secondaryActorTransform;

        [Header("Direct Collection Cascading")]
        [ValidateIsSceneObject]
        [Tooltip("Cascades live scene object validation to each waypoint in the array.")]
        public Transform[] patrolWaypoints;

        [ValidateIsSceneObject]
        [Tooltip("Cascades scene instance verification to each dynamic anchor in the list.")]
        public List<GameObject> dynamicSpawnAnchors = new List<GameObject>();

        private void LateUpdate()
        {
            if (primaryActorTransform != null)
            {
                transform.position = primaryActorTransform.position + Vector3.back * 10f;
            }
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

### 7.1 Layout & Conditional Stacking

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateIsPrefab]`** | Inverse | Exact complement: use `[ValidateIsPrefab]` when project assets are required. |
| **`[ValidateActiveState]`** | High | Combine scene object verification with active/inactive state validation. |
| **`[Required]` / `[NotNull]`** | High | Guarantee the reference is assigned before checking its scene status. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans via `ValidateIsSceneObjectRule`. |

### 7.2 Collection Cascading & Serializer Behavior Matrix

| Target Context | Support Status | Architecture Notes |
| :--- | :---: | :--- |
| **Direct Arrays (`T[]`)** | Supported | Implements `ICollectionElementAttribute`; cascades scene instance checks to each Transform or GameObject in the array. |
| **Generic Lists (`List<T>`)** | Supported | Dynamic list support; flags immediate error banners if an un-instantiated prefab is added to the list. |
| **Custom `[Serializable]` Classes** | Supported | Operates seamlessly on nested class fields when rendered inline or within collections. |
| **Validation Engine Iteration** | Supported | `ValidateIsSceneObjectRule` iterates `IEnumerable` collections during static project validation audits. |
