# [SuffixLabel]

> Appends a suffix label, unit badge, or icon to the end of a field (ideal for units like "meters", "sec", or "px").

---

## 1. Overview & Value Proposition

**What it does:**
Pins a clean measurement unit label (like `kg`, `km/h`, `sec`, or `%`) or icon badge directly on the right edge of any input field.

**The Problem:**
Numbers without units force developers to guess what they represent. Is a `speed` variable measured in meters per second, kilometers per hour, or knots? Adding units into variable names (`speedInMetersPerSecond`) creates bloated code, while omitting them leads to physics and design bugs.

**The Solution:**
Add `[SuffixLabel]` to any field:
- **Explicit Units of Measurement:** Display clear units (`sec`, `m/s`, `rad`, `dB`, `px`) right on the field.
- **Badge & Pill Styling:** Render as plain text or as a stylish pill badge with background colors and borders.
- **Icon Support:** Display accompanying icons (like clock icons for durations or ruler icons for distances).
- **Collection Cascading:** Automatically attaches suffix units to elements within lists, arrays, and tables.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class VehiclePhysics : MonoBehaviour
{
    [SuffixLabel("km/h")]
    public float topSpeed = 220f;

    [SuffixLabel("sec", colorHex: "#f39c12")]
    public float zeroToHundredTime = 3.8f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public SuffixLabelAttribute(string label)
public SuffixLabelAttribute(string label, string colorHex)
public SuffixLabelAttribute(string label, string icon, string colorHex = null)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `label` | `string` | *(Required)* | Text string displayed in the suffix badge. |
| `colorHex` | `string` | `null` | Hex text color string. |
| `icon` | `string` | `""` | Built-in Unity icon name or asset path. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Label` | `string` | *(Required)* | Suffix display string. |
| `Icon` | `string` | `""` | Optional icon identifier. |
| `TextColor` / `ColorHex` | `string` | `""` | Text color hex string. |
| `BackgroundColor` | `string` | `""` | Badge background color. |
| `IconColor` | `string` | `""` | Icon tint color. |
| `FontSize` | `float` | `12f` | Font size in pixels. |
| `Padding` | `float` | `2f` | Internal padding within the suffix badge. |
| `BorderRadius` | `float` | `0f` | Corner radius for badge styling. |
| `BorderWidth` | `float` | `0f` | Border outline thickness in pixels. |
| `BorderColor` | `string` | `""` | Hex border outline color. |
| `Placement` | `SuffixPlacement` | `SuffixPlacement.FieldRow` | Placement mode (`FieldRow`, `Below`). |
| `Order` | `int` | `0` | Execution priority relative to other decorator attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CannonBallistics : MonoBehaviour
{
    [Header("Firing Parameters")]
    [SuffixLabel("m/s", BackgroundColor = "#1a365d", TextColor = "#3498db", BorderRadius = 3f, Padding = 3f)]
    public float muzzleVelocity = 850f;

    [SuffixLabel("deg")]
    [Range(0, 90)]
    public float elevationAngle = 35f;

    [SuffixLabel("kg")]
    public float projectileMass = 25f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[FieldTag]` | Supported | Tag appears on the left near the label while suffix docks on the far right. |
| `[CustomRange]` | Supported | Suffix stays docked on the right side of the slider row. |
| `[BoxGroup]` | Supported | Nests cleanly inside box groups and tab cards. |
