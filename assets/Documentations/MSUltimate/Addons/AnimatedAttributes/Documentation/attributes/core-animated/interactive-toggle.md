# [InteractiveToggle]

> Replaces standard boolean checkboxes with an animated iOS-style sliding switch toggle featuring smooth knob transitions and custom track styling.

---

## 1. Overview & Value Proposition

**What it does:**
Transforms clunky standard Unity boolean checkboxes into modern, tactile, animated sliding switch toggles (inspired by modern mobile OS and high-end web design). The knob slides smoothly between active (`TrackColorOn`) and inactive (`TrackColorOff`) states with spring easing and click feedback.

**The Problem:**
Native Unity boolean checkboxes are small (16x16 pixels), hard to click accurately on high-DPI displays, and feel outdated compared to modern sliding switches.

**The Solution:**
Add `[InteractiveToggle]` to any boolean field:
- **Tactile Sliding Animation:** The switch knob slides smoothly with configurable duration (`TransitionDuration = 250ms`).
- **High-DPI Hit Area:** Larger pill shape (`ToggleWidth = 40px`) ensures effortless clicking.
- **Custom Theming:** Independent track colors for active/inactive states and knob tinting.
- **Collection Elements:** Replaces boolean check elements inside arrays or lists individually (`ICollectionElementAttribute`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class AudioOptions : MonoBehaviour
{
    [InteractiveToggle(TrackColorOn = "#007AFF", ToggleWidth = 44f)]
    public bool enableSpatialAudio = true;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `bool` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public InteractiveToggleAttribute()
```

*Attribute initializes with standard green-on-gray iOS switch styling; customize properties via object initializers.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `TrackColorOn` | `string` | `"#34C759"` | Hex color string for the switch track when enabled (`true`). |
| `TrackColorOff` | `string` | `"#E5E5EA"` | Hex color string for the switch track when disabled (`false`). |
| `KnobColor` | `string` | `"#FFFFFF"` | Hex color string for the sliding switch knob. |
| `TransitionDuration` | `float` | `250f` | Sliding animation duration in milliseconds. |
| `ToggleWidth` | `float` | `40f` | Total width of the toggle switch in pixels. |
| `IsEditable` | `bool` | `true` | Whether the toggle switch is interactively clickable. |
| `Interactive` | `bool` | `true` | Alias for `IsEditable`. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class GameRenderSettings : MonoBehaviour
{
    [Header("Post-Processing Toggles")]
    [InteractiveToggle(TrackColorOn = "#2ecc71", TrackColorOff = "#34495e", ToggleWidth = 46f)]
    public bool enableBloom = true;

    [InteractiveToggle(TrackColorOn = "#e74c3c", TrackColorOff = "#2c3e50")]
    public bool motionBlurActive = false;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Sliding switches sit cleanly within cards and group containers. |
| `ICollectionElement` | Supported | Converts `List<bool>` or `bool[]` elements into individual sliding toggles. |
| Category | PrimaryDrawer | Completely replaces the default checkbox drawer for boolean properties. |
