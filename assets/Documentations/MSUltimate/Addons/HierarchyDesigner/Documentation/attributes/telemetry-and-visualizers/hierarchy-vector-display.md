# [HierarchyVectorDisplay]

> Formats Vector2 or Vector3 coordinates into a compact badge on the hierarchy row with optional magnitude info.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyVectorDisplay]` formats 2D and 3D vector coordinates (`Vector2`, `Vector3`) into a sleek, compact badge on the hierarchy row. Driven by `HierarchyVectorDisplayRenderer`, it displays coordinates cleanly (e.g., `(1.2, 0.0, -4.5)`), with options to format numeric precision (`Format = "{0:F1}"`), customize colors (`TextColor = "#B8E994"`, `BadgeColor = "#1E272E"`), and append the Euclidean length magnitude (`ShowMagnitude = true`, e.g. `|4.7| (1.2, 0.0, -4.5)`).

**The Problem:**
Tracking spatial data (velocities, target offsets, aim directions, patrol waypoints, physics forces) requires opening the Inspector and expanding vector foldouts. When debugging multiple physics bodies or wandering AI units, comparing velocities or verifying whether a vector is zeroed is tedious.

**The Solution:**
Decorating vector fields or properties with `[HierarchyVectorDisplay]`:
- **At-a-Glance Coordinate Telemetry:** See current position offsets, velocities, or directional vectors directly in the hierarchy.
- **Euclidean Magnitude Readout:** Instantly verify whether a velocity vector is nonzero or within threshold speed (`ShowMagnitude = true`).
- **Compact Badge Styling:** Encapsulates numbers in a clean rounded dark pill badge.
- **Zero Inspector Distraction:** Inspect multiple moving entities simultaneously while keeping Scene View unobstructed.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class RigidbodyTelemetry : MonoBehaviour
{
    [HierarchyVectorDisplay(ShowMagnitude = true, TextColor = "#38BDF8")]
    public Vector3 velocity;
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
| **Render Engine** | `HierarchyVectorDisplayRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyVectorDisplayAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Format` | `string` | `"{0:F1}"` | Numerical format string applied to each vector component. |
| `BadgeColor` | `string` | `"#1E272E"` | Hex background color of the vector display badge container. |
| `TextColor` | `string` | `"#B8E994"` | Hex text color of the coordinates and magnitude text. |
| `ShowMagnitude` | `bool` | `false` | Whether to prepend the vector's Euclidean length magnitude (e.g. `\|3.2\| (x, y)`). |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the vector display remains visible and updates during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class ProjectileTracker : MonoBehaviour
{
    [Header("Flight Dynamics")]
    [HierarchyVectorDisplay(
        Format = "{0:F0}", 
        ShowMagnitude = true, 
        BadgeColor = "#0F172A", 
        TextColor = "#A3E635", 
        XOffset = 6f)]
    public Vector3 flightVelocity = new Vector3(15f, 2f, 45f);

    public float lifetimeSeconds = 3.0f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyBitmask]`** | High | Combine spatial vector displays with capability bitmasks for complete entity diagnostics. |
| **`[HierarchyStatusDot]`** | High | Use status dots for discrete alerts and vector displays for continuous spatial metrics. |
| **Vector Types** | High | Supports both `UnityEngine.Vector2` and `UnityEngine.Vector3` fields and properties. |
| **Repaint Hook** | High | Evaluated on repaint; does not intercept mouse clicks or alter selection logic. |
