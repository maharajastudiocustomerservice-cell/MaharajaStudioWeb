# [ValidateComponent]

> Validates that a referenced GameObject contains an attached component of a specific type (e.g. Rigidbody, Camera, Collider).

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateComponent]` inspects assigned `GameObject` reference fields. It asserts that the referenced GameObject has an attached component of the specified `System.Type` (`RequiredComponentType`). If the assigned GameObject lacks the required component, an informative error banner is displayed immediately in the Inspector.

**The Problem:**
Developers frequently assign generic `GameObject` references in inspector slots rather than strongly typed component references (such as when referencing prefabs, target dummies, or scene anchors). If the assigned GameObject does not have the expected component attached, runtime scripts calling `targetObject.GetComponent<T>()` fail, causing silent bugs or `NullReferenceExceptions` in the middle of gameplay.

**The Solution:**
Decorating `GameObject` fields with `[ValidateComponent]`:
- **Component Presence Verification:** Guarantees that any assigned GameObject owns the required component (e.g. `typeof(AudioSource)`, `typeof(Rigidbody)`).
- **Early Assignment Feedback:** Flags missing components immediately when the object is dragged into the inspector slot, rather than crashing at runtime.
- **Support for Inheritance & Interfaces:** Works with derived component types and abstract base classes.
- **Customizable Error Reporting:** Clear, friendly studio messages guiding designers on what component needs to be added to the referenced prefab or object.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class TargetTracker : MonoBehaviour
{
    [ValidateComponent(typeof(Collider), "Target object must have a Collider component.")]
    public GameObject targetObject;
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
public ValidateComponentAttribute(Type requiredComponentType, string message = null)
```

- **`requiredComponentType`** (`Type`): The component type that must exist on the referenced GameObject.
- **`message`** (`string`, optional): Custom error message displayed upon validation failure.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `RequiredComponentType` | `Type` | Assigned in constructor | The component type required to be present on the referenced GameObject. |
| `Message` | `string` | Auto-generated | Failure explanation displayed in the validation message banner. |
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

namespace ProjectZero.Interaction
{
    public class DoorHingeMechanism : MonoBehaviour
    {
        [Header("Physical Door Panel")]
        [ValidateComponent(typeof(Rigidbody), 
            message: "Assigned door panel must have a Rigidbody component for physics simulation.",
            MessageType = InspectorMessageType.Error)]
        public GameObject doorPanelObject;

        [Header("Audio Feedback")]
        [ValidateComponent(typeof(AudioSource), 
            message: "Hinge audio anchor must contain an AudioSource component.")]
        public GameObject audioAnchorObject;

        public void SwingOpen()
        {
            if (doorPanelObject != null && doorPanelObject.TryGetComponent<Rigidbody>(out var rb))
            {
                rb.AddTorque(Vector3.up * 50f, ForceMode.Impulse);
            }
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[Required]` / `[NotNull]`** | High | Guarantee the GameObject reference is assigned before validating attached components. |
| **`[ValidateActiveState]`** | High | Combine component existence checks with active scene state validation. |
| **`[ValidateIsPrefab]`** | High | Verify prefab status while asserting required components on the prefab root. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans. |

### Collection Cascading & Serializer Matrix

| Collection / Container Type | Supported | Behavior |
| :--- | :---: | :--- |
| **`List<GameObject>`** | Yes | Cascades to validate every GameObject element has the required component. |
| **`GameObject[]`** | Yes | Cascades to validate each array item contains the target component. |
| **`AdvancedList<GameObject>`** | Yes | Full element-level validation support with dynamic item reordering. |
| **`SerializableDictionary<K, GameObject>`** | Yes | Validates component presence when GameObject is value type. |
| **`SerializableNullable<GameObject>`** | Yes | Validates wrapped GameObject reference when populated. |
| **`SerializableTuple<...>`** | Yes | Validates GameObject fields within tuple members. |
