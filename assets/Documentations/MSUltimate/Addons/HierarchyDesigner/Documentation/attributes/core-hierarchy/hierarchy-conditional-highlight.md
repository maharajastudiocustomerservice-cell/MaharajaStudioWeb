# [HierarchyConditionalHighlight]

> Dynamically tints the hierarchy row background with customizable colors based on live boolean states or numeric thresholds.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyConditionalHighlight]` turns the hierarchy list into a responsive telemetry dashboard. Applied to a serialized field, `HierarchyConditionalHighlightRenderer` monitors field values in real time and paints a dynamic background highlight across the entire row (`FullRow = true`) or a right-side indicator band (`BandWidth = 80f`). For booleans, it displays distinct colors for true and false states (`TrueColor = "#1A3A1A"`). For numeric fields, it compares against a threshold (`Threshold = 50f`) or smoothly interpolates color gradients (`GradientMode = true`, `MaxValue = 100f`).

**The Problem:**
During playtesting and simulation debugging, developers must monitor critical runtime states (e.g., whether an AI has spotted the player, whether a boss shield is active, or whether a vehicle is out of fuel). Watching numeric fields in the Inspector is impossible when debugging multiple entities simultaneously.

**The Solution:**
Decorating critical runtime variables with `[HierarchyConditionalHighlight]`:
- **Live Scene Telemetry:** Spot state changes instantly across dozens of entities in the hierarchy without selecting them.
- **Dual Operating Modes:** Native support for boolean flags (`TrueColor` / `FalseColor`) and numerical thresholds (`Threshold` / `BelowColor`).
- **Smooth Gradient Mapping:** Map health or temperature from 0% to 100% across color gradients for dynamic heatmaps.
- **Full Row or Right Band:** Choose between full-row background tinting or unobtrusive right-hand edge color bands.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class SecurityPatrolDrone : MonoBehaviour
{
    [HierarchyConditionalHighlight(TrueColor = "#7F1D1D", TrueAlpha = 0.5f, FalseColor = "#064E3B", FalseAlpha = 0.3f)]
    public bool isAlertTriggered = false;

    public float batteryLevel = 84f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyConditionalHighlightRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyConditionalHighlightAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `TrueColor` | `string` | `"#1A3A1A"` | Hex color applied when condition is true or value is above threshold. |
| `TrueAlpha` | `float` | `0.4f` | Alpha transparency multiplier for the true/above highlight overlay. |
| `FalseColor` | `string` | `""` | Hex color applied when condition is false or value is below threshold. |
| `FalseAlpha` | `float` | `0.35f` | Alpha transparency multiplier for the false/below highlight overlay. |
| `Threshold` | `float` | `50f` | Numeric cutoff value separating above and below highlight colors. |
| `BelowColor` | `string` | `""` | Convenience alias for `FalseColor` in numeric threshold contexts. |
| `MaxValue` | `float` | `0f` | Maximum value for normalized gradient interpolation (or `0` for hard cutoff). |
| `GradientMode` | `bool` | `false` | When true, smoothly blends between colors based on field value. |
| `FullRow` | `bool` | `true` | Whether the highlight covers the entire row or only a right-side band. |
| `BandWidth` | `float` | `80f` | Width in pixels of the highlight band when `FullRow` is set to false. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the conditional highlight remains active in Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class RaidBossPhaseController : MonoBehaviour
{
    [Header("Boss Vitality")]
    [Tooltip("Health percentage that changes the hierarchy row from green to red when low.")]
    [HierarchyConditionalHighlight(
        Threshold = 25f, 
        TrueColor = "#064E3B", 
        BelowColor = "#7F1D1D", 
        TrueAlpha = 0.45f, 
        FalseAlpha = 0.6f, 
        FullRow = true)]
    public float currentHealthPercentage = 100f;

    [Header("Enrage State")]
    public bool isEnraged = false;
    public float enrageAttackSpeedMultiplier = 2.0f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyBadge]`** | High | Badges render on top of conditional row highlights with crisp contrast. |
| **Numeric Telemetry** | High | Supports `float`, `int`, `double`, and `bool` serialized field types. |
| **Hierarchy Selection** | High | Highlight alpha blends cleanly with Unity's native blue selection rectangle. |
| **Play Mode Performance**| High | Reads raw field reflection without boxing allocations during high-frequency updates. |
