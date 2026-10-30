# [Indent]

> Indents a field or property horizontally by a specified number of levels to express parent-child relationships and visual hierarchy.

---

## 1. Overview & Value Proposition

**What it does:**
Shifts a field horizontally to the right by one or more indentation steps (defaulting to 15 pixels per level) to clearly show sub-settings.

**The Problem:**
When toggling options (like "Enable Shadows" or "Use Custom Gravity"), dependent sub-parameters are drawn at the exact same horizontal level as the parent toggle. Without visual nesting, inspectors look flat and confusing, making it hard to see which controls belong to which toggle.

**The Solution:**
Add `[Indent]` to child settings:
- **Instant Visual Hierarchy:** Clearly signal that secondary properties depend on or belong to the setting directly above them.
- **Configurable Indentation Levels:** Pass `1`, `2`, or `3` to create deeply nested option trees.
- **Custom Pixel Step:** Adjust `PixelsPerLevel` (e.g. `20f`) to fit your studio's inspector layout guidelines.
- **Pairs with Conditionals:** Combine with `[ShowIf]` or `[EnableIf]` for clean, expandable option sub-menus.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CameraController : MonoBehaviour
{
    public bool enablePostProcessing = true;

    [Indent(1)]
    public float bloomIntensity = 1.2f;

    [Indent(1)]
    public float vignetteSpread = 0.45f;
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
public IndentAttribute(int level = 1)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `level` | `int` | `1` | Number of indent levels to shift the field horizontally to the right. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Level` | `int` | `1` | Indentation step count. |
| `PixelsPerLevel` | `float` | `15f` | Horizontal pixel offset applied per indent level. |
| `Order` | `int` | `0` | Modifier pipeline execution order. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class PlayerMovementController : MonoBehaviour
{
    [Header("Locomotion Mode")]
    public bool enableWallRun = true;

    [Indent(1)]
    [ShowIf(nameof(enableWallRun))]
    public float wallRunSpeed = 12f;

    [Indent(1)]
    [ShowIf(nameof(enableWallRun))]
    public bool allowWallJump = true;

    [Indent(2)]
    [ShowIf(nameof(allowWallJump))]
    public float wallJumpForce = 15f;

    [Indent(2)]
    [ShowIf(nameof(allowWallJump))]
    public Vector3 jumpAngleBias = new Vector3(0.5f, 1f, 0.5f);
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[ShowIf]` / `[EnableIf]` | Recommended | Essential pairing for creating clean parent-child collapsible inspector trees. |
| `[BoxGroup]` | Supported | Indentation works correctly inside group containers. |
| `[GUIColor]` | Supported | Color tints remain aligned with indented fields. |
| `[SuffixLabel]` | Supported | Suffix measurement labels respect row boundaries. |
