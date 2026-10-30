# [ComponentSeparator]

> Adds a styled horizontal separator rule line at the top or bottom of the component card with support for centered caption labels and custom margins.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentSeparator]` organizes component inspector layouts by drawing clean horizontal demarcation dividers. Docked above or below the inspector body (`Position = ComponentPosition.Top` $\to$ `BeforeBody`, `ComponentPosition.Bottom` $\to$ `AfterBody`), it renders a horizontal line (`Thickness`, `Color`) with optional centered label text (`Label`, `LabelColor`, `LabelFontSize`, `LabelBackgroundColor`). It provides fine-grained control over vertical and horizontal spacing (`MarginTop`, `MarginBottom`, `MarginHorizontal`), and because `AllowMultiple = true`, developers can place matching separator lines at both ends of a component card.

**The Problem:**
Long inspector windows featuring dozens of properties can feel like an undifferentiated wall of serialized controls. Standard Unity inspectors lack clean, component-level separator lines with embedded labels to bookend cards.

**The Solution:**
Decorating components with `[ComponentSeparator]`:
- **Integrated Centered Captions:** Embeds concise section labels (e.g. `"— RUNTIME SETTINGS —"`) centered along the divider line.
- **Top or Bottom Docking:** Position dividers above or below the inspector body using `ComponentPosition`.
- **Multiple Instances Allowed:** `AllowMultiple = true` allows framing both the top and bottom of a component.
- **Fine-Tuned Spacing Control:** Independently adjust top, bottom, and horizontal margins to achieve pixel-perfect layout alignments.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentSeparator(Position = ComponentPosition.Top, Label = "CONFIGURATION", Color = "#4F46E5")]
public class AudioMixerZoneTrigger : MonoBehaviour
{
    public float targetVolumeDb = -6.0f;
    public float crossfadeDurationSeconds = 2.0f;
    public bool isMutedOnEntry = false;
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
| **Component Slot** | `BeforeBody` (if `Position = Top`) or `AfterBody` (if `Position = Bottom`) |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentSeparatorAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Position` | `ComponentPosition` | `ComponentPosition.Top` | Docking placement (`ComponentPosition.Top` or `ComponentPosition.Bottom`). |
| `Color` | `string` | `"#3A3A5E"` | Hex color string for the divider line stroke. |
| `Thickness` | `float` | `1f` | Line stroke thickness in pixels. |
| `Label` | `string` | `""` | Optional caption label text centered on the divider line. |
| `LabelColor` | `string` | `"#888888"` | Hex color string for caption text. |
| `LabelFontSize` | `int` | `10` | Font size in points for caption text. |
| `LabelBackgroundColor`| `string` | `""` | Hex background plate color for text. If empty, matches inspector background. |
| `MarginTop` | `float` | `6f` | Vertical margin spacing in pixels above the separator. |
| `MarginBottom` | `float` | `6f` | Vertical margin spacing in pixels below the separator. |
| `MarginHorizontal` | `float` | `0f` | Horizontal indentation margin (left and right) in pixels. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#4B5563", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#111827", BorderRadius = 6f, Padding = 10f)]
[ComponentSeparator(Position = ComponentPosition.Top, Label = "TELEMETRY METRICS", Color = "#374151", LabelColor = "#9CA3AF", LabelFontSize = 10, MarginTop = 4f, MarginBottom = 8f)]
[ComponentSeparator(Position = ComponentPosition.Bottom, Label = "END OF METRICS", Color = "#374151", LabelColor = "#6B7280", LabelFontSize = 9, MarginTop = 8f, MarginBottom = 4f)]
public class NetworkBandwidthTelemetry : MonoBehaviour
{
    [Header("Network Stats")]
    public float upstreamBandwidthKbps = 1450f;
    public float downstreamBandwidthKbps = 3200f;
    public int droppedPacketsPerMinute = 2;

    [Header("Buffer Stats")]
    public int packetRingBufferSize = 1024;
    public bool enableJitterBuffer = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeader]`** | High | Places a clean separator directly below header elements. |
| **`[ComponentFooter]`** | High | Separators bookend the top while footers close out the bottom. |
| **Multiple Instances** | High | Stack an opening separator at `Top` and a closing separator at `Bottom`. |
