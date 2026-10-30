# [FieldCooldown]

> Enforces a temporary cooldown lock on a field after its value is modified, displaying an animated countdown overlay.

---

## 1. Overview & Value Proposition

**What it does:**
Overlays an animated cooldown timer gauge directly on a property to lock rapid edits and visualize ability recharge times in the Inspector.

**The Problem:**
Entering raw floating-point numbers (like `3.75s`) for ability cooldowns gives no sense of gameplay rhythm. In addition, rapid repetitive modifications to expensive serialized properties can trigger costly recalculations.

**The Solution:**
Add `[FieldCooldown]` to numeric properties:
- **Simulate Cooldowns in Edit Mode:** Prevents rapid repetitive edits to expensive settings with an animated cooldown lock.
- **Radial & Linear Visualizers:** Displays an animated countdown overlay or progress bar fill.
- **Custom Color & Message:** Style the cooldown gauge with custom hex accents and "Please wait..." status notes.
- **Accurate Real-Time Feedback:** Fine-tune combat cooldowns without building or launching Play Mode.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class MagicSpell : MonoBehaviour
{
    [FieldCooldown(cooldownSeconds: 3.5f, colorHex: "#9B59B6", message: "Channeling spell...")]
    public float spellCooldownSeconds = 3.5f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property, `T[]`, `List<T>`, `AdvancedList<T>`, `SerializableDictionary<K, V>` |
| **Collection Interface** | `ICollectionElementAttribute` (Automatic Element Cascading) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public FieldCooldownAttribute(float cooldownSeconds = 2f, string colorHex = "#e67e22", string message = "Please wait...")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `cooldownSeconds` | `float` | `2f` | Duration in seconds for the field lock cooldown. |
| `colorHex` | `string` | `"#e67e22"` | Hex color for the cooldown progress bar and message text. |
| `message` | `string` | `"Please wait..."` | Status message displayed while the cooldown is active. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `CooldownSeconds` | `float` | `2f` | Duration in seconds for the cooldown lock. |
| `ColorHex` | `string` | `"#e67e22"` | Progress fill color. |
| `Message` | `string` | `"Please wait..."` | Dynamic cooldown status message. |
| `Order` | `int` | `0` | Execution priority relative to other attributes. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class UltimateAbility : MonoBehaviour
{
    [BoxGroup("Ultimate Skill", Box = true)]
    public string abilityName = "Meteor Strike";

    [FieldCooldown(cooldownSeconds: 5f, colorHex: "#E74C3C", message: "Recalculating burst...")]
    [Range(5f, 120f)]
    public float rechargeDurationSeconds = 45f;

    [BoxGroup("Procedural Seeds Buffer", Box = true)]
    [InfoBox("Direct collection cascading via ICollectionElementAttribute.")]
    [FieldCooldown(2.0f, "#10B981", "Baking chunk data...")]
    public List<int> chunkSeedBuffer = new List<int> { 1001, 1002, 1003, 1004 };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Range]` | Supported | Functions cleanly alongside numeric sliders. |
| `[BoxGroup]` | Supported | Nests cleanly inside ability layout containers. |
| `[SuffixLabel]` | Supported | Can be paired with unit tags like `"seconds"`. |

### Collection Cascading Matrix

| Collection / Container Type | Cascading Support | Render Target | Notes |
| :--- | :---: | :--- | :--- |
| `float[]` | ✅ Yes | Individual array items | Throttles edits on individual array elements. |
| `List<T>` | ✅ Yes | Individual list items | Renders animated cooldown overlay on modified list rows. |
| `AdvancedList<T>` | ✅ Yes | Individual list elements | Supports animated drag, reordering, and element-level locks. |
| `SerializableDictionary<K, V>` | ✅ Yes | Dictionary value column | Locks value entries during recalculation cooldown. |
| `SerializableNullable<T>` | ✅ Yes | Inner value element | Applies cooldown overlay to wrapped value. |
| `SerializableTuple<...>` | ✅ Yes | Tuple member fields | Displays cooldown bar within tuple columns. |

