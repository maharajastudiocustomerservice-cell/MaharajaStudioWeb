# [LinkedField]

> Couples two numeric inspector fields with an interactive chain toggle to synchronize values proportionally, additively, or as inverse/exact mirrors.

---

## 1. Overview & Value Proposition

**What it does:**
Binds two numeric serialized fields together (such as width & height, minimum & maximum, or speed & acceleration) via an interactive chain link icon in the Inspector. When linked, editing one field automatically updates the other according to the selected mathematical mode.

**The Problem:**
In game development, many numeric values are intrinsically coupled—such as UI element dimensions, camera frustum ratios, bounding box extents, or audio pitch/reverb relationships. In default Unity, developers must manually calculate and enter reciprocal values or write custom `OnValidate` boilerplate for every pair of properties.

**The Solution:**
Applying `[LinkedField]` provides:
- **Interactive Chain Toggle:** A clickable chain icon right beside the field allows designers to toggle synchronization on or off at runtime or in edit mode.
- **Multiple Mathematical Modes:**
  - `LinkMode.Proportional`: Multiplies by the initial ratio (e.g. maintaining 16:9 aspect ratios when resizing resolution).
  - `LinkMode.Additive`: Preserves the fixed numerical difference/offset between both values.
  - `LinkMode.Mirror`: Clones the exact value across both fields simultaneously.
- **Bi-Directional Synchronization:** Changing either field updates its linked partner smoothly without infinite loop recursions.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class TextureResolutionConfig : MonoBehaviour
{
    public int textureWidth = 1920;

    [LinkedField("textureWidth", LinkMode.Proportional, startLinked: true)]
    public int textureHeight = 1080;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `int`, `float`, `double`, `long` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public LinkedFieldAttribute(string otherFieldName, LinkMode mode = LinkMode.Proportional, bool startLinked = true)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `otherFieldName` | `string` | *(Required)* | The name of the partner field or property to link with. |
| `mode` | `LinkMode` | `LinkMode.Proportional` | Mathematical linking mode (`Proportional`, `Additive`, `Mirror`). |
| `startLinked` | `bool` | `true` | Whether the chain link toggle starts active by default. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `OtherFieldName` | `string` | *(Set in constructor)* | Target field name bound for mathematical synchronization. |
| `Mode` | `LinkMode` | `LinkMode.Proportional` | Current active calculation model (`Proportional`, `Additive`, `Mirror`). |
| `StartLinked` | `bool` | `true` | Initial state of the link button upon Inspector creation. |
| `Order` | `int` | `0` | Drawing execution order in the inspector pipeline. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CameraFrustumBounds : MonoBehaviour
{
    [Header("Resolution Dimensions (16:9 Aspect Ratio Locked)")]
    public float renderWidth = 1920f;

    [LinkedField(nameof(renderWidth), LinkMode.Proportional, startLinked: true)]
    public float renderHeight = 1080f;

    [Header("Bounding Depth (Additive Delta Offset)")]
    public float nearPlane = 0.3f;

    [LinkedField(nameof(nearPlane), LinkMode.Additive, startLinked: false)]
    public float farPlane = 1000f;

    [Header("Symmetrical Particle Extents (Mirror)")]
    public float leftEmissionRate = 25f;

    [LinkedField(nameof(leftEmissionRate), LinkMode.Mirror, startLinked: true)]
    public float rightEmissionRate = 25f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Chain toggle and paired controls render compactly inside card groups. |
| `[ShowIf]` | Supported | When hidden, linking logic remains paused until condition evaluates to true. |
| `[MinMaxSlider]` | Supported | Compatible when targeting individual numeric bounds. |
| `[ReadOnly]` | Supported | Disables manual edits while preserving synchronization display. |
