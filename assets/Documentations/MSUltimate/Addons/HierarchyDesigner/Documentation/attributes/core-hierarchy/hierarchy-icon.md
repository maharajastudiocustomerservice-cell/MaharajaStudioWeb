# [HierarchyIcon]

> Displays built-in or custom icon badges on the hierarchy row statically or dynamically based on field states.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyIcon]` equips hierarchy rows with clear visual symbols representing component roles or runtime states. Processed by `HierarchyIconRenderer`, it draws any built-in Unity editor icon or custom texture (`IconName = "d_FilterByType"`, `Size = 14f`) alongside the object entry. It supports custom hex tinting (`Tint = "#10B981"`), hover tooltips (`Tooltip`), multi-icon slot stacking (`StackSlot = 0`), and conditional field visibility rules (`ShowCondition = HierarchyIconCondition.Always`, `WhenTrue`, `WhenFalse`, `WhenNotNull`, `WhenNull`).

**The Problem:**
By default, Unity shows only a generic blue cube prefab icon or an empty GameObject icon in the Hierarchy. Distinguishing cameras, light sources, trigger colliders, audio zones, or AI pathfinding nodes at a glance requires reading long name strings.

**The Solution:**
Tagging components and field states with `[HierarchyIcon]`:
- **Instant Visual Semantics:** Display unmistakable icons for lights, cameras, audio clips, weapons, and physics bodies.
- **Dynamic Field-State Display:** Automatically reveal warning icons when a critical object reference is null (`WhenNull`) or when a state flag is active (`WhenTrue`).
- **Multi-Icon Horizontal Stacking:** Stack multiple diagnostic icons side by side using deterministic `StackSlot` indices.
- **Custom Icon Tinting:** Colorize standard monochrome editor icons to match team color coding conventions.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyIcon(IconName = "d_Light", Tint = "#FBBF24", Tooltip = "Point Light Source")]
public class CustomLampFixture : MonoBehaviour
{
    public float lightRadius = 10f;
    public Color lampColor = Color.yellow;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class | Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyIconRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyIconAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `IconName` | `string` | `"d_FilterByType"` | Built-in Unity icon name or asset path to render. |
| `Size` | `float` | `14f` | Icon dimension in pixels (width and height). |
| `XOffset` | `float` | `0f` | Horizontal offset in pixels from the right margin. |
| `StackSlot` | `int` | `0` | Slot index for stacking multiple icons side-by-side horizontally. |
| `Tint` | `string` | `""` | Optional hex color tint applied to the icon texture. |
| `ShowCondition` | `HierarchyIconCondition` | `Always` | Display condition for field-level icons (`Always`, `WhenTrue`, `WhenFalse`, `WhenNotNull`, `WhenNull`). |
| `Tooltip` | `string` | `""` | Informational tooltip displayed upon hovering over the icon. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the icon badge remains visible in Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyIcon(IconName = "d_Camera Icon", Tint = "#38BDF8", Tooltip = "Cinematic Virtual Camera Anchor")]
public class CinematicVirtualCamera : MonoBehaviour
{
    [Header("Tracking Target")]
    [Tooltip("Shows a red warning icon in the hierarchy if the target is unassigned.")]
    [HierarchyIcon(
        IconName = "d_console.warnicon", 
        Tint = "#EF4444", 
        ShowCondition = HierarchyIconCondition.WhenNull, 
        StackSlot = 1, 
        Tooltip = "Missing Target Reference!")]
    public Transform followTarget;

    [Header("Camera Settings")]
    public float fieldOfView = 60f;
    public float blendDurationSec = 1.5f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyBadge]`** | High | Use `StackSlot` or `XOffset` to arrange icons cleanly alongside text badges. |
| **Missing Reference Auditing** | High | Pairing `ShowCondition = WhenNull` with a warning icon catches unlinked fields instantly. |
| **Built-in Unity Icons** | High | Supports all standard Unity Editor icon strings (e.g. `"d_Light"`, `"d_Camera Icon"`, `"d_AudioSource Icon"`). |
| **Hierarchy Hovering** | High | Native hover detection provides responsive tooltip bubbles during scene navigation. |
