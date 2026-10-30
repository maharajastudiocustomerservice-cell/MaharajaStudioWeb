# [Breadcrumb]

> Renders a stylized navigation breadcrumb trail above a serialized field to clarify complex subsystem hierarchies.

---

## 1. Overview & Value Proposition

**What it does:**
Draws a sleek navigation trail (e.g. `Combat › Abilities › Ultimate`) above a field so you know exactly where it belongs in your game architecture.

**The Problem:**
In large MonoBehaviours with 40+ serialized fields, it's easy to lose track of which category or subsystem a specific setting belongs to while scrolling through a long Inspector. Plain headers can get buried, and nested tabs can obscure parent context.

**The Solution:**
Add `[Breadcrumb]` above key configuration fields:
- **Instant Architectural Context:** Clearly indicates the domain hierarchy (e.g. `Player › Movement › Wall Run`).
- **Custom Delimiters:** Use arrows (`›`), slashes (`/`), or custom icons as segment separators.
- **Color Accent Control:** Tint breadcrumb chips with custom brand or system theme colors.
- **Zero Runtime Overhead:** Only drawn in the Unity Editor; completely stripped from player builds.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class PlayerMovement : MonoBehaviour
{
    [Breadcrumb("Player", "Locomotion", "Air Dash")]
    public float dashForce = 12f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public BreadcrumbAttribute()
public BreadcrumbAttribute(params string[] path)
public BreadcrumbAttribute(string separator, string colorHex, params string[] path)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `path` | `string[]` | `null` | Ordered list of hierarchy path steps (e.g. `"Audio"`, `"SFX"`, `"Explosions"`). |
| `separator` | `string` | `" › "` | String character or glyph separating each path breadcrumb. |
| `colorHex` | `string` | `"#888888"` | Hex color code for breadcrumb text and accent tags. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Path` | `string[]` | `null` | The array of step titles. |
| `Separator` | `string` | `" › "` | Divider character rendered between trail items. |
| `ColorHex` | `string` | `"#888888"` | Accent color hex string. |
| `MarginTop` | `float` | `2f` | Spacing in pixels above the breadcrumb trail. |
| `MarginBottom` | `float` | `2f` | Spacing in pixels below the breadcrumb trail. |
| `Width` | `float` | `0f` | Fixed container width (0 auto-fits). |
| `FullWidth` | `bool` | `false` | Stretches breadcrumb banner across the full inspector width. |
| `AboveGroup` | `bool` | `false` | Renders the breadcrumb outside of and above any surrounding group container. |
| `Order` | `int` | `-10` | Drawing order priority (defaults to -10 to render above the field). |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CombatBehaviorController : MonoBehaviour
{
    [Breadcrumb("/", "#3498DB", "AI System", "Combat Behavior", "Melee Targeting")]
    public float attackRangeMeters = 2.5f;

    [Breadcrumb("/", "#E74C3C", "AI System", "Combat Behavior", "Rage Mode")]
    public float enragedSpeedMultiplier = 1.8f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Works seamlessly inside or directly above group containers. |
| `[Header]` | Supported | Can be used alongside section headers for multi-level organization. |
| `[ShowIf]` | Supported | Dynamically hides or shows the breadcrumb trail with its field. |
