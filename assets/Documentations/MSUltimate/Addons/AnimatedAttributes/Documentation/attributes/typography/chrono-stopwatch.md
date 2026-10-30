# [ChronoStopwatch]

> Displays an interactive digital chronograph stopwatch widget with real-time play/pause/reset controls directly within the inspector.

---

## 1. Overview & Value Proposition

**What it does:**
`[ChronoStopwatch]` turns raw numerical timing fields (representing seconds or milliseconds) into a fully functional digital chronograph. It renders a modern HUD stopwatch panel (`#10131A`) featuring digital readouts in cyber cyan (`DigitColor`, defaulting to `#38BDF8`) formatted with minute, second, and optional millisecond precision (`00:00.00`). Equipped with interactive transport buttons—Start/Pause (`▶` / `⏸`) and Stop/Reset (`⏹`)—developers and level designers can benchmark physics durations, measure cooldown intervals, or record gameplay sequences directly inside the inspector.

**The Problem:**
Tuning duration values—such as stun durations, cutscene timers, cooldown delays, or speedrun splits—traditionally involves guessing raw numbers, entering Play Mode, and checking external stopwatches or console logs to verify real-world feel.

**The Solution:**
Decorating numeric time fields with `[ChronoStopwatch]`:
- **Integrated Transport Controls:** Start, pause, resume, and zero-out timers with single-click UI buttons directly beside serialized fields.
- **Bi-Directional Property Binding:** Automatically pushes stopwatch accumulated time into the underlying serialized property, recording full Undo/Redo transactions.
- **Millisecond Precision:** Toggles between standard minute/second (`00:00`) and high-resolution millisecond (`00:00.00`) displays via `ShowMilliseconds`.
- **Standalone or Companion Mode:** Keep the standard numeric text field (`DrawInputField = true`) or replace it entirely with the chronograph widget (`DrawInputField = false`).
- **Collection Support:** Full support for numeric lists and arrays via `ICollectionElementAttribute`.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class RaceLapTimer : MonoBehaviour
{
    [ChronoStopwatch(showMs: true, digitColor: "#38BDF8")]
    public float bestLapTime = 74.25f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `float`, `double`, `int`, `long` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Collection Element Support** | Yes (`ICollectionElementAttribute`) |

---

## 4. Constructors & Parameters

```csharp
public ChronoStopwatchAttribute(bool showMs = true, string digitColor = "#38BDF8")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `showMs` | `bool` | `true` | Whether to include millisecond precision in the time display. |
| `digitColor` | `string` | `"#38BDF8"` | Hex color string for the digital stopwatch readout text. |

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ShowMilliseconds` | `bool` | `true` | When true, formats display as `00:00.00`; when false, formats as `00:00`. |
| `DigitColor` | `string` | `"#38BDF8"` | Hex color code applied to digital numerical readouts. |
| `DrawInputField` / `ShowInputField` | `bool` | `true` | When false, hides the standard numerical field and renders the chronograph widget standalone. |
| `IsEditable` / `Interactive` | `bool` | `true` | Controls whether transport buttons (play, pause, reset) are interactively clickable. |
| `CustomLabel` | `string` | `null` | Custom label string displayed alongside standalone chronograph widgets. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class BossFightEncounter : MonoBehaviour
{
    [Header("Encounter Phase Timers")]
    [ChronoStopwatch(showMs: false, digitColor: "#EF4444", CustomLabel = "Enrage Countdown")]
    public float enrageTimer = 180f;

    [ChronoStopwatch(showMs: true, digitColor: "#10B981", CustomLabel = "Vulnerability Window")]
    public float vulnerabilityDuration = 8.5f;

    [Header("Telemetry Benchmark")]
    [ChronoStopwatch(showMs: true, digitColor: "#F59E0B", DrawInputField = false)]
    public double recordedRunDuration = 0;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[BoxGroup]` / `[HorizontalGroup]`** | High | Fits nicely inside diagnostic groups or custom boss timeline panels. |
| **`[ShowIf]` / `[EnableIf]`** | High | Safely pauses and resumes time tracking when visibility state changes. |
| **`[ReadOnly]`** | High | Setting `IsEditable = false` disables the transport buttons for read-only benchmark tracking. |
| **Collection Elements** | High | Automatically wraps numerical elements within `List<float>` or `float[]`. |
