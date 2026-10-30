# [HideIf]

> Completely hides and collapses a serialized field, property, or method from the Inspector when a specified condition evaluates to true.
> Supports boolean flags, C#-style compound inline expressions, parameterized method calls, bitwise flags, engine macros, and relative parent traversal.

---

## 1. Overview & Value Proposition

**What it does:**
Removes irrelevant fields from view entirely when a condition is met, keeping your Inspector clean and focused on what matters right now.

**The Problem:**
Complex game components frequently accumulate dozens of specialized fields (e.g. invulnerability toggles, god-mode overrides, platform-specific settings, debug logs). In standard Unity, secondary parameters always remain visible, leading to confusing layouts and cluttered inspectors.

**The Solution:**
Add `[HideIf]` above fields, properties, or buttons:
- **Zero Screen Clutter:** Collapses the entire field row, reclaiming vertical Inspector space.
- **Inline C#-Style Expressions:** Hide fields when arbitrary formulas evaluate to true (e.g. `[HideIf("$health <= 0 || $isDead")]`).
- **Parameterized Methods:** Re-use a single validator to hide fields based on argument criteria (`[HideIf("IsRestrictedTier('Trial')")]`).
- **Bitwise Flag Support:** Hide fields when an enum bitmask flag is present (`ConditionOperator.HasFlag`).
- **Engine State Macros:** Hide scene-specific fields when editing in isolation (`[HideIf("@isPrefabStage")]`).
- **Parent Relative Traversal:** Hide fields in modular child objects based on parent settings (`[HideIf("$parent.lockSettings")]`).
- **Typo Protection:** Misspelled condition names trigger actionable console warnings with suggestions rather than failing silently.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class EnemyStats : MonoBehaviour
{
    public bool isInvulnerable;

    // 1. Basic Boolean Inversion
    [HideIf(nameof(isInvulnerable))]
    public int maxHealth = 100;

    // 2. Compound Inline Expression
    [HideIf("$isInvulnerable || $maxHealth <= 0")]
    public float damageVulnerability = 1.0f;
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
public HideIfAttribute(string condition)
public HideIfAttribute(string condition, object compareValue)
public HideIfAttribute(string condition, object compareValue, ConditionOperator conditionOp)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `condition` | `string` | *(Required)* | Name of the member, parameterized method (`Check('A')`), engine macro (`@isPrefabStage`), or inline expression (`$health <= 0`). |
| `compareValue` | `object` | `null` | Target value to compare against (enum value, string, number, or bitmask flag). |
| `conditionOp` | `ConditionOperator` | `ConditionOperator.Equals` | Comparison operator (`Equals`, `NotEquals`, `GreaterThan`, `LessThan`, `GreaterThanOrEqual`, `LessThanOrEqual`, `HasFlag`). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ConditionOp` | `ConditionOperator` | `ConditionOperator.Equals` | The comparison operator evaluated against `compareValue`. |
| `AnimateTransition` | `bool` | `false` | Enables smooth height collapse animations when visibility changes. |
| `FadeDuration` | `float` | `0.2f` | Duration in seconds of the collapse animation. |
| `Order` | `int` | `0` | Execution priority relative to other attributes. |

---

## 6. Production-Grade Example

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class LootChestController : ModularMonoBehaviour
{
    public enum ChestType { Wooden, Silver, LockedVault }

    [Flags]
    public enum ChestProtections
    {
        None = 0,
        FireTrap = 1 << 0,
        ElectricLock = 1 << 1,
        MagicSeal = 1 << 2
    }

    [Header("Chest Configuration")]
    public ChestType chestType = ChestType.Wooden;
    public ChestProtections protections = ChestProtections.None;
    public bool isUnlocked = false;
    public int tierLevel = 1;

    // 1. Hide when chest is already unlocked
    [HideIf(nameof(isUnlocked))]
    public int lockpickDifficulty = 5;

    // 2. Hide using direct enum comparison
    [HideIf(nameof(chestType), ChestType.LockedVault, ConditionOperator.NotEquals)]
    public string goldenKeyId = "KEY_VAULT_99";

    // 3. Hide using Bitwise HasFlag
    [HideIf(nameof(protections), ChestProtections.MagicSeal, ConditionOperator.HasFlag)]
    public float nonMagicalSmashResistance = 50f;

    // 4. Hide using Compound Inline Expression
    [HideIf("$isUnlocked || $tierLevel < 5")]
    [InfoBox("High Tier Defense Active: Visible only when chest is locked AND tier >= 5!")]
    public string reinforcedPlateMaterial = "Titanium";

    // 5. Hide using Parameterized Method Validator
    [HideIf("IsExemptFromLootTable('HolidayEvent')")]
    public string seasonalDropTable = "Loot_Halloween_2026";

    // 6. Global Context Engine Macro (@)
    [HideIf("@isPrefabStage")]
    [InfoBox("Hides when editing inside Prefab Isolation mode to prevent invalid scene references.")]
    public GameObject sceneWorldAnchor;

    public bool IsExemptFromLootTable(string eventName)
    {
        return eventName == "HolidayEvent" && tierLevel <= 1;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[ShowIf]` | Counterpart | Opposite behavior; reveals when condition evaluates to true. |
| `[DisableIf]` | Complementary | Greys out element instead of collapsing visibility. |
| `[BoxGroup]` | Supported | Functions normally inside card layouts and foldouts. |
| `[Button]` | Supported | Place above methods to conditionally hide action buttons. |
| `[InfoBox]` | Supported | Pair with info alerts to describe why fields disappear. |
