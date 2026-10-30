# [HierarchyPropertyPath]

> Evaluates and displays nested member paths on the hierarchy row with safe null propagation and custom badge styling.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyPropertyPath]` traverses dotted member paths (e.g. `stats.currentHp`, `profile.equipment.weapon.damage`) and renders the resolved value inside a styled badge directly on the hierarchy row. Driven by `HierarchyPropertyPathRenderer`, it handles deep reflection with safe null propagation (`NullFallbackText = "—"`), custom format strings, font weight styling, borders, and rounded corners. It supports `AllowMultiple = true`, enabling developers to stack multiple nested member readings side-by-side.

**The Problem:**
Modern game architectures favor clean data structures (composition, nested ScriptableObjects, state machines, serializable structs). However, Unity's default Hierarchy window only displays the GameObject's name. To inspect nested state variables (e.g. current stamina inside an AI sub-state object), developers must drill through nested foldouts in the Inspector.

**The Solution:**
Decorating components with `[HierarchyPropertyPath]`:
- **Deep Member Traversal:** Access nested sub-fields, properties, and serializable structs via dot notation (e.g. `"attributes.stamina"`).
- **Graceful Null Propagation:** Displays a configurable fallback string (e.g. `"None"` or `"—"`) without throwing `NullReferenceException` errors.
- **Multiple Stacked Badges:** Apply multiple `[HierarchyPropertyPath]` attributes to display multiple stats simultaneously.
- **Sleek Badge Styling:** Customize background badge colors, borders, font size, and text formatting.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[System.Serializable]
public class UnitStats
{
    public int level = 5;
    public float stamina = 85.5f;
}

[HierarchyPropertyPath(Path = "stats.level", Prefix = "LVL ", BadgeColor = "#1E293B", TextColor = "#F59E0B")]
public class CombatUnit : MonoBehaviour
{
    public UnitStats stats = new UnitStats();
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Field`, `Class`, `Property` |
| **Inherited** | Yes |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyPropertyPathRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyPropertyPathAttribute()
```

- Standard parameterless constructor. Dotted path and visual settings are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Path` | `string` | `""` | Dotted member path to evaluate (e.g. `"stats.currentHp"`). |
| `FormatString` | `string` | `"{0}"` | C# format string applied to the evaluated value. |
| `NullFallbackText` | `string` | `"—"` | Text displayed when any intermediate or leaf object is null. |
| `Prefix` | `string` | `""` | Optional string label prepended before the formatted value. |
| `TextColor` | `string` | `"#88FFAA"` | Hex color of the displayed value text. |
| `BadgeColor` | `string` | `"#1E2A22"` | Background hex color of the badge container pill. |
| `BorderColor` | `string` | `"#2E4A32"` | Hex border outline color, or empty for borderless. |
| `BorderRadius` | `float` | `3f` | Corner radius of the badge in pixels. |
| `FontSize` | `int` | `0` | Font size override in pixels, or `0` for default editor font size. |
| `Bold` | `bool` | `false` | Whether to render the badge text in bold. |
| `Width` | `float` | `0f` | Fixed badge width in pixels, or `0` to auto-calculate based on text width. |
| `Height` | `float` | `0f` | Fixed badge height in pixels, or `0` for row-adjusted height. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the badge remains active and updates during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[System.Serializable]
public class AIProfile
{
    public string faction = "Undead";
    public float aggressionRating = 0.85f;
}

[HierarchyPropertyPath(
    Path = "profile.faction", 
    Prefix = "FACTION: ", 
    BadgeColor = "#312E81", 
    TextColor = "#C7D2FE", 
    BorderColor = "#4338CA", 
    Bold = true, 
    XOffset = 4f)]
[HierarchyPropertyPath(
    Path = "profile.aggressionRating", 
    FormatString = "{0:P0}", 
    Prefix = "AGG: ", 
    BadgeColor = "#450A0A", 
    TextColor = "#FCA5A5", 
    BorderColor = "#991B1B", 
    XOffset = 95f)]
public class EnemyAIController : MonoBehaviour
{
    public AIProfile profile = new AIProfile();
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **Multiple Instances** | High | `AllowMultiple = true`. Use differing `XOffset` values to position multiple badges along the hierarchy row. |
| **`[HierarchyStatusDot]`** | High | Combine nested stat displays with status dots to highlight active states. |
| **`[HierarchyLabel]`** | High | Use `HierarchyLabel` for immediate field names and `HierarchyPropertyPath` for deep sub-properties. |
| **Deep Structures** | High | Resolves across serializable classes, structs, properties, and ScriptableObject references safely. |
