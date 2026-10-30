# [ConditionalField]

> Universal conditional visibility and interactivity attribute supporting compound C#-style inline expressions, multi-condition logic (AND/OR), bitwise flags, parameterized methods, smooth fade transitions, and disable-instead-of-hide modes.

---

## 1. Overview & Value Proposition

**What it does:**
The cornerstone attribute of the conditional suite. Controls whether an Inspector field is visible or interactable based on single conditions, multi-condition arrays, inline C# expressions, comparison values, or bitmask flags.

**The Problem:**
Inspectors quickly become overloaded with dozens of situational properties (e.g. showing "Homing Turn Rate" when trajectory is set to "Linear", or showing "Mana Cost" for pure melee warriors). Building custom editor drawers for every combination requires hundreds of lines of fragile GUI code.

**The Solution:**
Add `[ConditionalField]` above any field, property, or method:
- **Universal Expression Engine:** Write inline compound C# conditions (`$score > 50 && $hasKey`) directly in the attribute.
- **Parameterized Methods:** Pass literal arguments into condition methods (`CheckState(4, true)`).
- **Bitwise Flag Masks (`HasFlag`):** Test `[System.Flags]` enum bitmasks effortlessly with `ConditionOperator.HasFlag`.
- **Multi-Condition Arrays:** Combine multiple flags with `ConditionLogic.And` or `ConditionLogic.Or`.
- **Engine State Macros:** Built-in engine state macros (`@isPlayMode`, `@isEditor`, `@isPrefabStage`, `@selectionCount`).
- **Smooth Fade Animations:** Fluid UI Toolkit transition animations (`AnimateTransition = true`).
- **Disable vs Hide Flexibility:** Toggle between collapsing completely or greying out with custom opacity and disabled tooltips.
- **Zero-Polling Reactivity:** Bound to UI Toolkit property changes for immediate 0ms updates.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class AbilityConfig : MonoBehaviour
{
    public bool usesCooldown = true;

    // 1. Basic Boolean Toggle
    [ConditionalField(nameof(usesCooldown))]
    public float cooldownSeconds = 5.0f;

    // 2. Compound Inline Expression with DisableInsteadOfHide
    [ConditionalField("$usesCooldown && $cooldownSeconds > 10.0", DisableInsteadOfHide = true, DisabledTooltip = "Only active when cooldown exceeds 10s!")]
    public float cooldownReductionMultiplier = 0.8f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property | Method` |
| **Supported Types** | Any serializable field, property, or inspectable method |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes (Native VisualElement binding with zero-polling reactivity) |

---

## 4. Constructors & Parameters

```csharp
public ConditionalFieldAttribute()
public ConditionalFieldAttribute(string condition)
public ConditionalFieldAttribute(string condition, object compareValue)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `condition` | `string` | `null` | Primary condition string (member name, inline expression, parameterized method, or engine macro). |
| `compareValue` | `object` | `null` | Target value to compare against (enum value, integer threshold, string, or bitmask flag). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Condition` | `string` | `null` | Primary condition member name or expression. |
| `Conditions` | `string[]` | `null` | Array of multiple condition names to evaluate together. |
| `LogicOp` | `ConditionLogic` | `ConditionLogic.And` | Logical combination mode for multiple conditions (`And` or `Or`). |
| `CompareValue` | `object` | `null` | Value to compare the condition result against. |
| `ConditionOp` | `ConditionOperator` | `ConditionOperator.Equals` | Comparison operator (`Equals`, `NotEquals`, `GreaterThan`, `LessThan`, `GreaterThanOrEqual`, `LessThanOrEqual`, `HasFlag`). |
| `Inverse` | `bool` | `false` | Inverts the condition evaluation result (acts like Hide/Disable). |
| `DisableInsteadOfHide` | `bool` | `false` | When true, greys out the field rather than completely hiding it. |
| `DisabledOpacity` | `float` | `0.5f` | Visual opacity applied when disabled (`0.0f` to `1.0f`). |
| `DisabledTooltip` | `string` | `null` | Helpful tooltip displayed when hovering over the disabled field. |
| `AnimateTransition` | `bool` | `false` | Enables smooth fade animations when visibility toggles. |
| `FadeDuration` | `float` | `0.2f` | Duration in seconds of the fade animation. |
| `Order` | `int` | `0` | Execution priority relative to other attributes. |

---

## 6. Production-Grade Example

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class ProjectileLauncher : ModularMonoBehaviour
{
    public enum TrajectoryType { Linear, Ballistic, Homing }

    [Flags]
    public enum ProjectileModifiers
    {
        None = 0,
        Piercing = 1 << 0,
        Explosive = 1 << 1,
        Bouncing = 1 << 2,
        LaserBeam = 1 << 3
    }

    [Header("Trajectory & Modifiers")]
    public TrajectoryType trajectory = TrajectoryType.Linear;
    public ProjectileModifiers modifiers = ProjectileModifiers.Piercing;
    public int upgradeTier = 1;
    public float energyCost = 25f;

    // 1. Direct Enum Match with Animated Fade
    [ConditionalField(nameof(trajectory), TrajectoryType.Homing, AnimateTransition = true, FadeDuration = 0.3f)]
    public float homingTurnRate = 180f;

    // 2. Bitwise HasFlag Evaluation
    [ConditionalField(nameof(modifiers), ProjectileModifiers.Explosive, ConditionOp = ConditionOperator.HasFlag)]
    public float explosionRadius = 4.5f;

    // 3. Multi-Condition Array (AND / OR)
    [ConditionalField(nameof(trajectory), Conditions = new[] { "trajectory", "upgradeTier" }, LogicOp = ConditionLogic.And)]
    [InfoBox("High Tier Ballistic Trajectory Active!")]
    public float gravityMultiplier = 1.2f;

    // 4. Compound Inline C# Expression
    [ConditionalField("$upgradeTier >= 3 && ($energyCost < 50 || $trajectory == TrajectoryType.Homing)")]
    [InfoBox("Overcharged Core: Unlocked when Tier >= 3 AND (Energy < 50 OR Homing is active)!")]
    public ParticleSystem overchargeEffect;

    // 5. Parameterized Method Invocation with DisableInsteadOfHide
    [ConditionalField("CanEquipSpecialAmmo('Plasma', 5)", DisableInsteadOfHide = true, DisabledTooltip = "Requires Upgrade Tier 5!")]
    public int plasmaCartridges = 10;

    // 6. Global Engine State Macro (@)
    [ConditionalField("@isPlayMode")]
    public string liveBallisticsMonitor = "Active Projectiles: 0";

    public bool CanEquipSpecialAmmo(string ammoType, int minTier)
    {
        return upgradeTier >= minTier;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[ShowIf]` / `[HideIf]` | Specialized Aliases | Inherits from `ConditionalField`; use `ShowIf`/`HideIf` for cleaner syntax when simple visibility is needed. |
| `[EnableIf]` / `[DisableIf]` | Specialized Aliases | Inherits from `ConditionalField`; sets `DisableInsteadOfHide = true` automatically. |
| `[BoxGroup]` | Supported | Groups and cards respect conditional visibility of nested members. |
| `[CustomRange]` / `[ProgressBar]` | Supported | Dynamic fields work with all custom drawers seamlessly. |
