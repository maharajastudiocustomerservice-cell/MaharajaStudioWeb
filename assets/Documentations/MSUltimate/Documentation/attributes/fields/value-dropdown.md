# [ValueDropdown]

> Populates dropdown menus dynamically from C# methods, properties, lists, or ValueDropdownList&lt;T&gt; with custom labels and values.

---

## 1. Overview & Value Proposition

**What it does:**
Transforms standard serialized fields (strings, ints, floats, objects, or structs) into a rich dropdown menu populated dynamically from a C# method, property, or collection member that returns an `IEnumerable`. Supports custom display labels via `ValueDropdownList<T>`.

**The Problem:**
Game configuration often depends on data created elsewhere in code—such as audio bus names loaded from an audio manager, spawn node identifiers declared across a scene, or items queried from a database. Without a dynamic dropdown, designers must memorize and manually type strings or IDs, causing frequent runtime errors.

**The Solution:**
Add `[ValueDropdown("MyValuesGetter")]` to any field:
- **Dynamic Member Sourcing:** Pulls options directly from methods, properties, or fields returning `IEnumerable`, arrays, or lists.
- **Label-Value Decoupling:** Use `ValueDropdownList<T>` to display friendly designer labels (`"Sword of Destiny (Tier 5)"`) while storing exact underlying values (`"item_swd_005"`).
- **Alphabetical Sorting:** Toggle automatic alphabetical sorting via `SortItems = true`.
- **Optional Empty State:** Enable `AllowEmpty = true` to provide a default `(None)` option.

---

## 2. Quick Start

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class AudioEmitter : MonoBehaviour
{
    [ValueDropdown(nameof(GetAvailableAudioBuses))]
    public string outputAudioBus = "Master/SFX";

    private IEnumerable<string> GetAvailableAudioBuses()
    {
        return new string[] { "Master/Music", "Master/SFX", "Master/Voice", "Master/UI" };
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable type (`string`, `int`, `float`, `Object`, etc.) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ValueDropdownAttribute(string valuesGetter = null)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `valuesGetter` | `string` | `null` | Name of method, property, or field returning an `IEnumerable` of options. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ValuesGetter` | `string` | `null` | Name of member providing the collection of choices. |
| `CustomLabel` | `string` | `null` | Custom field display label override. |
| `SortItems` | `bool` | `false` | If `true`, sorts options alphabetically in the dropdown. |
| `AllowEmpty` | `bool` | `false` | If `true`, includes a default `(None)` initial option. |
| `DropdownWidth` | `float` | `0f` | Explicit dropdown width in pixels (`0` = full inspector width). |
| `DropdownHeight`| `float` | `0f` | Explicit dropdown popup height in pixels (`0` = auto). |
| `TextColor` | `string` | `null` | Hex text color for the dropdown selection. |
| `LabelColor` | `string` | `null` | Hex text color for the field label. |
| `BackgroundColor`| `string`| `null` | Hex background color for the dropdown control. |
| `Order` | `int` | `0` | Drawing order priority in the inspector pipeline. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class LootDropChest : MonoBehaviour
{
    [Header("Item Reward (Decoupled Label & ID)")]
    [ValueDropdown(nameof(GetWeaponCatalog), SortItems = true, AllowEmpty = true)]
    public string awardedWeaponId = "wpn_iron_sword";

    [Header("Difficulty Multiplier")]
    [ValueDropdown(nameof(GetDifficultyScalars))]
    public float damageScalar = 1.0f;

    private ValueDropdownList<string> GetWeaponCatalog()
    {
        return new ValueDropdownList<string>
        {
            { "Rusty Dagger (Tier 1)", "wpn_rusty_dagger" },
            { "Iron Broadsword (Tier 2)", "wpn_iron_sword" },
            { "Mithril Greatsword (Tier 3)", "wpn_mithril_greatsword" },
            { "Dragon Slayer (Legendary)", "wpn_dragon_slayer" }
        };
    }

    private static float[] GetDifficultyScalars()
    {
        return new float[] { 0.5f, 1.0f, 1.5f, 2.0f, 3.5f };
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Dropdown fits cleanly inside groups and layout cards. |
| `[ShowIf]` | Supported | Dynamically evaluates member options when field visibility activates. |
| `[ReadOnly]` | Supported | Locks dropdown interaction while displaying currently assigned value. |
| `ICollectionElement` | Supported | Usable inside `List<T>` to create lists of dropdown-selected items. |
