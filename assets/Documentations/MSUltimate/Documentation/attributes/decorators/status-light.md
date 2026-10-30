# [StatusLight]

> Displays a sleek LED-style status indicator light next to a field based on booleans, numeric thresholds, or conditions.

---

## 1. Overview & Value Proposition

**What it does:**
Renders a glowing LED light indicator (Green, Yellow, Red, or custom colors) next to a field to signal health, connectivity, or thresholds.

**The Problem:**
Looking at an inspector filled with connection strings, ping latencies, or state enums requires reading and interpreting numbers. There is no quick "traffic light" visual check to see if a system is healthy, struggling, or disconnected at a glance.

**The Solution:**
Add `[StatusLight]` to any field:
- **Instant Traffic Light Status:** Circular LED glows green for normal, yellow for warning, and red for error.
- **Dynamic Threshold Logic:** Automatically evaluates numeric fields (e.g. green $> 70$, yellow $> 30$, red $< 30$).
- **Custom Boolean Members:** Link to custom methods or properties (e.g. `IsServerConnected`) for custom state evaluation.
- **Collection Cascading:** Displays indicator lights on elements inside lists, arrays, or tables.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class ServerMonitor : MonoBehaviour
{
    [StatusLight]
    public bool isConnected = true;

    [StatusLight(greenThreshold: 80f, yellowThreshold: 40f)]
    public float signalStrength = 92f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `bool`, `float`, `int`, `double`, `byte`, `short`, `long` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public StatusLightAttribute()
public StatusLightAttribute(float greenThreshold, float yellowThreshold, bool invertDirection = false, float lightSize = 10f)
public StatusLightAttribute(string conditionMember)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `greenThreshold` | `float` | `70f` | Numeric threshold above which light displays green. |
| `yellowThreshold` | `float` | `30f` | Numeric threshold above which light displays yellow. |
| `invertDirection` | `bool` | `false` | If `true`, lower values are positive (useful for latency/ping). |
| `lightSize` | `float` | `10f` | Diameter of the LED dot in pixels. |
| `conditionMember` | `string` | `null` | Name of method or property returning bool for custom evaluation. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `GreenThreshold` | `float` | `70f` | Value threshold for positive green state. |
| `YellowThreshold` | `float` | `30f` | Value threshold for warning yellow state. |
| `InvertDirection` | `bool` | `false` | Inverts threshold evaluation polarity. |
| `LightSize` | `float` | `10f` | Diameter in pixels. |
| `ConditionMember` | `string` | `null` | Name of boolean member condition. |
| `GreenColorHex` | `string` | `null` | Custom hex color override for green state (`#2ecc71`). |
| `YellowColorHex` | `string` | `null` | Custom hex color override for yellow state (`#f1c40f`). |
| `RedColorHex` | `string` | `null` | Custom hex color override for red state (`#e74c3c`). |
| `CustomTooltip` | `string` | `null` | Tooltip displayed on hovering the indicator light. |
| `Order` | `int` | `0` | Execution priority relative to other decorator attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class NetworkHealthDashboard : MonoBehaviour
{
    [Header("Network Connection")]
    [StatusLight(nameof(CheckConnection))]
    public string serverHost = "gateway.region.internal";

    [Header("Ping & Latency")]
    [StatusLight(greenThreshold: 50f, yellowThreshold: 120f, invertDirection: true, CustomTooltip = "Round-trip ping time")]
    public float latencyMs = 28f;

    [Header("Cluster Load")]
    [StatusLight(greenThreshold: 85f, yellowThreshold: 50f)]
    public float batteryLevel = 94f;

    private bool CheckConnection => !string.IsNullOrEmpty(serverHost);
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[FieldTag]` | Supported | Pairs cleanly with field tags on the left and status light on the right. |
| `[BoxGroup]` | Supported | Displays inside group containers without breaking alignment. |
| `[ReadOnly]` | Supported | Continues to update live status even when property is read-only. |
