# [PullToRefreshTrigger]

> Renders an interactive pull-to-refresh spring gesture that triggers callbacks or methods upon elastic release.

---

## 1. Overview & Value Proposition

**What it does:**
`[PullToRefreshTrigger]` adapts modern mobile pull-to-refresh UX into the Unity Inspector. It places a tactile pull handle inside a recessed track chamber (`#0F172A`, height 62px). When dragged vertically with the mouse, it exhibits elastic rubber-band resistance. Dragging beyond the activation threshold (`PullThreshold`, defaulting to 40px) triggers a vivid threshold bloom (`AccentColor`, defaulting to `#10B981` emerald). Upon mouse release, the handle snaps back with spring kinematics and invokes the target method, callback, or property refresh.

**The Problem:**
Editor maintenance tasks—such as refreshing network databases, querying cloud catalogs, re-scanning asset directories, or refreshing procedural preview caches—are traditionally triggered by ordinary buttons. Buttons can be accidentally clicked, and they lack the deliberate physical intent that prevents accidental server or cache queries.

**The Solution:**
Decorating refresh methods or telemetry properties with `[PullToRefreshTrigger]`:
- **Tactile Elastic Drag:** Simulates true rubber-band resistance, requiring deliberate physical pulling before triggering.
- **Visual Threshold Bloom:** Glows brightly with an accent hue (`AccentColor`) when dragged past the threshold point.
- **Spring Kinematics:** Automatically snaps back into resting position upon release with harmonic damping.
- **Method & Property Compatibility:** Overrides both property (`OnGUI`) and method (`OnMethodGUI`) execution, with full collection cascading via `ICollectionElementAttribute`.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class AssetCatalogManager : MonoBehaviour
{
    [PullToRefreshTrigger(pullThreshold: 45f, triggerText: "Pull to Sync Catalog")]
    public void RefreshRemoteAssetCatalog()
    {
        Debug.Log("Asset catalog queried and synced!");
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property | Method` |
| **Supported Types** | Methods or any serializable field/property |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Collection Element Support** | Yes (`ICollectionElementAttribute`) |

---

## 4. Constructors & Parameters

```csharp
public PullToRefreshTriggerAttribute(string triggerText = "Pull to Refresh", float pullThreshold = 40f)

public PullToRefreshTriggerAttribute(float pullThreshold, string triggerText = "Pull to Refresh")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `triggerText` | `string` | `"Pull to Refresh"` | Prompt text displayed on the draggable pull handle. |
| `pullThreshold` | `float` | `40f` | Drag distance in pixels required to activate the refresh trigger. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `PullThreshold` | `float` | `40f` | Required downward pull distance in pixels to trigger execution. |
| `TriggerText` | `string` | `"Pull to Refresh"` | Prompt text rendered on the handle surface. |
| `AccentColor` | `string` | `"#10B981"` | Hex color string for active threshold glow (defaults to Emerald). |
| `TrackColor` | `string` | `"#0F172A"` | Hex color string for the recessed spring track chamber background. |
| `IsEditable` | `bool` | `true` | Whether the pull handle can be interactively dragged. |
| `Interactive` | `bool` | `true` | Alias for `IsEditable`. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class LiveLeaderboardController : MonoBehaviour
{
    [Header("Leaderboard Synchronization")]
    [PullToRefreshTrigger(
        triggerText: "Pull to Fetch Global Top 100", 
        pullThreshold: 50f, 
        AccentColor = "#3B82F6", 
        TrackColor = "#020617"
    )]
    public void SyncGlobalLeaderboardData()
    {
        Debug.Log("Leaderboard refreshed from cloud endpoint.");
    }

    [Header("Telemetry Cache Timestamp")]
    [PullToRefreshTrigger(35f, "Pull to Invalidate Cache")]
    public string cachedSyncTimestamp = "2026-10-12 01:00 UTC";
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Sits safely inside network settings panels or maintenance sections. |
| `[LiveSyncPulse]` | Stacking | Pairs with live sync pulses to visually indicate synchronization status after pull. |
| Method Buttons | Supported | Replaces traditional flat action buttons with deliberate pull-to-refresh gestures. |
