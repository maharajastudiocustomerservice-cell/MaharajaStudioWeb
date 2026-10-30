# [Drawer]

> Foundational base class for primary field drawers that control, replace, or customize how a field's interactive data is edited and rendered in the Inspector.

---

## 1. Overview & Value Proposition

**What it does:**
Acts as the abstract base class and category assigner for primary field drawers across MSUltimate. Attributes inheriting from `DrawerAttribute` are categorized under `AttributeCategory.PrimaryDrawer`, establishing them as the primary rendering authority for the decorated field.

**The Problem:**
Standard Unity `PropertyDrawer` implementations are difficult to chain, cannot easily communicate with decorators or validators on the same field, and struggle with custom collection element rendering.

**The Solution:**
Extend `DrawerAttribute` when creating custom input controls or replacement fields:
- **Primary Drawer Authority:** Replaces or restyles the main input control while maintaining pipeline interoperability.
- **Interoperable with Decorators & Modifiers:** Works harmoniously alongside pre-decorators (headers) and post-modifiers (suffixes).
- **Foundation of MSUltimate Field Drawers:** Serves as the base for attributes such as `[MinMaxSlider]`, `[Calendar]`, `[DrawDateTime]`, `[DrawRange]`, `[DrawNullable]`, and `[DrawTuple]`.

---

## 2. Quick Start

```csharp
using System;
using MaharajaStudio.MSUltimate.Runtime;

// Creating a custom primary drawer attribute
[AttributeUsage(AttributeTargets.Field | AttributeTargets.Property, AllowMultiple = false, Inherited = true)]
public class RadialKnobAttribute : DrawerAttribute
{
    public float Min { get; set; } = 0f;
    public float Max { get; set; } = 100f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field type |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
protected DrawerAttribute()
```

*Abstract base class constructor; derived classes define custom constructor parameters.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Category` | `AttributeCategory` | `AttributeCategory.PrimaryDrawer` | Read-only category defining drawer resolution and primary field drawer authority. |
| `Order` | `int` | `0` | Execution priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

// Custom Hex Color Palette Drawer Attribute
[AttributeUsage(AttributeTargets.Field, AllowMultiple = false, Inherited = true)]
public class CompactColorDrawerAttribute : DrawerAttribute
{
    public bool ShowAlpha { get; set; } = true;
    public bool Hdr { get; set; } = false;

    public CompactColorDrawerAttribute(bool showAlpha = true, bool hdr = false)
    {
        ShowAlpha = showAlpha;
        Hdr = hdr;
    }
}

public class ParticleEffectSettings : MonoBehaviour
{
    [CompactColorDrawer(showAlpha: true, hdr: true)]
    public Color burstGlowColor = Color.cyan;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Primary drawers render smoothly inside layout containers. |
| `[ShowIf]` | Supported | Fully respects dynamic conditional visibility. |
| Decorators | Supported | Decorators render cleanly above the primary drawer without interference. |
