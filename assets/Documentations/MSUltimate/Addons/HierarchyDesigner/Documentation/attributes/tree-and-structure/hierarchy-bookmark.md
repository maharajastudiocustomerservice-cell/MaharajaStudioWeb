# [HierarchyBookmark]

> Marks a high-priority GameObject with a colored bookmark ribbon and quick slot indicator directly on the hierarchy row.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyBookmark]` anchors a prominent, colored bookmark ribbon (`BookmarkColor = "#FF5E57"`) with a slot index (e.g. `"#1"`, `"#2"`) directly on the hierarchy row of high-priority GameObjects. Driven by `HierarchyBookmarkRenderer`, clicking the bookmark ribbon immediately highlights and selects the GameObject (`Selection.activeGameObject = go`) and pings it via `EditorGUIUtility.PingObject(go)`.

**The Problem:**
In large, multi-branch hierarchies with hundreds or thousands of entities, finding the key manager, the level exit trigger, the current player rig, or a specific debug spawner requires scrolling up and down through the list repeatedly or typing into the search filter (which collapses the tree hierarchy view).

**The Solution:**
Decorating critical scene objects with `[HierarchyBookmark]`:
- **Visual Bookmark Ribbon:** Instantly spot key landmark objects even when scrolling past dense trees.
- **Single-Click Selection & Ping:** Click the ribbon to select and ping the object without needing to click its text label.
- **Slot Index or Custom Text:** Display a slot number (`#1`, `#2`) or a short custom label (`Label = "KEY"`).
- **Custom Color Ribbons:** Assign different ribbon colors (e.g., cyan for lighting, red for boss rigs, green for spawners).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyBookmark(Slot = 1, BookmarkColor = "#38BDF8")]
public class PlayerController : MonoBehaviour
{
    public float moveSpeed = 6.0f;
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
| **Render Engine** | `HierarchyBookmarkRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyBookmarkAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Slot` | `int` | `1` | Numeric bookmark slot index displayed when `Label` is empty (e.g. `"#1"`). |
| `BookmarkColor` | `string` | `"#FF5E57"` | Hex color of the bookmark ribbon background. |
| `TextColor` | `string` | `"#FFFFFF"` | Hex color of the bookmark text label. |
| `Label` | `string` | `""` | Optional short text label displayed on the ribbon (overrides `Slot`). |
| `Width` | `float` | `22f` | Width of the bookmark ribbon in pixels. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the bookmark remains visible and clickable during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyBookmark(
    Slot = 1, 
    Label = "BOSS", 
    BookmarkColor = "#EF4444", 
    TextColor = "#FFFFFF", 
    Width = 36f, 
    XOffset = 6f)]
public class DragonBossController : MonoBehaviour
{
    [Header("Encounter Parameters")]
    public float maxHealth = 10000f;
    public bool isEncounterActive = false;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchySceneViewPing]`** | High | Use bookmarks for hierarchy selection and SceneView pings for camera framing. |
| **`[HierarchyGlow]`** | High | Pair bookmark ribbons with ambient glow to make top-tier hero entities unmistakably prominent. |
| **`[HierarchyFolder]`** | High | Bookmark key folders to jump between major scene sections instantly. |
| **Selection Integration** | High | Directly sets `Selection.activeGameObject = go` upon click, integrating cleanly with the Inspector. |
