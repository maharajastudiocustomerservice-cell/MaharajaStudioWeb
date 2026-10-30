# [TimeSpanSlider]

> Renders numeric duration fields as an interactive time slider with human-readable formatting (HH:mm:ss, mm:ss, ss.fff) and preset shortcuts.

---

## 1. Overview & Value Proposition

**What it does:**
Renders raw second values (`float`, `double`, `int`, `long`) as an interactive duration slider displaying formatted time readouts (such as `01m 45s`, `02:30:00`, or `12.500s`). Supports custom color accents, stepping, numeric input boxes, and quick preset buttons.

**The Problem:**
Entering time intervals—such as 3600 seconds for a 1-hour buff, 90 seconds for a cooldown, or 0.25 seconds for a dodge roll window—using plain float or int fields is confusing. Designers have to mentally convert between minutes, hours, and seconds, frequently making conversion errors.

**The Solution:**
Add `[TimeSpanSlider]` to any duration field:
- **Human-Readable Formats:** Displays formatted duration strings like `02m 30s` alongside the slider track.
- **Multiple Format Modes:** `"Auto"`, `"HH:mm:ss"`, `"mm:ss"`, or high-precision milliseconds `"ss.fff"`.
- **Quick Preset Shortcuts:** Option to display 1-click preset buttons (`Min`, `50%`, `Max`) via `ShowQuickButtons = true`.
- **Visual Color Accents:** Customize the track and dragger accent color to match gameplay themes.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class AbilityCooldown : MonoBehaviour
{
    [TimeSpanSlider(0f, 120f)]
    public float cooldownSeconds = 15f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `float`, `double`, `int`, `long` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public TimeSpanSliderAttribute()
public TimeSpanSliderAttribute(float maxSeconds)
public TimeSpanSliderAttribute(float minSeconds, float maxSeconds)
public TimeSpanSliderAttribute(float minSeconds, float maxSeconds, string colorHex)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `maxSeconds` | `float` | `60f` | Maximum upper duration bound in seconds. |
| `minSeconds` | `float` | `0f` | Minimum lower duration bound in seconds. |
| `colorHex` | `string` | `null` | Hex accent color for the slider track and thumb. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MinSeconds` | `float` | `0f` | Minimum duration in seconds. |
| `MaxSeconds` | `float` | `60f` | Maximum duration in seconds. |
| `Step` | `float` | `0f` | Step increment for slider snapping (`0` = continuous). |
| `ColorHex` | `string` | `null` | Hex color code for track and thumb accents (e.g. `"#3498db"`). |
| `CustomLabel` | `string` | `null` | Field display label override. |
| `Format` | `string` | `null` | Format display mode (`"Auto"`, `"HH:mm:ss"`, `"mm:ss"`, `"ss.fff"`). |
| `ShowInputField` | `bool` | `false` | Displays a numeric text box alongside the slider. |
| `ShowQuickButtons` | `bool` | `false` | Displays quick shortcut buttons (`Min`, `50%`, `Max`). |
| `Order` | `int` | `0` | Drawing order priority in the inspector pipeline. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class RaidBossEncounter : MonoBehaviour
{
    [Header("Encounter Time Limit (HH:mm:ss Format)")]
    [TimeSpanSlider(60f, 1800f, "#e74c3c", Format = "HH:mm:ss", ShowInputField = true)]
    public float berserkTimer = 600f; // 10 minutes

    [Header("Invulnerability Window (Precision ms)")]
    [TimeSpanSlider(0.1f, 5.0f, "#f39c12", Format = "ss.fff", Step = 0.05f)]
    public float dodgeInvulnerabilityDuration = 0.35f;

    [Header("Potion Buff Duration (Presets Enabled)")]
    [TimeSpanSlider(10f, 300f, "#2ecc71", ShowQuickButtons = true)]
    public float healthRegenBuffDuration = 60f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Slider, formatting badge, and quick buttons fit smoothly inside group containers. |
| `[ShowIf]` | Supported | Conditionally reveals duration timers based on effect type. |
| `[ReadOnly]` | Supported | Renders the formatted time readout while preventing slider scrubbing. |
| `ICollectionElement` | Supported | Directly usable inside lists of stage wave timers (`List<float>`). |
