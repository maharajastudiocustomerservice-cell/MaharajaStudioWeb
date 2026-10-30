# [DeltaTracker]

> Displays live numeric diffs (+/- change) beside a field to show how much a value has drifted since the Inspector was opened.

---

## 1. Overview & Value Proposition

**What it does:**
Shows an inline badge (e.g. `+2.5` or `-10`) beside a number showing how much you changed it during your current editing session.

**The Problem:**
When balancing game parameters (like weapon recoil, player speed, or jump gravity), designers tweak numbers repeatedly. After several tweaks, it's easy to forget what the starting value was or whether you increased or decreased the stat.

**The Solution:**
Add `[DeltaTracker]` to any float or int field:
- **Instant Change Readout:** Automatically displays the difference between the initial session value and the current value.
- **Color-Coded Feedback:** Accents positive and negative deltas with custom badge colors.
- **Configurable Precision:** Control decimal place rounding (`decimals: 2`).
- **Zero Performance Hit:** Lightweight editor-only tracking with zero allocations on repaint.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class PlayerBalancing : MonoBehaviour
{
    [DeltaTracker(colorHex: "#F39C12", decimals: 1)]
    public float sprintSpeed = 8.5f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `int`, `float`, `double`, `long`, `short`, `byte`, `uint`, `ulong` |
| **Collection Cascading** | Supported (`List<T>`, `T[]`, `AdvancedList<T>`, `SerializableDictionary<K, V>` via `ICollectionElementAttribute`) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public DeltaTrackerAttribute(string colorHex = "#f39c12", int decimals = 2, bool alwaysShow = false)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `colorHex` | `string` | `"#f39c12"` | Hex color string for the delta indicator pill badge. |
| `decimals` | `int` | `2` | Number of decimal places shown on floating-point deltas. |
| `alwaysShow` | `bool` | `false` | When true, displays `+0.00` even when no changes have occurred yet. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ColorHex` | `string` | `"#f39c12"` | Pill background accent color. |
| `Decimals` | `int` | `2` | Precision decimal places. |
| `AlwaysShow` | `bool` | `false` | Always show badge even when delta is zero. |
| `Order` | `int` | `0` | Execution priority relative to other attributes. |

---

## 6. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

namespace MaharajaStudio.MSUltimate.Example
{
    [AddComponentMenu("Maharaja Studio/MSUltimate/Samples/Decorators/Delta Tracker Example")]
    public class DeltaTrackerExample : ModularMonoBehaviour
    {
        // ─── 1. Standalone Numeric Delta Tracking ────────────────────────────────
        [BoxGroup("1. Standalone Numeric Delta Tracking", BackgroundColor = "#0F172A", BorderColor = "#2563EB", BorderRadius = 6, MarginBottom = 8)]
        [DeltaTracker("#EF4444", 1)]
        public float playerHealth = 100f;

        [DeltaTracker("#10B981", 0, true)]
        public int combatScore = 1250;

        // ─── 2. Inside Custom Class Showcase ─────────────────────────────────────
        [BoxGroup("2. Inside Custom Class Showcase", BackgroundColor = "#0F172A", BorderColor = "#6366F1", BorderRadius = 6, MarginBottom = 8)]
        public VehicleTelemetrySlot propulsionTelemetry = new VehicleTelemetrySlot();

        [Serializable]
        public class VehicleTelemetrySlot
        {
            [DeltaTracker("#38BDF8", 0, true)]
            public float engineRpm = 4500f;

            [DeltaTracker("#EF4444", 2)]
            public float manifoldPressureBar = 2.45f;
        }

        // ─── 3. Direct Collections Cascading Showcase ────────────────────────────
        [BoxGroup("3. Direct Collections Cascading Showcase", BackgroundColor = "#0F172A", BorderColor = "#10B981", BorderRadius = 6, MarginBottom = 8)]
        [InfoBox("[DeltaTracker] implements ICollectionElementAttribute to automatically attach inline delta badges (Δ) to each row in numeric arrays and lists.", InspectorMessageType.Info)]

        [DeltaTracker("#10B981", 1)]
        public List<float> sensorTemperatures = new List<float> { 42.5f, 68.2f, 95.1f, 110.4f };

        [DeltaTracker("#F59E0B", 2)]
        public float[] calibrationOffsets = new float[] { 0.12f, -0.45f, 1.20f };

        // ─── 4. Interactive Simulation Actions ───────────────────────────────────
        [BoxGroup("4. Interactive Simulation Actions", BackgroundColor = "#0F172A", BorderColor = "#EAB308", BorderRadius = 6)]
        [Button("Apply Damage (-15 HP)", BackgroundColor = "#DC2626", TextColor = "#FFFFFF")]
        public void TakeDamage()
        {
            playerHealth = Mathf.Max(0f, playerHealth - 15f);
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

### Attribute Stacking

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Range]` | Supported | Pairs smoothly with range sliders to observe delta while sliding. |
| `[EditCounter]` | Supported | Combine together for comprehensive session editing telemetry. |
| `[BoxGroup]` | Supported | Functions normally inside group containers. |

### Collection Cascading Matrix

| Collection Type | Element Type | Supported | Notes |
| :--- | :--- | :---: | :--- |
| `T[]` (Array) | `float[]`, `int[]`, `double[]` | Yes | Each element row displays its own inline Δ drift badge. |
| `List<T>` | `List<float>`, `List<int>` | Yes | Cascades down to individual list elements automatically. |
| `AdvancedList<T>` | Numeric types | Yes | Fully supported on reorderable list rows. |
| `SerializableDictionary<K, V>` | Numeric Key or Value | Yes | Renders delta indicator beside corresponding dictionary items. |
| `[Serializable] class/struct` | Nested numeric fields | Yes | Tracks drift on fields inside nested structures. |
| **Context Menu Reset** | Right-click badge | Yes | Right-click the Δ badge to instantly reset baseline to current value. |

