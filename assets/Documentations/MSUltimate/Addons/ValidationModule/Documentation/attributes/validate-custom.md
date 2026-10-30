# [ValidateCustom]

> Validates a serialized field using a custom boolean callback method declared on the enclosing class.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateCustom]` evaluates complex, domain-specific validation logic by invoking a designated method name (`ConditionMethod`) on the enclosing class via reflection. The callback method must return a `bool` (optionally accepting the field value as a parameter). If the method returns `false`, a validation error banner is displayed in the Inspector.

**The Problem:**
Generic attributes like `[ValidateRange]` or `[ValidateNotNull]` cover common primitive rules, but game development frequently requires bespoke, multi-variable business logic: e.g., checking if a weapon's ammo caliber matches its magazine type, verifying if a curve's integral equals 1.0, or ensuring a color palette contains sufficient perceptual contrast. Standard Unity provides no standardized way to display custom validation warnings in the Inspector without writing full custom property drawers.

**The Solution:**
Decorating fields with `[ValidateCustom]`:
- **Arbitrary C# Logic:** Write any custom validation predicate directly in your MonoBehaviour or ScriptableObject.
- **Auto-Discovery by Engine:** Implements `IValidationAttribute`, meaning the project-wide Validation Engine automatically discovers and executes your custom method during asset scans.
- **Multiple Custom Checks:** Stack multiple attributes (`AllowMultiple = true`) to evaluate distinct conditions on the same field.
- **Seamless Inspector Integration:** Renders standard MSUltimate styled validation warning banners without writing custom Editor scripts.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class EnergyShield : MonoBehaviour
{
    [ValidateCustom(nameof(ValidateShieldCapacity), "Shield capacity must be an even multiple of 50.")]
    public int shieldCapacity = 150;

    private bool ValidateShieldCapacity()
    {
        return shieldCapacity > 0 && shieldCapacity % 50 == 0;
    }
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
| **Validation Interface** | `IValidationAttribute`, `ICollectionElementAttribute` |

---

## 4. Constructors & Parameters

```csharp
public ValidateCustomAttribute(string conditionMethod, string message = "Validation failed.")
```

- **`conditionMethod`** (`string`): The name of the method to invoke (recommend using `nameof(MyMethod)`). The method should return a `bool`.
- **`message`** (`string`, optional): Custom error message displayed when the method returns `false`.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ConditionMethod` | `string` | Assigned in constructor | Name of the boolean callback method to invoke. |
| `Message` | `string` | `"Validation failed."` | Failure explanation displayed in the validation message banner. |
| `MessageType` | `InspectorMessageType` | `InspectorMessageType.Error` | Visual severity badge (`None`, `Info`, `Warning`, `Error`). |
| `ErrorColor` | `string` | `null` | Hex text color override for the validation error banner. |
| `ErrorBackgroundColor` | `string` | `null` | Hex background color override for the alert box. |
| `FontSize` | `int` | `0` | Font size override in pixels (0 uses default inspector font size). |
| `Padding` | `float` | `0f` | Internal padding around the validation banner. |
| `Margin` | `float` | `5f` | Outer margin spacing separating the banner from neighboring controls. |

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.ValidationModule;

namespace ProjectZero.Audio
{
    public class AudioEqualizerPreset : MonoBehaviour
    {
        [Header("Frequency Frequencies")]
        [ValidateCustom(nameof(ValidateFrequencyOrder), 
            message: "Low cut frequency must be strictly less than high cut frequency.",
            MessageType = InspectorMessageType.Error)]
        public float lowCutHz = 80f;
        public float highCutHz = 16000f;

        [Header("Gain Normalization")]
        [ValidateCustom(nameof(ValidateGainHeadroom), 
            message: "Master gain exceeds safe ceiling (+6 dB) and may cause clipping distortion.",
            MessageType = InspectorMessageType.Warning)]
        public float masterGainDb = 0f;

        private bool ValidateFrequencyOrder()
        {
            return lowCutHz < highCutHz;
        }

        private bool ValidateGainHeadroom()
        {
            return masterGainDb <= 6.0f;
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateIf]`** | High | Combine custom validation callbacks with conditional evaluation triggers. |
| **`[BoxGroup]`** | High | Visualizes cleanly inside grouped inspector cards. |
| **`[Range]` / `[MinMaxSlider]`** | High | Pair standard visual slider controls with custom validation logic. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans. |

### Collection Cascading & Serializer Matrix

| Collection / Container Type | Supported | Behavior |
| :--- | :---: | :--- |
| **`List<T>`** | Yes | Cascades callback evaluation to each element in the collection. |
| **`T[]`** | Yes | Cascades callback evaluation across each array element. |
| **`AdvancedList<T>`** | Yes | Full element-level validation support with dynamic item reordering. |
| **`SerializableDictionary<K, V>`** | Yes | Evaluates custom callback against key or value element entries. |
| **`SerializableNullable<T>`** | Yes | Evaluates custom callback when value is populated. |
| **`SerializableTuple<...>`** | Yes | Evaluates custom callback on tuple member fields. |
