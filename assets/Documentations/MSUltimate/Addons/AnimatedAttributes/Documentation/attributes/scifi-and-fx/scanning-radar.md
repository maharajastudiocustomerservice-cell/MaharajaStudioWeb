# [ScanningRadar]

> Displays a circular rotating radar screen with targeting crosshairs and a fading phosphor sweep beam beside inspector fields.

`Package: MSUltimate-AnimatedAttributes` `Targets: Field | Property` `AllowMultiple: False` `Inherited: True` `Performance: High (Hardware-Accelerated UI Toolkit 2D Vector Meshes)`

---

## 1. Overview & Value Proposition

**What it does:**
`[ScanningRadar]` embeds a functional 360-degree rotating radar display beside serialized properties and collection items. It renders a circular CRT scope (`RadarSize`, defaulting to 40px) styled in deep military radar green (`#0D1F14`). Using UI Toolkit's 2D vector painter, it draws internal crosshairs, a continuous 360-degree radial sweeping line (`painter.LineTo`), and a fading 45-degree phosphor trail arc (`painter.Arc`) that rotates continuously according to `SweepSpeed` (revolutions per second) in a chosen phosphor hue (`RadarColor`).

**The Problem:**
Submarine navigation, sonar ping systems, tactical radar arrays, or stealth detection radiuses require active visual feedback during balancing. Tweaking detection radiuses, sweep speeds, or target proximity with numeric fields alone provides no visual sense of scanning tempo.

**The Solution:**
Decorating stealth, radar, or detection properties with `[ScanningRadar]`:
- **Circular Scope Widget:** Compact circular instrument placed neatly beside the `PropertyField` input control.
- **Collection Element Cascading:** Implements `ICollectionElementAttribute` so every waypoint or target slot in `Vector3[]` or `List<T>` has its own radar sweep indicator.
- **Continuous 360° Sweep:** Full rotational sweep line with a trailing 45-degree fading phosphor decay arc.
- **Vector-Drawn Crosshairs:** Center reference crosshairs rendered at 25% opacity for authentic military display aesthetics.
- **Configurable Dimensions & Colors:** Scale scope diameter (`RadarSize`) from small indicators to prominent circular gauges in custom phosphor tints (`#10B981` green, `#38BDF8` cyan, or `#F59E0B` amber).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class ScoutDrone : MonoBehaviour
{
    [ScanningRadar(size: 42f, radarColor: "#10B981")]
    public float enemyDetectionRadiusMeters = 75f;
}
```

---

## 3. Constructors & Parameters

```csharp
public ScanningRadarAttribute(float size = 40f, string radarColor = "#10B981")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `size` | `float` | `40f` | Diameter in pixels of the circular radar screen. |
| `radarColor` | `string` | `"#10B981"` | Hex color string of the radar sweep line and fading phosphor trail arc. |

---

## 4. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `RadarSize` | `float` | `40f` | Diameter of the circular radar scope in pixels. |
| `RadarColor` | `string` | `"#10B981"` | Hex color string for the radar sweep beam (defaults to Emerald Green). |
| `SweepSpeed` | `float` | `1.5f` | Rotational speed in revolutions per second. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 5. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

namespace MaharajaStudio.MSUltimate.AnimatedAttributes.Sample
{
    public class ScanningRadarExample : ModularMonoBehaviour
    {
        [Title("ScanningRadar Attribute Showcase", "Continuous 360-degree radar sweep beam")]
        [InfoBox("ScanningRadar renders an authentic circular PPI radar display with a sweeping radial beam.", InspectorMessageType.Info)]

        [BoxGroup("1. Standalone Radar Scanners")]
        [ScanningRadar(size: 45f, radarColor: "#10B981", SweepSpeed = 1.5f)]
        public string primaryAirspaceSector = "SECTOR-BRAVO-AIRSPACE-NORTH";

        [ScanningRadar(size: 38f, radarColor: "#06B6D4", SweepSpeed = 1.0f)]
        public float sonarEchoDepthMeters = 840f;

        [BoxGroup("2. Inside Class Demonstration")]
        public RadarContactNode activeTarget = new RadarContactNode();

        [BoxGroup("3. Monitored Contact Radar Manifest")]
        [InfoBox("ScanningRadar cascades down to collections, rendering individual circular radar sweep displays beside each coordinate row.", InspectorMessageType.Info)]
        [Title("Tactical Airspace Waypoints (Radar Scanline Cascading)")]
        [ScanningRadar(size: 32f, radarColor: "#10B981", SweepSpeed = 1.2f)]
        public Vector3[] airspaceWaypoints = new Vector3[]
        {
            new Vector3(120f, 450f, 30f),
            new Vector3(250f, 480f, 90f),
            new Vector3(380f, 520f, 140f)
        };

        public List<RadarContactNode> contactList = new List<RadarContactNode>
        {
            new RadarContactNode { iffCode = "CIVILIAN-CARGO-77", lockOnDistanceKm = 42.0f },
            new RadarContactNode { iffCode = "ESCORT-FRIGATE-02", lockOnDistanceKm = 8.5f }
        };

        [Serializable]
        public class RadarContactNode
        {
            public string iffCode = "BOGEY-BANDIT-09";

            [ScanningRadar(size: 36f, radarColor: "#F59E0B", SweepSpeed = 1.8f)]
            public float lockOnDistanceKm = 14.8f;
        }

        [BoxGroup("4. Radar Station Controls")]
        [Button("Simulate Unidentified Blip Detection", BackgroundColor = "#10B981", TextColor = "#022C22")]
        public void DetectBlip()
        {
            activeTarget.lockOnDistanceKm = Mathf.Max(1.0f, activeTarget.lockOnDistanceKm - 2.5f);
            Debug.LogWarning($"<color=#34D399>[ScanningRadar]</color> Contact locked! Distance: {activeTarget.lockOnDistanceKm:F1} km.");
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Sits seamlessly alongside property inputs inside diagnostic or combat panels. |
| `[SonarPingWave]` | Stacking | Pairs with radial sonar ping waves for multi-layered acoustic/radar detection suites. |
| `[ReadOnly]` | Supported | Accentuates read-only surveillance logs and sensor telemetry readouts. |
| Validation Attributes | Supported | Fully compatible with `[Required]`, `[Range]`, and `[NotNull]`. |

---

## 7. Collection Cascading & Custom Serializer Discipline

| Context / Architecture | Support | Behavior & Guidelines |
| :--- | :---: | :--- |
| **Collection Element Cascading** | Supported (`ICollectionElementAttribute`) | Cascades down to individual collection rows (`Vector3[]`, `string[]`, `List<T>`), rendering individual rotating PPI radar widgets beside each row. |
| **Target Element Roles** | Supported | `CollectionElementRole.Element`, `Value`, `NullableValue`, `TupleItem`. |
| **Direct Collections** | Supported | Operates on direct coordinate arrays (`Vector3[]`, `Vector2[]`), transform lists, and target strings. |
| **Nested Serializable Classes** | Supported | Fully operates on fields inside child items and structs declared within lists. |
| **Custom Serializers** | Supported | Seamlessly functions in `AdvancedList<T>`, `SerializableDictionary<K, V>`, and `SerializableTuple<...>`. |
