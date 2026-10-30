# [Hierarchy]

> Foundational base attribute for all Unity Hierarchy window decorators, interactive widgets, badges, and telemetry overlays.

---

## 1. Overview & Value Proposition

**What it does:**
`[Hierarchy]` is the root architectural attribute powering the entire MSUltimate-HierarchyDesigner ecosystem. Decorator classes deriving from `HierarchyAttribute` hook directly into the Unity Editor's `hierarchyWindowItemOnGUI` pipeline via the high-performance `HierarchyRendererEngine`. The base attribute provides core lifecycle controls common to all hierarchy decorators: whether the decorator renders during active Play Mode (`IsActiveInPlayMode = true`), and the precise horizontal/drawing evaluation order when stacking multiple decorators on a single GameObject (`Order = 0`).

**The Problem:**
Standard Unity inspectors isolate component data strictly inside the Inspector window. When navigating complex game scenes with hundreds of nested entities, developers must click every individual GameObject one by one to inspect their component types, active states, health percentages, or layer assignments.

**The Solution:**
Extending and utilizing `[Hierarchy]`:
- **Direct Hierarchy Visualization:** Surfaces crucial runtime variables, alerts, and interactive buttons straight into the Hierarchy list view.
- **Unified Draw Order Architecture:** The `Order` property allows developers to arrange multiple decorators from left to right with deterministic priority.
- **PlayMode Lifecycle Control:** Toggle `IsActiveInPlayMode` to hide diagnostic clutter during gameplay testing or keep live debug telemetry active.
- **High-Performance Caching:** The underlying renderer engine caches component reflection metadata, preventing GC allocations during rapid editor repaints.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

// Demonstrating standard derived usage of the Hierarchy attribute family
[HierarchyHighlight("#2E4057", Order = 0)]
[HierarchyActiveButton(Order = 1)]
public class SpawnPointEntity : MonoBehaviour
{
    public string spawnZoneTag = "Sector-Alpha";
    public int teamAffiliation = 1;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class | Field | Method | Property` |
| **Inherited** | Yes |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyRendererEngine (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
// Abstract base class inherited by all MSUltimate hierarchy attributes
protected HierarchyAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `IsActiveInPlayMode` | `bool` | `true` | When true, renders this decorator while the Unity Editor is running in Play Mode. |
| `Order` | `int` | `0` | Draw priority order when multiple hierarchy attributes are stacked on the same entity. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

// Custom customizer demonstrating custom inheritance from HierarchyAttribute
[System.AttributeUsage(System.AttributeTargets.Class, AllowMultiple = false, Inherited = true)]
public class CustomLevelEntityAttribute : HierarchyAttribute
{
    public string ZoneName { get; set; }

    public CustomLevelEntityAttribute(string zoneName)
    {
        ZoneName = zoneName;
        Order = 10;
        IsActiveInPlayMode = true;
    }
}

[CustomLevelEntity("DUNGEON-BOSS-ROOM")]
public class BossRoomEncounterManager : MonoBehaviour
{
    [Header("Encounter Settings")]
    public float bossMaxHealth = 8500f;
    public bool isEncounterTriggered = false;
    public int activeMinionSpawners = 4;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **Hierarchy Badges & Buttons** | High | Use the `Order` property to prevent overlapping elements on narrow Hierarchy windows. |
| **Play Mode Telemetry** | High | Set `IsActiveInPlayMode = false` on static design tags to declutter the list during playtests. |
| **Inspector Decorators** | High | Fully orthogonal to MSUltimate Inspector attributes; does not affect Inspector drawing. |
| **Performance** | High | Processed via cached lookup tables to ensure 120+ FPS editor repaints even in scenes with thousands of nodes. |
