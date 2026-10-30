# [HierarchyHoloScanText]

> Displays a sci-fi holographic laser scan beam sweeping across the hierarchy label with optional HUD brackets.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyHoloScanText]` transforms the GameObject label into a sci-fi holographic HUD display. A radiant laser scan bar (`ScanColor = "#FFFFFF"`) continuously sweeps across the characters from left to right (`SweepSpeed = 2.5f`), with optional high-tech framing brackets (`⎡ ⎦`) surrounding the name.

**The Problem:**
In sci-fi, space simulator, or cyberpunk games, developer hierarchies often include drones, automated turrets, holographic projections, or targeting radars. Differentiating these active sensory objects with standard static text does not reflect their high-tech, actively scanning nature.

**The Solution:**
Decorating components with `[HierarchyHoloScanText]`:
- **Real-Time Holographic Scan Beam:** A dynamic laser specular highlight sweeps smoothly across the glyphs, illuminating individual characters as the beam passes.
- **Sci-Fi HUD Framing Brackets:** Automatically flanks the label with framing glyphs (`ShowCornerBrackets = true`) to mimic a futuristic targeting reticle.
- **Dual-Tone Customization:** Specify base holographic text tint (`TextColor = "#00D2FF"`) and scan beam intensity (`ScanColor = "#FFFFFF"`).
- **Zero Overhead:** Fully procedural IMGUI implementation requiring no custom shaders or materials.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyHoloScanText(TextColor = "#00D2FF", ScanColor = "#FFFFFF", SweepSpeed = 3.0f, ShowCornerBrackets = true)]
public class RadarScannerTower : MonoBehaviour
{
    public float detectionRadius = 150f;
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
| **Render Engine** | `HierarchyHoloScanTextRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyHoloScanTextAttribute()
```

- Standard parameterless constructor. Sweep velocity, colors, and bracket display are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `TextColor` | `string` | `"#00D2FF"` | Hex color string of the base holographic label text. |
| `ScanColor` | `string` | `"#FFFFFF"` | Hex color string of the sweeping laser beam highlight. |
| `SweepSpeed` | `float` | `2.5f` | Sweep velocity multiplier of the laser scan highlight. |
| `ShowCornerBrackets` | `bool` | `true` | Whether to wrap the name in sci-fi framing brackets (`⎡ ⎦`). |
| `Bold` | `bool` | `true` | Whether to render the label characters with bold font weight. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the holographic scan continues during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row decorations. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyHoloScanText(
    TextColor = "#38BDF8", 
    ScanColor = "#F0FDFA", 
    SweepSpeed = 3.2f, 
    ShowCornerBrackets = true, 
    Bold = true)]
public class DroneTargetingArray : MonoBehaviour
{
    [Header("Sensor Array")]
    public int activeTrackedTargets = 4;
    public float sweepAngle = 120.0f;
    public bool isTrackingHostiles = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyTooltip]`** | High | Display radar coordinates, scan frequencies, or detection logs on hover. |
| **`[HierarchyGlow]`** | High | Combine with a cyan or blue ambient glow to simulate holographic backlighting. |
| **`[HierarchyTextColor]`** | Incompatible | Do not stack with static color attributes as holographic scan manages character tinting. |
| **`[HierarchyBookmark]`** | High | Safely stacks with bookmark ribbon indicators without interfering with sweep animations. |
