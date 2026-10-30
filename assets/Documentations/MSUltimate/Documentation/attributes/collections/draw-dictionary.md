# [DrawDictionary]

> Customizes the visual presentation of SerializableDictionary fields with side-by-side key-value columns, duplicate validation, and column ratio sliders.

---

## 1. Overview & Value Proposition

**What it does:**
Renders dictionary key-value pairs side-by-side in a clean 2-column table with duplicate prevention and search.

**The Problem:**
Unity cannot serialize native `System.Collections.Generic.Dictionary<K, V>` in the Inspector. When using serializable dictionaries or custom key-value structs, Unity draws them as nested, clunky lists where the key and value are stacked vertically, making inspecting paired game data like item prices or localized text painful.

**The Solution:**
Add `[DrawDictionary]` above any `SerializableDictionary` field:
- **Clean Side-by-Side Columns:** View keys and values neatly aligned in split columns.
- **Adjustable Split Ratio:** Customize column width ratios (e.g. 30% Key / 70% Value) for long descriptions or wide inputs.
- **Duplicate Key Guard:** Automatically detects duplicate keys and displays a warning before serialization errors occur.
- **Sorting & Filtering:** Sort alphabetically by key or filter items with the built-in search bar.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.Runtime.Collections;

public class ShopPrices : MonoBehaviour
{
    [DrawDictionary(KeyLabel = "Item ID", ValueLabel = "Price (Gold)", KeyColumnRatio = 0.4f)]
    public SerializableDictionary<string, int> itemPrices = new SerializableDictionary<string, int>();
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `SerializableDictionary<TKey, TValue>`, custom key-value collection structs |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public DrawDictionaryAttribute()
```

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `KeyLabel` | `string` | `"Key"` | Column header text for the key column. |
| `ValueLabel` | `string` | `"Value"` | Column header text for the value column. |
| `KeyColumnRatio` | `float` | `0.5f` | Percentage ratio of the key column width relative to total width (`0.1f` to `0.9f`). |
| `KeyWidth` | `float` | `0f` | Explicit pixel width for the key column (`0` = use ratio). |
| `ShowSort` | `bool` | `true` | Enables 1-click A-Z / Z-A sorting by key. |
| `AllowDuplicateKeysInEditor` | `bool` | `false` | Whether duplicate keys in the inspector suppress errors or show inline warnings. |
| `ShowSearch` | `bool` | `true` | Enables real-time keyword search across keys and values. |
| `ShowPagination` | `bool` | `false` | Splits dictionary entries into pages for massive datasets. |
| `ItemsPerPage` | `int` | `15` | Maximum key-value pairs displayed per page. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.Runtime.Collections;

public class LocalizationDatabase : MonoBehaviour
{
    [Header("Localized Audio Dialogues")]
    [DrawDictionary(
        KeyLabel = "Voice Line Code",
        ValueLabel = "Audio Clip Asset",
        KeyColumnRatio = 0.35f,
        ShowSort = true,
        ShowSearch = true,
        HeaderBackgroundColor = "#1E272E"
    )]
    public SerializableDictionary<string, AudioClip> dialogueClips = new SerializableDictionary<string, AudioClip>();
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Nests cleanly inside box containers and collapsible groups. |
| `[ShowIf]` | Supported | Toggle dictionary visibility dynamically. |
| `[Searchable]` | Supported | Inherits parent container search capabilities. |
