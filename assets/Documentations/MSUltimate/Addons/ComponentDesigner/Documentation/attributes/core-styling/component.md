# [Component]

> Architectural base attribute and styling contract for component-level cards, visual themes, and inspector shell decorators.

---

## 1. Overview & Value Proposition

**What it does:**
`ComponentAttribute` serves as the foundational abstract base class for all class-level styling decorators in the **MSUltimate Component Designer** suite. Rather than styling individual serialized fields in isolation, attributes deriving from `ComponentAttribute` target the entire `MonoBehaviour` or `ScriptableObject` inspector class. They interface directly with `ComponentStyleProcessor` and `ComponentAttributeDrawer<T>`, injecting custom UI elements into dedicated component lifecycle slots (`BeforeBody`, `BodyWrapper`, `BodyOverlay`, `BeforeContent`, `ContentWrapper`, `ContentOverlay`, `AfterContent`, and `AfterBody`).

**The Problem:**
Standard Unity inspectors present every component as an unstyled, identical gray rectangle. When building complex game architectures containing dozens of managers, audio racks, network controllers, and combat modules, designers struggle to distinguish critical systems at a glance without external custom editors.

**The Solution:**
Using the `ComponentAttribute` hierarchy:
- **Class-Level Card Styling:** Transforms mundane inspectors into cohesive visual cards with custom borders, gradients, watermarks, and headers.
- **Slot-Based Architecture:** Predictably layers visual elements (wrappers, overlays, headers, and footers) without breaking standard field rendering.
- **Polymorphic Drawer Registration:** Custom drawers inheriting `ComponentAttributeDrawer<T>` automatically register into the UI Toolkit injection pipeline without manual attribute binding.
- **Zero Runtime Overhead:** All styling logic and drawer processors are completely stripped in player runtime builds.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

// Derived attributes (e.g. ComponentBorder, ComponentBackground) inherit from ComponentAttribute
[ComponentBorder(Color = "#4FC3F7", Width = 2f, Radius = 8f)]
public class CombatManager : MonoBehaviour
{
    public float globalDamageMultiplier = 1.0f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ComponentDesigner Addon |
| **Attribute Target** | `Class` |
| **Inheritance** | Abstract Base Class (`ModularAttribute`) |
| **Allow Multiple** | Controlled by derived classes |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Class Signature & Architecture

```csharp
namespace MaharajaStudio.MSUltimate.ComponentDesigner
{
    public abstract class ComponentAttribute : ModularAttribute
    {
    }
}
```

### Inherited Properties (from `ModularAttribute`)

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Order` | `int` | `0` | Execution and rendering order priority relative to other modular attributes within the same layout slot. |

### Component Injection Slots (`ComponentSlot`)

Every derived attribute drawer injects its elements into one of eight standardized layout slots:

| Slot | Value | Typical Usage |
| :--- | :---: | :--- |
| `BeforeBody` | `0` | Top separators, external help boxes, preset managers. |
| `BodyWrapper` | `10` | Outer decorative borders, glow wrappers, animated stroke frames. |
| `BodyOverlay` | `20` | Corner badges, brand tags, colored edge accent strips. |
| `BeforeContent` | `30` | Top title banners, header cards, icon toolbars. |
| `ContentWrapper` | `40` | Background colors, glassmorphism cards, image backdrops. |
| `ContentOverlay` | `50` | Auroras, digital circuits, starfield particles, watermarks. |
| `AfterContent` | `60` | Footer bars, author tags, diagnostic summary strips. |
| `AfterBody` | `70` | Bottom action buttons, footer separators, diagnostic help boxes. |

---

## 5. Creating a Custom Component Attribute

Developers can extend `ComponentAttribute` to build bespoke component decorators:

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[AttributeUsage(AttributeTargets.Class, AllowMultiple = false, Inherited = true)]
public class CustomStudioTagAttribute : ComponentAttribute
{
    public string StudioName { get; }

    public CustomStudioTagAttribute(string studioName = "Maharaja Studio")
    {
        StudioName = studioName;
    }
}
```

Companion Editor Drawer:

```csharp
#if UNITY_EDITOR
using UnityEngine.UIElements;
using MaharajaStudio.MSUltimate.ComponentDesigner.Editor.Drawers;

public class CustomStudioTagDrawer : ComponentAttributeDrawer<CustomStudioTagAttribute>
{
    public override ComponentSlot OnGetSlot(CustomStudioTagAttribute attr) => ComponentSlot.BeforeContent;

    public override VisualElement OnBuild(CustomStudioTagAttribute attr)
    {
        var tag = new Label($"✦ {attr.StudioName.ToUpper()}");
        tag.style.fontSize = 9;
        tag.style.unityFontStyleAndWeight = FontStyle.Bold;
        tag.style.color = new StyleColor(new Color(0.6f, 0.6f, 0.8f));
        tag.style.marginBottom = 4;
        return tag;
    }
}
#endif
```

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#10B981", Width = 2f, Radius = 6f, Glow = true)]
[ComponentBackground("#111827", BorderRadius = 6f, Padding = 10f)]
public class InventoryDatabase : MonoBehaviour
{
    public int maxInventorySlots = 100;
    public bool enableCloudSaving = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **Multiple Component Attributes** | High | Multiple derived attributes (`[ComponentBorder]`, `[ComponentHeader]`, `[ComponentBadge]`) compose seamlessly into a unified component shell. |
| **Field-Level Attributes** | High | Works natively with all MSUltimate field attributes (`[AnimatedOdometer]`, `[Range]`, `[ShowIf]`). |
| **MonoBehaviour & ScriptableObject** | High | Applies cleanly to both scene GameObjects and project ScriptableObject asset inspectors. |
| **Custom Editors** | High | Integrates through `ComponentStyleProcessor` without requiring custom Editor class rewrites. |
