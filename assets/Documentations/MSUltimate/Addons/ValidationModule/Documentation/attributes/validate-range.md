# [ValidateRange]

> Strict numeric range invariant guard with visual warning and error banners when values breach minimum or maximum bounds.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateRange]` enforces strict numerical boundaries (`[Min, Max]`) on floating-point (`float`, `double`) or integer (`int`, `long`) serialized fields. Unlike Unity's native `[Range]` attribute—which replaces the standard numeric input field with a horizontal slider—`[ValidateRange]` preserves the standard numeric input field (allowing free numerical entry and copy-paste) while rendering a prominent, styled error banner if entered values breach allowed boundaries.

**The Problem:**
While Unity's native `[Range(min, max)]` attribute is common, forcing an inspector field into a slider can be cumbersome when tuning high-precision values (e.g. typing `0.0035` on a slider with range `0..100` is nearly impossible). Furthermore, native `[Range]` does not communicate validation errors to automated CI build validators or external project scan tools.

**The Solution:**
Decorating numeric fields with `[ValidateRange]`:
- **Preserves Standard Numeric Field:** Retains standard numeric input boxes, allowing exact decimal typing without slider imprecision.
- **Visual Alert Banners:** Displays high-contrast validation warning or error banners directly beneath invalid values.
- **Automated Pipeline Integration:** Discovered and validated project-wide via the Validation Engine scan window.
- **Customizable Styling Tokens:** Customize banner text color (`ErrorColor`), background banner (`ErrorBackgroundColor`), and font sizes.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class PlayerMovement : MonoBehaviour
{
    [ValidateRange(1f, 30f, "Movement speed must stay between 1 and 30 units/sec.")]
    public float movementSpeed = 6.5f;
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
public ValidateRangeAttribute(float min, float max, string message = null)
```

- **`min`** (`float`): Minimum acceptable numerical boundary.
- **`max`** (`float`): Maximum acceptable numerical boundary.
- **`message`** (`string`, optional): Custom error message displayed upon validation failure.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Min` | `float` | Assigned in constructor | Minimum acceptable numerical limit. |
| `Max` | `float` | Assigned in constructor | Maximum acceptable numerical limit. |
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

namespace ProjectZero.Gameplay
{
    public class GravityController : MonoBehaviour
    {
        [Header("Global Physics Constants")]
        [ValidateRange(-50f, 0f, 
            message: "Downward gravity force must be between -50 and 0 units/sec².",
            MessageType = InspectorMessageType.Error)]
        public float gravityAcceleration = -9.81f;

        [Header("Terminal Velocity")]
        [ValidateRange(5f, 100f, 
            message: "Terminal velocity must be between 5 and 100 units/sec.",
            MessageType = InspectorMessageType.Warning)]
        public float terminalVelocity = 50f;

        [Header("Direct Collection Cascading")]
        [ValidateRange(0f, 1f)]
        [Tooltip("Cascades 0-1 probability range validation to each slot in the array.")]
        public float[] dropWeightings = new float[] { 0.25f, 0.75f, 0.5f };

        [ValidateRange(1, 100)]
        [Tooltip("Cascades 1-100 stat bounds validation to each entry in the progression list.")]
        public List<int> attributeProgression = new List<int> { 10, 25, 50, 100 };
    }
}
```

---

## 7. Stacking & Compatibility Matrix

### 7.1 Layout & Conditional Stacking

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateCompare]`** | High | Combine absolute numeric range limits with relative sibling comparisons. |
| **`[ValidateIf]`** | High | Conditionally apply range validation based on active feature toggles. |
| **`[BoxGroup]`** | High | Embeds cleanly inside grouped inspector cards and layout panels. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans via `RangeValidationRule`. |

### 7.2 Collection Cascading & Serializer Behavior Matrix

| Target Context | Support Status | Architecture Notes |
| :--- | :---: | :--- |
| **Direct Arrays (`T[]`)** | Supported | Implements `ICollectionElementAttribute`; cascades numeric range checking directly to each numeric element in arrays. |
| **Generic Lists (`List<T>`)** | Supported | Supports integer and floating-point lists; renders inline warning/error banners for any elements outside boundaries. |
| **Custom `[Serializable]` Classes** | Supported | Operates seamlessly on nested class fields when rendered inline or within collections. |
| **Validation Engine Iteration** | Supported | `RangeValidationRule` iterates `IEnumerable` numeric collections during static project validation audits. |
