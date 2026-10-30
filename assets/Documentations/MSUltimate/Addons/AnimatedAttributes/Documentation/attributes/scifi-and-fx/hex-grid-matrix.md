# [HexGridMatrix]

> Renders an animated hexagonal honeycomb grid pattern with subtle neon line pulses across the field background.

---

## 1. Overview & Value Proposition

**What it does:**
`[HexGridMatrix]` projects a cyberpunk, high-tech honeycomb tessellation directly into the background of inspector fields. Using UI Toolkit's 2D vector painter (`MeshGenerationContext.painter2D`), it computes a mathematical hexagonal lattice using trigonometric 6-point polygons (`HexRadius`, defaulting to 12px) in a translucent neon line style (`ColorHex` at 12% opacity). The grid updates periodically based on `PulseSpeed` to convey futuristic energy matrix fields.

**The Problem:**
Nanotechnology parameters, cyberpunk cyberware modules, energy shielding, or tactical turn-based grid maps look mundane against flat monochrome inspector panels. Standard UI layouts do not evoke high-tech hexagonal modularity.

**The Solution:**
Decorating tactical, cybernetic, or shield variables with `[HexGridMatrix]`:
- **Mathematical Hex Lattice:** Generates authentic 6-sided honeycomb cells with accurate spacing (`hDist = r * 1.5, vDist = r * sqrt(3)`).
- **Subtle Ambient Styling:** Rendered at a balanced 12% alpha so input values and labels remain crisp and readable in foreground.
- **Customizable Cell Scale:** Scale hexagon cell dimensions (`HexRadius`) from dense micro-meshes to bold architectural hex plates.
- **Hardware-Accelerated UI Toolkit Paths:** Drawn directly via vector strokes with `PickingMode.Ignore`, adding zero layout lag to your workflow.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class CyberwareImplant : MonoBehaviour
{
    [HexGridMatrix(colorHex: "#00F0FF", hexRadius: 14f)]
    public float neuralBandwidthOverclock = 1.35f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public HexGridMatrixAttribute(string colorHex = "#00F0FF", float hexRadius = 12f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `colorHex` | `string` | `"#00F0FF"` | Hex color string of the hexagonal grid lines and pulses. |
| `hexRadius` | `float` | `12f` | Outer radius of individual hexagon cells in pixels. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ColorHex` | `string` | `"#00F0FF"` | Hex color string for the honeycomb mesh lines (defaults to Cyan). |
| `HexRadius` | `float` | `12f` | Outer radius in pixels of each hexagon cell. |
| `PulseSpeed` | `float` | `1.2f` | Animation update speed multiplier. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class EnergyMatrixGenerator : MonoBehaviour
{
    [Header("Nanotech Shield Matrix")]
    [HexGridMatrix(
        colorHex: "#10B981", 
        hexRadius: 16f, 
        PulseSpeed = 1.5f
    )]
    public float honeycombShieldCoherence = 94.2f;

    [Header("Tactical Grid Dimensions")]
    [HexGridMatrix(colorHex: "#F59E0B", hexRadius: 10f)]
    public int activeSectorHexCount = 64;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Fills honeycomb background seamlessly inside box group boundaries. |
| `[EnergyBorderBeam]` | Stacking | Pairs with circulating energy border beams for high-tech sci-fi terminal cards. |
| `[ReadOnly]` | Supported | Enriches read-only tactical readouts with vibrant geometric background patterns. |
