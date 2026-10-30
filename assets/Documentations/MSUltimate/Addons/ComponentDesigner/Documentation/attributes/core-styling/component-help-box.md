# [ComponentHelpBox]

> Renders stylized callout help and alert boxes at the top or bottom of the component card with semantic color themes, icons, and custom styling.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentHelpBox]` provides component-level informational, warning, and tip callouts across inspector windows. Docked before (`ComponentPosition.Top` $\to$ `ComponentSlot.BeforeBody`) or after (`ComponentPosition.Bottom` $\to$ `ComponentSlot.AfterBody`) the inspector body, it formats message callouts with semantic visual indicators. It natively supports five status modes (`Type = Info`, `Warning`, `Error`, `Tip`, `Note`), automatic or custom icons (`Icon`), configurable background/border/text colors (`BackgroundColor`, `BorderColor`, `TextColor`), typography overrides (`FontSize`, `FontStyle`), and rounded box geometry (`BorderRadius`, `Padding`, `Margin`).

**The Problem:**
Standard Unity `[HelpBox]` is designed primarily for field-level decorators, creating repetitive or awkward layout gaps when communicating global component instructions, prerequisites, or deprecation alerts. Furthermore, default Unity help boxes lack modern theming and customizable corner radiuses.

**The Solution:**
Decorating components with `[ComponentHelpBox]`:
- **Five Semantic Status Presets:** Instant visual styling for `Info` (blue), `Warning` (amber), `Error` (crimson), `Tip` (emerald), and `Note` (purple/slate).
- **Component-Level Docking:** Positions cleanly at the top (`ComponentPosition.Top`) or bottom (`ComponentPosition.Bottom`) of the inspector card.
- **Multiple Allowed:** `AllowMultiple = true` enables stacking multiple notices (e.g. an informational overview plus a critical setup warning).
- **Total Aesthetic Customization:** Fully override colors, border thickness, padding, margins, and icons to match any studio design system.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentHelpBox("Ensure NavMesh baking is complete before adjusting agent patrol points.", Type = ComponentHelpBoxType.Warning)]
public class AIWaypointPatrolController : MonoBehaviour
{
    public float movementSpeed = 4.5f;
    public Transform[] patrolWaypoints;
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
public ComponentHelpBoxAttribute(string message)
```

- `message`: The informational or alert text string displayed inside the callout container.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Message` | `string` | *(Constructor)* | Primary callout message string. |
| `Type` | `ComponentHelpBoxType` | `ComponentHelpBoxType.Info` | Semantic box preset (`Info`, `Warning`, `Error`, `Tip`, `Note`). |
| `Position` | `ComponentPosition` | `ComponentPosition.Top` | Docking placement (`ComponentPosition.Top` or `ComponentPosition.Bottom`). |
| `BackgroundColor` | `string` | `""` | Hex background color override. If empty, uses preset color. |
| `TextColor` | `string` | `""` | Hex text color override. If empty, uses preset color. |
| `BorderColor` | `string` | `""` | Hex border stroke color override. If empty, uses preset color. |
| `BorderWidth` | `float` | `1f` | Border stroke thickness in pixels. |
| `BorderRadius` | `float` | `4f` | Corner rounding radius in pixels. |
| `FontSize` | `int` | `0` | Text font size in points (`0` uses default inspector size). |
| `FontStyle` | `FontStyle` | `FontStyle.Normal` | Font style (`Normal`, `Bold`, `Italic`). |
| `Padding` | `float` | `8f` | Internal padding in pixels. |
| `Margin` | `float` | `4f` | External margin spacing around the box. |
| `Icon` | `string` | `""` | Unity built-in icon identifier override (e.g. `"console.warnicon"`). |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#EAB308", Width = 1.5f, Radius = 6f)]
[ComponentHeader("PHYSICS RIGIDBODY BRIDGE", Subtitle = "Interpolation & Network Sync", BackgroundColor = "#1F1A0A", TitleColor = "#FEF08A")]
[ComponentHelpBox("Requires a Rigidbody component on this GameObject or continuous sync will fail.", Type = ComponentHelpBoxType.Warning, Position = ComponentPosition.Top)]
[ComponentHelpBox("Pro Tip: Enable 'Sub-Stepping' in Project Settings for smoother high-velocity ragdolls.", Type = ComponentHelpBoxType.Tip, Position = ComponentPosition.Bottom)]
public class PhysicsRigidbodyBridge : MonoBehaviour
{
    [Header("Sync Rates")]
    public float networkTickRateHz = 60f;
    public float interpolationLagCompensationMs = 33.3f;
    public bool enableContinuousCollisionDetection = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeader]`** | High | Help boxes positioned at `Top` tuck naturally below the header bar. |
| **`[ComponentNotification]`** | High | Use notifications for dismissible operational toasts and help boxes for persistent instructional guidelines. |
| **Multiple Instances** | High | Stack an `Info` overview at the `Top` and a `Tip` guide at the `Bottom`. |
