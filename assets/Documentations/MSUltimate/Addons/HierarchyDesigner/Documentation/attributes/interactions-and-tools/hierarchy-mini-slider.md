# [HierarchyMiniSlider]

> Renders a compact draggable horizontal slider directly on the hierarchy row for live numeric tuning.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyMiniSlider]` binds a compact, interactive slider directly to numeric fields or properties on the hierarchy row. Driven by `HierarchyMiniSliderRenderer`, dragging the slider bar updates the numeric value in real time. It uses Unity's `GUIUtility.hotControl` mechanism to capture mouse drag interactions smoothly without conflicting with hierarchy row dragging or selection. It records full Unity Undo history in Edit Mode (`Undo.RecordObject`) and mutates fields directly during Play Mode.

**The Problem:**
Balancing scalar properties (e.g., audio volume, light intensity, AI aggro radius, camera FOV, spawn probabilities) requires selecting each entity, locating its slider in the Inspector, scrubbing, and checking results in the Scene or Game View. Toggling back and forth between multiple GameObjects to balance their relative values is cumbersome.

**The Solution:**
Decorating numeric fields or properties with `[HierarchyMiniSlider]`:
- **Direct Hierarchy Scrubbing:** Click and drag the slider track right in the hierarchy row to tune values instantly.
- **Custom Value Range:** Set explicit `MinValue` and `MaxValue` boundaries (e.g., `0f` to `1f` or `0f` to `100f`).
- **Stylized Visual Bar:** Features custom fill and background colors with smooth rounded edges.
- **Conflict-Free Dragging:** Captures mouse drag focus so dragging does not accidentally reorder hierarchy nodes.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class AmbientAudioZone : MonoBehaviour
{
    [HierarchyMiniSlider(MinValue = 0f, MaxValue = 1f, FillColor = "#10B981")]
    public float masterVolume = 0.75f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Field`, `Property` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyMiniSliderRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyMiniSliderAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MinValue` | `float` | `0f` | Minimum slider value mapped to the left edge of the track. |
| `MaxValue` | `float` | `1f` | Maximum slider value mapped to the right edge of the track. |
| `FillColor` | `string` | `"#6C5CE7"` | Hex color of the filled portion of the slider bar. |
| `BackgroundColor` | `string` | `"#2D3436"` | Hex background color of the slider track. |
| `Width` | `float` | `50f` | Width of the slider bar in pixels. |
| `Height` | `float` | `8f` | Height of the slider bar in pixels. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the slider remains visible and interactive in Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class SpotLightRig : MonoBehaviour
{
    [Header("Lighting Controls")]
    [HierarchyMiniSlider(
        MinValue = 0f, 
        MaxValue = 10f, 
        FillColor = "#F59E0B", 
        BackgroundColor = "#1E293B", 
        Width = 60f, 
        Height = 8f, 
        XOffset = 6f)]
    public float lightIntensity = 3.5f;

    public Color lightColor = Color.white;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyColorSwatch]`** | High | Combine mini sliders with color swatches for full lighting/color tuning directly in the hierarchy. |
| **`[HierarchyToggle]`** | High | Place sliders alongside toggles to enable systems and tweak their intensity side-by-side. |
| **Numeric Member Types** | High | Supports `float`, `int`, and `double` serialized fields and properties. |
| **Undo Stack** | High | Modifying values registers `Undo.RecordObject(component, $"Change {fieldInfo.Name}")` in Edit Mode. |
