# [ValidateRequiresParent]

> Validates that a referenced GameObject has a parent (or ancestor) meeting specific tag, name, or component type criteria.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateRequiresParent]` inspects assigned `GameObject` or `Component` reference fields. It asserts that the referenced GameObject has a parent transform in the scene hierarchy that satisfies designated criteria: matching a required tag (`RequiredParentTag`), containing a name substring (`RequiredParentNameContains`), or owning a specific component type (`RequiredParentComponentType`). When `SearchAncestors = true`, it traverses the full ancestor hierarchy upward from the object.

**The Problem:**
In nested gameplay setups (such as UI list items, weapon socket attachments, wheel colliders on vehicles, or hitboxes), entities require a qualifying parent container to operate correctly. For example, a `WheelCollider` must be parented under a GameObject with a `Rigidbody`, and a `DialogueChoiceUI` button must be parented under a `DialogueWindow` container. If an artist creates or moves an instance without proper parenting, runtime parent searches fail or physics simulations crash.

**The Solution:**
Decorating reference fields with `[ValidateRequiresParent]`:
- **Parent Sanity Guarantees:** Ensures referenced objects are properly nested under qualifying containers.
- **Multi-Criteria Matching:** Match parents via Unity Tags, name substrings, or required component types.
- **Deep Ancestor Search:** Set `SearchAncestors = true` to verify that an ancestor anywhere up the hierarchy tree qualifies.
- **Stacks with Multiple Rules:** Support multiple stacked attributes (`AllowMultiple = true`) to enforce complex compound parenting conditions.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class TurretBarrel : MonoBehaviour
{
    [ValidateRequiresParent(RequiredParentComponentType = typeof(Rigidbody), 
        message: "Barrel must be parented under an object with a Rigidbody.")]
    public GameObject barrelModel;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ValidationModule Addon |
| **Attribute Target** | `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Window Surface** | Unity Inspector & Validation Engine Window |
| **Validation Interface** | `IValidationAttribute` |

---

## 4. Constructors & Parameters

```csharp
public ValidateRequiresParentAttribute(
    string message = "GameObject must have a qualifying parent in the hierarchy.")
```

- **`message`** (`string`, optional): Custom error message to display upon validation failure.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `RequiredParentTag` | `string` | `""` | Tag that the parent must have (empty skips tag check). |
| `RequiredParentNameContains` | `string` | `""` | Substring that the parent name must contain (empty skips check). |
| `RequiredParentComponentType` | `Type` | `null` | Component type that the parent must own (null skips check). |
| `SearchAncestors` | `bool` | `false` | When true, searches the full ancestor chain instead of only the direct parent. |
| `Message` | `string` | `"GameObject must have a qualifying parent..."` | Failure explanation displayed in the validation banner. |
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

namespace ProjectZero.Vehicles
{
    public class VehicleWheelSuspension : MonoBehaviour
    {
        [Header("Wheel Mount")]
        [ValidateRequiresParent(
            RequiredParentComponentType = typeof(Rigidbody),
            SearchAncestors = true,
            Message = "Suspension assembly must reside under an ancestor Rigidbody chassis.",
            MessageType = InspectorMessageType.Error)]
        public GameObject wheelAssembly;

        [Header("Brake Disc Mount")]
        [ValidateRequiresParent(
            RequiredParentNameContains = "WheelHub",
            Message = "Brake caliper must be parented under a 'WheelHub' container.")]
        public Transform brakeCaliperTransform;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateNoParent]`** | Inverse | Exact complement: use `[ValidateNoParent]` for root-level objects. |
| **`[ValidateParentName]`** | High | Sibling attribute focusing specifically on pattern matching parent names. |
| **`[ValidateHierarchyDepth]`** | High | Combine parent criteria checks with overall hierarchy tree depth bounds. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans. |
