# [PropertyOrder]

> Explicitly sets the display order of a field, property, or method in the Inspector. Lower values appear first.

---

## 1. Overview & Value Proposition

**What it does:**
Controls the vertical sequence of fields in the Inspector using integer order values, regardless of their declaration order in C# script files.

**The Problem:**
In standard Unity, the Inspector strictly follows the top-to-bottom variable declaration order in code. When deriving from base classes or organizing code logically for architecture, base class fields or helper variables end up awkwardly scattered across the Inspector.

**The Solution:**
Add `[PropertyOrder]` to any field, property, or method:
- **Precise Vertical Ordering:** Sort elements by integer rank (e.g. `-10` draws at the top, `100` draws at the bottom).
- **Cross-Hierarchy Organization:** Interleave derived class properties cleanly among base class properties.
- **Button & Method Placement:** Position action buttons directly next to the fields they manipulate.
- **Clean Default Handling:** Unordered properties maintain default order `0`.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class OrderedEntity : MonoBehaviour
{
    [PropertyOrder(10)]
    public string entityName = "Goblin";

    [PropertyOrder(-5)]
    [Title("Primary Entity Header")]
    public int entityId = 101;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public PropertyOrderAttribute(int order)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `order` | `int` | *(Required)* | Sorting priority index. Lower values render earlier. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Order` | `int` | *(Required)* | Display priority rank integer. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CharacterSheetBase : MonoBehaviour
{
    [PropertyOrder(0)]
    [Header("Core Identity")]
    public string characterName;

    [PropertyOrder(50)]
    [Header("Save & Serialization")]
    public string uniqueSaveGuid;
}

public class WarriorPlayer : CharacterSheetBase
{
    // Renders above base class Save GUID but below Identity!
    [PropertyOrder(20)]
    [Header("Combat Stats")]
    public float stamina = 100f;
    public float rage = 0f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Orders elements relative to other elements within the same group container. |
| `[Button]` | Supported | Positions action buttons exactly where desired in the property flow. |
| `[Title]` / `[Header]` | Supported | Decorators move along with the ordered property. |
