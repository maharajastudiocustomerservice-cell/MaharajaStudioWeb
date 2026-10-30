# [ValidateAnimatorParameter]

> Validates that an assigned Animator contains a specific parameter name and matching parameter type.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateAnimatorParameter]` inspects an assigned `Animator` or `RuntimeAnimatorController` field. It interrogates the controller's parameter definitions to verify that a required parameter exists (`ParameterName`) and matches the expected type (`AnimatorControllerParameterType`: `Float`, `Int`, `Bool`, or `Trigger`). If the parameter is missing or has an incompatible type, a high-visibility error banner is displayed.

**The Problem:**
In Unity gameplay scripting, animators are controlled using string-based or hash-based API calls (`animator.SetFloat("Speed", 5f)`, `animator.SetTrigger("Jump")`). If an animator designer renames `"Speed"` to `"MoveSpeed"`, or changes a parameter from `Float` to `Bool`, Unity provides zero compile-time or inspector warnings. The script continues running silently without driving animations, leaving programmers to debug animator state machines by hand.

**The Solution:**
Decorating fields with `[ValidateAnimatorParameter]`:
- **Instant Parameter Verification:** Verifies parameter presence immediately in the Inspector upon assigning an Animator or Controller.
- **Type Safety Enforcement:** Guarantees that the expected parameter type (`Float`, `Int`, `Bool`, `Trigger`) matches script expectations.
- **Clear Diagnostic Messages:** Displays clear error banners indicating the exact missing parameter and expected data type.
- **Descriptive Studio Feedback:** Prevents broken character rigs from reaching QA or production builds.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class CharacterMover : MonoBehaviour
{
    [ValidateAnimatorParameter("Speed", AnimatorControllerParameterType.Float)]
    public Animator characterAnimator;
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
public ValidateAnimatorParameterAttribute(
    string parameterName, 
    AnimatorControllerParameterType expectedType, 
    string message = null)
```

- **`parameterName`** (`string`): The required parameter identifier expected in the Animator Controller.
- **`expectedType`** (`AnimatorControllerParameterType`): The expected data type (`Float`, `Int`, `Bool`, or `Trigger`).
- **`message`** (`string`, optional): Custom error message to display upon validation failure.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ParameterName` | `string` | Assigned in constructor | Required animator parameter name. |
| `ExpectedType` | `AnimatorControllerParameterType` | Assigned in constructor | Expected type enum: `Float`, `Int`, `Bool`, or `Trigger`. |
| `Message` | `string` | Auto-generated | Failure explanation displayed in the validation message box. |
| `MessageType` | `InspectorMessageType` | `InspectorMessageType.Error` | Visual severity badge (`None`, `Info`, `Warning`, `Error`). |
| `ErrorColor` | `string` | `null` | Hex text color override for the validation error message. |
| `ErrorBackgroundColor` | `string` | `null` | Hex background banner color override for the alert box. |
| `FontSize` | `int` | `0` | Font size override in pixels (0 uses default inspector font size). |
| `Padding` | `float` | `0f` | Internal padding around the validation banner. |
| `Margin` | `float` | `5f` | Outer margin spacing separating the banner from neighboring controls. |

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.ValidationModule;

namespace ProjectZero.Animation
{
    public class CombatAnimationBridge : MonoBehaviour
    {
        [Header("Animator Binding")]
        [ValidateAnimatorParameter("IsAttacking", AnimatorControllerParameterType.Bool,
            "Animator is missing 'IsAttacking' boolean parameter.")]
        public Animator weaponAnimator;

        [ValidateAnimatorParameter("AttackSpeedMultiplier", AnimatorControllerParameterType.Float)]
        public Animator attackSpeedAnimator;

        [ValidateAnimatorParameter("TriggerImpact", AnimatorControllerParameterType.Trigger)]
        public Animator impactFxAnimator;

        public void ExecuteAttack()
        {
            if (weaponAnimator != null)
                weaponAnimator.SetBool("IsAttacking", true);
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[Required]` / `[NotNull]`** | High | Guarantee the Animator reference itself is assigned before verifying controller parameters. |
| **`[ValidateIf]`** | High | Conditionally validate animator parameters only when an animation system is active. |
| **`[BoxGroup]`** | High | Embeds cleanly into animation inspector layout cards. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans. |
