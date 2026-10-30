# [AnimatorParam]

> Renders a string or integer hash property as a smart dropdown populated with parameter names from an attached or referenced Animator.

---

## 1. Overview & Value Proposition

**What it does:**
Populates a string or integer field with a live dropdown list of animation parameters from your Animator Controller, preventing typos.

**The Problem:**
Triggering animations via `animator.SetTrigger("Attack")` or `animator.SetFloat("Speed", 5f)` requires typing magic strings. If an animator renames a parameter in the Animator Controller, the code silently fails with no compile-time error or warning.

**The Solution:**
Add `[AnimatorParam]` to any string or int parameter field:
- **Live Controller Reflection:** Automatically extracts parameters directly from the GameObject's Animator or AnimatorController.
- **Type-Specific Filtering:** Filter dropdowns specifically to `Trigger`, `Float`, `Int`, or `Bool` parameters.
- **Visual Type Badges:** Displays colored tags beside parameter names indicating their exact data types.
- **String or Hash Support:** Works with both parameter name strings and pre-hashed integer IDs (`Animator.StringToHash`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CharacterAnimatorController : MonoBehaviour
{
    [AnimatorParam(AnimatorControllerParameterType.Trigger)]
    public string jumpTriggerName = "Jump";

    [AnimatorParam(AnimatorControllerParameterType.Float)]
    public string movementSpeedParam = "ForwardSpeed";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `string`, `int` (parameter hash) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public AnimatorParamAttribute()
public AnimatorParamAttribute(AnimatorControllerParameterType parameterType)
public AnimatorParamAttribute(string animatorMember)
public AnimatorParamAttribute(string animatorMember, AnimatorControllerParameterType parameterType)
public AnimatorParamAttribute(AnimatorControllerParameterType parameterType, string animatorMember)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `parameterType` | `AnimatorControllerParameterType?` | `null` | Filters parameters to `Trigger`, `Float`, `Int`, or `Bool`. `null` shows all. |
| `animatorMember` | `string` | `""` | Name of member returning `Animator` or `RuntimeAnimatorController`. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ParameterType` | `AnimatorControllerParameterType?` | `null` | Type filter for parameters. |
| `AnimatorMember` / `AnimatorName` | `string` | `""` | Custom member returning target Animator. |
| `ShowTypeBadge` | `bool` | `true` | Renders colored badge chip indicating parameter type. |
| `ShowLabel` | `bool` | `true` | Draws field label before the dropdown. |
| `CustomLabel` | `string` | `null` | Custom display label override. |
| `TextColor` | `string` | `null` | Hex text color for the dropdown button. |
| `BackgroundColor` | `string` | `null` | Hex background color for the dropdown. |
| `BorderColor` | `string` | `null` | Hex border outline color. |
| `BorderRadius` | `float` | `3f` | Border corner radius in pixels. |
| `Height` | `float` | `22f` | Dropdown button height in pixels. |
| `LabelWidth` | `float` | `0f` | Fixed label width in pixels (0 uses default). |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CombatAnimationBridge : MonoBehaviour
{
    [Header("Animator Binding")]
    public Animator characterAnimator;

    [Header("Animation Triggers")]
    [AnimatorParam(nameof(characterAnimator), AnimatorControllerParameterType.Trigger)]
    public string lightAttackTrigger = "Attack_Light";

    [AnimatorParam(nameof(characterAnimator), AnimatorControllerParameterType.Trigger)]
    public string heavyAttackTrigger = "Attack_Heavy";

    [Header("Continuous Parameters")]
    [AnimatorParam(nameof(characterAnimator), AnimatorControllerParameterType.Float)]
    public string locomotionBlendParam = "MoveSpeed";
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Dropdown renders smoothly inside groups and tabs. |
| `[ShowIf]` | Supported | Dynamically display specific parameter selectors when combat modes are active. |
| `[ReadOnly]` | Supported | Displays chosen parameter without allowing selection changes. |
