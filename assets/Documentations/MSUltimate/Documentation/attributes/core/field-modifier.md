# [FieldModifier]

> Foundational base class for attributes that modify field styling, labels, layout constraints, prefixes/suffixes, or interactive state without replacing the core drawer.

---

## 1. Overview & Value Proposition

**What it does:**
Acts as the abstract base class and category assigner for field modifier attributes in MSUltimate. Attributes inheriting from `FieldModifierAttribute` are categorized under `AttributeCategory.FieldModifier`, allowing them to post-process, wrap, or modify an existing field's visual presentation (e.g. adding units, adjusting margins, locking editability) without replacing the underlying primary drawer.

**The Problem:**
In standard Unity, tweaking simple presentation details like adding unit labels (`"ms"`, `"kg"`), indenting fields, or locking a field to read-only requires writing custom property drawers from scratch or chaining cumbersome IMGUI calls.

**The Solution:**
Extend `FieldModifierAttribute` when building field-level visual modifiers:
- **Modifier Pipeline Hook:** Seamlessly attaches to the rendered field element to modify attributes, CSS classes, or inline badges.
- **Composable Stacking:** Stacks cleanly with other modifiers, decorators, and primary drawers.
- **Foundation of MSUltimate Modifiers:** Powers core attributes like `[ReadOnly]`, `[Prefix]`, `[Suffix]`, `[LabelWidth]`, and `[Indent]`.

---

## 2. Quick Start

```csharp
using System;
using MaharajaStudio.MSUltimate.Runtime;

// Creating a custom field modifier attribute
[AttributeUsage(AttributeTargets.Field | AttributeTargets.Property, AllowMultiple = true, Inherited = true)]
public class CurrencyBadgeAttribute : FieldModifierAttribute
{
    public string CurrencySymbol { get; } = "$";

    public CurrencyBadgeAttribute(string currencySymbol)
    {
        CurrencySymbol = currencySymbol;
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable member |
| **Allow Multiple** | Configurable on derived classes |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
protected FieldModifierAttribute()
```

*Abstract base class constructor; derived classes define custom constructor parameters.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Category` | `AttributeCategory` | `AttributeCategory.FieldModifier` | Read-only category defining drawer resolution and modifier pipeline priority. |
| `Order` | `int` | `0` | Execution priority relative to other modifiers on the same member. |

---

## 6. Production-Grade Example

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

// Custom Unit Suffix Modifier
[AttributeUsage(AttributeTargets.Field, AllowMultiple = false, Inherited = true)]
public class PhysicalUnitAttribute : FieldModifierAttribute
{
    public string Unit { get; }

    public PhysicalUnitAttribute(string unit)
    {
        Unit = unit;
        Order = 20;
    }
}

public class BallisticsModule : MonoBehaviour
{
    [PhysicalUnit("m/s")]
    public float muzzleVelocity = 850f;

    [PhysicalUnit("kg")]
    public float projectileMass = 0.045f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| Primary Drawers | Supported | Wraps and post-processes primary field drawers seamlessly. |
| Multiple Allowed | Supported | Multiple field modifiers can be chained on a single member. |
| `[BoxGroup]` | Supported | Fully compatible inside layout cards and foldout containers. |
