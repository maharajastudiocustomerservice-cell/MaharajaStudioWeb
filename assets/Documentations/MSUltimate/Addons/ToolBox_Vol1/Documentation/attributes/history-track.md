# [HistoryTrack]

> Records discrete serialized field mutations over time, persisting values, timestamps, usernames, and call stacks into an undo timeline.

---

## 1. Overview & Value Proposition

**What it does:**
`[HistoryTrack]` records changes made to a field or property over time, capturing the new value, previous value, timestamp, modifying user, and optional script call stack. Changes are visualized directly below the field via an inline interactive timeline bar (`ShowInlineTimeline`) or step graph (`ShowInlineGraph`), and are persisted to disk across recompiles and editor restarts.

**The Problem:**
Balancing game economy or tuning complex physics requires constant iterative adjustments. When a weapon balance tweak or level variable is inadvertently broken, developers and designers struggle to answer basic diagnostic questions: *"Who changed this value?"*, *"What was this set to yesterday before the recompile?"*, and *"Which script modified this at runtime?"*. Standard Unity offers only a volatile `Undo.RecordObject` buffer that disappears upon editor restart or domain reload.

**The Solution:**
Decorating fields or properties with `[HistoryTrack]`:
- **Persistent Change Audit Trail:** Persists value deltas, timestamps, and author usernames across editor sessions to disk in JSON format (`PersistAcrossSessions = true`).
- **Inline Timeline & Step Graph:** Renders a scrubbable mini-timeline directly beneath the property in the Inspector (`ShowInlineTimeline = true`).
- **Team Accountability & Collaboration:** Tracks the OS username of modifying developers (`TrackUser = true`), designates owners (`OwnerName`), and provides change reason prompts (`RequireReason = true`).
- **Field Locking & Policy Governance:** Lock critical parameters against accidental edits (`IsLocked = true`, `LockedBy = "LeadDesigner"`), or restrict editing to specific teammates (`AllowedEditors = "Alice, Bob"`).
- **Regression & Boundary Alerts:** Notifies developers if a value reverts to a previous regression state (`AlertOnRevert = true`) or breaches threshold limits (`ExpectedMin`, `ExpectedMax`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class WeaponBalanceData : MonoBehaviour
{
    [HistoryTrack(
        ColorHex = "#e67e22",
        ShowInlineTimeline = true,
        OwnerName = "Soutick",
        MaxEntries = 50)]
    public float baseDamage = 45f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ToolBox-Vol1 Addon |
| **Attribute Target** | `Field` \| `Property` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Inspector & HistoryTrack Window |
| **Render Engine** | UI Toolkit (`HistoryTrackDrawer`) & IMGUI Fallback |

---

## 4. Constructors & Parameters

```csharp
public HistoryTrackAttribute()
```

- Parameterless constructor defaults to `Order = 210`, 100 historical entries, and enabled inline timeline rendering.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MaxEntries` | `int` | `100` | Maximum number of change events stored per field before pruning the oldest. |
| `PersistAcrossSessions` | `bool` | `true` | Persist history to disk (JSON) across recompiles and editor restarts. |
| `CaptureStackTrace` | `bool` | `false` | When true, records the full C# call stack when values are mutated via scripts. |
| `ShowInlineTimeline` | `bool` | `true` | Renders a compact mini-timeline scrubber bar directly below the field in the Inspector. |
| `ShowInlineGraph` | `bool` | `false` | Renders an expandable step-function history graph below the timeline. |
| `GraphHeight` | `float` | `50f` | Height of the inline step graph in pixels. |
| `Collapsed` | `bool` | `true` | Whether the history timeline foldout starts in a collapsed state. |
| `AlertOnRevert` | `bool` | `false` | Warns if a value reverts back to an earlier historical value (regression detection). |
| `ExpectedMin` | `float` | `float.NaN` | Minimum expected value; triggers an alert badge if mutated below this floor. |
| `ExpectedMax` | `float` | `float.NaN` | Maximum expected value; triggers an alert badge if mutated above this ceiling. |
| `CorrelationGroup` | `string` | `""` | Group ID string for synchronizing timelines across multiple correlated fields. |
| `ColorHex` | `string` | `"#e67e22"` | Primary accent hex color for the timeline markers, dots, and graph lines. |
| `TrackUser` | `bool` | `true` | Automatically captures the current OS username with every change entry. |
| `RequireReason` | `bool` | `false` | Prompts the user to type an explanation before accepting a value change. |
| `IsLocked` | `bool` | `false` | Disallows Inspector edits, rendering a lock badge and designated owner notice. |
| `LockedBy` | `string` | `""` | Name or role of the team member who locked the field. |
| `AllowedEditors` | `string` | `""` | Comma-separated list of usernames permitted to modify this field. |
| `OwnerName` | `string` | `""` | Designated maintainer or owner displayed for team accountability. |
| `ChangePolicy` | `string` | `""` | Informative policy string displayed in the Inspector (e.g. `"Requires Lead approval"`). |
| `RequireApproval` | `bool` | `false` | Whether changes must be formally approved in the HistoryTrack window. |

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

namespace ProjectZero.Balancing
{
    public class EconomyBalanceConfig : ScriptableObject
    {
        [Header("Global Currency Multipliers")]
        [HistoryTrack(
            ColorHex = "#F39C12",
            OwnerName = "LeadEconomyDesigner",
            ChangePolicy = "Modifications directly affect live monetization.",
            ShowInlineTimeline = true,
            ShowInlineGraph = true,
            GraphHeight = 60f,
            ExpectedMin = 0.5f,
            ExpectedMax = 3.0f,
            AlertOnRevert = true,
            TrackUser = true,
            RequireReason = true)]
        public float goldDropMultiplier = 1.0f;

        [Header("Gated Tuning Field")]
        [HistoryTrack(
            IsLocked = true,
            LockedBy = "TechDirector",
            OwnerName = "TechDirector",
            ChangePolicy = "Locked during milestone RC1 freeze.")]
        public float serverTickRate = 60.0f;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[LiveTrack]`** | High | Pair `[HistoryTrack]` (discrete change history) with `[LiveTrack]` (continuous real-time telemetry). |
| **`[BoxGroup]`** | High | Nests cleanly within layout groups, displaying the mini-timeline inside the group container. |
| **`[ShowIf]`** | High | Timeline panel respects conditional visibility states dynamically. |
| **`[ValidateRange]`** | High | Combine validation bounds with historical audit trails for bulletproof tuning fields. |
