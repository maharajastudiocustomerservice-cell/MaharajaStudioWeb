# [SceneObjectOnly]

> Restricts object reference fields strictly to active Scene hierarchy instances, blocking project assets and prefabs from invalid assignment.

---

## 1. Overview & Value Proposition

**What it does:**
Enforces that an object reference field (e.g. `Transform`, `GameObject`, `Collider`) can only be populated by objects existing in the active scene hierarchy. If a designer drags a project asset or prefab asset from the Project browser, it immediately flags a warning or auto-rejects the assignment.

**The Problem:**
Certain gameplay references—such as patrol waypoints, player spawn points, cinematic cameras, or room boundary triggers—must exist as physical scene instances in the level. Accidentally dragging an uninstantiated prefab asset into a scene-only reference causes silent runtime bugs, broken positions, or missing component errors.

**The Solution:**
Add `[SceneObjectOnly]` to any `UnityEngine.Object` field:
- **Instant Drag Validation:** Detects whether an assigned asset resides in the Project database or an instantiated scene.
- **Configurable Auto-Clear:** Automatically nullifies illegal project asset assignments if `AutoClear = true`.
- **Active Scene Restriction:** Restricts references strictly to the currently active scene in multi-scene editing setups (`RequireInActiveScene = true`).
- **Customizable Warning Banners:** Formats clear warning messages with custom text and styling.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class PatrolAgent : MonoBehaviour
{
    [SceneObjectOnly]
    public Transform patrolRouteAnchor;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any `UnityEngine.Object` (Components, GameObjects) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public SceneObjectOnlyAttribute()
```

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ShowWarning` | `bool` | `true` | Displays a warning notification infobox if a project asset is assigned. |
| `AutoClear` | `bool` | `false` | Automatically resets the field to `null` if a project asset is dropped. |
| `RequireInActiveScene` | `bool` | `false` | Requires the assigned object to belong to the active scene in multi-scene setups. |
| `WarningMessage` | `string` | `"Assigning Project Assets is not allowed for this field. Please assign a Scene Object."` | Warning text displayed below the field. |
| `ErrorColor` | `string` | `""` | Hex color code for warning message text. |
| `ErrorBackgroundColor` | `string` | `""` | Hex background color for the warning banner. |
| `FontSize` | `int` | `0` | Font size override for the warning message. |
| `Padding` | `float` | `0f` | Internal padding for the warning banner. |
| `Margin` | `float` | `5f` | Spacing around the warning banner. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class LevelBossArena : MonoBehaviour
{
    [Header("Arena Spawn Locations")]
    [SceneObjectOnly(RequireInActiveScene = true, AutoClear = true)]
    public Transform bossSpawnPedestal;

    [Header("Cinematic Focal Camera")]
    [SceneObjectOnly(WarningMessage = "Focal camera must be an active camera placed inside this level scene!")]
    public Camera cutsceneCamera;

    [Header("Patrol Waypoint Ring")]
    [SceneObjectOnly]
    public List<Transform> arenaPerimeterWaypoints = new List<Transform>();
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Required]` | Recommended | Pairs together to ensure the field is both populated AND points to a scene object. |
| `[BoxGroup]` | Supported | Warning infobox renders inside the layout container without breaking borders. |
| `[AssetOnly]` | Mutually Exclusive | Do not combine on the same field; `[AssetOnly]` and `[SceneObjectOnly]` enforce opposite rules. |
| `ICollectionElement` | Supported | Validates every element inside `List<GameObject>` or `Transform[]`. |
