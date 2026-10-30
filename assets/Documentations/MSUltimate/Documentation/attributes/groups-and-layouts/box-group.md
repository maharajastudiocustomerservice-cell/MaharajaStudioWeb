# [BoxGroup]

> Groups fields, properties, and methods into a framed inspector box with styled headers, custom background fills, and borders.

---

## 1. Overview & Value Proposition

**What it does:**
Encloses related serialized fields, properties, and buttons inside a styled, framed box container with a distinct header bar. All members sharing the same `groupName` are clustered together automatically into the same visual card.

**The Problem:**
Standard Unity inspectors display hundreds of properties in an endless uninterrupted gray list. Without clear visual boundaries, related parameters (such as movement speeds, stamina costs, or audio settings) bleed together, resulting in cognitive fatigue and accidental parameter mistakes.

**The Solution:**
Add `[BoxGroup("GroupName")]` to any member:
- **Automatic Member Grouping:** Decorate multiple fields with the same group name to automatically gather them into a single container.
- **Custom Header Styling:** Customize header labels, font sizes, colors, alignments, and backgrounds.
- **Framed Card Aesthetics:** Adjust border widths, border colors, corner radii, and body background colors to match your studio's design language.
- **Method & Button Support:** Group utility methods alongside the variables they manipulate.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CharacterStats : MonoBehaviour
{
    [BoxGroup("Combat Attributes")]
    public int health = 100;

    [BoxGroup("Combat Attributes")]
    public float defenseRating = 25.5f;

    [BoxGroup("Combat Attributes")]
    public float attackSpeed = 1.2f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property | Method` |
| **Supported Types** | Any serialized type or method |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Drawer Resolution** | Handled natively by MSUltimate Inspector layout engine |

---

## 4. Constructors & Parameters

```csharp
public BoxGroupAttribute(string groupName)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `groupName` | `string` | *(Required)* | Unique name for the box group; also used as the default header label. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `GroupName` | `string` | *(Set in constructor)* | Identifying key that unites fields into this box. |
| `ShowLabel` | `bool` | `true` | Whether to draw the header title bar on the box. |
| `CenterLabel` | `bool` | `false` | Centers the header text horizontally across the card. |
| `LabelColor` | `string` | `null` | Hex text color for the header label. |
| `LabelFontSize` | `int` | `0` | Header font size in pixels (`0` = default). |
| `LabelFontStyle` | `FontStyle` | `FontStyle.Bold` | Font style for header text (`Bold`, `Normal`, `Italic`, etc.). |
| `LabelAlignment` | `TextAnchor` | `TextAnchor.UpperLeft` | Text alignment for the header label. |
| `BackgroundColor` | `string` | `null` | Hex fill color for the box body area. |
| `BorderColor` | `string` | `null` | Hex outline border color. |
| `BorderWidth` | `float` | `1f` | Border outline thickness in pixels. |
| `BorderRadius` | `float` | `3f` | Corner radius for the box in pixels. |
| `HeaderBackgroundColor`| `string`| `null` | Hex background color specifically for the header bar. |
| `HeaderBorderColor` | `string` | `null` | Hex border color specifically for the header bar. |
| `HeaderBorderWidth` | `float` | `0f` | Border width specifically for the header area. |
| `Padding` | `float` | `5f` | Internal padding around content within the box. |
| `MarginTop` | `float` | `5f` | Spacing above the box container in pixels. |
| `MarginBottom` | `float` | `5f` | Spacing below the box container in pixels. |
| `Order` | `int` | `0` | Execution priority in the inspector pipeline (inherited from `ModularAttribute`). |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class TurretDefenseController : MonoBehaviour
{
    [BoxGroup("Targeting Radar", CenterLabel = true, LabelColor = "#3498db", BorderColor = "#2980b9", BorderRadius = 6f)]
    public float scanRadius = 25f;

    [BoxGroup("Targeting Radar")]
    public LayerMask targetMask;

    [BoxGroup("Targeting Radar")]
    public bool lockOnAirUnits = true;

    [BoxGroup("Weapon Calibration", LabelColor = "#e74c3c", BorderColor = "#c0392b", BorderRadius = 6f)]
    public float roundsPerMinute = 450f;

    [BoxGroup("Weapon Calibration")]
    public float bulletSpreadAngle = 2.5f;

    [BoxGroup("Weapon Calibration")]
    [Button("Calibrate Weapon Zero")]
    public void CalibrateZero()
    {
        Debug.Log("Turret weapon calibrated.");
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Button]` | Supported | Methods marked with `[Button]` can be grouped seamlessly alongside fields. |
| `[ShowIf]` | Supported | Hides individual fields within the box, or collapses the box if all fields hide. |
| `[ReadOnly]` | Supported | Individual members inside the box can be locked while others remain editable. |
| Inner Drawers | Supported | Full support for nested attributes (`[MinMaxSlider]`, `[AutoFill]`, `[TagSelector]`). |
