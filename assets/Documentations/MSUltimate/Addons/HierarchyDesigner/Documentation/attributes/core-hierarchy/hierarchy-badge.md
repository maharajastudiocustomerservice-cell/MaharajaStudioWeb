# [HierarchyBadge]

> Draws a sleek colored pill badge on the hierarchy row for static entity categorization or dynamic conditional state display.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyBadge]` decorates hierarchy items with sharp, readable metadata pills. Rendered via `HierarchyBadgeRenderer`, it can be placed on a class for static categorization (`Text = "BOSS"`, `BadgeColor = "#DC2626"`) or on a serialized field for live conditional state monitoring (`ShowCondition = HierarchyBadgeCondition.WhenTrue`). When bound to fields, it supports dynamic toggling between primary and alternate text and colors (`AlternateText = "DEAD"`, `AlternateBadgeColor = "#374151"`), giving instant visual telemetry without selecting the object.

**The Problem:**
Hierarchy rows only show the GameObject name. As scene trees grow to thousands of entities, determining which entity is an AI NavMesh agent, a Network Player, an Environmental Hazard, or a Spawn Point requires reading naming conventions or opening component lists.

**The Solution:**
Decorating classes and serialized state variables with `[HierarchyBadge]`:
- **Instant Visual Identification:** Categorize entities with clean status pills (e.g. `"AUDIO"`, `"UI"`, `"PLAYER"`, `"LIGHT"`).
- **Dynamic Field-State Monitoring:** Automatically flips badges when bool fields change (e.g. `"READY"` vs `"CHARGING"`).
- **Customizable Pill Typography:** Control font sizes, bold weights, rounded corners (`BorderRadius = 4f`), and custom text hues.
- **Zero GC Footprint:** Fast layout calculations with zero runtime memory allocations during hierarchy repaints.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyBadge(Text = "PLAYER", BadgeColor = "#0284C7", TextColor = "#FFFFFF", Bold = true)]
public class PlayerCharacterEntity : MonoBehaviour
{
    [HierarchyBadge(Text = "ALIVE", AlternateText = "DEAD", BadgeColor = "#16A34A", AlternateBadgeColor = "#991B1B", ShowCondition = HierarchyBadgeCondition.WhenTrue)]
    public bool isAlive = true;

    public float currentHealth = 100f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class | Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyBadgeRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyBadgeAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Text` | `string` | `"TAG"` | Primary text label displayed inside the badge pill. |
| `AlternateText` | `string` | `""` | Alternate text displayed when the condition is false or unmet. |
| `BadgeColor` | `string` | `"#444466"` | Hex background color of the badge pill. |
| `AlternateBadgeColor`| `string` | `""` | Alternate hex background color used when alternate text is active. |
| `TextColor` | `string` | `"#FFFFFF"` | Hex text color inside the badge. |
| `BorderRadius` | `float` | `4f` | Corner rounding radius in pixels for the pill shape. |
| `FontSize` | `int` | `0` | Font size in pixels, or `0` to inherit Unity's hierarchy default. |
| `Bold` | `bool` | `false` | Whether to render the badge label in bold font. |
| `Width` | `float` | `0f` | Fixed pill width in pixels, or `0f` to auto-size based on text length. |
| `Height` | `float` | `0f` | Fixed pill height in pixels, or `0f` to auto-size. |
| `XOffset` | `float` | `2f` | Horizontal offset in pixels from the right margin. |
| `ShowCondition` | `HierarchyBadgeCondition` | `Always` | Display condition for field-level badges (`Always`, `WhenTrue`, `WhenFalse`, `WhenNotNull`, `WhenNull`). |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the badge pill remains visible in Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyBadge(Text = "NETWORK SPAWN", BadgeColor = "#7C3AED", TextColor = "#F5F3FF", Bold = true, XOffset = 4f)]
public class NetworkSpawnAnchor : MonoBehaviour
{
    [Header("Network Authority")]
    public int networkPlayerId = 1;

    [Header("Live Connection State")]
    [HierarchyBadge(
        Text = "CONNECTED", 
        AlternateText = "DISCONNECTED", 
        BadgeColor = "#059669", 
        AlternateBadgeColor = "#DC2626", 
        ShowCondition = HierarchyBadgeCondition.WhenTrue, 
        XOffset = 95f)]
    public bool isClientConnected = true;

    public float roundTripPingMs = 38.5f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyIcon]`** | High | Badges and icons sit neatly side-by-side using horizontal `XOffset` spacing. |
| **`[HierarchyActiveButton]`**| High | Position the active button at `XOffset = 2f` and badges starting at `XOffset = 22f`. |
| **Conditional Field Logic** | High | Supports booleans (`WhenTrue`/`WhenFalse`) and object references (`WhenNotNull`/`WhenNull`). |
| **Hierarchy Selection** | High | High contrast text colors ensure readability whether the hierarchy row is selected or unselected. |
