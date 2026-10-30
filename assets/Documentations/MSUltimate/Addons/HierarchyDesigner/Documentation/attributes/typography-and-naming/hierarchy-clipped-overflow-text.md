# [HierarchyClippedOverflowText]

> Truncates long hierarchy labels with an ellipsis to prevent clutter, with optional marquee scrolling on hover.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyClippedOverflowText]` caps excessively long GameObject names in the Hierarchy window at a specified character limit (`MaxCharacters = 18`), appending an ellipsis (`...`). When the user moves the mouse cursor over the row, an optional horizontal marquee animation smoothly scrolls the complete name so no information is lost.

**The Problem:**
In production pipelines (such as imported FBX rigs, photogrammetry scans, procedural dungeon rooms, or serialized network entity instances), GameObjects often have verbose names like `ModularMedievalCastle_WallSegment_VariationB_LOD0_CollisionAnchor`. These long labels push right-side controls off screen and create visual clutter in the Hierarchy window.

**The Solution:**
Decorating verbose prefabs or components with `[HierarchyClippedOverflowText]`:
- **Clean Truncation:** Clips the visible label neatly to a uniform width (`MaxCharacters = 18`).
- **Interactive Hover Marquee:** Hovering over the item triggers an automatic ticker tape scroll (`MarqueeOnHover = true`, `ScrollSpeed = 3.0f`) to reveal the full original identifier.
- **Custom Font Color:** Colorizes the visible name cleanly (`TextColor = "#E0E0E0"`).
- **Protects Layout Real Estate:** Preserves right-side margin space for icons, toggles, and metadata badges.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyClippedOverflowText(MaxCharacters = 16, MarqueeOnHover = true, ScrollSpeed = 2.5f)]
public class EnvironmentalDungeonProp : MonoBehaviour
{
    public int lodLevel = 0;
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
| **Render Engine** | `HierarchyClippedOverflowTextRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyClippedOverflowTextAttribute()
```

- Standard parameterless constructor. Truncation thresholds and marquee behavior are set via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MaxCharacters` | `int` | `18` | Maximum character length displayed before inserting an ellipsis. |
| `TextColor` | `string` | `"#E0E0E0"` | Hex color code of the displayed text. |
| `MarqueeOnHover` | `bool` | `true` | Whether hovering over the row initiates horizontal marquee scrolling of the full name. |
| `ScrollSpeed` | `float` | `3.0f` | Scrolling speed multiplier during hover marquee animation. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether clipping and hover marquee scrolling remain active during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy decorations. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyClippedOverflowText(
    MaxCharacters = 14, 
    TextColor = "#94A3B8", 
    MarqueeOnHover = true, 
    ScrollSpeed = 3.2f)]
public class ProceduralBi-DirectionalStreamingChunkProxy : MonoBehaviour
{
    [Header("Chunk Coordinates")]
    public Vector2Int chunkCoordinate = new Vector2Int(14, -8);
    public bool isChunkLoaded = true;
    public float streamDistanceThreshold = 120.0f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyTooltip]`** | High | Recommended companion: hover displays the complete GameObject name and documentation note in a tooltip window. |
| **`[HierarchyChildCounter]`** | High | Prevents long parent names from crowding out child counter badges on the right side. |
| **`[HierarchyIcon]`** | High | Leaves ample room for high-visibility custom component and prefab icons. |
| **`[HierarchyTextColor]`** | Incompatible | Do not stack with other text drawing attributes since clipped overflow takes over the label rendering pass. |
