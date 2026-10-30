# [ValidateTransformReset]

> Validates that a referenced GameObject or Component has its local position, rotation, and/or scale reset to identity values (zero position, zero rotation, unit scale).

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateTransformReset]` inspects assigned `GameObject` or `Component` reference fields (such as `Transform`). It compares the target object's local transform properties against identity values:
- `localPosition` $\approx$ `Vector3.zero` (when `CheckPosition = true`)
- `localEulerAngles` $\approx$ `Vector3.zero` (when `CheckRotation = true`)
- `localScale` $\approx$ `Vector3.one` (when `CheckScale = true`)
All floating-point comparisons evaluate against a configurable `Tolerance` threshold (default `0.001f`). If any selected component deviates from identity, a validation message banner is rendered in the Inspector.

**The Problem:**
In 3D game pipelines, pivot roots, attachment sockets, and weapon mount points must remain cleanly reset to identity:
- If a character mesh pivot or weapon socket has accidental non-zero local positions or rotations, projectiles fire at skewed angles and runtime equipment snaps to misaligned coordinates.
- Non-uniform scale (e.g. `(1, 0.8, 1)`) causes physics collider distortion, incorrect raycasts, and runtime transform shear that cannot easily be undone.
- Art imports often arrive with un-reset transforms, leading to hard-to-trace visual discrepancies between authoring time and gameplay runtime.

**The Solution:**
Decorating reference fields with `[ValidateTransformReset]`:
- **Identity Enforcement:** Ensures referenced pivots, sockets, and visual roots are completely zeroed and uniformly scaled.
- **Selective Component Checks:** Independently toggle `CheckPosition`, `CheckRotation`, or `CheckScale` depending on component requirements.
- **Configurable Floating-Point Tolerance:** Adjust comparison precision with `Tolerance` (e.g. `0.001f` or `0.01f`) to prevent micro-rounding false positives.
- **Defensive Warnings:** Defaults to `InspectorMessageType.Warning` to alert designers without halting iteration workflows.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class CharacterRig : MonoBehaviour
{
    [ValidateTransformReset("Art pivot must be reset to identity to prevent misaligned runtime animations.")]
    public GameObject artPivot;

    [ValidateTransformReset("Weapon socket local position must be zeroed.", CheckPosition = true, CheckRotation = false, CheckScale = false)]
    public Transform weaponSocket;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ValidationModule Addon |
| **Attribute Target** | `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Inspector & Validation Engine Window |
| **Validation Interface** | `IValidationAttribute` |

---

## 4. Constructors & Parameters

```csharp
public ValidateTransformResetAttribute(string message = "Transform must be at identity (position/rotation/scale not reset).")
```

- **`message`** (`string`, optional): Custom error message displayed upon validation failure. Default is `"Transform must be at identity (position/rotation/scale not reset)."`.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `CheckPosition` | `bool` | `true` | Asserts `localPosition` is `Vector3.zero` within `Tolerance`. |
| `CheckRotation` | `bool` | `true` | Asserts `localEulerAngles` is `Vector3.zero` within `Tolerance`. |
| `CheckScale` | `bool` | `true` | Asserts `localScale` is `Vector3.one` within `Tolerance`. |
| `Tolerance` | `float` | `0.001f` | Floating-point epsilon used for vector comparisons. |
| `Message` | `string` | `"Transform must be at identity..."` | Failure explanation displayed in the validation message banner. |
| `MessageType` | `InspectorMessageType` | `InspectorMessageType.Warning` | Visual severity badge (`None`, `Info`, `Warning`, `Error`). |
| `ErrorColor` | `string` | `null` | Hex text color override for the validation error banner. |
| `ErrorBackgroundColor` | `string` | `null` | Hex background color override for the alert box. |
| `FontSize` | `int` | `0` | Font size override in pixels (0 uses default inspector font size). |
| `Padding` | `float` | `0f` | Internal padding around the validation banner. |
| `Margin` | `float` | `5f` | Outer margin spacing separating the banner from neighboring controls. |

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.ValidationModule;

namespace ProjectZero.Weapons
{
    public class WeaponAttachmentRig : ModularMonoBehaviour
    {
        [Header("Mount Point Sockets")]
        [ValidateTransformReset("Barrel muzzle socket must be at local origin.",
            CheckPosition = true,
            CheckRotation = false,
            CheckScale = false,
            MessageType = InspectorMessageType.Error)]
        public Transform muzzleSocket;

        [Header("Optics Rail (Position + Rotation)")]
        [ValidateTransformReset("Scope mount rotation and position must be zeroed for accurate aiming raycasts.",
            CheckPosition = true,
            CheckRotation = true,
            CheckScale = false,
            MessageType = InspectorMessageType.Warning)]
        public Transform opticsRail;

        [Header("Physics Prop (Uniform Unit Scale)")]
        [ValidateTransformReset("Prop mesh scale must be exactly (1,1,1) to avoid distorted collider physics.",
            CheckPosition = false,
            CheckRotation = false,
            CheckScale = true,
            Tolerance = 0.005f,
            ErrorColor = "#FF4444")]
        public GameObject propMesh;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateNotNull]` / `[Required]`**| High | Guard target reference before evaluating transform vectors. |
| **`[ValidateRequiresParent]`** | High | Guarantee the object is parented before checking local transform relative coordinates. |
| **`[ValidateNoParent]`** | High | Ensure root entities stay at origin without parenting interference. |
| **Validation Engine** | Native | Audited automatically during scene-wide and prefab validation batch runs. |
