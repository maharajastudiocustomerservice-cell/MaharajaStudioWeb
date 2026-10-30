# [Decorator]

> Foundational base class for visual decorator attributes (headers, notes, badges, dividers) that augment Inspector presentation without altering serialized field values.

---

## 1. Overview & Value Proposition

**What it does:**
Serves as the abstract base class and category assigner for all decorator attributes in the MSUltimate ecosystem. Attributes inheriting from `DecoratorAttribute` are automatically classified under `AttributeCategory.PreDecorator`, ensuring they are evaluated and rendered prior to the primary field drawer.

**The Problem:**
Standard Unity `DecoratorDrawer` implementations are rigid, suffer from IMGUI spacing bugs, cannot easily bind to UI Toolkit visual trees, and frequently break layout stacking when multiple decorators are applied to a single field.

**The Solution:**
Extend `DecoratorAttribute` when building custom decorative inspector elements:
- **Pre-Drawer Pipeline:** Automatically positions decorations above or around the target field.
- **Pure Visual Augmentation:** Decorators do not alter or hijack the underlying field's data serialization or interactive controls.
- **Robust Stacking:** Seamlessly stacks with multiple decorators, notes, headers, and primary field drawers.
- **Foundation of MSUltimate:** Powers core decorators like `[Header]`, `[Note]`, `[Divider]`, and `[InlineHelp]`.

---

## 2. Quick Start

```csharp
using System;
using MaharajaStudio.MSUltimate.Runtime;

// Creating a custom decorative ribbon attribute
[AttributeUsage(AttributeTargets.Field | AttributeTargets.Property, AllowMultiple = true, Inherited = true)]
public class SectionRibbonAttribute : DecoratorAttribute
{
    public string RibbonTitle { get; }
    public string ColorHex { get; set; } = "#3498db";

    public SectionRibbonAttribute(string ribbonTitle)
    {
        RibbonTitle = ribbonTitle;
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property | Method` |
| **Supported Types** | Any member |
| **Allow Multiple** | Configurable on derived classes |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
protected DecoratorAttribute()
```

*Abstract base class constructor; derived classes define custom constructor parameters.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Category` | `AttributeCategory` | `AttributeCategory.PreDecorator` | Read-only category defining drawer resolution and pre-render pipeline priority. |
| `Order` | `int` | `0` | Execution priority relative to other decorators on the same member. |

---

## 6. Production-Grade Example

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

// Custom Game Department Header Decorator
[AttributeUsage(AttributeTargets.Field, AllowMultiple = true, Inherited = true)]
public class DevTeamTagAttribute : DecoratorAttribute
{
    public string TeamName { get; }

    public DevTeamTagAttribute(string teamName)
    {
        TeamName = teamName;
        Order = -50; // Ensure decorator draws early
    }
}

public class GameWorldDirector : MonoBehaviour
{
    [DevTeamTag("Audio & SFX Team")]
    public float ambientAudioVolume = 0.8f;

    [DevTeamTag("Design & Balance Team")]
    public float playerSpawnInterval = 3.5f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Decorators render cleanly inside group containers. |
| Multiple Allowed | Supported | Multiple decorator attributes can be stacked on a single field in specified `Order`. |
| Primary Drawers | Supported | Coexists with primary field drawers (`[Slider]`, `[ColorPalette]`) without interfering with data input. |
