# [AnimatedDrawer]

> Foundational base class for animated custom field drawers that replace default property rendering with dynamic interactive controls.

---

## 1. Overview & Value Proposition

**What it does:**
Serves as the abstract base class and category assigner for animated primary drawers in MSUltimate-AnimatedAttributes. Attributes inheriting from `AnimatedDrawerAttribute` are categorized under `AttributeCategory.PrimaryDrawer`, establishing them as the primary rendering authority for the decorated field while providing hardware-accelerated UI Toolkit animation loops.

**The Problem:**
Creating custom interactive animated controls (like sliding toggles, animated scrub bars, or vector-morphing checkboxes) in standard Unity requires complex `PropertyDrawer` overrides that frequently break layout stacking or drop frames.

**The Solution:**
Extend `AnimatedDrawerAttribute` when building custom animated field controls:
- **Primary Control Authority:** Replaces default IMGUI/UI Toolkit field rendering with a bespoke animated element.
- **Micro-Interaction Pipeline:** Manages gesture transitions, mouse hover, drag scrub, and state animations.
- **Powers Next-Gen Drawers:** Foundational base for `[InteractiveToggle]`, `[AnimatedProgressBar]`, `[AnimatedMarquee]`, and `[MorphingCheckbox]`.

---

## 2. Quick Start

```csharp
using System;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

// Creating a custom animated knob drawer
[AttributeUsage(AttributeTargets.Field | AttributeTargets.Property, AllowMultiple = false, Inherited = true)]
public class AnimatedKnobAttribute : AnimatedDrawerAttribute
{
    public float TurnSpeed { get; set; } = 150f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Class` (Base Attribute) |
| **Supported Types** | Any serializable field type |
| **Allow Multiple** | Configurable on derived classes |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
protected AnimatedDrawerAttribute()
```

*Abstract base constructor providing initial PrimaryDrawer classification.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Category` | `AttributeCategory` | `AttributeCategory.PrimaryDrawer` | Read-only category assigning animated drawers to the primary field rendering phase. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

// Custom Animated Numeric Gauge Drawer
[AttributeUsage(AttributeTargets.Field, AllowMultiple = false, Inherited = true)]
public class CyberDialAttribute : AnimatedDrawerAttribute
{
    public string DialColor { get; set; } = "#00FF88";
}

public class VehicleDashboard : MonoBehaviour
{
    [CyberDial(DialColor = "#00FFFF")]
    public float engineRPM = 4500f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| All Animated Drawers | Native Base | Root class for `[InteractiveToggle]`, `[AnimatedProgressBar]`, `[MorphingCheckbox]`. |
| Decorators | Supported | Decorators render cleanly above animated drawers without layout conflict. |
| `[BoxGroup]` | Supported | Fully compatible inside layout cards and foldouts. |
