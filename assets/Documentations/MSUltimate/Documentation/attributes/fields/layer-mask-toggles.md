# [LayerMaskToggles]

> Renders a LayerMask or integer bitfield as an interactive visual toggle grid or pill buttons with selection tools.

---

## 1. Overview & Value Proposition

**What it does:**
Expands standard dropdown LayerMask fields into a multi-column visual grid of toggle buttons with 1-click `All`, `None`, and `Invert` controls.

**The Problem:**
Unity's built-in LayerMask dropdown requires clicking to open a long checklist every time you want to verify or change collision layers. You cannot see which layers are active without opening the dropdown, and toggling multiple layers requires repeatedly clicking into the menu.

**The Solution:**
Add `[LayerMaskToggles]` to any LayerMask or integer bitmask:
- **Instant Visual Overview:** See every enabled and disabled physics layer clearly without clicking open a menu.
- **1-Click Quick Selection:** Includes fast `All`, `None`, and `Invert` selection action buttons.
- **Multi-Column Grid Layouts:** Configure fixed columns (`Columns = 2, 3, 4`) or let them flex-wrap dynamically.
- **Pill or Checkbox Styles:** Choose between modern rounded pill tags or traditional checkboxes.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class RaycastShooter : MonoBehaviour
{
    [LayerMaskToggles]
    public LayerMask hitLayers;

    [LayerMaskToggles(usePillStyle: true, colorHex: "#e74c3c")]
    public LayerMask obstacleOcclusionLayers;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Field | AttributeTargets.Property` |
| **Supported Types** | `LayerMask`, `int` (bitmask), `uint` |
| **Collection Interface** | `ICollectionElementAttribute` |
| **Collection Cascading** | Full (`List<LayerMask>`, `LayerMask[]`, `int[]`, `AdvancedList<LayerMask>`) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public LayerMaskTogglesAttribute()
public LayerMaskTogglesAttribute(int columns)
public LayerMaskTogglesAttribute(bool usePillStyle, string colorHex = null)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `columns` | `int` | `0` | Number of columns in grid layout (`0` = auto flex-wrap). |
| `usePillStyle` | `bool` | `false` | Renders modern compact pill buttons instead of checkboxes. |
| `colorHex` | `string` | `null` | Hex accent color for active layers (e.g. `"#3498db"`). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Columns` | `int` | `0` | Column count in the button grid. |
| `UsePillStyle` | `bool` | `false` | Pill button mode toggle. |
| `ShowBuiltinLayers` | `bool` | `true` | Includes default built-in layers (Default, Water, UI). |
| `ShowInvertButton` | `bool` | `true` | Displays the 1-click 'Invert' selection button. |
| `ColorHex` | `string` | `null` | Active layer highlight hex color. |
| `CustomLabel` | `string` | `null` | Custom field display label override. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class ExplosiveProjectile : MonoBehaviour
{
    [Serializable]
    public class ScanProfile
    {
        public string profileName = "Ground Radar";

        [LayerMaskToggles(usePillStyle: true, ColorHex = "#8B5CF6")]
        public LayerMask detectionMask = ~0;
    }

    [Header("Blast Collision Filter")]
    [LayerMaskToggles(columns: 3, ShowInvertButton = true, ColorHex = "#e67e22")]
    public LayerMask damageTargetLayers;

    [Header("Line of Sight Occluders")]
    [LayerMaskToggles(usePillStyle: true, ColorHex = "#3498db")]
    public LayerMask visionBlockers;

    [Header("Perception Profile (Inside Class)")]
    public ScanProfile primaryScan = new ScanProfile();

    [Header("Direct Collection Cascading")]
    [LayerMaskToggles(usePillStyle: true, ColorHex = "#10B981")]
    public LayerMask[] sensorPassFilters = new LayerMask[] { 1 << 0, (1 << 0) | (1 << 1) };

    [LayerMaskToggles(columns: 3, ShowBuiltinLayers = false, ColorHex = "#38BDF8")]
    public List<LayerMask> raycastScanProfiles = new List<LayerMask> { ~0, 1 << 0 };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[LayerSelector]` | Alternative | Use `[LayerSelector]` for single-layer integers; use `[LayerMaskToggles]` for multi-layer bitmasks. |
| `[BoxGroup]` | Supported | Grid wraps neatly inside boxed group panels and tabs. |
| `[ReadOnly]` | Supported | Displays active layers clearly while disabling toggle clicks. |

### Collection Cascading Matrix

| Collection Type | Cascading Behavior | Presentation Mode |
| :--- | :---: | :--- |
| `LayerMask[]` | **Supported** | Renders full interactive toggle grid or pill buttons per array element row. |
| `List<LayerMask>` | **Supported** | Multi-column grid wraps cleanly within reorderable list rows. |
| `int[]` (Bitmasks) | **Supported** | Bitwise layer toggles operate seamlessly on primitive integer arrays. |
| `AdvancedList<LayerMask>` | **Supported** | Fully compatible with reorderable lists and batch actions. |
| `SerializableDictionary<K, V>` | **Supported** | Cascades to dictionary value fields matching `LayerMask` or `int`. |
| Nested `[Serializable]` Classes | **Supported** | Fully supported across complex serialized structures. |
