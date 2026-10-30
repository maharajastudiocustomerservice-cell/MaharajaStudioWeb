# [HierarchyTreeBranch]

> Draws visual tree branch connector lines linking parents to children in the hierarchy window.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyTreeBranch]` renders smooth, anti-aliased guide lines (using `Handles.DrawAAPolyLine`) and endpoint junction dots (`Handles.DrawSolidDisc`) connecting nested child GameObjects directly to their parent foldout anchor in the Unity Hierarchy window.

**The Problem:**
In standard Unity, child indentations in the Hierarchy window are subtle and lack vertical guide lines. In deep hierarchies (such as skeletal rigs, complex UI canvases, or nested environmental prefabs), it is difficult to visually trace which parent a deeply nested entity belongs to, often leading to accidental misparenting or dragging into wrong groups.

**The Solution:**
Decorating parent or child MonoBehaviour classes with `[HierarchyTreeBranch]`:
- **Visual Branch Tracing:** Renders clear L-shaped and T-shaped connector lines from the parent foldout level to each child row.
- **Terminal Dot Indicators:** Optionally places crisp circular dots (`ShowDots = true`, `DotRadius = 2.0f`) at branch endpoints.
- **Custom Aesthetic Styling:** Fully configurable line color (`LineColor`), line thickness (`LineWidth`), and opacity (`LineAlpha`).
- **Dynamic Sibling Handling:** Automatically differentiates intermediate siblings (continuous vertical line) from the last sibling (terminating L-junction).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyTreeBranch(LineColor = "#5A8DEE", LineWidth = 1.5f, LineAlpha = 0.6f)]
public class NestedNodeComponent : MonoBehaviour
{
    public string nodeIdentifier;
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
| **Render Engine** | `HierarchyTreeBranchRenderer (IMGUI / Handles)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyTreeBranchAttribute()
```

- Standard parameterless constructor. Branch styling is configured via named object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `LineColor` | `string` | `"#5A8DEE"` | Hex color string for tree branch connector lines. |
| `LineWidth` | `float` | `1.5f` | Thickness of branch connector lines in pixels. |
| `LineAlpha` | `float` | `0.5f` | Opacity multiplier applied to `LineColor`. |
| `ShowDots` | `bool` | `true` | Whether to draw a circular disc at branch horizontal endpoints. |
| `DotRadius` | `float` | `2.0f` | Radius in pixels of endpoint junction dots. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether branch lines remain visible during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyTreeBranch(
    LineColor = "#38BDF8", 
    LineWidth = 2.0f, 
    LineAlpha = 0.8f, 
    ShowDots = true, 
    DotRadius = 2.5f)]
public class CharacterBoneRigNode : MonoBehaviour
{
    [Header("Rig Configuration")]
    public HumanBodyBones boneType = HumanBodyBones.Hips;
    public Transform targetConstraint;
    public bool isIKTarget = false;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyFolder]`** | High | Pair with virtual folders so children underneath display neat tree branch connectors. |
| **`[HierarchyChildCounter]`** | High | Display total child count badges alongside branch tracing lines for nested hierarchies. |
| **`[HierarchyBreadcrumb]`** | High | Combines parent-to-child tree lines with explicit ancestor name path breadcrumbs. |
| **`[HierarchyBookmark]`** | High | Branch connector lines draw behind bookmark ribbons without visual collision. |
