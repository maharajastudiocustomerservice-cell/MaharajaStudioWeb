# [CooldownProgressRing]

> Renders a circular progress ring that visually winds down as a cooldown timer ticks, with dynamic duration bindings and collection support.

---

## 1. Overview & Value Proposition

**What it does:**
`[CooldownProgressRing]` replaces standard linear progress bars with an elegant radial cooldown indicator. As a cooldown value counts down or recharges, the circular arc sweeps smoothly from 0 to 360 degrees, rendered in customizable foreground (`RingColor`) and background (`BackgroundColor`) colors. The diameter (`RingSize`) is fully adjustable, dynamic upper durations can be bound via reflection (`DynamicMaxDurationMember`), and circular dragging allows interactive scrubbing.

**The Problem:**
Linear bars require significant horizontal layout width and look bulky when grouped beside skill icons, spell matrices, or weapon loadouts. Displaying dozens of cooldown timers in compact inspector cards causes clutter.

**The Solution:**
Decorating timer fields with `[CooldownProgressRing]`:
- **Radial Cooldown Arc:** Draws a compact circular ring that winds clockwise or counter-clockwise as cooldowns expire.
- **Dynamic Capacity Binding:** Binds maximum cooldown duration dynamically via `dynamicMaxDurationMember`.
- **Flexible Numeric Overlays:** Toggle numeric time text (`ShowValue`) or percentage readouts (`ShowPercentage`).
- **Interactive Radial Scrubbing:** Click or drag around the circle (`IsEditable = true`) to scrub cooldown seconds in real time.
- **Collection Cascading:** Implements `ICollectionElementAttribute` for lists and arrays of ability cooldown timers.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class AbilityCooldowns : MonoBehaviour
{
    [CooldownProgressRing(maxDuration: 12f, ringColor: "#3B82F6")]
    public float dashCooldownRemaining = 8.5f;
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
public CooldownProgressRingAttribute(float maxDuration = 10f, string ringColor = "#3B82F6")

public CooldownProgressRingAttribute(string dynamicMaxDurationMember, string ringColor = "#3B82F6")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `maxDuration` | `float` | `10f` | Maximum cooldown duration in seconds (100% full ring). |
| `dynamicMaxDurationMember` | `string` | — | Name of a member providing dynamic upper duration capacity. |
| `ringColor` | `string` | `"#3B82F6"` | Hex color string for the active circular progress arc (defaults to Blue). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MaxDuration` | `float` | `10f` | Maximum duration represented by a complete circular arc. |
| `DynamicMaxDurationMember` | `string` | `null` | Name of a member providing dynamic max duration. |
| `RingSize` | `float` | `22f` | Diameter of the circular ring in pixels. |
| `RingColor` | `string` | `"#3B82F6"` | Hex color string for the progress arc. |
| `BackgroundColor` | `string` | `"#1E293B"` | Hex color string for the empty background ring track. |
| `DrawInputField` | `bool` | `true` | Whether to draw the standard serialized property input field. |
| `ShowInputField` | `bool` | `true` | Alias for `DrawInputField`. |
| `IsEditable` | `bool` | `true` | Whether the progress ring can be dynamically scrubbed via mouse click-drag. |
| `Interactive` | `bool` | `true` | Alias for `IsEditable`. |
| `CustomLabel` | `string` | `null` | Custom label prefix displayed beside the ring. |
| `ShowValue` | `bool` | `true` | Whether to display the numeric cooldown value beside the ring. |
| `ShowPercentage` | `bool` | `false` | Whether to display percentage text instead of raw seconds. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class SpellcasterGrimoire : MonoBehaviour
{
    [Header("Ultimate Spell Cooldown")]
    public float meteorCooldownMax = 45f;

    [CooldownProgressRing(
        nameof(meteorCooldownMax), 
        ringColor: "#EF4444", 
        RingSize = 32f, 
        ShowPercentage = true, 
        CustomLabel = "Meteor Strike"
    )]
    public float meteorCooldownTimer = 18f;

    [Header("Equipped Ability Slots")]
    [CooldownProgressRing(maxDuration: 8f, ringColor: "#10B981", RingSize = 24f)]
    public List<float> spellSlotCooldowns = new List<float> { 2f, 0f, 6.5f, 4f };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Fits into skill matrices, hero loadouts, and compact inventory cards. |
| Collections (`List<float>`) | Supported | Implements `ICollectionElementAttribute` for multiple radial cooldown rings. |
| `[ThresholdSpikeFlash]` | Stacking | Triggers milestone flashes when cooldown rings reach 0 seconds. |
