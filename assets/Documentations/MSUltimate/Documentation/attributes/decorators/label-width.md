# [LabelWidth]

> Sets a fixed pixel width for the property label column to optimize horizontal space for input controls.

---

## 1. Overview & Value Proposition

**What it does:**
Overrides Unity's default 40% label column split with an exact pixel width (such as `60px` or `200px`), preventing cramped inputs.

**The Problem:**
In standard Unity, the label width is fixed across the whole inspector column. For short label names (like `X`, `HP`, `ID`), half the inspector width sits empty while the numeric input is squeezed on the right. Conversely, long names get truncated with an ellipsis.

**The Solution:**
Add `[LabelWidth]` to any field or property:
- **Reclaim Input Space:** Shrink short labels down to 40–80px so numeric fields, sliders, and object pickers have ample room.
- **Prevent Text Clipping:** Expand label width for long technical names so descriptions are readable without truncation.
- **Collection Elements:** Implements collection cascading to format element labels cleanly within lists and tables.
- **Pixel-Perfect Alignment:** Maintain exact column alignment across complex multi-variable rows.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class TransformStats : MonoBehaviour
{
    [LabelWidth(40f)]
    public float x = 10f;

    [LabelWidth(40f)]
    public float y = 20f;

    [LabelWidth(180f)]
    public string detailedPlayerDescriptor;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public LabelWidthAttribute(float width)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `width` | `float` | *(Required)* | Fixed width in pixels for the label column. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Width` | `float` | *(Required)* | Label column width in pixels. |
| `Order` | `int` | `0` | Field modifier pipeline processing order. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class AudioFilterController : MonoBehaviour
{
    [Header("Compact Sliders")]
    [LabelWidth(50f)]
    [Range(20, 20000)]
    public float low = 120f;

    [LabelWidth(50f)]
    [Range(20, 20000)]
    public float mid = 2500f;

    [LabelWidth(50f)]
    [Range(20, 20000)]
    public float high = 16000f;

    [Header("Descriptive Parameters")]
    [LabelWidth(220f)]
    public float resonanceQualityFactor = 1.414f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[LabelText]` | Recommended | Ensure custom long names fit comfortably by pairing with adequate label widths. |
| `[CustomSlider]` | Supported | Gives sliders maximum horizontal drag resolution. |
| `[BoxGroup]` | Supported | Preserves custom width overrides inside grouped panels. |
