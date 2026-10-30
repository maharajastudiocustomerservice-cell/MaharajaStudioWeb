# [ContinuousRotate]

> Continuously rotates an inspector visual element (entire row, input control, or label icon) at a configurable rotational speed.

---

## 1. Overview & Value Proposition

**What it does:**
Applies a continuous rotational transform animation to an inspector element. Features targeted sub-element isolation via `AnimatedTargetElement` (`All`, `Input`, or `Label`), allowing developers to spin loading icons, gear indicators, or compass symbols continuously at a set speed (`RotationSpeed` in degrees/sec).

**The Problem:**
Indicating active background operations, spinning turbines, compass headings, or live loading states in custom inspectors normally requires manual repaint loops or gif sprites.

**The Solution:**
Add `[ContinuousRotate]` to any field:
- **Zero-Boilerplate Rotation:** Continuous smooth rotation powered by UI Toolkit style transforms.
- **Granular Targeting:** Choose whether to rotate the entire row (`All`), just the input control (`Input`), or just the label (`Label`).
- **Speed & Direction:** Positive speed values spin clockwise; negative values spin counter-clockwise.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class LoadingSpinner : MonoBehaviour
{
    [ContinuousRotate(RotationSpeed = 180f, TargetElement = AnimatedTargetElement.Label)]
    public bool isAssetLoading = false;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ContinuousRotateAttribute()
```

*Attribute initializes with standard 90 deg/sec rotation; customize properties via object initializers.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `RotationSpeed` | `float` | `90f` | Rotation speed in degrees per second (negative reverses direction). |
| `TargetElement` | `AnimatedTargetElement` | `AnimatedTargetElement.All` | Target element to rotate: `All` (entire row), `Input` (control only), `Label` (label only). |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class TurbineEngine : MonoBehaviour
{
    [Header("Engine Turbine Telemetry")]
    [ContinuousRotate(RotationSpeed = 360f, TargetElement = AnimatedTargetElement.Label)]
    public float currentTurbineRPM = 12000f;

    [Header("Radar Scanner Antenna")]
    [ContinuousRotate(RotationSpeed = 45f, TargetElement = AnimatedTargetElement.Input)]
    public float antennaAzimuthAngle = 0f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Rotates cleanly inside group cards. |
| TargetElement Isolation | Supported | Isolates rotation to icons/labels without twisting numeric inputs. |
| Primary Drawers | Supported | Retains full interactivity on the target element. |
