# [HierarchySceneViewPing]

> Adds a navigation crosshair button directly on the hierarchy row to instantly focus and frame the Scene View camera on the object.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchySceneViewPing]` places an interactive crosshair navigation icon on the hierarchy row of high-value GameObjects. Driven by `HierarchySceneViewPingRenderer`:
- **Single-Click Framing:** Instantly calculates the composite bounding box across all child Renderers and Colliders, then smoothly frames the active Scene View camera (`SceneView.lastActiveSceneView.Frame(bounds, false)`) onto the object.
- **Shift+Click Ping:** Holding Shift while clicking immediately triggers `EditorGUIUtility.PingObject(go)`, highlighting the entity in the Hierarchy without moving the Scene camera.
- **Custom Iconography & Tints:** Renders using Unity's native `d_ViewToolMove` icon with customizable color tinting (`IconColor = "#00E5FF"`).

**The Problem:**
In expansive 3D open worlds or large multi-room levels, navigating to specific spawn points, trigger volumes, boss arenas, or collectible items requires selecting the object in the Hierarchy, moving your cursor over to the Scene View, and pressing `F` to frame. If the Scene View is not active, framing fails. Repeating this dozens of times during level design is tedious.

**The Solution:**
Decorating key components with `[HierarchySceneViewPing]`:
- **One-Click Camera Navigation:** Instantly frame key scene entities with a single click right on the hierarchy row.
- **Composite Bounds Calculation:** Automatically encapsulates child renderers and colliders so the camera zooms to the perfect framing distance.
- **Dual Framing / Ping Modes:** Frame on regular click; ping on Shift+Click.
- **Visual Crosshair Cue:** Distinct cyan crosshair makes key gameplay landmarks stand out in the hierarchy.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchySceneViewPing]
public class PlayerSpawnPoint : MonoBehaviour
{
    public int spawnIndex = 0;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchySceneViewPingRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchySceneViewPingAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `IconColor` | `string` | `"#00E5FF"` | Hex color of the crosshair target icon. |
| `Size` | `float` | `16f` | Width and height in pixels of the crosshair button. |
| `XOffset` | `float` | `2f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the navigation button remains visible and interactive in Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchySceneViewPing(IconColor = "#38BDF8", Size = 16f, XOffset = 4f)]
public class BossArenaTrigger : MonoBehaviour
{
    [Header("Encounter Arena")]
    public string arenaName = "THRONE_ROOM";
    public float activationRadius = 25f;
    public bool lockDoorsOnEnter = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyBookmark]`** | High | Use bookmarks for quick slot indexing and `HierarchySceneViewPing` for direct SceneView camera jumps. |
| **`[HierarchySolo]`** | High | Pair framing with solo isolation to inspect and work on individual props in complete visual isolation. |
| **SceneView Integration** | High | Queries `SceneView.lastActiveSceneView`; falls back gracefully to `EditorGUIUtility.PingObject` if no Scene View is open. |
| **Event Consumption** | High | Consumes mouse clicks to frame the camera without altering GameObject selection or triggering rename fields. |
