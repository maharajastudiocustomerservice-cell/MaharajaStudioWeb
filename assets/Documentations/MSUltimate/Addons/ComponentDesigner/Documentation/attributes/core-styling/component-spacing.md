# [ComponentSpacing]

> Configures custom outer margins and inner padding around the entire component container to provide breathing room and visual separation.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentSpacing]` gives developers complete architectural control over the spacing geometry of component cards. Injected into `ComponentSlot.BodyWrapper`, it applies configurable outer margins (`MarginTop`, `MarginBottom`, `MarginLeft`, `MarginRight`) and internal padding (`PaddingTop`, `PaddingBottom`, `PaddingLeft`, `PaddingRight`). It provides shorthand constructors (`margin`, `padding`) to set uniform values instantly, as well as individual directional properties for asymmetric spacing needs.

**The Problem:**
When multiple decorated component cards sit on the same GameObject, they can crowd together without natural visual separation, creating cramped inspector layouts. Standard Unity inspectors do not provide a clean way to add outer margins or internal padding around entire components.

**The Solution:**
Decorating components with `[ComponentSpacing]`:
- **Uniform Shorthand Configuration:** Set all margins and paddings in a single constructor call (e.g. `[ComponentSpacing(8, 12)]`).
- **Directional Precision:** Independently tune top, bottom, left, and right margins or paddings to achieve exact pixel alignments.
- **Natural Visual Separation:** Introduces clean breathing room between vertically stacked component cards in the inspector.
- **Seamless Wrapper Integration:** Operates in `BodyWrapper`, modifying outer element styles without impacting serialized field layouts.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentSpacing(margin: 8f, padding: 12f)]
public class InventoryEquipmentGrid : MonoBehaviour
{
    public int maxSlotCapacity = 32;
    public float equipmentWeightKg = 14.5f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ComponentDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Component Slot** | `BodyWrapper` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentSpacingAttribute(float margin = 0, float padding = 0)
```

- `margin`: Shorthand value applied uniformly to top, bottom, left, and right outer margins.
- `padding`: Shorthand value applied uniformly to top, bottom, left, and right internal paddings.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Margin` | `float` | `0f` | Shorthand uniform margin value set via constructor. |
| `Padding` | `float` | `0f` | Shorthand uniform padding value set via constructor. |
| `MarginTop` | `float` | `0f` | Top outer margin in pixels. |
| `MarginBottom` | `float` | `0f` | Bottom outer margin in pixels. |
| `MarginLeft` | `float` | `0f` | Left outer margin in pixels. |
| `MarginRight` | `float` | `0f` | Right outer margin in pixels. |
| `PaddingTop` | `float` | `0f` | Top internal padding in pixels. |
| `PaddingBottom` | `float` | `0f` | Bottom internal padding in pixels. |
| `PaddingLeft` | `float` | `0f` | Left internal padding in pixels. |
| `PaddingRight` | `float` | `0f` | Right internal padding in pixels. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#6366F1", Width = 1.5f, Radius = 8f)]
[ComponentBackground("#0F1026", BorderRadius = 8f)]
[ComponentHeader("PLAYER STATS PANEL", Subtitle = "Attributes, Talents & Resists", BackgroundColor = "#1B1C3D", TitleColor = "#E0E7FF")]
[ComponentSpacing(margin: 6f, padding: 14f, MarginBottom = 12f)]
public class PlayerStatsPanel : MonoBehaviour
{
    [Header("Core Attributes")]
    public int strengthScore = 18;
    public int agilityScore = 14;
    public int intelligenceScore = 22;

    [Header("Defenses")]
    public float armorRating = 350f;
    public float magicResistancePercent = 30f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBorder]`** | High | Padding creates comfortable internal clearance between fields and border strokes. |
| **`[ComponentBackground]`** | High | Padding keeps inner controls comfortably inset from the colored background edges. |
| **Stacked Components** | High | `MarginBottom` provides consistent vertical spacing between multiple decorated components. |
