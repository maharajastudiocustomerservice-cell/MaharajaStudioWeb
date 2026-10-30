# [Modular]

> Foundational root base class for all MSUltimate attributes, establishing lifecycle execution phases, category classification, and order prioritization across the inspector pipeline.

---

## 1. Overview & Value Proposition

**What it does:**
Acts as the ultimate architectural foundation for all MSUltimate attributes. Every attribute in the suite inherits from `ModularAttribute`, equipping it with an execution `Category` (`PrimaryDrawer`, `PreDecorator`, `FieldModifier`, `PostDecorator`, `Validation`, `Behavioral`, `LayoutGroup`) and an explicit sorting `Order`.

**The Problem:**
Traditional Unity `PropertyAttribute` lacks execution phase awareness, making it impossible to predict whether a header renders before or after a slider, or whether validation checks occur before or after layout wrapping.

**The Solution:**
All MSUltimate attributes extend `ModularAttribute`:
- **Deterministic Pipeline Execution:** Categorizes each attribute into a distinct lifecycle phase.
- **Granular Sorting Priority:** The `Order` integer allows fine-grained execution prioritization on members with multiple attributes.
- **Universal Stacking Contract:** Guarantees decorators, validation rules, behavioral conditionals, and custom drawers compose seamlessly without conflicts.

---

## 2. Quick Start

```csharp
using System;
using MaharajaStudio.MSUltimate.Runtime;

// Creating a custom behavioral attribute
[AttributeUsage(AttributeTargets.Field | AttributeTargets.Property, AllowMultiple = false, Inherited = true)]
public class LogAccessAttribute : ModularAttribute
{
    public override AttributeCategory Category => AttributeCategory.Behavioral;
    public string LogTag { get; set; } = "ACCESS";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Class` (Base Attribute) |
| **Supported Types** | Any serializable member |
| **Allow Multiple** | Configurable on derived attributes |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
protected ModularAttribute()
```

*Abstract base constructor providing initial zero-order priority.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Order` | `int` | `0` | Controls execution and visual layout sorting priority relative to other attributes on the same member. |
| `Category` | `AttributeCategory` | `AttributeCategory.Behavioral` | Read-only lifecycle phase category governing drawer pipeline resolution. |

---

## 6. Production-Grade Example

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

// Custom Game Telemetry Tag Attribute
[AttributeUsage(AttributeTargets.Field, AllowMultiple = true, Inherited = true)]
public class TelemetryTrackedAttribute : ModularAttribute
{
    public override AttributeCategory Category => AttributeCategory.PostDecorator;
    public string MetricKey { get; }

    public TelemetryTrackedAttribute(string metricKey, int order = 10)
    {
        MetricKey = metricKey;
        Order = order;
    }
}

public class GameAnalyticsEmitter : MonoBehaviour
{
    [TelemetryTracked("player_currency_gold", order: 5)]
    public int playerGold = 1000;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| All MSUltimate Attributes | Native Foundation | Root class inherited by all decorators, drawers, validators, and layout groups. |
| UI Toolkit Integration | Supported | Pipeline categories map directly to visual element container hierarchies. |
| Reflection Caches | Supported | Cached by `MemberDiscovery` for high-performance zero-allocation inspector rendering. |
