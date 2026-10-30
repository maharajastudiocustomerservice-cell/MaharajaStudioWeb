# [HierarchyFlash]

> Briefly flashes the hierarchy row with an easing light strobe when a monitored boolean field transitions from false to true.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyFlash]` provides transient visual feedback for discrete scene events. Handled by `HierarchyFlashRenderer`, it monitors a boolean trigger flag. When the flag flips from `false` to `true`, the entire hierarchy row (`FullRowFlash = true`) or a right-side indicator band (`BandWidth = 80f`) flashes with sudden peak luminescence (`FlashColor = "#FF5555"`, `AttackTime = 0.05f`) before smoothly decaying away over time (`Duration = 0.8f`, `FadeToColor = "#FF555500"`). Built-in cooldowns (`CooldownTime = 0.3f`) and reset checks (`RequireReset = true`) prevent strobe spam during continuous triggers.

**The Problem:**
Event-driven behaviors—such as trigger volumes firing, hitscan shots connecting, dialogue cues triggering, or achievement unlock pulses—occur in single frames. Because boolean state flips happen and reset in milliseconds, developers watching the Inspector or Scene view completely miss whether an event actually fired.

**The Solution:**
Decorating event trigger booleans with `[HierarchyFlash]`:
- **Instant Optical Strobe Feedback:** Flashes the hierarchy row the exact frame an event fires, holding attention with a gentle fadeout curve.
- **Microsecond Event Capture:** Never miss single-frame pulses that reset before human eyes can catch them in standard Inspector checkboxes.
- **Configurable Flash Dynamics:** Adjust peak flash hues (crimson for hits, gold for pickups, electric cyan for portals) and duration decay.
- **Anti-Spam Cooldown Guards:** Built-in attack/decay easing and cooldown timers maintain smooth editor rendering even during rapid fire.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class ProximityMineTrigger : MonoBehaviour
{
    [HierarchyFlash(FlashColor = "#EF4444", Duration = 1.0f)]
    public bool isDetonated = false;

    public float explosionRadiusMeters = 8.5f;
    public int damageAmount = 250;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyFlashRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyFlashAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `FlashColor` | `string` | `"#FF5555"` | Hex color of the flash overlay at peak strobe intensity. |
| `FadeToColor` | `string` | `"#FF555500"` | Hex color (with alpha) that the flash fades into as it expires. |
| `Duration` | `float` | `0.8f` | Total duration of the flash effect in seconds. |
| `AttackTime` | `float` | `0.05f` | Attack phase duration in seconds before beginning exponential decay. |
| `RequireReset` | `bool` | `true` | When true, the field must return to `false` before triggering another flash. |
| `CooldownTime` | `float` | `0.3f` | Minimum cooldown in seconds between consecutive flash triggers. |
| `FullRowFlash` | `bool` | `true` | Whether the flash spans the entire row width or only a right-side band. |
| `BandWidth` | `float` | `80f` | Width of the flash band in pixels when `FullRowFlash` is false. |
| `XOffset` | `float` | `0f` | Horizontal offset in pixels from the right margin. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the flash strobe animation operates in Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class TurretTargetingSensor : MonoBehaviour
{
    [Header("Detection State")]
    [Tooltip("Flashes bright yellow when the sensor locks onto an enemy target.")]
    [HierarchyFlash(
        FlashColor = "#FBBF24", 
        FadeToColor = "#FBBF2400", 
        Duration = 0.6f, 
        AttackTime = 0.04f, 
        CooldownTime = 0.25f, 
        FullRowFlash = true)]
    public bool hasAcquiredTarget = false;

    [Header("Targeting Telemetry")]
    public Transform currentLockedTarget;
    public float targetDistanceMeters = 24.5f;
    public bool isFiringLaser = false;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyFieldAlert]`** | High | Use `HierarchyFlash` for momentary events and `HierarchyFieldAlert` for persistent error states. |
| **`[HierarchyHighlight]`** | High | The flash strobe superimposes cleanly over static row background colors. |
| **Play Mode Testing** | High | Essential for gameplay QA to visually confirm hitboxes, triggers, and audio event firings. |
| **Performance** | High | Internal timer evaluates via `EditorApplication.timeSinceStartup` without GC allocations. |
