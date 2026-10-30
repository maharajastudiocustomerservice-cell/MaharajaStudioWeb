# [FieldTimestamp]

> Displays the last modified timestamp beside a field to track when inspector values were edited.

---

## 1. Overview & Value Proposition

**What it does:**
Shows an automatic timestamp badge (like `2m ago` or `14:32:05`) right next to a field whenever its value changes in the Inspector.

**The Problem:**
During tuning sessions, game designers tweak dozens of numbers across prefabs. When testing builds, team members often ask: "Did anyone change the boss speed?", "When was this balance tweaked?", or "Are we still using default values from yesterday?" Unity provides zero edit timestamp tracking.

**The Solution:**
Add `[FieldTimestamp]` to any field:
- **Instant Audit Trail:** See immediately when a serialized variable was last modified right in the Inspector.
- **Relative or Absolute Display:** Choose between friendly relative time (e.g. `Just now`, `5m ago`, `2d ago`) or exact calendar timestamps.
- **Custom Tint:** Customize badge hex color to match your studio styling or indicate sensitive balance fields.
- **Zero Runtime Overhead:** Timestamp tracking runs strictly within the Editor GUI layer with no performance impact during gameplay builds.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CombatBalance : MonoBehaviour
{
    [FieldTimestamp]
    public float baseDamage = 45f;

    [FieldTimestamp(colorHex: "#e67e22", showRelative: false)]
    public float criticalMultiplier = 1.75f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **Interfaces** | `ICollectionElementAttribute` |
| **UI Toolkit Compatible** | Yes |

### Collection Cascading Behavior

| Target Placement | Cascades to Elements? | Behavior / Notes |
| :--- | :---: | :--- |
| `List<T>`, `T[]` (Default) | No | Tracks modifications to the collection container as a whole. |
| `List<T>`, `T[]` (`ApplyToElements = true`) | **Yes** | Displays individual last-edited timestamp badges on each element row. |
| `SerializableDictionary<K, V>` | Opt-In | Can cascade to key/value rows when `ApplyToElements = true`. |

---

## 4. Constructors & Parameters

```csharp
public FieldTimestampAttribute(string colorHex = "#7f8c8d", bool showRelative = true)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `colorHex` | `string` | `"#7f8c8d"` | Hex text color for the timestamp label badge. |
| `showRelative` | `bool` | `true` | If `true`, displays relative time (e.g. `5m ago`); otherwise shows full date and time. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ColorHex` | `string` | `"#7f8c8d"` | Hex text color for the timestamp label. |
| `ShowRelative` | `bool` | `true` | Toggles between relative time format and absolute time string. |
| `ApplyToElements` | `bool` | `false` | When `true`, cascades timestamp tracking down to individual collection element rows. |
| `Order` | `int` | `100` | Execution rendering order for UI Toolkit decorator passes. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class RaidBossTuning : MonoBehaviour
{
    [Header("Phase 1 Mechanics")]
    [FieldTimestamp(colorHex: "#2ecc71")]
    public float enrageTimerSeconds = 300f;

    [FieldTimestamp(colorHex: "#e74c3c", showRelative: true)]
    public float swipeCleaveRadius = 8.5f;

    [Header("Phase 2 Overdrive")]
    [FieldTimestamp(showRelative: false)]
    public int summonWaveCount = 4;

    [Header("Live Balance Updates")]
    [FieldTimestamp("#38BDF8", showRelative: true, ApplyToElements = true)]
    public List<string> mechanicPatchNotes = new List<string> { "Nerfed swipe radius", "Delayed phase transition" };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[EditCounter]` | Supported | Pair together to track both *how many times* and *when* a property was changed. |
| `[BoxGroup]` | Supported | Renders neatly inside box groups and tab containers. |
| `[SuffixLabel]` | Supported | Coexists with suffix measurement units. |
| Collections (`List<T>`, `T[]`) | Supported | Tracks container by default; opt-in element cascading via `ApplyToElements = true`. |

