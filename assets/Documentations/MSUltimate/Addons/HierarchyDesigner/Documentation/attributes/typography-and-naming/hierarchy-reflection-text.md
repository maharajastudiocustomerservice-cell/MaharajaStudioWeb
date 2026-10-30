# [HierarchyReflectionText]

> Renders a subtle mirrored vertical reflection shadow directly beneath the hierarchy label.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyReflectionText]` draws a mirrored, semi-transparent reflection directly beneath the GameObject's hierarchy row label, simulating a glossy glass or wet surface reflection.

**The Problem:**
In high-end visual showcases, tech demos, and aquatic or ice environments, scene hierarchies often benefit from thematic visual styling that reflects the in-game mood. Standard Unity Hierarchy labels are flat, 1D elements with zero depth or surface simulation.

**The Solution:**
Decorating components with `[HierarchyReflectionText]`:
- **Glossy Surface Reflection:** Renders an inverted duplicate pass with smooth alpha fade (`ReflectionAlpha = 0.35f`).
- **Precision Pixel Offset:** Configures the vertical distance between the text baseline and the reflection (`OffsetY = 2.0f`).
- **Subtle Luxury Aesthetic:** Adds depth without cluttering the screen or obstructing neighboring rows.
- **Pure Vector Drawing:** Uses native IMGUI transformation matrix operations with zero runtime overhead.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyReflectionText(TextColor = "#E0E0E0", ReflectionAlpha = 0.4f, OffsetY = 2.0f)]
public class IceCavernWaterSurface : MonoBehaviour
{
    public float waterReflectivity = 0.85f;
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
| **Render Engine** | `HierarchyReflectionTextRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyReflectionTextAttribute()
```

- Standard parameterless constructor. Alpha attenuation and offset properties are set via object initializers.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `TextColor` | `string` | `"#E0E0E0"` | Hex color string of the primary label text. |
| `ReflectionAlpha` | `float` | `0.35f` | Opacity multiplier applied to the mirrored reflection. |
| `OffsetY` | `float` | `2.0f` | Vertical pixel gap between the label and its reflection shadow. |
| `Bold` | `bool` | `true` | Whether to render characters with bold font weight. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether reflection styling remains active during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row decorations. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyReflectionText(
    TextColor = "#38BDF8", 
    ReflectionAlpha = 0.5f, 
    OffsetY = 2.5f, 
    Bold = true)]
public class PlanarReflectionProbeAnchor : MonoBehaviour
{
    [Header("Reflection System")]
    public Camera reflectionCamera;
    public RenderTexture targetTexture;
    public LayerMask reflectiveLayers;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyGlow]`** | High | Combines reflection effects with soft neon glow for underwater or synthwave scene hierarchies. |
| **`[HierarchyTooltip]`** | High | Hover tooltips display probe resolution and clipping plane settings without visual collision. |
| **`[HierarchyBookmark]`** | High | Works smoothly alongside bookmark ribbons. |
| **`[HierarchyTextColor]`** | Incompatible | Do not stack with standard text coloring attributes as reflection text handles the label rendering. |
