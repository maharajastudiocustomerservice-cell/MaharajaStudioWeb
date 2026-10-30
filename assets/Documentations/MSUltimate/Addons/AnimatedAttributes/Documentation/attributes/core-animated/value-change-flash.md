# [ValueChangeFlash]

> Flashes an energetic color accent and scale bump whenever an inspector field value is altered or updated by tools.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValueChangeFlash]` listens for value mutations on a serialized field and triggers an instantaneous animated visual flash. Whenever the value changes—via keyboard typing, slider dragging, undo/redo operations, or script assignment—the control produces a transient background color flash (`FlashColor`) and a tactile scale bump (`ScaleBump`).

**The Problem:**
When balancing gameplay stats, scrubbing live parameters in Play Mode, or running editor utility scripts, it is hard to tell whether a setting was modified or if an automation method actually touched a field.

**The Solution:**
Applying `[ValueChangeFlash]` to fields:
- **Instant Mutation Acknowledgment:** Confirms changes visually with a crisp, momentary highlight flash.
- **Micro-Scale Dynamics:** Applies a subtle, responsive scale bump (`ScaleBump`) that gives data editing a tactile, physical quality.
- **Customizable Flash Palette:** Pick any hex color and opacity (e.g., emerald green `#4CAF5055` for rewards, gold `#FFD70055` for levels).
- **Automation Visibility:** Instantly illuminates values when modified programmatically by custom inspector buttons or external tooling.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class PlayerStats : MonoBehaviour
{
    [ValueChangeFlash(FlashColor = "#10B98155", FlashDuration = 400f)]
    public int experiencePoints = 1200;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field, property, array (`T[]`), list (`List<T>`), or dictionary value |
| **Collection Interface** | `ICollectionElementAttribute` (Automatic Element Cascading) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ValueChangeFlashAttribute()
public ValueChangeFlashAttribute(string flashColor, float flashDuration = 500f)
```

*Initializes a value change flash with emerald tint and 1.05x scale bump by default, or with custom hex flash color and millisecond duration.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `FlashColor` | `string` | `"#4CAF5055"` | Hex color string for the background highlight flash tint. |
| `FlashDuration` | `float` | `500f` | Total fade duration in milliseconds of the flash transition. |
| `ScaleBump` | `float` | `1.05f` | Scale multiplier reached during the initial peak of the change bump. |
| `AnimateBackgroundColor` | `bool` | `true` | Whether to animate the background color flash on mutation. |
| `AnimateScale` | `bool` | `true` | Whether to apply the physical scale bump on mutation. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class InventoryItem : MonoBehaviour
{
    [Header("Currencies & Balances")]
    [ValueChangeFlash(FlashColor = "#F59E0B66", ScaleBump = 1.06f, FlashDuration = 450f)]
    public int goldCoins = 2500;

    [ValueChangeFlash(FlashColor = "#8B5CF666", ScaleBump = 1.08f)]
    public int premiumGems = 45;

    [Header("Live Health Monitoring")]
    [ValueChangeFlash(FlashColor = "#EF444466", FlashDuration = 350f)]
    public float currentHealth = 100f;

    [Header("Direct Collections Cascading")]
    [ValueChangeFlash(FlashColor = "#10B98177", FlashDuration = 400f)]
    public float[] elementalResistances = new float[] { 25.0f, 50.0f, 75.0f };

    [ValueChangeFlash(FlashColor = "#38BDF877", FlashDuration = 500f)]
    public List<string> activeQuestLog = new List<string> { "Find ancient relic", "Defeat forest guardian" };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Range]` | Supported | Flashes responsively as the user scrubs the slider control. |
| `[BoxGroup]` | Supported | Fits within group boxes without clipping neighboring controls. |
| `[ClickRipple]` | Supported | Can be combined with click ripples; ripples fire on press while flashes fire on mutation. |

### Collection Cascading Matrix

| Collection / Container Type | Cascading Support | Render Target | Notes |
| :--- | :---: | :--- | :--- |
| `T[]` | ✅ Yes | Individual array elements | Flashes specifically on the edited array element row. |
| `List<T>` | ✅ Yes | Individual list items | Flashes the modified item row without flashing the entire list. |
| `AdvancedList<T>` | ✅ Yes | Individual list rows | Compatible with element add/remove/reorder operations. |
| `SerializableDictionary<K, V>` | ✅ Yes | Dictionary key/value cells | Flashes edited key or value cells. |
| `SerializableNullable<T>` | ✅ Yes | Inner wrapped value | Flashes when nullable payload changes. |
| `SerializableTuple<...>` | ✅ Yes | Tuple member cells | Flashes the individual tuple item altered. |

