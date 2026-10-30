# [ValidateIf]

> Conditionally gates sibling validation attributes on the same field, evaluating them only when a predicate condition is met.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateIf]` serves as a conditional execution gate for sibling validation attributes declared on the same field (such as `[ValidateRange]`, `[ValidateNotNull]`, or `[ValidateComponent]`). It evaluates a condition member (`ConditionMember`: a boolean field, enum value, or property). Only when the condition matches the expected value (`ExpectedValue`, or evaluates to `true` when null) are the other validation attributes on that field executed.

**The Problem:**
Validation rules are rarely universal; they depend on mode selections and configuration flags. For example, a weapon only requires a projectile prefab when `weaponType == WeaponType.Ranged`; a damage radius field only needs validation when `isAreaOfEffect == true`. Without conditional validation gates, developers are forced to weaken validation rules or suffer from false positive error banners on irrelevant fields.

**The Solution:**
Decorating fields with `[ValidateIf]`:
- **Conditional Validation Gate:** Ensures sibling validation rules only run when the condition is active (e.g. `[ValidateIf("hasCustomAudio", true)]`).
- **Support for Enums and Primitives:** Matches boolean flags, integer modes, or enum states (`expectedValue = WeaponType.Ranged`).
- **Eliminates False Positives:** Keeps the Inspector clean from spurious validation errors when optional features are toggled off.
- **Pairs with `[ValidateUnless]`:** Use `[ValidateIf]` for positive matching and `[ValidateUnless]` for inverted negative bypass gates.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class WeaponConfig : MonoBehaviour
{
    public bool isRanged = true;

    [ValidateIf("isRanged", true)]
    [ValidateNotNull("Ranged weapons must have a projectile prefab assigned.")]
    public GameObject projectilePrefab;
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
public ValidateIfAttribute(string conditionMember, object expectedValue = null, string message = null)
```

- **`conditionMember`** (`string`): Name of the sibling field, property, or method returning a condition value.
- **`expectedValue`** (`object`, optional): The expected value that enables validation. If `null`, evaluates boolean truthiness.
- **`message`** (`string`, optional): Optional information or guidance note.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ConditionMember` | `string` | Assigned in constructor | Name of the condition member inspected. |
| `ExpectedValue` | `object` | `null` | Value that activates sibling validation attributes. |
| `Invert` | `bool` | `false` | Whether condition logic is inverted (see `[ValidateUnless]`). |
| `Message` | `string` | `null` | Informational message displayed in the validation banner. |
| `MessageType` | `InspectorMessageType` | `InspectorMessageType.Info` | Visual severity badge (`None`, `Info`, `Warning`, `Error`). |

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.ValidationModule;

namespace ProjectZero.Gameplay
{
    public enum MovementMode { Grounded, Airborne, Swimming }

    public class MovementSettings : MonoBehaviour
    {
        [Header("Locomotion Mode")]
        public MovementMode currentMode = MovementMode.Grounded;
        public bool hasSprintAbility = false;

        [Header("Sprint Multiplier")]
        [ValidateIf("hasSprintAbility", true)]
        [ValidateRange(1.2f, 3.0f, "Sprint speed multiplier must be between 1.2x and 3.0x.")]
        public float sprintSpeedMultiplier = 1.5f;

        [Header("Flight Controls")]
        [ValidateIf("currentMode", MovementMode.Airborne)]
        [ValidateNotNull("Airborne movement requires a FlightPhysicsData configuration asset.")]
        public ScriptableObject flightPhysicsConfig;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateNotNull]` / `[Required]`**| High | Conditionally require asset assignments based on feature flags. |
| **`[ValidateRange]`** | High | Conditionally enforce numeric bounds when active features demand them. |
| **`[ShowIf]`** | High | Pair `[ValidateIf]` (validation gate) with `[ShowIf]` (visual inspector visibility gate). |
| **Validation Engine** | Native | Audited conditionally during project-wide validation scans. |
