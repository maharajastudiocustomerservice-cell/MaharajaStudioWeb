# [HierarchyStateColorText]

> Dynamically tints the hierarchy label based on whether a serialized numeric field satisfies low, mid, or high thresholds.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyStateColorText]` links the color of the GameObject's hierarchy row label directly to a serialized numeric field (such as `health`, `fuel`, `temperature`, or `aiThreatLevel`). Driven by `HierarchyStateColorTextRenderer`, it compares the live runtime or serialized value against `HighThreshold` and `LowThreshold`, dynamically coloring the name green (`HighColor`), yellow (`MidColor`), or red (`LowColor`).

**The Problem:**
During playtesting and scene debugging, tracking which AI actors are wounded, which generators are out of fuel, or which physics bodies have exceeded critical velocity thresholds requires clicking on each object individually to check the Inspector.

**The Solution:**
Decorating numeric fields with `[HierarchyStateColorText]`:
- **At-a-Glance Status Monitoring:** Immediately spot low-health enemies, depleted resources, or overheated systems directly from the Hierarchy window without selecting them.
- **Three-Tier Threshold Grading:** Configure custom boundaries (`HighThreshold = 70f`, `LowThreshold = 30f`) to seamlessly map healthy, warning, and critical states.
- **Custom Color Triad:** Set tailored hex colors for high (`HighColor`), medium (`MidColor`), and low (`LowColor`) states.
- **Zero Polling Lag:** Evaluates the member via reflection during IMGUI repaint passes, reflecting live changes immediately during Play Mode.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class EnemyHealth : MonoBehaviour
{
    [HierarchyStateColorText(HighThreshold = 75f, LowThreshold = 25f)]
    public float currentHealth = 100f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Field` \| `Property` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyStateColorTextRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyStateColorTextAttribute()
```

- Standard parameterless constructor. Threshold values and color codes are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `HighThreshold` | `float` | `70f` | Numeric cutoff value that triggers the high state color (value $\ge$ threshold). |
| `LowThreshold` | `float` | `30f` | Numeric cutoff value separating mid from low state colors (value $\ge$ threshold triggers mid). |
| `HighColor` | `string` | `"#2ECC71"` | Hex color string when value meets or exceeds `HighThreshold`. |
| `MidColor` | `string` | `"#F1C40F"` | Hex color string when value is between `LowThreshold` and `HighThreshold`. |
| `LowColor` | `string` | `"#E74C3C"` | Hex color string when value falls below `LowThreshold`. |
| `Bold` | `bool` | `true` | Whether to render the dynamically colored label characters in bold font weight. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether dynamic state evaluation remains active during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row decorations. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class ReactorCoreSubsystem : MonoBehaviour
{
    [Header("Core Integrity")]
    [HierarchyStateColorText(
        HighThreshold = 80f, 
        LowThreshold = 35f, 
        HighColor = "#10B981", 
        MidColor = "#F59E0B", 
        LowColor = "#EF4444", 
        Bold = true)]
    public float coreIntegrity = 100.0f;

    [Header("Cooling System")]
    public float coolantFlowRate = 12.5f;
    public bool emergencyVentsOpen = false;

    public void ApplyDamage(float amount)
    {
        coreIntegrity = Mathf.Clamp(coreIntegrity - amount, 0f, 100f);
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchySubtitleText]`** | High | Display live numeric values (`↳ 45.2%`) alongside the dynamically tinted object name. |
| **`[HierarchyTooltip]`** | High | Hover tooltips display detailed breakdown of subsystem components and active states. |
| **`[HierarchyTextColor]`** | Incompatible | Do not decorate with static text color attributes as state coloring overrides label tinting. |
| **`[HierarchyChildCounter]`** | High | Works cleanly with parent/child counting and tree branch connector guides. |
