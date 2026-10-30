# [HierarchyMemoryTracker]

> Displays estimated RAM and VRAM asset footprint on the hierarchy row with threshold-based alert badges.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyMemoryTracker]` calculates the real-time runtime memory footprint of all assets referenced by a GameObject (Meshes, Textures, Sprites, and AudioClips) and displays the formatted size directly on the hierarchy row (e.g. `"💾 1.4 MB"` or `"💾 250 KB"`). Driven by `HierarchyMemoryTrackerRenderer`, it queries Unity's `Profiler.GetRuntimeMemorySizeLong` and applies a 3-tier color system:
- **Normal:** Displays in green (`NormalColor = "#27AE60"`) when below warning thresholds.
- **Warning:** Transitions to amber (`WarningColor = "#F39C12"`) when exceeding `WarningThresholdMB` (default 2.0 MB).
- **Critical:** Flashes red (`CriticalColor = "#C0392B"`) when exceeding `CriticalThresholdMB` (default 8.0 MB).
- **Child Subtree Aggregation:** Can optionally aggregate memory across all child GameObjects (`IncludeChildren = true`).

**The Problem:**
High-resolution 4K textures, uncompressed audio clips, and massive high-poly meshes frequently cause unexpected memory bloat, mobile crashes, and frame stutters during asset streaming. Finding which specific GameObject or prefab variant is consuming memory usually requires running a full memory capture in the Unity Memory Profiler, which takes time and cannot be monitored while building scenes.

**The Solution:**
Decorating components or prefabs with `[HierarchyMemoryTracker]`:
- **Real-Time Memory Telemetry:** See the exact asset memory consumption right beside the object name in the Hierarchy.
- **3-Tier Threshold Alerts:** Instantly spot bloated assets that violate memory budgets for mobile, VR, or consoles.
- **Subtree Memory Aggregation:** Sums up child assets to measure total prefab or environment cluster footprints.
- **Detailed Byte Tooltips:** Hovering over the badge displays exact byte counts alongside megabyte readouts.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyMemoryTracker(WarningThresholdMB = 4.0f, CriticalThresholdMB = 12.0f)]
public class HighResHeroCharacter : MonoBehaviour
{
    public Mesh heroMesh;
    public Texture2D diffuseMap;
    public Texture2D normalMap;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class`, `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyMemoryTrackerRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyMemoryTrackerAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `WarningThresholdMB` | `float` | `2.0f` | Warning threshold in megabytes (MB) that triggers `WarningColor`. |
| `CriticalThresholdMB` | `float` | `8.0f` | Critical alert threshold in megabytes (MB) that triggers `CriticalColor`. |
| `IncludeChildren` | `bool` | `false` | Whether to include asset memory from all child GameObjects in the subtree. |
| `NormalColor` | `string` | `"#27AE60"` | Hex color of the badge when memory is below the warning threshold. |
| `WarningColor` | `string` | `"#F39C12"` | Hex color of the badge when memory exceeds `WarningThresholdMB`. |
| `CriticalColor` | `string` | `"#C0392B"` | Hex color of the badge when memory exceeds `CriticalThresholdMB`. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the memory badge remains visible during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyMemoryTracker(
    WarningThresholdMB = 5.0f, 
    CriticalThresholdMB = 15.0f, 
    IncludeChildren = true, 
    NormalColor = "#10B981", 
    WarningColor = "#F59E0B", 
    CriticalColor = "#EF4444", 
    XOffset = 6f)]
public class BossPrefabRoot : MonoBehaviour
{
    [Header("Boss Identity")]
    public string bossId = "TITAN_GOLEM";
    public bool preloadAudio = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyPolyCount]`** | High | Combine memory tracking with poly count tracking for complete mesh and texture profiling. |
| **`[HierarchyDrawCallTracker]`** | High | Track memory footprints alongside material draw calls to optimize rendering performance. |
| **`Profiler.GetRuntimeMemorySizeLong`** | High | Queries Unity's official profiler API; deduplicates shared assets using internal hash sets. |
| **Class vs Field Targets** | High | Apply to classes for full-object asset profiling, or to specific asset fields for focused auditing. |
