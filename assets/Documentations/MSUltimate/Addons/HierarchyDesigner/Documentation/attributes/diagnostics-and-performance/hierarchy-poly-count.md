# [HierarchyPolyCount]

> Inspects mesh renderers and displays vertex or triangle counts directly on the hierarchy row with high-poly alert thresholds.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyPolyCount]` calculates polygon or vertex counts for GameObjects equipped with `MeshFilter` or `SkinnedMeshRenderer` components and renders a compact telemetry badge directly on the hierarchy row (e.g. `"🔺 14.2k"`, `"🔺 850"`). Driven by `HierarchyPolyCountRenderer`, it supports toggling between triangle counts (`ShowTriangles = true`) and vertex counts (`ShowTriangles = false`), aggregating counts across all child GameObjects (`IncludeChildren = true`), and switching to a distinct warning color (`WarnColor = "#FF4757"`) whenever counts exceed `WarnThreshold` (default 15,000).

**The Problem:**
Unoptimized 3D models with runaway triangle counts (un-decimated CAD imports, high-density photogrammetry assets, excessive hair/fur geometries) severely degrade rasterization performance and push mobile or VR projects over tight vertex budgets. Identifying high-poly culled meshes usually requires selecting each mesh and inspecting the Asset Importer or opening the Scene Statistics overlay, which only shows full-scene aggregates.

**The Solution:**
Decorating 3D models and prefab roots with `[HierarchyPolyCount]`:
- **Direct Poly Telemetry:** See exact triangle or vertex counts right in the hierarchy row without selecting the model.
- **Subtree Aggregation:** Sums up child mesh renderers to evaluate complete complex character or environment prefabs.
- **Budget Violation Alerts:** Turns vibrant red when exceeding defined polygon budgets (`WarnThreshold`).
- **Formatted Readouts:** Uses compact formatting (e.g., `12.4k`, `1.2M`) with exact counts displayed in hover tooltips.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyPolyCount(WarnThreshold = 20000, NormalColor = "#38BDF8", WarnColor = "#EF4444")]
public class PropMeshRoot : MonoBehaviour
{
    public string modelVariant = "CASTLE_TURRET_LOD0";
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
| **Render Engine** | `HierarchyPolyCountRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyPolyCountAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ShowTriangles` | `bool` | `true` | Displays triangle count when `true`, or vertex count when `false`. |
| `IncludeChildren` | `bool` | `true` | Whether to sum polygon counts from all child mesh renderers in the subtree. |
| `WarnThreshold` | `int` | `15000` | Polygon count threshold that triggers the warning color badge. |
| `NormalColor` | `string` | `"#70A1FF"` | Hex color of the badge for counts below the warning threshold. |
| `WarnColor` | `string` | `"#FF4757"` | Hex color of the badge for counts exceeding `WarnThreshold`. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the poly count badge remains visible during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyPolyCount(
    ShowTriangles = true, 
    IncludeChildren = true, 
    WarnThreshold = 35000, 
    NormalColor = "#60A5FA", 
    WarnColor = "#DC2626", 
    XOffset = 6f)]
public class HeroCharacterRig : MonoBehaviour
{
    [Header("Hero Model Settings")]
    public string characterName = "Paladin";
    public bool enableClothSimulation = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyDrawCallTracker]`** | High | Combine poly count tracking with material draw call tracking for comprehensive 3D asset profiling. |
| **`[HierarchyMemoryTracker]`** | High | Track mesh vertices and runtime RAM/VRAM footprint together. |
| **Supported Meshes** | High | Works with both static `MeshFilter` components and animated `SkinnedMeshRenderer` rigs. |
| **Subtree Aggregation** | High | Enabled by default (`IncludeChildren = true`) to give total prefab polygon budgets. |
