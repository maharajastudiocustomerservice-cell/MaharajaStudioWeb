# [HierarchyTransformWarning]

> Displays an alert badge if the GameObject has non-uniform or negative scale values, preventing physics and rendering bugs.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyTransformWarning]` inspects the GameObject's local transform scale vector (`transform.localScale`). If the scale components are non-uniform (`X != Y != Z`, when `CheckNonUniformScale = true`) or if any component has negative values (`X < 0 || Y < 0 || Z < 0`, when `CheckNegativeScale = true`), it renders an immediate alert badge on the hierarchy row.

**The Problem:**
In Unity 3D, non-uniform scaling on parent objects causes skewed child rotations, distorted capsule colliders, stretched particle emitters, and broken lighting normals. Negative scaling (often used by artists to flip meshes) can invert face normals, corrupt backface culling, and break PhysX collision detection algorithms. Discovering these transform anomalies usually only happens after bizarre physics or visual glitches occur in Play Mode.

**The Solution:**
Decorating components with `[HierarchyTransformWarning]`:
- **Proactive Scale Guarding:** Immediately highlights non-uniform or negative scaling directly in the Hierarchy before playtesting or baking.
- **Configurable Checks:** Independently toggle non-uniform scale audits (`CheckNonUniformScale`) and negative scale audits (`CheckNegativeScale`).
- **Physics & Mesh Safety:** Protects physics colliders and skinned meshes from subtle deformation artifacts.
- **Visual Alert Tint:** Customize alert badge color (`AlertColor`) to fit studio visual standards.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyTransformWarning]
public class PhysicsObstacle : MonoBehaviour
{
    public float mass = 50f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyTransformWarningRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyTransformWarningAttribute()
```

- Parameterless constructor with both non-uniform scale and negative scale checks enabled by default.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `CheckNonUniformScale` | `bool` | `true` | When true, flags an alert if local scale components are non-uniform (`X != Y != Z`). |
| `CheckNegativeScale` | `bool` | `true` | When true, flags an alert if any local scale component is negative (`< 0`). |
| `AlertColor` | `string` | `"#FF4757"` | Hex color code used for the transform warning alert badge. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether transform warning auditing continues during active Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row renderers. |

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

namespace ProjectZero.Physics
{
    // High-precision trigger volume requiring strictly uniform positive scaling
    [RequireComponent(typeof(SphereCollider))]
    [HierarchyTransformWarning(
        CheckNonUniformScale = true,
        CheckNegativeScale = true,
        AlertColor = "#E84118",
        XOffset = 6f)]
    public class ProximityRadarSphere : MonoBehaviour
    {
        public float scanRadius = 10f;
        public LayerMask detectionLayers;

        private void OnValidate()
        {
            // Optional editor clamp companion
            if (transform.localScale.x != transform.localScale.y || transform.localScale.y != transform.localScale.z)
            {
                Debug.LogWarning($"[ProximityRadarSphere] Non-uniform scale on {name} may distort sphere collision geometry!", this);
            }
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyLayerCollisionMatrix]`** | High | Combine physics collision matrix audits with physical transform scale validation. |
| **`[HierarchyPrefabState]`** | High | Audit prefab override drift while monitoring accidental scaling transforms. |
| **`[HierarchyRequirementCheck]`** | High | Validate presence of required colliders while ensuring uniform geometry scales. |
| **`[HierarchyTooltip]`** | High | Hover tooltip provides notes explaining why uniform scale is required on the object. |
