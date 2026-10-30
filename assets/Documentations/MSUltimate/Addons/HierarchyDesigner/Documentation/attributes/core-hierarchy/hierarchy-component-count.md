# [HierarchyComponentCount]

> Displays the total attached component count directly on the hierarchy row with customizable thresholds to catch bloated GameObjects.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyComponentCount]` audits GameObject complexity directly within the scene hierarchy. Rendered via `HierarchyComponentCountRenderer`, it counts all attached components (excluding `Transform` by default via `ExcludeTransform = true`) and displays a compact numerical counter badge (e.g. `"6C"`). When component density exceeds a healthy architectural threshold (`HighCountThreshold = 8`), the badge dynamically shifts to a prominent warning alert (`HighCountColor = "#552222"`, `HighCountTextColor = "#FF8888"`), highlighting bloated entities that require refactoring.

**The Problem:**
In large projects, GameObjects frequently become monolithic "God Objects" accumulating 10 to 20 unrelated components (scripts, colliders, audio sources, particle emitters). Because component counts are only visible by selecting the object and scrolling through the Inspector, architectural bloat goes unnoticed until performance degrades.

**The Solution:**
Tagging managers and core entities with `[HierarchyComponentCount]`:
- **At-a-Glance Architectural Auditing:** Scan your hierarchy tree to instantly spot GameObjects carrying excessive components.
- **Configurable Warning Thresholds:** Set component limits (e.g., alert at 8+ components) to enforce clean component composition across teams.
- **Smart Filtering:** Ignores the ubiquitous `Transform` component (`ExcludeTransform = true`) and suppresses badges on simple objects (`MinCountToShow = 2`).
- **Zero Runtime Performance Impact:** Lightweight editor-only reflection that refreshes cleanly upon component addition or removal.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyComponentCount(MinCountToShow = 2, HighCountThreshold = 6)]
public class ModularActorController : MonoBehaviour
{
    public float movementSpeed = 6.5f;
    public bool isGrounded = true;
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
| **Render Engine** | `HierarchyComponentCountRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyComponentCountAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ExcludeTransform` | `bool` | `true` | When true, does not include the standard `Transform` component in the total count. |
| `MinCountToShow` | `int` | `2` | Minimum attached component count required before the badge is displayed. |
| `BadgeColor` | `string` | `"#334455"` | Hex background color of the badge under normal counts. |
| `TextColor` | `string` | `"#AABBCC"` | Hex text color of the count text under normal counts. |
| `BorderRadius` | `float` | `3f` | Corner rounding radius in pixels for the counter badge pill. |
| `HighCountThreshold`| `int` | `8` | Component count threshold that triggers warning color styling (or `0` to disable). |
| `HighCountColor` | `string` | `"#552222"` | Warning background hex color when count meets or exceeds threshold. |
| `HighCountTextColor`| `string` | `"#FF8888"` | Warning text hex color when count meets or exceeds threshold. |
| `Suffix` | `string` | `"C"` | Suffix string appended to the number (e.g. `"C"` for `"5C"`, or `""`). |
| `Bold` | `bool` | `true` | Whether to render the count text in bold font weight. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the component count badge remains visible in Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyComponentCount(
    ExcludeTransform = true, 
    MinCountToShow = 3, 
    HighCountThreshold = 7, 
    HighCountColor = "#7F1D1D", 
    HighCountTextColor = "#FCA5A5", 
    Suffix = " Comps", 
    XOffset = 6f)]
public class CombatVehicleMasterEntity : MonoBehaviour
{
    [Header("Vehicle Subsystems")]
    public float engineHorsepower = 850f;
    public float armorThicknessMm = 120f;
    public bool isTurretOperational = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyBadge]`** | High | Place component count badges on the right edge while placing entity identity badges to the left. |
| **`[HierarchyActiveButton]`**| High | Set `XOffset = 26f` to leave room for the inline power toggle button on the far right. |
| **Prefabs & Instances** | High | Live count accurately reflects both prefab-inherited and instance-added components. |
| **Undo Stack** | High | Immediately updates count in real time when components are added or deleted via Undo/Redo. |
