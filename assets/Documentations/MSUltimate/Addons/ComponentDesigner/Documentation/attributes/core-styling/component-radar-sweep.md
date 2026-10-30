# [ComponentRadarSweep]

> Renders a circular tactical radar display with an animated rotating sweep line and trailing sonar beam docked in any corner of the component card.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentRadarSweep]` embeds an animated tactical radar display directly into the component inspector card. Anchored to any specified corner (`Position = TypingIndicatorPosition.TopRight`, `TopLeft`, `BottomLeft`, `BottomRight`), it renders a miniature circular HUD display (`Diameter = 30f`). It projects concentric range rings and a continuous rotating sweep line (`Speed = 0.3f` rev/sec) that leaves a fading phosphorescent wake. Featuring customizable luminous sonar colors (`Color`, defaulting to radar green `#00FF88`), transparency (`Opacity`), and dimensions, it provides visual identification for scanning, sensing, and detection systems.

**The Problem:**
Sonar systems, proximity triggers, target-lock radars, and spatial sensor scripts are visually indistinguishable from non-spatial systems in standard inspector windows. Developers configuring detection ranges and radar sweeps lack tactical HUD feedback.

**The Solution:**
Decorating sensory systems with `[ComponentRadarSweep]`:
- **Animated Rotational Sweep:** Simulates authentic rotating PPI radar scopes with angular beam sweep and trailing phosphorescent decay.
- **Dockable Corner Placement:** Anchors neatly in any corner (`TopRight`, `TopLeft`, etc.) without crowding serialized field inputs.
- **Configurable Scale & Colors:** Adjust diameter from subtle mini-blips (24px) to prominent 48px tactical radar scopes in green, amber, or cyan.
- **Input Transparency:** Positioned in `BodyOverlay` with `PickingMode.Ignore`, ensuring all standard Unity input controls remain completely responsive.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentRadarSweep(Color = "#10B981", Diameter = 32f, Speed = 0.4f, Position = TypingIndicatorPosition.TopRight)]
public class ProximityRadarScanner : MonoBehaviour
{
    public float detectionRadiusMeters = 50f;
    public LayerMask targetEntityMask;
    public bool triggerAlarmOnUnidentifiedTarget = true;
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
public ComponentRadarSweepAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color` | `string` | `"#00FF88"` | Hex color string for the radar rings and rotating sweep beam. |
| `Diameter` | `float` | `30f` | Outer diameter of the radar display in pixels. |
| `Speed` | `float` | `0.3f` | Rotation velocity in full revolutions per second. |
| `Opacity` | `float` | `0.5f` | Overall transparency alpha of the radar scope (0.0 to 1.0). |
| `Position` | `TypingIndicatorPosition` | `TypingIndicatorPosition.TopRight` | Corner placement (`TopRight`, `TopLeft`, `BottomRight`, `BottomLeft`). |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#059669", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#062319", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("TACTICAL AIR SEARCH RADAR", Subtitle = "Long-Range IFF Interrogator", BackgroundColor = "#0A3D2A", TitleColor = "#D1FAE5")]
[ComponentRadarSweep(Color = "#34D399", Diameter = 36f, Speed = 0.35f, Opacity = 0.6f, Position = TypingIndicatorPosition.TopRight)]
public class TacticalAirSearchRadar : MonoBehaviour
{
    [Header("Radar Specifications")]
    public float maxSearchRangeKilometers = 120f;
    public float sweepBeamAzimuthDegrees = 3.5f;
    public int simultaneousTrackCapacity = 32;

    [Header("Electronic Counter-Countermeasures")]
    public bool enableFrequencyHopping = true;
    public float chaffRejectionThresholdDb = 14f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeader]`** | High | Docking to `TopRight` mounts the radar display in the upper right header corner. |
| **`[ComponentBadge]`** | High | Position radar in an opposing corner to prevent overlap with corner badge tags. |
| **Inspector Controls** | High | Renders with `PickingMode.Ignore`, ensuring all standard Unity input controls remain completely responsive. |
