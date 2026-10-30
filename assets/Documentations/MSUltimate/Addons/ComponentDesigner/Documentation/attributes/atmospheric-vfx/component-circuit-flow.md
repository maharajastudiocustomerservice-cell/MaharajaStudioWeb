# [ComponentCircuitFlow]

> Renders an animated printed circuit board background with glowing electrical data packets traveling along geometric motherboard traces.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentCircuitFlow]` transforms the component inspector background into an active printed circuit board (PCB). Injected into `ComponentSlot.ContentOverlay`, it renders geometric circuit trace pathways (`TraceDensity = 8`) mapped across the card surface. Rapid luminous electronic data packets traverse these pathways (`PacketSpeed = 1.4f`), simulating real-time signal transmission on silicon. Developers can customize trace and packet illumination colors (`TraceColor`, defaulting to emerald `#10B981`), density, signal travel speed, and background opacity (`Opacity = 0.22f`).

**The Problem:**
Hardware drivers, CPU emulation logic, IoT device bridges, microchip controllers, and robotic sensor boards appear plain in standard inspector panels. Developers lack immediate visual cues that convey electronic hardware architectures.

**The Solution:**
Decorating electronic and computing systems with `[ComponentCircuitFlow]`:
- **Animated Data Pulse Packets:** Simulates active microchip electrical bus pathways with moving luminous data packets.
- **Geometric PCB Traces:** Generates orthogonal multi-segment circuit pathways with angled 45-degree bends.
- **Configurable Bus Density:** Scale trace count (`TraceDensity = 8`) and speed (`PacketSpeed = 1.4f`) to fit any component card.
- **Non-Obtrusive Overlay:** Placed in `ContentOverlay` with `PickingMode.Ignore`, guaranteeing completely unobstructed mouse interaction.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentCircuitFlow(traceColor: "#00E5FF", packetSpeed: 1.6f, traceDensity: 10)]
public class MicrocontrollerBusInterface : MonoBehaviour
{
    public int clockFrequencyMHz = 160;
    public float i2cBusBaudRateKbps = 400f;
    public bool isDmaTransferActive = true;
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
| **Component Slot** | `ContentOverlay` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentCircuitFlowAttribute()
public ComponentCircuitFlowAttribute(string traceColor = "#10B981", float packetSpeed = 1.4f, int traceDensity = 8)
```

- `traceColor`: Hex color string for circuit traces and moving data packets.
- `packetSpeed`: Propagation speed multiplier of traveling electronic packets.
- `traceDensity`: Total number of circuit trace pathways to generate across the card.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `TraceColor` | `string` | `"#10B981"` | Hex color string for circuit lines and travelling data packets. |
| `PacketSpeed` | `float` | `1.4f` | Speed multiplier governing packet movement along trace lines. |
| `TraceDensity` | `int` | `8` | Total count of geometric circuit trace paths rendered. |
| `Opacity` | `float` | `0.22f` | Visibility opacity alpha of the circuit simulation (0.0 to 1.0). |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#10B981", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#061710", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("ROBOTIC SENSOR BUS HUB", Subtitle = "SPI & CAN Bus Multiplexer", BackgroundColor = "#0A291C", TitleColor = "#D1FAE5")]
[ComponentCircuitFlow(TraceColor = "#34D399", PacketSpeed = 1.5f, TraceDensity = 12, Opacity = 0.25f)]
public class RoboticSensorBusHub : MonoBehaviour
{
    [Header("Bus Channels")]
    public int canBusBaudRate = 500000;
    public int activeTelemetryChannels = 8;
    public float sensorPollingRateHz = 100f;

    [Header("Diagnostics")]
    public float busLoadPercentage = 42.5f;
    public bool autoClearTxErrors = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Dark PCB green or deep slate backdrops enhance the radiance of glowing circuit traces. |
| **`[ComponentHeader]`** | High | Geometric data pulses flow seamlessly behind fields underneath tech header cards. |
| **Inspector Controls** | High | `PickingMode.Ignore` ensures complete click-through transparency for all inspector controls. |
