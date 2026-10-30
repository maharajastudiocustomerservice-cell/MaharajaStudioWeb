# [HierarchyBreathingColorText]

> Smoothly interpolates hierarchy label text color between two hues in a continuous breathing sine wave.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyBreathingColorText]` continuously blends the GameObject's label text between a `PrimaryColor` and a `SecondaryColor` using smooth sinusoidal interpolation (`Mathf.Sin(EditorApplication.timeSinceStartup * Speed)`).

**The Problem:**
Static color labels in the hierarchy can become visually monotonous, while aggressive kinetic animations (such as shaking, bouncing, or glitching) can be distracting for systems that simply require ambient, calm emphasis.

**The Solution:**
Decorating components with `[HierarchyBreathingColorText]`:
- **Ambient Chromatic Pulsing:** Gently shifts the text hue back and forth between two curated colors (e.g., cyan to magenta, or amber to deep orange) without distracting character displacement.
- **Adjustable Breathing Cadence:** Control how fast the color transition oscillates (`Speed = 1.5f`).
- **Bold Weight Support:** Enhances color legibility across both dark and light editor themes.
- **Zero Physics & Clean Rendering:** Uses standard Unity GUI label drawing with zero scene overhead.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyBreathingColorText(PrimaryColor = "#00D2FF", SecondaryColor = "#FF007F", Speed = 2.0f)]
public class AmbientLightingManager : MonoBehaviour
{
    public Light sunLight;
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
| **Render Engine** | `HierarchyBreathingColorTextRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyBreathingColorTextAttribute()
```

- Standard parameterless constructor. Color endpoints and oscillation speeds are set via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `PrimaryColor` | `string` | `"#00D2FF"` | Hex color representing the starting hue of the breathing cycle. |
| `SecondaryColor` | `string` | `"#FF007F"` | Hex color representing the target hue of the breathing cycle. |
| `Speed` | `float` | `1.5f` | Oscillation frequency of the sine-wave color transition. |
| `Bold` | `bool` | `true` | Whether to render the label characters with bold font weight. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether color breathing continues during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row decorations. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyBreathingColorText(
    PrimaryColor = "#F59E0B", 
    SecondaryColor = "#EF4444", 
    Speed = 1.2f, 
    Bold = true)]
public class LavaHazardZone : MonoBehaviour
{
    [Header("Hazard Configuration")]
    public float damagePerSecond = 50f;
    public float heatBuildupRate = 12.5f;
    public ParticleSystem steamPlume;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyGlow]`** | High | Combines color breathing with an ambient background halo for glowing atmospheric objects. |
| **`[HierarchyTooltip]`** | High | Display detailed status warnings and contact damage parameters on hover. |
| **`[HierarchyTextColor]`** | Incompatible | Do not combine with static text coloring attributes as both target the primary label color. |
| **`[HierarchyBreadcrumb]`** | High | Works alongside hierarchy path breadcrumbs without visual conflicts. |
