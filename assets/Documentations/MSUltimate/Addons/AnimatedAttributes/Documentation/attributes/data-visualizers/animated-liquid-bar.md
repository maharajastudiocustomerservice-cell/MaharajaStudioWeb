# [AnimatedLiquidBar]

> Renders a progress bar with undulating fluid wave ripples, rising micro-bubbles, and interactive level scrubbing.

---

## 1. Overview & Value Proposition

**What it does:**
`[AnimatedLiquidBar]` elevates numeric progress bars into an organic liquid container. The fill level features procedural surface waves (`WaveAmplitude`, `WaveSpeed`), a lighter surface wave crest (`SurfaceWaveColor`), and gentle rising effervescent bubbles. Users can click and drag horizontally on the fluid container to scrub levels interactively.

**The Problem:**
Alchemical flasks, potion volumes, fuel tanks, stamina reservoirs, and water tanks feel static when represented by rigid, mechanical progress bars. Standard bars fail to evoke the presence of fluid dynamics.

**The Solution:**
Decorating liquid or resource properties with `[AnimatedLiquidBar]`:
- **Fluid Wave Simulation:** Sine-wave surface crests ripple continuously to simulate organic fluid motion.
- **Surface Crest Highlights:** A two-tone fluid aesthetic with a brighter wave foam line (`SurfaceWaveColor`) on top of the main body (`LiquidColor`).
- **Interactive Drag Scrubbing:** Drag directly along the fluid bar (`IsEditable = true`) to fill or deplete fluid levels.
- **Dynamic Capacity Limits:** Bind `DynamicMaxValueMember` and `DynamicMinValueMember` for expandable flasks or tanks.
- **Collection Cascading:** Implements `ICollectionElementAttribute` for potion belts or chemical multi-tank inventories.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class PotionItem : MonoBehaviour
{
    [AnimatedLiquidBar(min: 0f, max: 100f, liquidColor: "#10B981")]
    public float remainingStamina = 78f;
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
public AnimatedLiquidBarAttribute(
    float min = 0f, 
    float max = 100f, 
    string liquidColor = "#06B6D4"
)

public AnimatedLiquidBarAttribute(
    string dynamicMaxValueMember, 
    string liquidColor = "#06B6D4"
)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `min` | `float` | `0f` | Minimum value represented by an empty liquid container. |
| `max` | `float` | `100f` | Maximum value represented by a full liquid container. |
| `liquidColor` | `string` | `"#06B6D4"` | Hex color string for the body of the liquid. |
| `dynamicMaxValueMember` | `string` | — | Member name providing dynamic maximum liquid capacity. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MinValue` | `float` | `0f` | Minimum capacity threshold. |
| `MaxValue` | `float` | `100f` | Maximum capacity threshold. |
| `DynamicMaxValueMember` | `string` | `null` | Member name returning dynamic upper bound. |
| `DynamicMinValueMember` | `string` | `null` | Member name returning dynamic lower bound. |
| `BarHeight` | `float` | `18f` | Height in pixels of the liquid container bar. |
| `LiquidColor` | `string` | `"#06B6D4"` | Hex color string for the main liquid body. |
| `SurfaceWaveColor` | `string` | `"#67E8F9"` | Hex color string for the surface wave crest and foam highlight. |
| `WaveSpeed` | `float` | `3f` | Oscillation frequency of the liquid ripples in cycles per second. |
| `WaveAmplitude` | `float` | `2.5f` | Height in pixels of the vertical wave crest peaks. |
| `DrawInputField` | `bool` | `true` | Whether to draw the standard serialized property field above the bar. |
| `ShowInputField` | `bool` | `true` | Alias for `DrawInputField`. |
| `IsEditable` | `bool` | `true` | Whether dragging across the bar scrubs the liquid volume. |
| `Interactive` | `bool` | `true` | Alias for `IsEditable`. |
| `CustomLabel` | `string` | `null` | Custom text label overlaid across the liquid bar. |
| `ShowValue` | `bool` | `true` | Whether to display numeric values in the overlay text. |
| `ShowPercentage` | `bool` | `false` | Whether to display percentage in the overlay text. |
| `LabelColor` | `string` | `"#FFFFFF"` | Hex color string for overlaid text label. |
| `LabelFontSize` | `int` | `11` | Font size in pixels for overlaid text label. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class AlchemistVessel : MonoBehaviour
{
    [Header("Flask Capacity")]
    public float maxFlaskCapacity = 250f;

    [Header("Elixir of Arcane Intellect")]
    [AnimatedLiquidBar(
        nameof(maxFlaskCapacity), 
        liquidColor: "#8B5CF6", 
        SurfaceWaveColor = "#C084FC",
        WaveSpeed = 2.5f,
        WaveAmplitude = 3.0f,
        BarHeight = 24f,
        CustomLabel = "MANA ELIXIR",
        ShowValue = true
    )]
    public float currentFluidVolume = 195f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Fluid bars fit neatly into inventory cards and crafting panels. |
| `[ValueChangeFlash]` | Stacking | Combines liquid ripples with momentary highlight flashes on refills. |
| Arrays & Lists | Supported | Implements `ICollectionElementAttribute` for multiple potion vials or flasks. |
