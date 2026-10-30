# [LiveTrack]

> Tracks continuous field values over time and renders an inline real-time sparkline graph, statistical telemetry, and threshold alert badges.

---

## 1. Overview & Value Proposition

**What it does:**
`[LiveTrack]` instruments numeric fields and properties (`float`, `int`, `Vector3.magnitude`, etc.) to sample values continuously at a configurable frequency (`SampleRate`). It renders an interactive, real-time animated sparkline graph directly in the Inspector or Scene View, complete with running statistical metrics (`ShowStats`: Current, Δ, Min, Max, Average, and Rate of change) and visual boundary alert notifications (`AlertBelow`, `AlertAbove`).

**The Problem:**
Watching numerical behavior in Unity during Play Mode (such as player velocity, AI suspicion levels, health decay, or frame time delta) requires writing throwaway `Debug.Log()` spam or opening cumbersome external profilers. Log lines scroll away rapidly and provide zero sense of trend, frequency, or wave oscillation, while Unity's native Animation Window requires tedious recording workflows.

**The Solution:**
Decorating fields or properties with `[LiveTrack]`:
- **Real-Time Inline Graphing:** Renders a high-frequency sparkline waveform directly below the field in the Inspector (`ShowGraph = true`, `GraphHeight = 60f`).
- **Live Statistical Dashboard:** Displays key live analytics including Min, Max, Mean Average, and instantaneous delta rate (`ShowStats = true`).
- **Threshold Limit Alarms:** Flashes high-visibility visual alert badges when values drop below minimum safety limits (`AlertBelow`) or spike beyond ceilings (`AlertAbove`).
- **Flexible Tracking Modes:** Track in `EditMode`, `PlayMode`, or `Both` (`TrackingMode = LiveTrackMode.Both`).
- **Session Recording & Snapshots:** Capture baseline comparison snapshots (`EnableSnapshots = true`) and record telemetry sessions for later review (`RecordSession = true`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class VehicleController : MonoBehaviour
{
    [LiveTrack(
        ColorHex = "#2ECC71",
        TimeWindow = 15f,
        SampleRate = 0.05f,
        ShowStats = true)]
    public float currentSpeed = 0f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ToolBox-Vol1 Addon |
| **Attribute Target** | `Field` \| `Property` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Inspector & LiveTrack Dashboard |
| **Render Engine** | UI Toolkit (`LiveTrackDrawer`) & IMGUI Fallback |

---

## 4. Constructors & Parameters

```csharp
public LiveTrackAttribute()
```

- Parameterless constructor defaults to `Order = 200`, a 30-second rolling time window, and `LiveTrackMode.Both`.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `GraphHeight` | `float` | `60f` | Height of the inline sparkline graph in pixels. |
| `ColorHex` | `string` | `"#3498db"` | Primary hex color code used for the graph waveform and live telemetry dots. |
| `ShowGraph` | `bool` | `true` | Whether to render the visual waveform graph. |
| `TimeWindow` | `float` | `30f` | Rolling time window in seconds represented across the horizontal graph axis. |
| `SampleRate` | `float` | `0.1f` | Sampling interval in seconds (lower values produce smoother curves with slightly higher CPU cost). |
| `BufferSize` | `int` | `300` | Maximum number of data points stored in the circular ring buffer. |
| `TrackingMode` | `LiveTrackMode` | `LiveTrackMode.Both` | When sampling occurs: `EditMode`, `PlayMode`, or `Both`. |
| `ShowStats` | `bool` | `true` | Whether to display the running statistical bar (Current, Δ, Min, Max, Avg, Rate). |
| `AlertBelow` | `float` | `float.NaN` | Minimum threshold; flashes an alert badge when value drops below this number. |
| `AlertAbove` | `float` | `float.NaN` | Maximum threshold; flashes an alert badge when value exceeds this number. |
| `CorrelationGroup` | `string` | `""` | Identifier string for correlating and comparing multiple tracked fields together. |
| `DashboardGroup` | `string` | `""` | Grouping name used in the multi-object LiveTrack Dashboard window. |
| `EnableSnapshots` | `bool` | `false` | Enables one-click baseline snapshot capture buttons in the Inspector. |
| `RecordSession` | `bool` | `false` | Enables full session recording and playback capabilities. |
| `SessionName` | `string` | `""` | Named label assigned to recorded telemetry sessions. |
| `Collapsed` | `bool` | `true` | Whether the telemetry graph panel begins collapsed in the Inspector. |

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

namespace ProjectZero.AI
{
    public class StealthEnemyAI : MonoBehaviour
    {
        [Header("Telemetry Monitoring")]
        [LiveTrack(
            ColorHex = "#E74C3C",
            TimeWindow = 20f,
            SampleRate = 0.05f,
            ShowStats = true,
            AlertAbove = 95f,      // Alert when enemy reaches near-detection threshold
            AlertBelow = 5f,
            DashboardGroup = "EnemyAI_Stealth",
            EnableSnapshots = true)]
        public float suspicionLevel = 0f;

        [LiveTrack(
            ColorHex = "#3498DB",
            TimeWindow = 20f,
            SampleRate = 0.1f,
            ShowStats = false)]
        public float distanceFromPlayer = 50f;

        private void Update()
        {
            // Dynamic gameplay calculations
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HistoryTrack]`** | High | Pair real-time runtime waveforms (`[LiveTrack]`) with discrete edit session audits (`[HistoryTrack]`). |
| **`[BoxGroup]`** | High | Embeds smoothly inside layout groups alongside other inspected properties. |
| **`[ShowIf]`** | High | Live telemetry display hides and shows based on conditional expression rules. |
| **`[ConsoleCommand]`** | High | Manipulate live tracked values via developer console commands during profiling sessions. |
