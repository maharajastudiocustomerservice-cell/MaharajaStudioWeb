# [ShowIf]

> Displays a serialized field, property, or method in the Inspector only when a specified condition evaluates to true.
> Supports boolean flags, C#-style compound inline expressions, parameterized method calls, bitwise flags, engine macros, and relative parent traversal.

---

## 1. Overview & Value Proposition

**What it does:**
Renders an element in the Inspector only when its condition evaluates to `true`, collapsing it completely otherwise.

**The Problem:**
Game components frequently have modular settings (e.g., custom weapon configs, audio overrides, AI thresholds, network telemetry) that are only meaningful when specific features or modes are active. In standard Unity, all secondary parameters clutter the Inspector permanently, confusing game designers and cluttering the UI.

**The Solution:**
Add `[ShowIf]` above your fields, properties, or buttons:
- **Clean Responsive Inspectors:** Fields appear only when relevant, drastically reducing cognitive load.
- **Inline C#-Style Expressions:** Write compound multi-variable conditions (`[ShowIf("$health > 50 && $shield <= 0")]`) without writing boilerplate helper properties.
- **Parameterized Methods:** Re-use a single validator across multiple fields (`[ShowIf("HasPermission('Admin')")]`).
- **Bitwise Flag Operations:** Test `[System.Flags]` bitmasks directly using `ConditionOperator.HasFlag`.
- **Global Engine Macros:** Gate settings behind editor states (`@isPlayMode`, `@isEditor`, `@isPrefabStage`, `@selectionCount == 1`).
- **Parent Traversal:** Nested classes can inspect parent settings (`[ShowIf("$parent.enableAdvanced")]` or `[ShowIf("../isUnlocked")]`).
- **Zero-Polling Reactivity:** Powered by UI Toolkit property tracking for instant 0ms response times.
- **Typo Protection:** If a member name is misspelled, MSUltimate logs a suggestion in the console (e.g., *"Did you mean 'isAlive'?"*) rather than failing silently.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class VehicleController : MonoBehaviour
{
    public bool enableTurboBoost;

    // 1. Basic Boolean Toggle
    [ShowIf(nameof(enableTurboBoost))]
    public float turboSpeedMultiplier = 2.0f;

    // 2. Inline C#-Style Expression (No helper property needed!)
    [ShowIf("$turboSpeedMultiplier >= 3.0 && enableTurboBoost")]
    public ParticleSystem overchargeFlames;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property | Method` |
| **Supported Types** | Any serializable field, property, or method |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes (Native VisualElement binding with zero-polling reactivity) |

---

## 4. Constructors & Parameters

```csharp
public ShowIfAttribute(string condition)
public ShowIfAttribute(string condition, object compareValue)
public ShowIfAttribute(string condition, object compareValue, ConditionOperator conditionOp)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `condition` | `string` | *(Required)* | Name of the boolean member, parameterized method (`Check('A')`), engine macro (`@isPlayMode`), or inline expression (`$a > 10 && $b`). |
| `compareValue` | `object` | `null` | Target value to compare against (enum value, string, number, or bitmask flag). |
| `conditionOp` | `ConditionOperator` | `ConditionOperator.Equals` | Comparison operator (`Equals`, `NotEquals`, `GreaterThan`, `LessThan`, `GreaterThanOrEqual`, `LessThanOrEqual`, `HasFlag`). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ConditionOp` | `ConditionOperator` | `ConditionOperator.Equals` | Comparison operator evaluated against `compareValue`. |
| `AnimateTransition` | `bool` | `false` | Enables smooth fade and height expansion animations when visibility toggles. |
| `FadeDuration` | `float` | `0.2f` | Duration in seconds of the reveal animation. |
| `Order` | `int` | `0` | Execution priority relative to other attributes. |

---

## 6. Production-Grade Example

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CombatController : ModularMonoBehaviour
{
    public enum WeaponMode { Melee, Ranged, Magic }

    [Flags]
    public enum ElementAffinities
    {
        None = 0,
        Fire = 1 << 0,
        Frost = 1 << 1,
        Lightning = 1 << 2
    }

    [Serializable]
    public class NestedCombatProfile
    {
        // 1. Sibling / Parent Relative Traversal
        [ShowIf("$parent.enableAdvancedCombat")]
        public float parentDrivenMultiplier = 2.5f;

        [ShowIf("../playerLevel", 20, ConditionOperator.GreaterThanOrEqual)]
        public string masterRankTitle = "Grandmaster";
    }

    [Header("Core State")]
    public bool enableAdvancedCombat = true;
    public WeaponMode activeWeaponMode = WeaponMode.Magic;
    public ElementAffinities activeElements = ElementAffinities.Fire | ElementAffinities.Lightning;
    public int playerLevel = 25;
    public float currentHealth = 20f;
    public bool isInvincible = false;

    // 2. Direct Enum Matching
    [ShowIf(nameof(activeWeaponMode), WeaponMode.Magic)]
    public float manaCostPerCast = 35f;

    // 3. Bitwise Flag Check (HasFlag)
    [ShowIf(nameof(activeElements), ElementAffinities.Fire, ConditionOperator.HasFlag)]
    public float fireBurnDuration = 6.0f;

    // 4. Inline C#-Style Expression (Compound Logic & Precedence)
    [ShowIf("$playerLevel >= 20 && $activeWeaponMode == WeaponMode.Magic")]
    [InfoBox("Archmage Stance Unlocked!", InspectorMessageType.Success)]
    public string ultimateSpell = "Cataclysmic Nova";

    // 5. Expression with Grouping & Negation
    [ShowIf("($currentHealth < 25 || $playerLevel < 5) && !$isInvincible")]
    [InfoBox("Critical Health Warning!", InspectorMessageType.Warning)]
    public Color alertVignetteColor = Color.red;

    // 6. Parameterized Method Invocation
    [ShowIf("CanEquipGear('Excalibur', 20)")]
    public string excaliburGemSocket = "Radiant Diamond";

    // 7. Global Context Engine Macro (@)
    [ShowIf("@isPlayMode")]
    public string liveTelemetry = "Target TPS: 60 | Active Buffs: 3";

    // 8. Nested Object Parent Traversal
    public NestedCombatProfile profile = new NestedCombatProfile();

    // Validator method used by [ShowIf("CanEquipGear(...)")]
    public bool CanEquipGear(string gearName, int minLevel)
    {
        return playerLevel >= minLevel;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[HideIf]` | Counterpart | Opposite behavior; hides when condition is true. |
| `[EnableIf]` / `[DisableIf]` | Complementary | Controls interactivity (greying out) rather than collapsing visibility. |
| `[BoxGroup]` / `[TabGroup]` | Supported | Fully compatible inside box cards, tab layouts, and foldouts. |
| `[Button]` | Supported | Place above methods to conditionally reveal action buttons in the Inspector. |
| `[InfoBox]` | Supported | Stacks cleanly to show explanatory alerts alongside conditional fields. |
| `[Range]` / `[MinMaxSlider]` | Supported | Works seamlessly with sliders, vectors, color pickers, and all serializable types. |
