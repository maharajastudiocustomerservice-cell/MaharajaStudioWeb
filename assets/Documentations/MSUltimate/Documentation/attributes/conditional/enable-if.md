# [EnableIf]

> Enables user interaction with a serialized field, property, or button only when a specified condition evaluates to true (greying it out otherwise).
> Supports boolean flags, C#-style compound inline expressions, parameterized method calls, bitwise flags, engine macros, and relative parent traversal.

---

## 1. Overview & Value Proposition

**What it does:**
Keeps a field visible in the Inspector but greys it out (read-only state) until a prerequisite setting or criteria is met.

**The Problem:**
In standard Unity, secondary settings sit wide open for editing even when their parent feature is turned off. Game designers modify values that have zero actual effect, leading to phantom bug reports and frustration.

**The Solution:**
Add `[EnableIf]` above dependent fields, properties, or methods:
- **Prerequisite Enforcement:** Dependent fields stay visible so designers know they exist, but are interactively locked until unlocked.
- **Custom Disabled Tooltips:** Inform designers exactly *why* a field is greyed out (e.g. `DisabledTooltip = "Unlock at Level 10!"`).
- **Inline C#-Style Expressions:** Enable fields based on compound logic (`[EnableIf("$playerLevel >= 10 && $isLicensed")]`).
- **Parameterized Methods:** Re-use flexible validator methods with literal arguments (`[EnableIf("HasPermission('Admin')")]`).
- **Bitwise Flag Checking:** Unlock fields when specific bitmasks are active (`ConditionOperator.HasFlag`).
- **Engine State Macros:** Enable fields only when conditions match (`[EnableIf("@selectionCount == 1")]`).
- **Parent Relative Traversal:** Modular child classes can read enable state from their parent (`[EnableIf("$parent.allowEditing")]`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CharacterShield : MonoBehaviour
{
    public bool hasEnergyShield;

    // 1. Basic Boolean Toggle with Custom Tooltip
    [EnableIf(nameof(hasEnergyShield), DisabledTooltip = "Enable Energy Shield to edit capacity!")]
    public float maxShieldCapacity = 100f;

    // 2. Compound Inline Expression
    [EnableIf("$hasEnergyShield && $maxShieldCapacity > 50")]
    public float shieldRechargeRate = 12.5f;
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
public EnableIfAttribute(string condition)
public EnableIfAttribute(string condition, object compareValue)
public EnableIfAttribute(string condition, object compareValue, ConditionOperator conditionOp)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `condition` | `string` | *(Required)* | Name of the boolean member, parameterized method (`Check('A')`), engine macro (`@isEditor`), or inline expression (`$level >= 10`). |
| `compareValue` | `object` | `null` | Target value to compare against (enum value, string, number, or bitmask flag). |
| `conditionOp` | `ConditionOperator` | `ConditionOperator.Equals` | Comparison operator (`Equals`, `NotEquals`, `GreaterThan`, `LessThan`, `GreaterThanOrEqual`, `LessThanOrEqual`, `HasFlag`). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `DisabledOpacity` | `float` | `0.5f` | Visual opacity applied to the element when disabled (`0.0f` to `1.0f`). |
| `DisabledTooltip` | `string` | `null` | Explanatory message displayed when hovering over the disabled field. |
| `ConditionOp` | `ConditionOperator` | `ConditionOperator.Equals` | Comparison operator evaluated against `compareValue`. |
| `AnimateTransition` | `bool` | `false` | Enables smooth fade transitions when the interactive state changes. |
| `FadeDuration` | `float` | `0.2f` | Duration in seconds of the fade animation. |
| `Order` | `int` | `0` | Execution priority relative to other attributes. |

---

## 6. Production-Grade Example

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class NetworkSyncManager : ModularMonoBehaviour
{
    [Flags]
    public enum LicenseFlags
    {
        None = 0,
        Standard = 1 << 0,
        Enterprise = 1 << 1,
        CloudAnalytics = 1 << 2
    }

    [Header("License & Connectivity")]
    public LicenseFlags licenses = LicenseFlags.Standard;
    public bool isConnectedToCloud = false;
    public int subscriptionTier = 2;

    // 1. Basic Boolean Toggle with Explanatory Tooltip
    [EnableIf(nameof(isConnectedToCloud), DisabledTooltip = "Connect to Cloud to configure server endpoint!")]
    public string cloudServerEndpoint = "https://gateway.mygame.com/v2";

    // 2. Bitwise Flag Check
    [EnableIf(nameof(licenses), LicenseFlags.Enterprise, ConditionOperator.HasFlag, DisabledTooltip = "Requires Enterprise License!")]
    public int maxConcurrentPlayers = 10000;

    // 3. Compound Inline C# Expression
    [EnableIf("$isConnectedToCloud && $subscriptionTier >= 2")]
    [InfoBox("Live Sync: Enabled when Connected AND Tier >= 2!")]
    public float syncTickRateHz = 60.0f;

    // 4. Parameterized Method Invocation
    [EnableIf("HasRole('Administrator')")]
    public string debugServerToken = "SEC-TOKEN-ADMIN-4491";

    // 5. Global Context Engine Macro (@)
    [EnableIf("@selectionCount == 1", DisabledTooltip = "Disabled during multi-selection to prevent batch overwrite.")]
    public string uniqueInstanceId = "INST-GLOBAL-01";

    public bool HasRole(string requiredRole)
    {
        return requiredRole == "Administrator" && subscriptionTier >= 3;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[DisableIf]` | Counterpart | Opposite behavior; disables when condition is true. |
| `[ShowIf]` / `[HideIf]` | Complementary | Use ShowIf to collapse visibility; use EnableIf to keep layout stable and grey out. |
| `[BoxGroup]` | Supported | Fully compatible inside box layouts and groups. |
| `[Button]` | Supported | Grey out action buttons when conditions are unmet. |
| `[Range]` / `[MinMaxSlider]` | Supported | Sliders smoothly lock and disable handles when condition evaluates to false. |
