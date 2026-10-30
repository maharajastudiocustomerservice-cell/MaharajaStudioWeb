# [HierarchyCooldownRing]

> Displays a circular radial cooldown ring directly on the hierarchy row for timed abilities, recharge meters, or weapon timers.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyCooldownRing]` renders a sleek circular radial progress ring directly on the hierarchy row for numeric cooldown or timer fields. Driven by `HierarchyCooldownRingRenderer`, it calculates the elapsed ratio (`current / MaxDuration`) and draws a background guide ring alongside a smoothly sweeping active radial arc (`DrawRadialArc`). It supports customizable ring colors (`RingColor = "#FF9F43"`), background track tints (`BackgroundColor = "#341F97"`), radius sizes, and horizontal offsets.

**The Problem:**
Watching cooldown timers, ability recharges, spawn delays, or spell cycle times during gameplay sessions usually requires watching in-game UI canvases or reading raw float values inside the Inspector. When balancing 10 different spells or weapon cooldowns simultaneously, developers need glanceable circular ring telemetry in the hierarchy.

**The Solution:**
Decorating numeric fields or properties with `[HierarchyCooldownRing]`:
- **Radial Sweeping Gauge:** Visualizes cooldown progress as a smooth radial arc sweeping from 0° to 360°.
- **Compact Hierarchy Footprint:** Uses a tiny radius (`Radius = 6f`) that fits neatly alongside object names without cluttering rows.
- **Configurable Durations:** Set fixed maximum durations (`MaxDuration = 10f`) to normalize progress calculation.
- **Play Mode & Edit Mode Support:** Updates smoothly every frame during active gameplay or editor testing.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class SpellCaster : MonoBehaviour
{
    [HierarchyCooldownRing(MaxDuration = 5.0f, RingColor = "#38BDF8")]
    public float fireballCooldown = 3.2f;
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
| **Render Engine** | `HierarchyCooldownRingRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyCooldownRingAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MaxDuration` | `float` | `10f` | Maximum cooldown duration in seconds used to calculate the 360° fill ratio. |
| `RingColor` | `string` | `"#FF9F43"` | Hex color of the sweeping cooldown arc. |
| `BackgroundColor` | `string` | `"#341F97"` | Hex color of the full 360° background track ring. |
| `Radius` | `float` | `6f` | Radius of the radial ring in pixels. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the radial ring remains visible and updating during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class TurretDefenseController : MonoBehaviour
{
    [Header("Weapon Systems")]
    public float reloadTimeSeconds = 4.5f;

    [HierarchyCooldownRing(
        MaxDuration = 4.5f, 
        RingColor = "#F97316", 
        BackgroundColor = "#1E293B", 
        Radius = 7f, 
        XOffset = 6f)]
    public float currentReloadTimer = 2.1f;

    public int ammoCount = 30;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyRadialGauge]`** | Related | Use `HierarchyCooldownRing` for time/cooldown counters and `HierarchyRadialGauge` for percentages/health. |
| **`[HierarchyStatusDot]`** | High | Pair cooldown rings with status dots to indicate when abilities are ready (green) vs on cooldown (amber). |
| **`[HierarchyToggle]`** | High | Combine with boolean toggles to manually trigger or freeze cooldown loops during testing. |
| **Numeric Member Types** | High | Supports `float`, `int`, and `double` fields and properties. |
