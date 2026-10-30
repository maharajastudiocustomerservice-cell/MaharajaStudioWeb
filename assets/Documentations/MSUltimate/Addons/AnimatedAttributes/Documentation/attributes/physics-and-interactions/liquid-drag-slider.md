# [LiquidDragSlider]

> Deforms the slider thumb into a liquid teardrop in the drag direction with viscous surface tension, snapping back into a droplet on release.

---

## 1. Overview & Value Proposition

**What it does:**
`[LiquidDragSlider]` delivers fluid, organic tactile feedback for numeric values in the Unity Inspector. When scrubbing the slider rapidly, the circular thumb handle deforms and stretches along the drag vector into an elongated liquid teardrop up to a maximum stretch factor (`MaxStretch`). Upon releasing the mouse, surface tension snaps the teardrop back into a resting droplet with a smooth fluid wobble. It supports dynamic bounds, companion numeric typing, and collection cascading.

**The Problem:**
Most sliders in developer tools look like rigid geometric widgets. When tuning organic, viscous, or fluid systems—such as slime elasticity, water volume, potion viscosity, fuel reserves, or paint density—rigid UI handles fail to evoke the physical property being configured.

**The Solution:**
Decorating numeric fields with `[LiquidDragSlider]`:
- **Liquid Teardrop Deformation:** Dynamically deforms the handle proportional to drag velocity and direction.
- **Surface Tension Snapping:** Springs back into a resting sphere with subtle fluid damping upon cursor release.
- **Dynamic Capacity Limits:** Bind maximum limits dynamically via `dynamicMaxValueMember` or `DynamicMinValueMember`.
- **Integrated Precision Input Field:** Includes a companion numeric text field (`DrawInputField = true`) for direct manual entry.
- **Collection Cascading:** Implements `ICollectionElementAttribute` for lists and arrays of fluid parameters.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class SlimePhysics : MonoBehaviour
{
    [LiquidDragSlider(min: 0f, max: 100f, thumbColor: "#10B981")]
    public float slimeViscosity = 65f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `int`, `float`, `double`, `long`, `short`, `byte` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Collection Element Support** | Yes (`ICollectionElementAttribute`) |

---

## 4. Constructors & Parameters

```csharp
public LiquidDragSliderAttribute(float min = 0f, float max = 100f, string thumbColor = "#3B82F6")

public LiquidDragSliderAttribute(string dynamicMaxValueMember, string thumbColor = "#3B82F6")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `min` | `float` | `0f` | Minimum slider value range limit. |
| `max` | `float` | `100f` | Maximum slider value range limit. |
| `dynamicMaxValueMember` | `string` | — | Name of a member providing dynamic upper range capacity. |
| `thumbColor` | `string` | `"#3B82F6"` | Hex color string for the liquid thumb handle (defaults to Blue). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MinValue` | `float` | `0f` | Minimum slider value. |
| `MaxValue` | `float` | `100f` | Maximum slider value. |
| `DynamicMaxValueMember` | `string` | `null` | Name of a member providing dynamic maximum bound. |
| `DynamicMinValueMember` | `string` | `null` | Name of a member providing dynamic minimum bound. |
| `ThumbColor` | `string` | `"#3B82F6"` | Hex color string for the liquid thumb handle. |
| `MaxStretch` | `float` | `1.4f` | Maximum elongation factor when dragging rapidly. |
| `DrawInputField` | `bool` | `true` | Whether to draw companion numeric text field for precise typing. |
| `ShowInputField` | `bool` | `true` | Alias for `DrawInputField`. |
| `IsEditable` | `bool` | `true` | Whether the slider is interactive. |
| `Interactive` | `bool` | `true` | Alias for `IsEditable`. |
| `CustomLabel` | `string` | `null` | Custom label prefix displayed beside the slider. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class AlchemyLabCauldron : MonoBehaviour
{
    [Header("Dynamic Fluid Volume")]
    public float maximumCauldronCapacityLiters = 500f;

    [Header("Viscous Liquid Potion")]
    [LiquidDragSlider(
        nameof(maximumCauldronCapacityLiters), 
        thumbColor: "#8B5CF6", 
        MaxStretch = 1.6f, 
        CustomLabel = "Elixir Level"
    )]
    public float currentBrewVolume = 320f;

    [Header("Ingredient Reagents")]
    [LiquidDragSlider(0f, 100f, thumbColor: "#06B6D4")]
    public List<float> reagentConcentrations = new List<float> { 25f, 40f, 85f };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[FloatingBubbles]` | Stacking | Pairs with background floating bubbles for ultimate alchemical/aquatic interfaces. |
| `[BoxGroup]` | Supported | Liquid handle deforms smoothly without clipping outside group margins. |
| Collections (`List<float>`) | Supported | Implements `ICollectionElementAttribute` for multiple liquid sliders. |
