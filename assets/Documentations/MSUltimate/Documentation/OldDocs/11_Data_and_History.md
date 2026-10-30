# 11. Data and History Tracking

These attributes provide powerful telemetry and forensics tools for tracking field changes over time, both in the Editor and at Runtime.

---

## `[HistoryTrack]`
Tracks a field's change history over time, persisting discrete change events to disk. Unlike `LiveTrack`, it records only when values actually change.

**Key Features:**
- Records old/new values, timestamps, and change sources.
- Captures stack traces to identify which script modified a value.
- Team collaboration features: Track which user made a change, require reasons, and approval workflows.
- Forensics Window: A dedicated window for viewing and reverting changes across the entire project.

**Properties:**
| Property | Type | Description |
| :--- | :--- | :--- |
| `MaxEntries` | `int` | Maximum events stored per field. Default: `100`. |
| `PersistAcrossSessions` | `bool` | Saves history to JSON on disk. |
| `CaptureStackTrace` | `bool` | Records the C# call stack for each change. |
| `ShowInlineTimeline` | `bool` | Shows a compact history bar in the Inspector. |
| `AlertOnRevert` | `bool` | Warns if a value regresses to a previous state. |
| `RequireReason` | `bool` | Prompts for a "Change Reason" before allowing edits. |
| `IsLocked` | `bool` | Disallows changes and shows a "Locked by [User]" badge. |
| `RequireApproval` | `bool` | Changes are queued as "Pending" until approved in the History Window. |

---

## `[LiveTrack]`
Tracks a field's value continuously and renders a live sparkline graph and statistics directly in the Inspector.

**Key Features:**
- High-frequency sampling for physics, performance metrics, or AI state.
- Threshold alerts (Flash red when too high/low).
- Baseline snapshots for comparing current values against a "gold standard".
- Session recording and replay.

**Properties:**
| Property | Type | Description |
| :--- | :--- | :--- |
| `TimeWindow` | `float` | Rolling time window in seconds for the X-axis. |
| `SampleRate` | `float` | Seconds between samples. Default: `0.1s`. |
| `ShowGraph` | `bool` | Renders the inline sparkline. |
| `ShowStats` | `bool` | Shows Current, Δ, Min, Max, Avg, and Rate. |
| `AlertAbove` / `Below` | `float` | Thresholds for visual alerts. |
| `TrackingMode` | `Enum` | `EditMode`, `PlayMode`, or `Both`. |
| `RecordSession` | `bool` | Enables recording for later analysis in the Dashboard. |

---

## `[DeltaTracker]`
A lightweight alternative to HistoryTrack that simply displays the difference between the current value and the value when the inspector was loaded.

---

## `[FieldTimestamp]`
Automatically records and displays the date and time when the field was last modified.

---

## `[ProbabilityPie]`
Renders a collection of weighted items (`List<T>`, `T[]`, or `float[]`) as an interactive vector **Donut/Pie chart** and segmented probability distribution ribbon with 1-click normalization tools.

**Key Features:**
- **Vector Donut/Pie Chart:** Hardware-accelerated UI Toolkit vector canvas rendering smooth, anti-aliased sectors with item color coding.
- **Probability Ribbon:** Multi-color proportional horizontal bar displaying instant percentage breakdown on hover.
- **Interactive Legend:** Displays individual item names, raw weight, and exact percentage chance badges.
- **1-Click Balancing Tools:** Includes **"⚖️ Normalize (100%)"** to scale all weights proportionally to 100%, and **"🟰 Equalize"** to distribute weights equally across all items.
- **Flexible Struct/Class Binding:** Works seamlessly with custom structs/classes by specifying `WeightMember` and `LabelMember`.

**Properties:**
| Property | Type | Description |
| :--- | :--- | :--- |
| `WeightMember` | `string` | Name of the numeric weight field inside child items. Default: `"weight"`. |
| `LabelMember` | `string` | Name of the label/title field inside child items. Default: `"name"`. |
| `ShowPieChart` | `bool` | Whether to draw the circular vector Donut/Pie chart. Default: `true`. |
| `ShowPercentageBar`| `bool` | Whether to draw the stacked probability ribbon bar. Default: `true`. |
| `ShowLegend` | `bool` | Displays the legend table with names and percentages. Default: `true`. |
| `ShowActionButtons`| `bool` | Enables the Normalize and Equalize action buttons. Default: `true`. |
| `ChartRadius` | `float` | Radius of the vector chart in pixels. Default: `55`. |
| `DonutHoleRatio` | `float` | Hole ratio for donut chart (`0` = solid pie, `0.5` = donut). Default: `0.5`. |

**Example Usage:**
```csharp
[System.Serializable]
public class DropItem
{
    public string itemName;
    public float dropWeight = 10f;
    public GameObject prefab;
}

public class LootChest : ModularMonoBehaviour
{
    [ProbabilityPie(WeightMember = "dropWeight", LabelMember = "itemName")]
    public List<DropItem> lootTable = new List<DropItem>()
    {
        new DropItem { itemName = "Common Potion", dropWeight = 60f },
        new DropItem { itemName = "Rare Sword", dropWeight = 30f },
        new DropItem { itemName = "Legendary Ring", dropWeight = 10f }
    };
}
```

