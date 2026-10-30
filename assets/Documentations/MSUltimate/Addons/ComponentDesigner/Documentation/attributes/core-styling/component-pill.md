# [ComponentPill]

> Renders an interactive horizontal navigation pill bar above the component body for filtering, grouping, or multi-component switching in the inspector.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentPill]` equips component inspectors with an interactive category pill switcher. Positioned in `ComponentSlot.BeforeBody`, it renders a styled horizontal tab strip (`StripBackgroundColor`, `StripBorderColor`) containing rounded toggle pills. Pills can represent individual components or filter groups (`Group`), sporting custom icons (`Icon`), status badges (`Badge`), tooltips (`Tooltip`), and distinct active/inactive color palettes (`Color`, `InactiveColor`, `TextColor`, `InactiveTextColor`). An optional `"All"` master toggle (`ShowAllPill = true`) enables developers to show all grouped components simultaneously or isolate a specific module.

**The Problem:**
GameObjects containing multiple related components (such as an entity with AI Controller, Pathfinding, Combat, and Inventory) generate overwhelming vertical scrolling in inspector windows. Developers waste time searching through long property lists rather than focusing on the subsystem currently being tuned.

**The Solution:**
Decorating grouped modules with `[ComponentPill]`:
- **Subsystem Focus Bar:** Toggles visibility or highlights active component cards via a clean, compact pill strip.
- **Master "All" Toggle:** Automatically includes an `"All"` filter pill to restore full multi-component inspection with a single click.
- **Rich Status Badging:** Attach badges (e.g. `"Core"`, `"v2"`, `"Beta"`) directly onto pills to convey architectural tier or release state.
- **Deep Theming:** Customize pill corner radiuses (`BorderRadius = 12f`), heights, margins, active/inactive borders, and typography.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentPill("Combat", "#EF4444", "d_CustomTool", Group = "CharacterSystems", Badge = "Core")]
public class PlayerCombatController : MonoBehaviour
{
    public float baseAttackDamage = 35f;
    public float attackSpeedMultiplier = 1.25f;
    public bool canPerformComboAttacks = true;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ComponentDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Component Slot** | `BeforeBody` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentPillAttribute()
public ComponentPillAttribute(string label)
public ComponentPillAttribute(string label, string color)
public ComponentPillAttribute(string label, string color, string icon)
```

- `label`: Display text on the pill (defaults to class name if omitted).
- `color`: Active hex background color string (e.g. `"#3B82F6"`).
- `icon`: Unity built-in editor icon identifier or emoji.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Label` | `string` | `null` | Display text for the pill button. |
| `Icon` | `string` | `null` | Built-in Unity icon identifier or glyph. |
| `Color` | `string` | `"#3B82F6"` | Active background color (hex) when selected. |
| `InactiveColor` | `string` | `"#232330"` | Inactive background color (hex). |
| `TextColor` | `string` | `"#FFFFFF"` | Active text color (hex). |
| `InactiveTextColor` | `string` | `"#A0A0B5"` | Inactive text color (hex). |
| `ActiveBorderColor` | `string` | `null` | Border stroke color (hex) when selected. |
| `InactiveBorderColor` | `string` | `"#38384A"` | Border stroke color (hex) when inactive. |
| `BorderWidth` | `float` | `1f` | Border stroke thickness in pixels. |
| `BorderRadius` | `float` | `12f` | Corner rounding radius in pixels for the pill shape. |
| `Height` | `float` | `22f` | Height in pixels for the pill button element. |
| `Padding` | `float` | `10f` | Internal horizontal padding in pixels. |
| `FontSize` | `int` | `11` | Font size in points for the pill label text. |
| `Group` | `string` | `null` | Group identifier linking multiple components into the same switcher strip. |
| `Order` | `int` | `0` | Numerical sort index within the horizontal pill bar. |
| `Badge` | `string` | `null` | Optional tag badge text displayed on the pill (e.g. `"Core"`, `"v2"`). |
| `BadgeColor` | `string` | `"#10B981"` | Hex background color for the badge tag. |
| `BadgeTextColor` | `string` | `"#FFFFFF"` | Hex text color for the badge tag. |
| `Tooltip` | `string` | `null` | Hover tooltip description text. |
| `ShowAllPill` | `bool` | `true` | Whether to show the master "All" toggle button in the strip. |
| `AllPillLabel` | `string` | `"All"` | Display label for the master "All" pill. |
| `AllPillColor` | `string` | `"#5973A6"` | Active background color (hex) for the "All" pill. |
| `StripBackgroundColor`| `string` | `"#161622"` | Background color (hex) of the container strip. |
| `StripBorderColor` | `string` | `"#2D2D3E"` | Border stroke color (hex) of the container strip. |
| `StripPadding` | `float` | `4f` | Internal padding in pixels of the container strip. |
| `StripMarginBottom` | `float` | `6f` | Bottom margin spacing below the container strip. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#3B82F6", Width = 1.5f, Radius = 8f)]
[ComponentBackground("#0E1424", BorderRadius = 8f, Padding = 10f)]
[ComponentPill("Movement", "#2563EB", "d_NavMeshData Icon", Group = "HeroSystems", Order = 1, Badge = "v2", Tooltip = "Locomotion & Traversal Settings")]
public class HeroLocomotionEngine : MonoBehaviour
{
    [Header("Locomotion Tuning")]
    public float sprintMaxSpeedKmh = 24.5f;
    public float crouchWalkSpeedKmh = 6.2f;
    public float jumpImpulseVelocity = 7.8f;

    [Header("Stamina Costs")]
    public float sprintStaminaPerSec = 8f;
    public bool canSprintWhileExhausted = false;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeader]`** | High | Injected into `BeforeBody`, rendering directly below the header for tab-like navigation. |
| **`[ComponentBorder]`** | High | Rounded container strip fits neatly inside bordered component cards. |
| **Inspector Controls** | High | Click events switch active pill tabs while preserving immediate access to controls below. |
