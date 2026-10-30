# [Searchable]

> Injects a real-time, interactive search and filter bar into the Inspector for MonoBehaviour and ScriptableObject classes.

---

## 1. Overview & Value Proposition

**What it does:**
Adds a live search and filter bar at the top of your Inspector so you can find any field or property instantly.

**The Problem:**
Large components and balance ScriptableObjects (like character stats, weapon databases, or audio managers) easily grow to 50–100+ fields. Finding one setting—like "jumpHeight" or "reloadTime"—forces you to scroll up and down endlessly through long lists of variables.

**The Solution:**
Add `[Searchable]` right above your MonoBehaviour or ScriptableObject class declaration:
- **Instant Live Filtering:** Type a word, and non-matching fields instantly fade away while matches stay visible.
- **Gold Match Highlighting:** Matching letters are highlighted in gold so your eyes lock onto the property immediately.
- **Auto-Unfolds Groups:** If a matched field is hidden inside a closed foldout or box group, the group automatically opens for you.
- **1-Click Clear:** Click the "✕" button or press Escape to instantly restore the full inspector view.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

[Searchable]
public class MasterGameConfig : MonoBehaviour
{
    public float movementSpeed = 6f;
    public float jumpForce = 12f;
    public int maxPlayerHealth = 100;
    public string serverEndpoint = "https://api.game.com";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Class` |
| **Allow Multiple** | `false` |
| **Inherited** | `true` |
| **Build Overhead** | Editor-only (Zero runtime build overhead / stripped in builds) |
| **Minimum Unity** | Unity 6 (6000.x)+ |

---

## 4. Constructors & Signatures

```csharp
public SearchableAttribute()
```

---

## 5. Properties & Customization Options

### Filtering & Behavior
| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Placeholder` | `string` | `"🔍 Search fields..."` | Watermark text displayed when the search box is empty. |
| `CaseSensitive` | `bool` | `false` | When `true`, matches character casing strictly. |
| `SearchDelay` | `long` | `0` | Debounce delay in milliseconds before filtering fires (`0` for instant). |
| `AnimateFilter` | `bool` | `true` | Smoothly fades and transitions visibility changes during typing. |
| `HighlightMatches` | `bool` | `true` | Highlights matching substring characters in the label. |
| `HighlightColor` | `string` | `"#FFD700"` | Hex color string for search term text highlighting. |
| `NoMatchMessage` | `string` | `"No fields match your search."` | Message banner displayed when query yields zero results. |
| `NoMatchMessageColor` | `string` | `""` | Hex color for the no-match message label. |

### Badges, Buttons & Styling
| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ShowMatchCount` | `bool` | `true` | Displays a match count badge (e.g. `3 / 7`) to the right. |
| `BadgeBackgroundColor` | `string` | `""` | Override hex background color of the match-count badge. |
| `BadgeTextColor` | `string` | `""` | Override hex text color of the match-count badge. |
| `ShowClearButton` | `bool` | `true` | Displays quick clear button inside search bar. |
| `ClearButtonLabel` | `string` | `"✕"` | Label displayed on the clear button. |
| `SearchIcon` | `string` | `"d_Search Icon"` | Unity built-in icon drawn on left of search bar (`""` to disable). |
| `SearchBarHeight` | `float` | `24f` | Total pixel height of the search bar input. |
| `SearchBarBorderRadius` | `float` | `12f` | Corner rounding radius of the search bar for a pill look. |
| `SearchBarBackgroundColor` | `string` | `""` | Override hex background color of the search bar. |
| `SearchBarTextColor` | `string` | `""` | Override hex text color of the search bar. |
| `SearchBarBorderColor` | `string` | `""` | Override hex border color of the search bar. |
| `SearchBarBorderWidth` | `float` | `1f` | Border stroke thickness in pixels. |
| `HeaderLabel` | `string` | `""` | Optional header label shown above search bar. |
| `HeaderFontSize` | `float` | `0f` | Font size for optional header label (`0` for default). |
| `HeaderLabelColor` | `string` | `""` | Hex color for optional header label. |
| `MarginTop` | `float` | `4f` | Top margin in pixels. |
| `MarginBottom` | `float` | `4f` | Bottom margin in pixels. |
| `SearchBarBottomSpacing` | `float` | `6f` | Space in pixels between search bar and first field. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

[CreateAssetMenu(fileName = "GlobalEconomySettings", menuName = "Game/Economy/Global Settings")]
[Searchable(
    Placeholder = "Filter economy parameters...",
    HighlightColor = "#00FFCC",
    ShowMatchCount = true,
    SearchBarBorderRadius = 14f,
    HeaderLabel = "Economy Quick Filter"
)]
public class GlobalEconomySettings : ScriptableObject
{
    [BoxGroup("Player Currencies", Box = true)]
    public int startingGold = 500;
    [BoxGroup("Player Currencies")]
    public int startingGems = 25;

    [BoxGroup("Drop Multipliers", Box = true)]
    public float globalExpMultiplier = 1.0f;
    [BoxGroup("Drop Multipliers")]
    public float globalGoldMultiplier = 1.25f;

    [BoxGroup("Shop Taxes", Box = true)]
    public float auctionHouseTaxPercent = 5.0f;
}
```

---

## 7. Stacking & Compatibility Matrix

- **Class-Level Scope:** Placed directly above the `class` declaration; automatically indexes all serialized fields and groups inside.
- **Group Hierarchy Compatibility:** Respects `[BoxGroup]`, `[TabGroup]`, and `[FoldoutGroup]`. If a nested field matches, its parent container automatically unfolds to display the result.
- **Clear Button:** Clicking "✕" or pressing Escape instantly restores all fields to their default visibility.
