# [Validation]

> Base class and foundational contract for all data validation and integrity guard attributes in MSUltimate, assigning them to the Validation execution pipeline.

---

## 1. Overview & Value Proposition

**What it does:**
Acts as the abstract base class and category assigner for the entire MSUltimate Validation pipeline. Attributes inheriting from `ValidationAttribute` are automatically classified under `AttributeCategory.Validation`, ensuring consistent execution ordering, defensive fallback handling, and centralized inspector error aggregation.

**The Problem:**
Custom validation systems in standard Unity or third-party tools are often fragmented, with inconsistent drawer lifecycles, ad-hoc execution timing, and poor UI Toolkit element synchronization.

**The Solution:**
Extend `ValidationAttribute` when authoring custom validation rules:
- **Central Pipeline Classification:** Automatically categorizes attributes into `AttributeCategory.Validation`.
- **Consistent Ordering:** Standardized execution flow across all validation rules (`Order` sorting).
- **Extensible Base:** Serves as the foundation for `[Required]`, `[ValidateInput]`, `[ClampWarning]`, `[CompareWith]`, and custom domain rules.
- **UI Toolkit & IMGUI Parity:** Handles both legacy and modern UI Toolkit lifecycle integration automatically.

---

## 2. Quick Start

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

// Creating a custom validation attribute
[AttributeUsage(AttributeTargets.Field, AllowMultiple = false, Inherited = true)]
public class PositiveOnlyAttribute : ValidationAttribute
{
    public string CustomMessage { get; set; } = "Value must be strictly positive!";
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
public ValidationAttribute()
```

*Parameterless default constructor initializing the base validation category.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Category` | `AttributeCategory` | `AttributeCategory.Validation` | Read-only category defining drawer resolution and execution pipeline priority. |
| `Order` | `int` | `0` | Execution priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

// Custom Game-Specific Non-Zero Validator
[AttributeUsage(AttributeTargets.Field | AttributeTargets.Property, AllowMultiple = false, Inherited = true)]
public class NonZeroAttribute : ValidationAttribute
{
    public string ErrorMessage { get; }

    public NonZeroAttribute(string message = "Value cannot be zero!")
    {
        ErrorMessage = message;
        Order = 50;
    }
}

public class GameSettings : MonoBehaviour
{
    [NonZero("Game time scale cannot be 0!")]
    public float timeScale = 1.0f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | All derived validation attributes render seamlessly inside group cards. |
| `[ShowIf]` | Supported | Derived validation attributes respect conditional visibility and suppress checks when hidden. |
| Multiple Allowed | Supported | Multiple derived validation attributes can be stacked on a single member. |
