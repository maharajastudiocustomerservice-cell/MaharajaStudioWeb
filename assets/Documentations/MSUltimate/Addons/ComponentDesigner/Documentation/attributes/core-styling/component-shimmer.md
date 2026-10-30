# [ComponentShimmer]

> Renders an animated diagonal shimmer sweep across the component card, creating a metallic luster and glassmorphism light reflection effect.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentShimmer]` gives component inspector cards a polished, high-end sheen. It animates an angled light reflection band (`Width = 60f`, `Angle = -20f`) sweeping steadily across the card surface (`Speed = 2.5f` seconds). Featuring customizable reflection color (`Color`, defaulting to white `#FFFFFF`), delicate ambient opacity (`Opacity = 0.08f`), and layer ordering (`Behind = true` $\to$ `ContentOverlay`, `Behind = false` $\to$ `BodyOverlay`), it imparts a premium glass or brushed metallic finish that brings cards to life without distracting developers.

**The Problem:**
Premium items, legendary loot tables, golden trophies, and master audio engines look flat and static in standard grayscale inspector forms. Without light reflections, luxury or high-tier game components fail to feel special.

**The Solution:**
Decorating prestige systems with `[ComponentShimmer]`:
- **Diagonal Reflection Sweep:** Animates an angled light glare sweeping smoothly across the card canvas.
- **Configurable Angle & Width:** Fine-tune beam rotation (`Angle = -20f`) and band thickness (`Width = 60f`) to fit any card dimensions.
- **Subtle Ambient Glare:** Low default opacity (`0.08f`) ensures labels and input values remain completely legible.
- **Zero Input Obstruction:** Absolutely positioned with `PickingMode.Ignore`, ensuring all standard Unity input controls remain completely responsive.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentShimmer(Color = "#FFD700", Width = 70f, Speed = 3.0f, Opacity = 0.12f)]
public class LegendaryLootDropTable : MonoBehaviour
{
    public string lootTableId = "TBL_MYTHIC_VAULT";
    public float legendaryDropProbability = 0.05f;
    public bool guaranteedDropOnBossKill = true;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ComponentDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Component Slot** | `ContentOverlay` (if `Behind = true`) or `BodyOverlay` (if `Behind = false`) |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentShimmerAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color` | `string` | `"#FFFFFF"` | Hex color string for the shimmer highlight sheen. |
| `Opacity` | `float` | `0.08f` | Transparency alpha of the shimmer bar (0.0 to 1.0). |
| `Width` | `float` | `60f` | Width in pixels of the traveling shimmer beam. |
| `Speed` | `float` | `2.5f` | Duration in seconds required for one complete horizontal sweep pass. |
| `Angle` | `float` | `-20f` | Diagonal tilt angle in degrees for the shimmer beam. |
| `Behind` | `bool` | `false` | When true, renders behind inspector controls; when false, renders on top. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#D97706", Width = 1.5f, Radius = 8f)]
[ComponentBackground("#1A1408", BorderRadius = 8f, Padding = 10f)]
[ComponentHeader("EXCALIBUR WEAPON LOGIC", Subtitle = "Holy Relic Blade Modifiers", BackgroundColor = "#2E1F0A", TitleColor = "#FEF3C7")]
[ComponentShimmer(Color = "#FDE68A", Width = 80f, Speed = 2.8f, Angle = -25f, Opacity = 0.14f, Behind = true)]
public class ExcaliburWeaponLogic : MonoBehaviour
{
    [Header("Holy Blade Stats")]
    public float radiantHolyDamage = 150f;
    public float smiteUndeadMultiplier = 3.5f;
    public bool isDivineShieldActive = true;

    [Header("Blessing Modifiers")]
    public float auraHealRadiusMeters = 8.0f;
    public float manaCostPerSwing = 15f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Dark backdrops dramatically heighten the perceived luster of the passing shine. |
| **`[ComponentBorder]`** | High | Gold, silver, or neon borders frame the shimmering card container cleanly. |
| **Inspector Controls** | High | `PickingMode.Ignore` ensures complete click-through transparency for all inspector controls. |
