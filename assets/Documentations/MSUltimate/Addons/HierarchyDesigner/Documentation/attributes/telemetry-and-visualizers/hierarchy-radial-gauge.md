# [HierarchyRadialGauge]

> Renders a circular donut progress ring for percentages, stamina, heat, or energy on the hierarchy row.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyRadialGauge]` transforms numeric fields into a compact, circular donut progress ring directly on the hierarchy row. Driven by `HierarchyRadialGaugeRenderer`, it computes the fill ratio between `MinValue` and `MaxValue`, rendering a full 360° background guide track (`BackgroundColor = "#2C3E50"`) and an active radial progress arc (`RingColor = "#00D2FF"`, `Thickness = 2.5f`).

**The Problem:**
Linear horizontal progress bars can consume significant horizontal space on the hierarchy row, competing with long GameObject names or adjacent status icons. Circular radial meters provide the same telemetry in a compact, square footprint (`12x12px`), maximizing usable hierarchy width.

**The Solution:**
Decorating numeric fields or properties with `[HierarchyRadialGauge]`:
- **Ultra-Compact Donut Ring:** Fits neatly on any hierarchy row without crowding text or other icons.
- **Normalized Range Mapping:** Normalizes values between custom `MinValue` and `MaxValue` (e.g., `0f` to `100f`).
- **Smooth Arc Drawing:** Uses procedural anti-aliased radial arc geometry for crisp rendering.
- **Play Mode Telemetry:** Updates smoothly every frame as energy, stamina, or heat levels change during gameplay.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class PlayerStamina : MonoBehaviour
{
    [HierarchyRadialGauge(MinValue = 0f, MaxValue = 100f, RingColor = "#38BDF8")]
    public float currentStamina = 75f;
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
| **Render Engine** | `HierarchyRadialGaugeRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyRadialGaugeAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MinValue` | `float` | `0f` | Minimum value of the gauge range (0% fill). |
| `MaxValue` | `float` | `100f` | Maximum value of the gauge range (100% fill / 360° arc). |
| `RingColor` | `string` | `"#00D2FF"` | Hex color of the active progress ring arc. |
| `BackgroundColor` | `string` | `"#2C3E50"` | Hex background color of the full 360° guide track. |
| `Radius` | `float` | `6f` | Outer radius of the radial gauge in pixels. |
| `Thickness` | `float` | `2.5f` | Line thickness of the radial ring in pixels. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the radial gauge remains visible and updates during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class JetpackThruster : MonoBehaviour
{
    [Header("Fuel Telemetry")]
    [HierarchyRadialGauge(
        MinValue = 0f, 
        MaxValue = 250f, 
        RingColor = "#F59E0B", 
        BackgroundColor = "#1E293B", 
        Radius = 7f, 
        Thickness = 3f, 
        XOffset = 6f)]
    public float currentFuel = 180f;

    public bool isThrusterFiring = false;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyCooldownRing]`** | Complementary | Use `HierarchyCooldownRing` for countdown timers and `HierarchyRadialGauge` for resource meters. |
| **`[HierarchyStatusDot]`** | High | Place status dots next to radial gauges for dual state + resource percentage visualization. |
| **`[HierarchyProgressBar]`** | Alternative | Use radial gauges when horizontal row space is tight, and horizontal bars when numerical labels are needed. |
| **Numeric Member Types** | High | Works directly with `float`, `int`, and `double` fields and properties. |
