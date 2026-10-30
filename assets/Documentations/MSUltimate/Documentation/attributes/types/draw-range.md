# [DrawRange]

> Customizes the visual presentation of SerializableRange fields with an interactive dual-thumb min/max range slider, boundary limits, and numeric input fields.

---

## 1. Overview & Value Proposition

**What it does:**
Renders an interactive min-max dual-handle slider for `SerializableRange` fields. Allows developers and designers to adjust lower and upper bounds simultaneously with visual feedback, numeric inputs, and custom colored slider fill bars.

**The Problem:**
Standard serialized min-max ranges in Unity require two separate numeric fields (e.g. `minDamage` and `maxDamage`), with no visual boundary slider and no built-in guard against setting the minimum higher than the maximum.

**The Solution:**
Add `[DrawRange]` to any `SerializableRange` field:
- **Interactive Dual-Thumb Slider:** Drag min and max handles visually along the range track.
- **Accurate Numeric Fields:** Edit exact min and max numbers directly in synced input boxes.
- **Step Snapping:** Specify a `Step` increment for integer or discrete stepping (e.g. `Step = 5f`).
- **Accent Theming:** Color the slider bar with custom hex palettes (`ColorHex = "#f1c40f"`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.Types;

public class LootDrop : MonoBehaviour
{
    [DrawRange(0f, 100f, Step = 1f, ColorHex = "#f1c40f")]
    public SerializableRange goldReward = new SerializableRange(10f, 50f);
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `SerializableRange<T>`, or collections (`SerializableRange<T>[]`, `List<SerializableRange<T>>`) |
| **Collection Cascading**| Supported via `ICollectionElementAttribute` (`CollectionElementRole.Element \| Key \| Value \| NullableValue \| TupleItem`) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public DrawRangeAttribute(float minLimit = 0f, float maxLimit = 100f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `minLimit` | `float` | `0f` | Minimum boundary limit for the range slider. |
| `maxLimit` | `float` | `100f` | Maximum boundary limit for the range slider. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MinLimit` | `float` | `0f` | Minimum boundary limit for the slider. |
| `MaxLimit` | `float` | `100f` | Maximum boundary limit for the slider. |
| `Step` | `float` | `0f` | Dragging step increment (`0` for smooth continuous). |
| `ShowSlider` | `bool` | `true` | Whether to display the interactive slider bar. |
| `ShowInputs` | `bool` | `true` | Whether to show numeric min/max input fields beside the slider. |
| `ColorHex` | `string` | `null` | Hex color for the active range slider fill bar. |
| `Order` | `int` | `0` | Execution priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.Types;

public class EnemySpawner : MonoBehaviour
{
    [Header("Wave Spawn Delay (Seconds)")]
    [DrawRange(1f, 60f, Step = 0.5f, ColorHex = "#3498db")]
    public SerializableRange spawnDelaySeconds = new SerializableRange(5f, 15f);

    [Header("Encounter Enemy Pack Size")]
    [DrawRange(1f, 30f, Step = 1f, ColorHex = "#e74c3c")]
    public SerializableRange packSize = new SerializableRange(3f, 8f);

    [Header("Direct Collection Cascading")]
    [DrawRange(0f, 500f, Step = 10f, ColorHex = "#10B981")]
    [Tooltip("Cascades range sliders and limits to each list element.")]
    public List<SerializableRange<float>> difficultyDamageBands;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Fits cleanly inside groups and layout cards. |
| `[ShowIf]` | Supported | Dynamic conditional visibility supported. |
| `[ReadOnly]` | Supported | Disables handle dragging and greys out numeric inputs. |
| Collections (`List<T>`, `T[]`) | Supported | Implements `ICollectionElementAttribute` to automatically cascade range sliders and limits to collection elements. |

