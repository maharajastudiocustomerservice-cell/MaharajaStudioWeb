# [ComponentBadge]

> Anchors a stylized floating metadata badge or tag at any corner of the component inspector card.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentBadge]` overlays a floating pill-shaped tag badge at any corner of the component inspector. Injecting into `ComponentSlot.BodyOverlay` with absolute positioning, it allows decorating components with prominent status tags such as `"BETA"`, `"DEPRECATED"`, `"SINGLETON"`, `"NETWORK"`, or custom release flags. It supports corner anchoring (`BadgeCorner`), custom background/text coloring, typography adjustments, optional Unity built-in icons, and allows multiple instances (`AllowMultiple = true`) to display stacked or opposite-corner tags.

**The Problem:**
Developers frequently need to communicate component status—such as alerting teammates that a component is experimental, legacy, work-in-progress, or restricted to specific environments—without cluttering the primary inspector field area with giant info boxes.

**The Solution:**
Decorating classes with `[ComponentBadge]`:
- **Unobtrusive Corner Placement:** Anchors cleanly to the top-right, top-left, bottom-right, or bottom-left corner of the component card.
- **Support for Multiple Badges:** Decorate a single component with multiple tags simultaneously (e.g. `"PRO"` at TopRight and `"EXPERIMENTAL"` at TopLeft).
- **Built-In Unity Icons:** Prepend official Editor icons (`Icon`) directly before the badge label.
- **Custom Aesthetic Themes:** Style colors to indicate severity (crimson red for deprecated, emerald green for stable, violet for network).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBadge("BETA", Corner = BadgeCorner.TopRight, BackgroundColor = "#F59E0B")]
public class ProceduralDungeonGenerator : MonoBehaviour
{
    public int dungeonSeed = 1337;
    public int roomCount = 15;
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
| **Component Slot** | `BodyOverlay` (`Order = 20`) |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentBadgeAttribute(string text)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `text` | `string` | *Required* | Text displayed inside the corner badge (e.g. `"CORE"`, `"WIP"`). |

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Text` | `string` | *Set via constructor* | Label string rendered within the pill tag. |
| `Corner` | `BadgeCorner` | `BadgeCorner.TopRight` | Corner position (`TopRight`, `TopLeft`, `BottomRight`, `BottomLeft`). |
| `BackgroundColor` | `string` | `"#E94560"` | Hex color string for the pill background. |
| `TextColor` | `string` | `"#FFFFFF"` | Hex color string for the badge text. |
| `FontSize` | `int` | `10` | Typography font size in points. |
| `FontStyle` | `FontStyle` | `FontStyle.Bold` | Font style (`Bold`, `Normal`, `Italic`). |
| `PaddingHorizontal` | `float` | `8f` | Left and right internal padding in pixels. |
| `PaddingVertical` | `float` | `3f` | Top and bottom internal padding in pixels. |
| `BorderRadius` | `float` | `10f` | Corner radius for the pill container. |
| `OffsetX` | `float` | `6f` | Horizontal pixel offset from the selected edge. |
| `OffsetY` | `float` | `6f` | Vertical pixel offset from the selected edge. |
| `Icon` | `string` | `""` | Unity built-in editor icon name shown before the text (e.g. `"d_Settings Icon"`). |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBadge("NETWORK CORE", Corner = BadgeCorner.TopRight, BackgroundColor = "#6366F1", TextColor = "#FFFFFF")]
[ComponentBadge("v2.4", Corner = BadgeCorner.BottomRight, BackgroundColor = "#1F2937", TextColor = "#9CA3AF", FontSize = 9)]
public class MultiplayerReplicationHub : MonoBehaviour
{
    [Header("Replication Settings")]
    public int tickRate = 60;
    public float timeoutSeconds = 15f;
    public bool enableInterpolation = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBorder]` / `[ComponentHeader]`** | High | Badges sit elegantly atop borders and header bars via absolute positioning. |
| **Multiple `[ComponentBadge]`** | High | Fully supported via `AllowMultiple = true`; use distinct corners or offset margins to avoid overlapping. |
| **`[ComponentColorStrip]`** | High | Pairs cleanly to establish instant color-coded visual categorization. |
| **All Inspector Fields** | High | Positioned out of the way in corner margins to prevent obscuring serialized input fields. |
