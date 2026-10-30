# [HighlightIfNull]

> Highlights an object reference field with a high-visibility colored border outline when it is null or unassigned.

---

## 1. Overview & Value Proposition

**What it does:**
Applies a crisp colored border outline around object reference fields whenever they are null or unassigned. Unlike large error banners that displace inspector layout, `[HighlightIfNull]` offers clean, zero-vertical-space visual alerting.

**The Problem:**
Large error boxes can clutter compact inspector forms or lists. Yet, missing critical asset references leads to `NullReferenceException` crashes in play mode.

**The Solution:**
Add `[HighlightIfNull]` to any object, component, or class reference:
- **Zero-Footprint Alerting:** Draws a distinct colored outline around the field without expanding or shifting layout heights.
- **Customizable Color:** Pick warning orange, neon cyan, or alert red (`"#FF0000"`).
- **Auto-Clearing:** The highlight automatically vanishes the instant a valid reference is assigned.
- **Collection Elements:** Outlines individual empty slots inside arrays and lists.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class EnemyCombat : MonoBehaviour
{
    [HighlightIfNull("#FF3366")]
    public Transform targetPlayer;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `UnityEngine.Object`, interfaces, reference types/classes |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public HighlightIfNullAttribute(string colorHex = "#FF0000")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `colorHex` | `string` | `"#FF0000"` | Hex color code for the field highlight outline. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ColorHex` | `string` | `"#FF0000"` | Hex color code used for the unassigned outline border. |
| `Order` | `int` | `0` | Execution priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class BossArenaDirector : MonoBehaviour
{
    [Header("Core Dependencies (Must Not Be Null)")]
    [HighlightIfNull("#e74c3c")]
    public GameObject bossPrefab;

    [HighlightIfNull("#f39c12")]
    public Transform spawnPoint;

    [Header("Stage Waypoints Collection")]
    [HighlightIfNull("#e74c3c")]
    public List<Transform> arenaWaypoints = new List<Transform>();
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Border outline renders cleanly inside group cards. |
| `[Required]` | Supported | Can be combined with `[Required]` for both a colored border and an explanatory message. |
| `ICollectionElement` | Supported | Outlines unassigned elements inside collection slots. |
