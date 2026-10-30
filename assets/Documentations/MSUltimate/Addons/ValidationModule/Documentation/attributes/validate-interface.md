# [ValidateInterface]

> Validates that an assigned object reference or GameObject implements a specified C# interface type.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateInterface]` inspects assigned object reference fields (`UnityEngine.Object`, `MonoBehaviour`, `ScriptableObject`, or `GameObject`). Because Unity's standard serializer cannot serialize interface types directly (e.g. `public IDamageable target;` does not display in the Inspector), developers must serialize `MonoBehaviour` or `GameObject` fields. `[ValidateInterface]` validates that the assigned object actually implements the specified interface (`RequiredInterfaceType`).

**The Problem:**
To work around Unity's inability to serialize interface types, developers declare fields as `public MonoBehaviour listener;` or `public GameObject interactor;`. At edit time, however, nothing stops someone from assigning any arbitrary component or GameObject that does not implement the interface. The code is forced to rely on runtime casting `(listener as IDamageable)` that fails silently or throws `InvalidCastException` during gameplay.

**The Solution:**
Decorating interface reference fields with `[ValidateInterface]`:
- **Interface Contract Safety:** Guarantees that any assigned object or GameObject implements the specified interface (e.g. `typeof(IDamageable)`).
- **Supports Both Components and GameObjects:** When assigned a `GameObject`, scans all attached components to ensure at least one component implements the interface.
- **Immediate Drag-and-Drop Feedback:** Displays an error banner in the Inspector the moment an incompatible object is assigned.
- **Clean Architecture Integration:** Enables clean SOLID inversion of control architecture within standard Unity inspector workflows.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public interface IDamageable
{
    void TakeDamage(float amount);
}

public class AttackTrigger : MonoBehaviour
{
    [ValidateInterface(typeof(IDamageable), "Assigned target must implement IDamageable.")]
    public MonoBehaviour damageableTarget;
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
public ValidateInterfaceAttribute(Type requiredInterfaceType, string message = null)
```

- **`requiredInterfaceType`** (`Type`): The interface `System.Type` that the assigned object must implement.
- **`message`** (`string`, optional): Custom error message displayed upon validation failure.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `RequiredInterfaceType` | `Type` | Assigned in constructor | Interface type required for the assigned reference. |
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
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.ValidationModule;

namespace ProjectZero.Interaction
{
    public interface IInteractable
    {
        string InteractionPrompt { get; }
        void OnInteract(GameObject instigator);
    }

    public class PlayerInteractionRaycaster : MonoBehaviour
    {
        [Header("Default Interaction Target")]
        [ValidateInterface(typeof(IInteractable), 
            message: "Assigned default interactable must implement the IInteractable interface.",
            MessageType = InspectorMessageType.Error)]
        public GameObject defaultInteractableTarget;

        [Header("Direct Collection Cascading")]
        [ValidateInterface(typeof(IInteractable))]
        [Tooltip("Cascades interface contract checking to each MonoBehaviour in the array.")]
        public MonoBehaviour[] combatTargets;

        [ValidateInterface(typeof(IInteractable))]
        [Tooltip("Cascades interface contract checking to each entry in the dynamic list.")]
        public List<MonoBehaviour> interactableObjects = new List<MonoBehaviour>();

        public void TriggerDefaultInteraction()
        {
            if (defaultInteractableTarget != null && 
                defaultInteractableTarget.TryGetComponent<IInteractable>(out var interactable))
            {
                interactable.OnInteract(gameObject);
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
| **`[Required]` / `[NotNull]`** | High | Guarantee the reference is assigned before validating interface compliance. |
| **`[ValidateComponent]`** | High | Use `[ValidateComponent]` for concrete types; use `[ValidateInterface]` for interface contracts. |
| **`[ValidateIf]`** | High | Conditionally enforce interface requirements based on selected interaction mode. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans via `ValidateInterfaceRule`. |

### 7.2 Collection Cascading & Serializer Behavior Matrix

| Target Context | Support Status | Architecture Notes |
| :--- | :---: | :--- |
| **Direct Arrays (`T[]`)** | Supported | Implements `ICollectionElementAttribute`; cascades interface verification to each element with dedicated error alerts. |
| **Generic Lists (`List<T>`)** | Supported | Validates dynamic list entries individually; supports both direct component references and GameObjects with matching components. |
| **Custom `[Serializable]` Classes** | Supported | Operates seamlessly on nested class fields when rendered inline or within collections. |
| **Validation Engine Iteration** | Supported | `ValidateInterfaceRule` iterates `IEnumerable` collections during static project validation audits. |
