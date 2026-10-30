# [HierarchyLayerCollisionMatrix]

> Displays a compact hierarchy badge showing how many layers can physically collide with this GameObject's layer.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyLayerCollisionMatrix]` renders an interactive telemetry badge directly on the GameObject's hierarchy row indicating how many physics layers are configured to collide with the GameObject's current layer in Unity's Physics Collision Matrix. It supports both 3D Physics (`Physics.GetIgnoreLayerCollision`) and 2D Physics (`Physics2D.GetIgnoreLayerCollision`).

**The Problem:**
Diagnosing unintended physics interactions or dead collision events in Unity requires opening `Project Settings > Physics` or `Physics 2D`, scrolling through a massive grid of 32x32 checkboxes, and manually calculating which layer combinations are active. When objects are assigned improper layers (e.g. `Default` colliding with everything, or a `Projectile` layer colliding with nothing), physics performance degrades or critical gameplay triggers fail silently.

**The Solution:**
Decorating components with `[HierarchyLayerCollisionMatrix]`:
- **Instant Collision Audit:** See at a glance how many layers collide with this object (e.g. `⚡ 6 Layers` or `⚡ 0 Layers` if completely ignored).
- **Zero Configuration Setup:** Automatically extracts the GameObject's active layer (`gameObject.layer`) and cross-references the project collision matrix.
- **2D & 3D Physics Modes:** Toggle between 3D physics evaluation and 2D physics matrix with a single boolean property (`Show2DPhysics = true`).
- **Visual Styling:** Customize badge background (`BadgeColor`), text color (`TextColor`), and border outline (`BorderColor`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyLayerCollisionMatrix]
public class CombatHitbox : MonoBehaviour
{
    public float damage = 25f;
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
| **Render Engine** | `HierarchyLayerCollisionMatrixRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyLayerCollisionMatrixAttribute()
```

- Parameterless constructor defaults to 3D physics analysis, customizable via named properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Show2DPhysics` | `bool` | `false` | When true, evaluates Unity's `Physics2D` collision matrix instead of 3D `Physics`. |
| `BadgeColor` | `string` | `"#1E2A38"` | Hex background color of the collision telemetry badge. |
| `TextColor` | `string` | `"#55AAFF"` | Hex text color displaying the active colliding layer count. |
| `BorderColor` | `string` | `"#2C4058"` | Hex border outline color framing the badge pill. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right edge of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the collision matrix badge continues evaluating during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row decorations. |

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

namespace ProjectZero.Physics
{
    // High-speed projectile ensuring layer matrix isolates it from hitting friendly units
    [RequireComponent(typeof(Rigidbody))]
    [HierarchyLayerCollisionMatrix(
        Show2DPhysics = false,
        BadgeColor = "#2D1B36",
        TextColor = "#D980FA",
        BorderColor = "#572F6E",
        XOffset = 6f)]
    public class KineticMissile : MonoBehaviour
    {
        public float velocity = 50f;
        public float blastRadius = 5f;
    }

    // 2D platformer hazard auditing 2D physics collision layers
    [RequireComponent(typeof(Collider2D))]
    [HierarchyLayerCollisionMatrix(
        Show2DPhysics = true,
        BadgeColor = "#1B2A1E",
        TextColor = "#2ED573",
        BorderColor = "#266B38")]
    public class AcidPool2D : MonoBehaviour
    {
        public float dps = 15f;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyTooltip]`** | High | Hovering over the row can provide detailed notes on the intended layer matrix design. |
| **`[HierarchyRaycastAudit]`** | High | Combine 2D/3D physics collision audit with UI raycast auditing for comprehensive scene profiling. |
| **`[HierarchyTransformWarning]`** | High | Simultaneously monitor collision matrix layer health and non-uniform scale warnings on physics bodies. |
| **`[HierarchyFolder]`** | High | Group physics triggers inside dedicated hierarchy folders for streamlined scene management. |
