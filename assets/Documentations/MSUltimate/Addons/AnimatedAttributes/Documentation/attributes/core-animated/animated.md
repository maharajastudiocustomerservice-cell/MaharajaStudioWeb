# [Animated]

> Foundational base class for all decorative animation attributes in the MSUltimate-AnimatedAttributes addon, integrating micro-interactions into the PreDecorator pipeline.

---

## 1. Overview & Value Proposition

**What it does:**
Serves as the abstract base class and category assigner for all decorative animation attributes in the MSUltimate-AnimatedAttributes addon. Attributes extending `AnimatedAttribute` are classified under `AttributeCategory.PreDecorator`, equipping them with high-performance UI Toolkit transition hooks, zero-allocation animation lifecycles, and automatic editor stripping in player builds.

**The Problem:**
Adding animations, micro-interactions, or reactive hover states to custom Unity inspectors typically requires hundreds of lines of boilerplate USS stylesheets, visual element transitions, and manual editor ticking logic.

**The Solution:**
Extend `AnimatedAttribute` when crafting custom animated inspector behaviors:
- **PreDecorator Lifecycle:** Seamlessly attaches visual transitions to target fields.
- **Hardware-Accelerated:** Backed by modern UI Toolkit animation loops with smooth 60fps refresh.
- **Zero Player Build Footprint:** Stripped automatically during standalone build compilation.
- **Foundation of Animated Attributes:** Powers attributes like `[AnimatedHover]`, `[AnimatedFocus]`, `[AnimatedSlideIn]`, and `[PulseAttention]`.

---

## 2. Quick Start

```csharp
using System;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

// Creating a custom pulse animation attribute
[AttributeUsage(AttributeTargets.Field | AttributeTargets.Property, AllowMultiple = false, Inherited = true)]
public class CustomPulseAttribute : AnimatedAttribute
{
    public float PulseDuration { get; set; } = 300f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Class` (Base Attribute) |
| **Supported Types** | Any serializable member |
| **Allow Multiple** | Configurable on derived classes |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
protected AnimatedAttribute()
```

*Abstract base constructor providing initial PreDecorator classification.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Category` | `AttributeCategory` | `AttributeCategory.PreDecorator` | Read-only category assigning animated decorators to the PreDecorator execution phase. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

// Custom Animated Glow Wrapper
[AttributeUsage(AttributeTargets.Field, AllowMultiple = false, Inherited = true)]
public class NeonAuraAttribute : AnimatedAttribute
{
    public string GlowColor { get; set; } = "#00FFCC";
}

public class CyberShieldController : MonoBehaviour
{
    [NeonAura(GlowColor = "#00FFFF")]
    public float shieldCapacitance = 100f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| All Animated Attributes | Native Base | Root class for all decorative motion and micro-interaction attributes. |
| `[BoxGroup]` | Supported | Animations operate cleanly inside layout cards and foldouts. |
| Primary Drawers | Supported | Decorates primary field drawers without intercepting serialization. |
