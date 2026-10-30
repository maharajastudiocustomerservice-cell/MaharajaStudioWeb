# [HierarchyFieldAlert]

> Draws an attention-grabbing warning icon and pulsing background overlay on the hierarchy row when a field value violates defined constraints.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyFieldAlert]` turns the hierarchy list into an active error and outlier surveillance radar. Powered by `HierarchyFieldAlertRenderer`, it monitors numeric bounds (`MinValue = 0f`, `MaxValue = float.MaxValue`) or boolean criteria (`AlertWhenFalse = true`). When the field violates these rules, it renders a pulsing alert icon (`AlertIcon = "d_console.erroricon"`, `AlertIconColor = "#FF6666"`, `Pulse = true`) alongside an urgent background row tint (`AlertColor = "#400000"`, `AlertAlpha = 0.55f`).

**The Problem:**
Out-of-bounds gameplay variables—such as negative enemy health, zero weapon damage, depleted fuel tanks, or unassigned critical booleans—silently corrupt game balance. Tracking down which GameObject in a scene of 500 entities has invalid numbers usually requires manual inspection or custom console log spam.

**The Solution:**
Decorating critical thresholds with `[HierarchyFieldAlert]`:
- **Immediate Hierarchy Error Surfacing:** Spot corrupt, zeroed, or out-of-bounds variables in seconds without opening console logs.
- **Pulsing Animation Support:** Smooth alpha oscillation (`Pulse = true`) ensures alerts immediately catch the developer's eye.
- **Multi-Type Validation:** Seamlessly handles numeric floats/ints (minimum and maximum bounds) and boolean failure states (`AlertWhenFalse`).
- **Flexible Alert Scope:** Choose between full row highlighting (`FullRowAlert = true`) or a discreet right-hand icon badge.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class EnemyHealthEntity : MonoBehaviour
{
    [HierarchyFieldAlert(MinValue = 1f, AlertColor = "#7F1D1D", AlertIconColor = "#EF4444")]
    public float currentHealth = 100f;

    public float maxHealth = 100f;
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
| **Render Engine** | `HierarchyFieldAlertRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyFieldAlertAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MinValue` | `float` | `0f` | Minimum acceptable numeric value; values strictly below this trigger the alert. |
| `MaxValue` | `float` | `float.MaxValue` | Maximum acceptable numeric value; values strictly above this trigger the alert. |
| `AlertWhenFalse` | `bool` | `false` | When true, triggers the alert if a monitored boolean field evaluates to false. |
| `AlertColor` | `string` | `"#400000"` | Hex background color of the row tint when the alert is triggered. |
| `AlertAlpha` | `float` | `0.55f` | Alpha transparency of the background alert tint. |
| `AlertIcon` | `string` | `"d_console.erroricon"` | Built-in Unity icon name drawn on the hierarchy row during alert. |
| `AlertIconColor` | `string` | `"#FF6666"` | Hex color tint applied to the alert icon. |
| `AlertIconSize` | `float` | `13f` | Dimension in pixels of the alert icon. |
| `Pulse` | `bool` | `true` | Whether the alert overlay pulses continuously in alpha for high visibility. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin. |
| `FullRowAlert` | `bool` | `true` | Whether the alert background tint spans the full row width. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the field alert remains active and pulsing in Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class PowerGridGenerator : MonoBehaviour
{
    [Header("Generator Stability")]
    [Tooltip("Alerts with pulsing red glow if reactor core temperature exceeds 850 degrees.")]
    [HierarchyFieldAlert(
        MinValue = 100f, 
        MaxValue = 850f, 
        AlertColor = "#881337", 
        AlertIconColor = "#FDA4AF", 
        Pulse = true, 
        FullRowAlert = true)]
    public float coreTemperatureCelsius = 420f;

    [Header("Grid Connection")]
    [Tooltip("Alerts if the generator disconnects from the substation.")]
    [HierarchyFieldAlert(AlertWhenFalse = true, AlertIcon = "d_console.warnicon", AlertIconColor = "#FBBF24")]
    public bool isConnectedToSubstation = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyBadge]`** | High | Badges remain readable over alert backdrops due to alpha transparency blending. |
| **`[HierarchyHighlight]`** | High | Alert overrides standard static highlights when an active violation is present. |
| **Zero Runtime Overhead** | High | Only evaluates logic in Editor update cycles; no runtime heap allocations or garbage collection. |
| **Multi-Object Auditing**| High | Highly recommended for level design passes to quickly verify scene integrity before builds. |
