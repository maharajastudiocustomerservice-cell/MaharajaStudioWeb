# [ManageableAsset]

> Registers ScriptableObject classes directly into the MSUltimate Asset Manager Window for centralized cataloging, filtering, and 1-click instantiation.

---

## 1. Overview & Value Proposition

**What it does:**
Decorates a `ScriptableObject` class to register it as an indexed asset catalog entry in the MSUltimate Asset Manager. Once tagged, designers and programmers can browse, filter, inspect, and instantiate instances of this asset type through a single unified project-wide manager window.

**The Problem:**
In mid-to-large Unity projects, ScriptableObjects become scattered across deeply nested folders (`Assets/GameData/Items/Weapons/...`). Locating existing data assets requires tedious navigation in the Project window, and remembering their `[CreateAssetMenu]` path causes friction for team members creating new balance configs or quest definitions.

**The Solution:**
Add `[ManageableAsset]` to any `ScriptableObject` class definition:
- **Centralized Hub:** Automatically gathers all project instances of this ScriptableObject into the Asset Manager Window (`Tools > Maharaja Studio > MSUltimate > Windows > Asset Manager`).
- **Categorized Menu Tree:** Groups types hierarchically (e.g. `"Inventory/Weapons"`, `"Dialogue/Quests"`).
- **1-Click Creation & Renaming:** Fast creation with predefined template names and folder targets without right-clicking menus.
- **Visual Branding:** Custom icons and descriptions display directly in the Asset Manager registry.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

[ManageableAsset("Combat/Weapons", Icon = "d_CustomTool", DefaultFileName = "New_Weapon_Config")]
[CreateAssetMenu(fileName = "NewWeapon", menuName = "Combat/Weapon Data")]
public class WeaponData : ScriptableObject
{
    public string weaponName = "Excalibur";
    public float baseDamage = 45f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Class` (Decorates `ScriptableObject` definitions) |
| **Supported Types** | Subclasses of `UnityEngine.ScriptableObject` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | No (`Inherited = false`) |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ManageableAssetAttribute(string menuPath)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `menuPath` | `string` | *(Required)* | Hierarchy category path inside the Asset Manager (e.g. `"Audio/Soundtracks"`). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MenuPath` | `string` | *(Set in constructor)* | Virtual category path used to organize the asset in the catalog tree. |
| `Icon` | `string` | `null` | Unity Editor built-in icon identifier (e.g. `"d_ScriptableObject Icon"`). |
| `DefaultFileName` | `string` | `"New Asset"` | Suggested default file name when creating new asset instances. |
| `Description` | `string` | `null` | Descriptive summary displayed in the Asset Manager header panel. |
| `Order` | `int` | `0` | Execution priority relative to other modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

[ManageableAsset(
    menuPath: "GameDatabase/Loot/Armor",
    Icon = "d_Prefab Icon",
    DefaultFileName = "Armor_Config",
    Description = "Defines defensive equipment attributes, resistance ratings, and equipment slot tags."
)]
[CreateAssetMenu(fileName = "ArmorConfig", menuName = "Loot/Armor Config")]
public class ArmorItemData : ScriptableObject
{
    [Header("Item Identification")]
    public string itemId = "ARM_IRON_CHEST";
    public string displayName = "Iron Breastplate";

    [Header("Defense Attributes")]
    [Range(0, 100)]
    public int armorRating = 35;
    public float weightKg = 18.5f;

    [Header("Durability")]
    public float maxDurability = 250f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[CreateAssetMenu]` | Recommended | Pairs seamlessly with native Unity Asset creation menus. |
| `[BoxGroup]` | Supported | Asset inspector within the Asset Manager respects all internal group layouts. |
| `[Searchable]` | Supported | Fields inside the managed asset remain fully searchable in manager panes. |
| `[CustomInspectorWindow]` | Supported | Functions as an integrated data source for custom inspector workbenches. |
