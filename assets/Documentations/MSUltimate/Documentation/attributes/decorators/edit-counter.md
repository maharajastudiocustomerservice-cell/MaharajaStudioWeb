# [EditCounter]

> Tracks and displays the total number of times a field has been edited during the current Editor session or across project saves.

---

## 1. Overview & Value Proposition

**What it does:**
Displays a small counter badge (e.g. `✏️ 14`) next to a field showing how many times it was modified.

**The Problem:**
During level design and balancing passes, team leads and technical artists want to know which game variables are being modified frequently and which ones remain untouched defaults. Unity provides zero per-property edit telemetry out of the box.

**The Solution:**
Add `[EditCounter]` next to any property:
- **Automatic Modification Tally:** Increments a clean visual counter whenever the field's value changes.
- **Session vs Persistent:** Track modifications during the active Editor session or persist counts across domain reloads (`persistent: true`).
- **QA & Balancing Insight:** Identify "hot" variables that are undergoing heavy tuning versus neglected stats.
- **Stylized Indicator Badge:** Styled with custom color accents and tooltip stats.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class BalanceTuning : MonoBehaviour
{
    [EditCounter(colorHex: "#3498DB")]
    public float enemyMovementSpeed = 4.5f;
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
public EditCounterAttribute(string colorHex = "#95a5a6", bool persistent = false)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `colorHex` | `string` | `"#95a5a6"` | Hex color string for the counter pill badge. |
| `persistent` | `bool` | `false` | When true, stores edit counts across domain reloads and Unity restarts. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ColorHex` | `string` | `"#95a5a6"` | Pill background accent color. |
| `Persistent` | `bool` | `false` | Saves edit counts into EditorPrefs for long-term telemetry. |
| `Order` | `int` | `0` | Execution priority relative to other attributes. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CombatTuningRig : MonoBehaviour
{
    [BoxGroup("Heavily Balanced Parameters", Box = true)]
    [EditCounter(colorHex: "#E67E22", persistent: true)]
    public float heavyAttackDamage = 120f;

    [EditCounter(colorHex: "#9B59B6")]
    public float parryWindowDurationSeconds = 0.2f;

    [BoxGroup("Damage Multipliers", Box = true)]
    [InfoBox("Direct collection cascading via ICollectionElementAttribute.")]
    [EditCounter("#10B981")]
    public List<float> enemyWaveTimings = new List<float> { 15f, 30f, 45f, 60f };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[DeltaTracker]` | Supported | Pair together for full change insights (magnitude + frequency). |
| `[FieldTimestamp]` | Supported | Pair to record both edit count and the exact time of the last modification. |
| `[BoxGroup]` | Supported | Functions normally inside group containers. |

### Collection Cascading Matrix

| Collection / Container Type | Cascading Support | Render Target | Notes |
| :--- | :---: | :--- | :--- |
| `float[]` | ✅ Yes | Individual array items | Tracks modifications per array element row. |
| `List<T>` | ✅ Yes | Individual list items | Renders dedicated edit counter badge per row. |
| `AdvancedList<T>` | ✅ Yes | Individual list elements | Supports animated drag, reordering, and independent counting. |
| `SerializableDictionary<K, V>` | ✅ Yes | Dictionary value column | Tracks value modifications per dictionary entry. |
| `SerializableNullable<T>` | ✅ Yes | Inner value element | Tracks edits to wrapped value. |
| `SerializableTuple<...>` | ✅ Yes | Tuple member fields | Displays edit counter badge within tuple column. |

