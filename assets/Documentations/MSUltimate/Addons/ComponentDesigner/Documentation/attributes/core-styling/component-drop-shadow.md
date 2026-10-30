# [ComponentDropShadow]

> Projects an elevated drop shadow behind the component inspector card, delivering modern depth and elevation hierarchy.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentDropShadow]` introduces modern UI depth and elevation into the Unity Inspector. Injecting into `ComponentSlot.BodyWrapper`, it projects a customizable shadow plane behind the entire component card. It provides fine-grained control over shadow color (`Color`, defaulting to black `#000000`), opacity (`Opacity`, defaulting to 0.3), horizontal/vertical offsets (`OffsetX` and `OffsetY`), blur radius (`Blur`), and corner matching (`BorderRadius`). Because `AllowMultiple = true`, developers can stack a tight contact shadow with a wide ambient occlusion shadow for photorealistic multi-layer depth.

**The Problem:**
Standard Unity inspectors are completely flat 2D panels. Without elevation or shadow modeling, stacked cards feel crowded and lack visual hierarchy.

**The Solution:**
Decorating component cards with `[ComponentDropShadow]`:
- **Card Elevation & Depth:** Creates a subtle floating card illusion that lifts the component off the editor background.
- **Multi-Layer Stacking:** Stacks multiple shadow layers (`AllowMultiple = true`) to achieve natural light falloff (ambient + directional).
- **Matching Corner Geometry:** Matches border radii (`BorderRadius`) to align perfectly with rounded cards.
- **BodyWrapper Slot Integration:** Cleanly encloses the component body without altering internal field coordinates.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBackground("#1E293B", BorderRadius = 8f, Padding = 10f)]
[ComponentDropShadow(OffsetX = 0f, OffsetY = 4f, Blur = 12f, Opacity = 0.4f, BorderRadius = 8f)]
public class FloatingCardExample : MonoBehaviour
{
    public string cardTitle = "Elevated Module";
    public bool isFloating = true;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ComponentDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Component Slot** | `BodyWrapper` (`Order = 15`) |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentDropShadowAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color` | `string` | `"#000000"` | Hex color string for the projected shadow. |
| `Opacity` | `float` | `0.3f` | Shadow alpha opacity clamped between `0.0` and `1.0`. |
| `OffsetX` | `float` | `4f` | Horizontal shadow displacement in pixels. |
| `OffsetY` | `float` | `4f` | Vertical shadow displacement in pixels. |
| `Blur` | `float` | `10f` | Shadow blur spread distance in pixels. |
| `BorderRadius` | `float` | `0f` | Corner radius applied to the shadow perimeter to match the card. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#475569", Width = 1f, Radius = 10f)]
[ComponentBackground("#0F172A", BorderRadius = 10f, Padding = 12f)]
[ComponentDropShadow(OffsetX = 0f, OffsetY = 2f, Blur = 4f, Opacity = 0.5f, BorderRadius = 10f)]
[ComponentDropShadow(OffsetX = 0f, OffsetY = 8f, Blur = 20f, Opacity = 0.3f, BorderRadius = 10f)]
public class InventoryHubController : MonoBehaviour
{
    [Header("Hub State")]
    public int connectedStorageUnits = 4;
    public float maximumWeightCapacity = 250f;
    public bool autoSortOnDeposit = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Best practice; set `BorderRadius` on both attributes to identical values for crisp alignment. |
| **`[ComponentBorder]`** | High | Sits beneath the border frame, casting depth behind the border stroke. |
| **Multiple `[ComponentDropShadow]`** | High | Combine a tight contact shadow with a wide ambient shadow for premium elevation. |
| **Field Inputs & Controls** | High | Transparently wraps behind the card without impacting field click targets. |
