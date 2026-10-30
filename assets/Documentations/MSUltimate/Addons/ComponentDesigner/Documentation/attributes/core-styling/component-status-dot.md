# [ComponentStatusDot]

> Displays a minimal glowing LED status dot in any corner of the component card with optional text labels and outer glow bloom.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentStatusDot]` provides an immediate hardware-style LED status indicator on the component card. Injected into `ComponentSlot.BodyOverlay`, it renders a circular indicator dot (`Size = 10f`, `Color`) in a chosen corner (`Position = DotPosition.TopRight`, `TopLeft`, `BottomRight`, `BottomLeft`, `NextToHeaderRow`). It supports an optional soft outer glow halo (`Glow = true`), accompanying text label (`Label`, `LabelColor`), and customizable corner offset distance (`Offset`). Because `AllowMultiple = true`, developers can display multiple status dots concurrently (e.g., green for online network status and blue for telemetry recording).

**The Problem:**
Identifying whether a component represents an active runtime service, offline mock, debug testbed, or faulted state requires inspecting boolean fields or reading inspector labels. Developers need a clean, glanceable visual status light.

**The Solution:**
Decorating components with `[ComponentStatusDot]`:
- **Glanceable Status Light:** Instant LED feedback (green for active, red for error, amber for standby) without opening folded sections.
- **Corner Anchoring Options:** Dock the dot in any corner or beside header elements using `DotPosition`.
- **Soft Ambient Glow:** Renders a subtle outer glow bloom around the dot for an authentic illuminated hardware LED appearance.
- **Multiple Allowed:** `AllowMultiple = true` enables displaying multiple operational status indicators concurrently.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentStatusDot("#10B981", Label = "ONLINE", Position = DotPosition.TopRight)]
public class CloudTelemetryBroadcaster : MonoBehaviour
{
    public string apiEndpoint = "https://telemetry.studio.net";
    public int pingLatencyMs = 28;
    public bool isBroadcastingActive = true;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ComponentDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Component Slot** | `BodyOverlay` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentStatusDotAttribute(string color)
```

- `color`: Hex color string for the LED status dot (e.g. `"#00FF00"`).

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color` | `string` | *(Constructor)* | Hex color string for the LED dot circle. |
| `Position` | `DotPosition` | `DotPosition.TopRight` | Placement location (`TopRight`, `TopLeft`, `BottomRight`, `BottomLeft`, `NextToHeaderRow`). |
| `Size` | `float` | `10f` | Diameter in pixels of the status dot. |
| `Label` | `string` | `""` | Optional text caption displayed adjacent to the dot. |
| `LabelColor` | `string` | `"#888888"` | Hex color string for caption text. |
| `Glow` | `bool` | `true` | When true, renders a soft outer glow halo around the dot. |
| `Offset` | `float` | `8f` | Inset distance in pixels from the card corner edge. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#3B82F6", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#0D172A", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("SPATIAL AUDIO ENGINE", Subtitle = "HRTF Ambisonics Processor", BackgroundColor = "#1E293B", TitleColor = "#F1F5F9")]
[ComponentStatusDot("#22C55E", Label = "DSP ACTIVE", Position = DotPosition.TopRight, Size = 9f, Glow = true)]
[ComponentStatusDot("#38BDF8", Label = "VOIP READY", Position = DotPosition.TopLeft, Size = 9f, Glow = true)]
public class SpatialAudioEngine : MonoBehaviour
{
    [Header("Ambisonic Bins")]
    public int convolutionFilterTaps = 512;
    public float binauralCrossfeedGain = 0.35f;
    public bool enableDopplerShift = true;

    [Header("Acoustic Occlusion")]
    public LayerMask roomGeometryMask;
    public float raycastProbeDensity = 16f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeader]`** | High | Tucks into header corners, adding an authentic hardware LED status light. |
| **`[ComponentBorder]`** | High | Set `Offset` appropriately so the dot sits comfortably inside the border perimeter. |
| **Multiple Instances** | High | Place multiple status dots on opposing corners to show distinct subsystem states. |
