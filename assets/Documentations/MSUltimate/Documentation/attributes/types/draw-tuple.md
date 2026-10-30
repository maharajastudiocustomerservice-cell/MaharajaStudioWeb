# [DrawTuple]

> Customizes the visual presentation of SerializableTuple fields with custom element labels, width ratios, and horizontal or stacked layouts.

---

## 1. Overview & Value Proposition

**What it does:**
Formats multi-value tuple structures (`SerializableTuple<T1, T2>`, etc.) into clean inline horizontal columns or structured stacked rows. Supports custom label captions for each tuple component (e.g. "Key" & "Value" or "Min" & "Max") and explicit width ratio splitting.

**The Problem:**
Standard serialized tuples or multi-field structs take up multiple vertical lines in the Inspector by default with generic names like `Item1`, `Item2`, creating cluttered and unreadable inspectors.

**The Solution:**
Add `[DrawTuple]` to any `SerializableTuple` field:
- **Clean Inline Layout:** Displays tuple items side-by-side in a single unified line.
- **Meaningful Labels:** Replaces `Item1`, `Item2` with domain-specific labels like `"Min", "Max"` or `"Key", "Weight"`.
- **Custom Width Ratios:** Allocate exact space to each item (e.g. `Ratios = new float[] { 0.3f, 0.7f }`).
- **Stacked Mode Option:** Switch to vertical stacking when tuple contents contain complex multi-field objects.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.Types;

public class DropTable : MonoBehaviour
{
    [DrawTuple("Item ID", "Probability Weight", Ratios = new float[] { 0.6f, 0.4f })]
    public SerializableTuple<string, float> lootEntry;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `SerializableTuple<...>`, `List<SerializableTuple<...>>`, `SerializableTuple<...>[]` |
| **Collection Cascading** | Yes (`ICollectionElementAttribute`) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public DrawTupleAttribute(params string[] labels)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `labels` | `params string[]` | `null` | Custom labels for each item in the tuple (e.g. `"Min"`, `"Max"`). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Labels` | `string[]` | `null` | Custom label captions assigned to each tuple element. |
| `Ratios` | `float[]` | `null` | Width distribution ratios for each item (must sum to `1.0`). |
| `Stacked` | `bool` | `false` | If true, stacks tuple items vertically instead of inline horizontally. |
| `Order` | `int` | `0` | Execution priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.Types;

public class DialogueTrigger : MonoBehaviour
{
    [Header("Speaker Mapping (Inline Tuple)")]
    [DrawTuple("Speaker Name", "Audio Clip", Ratios = new float[] { 0.4f, 0.6f })]
    public SerializableTuple<string, AudioClip> dialogueCue;

    [Header("Coordinate Bounds (3-Item Tuple)")]
    [DrawTuple("X", "Y", "Z")]
    public SerializableTuple<float, float, float> coordinateBound;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Inline tuples fit cleanly inside card rows. |
| `[TableList]` | Supported | Integrates inside collection tables for dense data representation. |
| `[ReadOnly]` | Supported | Disables all child fields across the tuple simultaneously. |
| Direct Collections | Supported | Cascades custom labels, column ratios, and stacked cards across `List<SerializableTuple<...>>` and arrays via `ICollectionElementAttribute`. |
