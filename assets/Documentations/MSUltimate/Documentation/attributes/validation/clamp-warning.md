# [ClampWarning]

> Displays a non-intrusive warning box when a numeric value falls outside a recommended soft range without hard clamping.

---

## 1. Overview & Value Proposition

**What it does:**
Monitors numeric fields (float, int, double, etc.) against a recommended "soft" boundary range. If the value falls below `SoftMin` or exceeds `SoftMax`, it renders a styled non-intrusive warning banner directly beneath the field in the Inspector without forcibly clamping or reverting the user's input.

**The Problem:**
Hard limits (`[Range]`, `Mathf.Clamp`) prevent designers from testing edge-case values or extreme tuning outside typical limits. Conversely, having no feedback allows accidental out-of-spec values that cause physics explosions or performance degradation.

**The Solution:**
Add `[ClampWarning]` to numeric fields:
- **Soft Guidance:** Warns developers when values are outside recommended ranges without hard restriction.
- **Custom Warnings:** Specify a clear reason message (e.g. `"Velocities > 50 m/s may cause physics tunneling"`).
- **Customizable Theming:** Pick custom warning border and text colors via `ColorHex`.
- **Collection Support:** Validates elements inside arrays or lists individually via `ICollectionElementAttribute`.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class Projectile : MonoBehaviour
{
    [ClampWarning(10f, 100f, "High velocities may require continuous collision detection!", "#e67e22")]
    public float launchSpeed = 50f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `float`, `int`, `double`, `byte`, `short`, `long` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ClampWarningAttribute(float softMin, float softMax, string message = "Value outside recommended range!", string colorHex = "#e67e22")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `softMin` | `float` | *(Required)* | Recommended soft minimum threshold. |
| `softMax` | `float` | *(Required)* | Recommended soft maximum threshold. |
| `message` | `string` | `"Value outside recommended range!"` | Warning message text shown when outside boundaries. |
| `colorHex` | `string` | `"#e67e22"` | Hex color code for the warning banner. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `SoftMin` | `float` | *(Constructor)* | Recommended lower soft boundary limit. |
| `SoftMax` | `float` | *(Constructor)* | Recommended upper soft boundary limit. |
| `Message` | `string` | *(Constructor)* | Warning message displayed when out of bounds. |
| `ColorHex` | `string` | `"#e67e22"` | Hex color string for warning background and border. |
| `Order` | `int` | `100` | Execution priority relative to other attributes on the same member (defaults to 100). |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class AudioEmitterConfig : MonoBehaviour
{
    [Header("Volume Gain Settings")]
    [ClampWarning(0f, 1.2f, "Volumes exceeding 1.2 may distort or clip audio mixers!")]
    public float masterGain = 1.0f;

    [Header("Audible Distance Threshold")]
    [ClampWarning(5f, 150f, "Distances > 150m may impact sound occlusion performance.")]
    public float maxAudibleDistance = 50f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Warning box renders neatly inside group containers. |
| `[ShowIf]` | Supported | Warning dynamically appears or hides alongside the field. |
| `ICollectionElement` | Supported | Validates each numeric item inside lists and arrays. |
