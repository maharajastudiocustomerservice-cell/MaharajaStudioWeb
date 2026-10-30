# [AdvancedClass]

> Renders serialized structs and classes as sleek, structured inspector cards featuring real-time search, pagination, foldouts, and accent bars.

---

## 1. Overview & Value Proposition

**What it does:**
Transforms plain serialized classes and structs into modern card panels with customizable headers, collapsible foldouts, left accent bars, real-time search filtering, and pagination for massive data structures.

**The Problem:**
In standard Unity, complex serialized structs or nested classes (such as player stats, weapon specs, or AI brain nodes) render as flat, indented blocks. As data structures grow, they clutter the inspector, make finding specific fields difficult, and lack clear visual boundaries between parent and child data.

**The Solution:**
Add `[AdvancedClass]` to any serialized class or struct field:
- **Card Framing & Headers:** Wraps all inner fields within a styled container with custom borders, rounded corners, and headers.
- **Collapsible Foldout:** Toggle collapse/expansion (`IsFoldable`, `StartExpanded`) with field count badges (`ShowFieldCount = true`).
- **Real-Time Search Bar:** Instantly filter inner fields by name with `ShowSearch = true`.
- **Built-In Pagination:** Cleanly paginate massive structures (`ShowPagination = true`, `ItemsPerPage = 10`).
- **Visual Ergonomics:** Left accent bars, alternating row colors, field separators, and custom padding.

---

## 2. Quick Start

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

[Serializable]
public class CharacterStats
{
    public int strength = 18;
    public int agility = 14;
    public int intelligence = 22;
    public float criticalChance = 0.15f;
}

public class HeroEntity : MonoBehaviour
{
    [AdvancedClass(HeaderLabel = "RPG Core Attributes", AccentBarColor = "#3498db", ShowFieldCount = true)]
    public CharacterStats attributes;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field` |
| **Supported Types** | Any serializable `class` or `struct`, or collections (`List<T>`, `T[]`) of serializable classes/structs |
| **Collection Cascading**| Supported via `ICollectionElementAttribute` (`CollectionElementRole.Element \| Value \| NullableValue \| TupleItem`) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public AdvancedClassAttribute()
```

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `IsFoldable` | `bool` | `true` | Allows collapsing the entire class card via a foldout toggle. |
| `ShowHeader` | `bool` | `true` | Draws the top header bar with title and icon. |
| `StartExpanded` | `bool` | `true` | Initial expansion state when inspected. |
| `HeaderLabel` | `string` | `""` | Custom header title (defaults to property name if empty). |
| `HeaderIcon` | `string` | `null` | Built-in Unity icon name displayed before header text. |
| `ShowFieldCount` | `bool` | `false` | Displays a field count pill badge (e.g. `"4 Fields"`). |
| `HeaderFontSize` | `int` | `0` | Header font size override (`0` = default). |
| `HeaderFontStyle` | `FontStyle` | `FontStyle.Bold` | Font style for header text. |
| `AccentBarColor` | `string` | `null` | Hex color code for a vertical accent bar on the left edge. |
| `AccentBarWidth` | `float` | `3f` | Width in pixels of the left accent bar. |
| `BorderWidth` | `float` | `0f` | Border outline width in pixels. |
| `BorderRadius` | `float` | `0f` | Corner radius of the card container. |
| `BorderColor` | `string` | `null` | Hex border color. |
| `BackgroundColor` | `string` | `null` | Hex background fill color for the card body. |
| `HeaderBackgroundColor`| `string`| `null` | Hex background fill color for the header bar. |
| `ShowSearch` | `bool` | `false` | Enables a real-time text filter search bar for child fields. |
| `ShowPagination` | `bool` | `false` | Enables pagination navigation for large structures. |
| `ItemsPerPage` | `int` | `10` | Maximum fields displayed per page when pagination is active. |
| `ShowAlternatingFieldBackgrounds` | `bool` | `false` | Adds subtle zebra-striping to alternating child fields. |
| `ReadOnly` | `bool` | `false` | Locks all child fields against user edits. |
| `Order` | `int` | `0` | Drawing order priority in the inspector pipeline. |

---

## 6. Production-Grade Example

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

[Serializable]
public class BossCombatPhase
{
    public string phaseName = "Phase 1 - Enrage";
    public float triggerHealthPercent = 0.5f;
    public float attackSpeedMultiplier = 1.35f;
    public float damageScalar = 1.5f;
    public GameObject summonPrefab;
    public AudioClip phaseMusicTrack;
}

public class BossController : MonoBehaviour
{
    [AdvancedClass(
        HeaderLabel = "Phase 2 Transition Config",
        HeaderIcon = "d_Prefab Icon",
        AccentBarColor = "#e74c3c",
        ShowFieldCount = true,
        BorderRadius = 6f,
        BorderWidth = 1f,
        BorderColor = "#444444",
        ShowSearch = true
    )]
    public BossCombatPhase enragePhaseConfig;

    [MSSpace(10)]
    [AdvancedClass(
        HeaderLabel = "Encounter Phase List",
        HeaderBackgroundColor = "#1E293B",
        BorderColor = "#3B82F6",
        ShowFieldCount = true
    )]
    [Tooltip("Collection cascading: each BossCombatPhase element card receives full AdvancedClass framing.")]
    public List<BossCombatPhase> allCombatPhases = new List<BossCombatPhase>();
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[ShowIf]` | Supported | Dynamic condition evaluated at the root card level. |
| `[ReadOnly]` | Supported | Internal fields remain editable unless root `ReadOnly = true` or `[ReadOnly]` is stacked. |
| `[BoxGroup]` | Supported | Nests cleanly within multi-level layout containers. |
| Collections (`List<T>`, `T[]`) | Supported | Implements `ICollectionElementAttribute` to automatically cascade card styling, headers, and foldout controls to each element. |
| Inner MSUltimate Attributes | Supported | Child fields inside the class support all MSUltimate drawers (`[MinMaxSlider]`, `[AutoFill]`, etc.). |
