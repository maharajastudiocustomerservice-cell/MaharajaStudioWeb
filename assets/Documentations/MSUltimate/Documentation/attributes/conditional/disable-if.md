# [DisableIf]

> Greys out and disables user interaction with a serialized field, property, or button when a specified condition evaluates to true.
> Supports boolean flags, C#-style compound inline expressions, parameterized method calls, bitwise flags, engine macros, and relative parent traversal.

---

## 1. Overview & Value Proposition

**What it does:**
Disables (greys out) a field so designers cannot edit it when conditions are met, while still keeping its current value clearly readable.

**The Problem:**
Hiding a field completely can disorient game designers who wonder why a setting disappeared from the Inspector. In many design setups, you want the setting to remain visible for scannability and context, but prevent modifications when a master feature is toggled off or inactive.

**The Solution:**
Add `[DisableIf]` above any serialized field, property, or button:
- **Preserve Context & Values:** Fields remain visible with a clean greyed-out disabled style so team members can still inspect data.
- **Accidental Edit Protection:** Prevents altering stats when prerequisites or sub-systems are inactive.
- **Inline C#-Style Expressions:** Disable fields when multi-variable formulas evaluate to true (`[DisableIf("$isInvulnerable || $maxHealth <= 0")]`).
- **Parameterized Methods:** Re-use a single validator across multiple fields (`[DisableIf("IsRestrictedRole('Guest')")]`).
- **Bitwise Flag Checking:** Disable fields when specific bitmasks are active (`ConditionOperator.HasFlag`).
- **Engine State Macros:** Lock fields dynamically during runtime play mode (`[DisableIf("@isPlayMode")]`).
- **Parent Relative Traversal:** Modular child classes can disable fields based on parent state (`[DisableIf("$parent.lockSettings")]`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class WeaponSettings : MonoBehaviour
{
    public bool isInfiniteAmmo;

    // 1. Basic Boolean Inversion with Disabled Tooltip
    [DisableIf(nameof(isInfiniteAmmo), DisabledTooltip = "Magazine capacity cannot be edited while Infinite Ammo is ON.")]
    public int maxMagazineCapacity = 30;

    // 2. Compound Inline Expression
    [DisableIf("$isInfiniteAmmo || $maxMagazineCapacity <= 0")]
    public float reloadDurationSeconds = 2.2f;
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
public DisableIfAttribute(string condition)
public DisableIfAttribute(string condition, object compareValue)
public DisableIfAttribute(string condition, object compareValue, ConditionOperator conditionOp)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `condition` | `string` | *(Required)* | Name of the member, parameterized method (`Check('A')`), engine macro (`@isPlayMode`), or inline expression (`$val <= 0`). |
| `compareValue` | `object` | `null` | Target value to compare against (enum value, string, number, or bitmask flag). |
| `conditionOp` | `ConditionOperator` | `ConditionOperator.Equals` | Comparison operator (`Equals`, `NotEquals`, `GreaterThan`, `LessThan`, `GreaterThanOrEqual`, `LessThanOrEqual`, `HasFlag`). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `DisabledOpacity` | `float` | `0.5f` | Visual opacity applied to the field elements when disabled (`0.0f` to `1.0f`). |
| `DisabledTooltip` | `string` | `null` | Explanatory message displayed when the user hovers over the disabled field. |
| `ConditionOp` | `ConditionOperator` | `ConditionOperator.Equals` | Comparison operator evaluated against `compareValue`. |
| `AnimateTransition` | `bool` | `false` | Enables smooth fade transitions when the disabled state changes. |
| `FadeDuration` | `float` | `0.2f` | Duration in seconds of the fade animation. |
| `Order` | `int` | `0` | Execution priority relative to other attributes. |

---

## 6. Production-Grade Example

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class VehicleDrivetrain : ModularMonoBehaviour
{
    public enum TransmissionType { Automatic, Manual, Electric }

    [Flags]
    public enum EngineLocks
    {
        None = 0,
        Overheated = 1 << 0,
        MaintenanceMode = 1 << 1,
        EmergencyBrake = 1 << 2
    }

    [Header("Drivetrain Setup")]
    public TransmissionType transmission = TransmissionType.Automatic;
    public EngineLocks activeLocks = EngineLocks.None;
    public float engineHealth = 100f;
    public bool isParked = true;

    // 1. Direct Enum Match
    [DisableIf(nameof(transmission), TransmissionType.Automatic, DisabledTooltip = "Clutch stiffness only applies to Manual transmission.")]
    [Range(0.1f, 1.0f)]
    public float clutchStiffness = 0.5f;

    // 2. Bitwise HasFlag Check
    [DisableIf(nameof(activeLocks), EngineLocks.EmergencyBrake, ConditionOperator.HasFlag, DisabledTooltip = "Disabled while Emergency Brake is engaged!")]
    public float accelerationThrottle = 1.0f;

    // 3. Compound Inline Expression
    [DisableIf("$engineHealth <= 0 || $isParked")]
    [InfoBox("Engine Offline: Controls are locked when Engine Health <= 0 OR Vehicle is Parked!")]
    public float targetRpmLimit = 7500f;

    // 4. Parameterized Method Invocation
    [DisableIf("IsLockActive('MaintenanceMode')")]
    public float nitrousBoostMultiplier = 2.0f;

    // 5. Global Context Engine Macro (@)
    [DisableIf("@isPlayMode", DisabledTooltip = "Core tuning constants cannot be modified while Play Mode is running.")]
    public int baseGearRatio = 4;

    public bool IsLockActive(string lockName)
    {
        return lockName == "MaintenanceMode" && activeLocks.HasFlag(EngineLocks.MaintenanceMode);
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[EnableIf]` | Counterpart | Opposite behavior; enables when condition is true. |
| `[ShowIf]` / `[HideIf]` | Complementary | Use ShowIf to collapse visibility; use DisableIf to preserve layout and grey out. |
| `[BoxGroup]` | Supported | Functions normally inside card layouts and foldouts. |
| `[Button]` | Supported | Grey out action buttons when conditions are met. |
| `[Range]` / `[MinMaxSlider]` | Supported | Sliders smoothly lock and disable handles when condition evaluates to true. |
