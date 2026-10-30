# [OnStateUpdate]

> Periodically executes a C# polling method while the Inspector window is visible and active.

---

## 1. Overview & Value Proposition

**What it does:**
Runs a method on a regular timer (e.g. every 100ms) while you are viewing the object in the Inspector.

**The Problem:**
In standard Unity, the Inspector only redraws when an input event happens or when you actively edit a property. If you want to poll runtime server health, refresh live telemetry stats, or animate editor preview elements, you have to write heavy custom `EditorApplication.update` loops that constantly chew CPU cycles.

**The Solution:**
Add `[OnStateUpdate]` above your polling method:
- **Configurable Tick Rate:** Choose your exact interval (e.g. 50ms, 100ms, 500ms) to preserve CPU performance.
- **Active-Only Execution:** Only ticks when the object is actively selected and displayed in the Inspector.
- **Live Telemetry & Diagnostics:** Continuously pull live metrics, network ping, or memory usage without manually clicking refresh.
- **Automatic Cleanup:** Immediately halts polling when the Inspector is closed or deselected.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class NetworkHealthMonitor : MonoBehaviour
{
    [ReadOnly]
    public float currentPingMs;

    [OnStateUpdate(250)]
    private void PollTelemetry()
    {
        currentPingMs = Random.Range(15f, 45f); // Example live metric
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Method | Field | Property` |
| **Supported Types** | Parameterless methods |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public OnStateUpdateAttribute()
public OnStateUpdateAttribute(long intervalMs)
public OnStateUpdateAttribute(string methodName, long intervalMs = 100)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `intervalMs` | `long` | `100` | The update interval in milliseconds between callback executions. |
| `methodName` | `string` | `null` | Optional method name when placing the attribute on a field instead of directly on the method. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `IntervalMs` | `long` | `100` | Polling rate frequency in milliseconds. |
| `MethodName` | `string` | `null` | Target method name invoked when attribute decorates a field or property. |
| `Order` | `int` | `0` | Execution priority relative to other callbacks. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class LiveBossTelemetry : MonoBehaviour
{
    [Header("Boss Live Stats")]
    [ReadOnly]
    public float currentHealthPercentage;

    [ReadOnly]
    public string currentAiState;

    [OnStateUpdate(150)]
    private void RefreshInspectorMetrics()
    {
        if (Application.isPlaying)
        {
            // Pull live runtime states into the Inspector display
            currentHealthPercentage = Mathf.PingPong(Time.time * 20f, 100f);
            currentAiState = currentHealthPercentage > 50f ? "Phase 1 - Melee" : "Phase 2 - Enraged";
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[ReadOnly]` | Supported | Ideal for displaying values updated on each state tick. |
| `[ProgressBar]` | Supported | Pair with live progress bars to create animated gauges in the Inspector. |
| `[BoxGroup]` | Supported | Fully functional inside layout containers. |
