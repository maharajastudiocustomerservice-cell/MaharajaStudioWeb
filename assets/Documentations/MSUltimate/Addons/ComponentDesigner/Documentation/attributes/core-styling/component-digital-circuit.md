# [ComponentDigitalCircuit]

> Renders an animated digital PCB circuit board pattern with luminous data packets traveling along motherboard traces.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentDigitalCircuit]` transforms the component inspector into an active electronic circuit board. Injected as an ambient background or overlay layer (`Behind = true` $\to$ `ContentOverlay`), it draws etched motherboard copper traces (`TraceColor`, defaulting to dark PCB green `#1A3A1A`) across the card. Luminous data packets (`PulseColor`, defaulting to glowing phosphor green `#00FF00`) travel continuously along the traces with independent speeds and directions. Designed with built-in performance optimization, it maintains lightweight DOM footprint while providing a rich hardware-engineering aesthetic.

**The Problem:**
Cybernetic microchips, robotics logic boards, PCB firmware configurations, and electronic hardware components appear generic when presented with standard gray boxes and black lines.

**The Solution:**
Decorating electronics components with `[ComponentDigitalCircuit]`:
- **Animated Data Packets:** Simulates active electronic telemetry with data packet pulses gliding along circuit tracks.
- **Bi-Directional Signal Flow:** Pulses travel naturally in both left-to-right and right-to-left directions.
- **Safe Element Budgets:** Clamps trace count (`Traces`, between 2 and 8) and monitors DOM elements with proactive safety warnings to guarantee optimal editor performance.
- **Configurable Hardware Colors:** Switch between classic green silicon PCB (`#1A3A1A` / `#00FF00`), cyber cyan (`#0B253A` / `#00E5FF`), or amber vacuum-tube tracks (`#2A1A08` / `#FFB300`).
- **Non-Obtrusive Background Placement:** Positioned behind content (`Behind = true`) with `PickingMode.Ignore` so all buttons and fields remain fully clickable.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentDigitalCircuit(Traces = 4, TraceColor = "#0D2818", PulseColor = "#00FF66", Speed = 1.2f, Opacity = 0.4f)]
public class CyberwareMicrocontroller : MonoBehaviour
{
    public int clockFrequencyMHz = 800;
    public bool isNeuralInterfaceOnline = true;
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
| **Component Slot** | `ContentOverlay` (if `Behind = true`) or `BodyOverlay` (if `Behind = false`) |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentDigitalCircuitAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `TraceColor` | `string` | `"#1A3A1A"` | Hex color string for the stationary PCB circuit traces. |
| `PulseColor` | `string` | `"#00FF00"` | Hex color string for the traveling glowing data packet signals. |
| `Traces` | `int` | `4` | Number of horizontal circuit tracks generated (clamped between 2 and 8). |
| `Thickness` | `float` | `2f` | Stroke thickness of the circuit traces in pixels. |
| `PulseSize` | `float` | `6f` | Diameter in pixels of traveling data signal packets. |
| `Speed` | `float` | `1f` | Data packet velocity speed multiplier. |
| `Opacity` | `float` | `0.3f` | Global transparency alpha of the circuit container (0.0 to 1.0). |
| `Behind` | `bool` | `true` | When true, renders behind inspector controls; when false, renders as a top overlay. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#10B981", Width = 2f, Radius = 6f)]
[ComponentBackground("#051B11", BorderRadius = 6f, Padding = 12f)]
[ComponentDigitalCircuit(Traces = 4, TraceColor = "#0A3320", PulseColor = "#34D399", Thickness = 2f, Speed = 1.4f, Opacity = 0.5f, Behind = true)]
public class RobotCoreProcessor : MonoBehaviour
{
    [Header("Hardware Architecture")]
    public string firmwareVersion = "v4.18.2-rt";
    public int activeCoreThreads = 8;
    public float memoryBusUtilization = 64.2f;
    public bool enableOverclockProtection = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Recommended companion; dark green, navy, or charcoal backgrounds make glowing circuit tracks pop. |
| **`[ComponentHeader]`** | High | Combines cleanly with cyber headers or terminal titles. |
| **`[ComponentBadge]`** | High | Pairs well with corner badges (e.g. `"CPU-01"` or `"FIRMWARE"`). |
| **Inspector Controls** | High | `PickingMode.Ignore` ensures zero interference with field interaction or scrolling. |
