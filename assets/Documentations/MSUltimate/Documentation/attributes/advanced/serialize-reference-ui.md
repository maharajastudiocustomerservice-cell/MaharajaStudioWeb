# [SerializeReferenceUI]

> Enhances Unity's `[SerializeReference]` polymorphic fields with an interactive type-selector dropdown, instance factory, and custom card styling.

---

## 1. Overview & Value Proposition

**What it does:**
Adds an easy type-selection dropdown to Unity's `[SerializeReference]` fields so you can create and switch between derived C# classes with one click.

**The Problem:**
Unity supports polymorphism using `[SerializeReference]`, but gives you almost no UI for it. By default, there is no dropdown to pick which class you want to create, no way to switch between different behaviors without writing custom editor code, and no easy way to see which subclass is currently assigned.

**The Solution:**
Add `[SerializeReferenceUI]` next to any `[SerializeReference]` field:
- **1-Click Class Dropdown:** Automatically finds all subclasses of your interface or base class and displays them in a clean dropdown.
- **Instant Creation:** Pick a class from the list, and it immediately instantiates it and displays all of its fields.
- **Clear Visual Cards:** Wraps the active class instance in a tidy, collapsible card with a header and border.
- **List & Array Support:** Works seamlessly with collections, giving every item in your list its own type-switcher.

---

## 2. Quick Start

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class AIController : MonoBehaviour
{
    [SerializeReference]
    [SerializeReferenceUI]
    public IAITask activeBehavior;
}

public interface IAITask { }

[Serializable]
public class PatrolTask : IAITask { public float patrolRadius = 10f; }

[Serializable]
public class ChaseTask : IAITask { public float maxSpeed = 8f; }
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Field | AttributeTargets.Property` |
| **Supported Types** | Interfaces, abstract classes decorated with `[SerializeReference]` (including `List<TInterface>`, `TBaseClass[]`) |
| **Collection Cascading** | Supported (`ICollectionElementAttribute`) |
| **Allow Multiple** | `false` |
| **Inherited** | `true` |
| **Build Overhead** | Editor-only (Zero runtime build overhead / stripped in builds) |
| **Minimum Unity** | Unity 6 (6000.x)+ |

---

## 4. Constructors & Signatures

```csharp
public SerializeReferenceUIAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `NullLabel` | `string` | `"None (Select a Type)"` | Label displayed when the polymorphic reference is null. |
| `ShowFullTypeName` | `bool` | `false` | Displays full namespace and class name instead of just the class name. |
| `AllowedNamespaces`| `string[]` | `null` | Filters type discovery strictly to designated namespaces. |
| `ExcludeNamespaces`| `string[]` | `null` | Excludes internal or deprecated namespaces from type dropdown. |
| `DefaultExpanded` | `bool` | `true` | Expands child instance fields automatically upon creation. |
| `HeaderBackgroundColor`| `string`| `"#2A2A2A"` | Background color for the type-selector header bar. |
| `HeaderTextColor` | `string` | `null` | Hex text color of the header label. |
| `BorderColor` | `string` | `"#444444"` | Outline stroke color framing the polymorphic instance card. |
| `BorderWidth` | `float` | `1f` | Border outline stroke thickness in pixels. |
| `BorderRadius` | `float` | `4f` | Corner rounding radius of the type container. |
| `Padding` | `float` | `6f` | Inner padding in pixels for reference contents. |
| `MarginTop` | `float` | `4f` | Top margin spacing in pixels. |
| `MarginBottom` | `float` | `4f` | Bottom margin spacing in pixels. |
| `ButtonColor` | `string` | `null` | Hex background color for the type selector dropdown button. |
| `ButtonTextColor` | `string` | `null` | Hex text color for the type selector dropdown button. |

---

## 6. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class SkillSystem : MonoBehaviour
{
    public interface ISkillEffect
    {
        void Execute(GameObject target);
    }

    [Serializable]
    public class DamageEffect : ISkillEffect
    {
        public float baseDamage = 50f;
        public void Execute(GameObject target) { }
    }

    [Serializable]
    public class HealEffect : ISkillEffect
    {
        public float healAmount = 30f;
        public void Execute(GameObject target) { }
    }

    [BoxGroup("Active Skill Payload", Box = true)]
    [SerializeReference]
    [SerializeReferenceUI(
        NullLabel = "No Effect Assigned",
        DefaultExpanded = true,
        HeaderBackgroundColor = "#1E272E"
    )]
    public ISkillEffect primaryEffect = new DamageEffect();
}
```

---

## 7. Stacking & Compatibility Matrix

- **Pairing Requirement:** Must be applied alongside Unity's native `[SerializeReference]` attribute.
- **Collection Support:** Fully supports polymorphic collections such as `List<ISkillEffect>` or arrays. Each list item receives its own independent type switcher dropdown.
- **Null Safety:** Switching a type to "None" safely sets the reference to `null` and frees serialized buffers without throwing dangling reference warnings.
