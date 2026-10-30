# [HierarchyDrawCallTracker]

> Analyzes submesh and material counts across renderers, flagging potential batch-breaking setups with an alert badge.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyDrawCallTracker]` inspects the GameObject and all of its child renderers (`Renderer.sharedMaterials`) to identify how many unique materials are assigned. Driven by `HierarchyDrawCallTrackerRenderer`, it renders a compact badge directly on the hierarchy row displaying the unique material count (e.g., `"2 Mat"`). When the count exceeds `MaxAllowedMaterials` (default 2), it switches from a neutral gray badge (`NormalColor = "#57606F"`) to a vibrant alert color (`AlertColor = "#FFA502"`).

**The Problem:**
In 3D game development, excessive material assignments are the number one cause of broken SRP batching, high draw call counts, and degraded GPU frame rates. Artists and level designers often combine models with multiple submeshes and independent materials without realizing that each unique material introduces separate draw calls.

**The Solution:**
Decorating environment props and character rigs with `[HierarchyDrawCallTracker]`:
- **Immediate Batching Auditing:** See the exact material footprint directly in the Hierarchy window.
- **Automated High-Material Alerts:** Visually flags objects that break batching thresholds (`AlertColor`).
- **Child Subtree Aggregation:** Uses `GetComponentsInChildren<Renderer>(true)` to gather all mesh renderers and skinned meshes in the subtree.
- **Zero Runtime Draw Calls:** Runs purely within editor GUI rendering without allocating game materials or mutating instances.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyDrawCallTracker(MaxAllowedMaterials = 2, AlertColor = "#EF4444")]
public class ModularEnvironmentPiece : MonoBehaviour
{
    public string assetId = "WALL_MODULAR_A";
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
| **Render Engine** | `HierarchyDrawCallTrackerRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyDrawCallTrackerAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MaxAllowedMaterials` | `int` | `2` | Maximum unique material count allowed before triggering an alert badge. |
| `NormalColor` | `string` | `"#57606F"` | Hex color of the badge when material count is within threshold. |
| `AlertColor` | `string` | `"#FFA502"` | Hex color of the badge when material count exceeds `MaxAllowedMaterials`. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the badge remains visible during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyDrawCallTracker(
    MaxAllowedMaterials = 1, 
    NormalColor = "#334155", 
    AlertColor = "#DC2626", 
    XOffset = 6f)]
public class StaticPropOptimizer : MonoBehaviour
{
    [Header("Static Batching Target")]
    public bool isStaticBatched = true;
    public int lodLevel = 0;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyPolyCount]`** | High | Combine material draw call tracking with poly count tracking for complete mesh optimization. |
| **`[HierarchyMemoryTracker]`** | High | Track both draw call material complexity and texture/mesh memory footprint side-by-side. |
| **Renderer Inspection** | High | Works with `MeshRenderer`, `SkinnedMeshRenderer`, and `SpriteRenderer`. |
| **Performance Impact** | Minimal | Deduplicates shared materials via hash set caches; skips calculation if no renderers exist. |
