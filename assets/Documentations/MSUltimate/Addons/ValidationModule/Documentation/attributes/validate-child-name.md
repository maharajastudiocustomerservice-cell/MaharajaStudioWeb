# [ValidateChildName]

> Validates that child names of a referenced GameObject conform to a string pattern matching condition (contains, exact, prefix, suffix, regex).

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateChildName]` inspects the names of child GameObjects belonging to an assigned `GameObject` or `Component` reference. It evaluates whether child names satisfy a string pattern condition (`Pattern`) according to a designated `MatchMode` (`Contains`, `Exact`, `StartsWith`, `EndsWith`, or `Regex`) across a specified `Scope` (`Any`, `All`, or `None`).

**The Problem:**
In procedural rigging, skeletal animation rigs, UI menu hierarchies, and socket systems, child objects must follow precise naming conventions (e.g. `Socket_Weapon`, `Bone_Root`, `Slot_01`). Misnamed children break path lookups like `transform.Find("Socket_Weapon")`, resulting in missing equip items, broken IK rigs, or failed script lookups at runtime.

**The Solution:**
Decorating reference fields with `[ValidateChildName]`:
- **Versatile Matching Modes:** Supports substring searches (`Contains`), exact comparisons (`Exact`), affixes (`StartsWith`, `EndsWith`), and full regular expressions (`Regex`).
- **Flexible Scope Rules:** Enforce that `Any`, `All`, or `None` of the children conform to the pattern.
- **Case Sensitivity Controls:** Toggle `IgnoreCase = true` for forgiving case-insensitive matching.
- **Multiple Rules Supported:** Stack multiple attributes (`AllowMultiple = true`) to enforce complex composite naming rules on children.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class CharacterRig : MonoBehaviour
{
    [ValidateChildName("Socket_", 
        MatchMode = NameMatchMode.StartsWith, 
        Scope = ChildNameMatchScope.Any,
        message: "Rig root must contain at least one child socket starting with 'Socket_'.")]
    public GameObject rigRoot;
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
public ValidateChildNameAttribute(string pattern, string message = null)
```

- **`pattern`** (`string`): The search string, substring, affix, or regex pattern to evaluate against child names.
- **`message`** (`string`, optional): Custom error message to display upon validation failure.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Pattern` | `string` | Assigned in constructor | Pattern string or regular expression evaluated against child names. |
| `MatchMode` | `NameMatchMode` | `NameMatchMode.Contains` | Pattern matching strategy: `Contains`, `Exact`, `StartsWith`, `EndsWith`, `Regex`. |
| `Scope` | `ChildNameMatchScope` | `ChildNameMatchScope.Any` | Match requirement scope: `Any`, `All`, or `None`. |
| `IgnoreCase` | `bool` | `false` | When true, string comparisons ignore character casing. |
| `IncludeInactive` | `bool` | `true` | When true, includes inactive child GameObjects in the pattern audit. |
| `Message` | `string` | Auto-generated | Failure explanation displayed in the validation message box. |
| `MessageType` | `InspectorMessageType` | `InspectorMessageType.Error` | Visual severity badge (`None`, `Info`, `Warning`, `Error`). |
| `ErrorColor` | `string` | `null` | Hex text color override for the validation error message. |
| `ErrorBackgroundColor` | `string` | `null` | Hex background banner color override for the alert box. |
| `FontSize` | `int` | `0` | Font size override in pixels (0 uses default inspector font size). |
| `Padding` | `float` | `0f` | Internal padding around the validation banner. |
| `Margin` | `float` | `5f` | Outer margin spacing separating the banner from neighboring controls. |

### Enums
- **`NameMatchMode`**:
  - `Contains`: Substring search within child names.
  - `Exact`: Child name must match pattern identically.
  - `StartsWith`: Child name must begin with prefix pattern.
  - `EndsWith`: Child name must conclude with suffix pattern.
  - `Regex`: Child name must match regular expression pattern.
- **`ChildNameMatchScope`**:
  - `Any`: At least one child must match the pattern.
  - `All`: Every child must match the pattern.
  - `None`: No child may match the pattern (disallow pattern).

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.ValidationModule;

namespace ProjectZero.Inventory
{
    public class UIInventoryGrid : MonoBehaviour
    {
        [Header("Slot Container")]
        [ValidateChildName(@"^Slot_\d{2}$", 
            MatchMode = NameMatchMode.Regex, 
            Scope = ChildNameMatchScope.All,
            Message = "All child slots must follow the regex format 'Slot_00', 'Slot_01', etc.",
            MessageType = InspectorMessageType.Error)]
        public GameObject slotContainer;

        [Header("Weapon Sockets")]
        [ValidateChildName("WeaponMount", 
            MatchMode = NameMatchMode.Contains, 
            Scope = ChildNameMatchScope.Any,
            IgnoreCase = true)]
        public Transform mountRoot;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateChildCount]`** | High | Combine child naming constraints with child count limits. |
| **`[ValidateChildHasComponent]`** | High | Ensure children follow naming patterns and possess required components. |
| **`[ValidateChildTag]`** | High | Enforce naming conventions alongside required child tags. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans. |
