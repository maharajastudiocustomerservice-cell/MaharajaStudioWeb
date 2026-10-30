# [AssetSelector]

> Adds a searchable popup picker to an Object reference field, filtering matching project assets with previews and path scoping.

---

## 1. Overview & Value Proposition

**What it does:**
Replaces Unity's slow, cluttered object picker window with an instant, searchable popup list scoped to specific folders and filters.

**The Problem:**
Unity's built-in Object Picker window is notoriously cumbersome: it searches the entire project including packages and temporary caches, displays thousands of irrelevant assets, and cannot be scoped to specific sub-folders like `Assets/Game/Audio/SFX`.

**The Solution:**
Add `[AssetSelector]` to any object field:
- **Instant Search Bar:** Filter thousands of assets instantaneously with real-time text search.
- **Folder Scoping:** Scope searches strictly to assigned paths (e.g. `SearchPaths = new[] { "Assets/Weapons" }`).
- **Thumbnail Previews:** Shows visual asset preview icons directly inside the popup list.
- **Custom Button Styling:** Customize search button colors, icons, borders, and margins.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class WeaponLoader : MonoBehaviour
{
    [AssetSelector(SearchPaths = new[] { "Assets/Game/Prefabs/Weapons" })]
    public GameObject equippedWeaponPrefab;

    [AssetSelector(Filter = "t:AudioClip")]
    public AudioClip attackSound;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any `UnityEngine.Object` reference (including `T[]` and `List<T>`) |
| **Collection Cascading** | Supported (`ICollectionElementAttribute`) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public AssetSelectorAttribute()
```

*This attribute is configured using public object initializer properties.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ShowSearchField` | `bool` | `true` | Displays search text input field at the top of the popup. |
| `SearchPaths` | `string[]` | `null` | Folder path array used to scope asset search results. |
| `ShowPreview` | `bool` | `true` | Renders thumbnail preview icons beside found assets. |
| `Filter` | `string` | `null` | Asset search filter (e.g. `"t:Material"`, `"l:Boss"`). |
| `CustomIcon` | `string` | `"d_search_icon"` | Unity icon name for the selector search button. |
| `ButtonColor` | `string` | `""` | Hex background color for the selector button. |
| `TextColor` | `string` | `""` | Hex text color for the button. |
| `BorderColor` | `string` | `""` | Hex border outline color. |
| `BorderWidth` | `float` | `1f` | Border outline line thickness in pixels. |
| `BorderRadius` | `float` | `3f` | Corner rounding radius in pixels. |
| `Height` | `float` | `22f` | Dropdown button height in pixels. |
| `Padding` | `float` | `4f` | Button internal padding in pixels. |
| `MarginLeft` | `float` | `2f` | Left margin spacing in pixels. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class AudioEventManager : MonoBehaviour
{
    [Header("Impact Sound Effects")]
    [AssetSelector(SearchPaths = new[] { "Assets/Audio/SFX/Combat" }, Filter = "t:AudioClip", ShowPreview = true)]
    public AudioClip swordClashClip;

    [Header("Environment Ambience")]
    [AssetSelector(SearchPaths = new[] { "Assets/Audio/Ambience" })]
    public AudioClip windAmbienceClip;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `Collections (T[], List<T>)` | Supported | Automatically cascades searchable picker buttons to each item row in `AudioClip[]`, `List<GameObject>`, etc. (`ICollectionElementAttribute`). |
| `[AssetOnly]` | Recommended | Pairs together to ensure only project assets from the scoped folders are valid. |
| `[PreviewField]` | Supported | Selected asset can still be rendered with a preview card. |
| `[BoxGroup]` | Supported | Functions normally inside group layouts. |
