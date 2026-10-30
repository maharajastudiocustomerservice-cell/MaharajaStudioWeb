# [HierarchyHighlight]

> Paints an elegant colored background tint across the hierarchy row with solid, gradient, or striped patterns.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyHighlight]` structures complex scene trees into visually distinct, color-coded zones. Managed by `HierarchyHighlightRenderer`, it tints the full width of the GameObject's hierarchy row using customizable hex colors (`ColorHex = "#4D4D4D40"`). It features three aesthetic fill patterns (`Mode = HierarchyHighlightMode.Solid`, `Gradient`, or `Striped`), optional child inheritance (`ApplyToChildren = true`) that applies dimmed tints to nested hierarchy branches, and selection-gated rendering (`ShowOnlyWhenSelected = true`).

**The Problem:**
In dense 3D scenes with hundreds of nested GameObjects, environmental set pieces, audio emitters, lighting rigs, and UI canvases blend into an indistinguishable gray wall of text. Finding the root object of a subsystem or distinguishing gameplay entities from static geometry requires endless scrolling.

**The Solution:**
Color-coding scene architecture with `[HierarchyHighlight]`:
- **Instant Subsystem Recognition:** Group lighting, audio, gameplay, and UI hierarchies with distinct color palettes.
- **Multiple Visual Fill Styles:** Choose between clean solid tints, modern left-to-right gradients (`GradientEndColor`), or subtle diagonal hazard stripes.
- **Recursive Branch Tinting:** Automatically tint child objects (`ApplyToChildren = true`) to visually encapsulate entire folder structures.
- **Selection Gating:** Optionally reveal highlights only when an entity or parent is actively selected.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyHighlight("#1E3A8A")]
public class AudioSubsystemRoot : MonoBehaviour
{
    public float masterMusicVolume = 0.8f;
    public float soundEffectsVolume = 1.0f;
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
| **Render Engine** | `HierarchyHighlightRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyHighlightAttribute()
public HierarchyHighlightAttribute(string colorHex)
```

- `colorHex`: Primary hex color string (with optional alpha) for the hierarchy row highlight tint.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ColorHex` | `string` | `"#4D4D4D40"` | Hex color string for the row highlight tint. |
| `Mode` | `HierarchyHighlightMode` | `Solid` | Visual fill mode (`Solid`, `Gradient`, or `Striped`). |
| `GradientEndColor` | `string` | `""` | Ending hex color used when `Mode` is set to `Gradient`. |
| `ApplyToChildren` | `bool` | `false` | When true, renders a subtle matching highlight on all child GameObjects. |
| `ShowOnlyWhenSelected`| `bool` | `false` | When true, the highlight is only rendered when the object is actively selected. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the row highlight remains active in Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyHighlight(
    ColorHex = "#065F46", 
    Mode = HierarchyHighlightMode.Gradient, 
    GradientEndColor = "#064E3B00", 
    ApplyToChildren = true)]
public class EnvironmentalFoliageGroup : MonoBehaviour
{
    [Header("Foliage Cluster Parameters")]
    public int treeCount = 45;
    public float windSwayStrength = 1.25f;
    public bool enableGPUInstancing = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyIcon]`** | High | Highlight colors serve as a gentle backdrop for high-resolution icons. |
| **`[HierarchyBadge]`** | High | Badges float clearly over highlights without color muddiness. |
| **Striped Mode** | High | Recommended for hazardous or debug-only scene objects (e.g. NavMesh blockers). |
| **Hierarchy Selection** | High | Highlighting blends cleanly with Unity's native multi-selection highlight box. |
