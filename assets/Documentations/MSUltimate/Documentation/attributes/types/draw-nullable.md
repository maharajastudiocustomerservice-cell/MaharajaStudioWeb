# [DrawNullable]

> Customizes the visual presentation of SerializableNullable fields with optional null indicators, custom toggle labels, accent coloring, and layout alignments.

---

## 1. Overview & Value Proposition

**What it does:**
Enhances the display of nullable wrapped types (`SerializableNullable<T>`) in the Inspector. Renders an intuitive on/off toggle beside the value, with custom placeholder text for null states, toggle position swapping, and colored accent badges.

**The Problem:**
Standard Unity serialization cannot natively serialize `Nullable<T>` or `T?` value types. Custom nullable wrapper structs often render clumsily with raw boolean flags and separate value fields taking up unnecessary inspector space.

**The Solution:**
Add `[DrawNullable]` to any `SerializableNullable` field:
- **Clean Inline Toggle:** An integrated checkbox directly activates or deactivates the value without messy nested foldouts.
- **Null State Feedback:** Clear customizable placeholder text (`NullLabel = "Disabled / No Limit"`) when toggled off.
- **Layout Inversion:** Use `ToggleOnRight = true` to align the enable checkbox with right-hand toggles.
- **Accent Theming:** Highlight active nullable states using custom hex accents.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.Types;

public class PlayerMovement : MonoBehaviour
{
    [DrawNullable(NullLabel = "Unlimited Speed", ColorHex = "#00FF88")]
    public SerializableNullable<float> maxSprintSpeed;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `SerializableNullable<T>`, or collections (`SerializableNullable<T>[]`, `List<SerializableNullable<T>>`) |
| **Collection Cascading**| Supported via `ICollectionElementAttribute` (`CollectionElementRole.Element \| Key \| Value \| NullableValue \| TupleItem`) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public DrawNullableAttribute()
```

*This attribute uses parameterless initialization; customize its appearance via object initializer properties.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `NullLabel` | `string` | `"None (null)"` | Custom label shown when the nullable field is null / toggled off. |
| `ToggleLabel` | `string` | `null` | Optional custom label beside the field toggle checkbox. |
| `ColorHex` | `string` | `null` | Hex color string for active checkbox and accent state. |
| `ToggleOnRight` | `bool` | `false` | If true, positions the toggle checkbox on the right side of the control. |
| `Order` | `int` | `0` | Execution priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.Types;

public class WeaponStats : MonoBehaviour
{
    [Header("Optional Ammo Capacity (Null = Infinite)")]
    [DrawNullable(NullLabel = "Infinite Ammo", ColorHex = "#3498db")]
    public SerializableNullable<int> maxMagazineCapacity;

    [Header("Optional Weapon Overheat Temperature")]
    [DrawNullable(NullLabel = "No Overheat", ToggleOnRight = true)]
    public SerializableNullable<float> maxTemperature;

    [Header("Direct Collection Cascading")]
    [DrawNullable(ToggleLabel = "Equip Buff", NullLabel = "No Buff", ColorHex = "#38BDF8")]
    [Tooltip("Cascades nullable toggle styling to each collection item.")]
    public List<SerializableNullable<int>> slotBuffs;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Renders compactly inside group layouts. |
| `[ShowIf]` | Supported | Conditionally reveal or hide based on other boolean conditions. |
| `[ReadOnly]` | Supported | Locks both the toggle checkbox and the wrapped value field. |
| Collections (`List<T>`, `T[]`) | Supported | Implements `ICollectionElementAttribute` to automatically cascade nullable styling to each element. |

