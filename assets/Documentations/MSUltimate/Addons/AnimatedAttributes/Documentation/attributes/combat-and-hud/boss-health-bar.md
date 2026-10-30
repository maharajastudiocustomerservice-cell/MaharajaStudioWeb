# [BossHealthBar]

> Renders an arcade boss health bar with a lingering damage ghost bar, multi-phase dividers, and interactive click-drag scrubbing.

---

## 1. Overview & Value Proposition

**What it does:**
`[BossHealthBar]` renders an authentic, multi-layered boss health bar directly inside the Unity Inspector. When health decreases, an underlying amber "ghost bar" lingers at the previous health level and slowly decays (`GhostDecaySpeed`), mirroring fighting game and souls-like visual mechanics. The bar supports custom phase thresholds (`PhaseThresholds`), boss titles (`BossName`), and interactive mouse scrubbing.

**The Problem:**
Balancing boss encounters, phase transitions, and damage thresholds requires constantly adjusting health values. Standard numeric input fields fail to convey the visual impact of phase triggers and health pacing.

**The Solution:**
Decorating boss health fields with `[BossHealthBar]`:
- **Dual-Layer Ghost Damage Bar:** Immediately highlights recent damage decrements with decaying ghost trails.
- **Phase Threshold Dividers:** Visual notch markers split the health bar into phases (e.g., `0.75f, 0.5f, 0.25f`) for staged boss mechanics.
- **Dynamic Upper Bounds:** Support dynamic max health scaling via `DynamicMaxHealthMember` for scaling encounters.
- **Interactive Drag Editing:** Scrub health percentages seamlessly with mouse dragging (`IsEditable = true`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class BossEncounter : MonoBehaviour
{
    [BossHealthBar(maxHealth: 5000f, barHeight: 26f, BossName = "Ignis, Lord of Cinders")]
    public float currentHealth = 3500f;
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
public BossHealthBarAttribute(float maxHealth = 100f, float barHeight = 22f)

public BossHealthBarAttribute(string dynamicMaxHealthMember, float barHeight = 22f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `maxHealth` | `float` | `100f` | Maximum health capacity represented by a 100% full bar. |
| `dynamicMaxHealthMember` | `string` | — | Name of a member returning dynamic maximum health capacity. |
| `barHeight` | `float` | `22f` | Vertical height in pixels of the boss health bar container. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MaxHealth` | `float` | `100f` | Static maximum health represented by a full bar. |
| `DynamicMaxHealthMember` | `string` | `null` | Name of a member returning dynamic max health. |
| `BarHeight` | `float` | `22f` | Vertical height of the health bar in pixels. |
| `BarColor` | `string` | `"#EF4444"` | Hex color string for the active foreground health fill. |
| `GhostColor` | `string` | `"#FBBF24"` | Hex color string for the decaying damage ghost bar. |
| `BackgroundColor` | `string` | `"#1E1B4B"` | Hex color string for the empty health bar background trough. |
| `GhostDecaySpeed` | `float` | `0.5f` | Decay speed multiplier for the lingering ghost damage bar. |
| `DrawInputField` | `bool` | `true` | Whether to draw standard numeric input field above the bar. |
| `ShowInputField` | `bool` | `true` | Alias for `DrawInputField`. |
| `IsEditable` | `bool` | `true` | Whether the health bar is interactively scrubbable via mouse click-drag. |
| `Interactive` | `bool` | `true` | Alias for `IsEditable`. |
| `BossName` | `string` | `null` | Boss title/name string overlaid across the health bar. |
| `ShowHealthText` | `bool` | `true` | Whether to display numeric current/max health readout overlay. |
| `PhaseThresholds` | `float[]` | `null` | Normalized threshold markers (e.g., `{ 0.75f, 0.5f, 0.25f }`) dividing phases. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class DragonBoss : MonoBehaviour
{
    [Header("Encounter Max Health")]
    public float maximumDragonHealth = 12000f;

    [Header("Active Boss Health")]
    [BossHealthBar(
        nameof(maximumDragonHealth), 
        barHeight: 28f, 
        BossName = "Ancient Wyrm of the Peak",
        BarColor = "#DC2626",
        GhostColor = "#F59E0B",
        GhostDecaySpeed = 0.4f,
        PhaseThresholds = new float[] { 0.70f, 0.35f }
    )]
    public float currentHealth = 8400f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Integrates cleanly inside encounter panels and boss profile sections. |
| `[ValueChangeFlash]` | Stacking | Flashes accent frames when damage values mutate programmatically. |
| Arrays & Lists | Supported | Implements `ICollectionElementAttribute` for multiple boss parts or multi-target encounters. |
