# [HierarchyLabel]

> Displays static descriptive text or live serialized field values directly on the hierarchy row with custom typography and alignments.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyLabel]` surfaces text strings and variable values directly into the hierarchy view. Processed by `HierarchyLabelRenderer`, it can render static descriptive text (`Text = "Zone Anchor"`) when applied to a class, or automatically mirror the live runtime value of a field (`FormatString = "{0:F1} m/s"`). It features flexible horizontal positioning (`Alignment = HierarchyLabelAlignment.Right` or `Left`), rich typography controls (bold, italic, custom colors, and font sizes), character truncation limits (`MaxLength = 16`), and optional background pill framing (`BackgroundColor`).

**The Problem:**
GameObject names are often terse or standardized for code (e.g. `Enemy_04`, `LightRig_B`), obscuring important human context such as target patrol zones, assigned audio busses, network IDs, or current speed metrics. Developers waste time clicking between objects just to read basic text details.

**The Solution:**
Decorating classes and serialized values with `[HierarchyLabel]`:
- **Live Variable Projection:** Watch string values, floats, coordinates, or states update in real time in the hierarchy list.
- **Dual Horizontal Anchoring:** Pin text flush against the right edge of the row or immediately following the GameObject name on the left.
- **Rich Typography Styling:** Format labels with bespoke colors, italic accents, bold weights, and custom font sizes.
- **Defensive Character Truncation:** Keep hierarchy layouts neat and prevent horizontal overflow using the `MaxLength` property.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class PatrolUnitMovement : MonoBehaviour
{
    [HierarchyLabel(FormatString = "Speed: {0:F1}", Color = "#38BDF8")]
    public float currentSpeed = 4.5f;

    public float maxSpeed = 10f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class | Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyLabelRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyLabelAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Text` | `string` | `""` | Static text label, or empty to display the field's live value. |
| `ShowPrefix` | `bool` | `false` | When true, prepends the field name before the displayed value. |
| `FormatString` | `string` | `"{0}"` | C# string format applied to the displayed field value (e.g. `"{0:F2}"`). |
| `MaxLength` | `int` | `16` | Maximum displayed character count before truncating with an ellipsis. |
| `Color` | `string` | `"#AAAAAA"` | Hex color string for the label typography. |
| `Bold` | `bool` | `false` | Whether to render the label text in bold font. |
| `Italic` | `bool` | `false` | Whether to render the label text in italic font. |
| `FontSize` | `int` | `0` | Font size in pixels, or `0` to inherit Unity hierarchy defaults. |
| `BackgroundColor` | `string` | `""` | Optional hex background color behind the label text. |
| `BackgroundPadding`| `float` | `2f` | Padding in pixels around the label when a background is drawn. |
| `Alignment` | `HierarchyLabelAlignment` | `Right` | Anchor side on the row (`Right` edge or `Left` next to name). |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the anchor edge. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the text label remains visible in Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyLabel(
    Text = "[AUDIO ZONE]", 
    Color = "#A78BFA", 
    Alignment = HierarchyLabelAlignment.Left, 
    Bold = true)]
public class AmbientAudioZoneAnchor : MonoBehaviour
{
    [Header("Zone Profile")]
    [Tooltip("Live acoustic profile name displayed on the right edge of the hierarchy row.")]
    [HierarchyLabel(
        FormatString = "\"{0}\"", 
        Color = "#FCD34D", 
        Alignment = HierarchyLabelAlignment.Right, 
        XOffset = 6f)]
    public string activeSoundtrackProfile = "Cathedral_Reverb_Main";

    public float blendTransitionDuration = 2.5f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyIcon]`** | High | Place an icon on the right margin while using `HierarchyLabelAlignment.Left` for subtitle text. |
| **`[HierarchyHighlight]`** | High | Text colors contrast cleanly over solid and gradient row highlights. |
| **Multi-Type Formatting** | High | Supports strings, floats, ints, vectors, and custom object `.ToString()` output. |
| **Performance** | High | Internal string formatting caches results, preventing allocations when field values are steady. |
