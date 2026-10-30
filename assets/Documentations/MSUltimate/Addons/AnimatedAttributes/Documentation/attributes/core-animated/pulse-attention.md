# [PulseAttention]

> Pulses the field scale and color cyclically to draw user attention to critical or unconfigured inspector settings.

---

## 1. Overview & Value Proposition

**What it does:**
`[PulseAttention]` animates a cyclic, breathing pulse across the decorated field's scale and background or border color. It draws immediate visual priority to mandatory configuration fields, warning thresholds, or newly added inspector options without requiring disruptive modal dialogs.

**The Problem:**
Complex components often contain critical fields that designers inadvertently overlook during setup (e.g., missing essential references or unassigned gameplay multipliers). Static labels blend into long inspector layouts, leading to runtime null references or misconfigured mechanics.

**The Solution:**
Applying `[PulseAttention]` to an inspector field:
- **Draws Immediate Focus:** A rhythmic, pulsating breathing animation commands designer attention immediately upon opening the inspector.
- **Configurable Scale & Color:** Independently toggle and fine-tune scaling bounds (`MinScale`, `MaxScale`) and color oscillations (`PulseColor`, `BaseColor`).
- **Adjustable Frequency:** Modulate oscillation speed via `Speed` (cycles per second) to create subtle guidance or urgent alerts.
- **Performant & Zero Allocations:** Built directly on UI Toolkit's scheduler, ensuring smooth 60fps rendering without garbage collection spikes.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class SpawnerConfig : MonoBehaviour
{
    [PulseAttention(Speed = 1.2f, PulseColor = "#FF5555", AnimateColor = true)]
    public GameObject requiredSpawnPrefab;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `AttributeTargets.Field | AttributeTargets.Property` |
| **Supported Types** | Any serializable field or property |
| **Collection Interface** | `ICollectionElementAttribute` |
| **Collection Cascading** | Full (`List<T>`, `T[]`, `AdvancedList<T>`, `SerializableDictionary<K, V>`) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public PulseAttentionAttribute()
```

*Initializes a pulse animation with standard breathing scale bounds. Customize scale, color, and oscillation speed via object initializers.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MaxScale` | `float` | `1.05f` | Maximum scale multiplier reached at the peak of the pulse. |
| `MinScale` | `float` | `0.98f` | Minimum scale multiplier reached at the trough of the pulse. |
| `PulseColor` | `string` | `"#FF4444"` | Hex color string for the pulse color overlay or border tint. |
| `BaseColor` | `string` | `""` | Normal base color of the element when not pulsing (empty keeps default). |
| `Speed` | `float` | `1.0f` | Pulse oscillation speed in cycles per second (Hz). |
| `AnimateScale` | `bool` | `true` | Whether to animate the element scale during pulsing. |
| `AnimateColor` | `bool` | `false` | Whether to cycle element background/border color during pulsing. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class RaidBossEncounter : MonoBehaviour
{
    [Serializable]
    public class CoreMonitor
    {
        public string monitorName = "Alpha Reactor";

        [PulseAttention(PulseColor = "#DC2626", AnimateColor = true, Speed = 1.8f)]
        public float coreTemperature = 3450f;
    }

    [Header("Crucial Boss Setup")]
    [Tooltip("Must be assigned before entering the dungeon scene!")]
    [PulseAttention(
        MaxScale = 1.04f, 
        MinScale = 0.99f, 
        PulseColor = "#FF3366", 
        Speed = 1.5f, 
        AnimateColor = true, 
        AnimateScale = true
    )]
    public Transform bossSpawnAnchor;

    [Header("Core Monitor (Inside Class)")]
    public CoreMonitor mainCore = new CoreMonitor();

    [Header("Direct Collections Cascading")]
    [PulseAttention(PulseColor = "#EF4444", AnimateColor = true, Speed = 1.5f)]
    public int[] criticalAlarmThresholds = new int[] { 85, 90, 95, 99 };

    [PulseAttention(MinScale = 0.99f, MaxScale = 1.03f, Speed = 1f)]
    public List<float> reactorFrequencies = new List<float> { 433.92f, 868.0f, 915.0f };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Pulses comfortably within framed group boxes without clipping borders. |
| `[ShowIf]` | Supported | Pulsing timer pauses automatically when hidden and resumes when shown. |
| `[Tooltip]` | Supported | Tooltip overlays remain fully responsive during pulse animations. |

### Collection Cascading Matrix

| Collection Type | Cascading Behavior | Presentation Mode |
| :--- | :---: | :--- |
| `int[]`, `float[]` | **Supported** | Animates harmonic scale/color pulsing on individual collection element fields. |
| `List<string>`, `List<Transform>` | **Supported** | Pulses target object/string input slots in reorderable lists. |
| `AdvancedList<T>` | **Supported** | Fully compatible with reorderable lists and batch actions. |
| `SerializableDictionary<K, V>` | **Supported** | Cascades to dictionary value element rows. |
| Nested `[Serializable]` Classes | **Supported** | Independent pulse animations maintain phase without interference. |
