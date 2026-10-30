# [HierarchyColorSwatch]

> Displays an interactive color swatch square that opens Unity's native Color Picker directly from the hierarchy row.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyColorSwatch]` binds an interactive color preview square (`Size = 12f`) directly onto the hierarchy row for `Color` or `Color32` fields or properties. Driven by `HierarchyColorSwatchRenderer`, it uses `EditorGUI.ColorField` to allow single-click opening of Unity's native Color Picker. Modifying the color records full Unity Undo history (`Undo.RecordObject`) in Edit Mode, marks components dirty, and prevents accidental GameObject selection or name renaming.

**The Problem:**
Tuning visual colors across scene lights, particle effects, UI themes, environment props, or debug markers requires repeatedly clicking GameObjects, waiting for the Inspector to load, finding the color property, tweaking it, and repeating for adjacent objects.

**The Solution:**
Decorating color fields or properties with `[HierarchyColorSwatch]`:
- **Direct Color Tweaking:** Open Unity's Color Picker straight from the hierarchy row with a single click.
- **Instant Visual Identification:** Color swatches immediately show current team colors, lighting tints, or material color states.
- **Alpha Channel Support:** Option to include or omit the alpha channel (`ShowAlpha`).
- **Supports `Color` and `Color32`:** Automatically handles both standard floating-point `UnityEngine.Color` and byte-based `UnityEngine.Color32` types.
- **Full Undo Registration:** Supports standard `Ctrl+Z` rollbacks during Edit Mode editing sessions.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class MinimapMarker : MonoBehaviour
{
    [HierarchyColorSwatch(ShowAlpha = false, Size = 13f)]
    public Color markerColor = Color.cyan;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Field`, `Property` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyColorSwatchRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyColorSwatchAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ShowAlpha` | `bool` | `true` | Whether to include alpha channel editing in the popup color picker. |
| `Size` | `float` | `12f` | Width and height in pixels of the color swatch square. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the color swatch remains visible and interactive during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class TeamZoneVolume : MonoBehaviour
{
    [Header("Team Configuration")]
    public string teamName = "Solaris";

    [HierarchyColorSwatch(ShowAlpha = true, Size = 14f, XOffset = 6f)]
    public Color teamTint = new Color(0.2f, 0.8f, 1.0f, 0.75f);

    public float zoneRadius = 25f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyStatusDot]`** | High | Use status dots for functional state indicators and color swatches for editable gameplay colors. |
| **`[HierarchyToggle]`** | High | Place color swatches alongside boolean toggles to control team colors and active status together. |
| **Field & Property Types** | High | Works directly with both `Color` and `Color32` member fields and properties. |
| **Event Consumption** | High | Automatically consumes mouse down/up clicks within the swatch rect, preventing accidental object renaming. |
