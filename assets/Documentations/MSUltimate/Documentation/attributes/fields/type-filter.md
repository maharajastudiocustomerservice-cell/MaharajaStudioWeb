# [TypeFilter]

> Restricts object reference fields to GameObjects or Components that implement a specific interface or inherit from an abstract base class.

---

## 1. Overview & Value Proposition

**What it does:**
Enforces type constraints on serialized object fields (such as `MonoBehaviour`, `Component`, or `UnityEngine.Object`), restricting drag-and-drop assignment strictly to assets or components that implement a specified C# interface or inherit from a specific abstract class.

**The Problem:**
Unity cannot serialize interface types directly (e.g. `public IDamageable target;` does not appear in the Inspector). To work around this, developers serialize `MonoBehaviour` or `GameObject` references and cast them in `Awake()`. However, designers can accidentally drag any unrelated component into the field, causing `NullReferenceException` or `InvalidCastException` crashes when playing.

**The Solution:**
Add `[TypeFilter(typeof(IInterface))]` to your serialized field:
- **Interface Drag Validation:** Object picker popup and drag-and-drop operations only accept components implementing the target interface.
- **Visual Feedback:** Objects lacking the expected interface or base type are immediately rejected or highlighted with an error banner.
- **Abstract Base Class Filtering:** Restrict assignments to specific subclass branches.
- **Collection Support:** Full support for `List<MonoBehaviour>` or interface collections via `ICollectionElementAttribute`.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public interface IDamageable
{
    void TakeDamage(float amount);
}

public class AttackTrigger : MonoBehaviour
{
    [TypeFilter(typeof(IDamageable))]
    public MonoBehaviour damageTarget;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `UnityEngine.Object`, `MonoBehaviour`, `Component`, `GameObject` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public TypeFilterAttribute(Type expectedType)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `expectedType` | `Type` | *(Required)* | The expected interface or base class type required for assignment. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ExpectedType` | `Type` | *(Set in constructor)* | The required interface or base class contract. |
| `Order` | `int` | `1` | Drawer execution priority (evaluated early in the modification stack). |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public interface IInteractable
{
    void Interact(GameObject instigator);
    string GetInteractionPrompt();
}

public interface IInventoryItem
{
    string ItemId { get; }
    int MaxStack { get; }
}

public class PlayerInteractionRaycast : MonoBehaviour
{
    [Header("Current Targeted Object (Must Implement IInteractable)")]
    [TypeFilter(typeof(IInteractable))]
    public MonoBehaviour currentInteractableTarget;

    [Header("Nearby Usable Objects (List Filtered by Interface)")]
    [TypeFilter(typeof(IInteractable))]
    public List<MonoBehaviour> nearbyInteractables = new List<MonoBehaviour>();

    public void TriggerInteraction()
    {
        if (currentInteractableTarget is IInteractable interactable)
        {
            interactable.Interact(gameObject);
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Required]` | Recommended | Pairs together to ensure the field is both assigned and conforms to the interface. |
| `[BoxGroup]` | Supported | Object picker container renders compactly inside card layouts. |
| `[ShowIf]` | Supported | Dynamically toggles interface references based on component mode. |
| `ICollectionElement` | Supported | Restricts items added to `List<MonoBehaviour>` or `Component[]`. |
