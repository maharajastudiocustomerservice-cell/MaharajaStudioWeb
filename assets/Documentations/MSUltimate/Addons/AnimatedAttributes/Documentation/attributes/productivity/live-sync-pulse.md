# [LiveSyncPulse]

> Displays a pulsating live beacon dot and badge indicating active synchronization with runtime or network state, with interactive click toggling.

---

## 1. Overview & Value Proposition

**What it does:**
`[LiveSyncPulse]` displays a real-time status beacon beside inspector fields. It renders a glowing circular beacon dot (8x8px) that smoothly pulses its alpha transparency according to a configurable cycle rate (`PulseRate`). Beside the dot is a high-contrast badge (`SyncLabel`, defaulting to `"LIVE"`). When interactive mode is enabled (`IsEditable = true`), clicking the badge triggers an instant Undo-recorded toggle for boolean properties alongside a 1.8x scale pop pulse on the beacon dot. It also implements `ICollectionElementAttribute` for multi-item list cascading.

**The Problem:**
When developing networked multiplayer games, live telemetry tools, or hot-reloading configurations, developers cannot easily distinguish fields that are synchronized live over socket/IPC connections from static offline properties. Accidental manual edits during runtime can desynchronize states without visual feedback.

**The Solution:**
Decorating live-synced fields with `[LiveSyncPulse]`:
- **Pulsing Circular Beacon:** Uses hardware-accelerated alpha oscillation (`PulseRate` cycles/sec) to communicate live connectivity.
- **Interactive Click Toggle:** Clicking the badge immediately toggles boolean properties with full Unity `Undo.RecordObject` registration and scale feedback.
- **Companion Field Layout:** Supports drawing the standard serialized property field (`DrawInputField = true`) or displaying standalone beacon labels.
- **Universal Collection Cascading:** Implements `ICollectionElementAttribute` to decorate collections, arrays, and lists of telemetry properties.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class NetworkPlayerSync : MonoBehaviour
{
    [LiveSyncPulse(beaconColor: "#10B981", syncLabel: "LIVE")]
    public bool isConnectedToMasterServer = true;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property (`bool`, `float`, `string`, etc.) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Collection Element Support** | Yes (`ICollectionElementAttribute`) |

---

## 4. Constructors & Parameters

```csharp
public LiveSyncPulseAttribute(string beaconColor = "#10B981", string syncLabel = "LIVE")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `beaconColor` | `string` | `"#10B981"` | Hex color string for the pulsing circular beacon dot and badge text. |
| `syncLabel` | `string` | `"LIVE"` | Text string displayed on the badge next to the beacon dot. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `BeaconColor` | `string` | `"#10B981"` | Hex color string for the beacon dot (defaults to Emerald). |
| `PulseRate` | `float` | `1.2f` | Pulse oscillation frequency in cycles per second. |
| `SyncLabel` | `string` | `"LIVE"` | Text displayed inside the status badge. |
| `DrawInputField` | `bool` | `true` | Whether to draw standard serialized property input field alongside the beacon. |
| `ShowInputField` | `bool` | `true` | Alias for `DrawInputField`. |
| `IsEditable` | `bool` | `true` | Whether clicking the badge interactively toggles boolean properties. |
| `Interactive` | `bool` | `true` | Alias for `IsEditable`. |
| `CustomLabel` | `string` | `null` | Custom label prefix displayed beside the beacon row. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class RemoteDeviceTelemetry : MonoBehaviour
{
    [Header("Server Connection")]
    [LiveSyncPulse(
        beaconColor: "#10B981", 
        syncLabel: "ONLINE", 
        PulseRate = 1.5f, 
        CustomLabel = "Cloud State"
    )]
    public bool isSyncingWithBackend = true;

    [Header("Sensor Feeds")]
    [LiveSyncPulse(beaconColor: "#38BDF8", syncLabel: "TELEMETRY")]
    public List<float> sensorHeartbeatChannels = new List<float> { 60f, 120f, 45f };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Integrates cleanly inside telemetry panels and networking status groups. |
| Collections (`List<T>`) | Supported | Implements `ICollectionElementAttribute` for cascading across list elements. |
| `[ReadOnly]` | Supported | Set `IsEditable = false` to display passive status without click toggle capability. |
