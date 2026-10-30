# [XYPadController]

> Renders an interactive 2D touchpad joystick for Vector2 properties with crosshair grids, movable pucks, and optional spring recentering.

---

## 1. Overview & Value Proposition

**What it does:**
`[XYPadController]` replaces dual numeric float fields with a tactile 2D touchpad controller. It renders a square touch canvas (`PadSize`, defaulting to 80px) equipped with crosshairs and a draggable cursor puck (`PuckColor`, defaulting to hot pink `#EC4899`). Dragging the puck interactively maps normalized coordinates across `MinValue` and `MaxValue` (or dynamic bounds via `DynamicMaxValueMember`). It supports optional spring-return to origin upon release (`SpringReturn = true`), coordinate readouts (`ShowValue`), and collection cascading.

**The Problem:**
Tuning two-dimensional vectors—such as virtual thumbstick deadzones, wind directions, texture UV offsets, aim offsets, or gravity direction—requires guessing raw X and Y numbers in separate float fields. Visualizing how X and Y relate spatially is difficult without a visual 2D coordinate plane.

**The Solution:**
Decorating `Vector2` properties with `[XYPadController]`:
- **Intuitive 2D Cartesian Pad:** Drag the puck freely across 2D planar space to set X and Y coordinates simultaneously.
- **Elastic Spring Return:** Optional snap-back to `(0, 0)` upon releasing the mouse (`SpringReturn = true`) for joystick simulation.
- **Dynamic Limits Binding:** Bind maximum limits dynamically via `dynamicMaxValueMember` or `DynamicMinValueMember`.
- **Integrated Precision Input Field:** Includes a companion `Vector2` input field (`DrawInputField = true`) for direct manual entry.
- **Collection Cascading:** Implements `ICollectionElementAttribute` strictly constrained to `Vector2` elements.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class VirtualJoystick : MonoBehaviour
{
    [XYPadController(padSize: 90f, min: -1f, max: 1f)]
    public Vector2 analogStickInput = Vector2.zero;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `UnityEngine.Vector2` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Collection Element Support** | Yes (`ICollectionElementAttribute` for `Vector2`) |

---

## 4. Constructors & Parameters

```csharp
public XYPadControllerAttribute(float padSize = 80f, float min = -1f, float max = 1f)

public XYPadControllerAttribute(string dynamicMaxValueMember, float padSize = 80f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `padSize` | `float` | `80f` | Width and height of the touchpad square in pixels. |
| `min` | `float` | `-1f` | Minimum value bound on both X and Y axes. |
| `max` | `float` | `1f` | Maximum value bound on both X and Y axes. |
| `dynamicMaxValueMember` | `string` | — | Name of a member providing dynamic upper range capacity. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `PadSize` | `float` | `80f` | Dimensions of the touchpad canvas square in pixels. |
| `MinValue` | `float` | `-1f` | Minimum value bound on both axes. |
| `MaxValue` | `float` | `1f` | Maximum value bound on both axes. |
| `DynamicMaxValueMember` | `string` | `null` | Name of a member providing dynamic maximum bound. |
| `DynamicMinValueMember` | `string` | `null` | Name of a member providing dynamic minimum bound. |
| `PuckColor` | `string` | `"#EC4899"` | Hex color string for the movable cursor puck (defaults to Hot Pink). |
| `SpringReturn` | `bool` | `false` | Whether the puck automatically springs back to origin `(0, 0)` upon release. |
| `DrawInputField` | `bool` | `true` | Whether to draw the companion Vector2 input field. |
| `ShowInputField` | `bool` | `true` | Alias for `DrawInputField`. |
| `IsEditable` | `bool` | `true` | Whether the XY pad puck can be dragged interactively. |
| `Interactive` | `bool` | `true` | Alias for `IsEditable`. |
| `ShowValue` | `bool` | `true` | Whether to display numeric coordinate text readout below the pad. |
| `CustomLabel` | `string` | `null` | Custom label prefix displayed above the joystick pad. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class TwinStickController : MonoBehaviour
{
    [Header("Aiming Reticle Direction")]
    [XYPadController(
        padSize: 100f, 
        min: -1f, 
        max: 1f, 
        PuckColor = "#38BDF8", 
        SpringReturn = true, 
        CustomLabel = "Aim Vector"
    )]
    public Vector2 rightStickAimDirection = Vector2.zero;

    [Header("Material UV Pan Offsets")]
    [XYPadController(min: 0f, max: 10f, padSize: 75f, PuckColor = "#10B981")]
    public List<Vector2> materialScrollTiling = new List<Vector2> { Vector2.one, new Vector2(2f, 2f) };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Arranges cleanly inside control panels, input settings, and flight consoles. |
| Collections (`List<Vector2>`) | Supported | Implements `ICollectionElementAttribute` for multiple Vector2 touchpad controllers. |
| `[ReadOnly]` | Supported | Disables dragging while displaying live 2D coordinate puck telemetry. |
