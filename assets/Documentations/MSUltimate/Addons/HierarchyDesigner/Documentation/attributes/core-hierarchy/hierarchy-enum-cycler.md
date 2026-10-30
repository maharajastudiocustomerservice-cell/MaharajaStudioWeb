# [HierarchyEnumCycler]

> Displays an enum field as an interactive badge on the hierarchy row that cycles through enum values on click with full Undo support.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyEnumCycler]` equips hierarchy rows with a rapid one-click enum state cycler. Applied to an enum field, `HierarchyEnumCyclerRenderer` renders the current enum value inside an interactive badge pill (`BadgeColor = "#1E3A5F"`, `TextColor = "#64B5F6"`). Left-clicking the badge advances the field to the next enum entry, while right-clicking cycles in reverse (`RightClickReverse = true`, `WrapAround = true`). Changes register full Undo operations in Edit Mode and update instant state in Play Mode.

**The Problem:**
Switching states—such as AI combat behaviors (Idle, Patrol, Alert, Combat), team affiliations (Red, Blue, Neutral), or lighting modes—requires selecting each entity, locating the enum dropdown in the Inspector, and clicking through a menu. Toggling states across several dozen entities is slow and tedious.

**The Solution:**
Decorating enum state fields with `[HierarchyEnumCycler]`:
- **Single-Click Value Cycling:** Step through enum modes instantly with a single mouse click directly in the hierarchy.
- **Bi-Directional Navigation:** Left-click steps forward; right-click steps backward through enum values.
- **Continuous Wrapping:** Loops automatically from the last enum value back to the first (`WrapAround = true`).
- **Complete Undo Integration:** Every click creates a registered Undo step in Edit Mode, allowing effortless batch rollbacks.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public enum AIState { Idle, Patrol, Investigate, Combat }

public class GuardDroneAI : MonoBehaviour
{
    [HierarchyEnumCycler(BadgeColor = "#1E3A5F", TextColor = "#93C5FD")]
    public AIState currentBehavior = AIState.Patrol;

    public float detectionRadiusMeters = 15f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyEnumCyclerRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyEnumCyclerAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `BadgeColor` | `string` | `"#1E3A5F"` | Hex background color of the clickable enum badge. |
| `TextColor` | `string` | `"#64B5F6"` | Hex color of the enum text inside the badge. |
| `BorderRadius` | `float` | `4f` | Corner rounding radius in pixels for the badge pill. |
| `Bold` | `bool` | `false` | Whether to render the enum name in bold text. |
| `FontSize` | `int` | `0` | Font size in pixels, or `0` for default hierarchy font. |
| `Width` | `float` | `0f` | Fixed badge width in pixels, or `0f` to auto-size based on text. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin. |
| `RightClickReverse` | `bool` | `true` | When true, right-clicking the badge cycles in reverse order. |
| `WrapAround` | `bool` | `true` | When true, wraps between the first and last enum values continuously. |
| `UndoLabel` | `string` | `"Cycle Enum"` | Transaction description registered with Unity Undo in Edit Mode. |
| `Tooltip` | `string` | `""` | Optional hover tooltip text displayed over the badge. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the enum cycler badge remains interactive in Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public enum TeamFaction { Neutral, Vanguard, Marauders, Syndicate }

public class FactionSpawnMarker : MonoBehaviour
{
    [Header("Faction Affiliation")]
    [Tooltip("Click to advance faction; right-click to cycle backwards.")]
    [HierarchyEnumCycler(
        BadgeColor = "#312E81", 
        TextColor = "#C7D2FE", 
        BorderRadius = 4f, 
        Bold = true, 
        RightClickReverse = true, 
        Tooltip = "Click to cycle team affiliation", 
        XOffset = 6f)]
    public TeamFaction assignedFaction = TeamFaction.Neutral;

    [Header("Spawn Settings")]
    public int initialReinforcementUnits = 5;
    public float respawnDelaySeconds = 12f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyActiveButton]`**| High | Position cycler to the left of the active power button using `XOffset = 24f`. |
| **`[HierarchyIcon]`** | High | Combine with status icons to visually clarify active states. |
| **Custom Enums** | High | Automatically supports any standard C# `enum` definition without configuration. |
| **Undo Stack** | High | Toggling registers with `Undo.RecordObject` and calls `EditorUtility.SetDirty`. |
