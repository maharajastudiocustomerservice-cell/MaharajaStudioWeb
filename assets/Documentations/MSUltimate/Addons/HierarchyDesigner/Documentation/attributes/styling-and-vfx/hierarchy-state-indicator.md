# [HierarchyStateIndicator]

> Displays finite state machine status with transition pills and directional arrows directly on the hierarchy row.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyStateIndicator]` displays active state machine or enum values directly on the hierarchy row formatted with a directional arrow badge (`➔ State`). Driven by `HierarchyStateIndicatorRenderer`, it reads current state values from serialized fields or properties (`raw.ToString()`), wraps them in a rounded pill badge (`ActiveBadgeColor = "#2ED573"`), and renders crisp white state labels (`TextColor = "#FFFFFF"`).

**The Problem:**
Monitoring AI states (e.g., `Idle`, `Patrol`, `Chase`, `Attack`, `Flee`), player movement states (`Grounded`, `Airborne`, `Sliding`), or cutscene stages during play testing requires selecting each entity and inspecting internal state machine foldouts. When testing group behaviors (e.g. pack AI coordination), watching 8 entities simultaneously in the inspector is impossible.

**The Solution:**
Decorating state fields or properties with `[HierarchyStateIndicator]`:
- **Live State Machine Feedback:** Instantly see what state each AI or player entity is executing right in the hierarchy row.
- **Directional Arrow Cue:** Formats text with an intuitive directional prefix (e.g. `➔ Patrol`, `➔ Attack`).
- **Rounded Pill Container:** Auto-sizes around the text and applies custom background badge styling.
- **Supports Enums and Strings:** Evaluates any enum, string, or class state object via clean `.ToString()` resolution.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public enum EnemyState { Idle, Patrol, Chase, Attack }

public class EnemyBrain : MonoBehaviour
{
    [HierarchyStateIndicator(ActiveBadgeColor = "#6366F1")]
    public EnemyState currentState = EnemyState.Patrol;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Field`, `Property` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyStateIndicatorRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyStateIndicatorAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ActiveBadgeColor` | `string` | `"#2ED573"` | Hex background color of the active state pill badge. |
| `TextColor` | `string` | `"#FFFFFF"` | Hex text color for the state badge label. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the state indicator remains visible and updates during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public enum BossPhase { Phase1_Intro, Phase2_Enrage, Phase3_Desperation }

public class BossStateMachine : MonoBehaviour
{
    [Header("State Telemetry")]
    [HierarchyStateIndicator(
        ActiveBadgeColor = "#DC2626", 
        TextColor = "#FEF2F2", 
        XOffset = 6f)]
    public BossPhase activePhase = BossPhase.Phase1_Intro;

    public float phaseTimer = 0f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyStateSnapshot]`** | High | Use `HierarchyStateIndicator` for the single current state and `HierarchyStateSnapshot` for historical transition trails. |
| **`[HierarchyStatusDot]`** | High | Pair state indicators with status dots to represent both categorical state and health/error status. |
| **`[HierarchyEnumCycler]`** | High | Use `HierarchyEnumCycler` when you want clicking the badge to change enum values; use `HierarchyStateIndicator` for clean telemetry. |
| **Enum & String Types** | High | Works with any `Enum`, `string`, `int`, or object implementing `.ToString()`. |
