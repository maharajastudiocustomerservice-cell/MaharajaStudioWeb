# [ValidateParentName]

> Validates that the direct parent (or ancestor) of a referenced GameObject matches a specified name pattern.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateParentName]` inspects assigned `GameObject` or `Component` reference fields. It evaluates the name of the object's direct parent transform (`transform.parent.name`), asserting that it satisfies a string pattern condition (`Pattern`). Supported matching modes include `Contains`, `Exact`, `StartsWith`, `EndsWith`, and `Regex`. When `SearchAncestors = true`, it searches up the entire transform ancestor hierarchy.

**The Problem:**
In modular environment kits, procedural dungeon rooms, or character equipment rigs, GameObjects are intended to be parented under specific parent containers (e.g. `transform.parent.name == "Socket_RightHand"` or `transform.parent.name.StartsWith("Room_")`). If an artist inadvertently parents a weapon under `"Root"` or `"Spine"` instead of `"Socket_RightHand"`, animations or attachment scripts fail to locate the expected container or position items at improper coordinate origins.

**The Solution:**
Decorating reference fields with `[ValidateParentName]`:
- **Parent Container Verification:** Ensures referenced entities are parented under properly designated containers.
- **Multiple Match Modes:** Substring matching (`Contains`), exact comparisons (`Exact`), affixes (`StartsWith`, `EndsWith`), or regular expressions (`Regex`).
- **Ancestor Traversal:** Toggle `SearchAncestors = true` to verify that an ancestor anywhere up the transform hierarchy matches the pattern.
- **Case Sensitivity Control:** Toggle `IgnoreCase = true` for case-insensitive matching.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class HandheldWeapon : MonoBehaviour
{
    [ValidateParentName("Socket_Hand", 
        MatchMode = NameMatchMode.Contains, 
        message: "Weapon must be parented under a Hand socket transform.")]
    public GameObject weaponModel;
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
public ValidateParentNameAttribute(string pattern, string message = null)
```

- **`pattern`** (`string`): The search string, substring, affix, or regex pattern to evaluate against parent names.
- **`message`** (`string`, optional): Custom error message to display upon validation failure.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Pattern` | `string` | Assigned in constructor | Pattern string or regular expression evaluated against parent names. |
| `MatchMode` | `NameMatchMode` | `NameMatchMode.Contains` | Pattern matching mode: `Contains`, `Exact`, `StartsWith`, `EndsWith`, `Regex`. |
| `IgnoreCase` | `bool` | `false` | When true, string comparisons ignore character casing. |
| `SearchAncestors` | `bool` | `false` | When true, walks the full ancestor chain until a matching parent is found. |
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

namespace ProjectZero.Environment
{
    public class InteractiveLightFixture : MonoBehaviour
    {
        [Header("Hierarchy Structure")]
        [ValidateParentName("LightGrid_", 
            MatchMode = NameMatchMode.StartsWith, 
            SearchAncestors = true,
            IgnoreCase = true,
            Message = "Light fixture must be placed within an ancestor container starting with 'LightGrid_'.",
            MessageType = InspectorMessageType.Error)]
        public GameObject fixtureRoot;

        [Header("Mount Point")]
        [ValidateParentName("Ceiling_Mount", MatchMode = NameMatchMode.Exact)]
        public Transform mountSocket;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateRequiresParent]`** | High | Combine parent name pattern checks with parent component/tag requirements. |
| **`[ValidateChildName]`** | High | Sibling attribute for validating child transform names below an object. |
| **`[ValidateNoParent]`** | Inverse | Exact complement: use `[ValidateNoParent]` when an object must have no parent. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans. |
