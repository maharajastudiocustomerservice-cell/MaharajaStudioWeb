# [InlineEditor]

> Inlines the full Inspector editor of assigned ScriptableObjects, Materials, or Components directly beneath the reference field.

---

## 1. Overview & Value Proposition

**What it does:**
Embeds the complete inspector GUI of referenced assets or components directly inside the current object's inspector, eliminating the need to click away.

**The Problem:**
In standard Unity, editing a referenced ScriptableObject (such as an item definition or weapon config) requires selecting the asset in the Project window or locking inspectors. Designers constantly lose their place jumping back and forth between prefabs and asset databases.

**The Solution:**
Add `[InlineEditor]` to any object reference field:
- **Zero Inspector Switching:** View and edit ScriptableObjects, Materials, and Components inline in place.
- **Collapsible Card Frame:** Expand or collapse the embedded editor with an integrated foldout header.
- **Scrollable Height Control:** Set `MaxHeight` with scrollbars for complex nested assets to prevent overly long inspectors.
- **Custom Header Styling:** Personalize banner background colors, text colors, borders, and margins.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class PlayerInventory : MonoBehaviour
{
    [InlineEditor]
    public WeaponData primaryWeapon;

    [InlineEditor(DrawHeader = true, DefaultExpanded = false, MaxHeight = 220f)]
    public Material armorMaterial;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `ScriptableObject`, `Material`, `Component`, and any `UnityEngine.Object` (including `T[]` and `List<T>`) |
| **Collection Cascading** | Supported (`ICollectionElementAttribute`) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public InlineEditorAttribute()
```

*This attribute is configured using public object initializer properties.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `DrawHeader` | `bool` | `true` | Displays collapsible foldout banner header above the embedded editor. |
| `DefaultExpanded` | `bool` | `true` | Whether the inline editor starts expanded by default. |
| `HideObjectField` | `bool` | `false` | Conceals the object reference picker, drawing only the inline editor. |
| `HideScriptField` | `bool` | `true` | Conceals the default `Script` reference field inside the embedded editor. |
| `MaxHeight` | `float` | `0f` | Maximum scrollable height in pixels (`0f` means unlimited height). |
| `HeaderBackgroundColor` | `string` | `null` | Hex color string for the header banner background. |
| `HeaderTextColor` | `string` | `null` | Hex color string for the header title label. |
| `BorderColor` | `string` | `null` | Hex outline border color for the embedded card container. |
| `BorderWidth` | `float` | `1f` | Border outline line thickness in pixels. |
| `BorderRadius` | `float` | `3f` | Corner rounding radius in pixels. |
| `Padding` | `float` | `5f` | Internal padding in pixels within the card. |
| `MarginTop` | `float` | `4f` | Top margin spacing in pixels. |
| `MarginBottom` | `float` | `4f` | Bottom margin spacing in pixels. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class EnemySpawner : MonoBehaviour
{
    [Header("Enemy Definition")]
    [InlineEditor(DefaultExpanded = true, HeaderBackgroundColor = "#2c3e50", BorderColor = "#3498db")]
    public EnemyProfile enemyProfileAsset;

    [Header("Visual Effects Profile")]
    [InlineEditor(MaxHeight = 180f, HideScriptField = true)]
    public Material spawnVfxMaterial;

    [Header("Direct Collections Cascading")]
    [InlineEditor(DrawHeader = true, DefaultExpanded = false, BorderColor = "#3B82F6")]
    public Material[] characterMaterialLayers;

    [InlineEditor(DrawHeader = true, DefaultExpanded = false)]
    public List<ScriptableObject> waveLootProfiles;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `Collections (T[], List<T>)` | Supported | Directly cascades embedded inline inspectors to each item slot without wrapper classes (`ICollectionElementAttribute`). |
| `[BoxGroup]` | Supported | Nests cleanly inside box groups, tabs, and foldouts. |
| `[AssetOnly]` | Recommended | Ensure only saved project assets are assigned to prevent scene object leaks. |
| `[ShowIf]` | Supported | Shows or hides the entire embedded editor dynamically based on conditions. |
