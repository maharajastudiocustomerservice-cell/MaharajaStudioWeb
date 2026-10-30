# [AdvancedCurve]

> Renders an enhanced, high-precision AnimationCurve editor field with custom graph colors, coordinate bounds, and background styling.

---

## 1. Overview & Value Proposition

**What it does:**
Transforms standard AnimationCurve fields into styled, color-coded curve editors with custom graph coordinate ranges.

**The Problem:**
In standard Unity, all curve fields look identical: a tiny green curve on a grey background locked to a default (0 to 1) coordinate box. When designing recoil curves, damage falloff, or camera shake that need negative values or specific ranges (like -180° to 180°), Unity's default curve picker requires opening multiple popup windows and manual panning.

**The Solution:**
Add `[AdvancedCurve]` above any `AnimationCurve` field:
- **Custom Coordinate Ranges:** Lock graph bounds (e.g. X: 0 to 10s, Y: -50 to 50) directly from code.
- **Color-Coded Curves:** Set curve stroke color via hex codes (e.g. orange for explosion falloff, cyan for shield recharge).
- **Custom Dimensions:** Adjust graph height and padding to fit comfortably into your inspector layout.
- **Embedded Labeling:** Customize label colors, widths, and styling for quick visual recognition.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class RecoilPattern : MonoBehaviour
{
    [AdvancedCurve(0f, -10f, 1f, 20f, "#FF5722")]
    public AnimationCurve verticalKickCurve = AnimationCurve.Linear(0, 0, 1, 10);
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `AnimationCurve`, `AnimationCurve[]`, `List<AnimationCurve>`, `SerializableDictionary<K, AnimationCurve>` |
| **Collection Interface** | `ICollectionElementAttribute` (Automatic Element Cascading) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public AdvancedCurveAttribute()
public AdvancedCurveAttribute(string colorHex)
public AdvancedCurveAttribute(float rectX, float rectY, float rectWidth, float rectHeight, string colorHex = null)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `colorHex` | `string` | `null` | Hex color code for the rendered curve stroke line (e.g. `"#E74C3C"`). |
| `rectX` | `float` | `0f` | Minimum horizontal start coordinate value on the graph. |
| `rectY` | `float` | `0f` | Minimum vertical start coordinate value on the graph. |
| `rectWidth` | `float` | `1f` | Total width duration range along the X axis. |
| `rectHeight` | `float` | `1f` | Total height value range along the Y axis. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ColorHex` | `string` | `null` | Curve line stroke color hex string. |
| `BackgroundColor` | `string` | `null` | Graph canvas background hex color. |
| `Height` | `float` | `0f` | Explicit pixel height for the curve preview area (0 = default). |
| `UseCustomRect` | `bool` | `false` | Enables custom coordinate rectangle boundaries. |
| `RectX` | `float` | `0f` | Horizontal start coordinate. |
| `RectY` | `float` | `0f` | Vertical start coordinate. |
| `RectWidth` | `float` | `1f` | Width/duration range of the curve. |
| `RectHeight` | `float` | `1f` | Height/value range of the curve. |
| `ShowLabel` | `bool` | `true` | Shows or hides the property name label. |
| `LabelColor` | `string` | `null` | Custom hex color for the label text. |
| `LabelWidth` | `float` | `0f` | Fixed width for label (0 = default inspector split). |
| `BorderColor` | `string` | `null` | Outline border hex color. |
| `BorderWidth` | `float` | `0f` | Outline border line thickness. |
| `BorderRadius` | `float` | `0f` | Corner rounding radius in pixels. |
| `Padding` | `float` | `0f` | Inner padding in pixels. |
| `MarginTop` | `float` | `4f` | Spacing above the field in pixels. |
| `MarginBottom` | `float` | `4f` | Spacing below the field in pixels. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class ExplosionForceController : MonoBehaviour
{
    [Header("Blast Wave Dynamics")]
    [AdvancedCurve(0f, 0f, 25f, 1000f, "#F39C12",
        Height = 45f,
        BackgroundColor = "#1A1A24"
    )]
    public AnimationCurve blastDamageByDistance = AnimationCurve.EaseInOut(0, 1000, 25, 0);

    [Header("Direct Collections Cascading")]
    [AdvancedCurve(ColorHex = "#38BDF8", Height = 40f, BackgroundColor = "#0F172A")]
    public AnimationCurve[] vehicleGearTorqueCurves = new AnimationCurve[]
    {
        AnimationCurve.EaseInOut(0f, 100f, 1f, 300f),
        AnimationCurve.EaseInOut(0f, 200f, 1f, 450f)
    };

    [AdvancedCurve(ColorHex = "#10B981", Height = 40f)]
    public List<AnimationCurve> comboTrajectoryCurves = new List<AnimationCurve>
    {
        AnimationCurve.Linear(0f, 0f, 0.5f, 1.2f)
    };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Nests cleanly inside box layouts and cards. |
| `[ShowIf]` | Supported | Conditionally reveals the curve editor when relevant modes are active. |
| `[ReadOnly]` | Supported | Locks curve editing while preserving visual rendering. |

### Collection Cascading Matrix

| Collection / Container Type | Cascading Support | Render Target | Notes |
| :--- | :---: | :--- | :--- |
| `AnimationCurve[]` | ✅ Yes | Individual array items | Each curve row renders with styled line color, height, and custom rect. |
| `List<AnimationCurve>` | ✅ Yes | Individual list items | Renders embedded curve cards for every element in the list. |
| `AdvancedList<AnimationCurve>` | ✅ Yes | Individual list rows | Supports item reordering and animated additions with custom curve views. |
| `SerializableDictionary<K, AnimationCurve>` | ✅ Yes | Value cells | Curve values display interactive custom curve preview in dictionary table. |
| `SerializableTuple<..., AnimationCurve>` | ✅ Yes | Tuple curve element | Renders styled curve field inside tuple column. |

