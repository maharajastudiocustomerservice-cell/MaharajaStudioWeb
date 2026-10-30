# [RequireInterface]

> Restricts an Object field to only accept components or assets that implement a specified C# interface type, rejecting non-conforming objects.

---

## 1. Overview & Value Proposition

**What it does:**
Enforces interface type contracts on Unity `Object` fields (GameObjects, MonoBehaviours, ScriptableObjects). When an assigned object does not implement `InterfaceType`, it rejects the assignment or renders an explicit error callout.

**The Problem:**
Unity's serializer cannot natively serialize interfaces (`public IDamageable target;` does not appear in the Inspector). Developers often compromise with generic `UnityEngine.Object` or `GameObject` fields, leaving them open to assigning components that fail to implement the required interface.

**The Solution:**
Add `[RequireInterface(typeof(IMyInterface))]` to any `Object` or `MonoBehaviour` field:
- **Interface Contract Safety:** Enforces interface adherence directly inside the Inspector GUI.
- **Drag-and-Drop Filtering:** Automatically checks dragged objects and extracts the implementing component.
- **Custom Error Callout:** Displays error feedback when invalid objects are assigned.
- **Eliminates Null Casts:** Prevents runtime `GetComponent<IInterface>() == null` bugs.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public interface IDamageable
{
    void TakeDamage(float amount);
}

public class ProjectileImpact : MonoBehaviour
{
    [RequireInterface(typeof(IDamageable))]
    public MonoBehaviour damageTarget;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `UnityEngine.Object`, `MonoBehaviour`, `GameObject`, `ScriptableObject` (including `T[]` and `List<T>`) |
| **Collection Cascading** | Supported (`ICollectionElementAttribute`) |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public RequireInterfaceAttribute(Type interfaceType)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `interfaceType` | `Type` | *(Required)* | Expected C# interface type (e.g. `typeof(IInteractable)`). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `InterfaceType` | `Type` | *(Constructor)* | Required interface contract type. |
| `Message` | `string` | `null` | Custom error message displayed if assigned object lacks the interface. |
| `ErrorColor` | `string` | `null` | Hex color code for error text. |
| `ErrorBackgroundColor` | `string` | `null` | Hex color code for error box background plate. |
| `FontSize` | `int` | `0` | Font size for error message (`0` = default). |
| `Padding` | `float` | `0f` | Internal padding inside error box. |
| `Margin` | `float` | `5f` | Margin spacing around error box. |
| `Order` | `int` | `0` | Execution priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public interface IInteractable
{
    void Interact(GameObject user);
}

public class PlayerInteractionRaycast : MonoBehaviour
{
    [Header("Current Target (Must Implement IInteractable)")]
    [RequireInterface(typeof(IInteractable), 
        Message = "Assigned object does not implement IInteractable interface!", 
        ErrorColor = "#FFFFFF", 
        ErrorBackgroundColor = "#c0392b"
    )]
    public MonoBehaviour currentInteractableTarget;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `Collections (T[], List<T>)` | Supported | Automatically cascades interface validation to every slot in arrays and lists (`ICollectionElementAttribute`). |
| `[Required]` | Supported | Pair with `[Required]` to demand that the interface field is both non-null and implements the type. |
| `[BoxGroup]` | Supported | Integrates cleanly into structured inspector cards. |
| Multiple Allowed | Supported | Specify multiple interface requirements on a single reference. |
