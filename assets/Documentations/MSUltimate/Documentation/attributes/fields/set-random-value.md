# [SetRandomValue]

> Automatically seeds pseudo-random values across numeric ranges, vibrant colors, GUIDs, or member lists upon creation, with an inline 🎲 reroll button.

---

## 1. Overview & Value Proposition

**What it does:**
Automatically initializes serialized fields with randomized values upon creation or reset. Supports numeric ranges, vibrant/pastel colors, alphanumeric strings, GUIDs, enum choices, boolean probabilities, and custom member pools. Includes an inline 🎲 reroll button in the Inspector to generate new variations on click.

**The Problem:**
Placing multiple instances of props or enemies in a level creates repetitive visual uniformity unless designers manually tweak variables like scale offsets, rotation variations, color tints, or starting speeds. Manually randomizing dozens of components one by one is time-consuming and often neglected.

**The Solution:**
Add `[SetRandomValue]` to any serialized field:
- **Rich Randomization Presets:** Built-in presets for `Range`, `Guid`, `Color`, `ColorVibrant`, `ColorPastel`, `Enum`, `Boolean`, `Alphanumeric`, `Vector2`, and `Vector3`.
- **Inline 🎲 Reroll Button:** Click the reroll button directly in the Inspector to test new permutations instantly.
- **Member Source Integration:** Randomly pick items from an existing array, list, or generator method.
- **Creation-Only Safety:** By default, seeds values only on creation or reset (`OnlyOnCreation = true`), preserving existing designer work.
- **Custom Seeds:** Seed reproducibility support via explicit `Seed` or dynamic `SeedMember`.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class ProceduralTreeProp : MonoBehaviour
{
    [SetRandomValue(0.8f, 1.3f)]
    public float scaleVariation = 1.0f;

    [SetRandomValue(RandomPreset.ColorVibrant)]
    public Color leafTint = Color.green;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `int`, `float`, `double`, `string`, `Color`, `bool`, `Enum`, `Vector2`, `Vector3` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public SetRandomValueAttribute()
public SetRandomValueAttribute(RandomPreset preset)
public SetRandomValueAttribute(float min, float max, float step = 0f)
public SetRandomValueAttribute(int min, int max, int step = 1)
public SetRandomValueAttribute(string sourceMember)
public SetRandomValueAttribute(Type staticType, string sourceMember)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `preset` | `RandomPreset` | `RandomPreset.Auto` | Built-in randomization algorithm mode. |
| `min` | `float` / `int` | *(Required)* | Minimum numeric bound or coordinate limit. |
| `max` | `float` / `int` | *(Required)* | Maximum numeric bound or coordinate limit. |
| `step` | `float` / `int` | `0f` / `1` | Increment snap step (`0` = continuous). |
| `sourceMember` | `string` | `null` | Member name providing random value calculation or item collection. |
| `staticType` | `Type` | `null` | Class containing static member generator. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Preset` | `RandomPreset` | `RandomPreset.Auto` | Randomization algorithm mode (`Range`, `Guid`, `Color`, `Vector3`, etc.). |
| `Min` | `double` | `0` | Lower bound for numeric and coordinate randomization. |
| `Max` | `double` | `100` | Upper bound for numeric and coordinate randomization. |
| `Step` | `double` | `0` | Optional snap step increment for numeric values. |
| `Probability` | `float` | `0.5f` | Probability (`0.0` to `1.0`) that a boolean evaluates to `true`. |
| `StringLength` | `int` | `8` | Character length for `Alphanumeric` presets. |
| `Prefix` | `string` | `""` | Optional string prepended to string results. |
| `Suffix` | `string` | `""` | Optional string appended to string results. |
| `Format` | `string` | `""` | Numeric format string (e.g. `"F2"`). |
| `SourceMember` | `string` | `null` | Name of method, field, property, or list to draw random values from. |
| `StaticType` | `Type` | `null` | Type containing static `SourceMember`. |
| `Seed` | `int` | `0` | Explicit random seed (`0` = environment random). |
| `SeedMember` | `string` | `null` | Dynamic member providing integer seed. |
| `Overwrite` | `bool` | `false` | Overwrites existing values upon initialization if true. |
| `OnlyOnCreation` | `bool` | `true` | Only runs auto-assignment on creation/reset. |
| `ShowRerollButton` | `bool` | `true` | Renders inline 🎲 button in Inspector. |
| `ButtonTooltip` | `string` | `"Reroll random value"` | Tooltip displayed on the 🎲 reroll button. |
| `Order` | `int` | `0` | Execution priority in modifier pipeline. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public enum EnemyArchetype { Minion, Brute, Shaman, Assassin }

public class ProceduralEnemySpawn : MonoBehaviour
{
    [Header("Unique Instance Identity")]
    [SetRandomValue(RandomPreset.Guid)]
    public string instanceGuid;

    [Header("Combat Variation")]
    [SetRandomValue(RandomPreset.Enum)]
    public EnemyArchetype enemyClass;

    [SetRandomValue(80f, 150f, step: 5f)]
    public float startingHealth = 100f;

    [SetRandomValue(Probability = 0.25f)]
    public bool isEliteUnit = false;

    [Header("Visual Tinting")]
    [SetRandomValue(RandomPreset.ColorPastel)]
    public Color armorTint;

    [Header("Spawn Position Offset")]
    [SetRandomValue(RandomPreset.Vector3, Min = -5, Max = 5)]
    public Vector3 randomPatrolOffset;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Reroll button sits cleanly within row layouts. |
| `[ReadOnly]` | Supported | Locks manual text/number input while allowing 🎲 reroll clicks. |
| `[ShowIf]` | Supported | Randomizer honors conditional visibility states. |
| `ICollectionElement` | Supported | Randomizes new elements added to lists and arrays with per-cell reroll buttons. |
| `ICollectionBatch` | Supported | Executes batch randomization across all paginated elements on initial load / item addition, and provides a header `🎲` button to reroll the entire collection. |
