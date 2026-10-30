# [ReadOnly]

> Locks fields, properties, or buttons against user edits in the Inspector while keeping them visible, with optional dynamic conditional rules.

---

## 1. Overview & Value Proposition

**What it does:**
Disables interaction for decorated serialized fields, properties, or inspector buttons so they cannot be modified by designers, while remaining visible for debugging and telemetry. Supports dynamic condition members to toggle read-only state on the fly.

**The Problem:**
Developers frequently need to display internal state—such as current health, calculated DPS, unique entity GUIDs, or weapon cooldown states—in the Inspector so team members can monitor them during testing. Without a read-only attribute, designers might inadvertently change calculated fields or break system identifiers during runtime.

**The Solution:**
Add `[ReadOnly]` to any target:
- **Unconditional Locking:** Simply mark `[ReadOnly]` to keep the field permanently grayed out and unmodifiable.
- **Dynamic Condition Binding:** Pass a boolean field, property, or method name to toggle read-only state conditionally (e.g. `[ReadOnly("isLockedInCombat")]`).
- **Inverse Evaluation:** Pass `inverse: true` to make the field read-only when the condition evaluates to `false`.
- **Custom Visual Styling:** Adjust `DisabledOpacity` or inject custom disabled text colors to tailor visual hierarchy.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CharacterTelemetry : MonoBehaviour
{
    [ReadOnly]
    public string uniqueId = "HERO_PLAYER_001";

    [ReadOnly]
    public float currentSpeed = 12.4f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Field | AttributeTargets.Property | AttributeTargets.Method` |
| **Supported Types** | Any serialized type or parameterless method |
| **Collection Interface** | `ICollectionElementAttribute` |
| **Collection Cascading** | Full (`List<T>`, `T[]`, `AdvancedList<T>`, `SerializableDictionary<K, V>`) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ReadOnlyAttribute()
public ReadOnlyAttribute(string condition)
public ReadOnlyAttribute(string condition, bool inverse)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `condition` | `string` | `null` | Name of a boolean field, property, or method governing the read-only state. |
| `inverse` | `bool` | `false` | When `true`, inverts the condition evaluation (locks when condition is false). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Condition` | `string` | `null` | Evaluated member identifier controlling editability. |
| `Inverse` | `bool` | `false` | Inverts the conditional check logic. |
| `DisabledOpacity` | `float` | `0.5f` | Visual opacity applied to the element when disabled (`0.0` to `1.0`). |
| `DisabledColor` | `string` | `null` | Hex color tint applied to disabled labels or text. |
| `Order` | `int` | `0` | Execution order in the drawer modification stack. |

---

## 6. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class WeaponEquipmentManager : MonoBehaviour
{
    [Serializable]
    public class WeaponCalibration
    {
        public string calibrationId = "CAL-092";

        [ReadOnly]
        public float baseFrequency = 433.92f;
    }

    [Header("Permanent Hardware Specs")]
    [ReadOnly]
    public string weaponSerialNumber = "WEP-98421-MK4";

    [Header("Dynamic Locking State")]
    public bool isEquippedInBattle = false;

    // Only editable when NOT equipped in battle
    [ReadOnly(nameof(isEquippedInBattle))]
    public int ammoCapacity = 30;

    // Inverted: Only editable WHEN isEquippedInBattle is true
    [ReadOnly(nameof(isEquippedInBattle), inverse: true)]
    public float activeBattleOverheat = 15.2f;

    [Header("Calibration Profile (Inside Class)")]
    public WeaponCalibration calibrationProfile = new WeaponCalibration();

    [Header("Direct Collections Cascading")]
    [ReadOnly]
    public int[] hardwareUnitIds = new int[] { 1001, 1002, 1003, 1004 };

    [ReadOnly]
    public List<string> systemAuditLog = new List<string> { "Engine Initialized", "Server Connected" };

    [Header("Button Locking")]
    [ReadOnly(nameof(isEquippedInBattle))]
    [Button("Dismantle Weapon")]
    public void DismantleWeapon()
    {
        Debug.Log("Weapon dismantled into scrap materials.");
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Button]` | Supported | Safely disables button clicks when the read-only condition is met. |
| `[BoxGroup]` | Supported | Elements remain grouped inside boxes with dimmed appearance. |
| `[ShowIf]` | Supported | Plays nicely in sequence: condition evaluates visibility, read-only evaluates interaction. |
| `[AutoFill]` | Recommended | Lock auto-populated components from accidental drag modification. |

### Collection Cascading Matrix

| Collection Type | Cascading Behavior | Presentation Mode |
| :--- | :---: | :--- |
| `T[]` (Arrays) | **Supported** | Locks individual array element controls while retaining inspector readability. |
| `List<T>` | **Supported** | Elements in list rows are locked against user modification. |
| `AdvancedList<T>` | **Supported** | Read-only state cascades across advanced list card elements. |
| `SerializableDictionary<K, V>` | **Supported** | Locks dictionary value elements against edits. |
| Nested `[Serializable]` Classes | **Supported** | Fully locks specified member fields inside serialized objects. |
