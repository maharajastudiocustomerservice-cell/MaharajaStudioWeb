# [ValidateCompare]

> Validates that a numeric or comparable field satisfies a comparative relation against another serialized field (e.g. currentHealth <= maxHealth).

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateCompare]` validates the value of one serialized field by comparing it against another serialized field on the same object using relational operators (`LessThan`, `LessThanOrEqual`, `Equal`, `NotEqual`, `GreaterThanOrEqual`, `GreaterThan`). If the relational expression evaluates to false, it immediately renders a clear validation error banner in the Inspector.

**The Problem:**
In gameplay balance setups, pairs of dependent values must maintain strict invariants: `minDamage <= maxDamage`, `currentAmmo <= maxAmmo`, `attackSpeed > 0`, or `innerRadius < outerRadius`. Standard Unity allows designers to set `minDamage = 50` and `maxDamage = 20`, causing calculation glitches, negative ranges, or inverted gameplay logic at runtime.

**The Solution:**
Decorating dependent fields with `[ValidateCompare]`:
- **Relational Invariant Safeguards:** Enforces natural mathematical relations directly between serialized fields (e.g. `[ValidateCompare("maxHealth", CompareOp.LessThanOrEqual)]`).
- **Support for Multiple Comparisons:** Stack multiple attributes (`AllowMultiple = true`) to validate against multiple bounds (e.g. `> minRange` and `< maxRange`).
- **Comprehensive Operator Suite:** Full relational operator enum (`CompareOp`): `<`, `<=`, `==`, `!=`, `>=`, `>`.
- **Informative Error Messages:** Displays custom or automatic messages indicating both values and why the comparison failed.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class HealthComponent : MonoBehaviour
{
    public float maxHealth = 100f;

    [ValidateCompare("maxHealth", CompareOp.LessThanOrEqual, 
        message: "Current health cannot exceed max health.")]
    public float currentHealth = 100f;
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
public ValidateCompareAttribute(string otherFieldName, CompareOp op, string message = null)
```

- **`otherFieldName`** (`string`): The name of the sibling serialized field to compare against.
- **`op`** (`CompareOp`): Relational operator enum (`LessThan`, `LessThanOrEqual`, `Equal`, `NotEqual`, `GreaterThanOrEqual`, `GreaterThan`).
- **`message`** (`string`, optional): Custom error message displayed upon validation failure.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `OtherFieldName` | `string` | Assigned in constructor | Name of the sibling field being compared against. |
| `Operator` | `CompareOp` | Assigned in constructor | Comparison operation to evaluate. |
| `Message` | `string` | Auto-generated | Failure explanation displayed in the validation message banner. |
| `MessageType` | `InspectorMessageType` | `InspectorMessageType.Error` | Visual severity badge (`None`, `Info`, `Warning`, `Error`). |
| `ErrorColor` | `string` | `null` | Hex text color override for the validation error banner. |
| `ErrorBackgroundColor` | `string` | `null` | Hex background color override for the alert box. |
| `FontSize` | `int` | `0` | Font size override in pixels (0 uses default inspector font size). |
| `Padding` | `float` | `0f` | Internal padding around the validation banner. |
| `Margin` | `float` | `5f` | Outer margin spacing separating the banner from neighboring controls. |

### `CompareOp` Enum Values
- **`LessThan`**: Current field must be strictly less than (`<`) `OtherFieldName`.
- **`LessThanOrEqual`**: Current field must be less than or equal to (`<=`) `OtherFieldName`.
- **`Equal`**: Current field must equal (`==`) `OtherFieldName`.
- **`NotEqual`**: Current field must not equal (`!=`) `OtherFieldName`.
- **`GreaterThanOrEqual`**: Current field must be greater than or equal to (`>=`) `OtherFieldName`.
- **`GreaterThan`**: Current field must be strictly greater than (`>`) `OtherFieldName`.

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.ValidationModule;

namespace ProjectZero.Combat
{
    public class WeaponDamageProfile : MonoBehaviour
    {
        [Header("Damage Bounds")]
        public float baseDamage = 15f;

        [ValidateCompare("baseDamage", CompareOp.GreaterThanOrEqual, 
            message: "Critical damage must be greater than or equal to base damage.",
            MessageType = InspectorMessageType.Error)]
        public float criticalDamage = 30f;

        [Header("Range Radii")]
        public float innerDangerRadius = 5f;

        [ValidateCompare("innerDangerRadius", CompareOp.GreaterThan,
            message: "Outer boundary must be larger than inner danger radius.")]
        public float outerBoundaryRadius = 15f;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateRange]`** | High | Combine absolute numeric range limits with relative sibling comparisons. |
| **`[BoxGroup]`** | High | Visualizes cleanly within layout cards containing paired numeric fields. |
| **`[ValidateIf]`** | High | Conditionally apply comparison checks when specific combat modes are active. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans. |
