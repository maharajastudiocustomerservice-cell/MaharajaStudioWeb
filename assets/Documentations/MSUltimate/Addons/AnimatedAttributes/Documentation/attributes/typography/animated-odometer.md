# [AnimatedOdometer]

> Displays numeric fields with an animated rolling odometer reel effect, live value scrubbing, and luminous value-change glow.

---

## 1. Overview & Value Proposition

**What it does:**
`[AnimatedOdometer]` upgrades standard numeric input fields with an animated mechanical odometer ticker. Whenever a serialized numeric value changes—whether through script changes, Undo/Redo operations, or inspector editing—the displayed digits roll fluidly to the new value using a cubic ease-out curve over `RollDuration` (defaulting to 400ms). While rolling, the container frame blooms with a customizable luminous highlight (`GlowColor`, defaulting to sapphire `#3B82F6`). It supports interactive vertical drag scrubbing (`IsEditable`), prefix/suffix formatting (e.g. `"$"` or `" XP"`), and flexible companion input field rendering (`DrawInputField`).

**The Problem:**
Standard numeric float and int fields in Unity update instantly with zero visual transition. When inspecting fluctuating live values, balancing currency rates, or scrubbing health pools, static numbers make it difficult to perceive the direction and velocity of changes.

**The Solution:**
Decorating numeric fields with `[AnimatedOdometer]`:
- **Rolling Reel Simulation:** Numbers roll smoothly toward target values via a cubic ease-out interpolation function ($v = v_0 + \Delta v \cdot (1 - (1 - p)^3)$).
- **Interactive Drag Scrubbing:** Click and drag vertically over the odometer badge to rapidly increment or decrement values.
- **Dynamic Change Glow:** Emits a bright luminous glow around the badge container while values are in motion.
- **Prefix & Suffix Support:** Affixes currency symbols, units of measurement, or custom markers without altering the underlying raw numeric type.
- **Collection Cascading:** Full collection element support via `ICollectionElementAttribute` for integer and floating-point collections.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class PlayerWallet : MonoBehaviour
{
    [AnimatedOdometer(rollDuration: 500f, Prefix = "$", Suffix = " USD", GlowColor = "#10B981")]
    public float balance = 1250.75f;
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
| **Collection Element Support** | Yes (`ICollectionElementAttribute` for numeric types) |

---

## 4. Constructors & Parameters

```csharp
public AnimatedOdometerAttribute(float rollDuration = 400f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `rollDuration` | `float` | `400f` | Total duration of the roll animation in milliseconds. |

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `RollDuration` | `float` | `400f` | Rolling transition time in milliseconds. |
| `DigitHeight` | `float` | `18f` | Height in pixels allocated for the individual digit reel slot. |
| `GlowOnChange` | `bool` | `true` | When true, renders a luminous border bloom during active number rolls. |
| `GlowColor` | `string` | `"#3B82F6"` | Hex color string for the active reel glow bloom. |
| `Prefix` | `string` | `null` | Preceding marker text (e.g. `"$"` or `"LVL "`). |
| `Suffix` | `string` | `null` | Trailing unit text (e.g. `" pts"`, `" XP"`, or `" kg"`). |
| `DrawInputField` / `ShowInputField` | `bool` | `true` | When false, hides the companion text input field and displays the badge standalone. |
| `IsEditable` / `Interactive` | `bool` | `true` | Enables vertical mouse drag scrubbing on the odometer badge. |
| `CustomLabel` | `string` | `null` | Custom label string displayed beside standalone odometer displays. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class MMOProgressionManager : MonoBehaviour
{
    [Header("Player Economy")]
    [AnimatedOdometer(rollDuration: 600f, Prefix = "🪙 ", Suffix = " Gold", GlowColor = "#F59E0B")]
    public int goldCoins = 45000;

    [AnimatedOdometer(rollDuration: 400f, Prefix = "⭐ ", Suffix = " XP", GlowColor = "#8B5CF6")]
    public int currentExperience = 8920;

    [Header("Combat Telemetry")]
    [AnimatedOdometer(rollDuration: 300f, Suffix = " DPS", GlowColor = "#EF4444", IsEditable = false)]
    public float damagePerSecond = 1420.8f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[BoxGroup]` / `[HorizontalGroup]`** | High | Fits cleanly inside card containers; pairs especially well with dashboards and stat panels. |
| **`[ShowIf]` / `[EnableIf]`** | High | Resumes smooth rolling animation immediately when the host group becomes visible. |
| **`[Range]` / `[MinMaxSlider]`** | Caution | Setting `DrawInputField = false` while using standard range sliders may conflict with layout widths; keep companion input active when range clamping is desired. |
| **Numeric Collections** | High | Applies cleanly across `List<int>`, `float[]`, and numerical arrays using `ICollectionElementAttribute`. |
