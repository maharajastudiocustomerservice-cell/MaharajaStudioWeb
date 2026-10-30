# [ValidateHierarchyDepth]

> Validates that the hierarchy nesting depth of a referenced GameObject falls within specified minimum and maximum bounds.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateHierarchyDepth]` calculates the nesting depth of a referenced `GameObject` or `Component` in the scene hierarchy (where a root-level GameObject has depth 0, direct child has depth 1, grandchild has depth 2, etc.). It asserts that the object's depth falls strictly within allowed `MinDepth` and `MaxDepth` bounds, displaying an error banner if the object is nested too deeply or placed too close to the scene root.

**The Problem:**
In large-scale production architectures, deeply nested transform hierarchies cause CPU transform-change propagation overhead, matrix calculation penalties, and messy level organization. Conversely, some systems strictly require objects to be parented under specific containers (depth >= 1) rather than floating at scene root (depth 0), or require objects to remain root-level managers (depth 0).

**The Solution:**
Decorating reference fields with `[ValidateHierarchyDepth]`:
- **Nesting Sanity Constraints:** Restricts hierarchy depth (e.g. `minDepth: 1, maxDepth: 4`) to prevent excessive tree nesting.
- **Root Enforcement:** Require root managers to remain unparented by setting `minDepth: 0, maxDepth: 0`.
- **Performance Optimization:** Prevents deep transform hierarchy chains that severely degrade performance during bulk moving or physics updates.
- **Clear Error Reporting:** Displays the current depth vs. acceptable bounds directly in the Inspector.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class LevelAnchor : MonoBehaviour
{
    [ValidateHierarchyDepth(1, 3, "Anchor must be a child within 1 to 3 levels of nesting.")]
    public GameObject subAnchorObject;
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
public ValidateHierarchyDepthAttribute(int minDepth, int maxDepth, string message = null)
```

- **`minDepth`** (`int`): Minimum acceptable nesting depth (0 = root level).
- **`maxDepth`** (`int`): Maximum acceptable nesting depth.
- **`message`** (`string`, optional): Custom error message to display upon validation failure.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MinDepth` | `int` | `0` | Minimum allowed nesting depth in the scene hierarchy. |
| `MaxDepth` | `int` | `int.MaxValue` | Maximum allowed nesting depth in the scene hierarchy. |
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

namespace ProjectZero.World
{
    public class SectorPartitionController : MonoBehaviour
    {
        [Header("Root Subsystem Managers")]
        [ValidateHierarchyDepth(0, 0, 
            message: "Master partition coordinator must remain a root-level GameObject (depth 0).",
            MessageType = InspectorMessageType.Error)]
        public GameObject rootPartitionManager;

        [Header("Zone Entities")]
        [ValidateHierarchyDepth(2, 5, 
            message: "Zone prop must be parented within a Sector container (depth 2 to 5).")]
        public GameObject sectorDecorProp;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateNoParent]`** | High | Specialized companion attribute for enforcing `depth == 0` root objects. |
| **`[ValidateRequiresParent]`** | High | Combine hierarchy depth bounds with required parent tag or name criteria. |
| **`[ValidateChildCount]`** | High | Validate vertical depth alongside horizontal child sibling counts. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans. |
