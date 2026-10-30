# [AssetOnly]

> Restricts an object reference field to project assets only, preventing scene hierarchy objects from being accidentally assigned.

---

## 1. Overview & Value Proposition

**What it does:**
Restricts Object fields to saved Project window assets (prefabs, materials, audio clips, scriptable objects) and rejects scene instances.

**The Problem:**
In ScriptableObjects and prefab assets, dragging a GameObject from the active Scene hierarchy creates an invalid cross-scene reference. When loading another scene or building the game, these scene references break, turning into `MissingReferenceException` errors.

**The Solution:**
Add `[AssetOnly]` to any object reference field:
- **Scene Reference Block:** Disallows dragging or selecting objects from the active scene hierarchy.
- **Immediate Warning Callout:** Displays an informative warning box when an invalid scene object is dragged into the field.
- **Auto-Clear Protection:** Enable `AutoClear = true` to automatically reject and wipe invalid scene assignments.
- **Collection Support:** Fully validated inside lists, arrays, and serialized dictionaries of assets.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

[CreateAssetMenu(menuName = "Game/Weapon Config")]
public class WeaponConfig : ScriptableObject
{
    [AssetOnly]
    public GameObject weaponPrefab;

    [AssetOnly(AutoClear = true)]
    public AudioClip fireSfx;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any `UnityEngine.Object` reference |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public AssetOnlyAttribute()
```

*This attribute is configured using public object initializer properties.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ShowWarning` | `bool` | `true` | Displays a warning infobox when an invalid scene object is assigned. |
| `AutoClear` | `bool` | `false` | Automatically resets the field to `null` if a scene object is assigned. |
| `WarningMessage` | `string` | `"Assigning Scene Objects is not allowed..."` | Custom error message string displayed on invalid assignment. |
| `ErrorColor` | `string` | `""` | Hex text color for the error callout. |
| `ErrorBackgroundColor` | `string` | `""` | Hex background color for the error callout card. |
| `FontSize` | `int` | `0` | Font size for error callout text (0 uses default). |
| `Padding` | `float` | `0f` | Internal padding in pixels for error callout card. |
| `Margin` | `float` | `5f` | Outer margin in pixels for error callout card. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

[CreateAssetMenu(menuName = "Game/Dungeon Pool")]
public class DungeonPrefabPool : ScriptableObject
{
    [Header("Room Prefabs (Project Assets Only)")]
    [AssetOnly(ShowWarning = true, AutoClear = true)]
    public GameObject bossChamberPrefab;

    [AssetOnly]
    public List<GameObject> commonRoomPrefabs = new List<GameObject>();
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[AssetSelector]` | Recommended | Pairs together to filter the asset picker popup to project assets only. |
| `[PreviewField]` | Supported | Visual preview works cleanly while enforcing project asset constraints. |
| `[BoxGroup]` | Supported | Functions normally inside group layouts. |
