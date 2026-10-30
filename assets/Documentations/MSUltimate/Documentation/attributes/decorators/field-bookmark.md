# [FieldBookmark]

> Pins and bookmarks key serialized fields for instant 1-click navigation in long component inspectors.

---

## 1. Overview & Value Proposition

**What it does:**
Pins a star or bookmark tag to your most important settings so you can jump straight to them without scrolling through hundreds of lines.

**The Problem:**
In massive monolithic game components (like character controllers, inventory managers, or level directors), you frequently need to adjust 2 or 3 specific variables (e.g. "Max Health", "Debug Invincible", or "Spawn Rate"). Hunting for those 3 settings among 60 other fields wastes time.

**The Solution:**
Add `[FieldBookmark]` above your essential properties:
- **Quick Jump Navigation:** Registers the field into the MSUltimate inspector bookmark bar.
- **Custom Bookmark Groups:** Organize favorites into named categories (e.g. `"⭐ Combat Core"`, `"⚡ Live Tuning"`).
- **Visual Star Accent:** Displays a clean gold star icon beside the field row.
- **Zero Runtime Overhead:** Runs purely in the Editor; completely omitted from final game builds.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class PlayerController : MonoBehaviour
{
    [FieldBookmark("⭐ Core Combat")]
    public float baseMovementSpeed = 6f;

    [FieldBookmark("⭐ Core Combat")]
    public int maxHealth = 100;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public FieldBookmarkAttribute(string groupName = "⭐ Favorites")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `groupName` | `string` | `"⭐ Favorites"` | The category tab or section under which this bookmarked field appears. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `GroupName` | `string` | `"⭐ Favorites"` | Target bookmark collection group. |
| `Order` | `int` | `0` | Execution priority relative to other attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class GameDirector : MonoBehaviour
{
    [Header("Core Mission Variables")]
    [FieldBookmark("🎯 Mission Objectives")]
    public string activeObjectiveId = "OBJECTIVE_DEFEND_OUTPOST";

    [FieldBookmark("🎯 Mission Objectives")]
    public float objectiveTimerMinutes = 15f;

    [Header("Tuning Settings")]
    [FieldBookmark("⚙️ Balance Overrides")]
    public float globalEnemySpawnRateMultiplier = 1.0f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Searchable]` | Supported | Bookmarked fields appear at the top of quick search results. |
| `[BoxGroup]` | Supported | Functions normally inside nested box groups. |
| `[GUIColor]` | Supported | Combines with color tints for maximum visual pop. |
