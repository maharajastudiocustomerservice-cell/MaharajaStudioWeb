# [ValidateUniqueInHierarchy]

> Validates that a referenced GameObject or Component possesses a name that is completely unique among its sibling GameObjects or across all descendants of its parent container.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateUniqueInHierarchy]` inspects assigned `GameObject` or `Component` reference fields (such as `Transform` or `RectTransform`). It examines the object's parent and iterates through all other child objects belonging to that parent to verify that no other object shares the same `name`. When `DeepSearch = true`, it extends the uniqueness check across all recursive descendants of the parent tree. It also supports case-insensitive name matching via `IgnoreCase = true`.

**The Problem:**
In many game architectures, subsystems locate child nodes dynamically using name-based path queries (e.g. `transform.Find("Slot_Inventory")`, UI button lookups, or dialogue tree node resolution):
- When level designers duplicate a prefab node or UI button without renaming it, multiple siblings end up sharing the exact same name (e.g., two objects named `"Slot_01"`).
- `transform.Find()` will always bind to the first matching sibling encountered, silently ignoring the second object or causing data to write to the wrong container.
- Such name conflicts cause phantom input bugs, broken event triggers, and data desynchronization that are exceptionally time-consuming to isolate.

**The Solution:**
Decorating reference fields with `[ValidateUniqueInHierarchy]`:
- **Sibling Uniqueness Guard:** Asserts that no two direct sibling GameObjects share the same name.
- **Deep Hierarchy Traversal:** Enable `DeepSearch = true` to guarantee name uniqueness across all nested child generations beneath the parent root.
- **Case Sensitivity Control:** Toggle `IgnoreCase = true` to catch collisions like `"InventorySlot"` vs `"inventoryslot"`.
- **Prevents Ambiguous Lookups:** Guarantees name-based queries (`transform.Find`, animation bindings, UI wiring) resolve deterministically.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class UIWindowManager : MonoBehaviour
{
    [ValidateUniqueInHierarchy("UI panel name must be unique among its sibling views to ensure reliable lookups.")]
    public GameObject panelView;

    [ValidateUniqueInHierarchy("Slot node must be uniquely named across the entire container hierarchy.", DeepSearch = true)]
    public Transform equipmentSlot;
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
| **Validation Interface** | `IValidationAttribute` |

---

## 4. Constructors & Parameters

```csharp
public ValidateUniqueInHierarchyAttribute(string message = "GameObject name must be unique among its siblings.")
```

- **`message`** (`string`, optional): Custom error message displayed upon name collision. Default is `"GameObject name must be unique among its siblings."`.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `IgnoreCase` | `bool` | `false` | When true, performs case-insensitive name comparisons. |
| `DeepSearch` | `bool` | `false` | When true, verifies uniqueness across all recursive descendants of the parent. |
| `Message` | `string` | `"GameObject name must be unique..."` | Failure explanation displayed in the validation message banner. |
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

namespace ProjectZero.UI
{
    public class TabGroupPresenter : ModularMonoBehaviour
    {
        [Header("Tab Header Elements")]
        [ValidateUniqueInHierarchy("Tab button names must be distinct to prevent routing collisions.",
            IgnoreCase = true,
            MessageType = InspectorMessageType.Error)]
        public GameObject tabButtonHeader;

        [Header("Dialogue Tree Root")]
        [ValidateUniqueInHierarchy("Dialogue node name conflicts with another node in this hierarchy.",
            DeepSearch = true,
            MessageType = InspectorMessageType.Warning)]
        public Transform dialogueResponseNode;

        [Header("Container Slot")]
        [ValidateUniqueInHierarchy("Inventory slot must have a unique identifier name within its parent.",
            IgnoreCase = false,
            ErrorColor = "#FF8800")]
        public Transform quickSlot;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateChildName]`** | High | Combine with pattern naming rules (e.g. prefix `Slot_`) while enforcing uniqueness. |
| **`[ValidateSiblingCount]`** | High | Enforce both total sibling count caps and distinct naming across all siblings. |
| **`[ValidateRequiresParent]`** | High | Guarantee the object is nested under a parent container before checking sibling uniqueness. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans. |
