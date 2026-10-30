# [HierarchyStatusDot]

> Draws an interactive colored status indicator dot on the hierarchy row driven by boolean states, numeric thresholds, or static tints.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyStatusDot]` renders a crisp status indicator dot (or ring) directly on the hierarchy row. Driven by `HierarchyStatusDotRenderer`, it adapts intelligently to its target:
- **Class-Level:** Displays a fixed static status tint (`StaticColor = "#888888"`), ideal for categorizing subsystems or tagging entity types.
- **Boolean Field:** Toggles dynamically between active (`TrueColor = "#2ECC71"`) and inactive states (`FalseColor = "#E74C3C"`).
- **Numeric Field:** Evaluates 3-tier thresholds (`GreenThreshold`, `YellowThreshold`, `MaxValue`), transitioning smoothly between Green, Yellow, and Red alerts.
- **Pulsing Animation:** Features optional live pulsing when in critical or alert states (`PulseWhenCritical = true`).

**The Problem:**
Identifying whether an entity is currently online, connected, loaded, or in a critical state (e.g. low energy, dead, disarmed) requires selecting the object and scanning the Inspector. When managing scores of networked entities, drones, or AI bots, developers need instant visual cues to detect failing or inactive systems immediately.

**The Solution:**
Decorating classes or fields with `[HierarchyStatusDot]`:
- **At-a-Glance State Visibility:** Monitor operational health across dozens of entities without clicking into inspectors.
- **Multi-Mode Flexibility:** Works with static class tags, boolean switches, and numeric thresholds.
- **Solid or Ring Styles:** Render as a solid filled circle or a sleek outlined ring (`Outline = true`).
- **Critical Pulse Alerts:** Subtly pulses dot opacity to grab developer attention during errors or low health states.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class NetworkPeer : MonoBehaviour
{
    [HierarchyStatusDot(TrueColor = "#10B981", FalseColor = "#EF4444", PulseWhenCritical = true)]
    public bool isConnected;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class`, `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyStatusDotRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyStatusDotAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Size` | `float` | `10f` | Diameter of the status dot in pixels. |
| `XOffset` | `float` | `6f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `Outline` | `bool` | `false` | Draws the dot as an outline ring instead of a filled circle. |
| `OutlineWidth` | `float` | `2f` | Thickness of the outline ring in pixels when `Outline` is `true`. |
| `StaticColor` | `string` | `"#888888"` | Fixed hex color for class-level dots or fallback color. |
| `TrueColor` | `string` | `"#2ECC71"` | Hex color rendered when a monitored boolean field is `true`. |
| `FalseColor` | `string` | `"#E74C3C"` | Hex color rendered when a monitored boolean field is `false`. |
| `MaxValue` | `float` | `100f` | Maximum value for normalizing numeric thresholds. |
| `GreenThreshold` | `float` | `70f` | Percentage of `MaxValue` at or above which `GreenColor` is displayed. |
| `YellowThreshold` | `float` | `30f` | Percentage of `MaxValue` at or above which `YellowColor` is displayed. |
| `GreenColor` | `string` | `"#2ECC71"` | Hex color for numeric values at or above `GreenThreshold`. |
| `YellowColor` | `string` | `"#F39C12"` | Hex color for numeric values between `YellowThreshold` and `GreenThreshold`. |
| `RedColor` | `string` | `"#E74C3C"` | Hex color for numeric values below `YellowThreshold`. |
| `PulseWhenCritical` | `bool` | `false` | Whether the dot gently pulses in opacity when in a critical or false state. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the status dot remains visible and active during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class ShieldGenerator : MonoBehaviour
{
    [Header("Shield Energy Telemetry")]
    [HierarchyStatusDot(
        MaxValue = 1000f, 
        GreenThreshold = 60f, 
        YellowThreshold = 25f, 
        GreenColor = "#3B82F6", 
        YellowColor = "#F59E0B", 
        RedColor = "#EF4444", 
        PulseWhenCritical = true, 
        Size = 12f, 
        XOffset = 8f)]
    public float currentShieldPower = 850f;

    public bool isShieldOvercharged;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyToggle]`** | High | Pair status dots with toggle checkboxes to show state and allow direct interaction. |
| **`[HierarchyProgressBar]`** | High | Place a compact status dot next to progress bars for dual numeric + state visualization. |
| **`[HierarchyFlash]`** | High | Flash the row when boolean states switch while the status dot maintains persistent status. |
| **Class vs Field Targets** | High | Apply at the class level for static team identification or at the field level for live telemetry. |
