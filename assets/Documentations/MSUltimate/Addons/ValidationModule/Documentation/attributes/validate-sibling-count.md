# [ValidateSiblingCount]

> Validates that the number of siblings sharing the same parent falls within specified minimum and maximum bounds.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateSiblingCount]` inspects assigned `GameObject` or `Component` reference fields. It evaluates the target object's parent container and counts its sibling GameObjects (other children belonging to the same parent transform). It asserts that the sibling tally falls within specified `Min` and `Max` limits. By default, it excludes the object itself (`IncludeSelf = false`), but setting `IncludeSelf = true` counts all children of the parent.

**The Problem:**
In modular UI rows, equipment slot groups, or multiplayer team containers, containers must enforce a specific capacity of entries (e.g. an inventory row must have between 1 and 6 buttons; a 3-lane mob spawner must have exactly 2 sibling lane nodes). When designers inadvertently duplicate or delete sibling items, grid layout calculations distort, UI pagination breaks, or array index bounds fail at runtime.

**The Solution:**
Decorating reference fields with `[ValidateSiblingCount]`:
- **Sibling Population Constraints:** Enforces minimum and maximum limits on sibling GameObjects.
- **Self-Inclusion Toggle:** Toggle `IncludeSelf = true` to evaluate the total parent child count including the target object.
- **Inactive Sibling Support:** Toggle `IncludeInactive` to include or exclude disabled sibling transforms.
- **Immediate Structural Alerts:** Warns developers when a container is overpopulated or missing required entries.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class InventoryRow : MonoBehaviour
{
    [ValidateSiblingCount(min: 3, max: 5, message: "Inventory slot must have between 3 and 5 siblings in this row.")]
    public GameObject slotButton;
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
public ValidateSiblingCountAttribute(int min, int max, string message = null)
```

- **`min`** (`int`): Minimum acceptable sibling count.
- **`max`** (`int`): Maximum acceptable sibling count.
- **`message`** (`string`, optional): Custom error message displayed upon validation failure.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Min` | `int` | Assigned in constructor | Minimum acceptable sibling count. |
| `Max` | `int` | Assigned in constructor | Maximum acceptable sibling count. |
| `IncludeSelf` | `bool` | `false` | When true, includes the object itself in the count (total children of parent). |
| `IncludeInactive` | `bool` | `true` | When true, inactive sibling GameObjects are counted. |
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

namespace ProjectZero.UI
{
    public class ActionButtonBar : MonoBehaviour
    {
        [Header("Button Container Member")]
        [ValidateSiblingCount(min: 2, max: 6, 
            IncludeSelf = true, 
            IncludeInactive = false,
            message: "Action button bar must contain between 2 and 6 active buttons.",
            MessageType = InspectorMessageType.Error)]
        public GameObject primaryActionButton;

        [Header("Secondary Slot")]
        [ValidateSiblingCount(min: 0, max: 2, message: "Shortcut slot allows at most 2 sibling shortcuts.")]
        public GameObject secondaryShortcutSlot;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateSiblingIndex]`** | High | Sibling companion attribute for enforcing specific order index within the siblings. |
| **`[ValidateUniqueInHierarchy]`** | High | Ensure siblings maintain unique names while staying within count bounds. |
| **`[ValidateChildCount]`** | High | Use `[ValidateChildCount]` for counting downwards; use `[ValidateSiblingCount]` horizontally. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans. |
