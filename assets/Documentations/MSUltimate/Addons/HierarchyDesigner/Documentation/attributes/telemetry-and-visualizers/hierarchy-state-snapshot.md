# [HierarchyStateSnapshot]

> Displays a real-time sliding history breadcrumb of finite state transitions directly on the hierarchy row during Play Mode.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyStateSnapshot]` captures finite state machine transitions and displays a real-time sliding breadcrumb trail (e.g. `Patrol → Chase → Attack`) on the hierarchy row. Driven by `HierarchyStateSnapshotRenderer`, it detects whenever the monitored state variable changes, adds the new state to an internal sliding history buffer (`MaxHistoryCount = 3`), formats past states in subtle gray (`HistoryColor = "#7F8C8D"`), and highlights the active state in bright green (`ActiveColor = "#2ECC71"`).

**The Problem:**
When debugging complex AI behaviors or character state machines, unexpected bugs frequently arise from invalid transition sequences (e.g., an AI skipping from `Stunned` directly into `Attack` without going through `Recover`). Catching these momentary skips in real time by looking at a single instantaneous state variable in the Inspector is nearly impossible.

**The Solution:**
Decorating state variables with `[HierarchyStateSnapshot]`:
- **Real-Time Transition Breadcrumbs:** Immediately observe how an entity arrived at its current state (e.g. `Idle → Alert → Chase`).
- **Configurable History Depth:** Retain the last 2, 3, or more consecutive states in the sliding window.
- **Color-Coded Status Distinction:** Active state is clearly highlighted while historical precursors remain dim.
- **Detailed History Tooltips:** Hovering over the badge displays full transition history descriptions.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public enum AIState { Idle, Patrol, Investigate, Combat }

public class SentryBot : MonoBehaviour
{
    [HierarchyStateSnapshot(MaxHistoryCount = 3, ActiveColor = "#10B981")]
    public AIState botState = AIState.Idle;
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
| **Render Engine** | `HierarchyStateSnapshotRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyStateSnapshotAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MaxHistoryCount` | `int` | `3` | Maximum number of recent states to display in the breadcrumb trail. |
| `ActiveColor` | `string` | `"#2ECC71"` | Hex text color for the current active state. |
| `HistoryColor` | `string` | `"#7F8C8D"` | Hex text color for past historical states. |
| `BackgroundColor` | `string` | `"#141C24"` | Hex background color of the breadcrumb badge container. |
| `BorderColor` | `string` | `"#243242"` | Hex border outline color around the badge. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the state history remains visible and active during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public enum CombatFSM { Guard, Parrying, Stunned, CounterAttacking }

public class BossCombatBrain : MonoBehaviour
{
    [Header("Combat FSM Telemetry")]
    [HierarchyStateSnapshot(
        MaxHistoryCount = 4, 
        ActiveColor = "#F59E0B", 
        HistoryColor = "#64748B", 
        BackgroundColor = "#0F172A", 
        BorderColor = "#334155", 
        XOffset = 6f)]
    public CombatFSM combatState = CombatFSM.Guard;

    public float poiseMeter = 100f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyStateIndicator]`** | High | Use `HierarchyStateIndicator` for a compact single pill, and `HierarchyStateSnapshot` for full sequence debugging. |
| **`[HierarchyStatusDot]`** | High | Place status dots alongside state snapshots to show entity health or connectivity. |
| **State Member Types** | High | Works directly with `enum`, `string`, `int`, or any class/struct implementing `.ToString()`. |
| **Play Mode Lifecycle** | High | Transition history is recorded during live gameplay and resets smoothly on session end. |
