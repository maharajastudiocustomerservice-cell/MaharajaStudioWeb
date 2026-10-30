# [HierarchyTooltip]

> Displays a rich hover tooltip over the GameObject row, showing optional notes, category, author, status, and components.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyTooltip]` displays a comprehensive metadata tooltip window when hovering over the GameObject's row in the Unity Hierarchy window. Driven by `HierarchyTooltipRenderer`, it composes multi-line documentation including category tags (`Category`), developer notes (`Tooltip`), author attribution (`Author`), active/inactive status (`ShowActiveState`), and an automatic attached component summary (`ShowComponentSummary`).

**The Problem:**
In team environments with multiple level designers, technical artists, and programmers, inspecting unfamiliar GameObjects requires selecting them, scrolling through the Inspector, and deciphering which components are attached and what purpose the object serves. Standard Unity provides no tooltip mechanism on hierarchy rows.

**The Solution:**
Decorating components with `[HierarchyTooltip]`:
- **Instant On-Hover Documentation:** Hovering reveals developer notes without selecting or deselecting the active scene context.
- **Component Stack Inspection:** Enabling `ShowComponentSummary = true` dynamically discovers and lists all attached non-Transform components (`Components (4): MeshFilter, MeshRenderer, BoxCollider, AudioSource`).
- **Team Attribution & Categorization:** Displays who created or owns the subsystem (`Author = "Soutick"`) and which department it belongs to (`Category = "Gameplay / AI"`).
- **Flexible Overload Constructors:** Set simple tooltip strings directly (`[HierarchyTooltip("Main cinematic camera rig")]`) or configure advanced metadata properties.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyTooltip("Handles scene streaming and level boundary transitions.")]
public class LevelStreamingController : MonoBehaviour
{
    public string targetSceneName = "Zone_02";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class` \| `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyTooltipRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyTooltipAttribute()
public HierarchyTooltipAttribute(string tooltip)
```

- **`tooltip`** (`string`): Description text displayed in the hover tooltip window.
- Parameterless constructor allows constructing empty tooltips configured via named object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Tooltip` | `string` | `""` | Main description or usage notes displayed in the tooltip body. |
| `Author` | `string` | `""` | Author, owner, or team discipline attribution tag (e.g. `"Author: Soutick"`). |
| `Category` | `string` | `""` | High-level category grouping header displayed as `"[Category]"`. |
| `ShowComponentSummary` | `bool` | `false` | Whether to automatically inspect and list attached non-Transform components. |
| `ShowActiveState` | `bool` | `false` | Whether to display GameObject active/inactive status in the tooltip. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the hover tooltip remains accessible during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row decorations. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyTooltip(
    "Spawns elite enemy waves when player enters trigger volume.",
    Category = "Combat / Encounter",
    Author = "DesignTeam",
    ShowComponentSummary = true,
    ShowActiveState = true)]
public class CombatWaveTrigger : MonoBehaviour
{
    [Header("Encounter Spawning")]
    public GameObject eliteEnemyPrefab;
    public int waveCount = 3;
    public float waveSpawnDelay = 4.0f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyTextColor]`** | High | Universal companion: colorize the visible hierarchy row and attach deep documentation via tooltip. |
| **`[HierarchyIcon]`** | High | Display visual component icons on the row and full component summaries on hover. |
| **`[HierarchyFolder]`** | High | Document virtual folder usage policies and scene organization guidelines. |
| **`[HierarchyBookmark]`** | High | Pair bookmark ribbon landmarks with instant ownership notes and descriptions. |
