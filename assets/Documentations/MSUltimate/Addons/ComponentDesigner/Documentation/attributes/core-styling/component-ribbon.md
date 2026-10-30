# [ComponentRibbon]

> Adds a stylized diagonal banner ribbon across any corner of the component card for status markers such as "NEW", "BETA", "EXPERIMENTAL", or "PRO".

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentRibbon]` decorates the component card with an angled corner sash ribbon. Injected into `ComponentSlot.BodyOverlay`, it renders an angled geometric banner ribbon cutting diagonally across a chosen corner (`Corner = RibbonCorner.TopRight`, `TopLeft`, `BottomLeft`, `BottomRight`). It displays centered bold text (`Text`, `FontSize`, `FontStyle`), supporting custom background and text color styling (`BackgroundColor`, `TextColor`), ribbon width/thickness (`Thickness`), and diagonal corner displacement (`Distance`). Moreover, `AllowMultiple = true` allows tagging opposing corners (e.g. `"ALPHA"` at TopLeft and `"CRITICAL"` at TopRight).

**The Problem:**
During rapid iterative development, scripts transition through alpha, beta, experimental, or deprecated phases. Simple class comments or field notes fail to grab attention, leading to team members using unfinished or unapproved modules in production scenes.

**The Solution:**
Decorating components with `[ComponentRibbon]`:
- **Unmissable Corner Tagging:** Angled corner sashes provide immediate identification of component lifecycle stage.
- **Four Corner Anchoring:** Position ribbons at `TopRight`, `TopLeft`, `BottomRight`, or `BottomLeft` via `RibbonCorner`.
- **Multiple Allowed:** `AllowMultiple = true` allows stacking multiple ribbons across different corners simultaneously.
- **Click-Through Design:** UI Toolkit layout with `PickingMode.Ignore` ensures controls underneath remain fully interactable.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentRibbon("EXPERIMENTAL", Corner = RibbonCorner.TopRight, BackgroundColor = "#DC2626", TextColor = "#FFFFFF")]
public class ProceduralVoxelDestruction : MonoBehaviour
{
    public float voxelDebrisCount = 250f;
    public bool enableGpuAcceleration = true;
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
public ComponentRibbonAttribute(string text)
```

- `text`: Label text displayed across the diagonal ribbon (e.g. `"BETA"`, `"NEW"`).

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Text` | `string` | *(Constructor)* | Display text label rendered along the diagonal ribbon. |
| `Corner` | `RibbonCorner` | `RibbonCorner.TopRight` | Corner placement (`TopLeft`, `TopRight`, `BottomLeft`, `BottomRight`). |
| `BackgroundColor` | `string` | `"#FF3366"` | Hex background color string for the diagonal ribbon strip. |
| `TextColor` | `string` | `"#FFFFFF"` | Hex color string for ribbon text. |
| `FontSize` | `int` | `10` | Text font size in points. |
| `FontStyle` | `FontStyle` | `FontStyle.Bold` | Font styling (`Normal`, `Bold`, `Italic`). |
| `Distance` | `float` | `30f` | Perpendicular offset distance in pixels from the corner vertex. |
| `Thickness` | `float` | `20f` | Cross-sectional width/thickness in pixels of the ribbon strip. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#8B5CF6", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#100E1D", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("NEURAL ENEMY BEHAVIOR", Subtitle = "Deep Reinforcement Learning Agent", BackgroundColor = "#1D1838", TitleColor = "#EDE9FE")]
[ComponentRibbon("PREVIEW", Corner = RibbonCorner.TopRight, BackgroundColor = "#7C3AED", TextColor = "#F5F3FF", Distance = 32f, Thickness = 22f)]
[ComponentRibbon("GPU ACCEL", Corner = RibbonCorner.TopLeft, BackgroundColor = "#2563EB", TextColor = "#EFF6FF", Distance = 32f, Thickness = 22f)]
public class NeuralEnemyBehavior : MonoBehaviour
{
    [Header("Inference Model")]
    public TextAsset onnxModelAsset;
    public int inferenceBatchSize = 16;
    public float decisionEpsilonGreedy = 0.05f;

    [Header("Action Space")]
    public float movementVelocityClamp = 6.0f;
    public bool isDebugObservationVectorLogged = false;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeader]`** | High | Diagonally overlaps header corners, adding a banner ribbon look. |
| **`[ComponentBorder]`** | High | Align `Corner` placement to frame inside bordered component containers cleanly. |
| **Multiple Instances** | High | Supports multiple ribbons on different corners (e.g. `TopLeft` and `TopRight`). |
