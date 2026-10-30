# [ComponentOrbiting]

> Renders animated dots orbiting in circular paths at any corner of the component card as a subtle activity or status indicator.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentOrbiting]` adds delicate planetary motion to component inspectors. Anchored at a selected corner (`Position = TypingIndicatorPosition.TopRight`, `TopLeft`, `BottomLeft`, `BottomRight`), it animates small glowing dots (`Count = 3`) orbiting along a circular path of radius `Radius` at a steady rotational velocity (`Speed`). Developers can customize the satellite dot hue (`Color`), dot diameter (`Size`), transparency (`Opacity`), and corner placement. Injected into `ComponentSlot.BodyOverlay`, it serves as an elegant indicator that an active background job, thread, or network socket is associated with the component.

**The Problem:**
Long-running async tasks, active AI state machines, continuous network bridges, and background worker threads operate invisibly in the inspector. Developers often cannot tell if a component is actively processing data or idling without opening external debug logs.

**The Solution:**
Decorating active services with `[ComponentOrbiting]`:
- **Subtle Corner Activity Indicator:** Replaces bulky progress bars with a minimalist planetary orbit spinner tucked away in a card corner.
- **Corner Anchoring Flexibility:** Position the orbit cluster in any corner (`TopRight`, `TopLeft`, `BottomRight`, `BottomLeft`) via `TypingIndicatorPosition`.
- **Customizable Dot Counts & Speed:** Configure from a brisk 2-dot binary star system to a 5-dot atomic electron cloud.
- **Zero Click Interference:** Runs with `PickingMode.Ignore`, ensuring corner-adjacent fields or buttons remain completely responsive.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentOrbiting(Color = "#38BDF8", Count = 4, Radius = 10f, Speed = 0.8f, Position = TypingIndicatorPosition.TopRight)]
public class NetworkSyncSocket : MonoBehaviour
{
    public string remoteServerHost = "wss://game.studio.net/live";
    public int pingLatencyMs = 24;
    public bool isSocketConnected = true;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ComponentDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Component Slot** | `BodyOverlay` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentOrbitingAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color` | `string` | `"#4FC3F7"` | Hex color string for the orbiting satellite dots. |
| `Count` | `int` | `3` | Total number of orbiting dots spaced evenly along the circular orbit. |
| `Radius` | `float` | `8f` | Orbital circle radius in pixels from the pivot anchor. |
| `Size` | `float` | `3f` | Diameter in pixels for each orbiting dot. |
| `Speed` | `float` | `0.5f` | Orbital rotation rate (rotations per second). |
| `Opacity` | `float` | `0.6f` | Transparency alpha of the orbiting dots (0.0 to 1.0). |
| `Position` | `TypingIndicatorPosition` | `TypingIndicatorPosition.TopRight` | Corner placement (`TopRight`, `TopLeft`, `BottomRight`, `BottomLeft`). |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#38BDF8", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#081A24", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("ORBITAL TELEMETRY RELAY", Subtitle = "Asynchronous Satellite Uplink", BackgroundColor = "#0C2938", TitleColor = "#E0F2FE")]
[ComponentOrbiting(Color = "#7DD3FC", Count = 4, Radius = 9f, Size = 3.5f, Speed = 0.75f, Opacity = 0.7f, Position = TypingIndicatorPosition.TopRight)]
public class OrbitalTelemetryRelay : MonoBehaviour
{
    [Header("Telemetry Uplink")]
    public string satelliteIdentifier = "SAT-ORION-9";
    public float signalToNoiseRatioDb = 18.4f;
    public int packetQueueCount = 14;

    [Header("Orbital State")]
    public float orbitalPeriodMinutes = 94.2f;
    public bool isUplinkLocked = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeader]`** | High | Docking to `TopRight` places the orbiting dots cleanly in the corner of the header bar. |
| **`[ComponentBadge]`** | High | Position `[ComponentOrbiting]` in an opposite corner to prevent visual overlap with corner badge tags. |
| **Inspector Controls** | High | Positioned in `BodyOverlay` with `PickingMode.Ignore`, ensuring all standard Unity input controls remain completely responsive. |
