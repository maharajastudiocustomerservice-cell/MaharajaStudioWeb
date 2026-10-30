# [Calendar]

> Displays a string, timestamp, or SerializableDateTime field with an interactive web-style calendar and time picker popup.

---

## 1. Overview & Value Proposition

**What it does:**
Opens an interactive calendar popup with time steppers, preset themes, and relative time badges when clicking a date field.

**The Problem:**
Entering dates and timestamps in Unity requires typing arbitrary date strings (like `"2026-10-15 14:30:00"`) or calculating Unix epoch seconds by hand. A single formatting error, missing zero, or invalid day causes silent serialization bugs and live-ops parsing crashes.

**The Solution:**
Add `[Calendar]` to any date string or numeric timestamp field:
- **Interactive Visual Calendar:** Click to pick days, months, and years from a responsive calendar popup.
- **Integrated Time Stepper:** Toggle `IncludeTime` to adjust hours, minutes, and seconds with 12/24-hour modes.
- **Rich Theme Presets:** Choose from built-in theme presets (`Ocean`, `Emerald`, `Midnight`, `Sunset`, `Violet`) or custom colors.
- **Multi-Format Storage:** Works on `string`, `long` (Ticks, Unix seconds/milliseconds), `int`, and `SerializableDateTime`.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class LiveOpsEventConfig : MonoBehaviour
{
    [Calendar]
    public string eventStartDate = "2026-12-01";

    [Calendar(includeTime: true)]
    public string raidBossSpawnTime;

    [Calendar(CalendarTheme.Emerald)]
    public long registrationDeadlineTicks;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `string`, `long`, `int`, `SerializableDateTime`, or collections (`string[]`, `List<string>`, `SerializableDateTime[]`, `List<SerializableDateTime>`) |
| **Collection Cascading**| Supported via `ICollectionElementAttribute` (`CollectionElementRole.Element \| Key \| Value \| NullableValue \| TupleItem`) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public CalendarAttribute()
public CalendarAttribute(string dateFormat)
public CalendarAttribute(CalendarTheme theme)
public CalendarAttribute(string dateFormat, string accentColor)
public CalendarAttribute(bool includeTime)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `dateFormat` | `string` | `"yyyy-MM-dd"` | Date format string for display and serialization. |
| `theme` | `CalendarTheme` | `CalendarTheme.Default` | Pre-configured theme preset for the calendar popup. |
| `accentColor` | `string` | `"#3B82F6"` | Hex color for selected days and active highlights. |
| `includeTime` | `bool` | `false` | If `true`, enables time controls (hours, minutes, seconds). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `DateFormat` | `string` | `"yyyy-MM-dd"` | Custom date formatting string pattern. |
| `TimestampStorage` | `CalendarTimestampStorage` | `Ticks` | Storage mode for numbers (`Ticks`, `UnixSeconds`, `UnixMilliseconds`). |
| `IncludeTime` | `bool` | `false` | Enables hours and minutes selectors in popup. |
| `ShowSeconds` | `bool` | `false` | Enables seconds selector in the time picker. |
| `Use24HourFormat` | `bool` | `true` | Uses 24-hour time instead of 12-hour AM/PM format. |
| `FirstDayOfWeek` | `DayOfWeek` | `Monday` | First column day of the week in the calendar grid. |
| `MinDate` | `string` | `null` | Earliest selectable date boundary string. |
| `MaxDate` | `string` | `null` | Latest selectable date boundary string. |
| `MinuteStep` | `int` | `1` | Stepping increment for minute arrows (e.g. 5, 15). |
| `ShowWeekNumbers` | `bool` | `false` | Displays ISO 8601 week numbers on the left edge. |
| `ShowRelativeTime` | `bool` | `true` | Displays friendly relative badges (e.g. "In 3 days"). |
| `Inline` | `bool` | `false` | Renders calendar widget inline directly in inspector. |
| `Theme` | `CalendarTheme` | `Default` | Theme palette preset (`Default`, `Ocean`, `Emerald`, etc.). |
| `AccentColor` | `string` | `"#3B82F6"` | Primary accent hex color. |
| `HeaderColor` | `string` | `"#1E293B"` | Header background hex color. |
| `BackgroundColor` | `string` | `"#0F172A"` | Popup background hex color. |
| `TextColor` | `string` | `"#F8FAFC"` | Primary text hex color. |
| `BorderColor` | `string` | `"#334155"` | Border and divider hex color. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.Runtime.Types;

public class BattlePassSeason : MonoBehaviour
{
    [Header("Season Schedule")]
    [Calendar(Theme = CalendarTheme.Ocean, ShowRelativeTime = true, ShowPresetsSidebar = true)]
    public string seasonLaunchDate = "2026-11-01";

    [Calendar(includeTime: true, ShowSeconds = false, AccentColor = "#f39c12")]
    public string seasonCutoffTimestamp;

    [Header("Server Epoch Storage")]
    [Calendar(TimestampStorage = CalendarTimestampStorage.UnixSeconds)]
    public long serverSyncTimestampUtc;

    [Header("Direct Collection Cascading")]
    [Calendar(Theme = CalendarTheme.Emerald, DateFormat = "yyyy-MM-dd")]
    [Tooltip("Cascades calendar date picker to every string entry.")]
    public List<string> tournamentMilestoneDates = new List<string>
    {
        "2026-11-10",
        "2026-11-20"
    };

    [Calendar(IncludeTime = true, Theme = CalendarTheme.Violet)]
    [Tooltip("Cascades date/time controls to every SerializableDateTime slot.")]
    public SerializableDateTime[] maintenanceWindows;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Functions cleanly inside box groups and tab containers. |
| `[ShowIf]` | Supported | Conditionally displays date pickers based on scheduled event toggles. |
| `[ReadOnly]` | Supported | Locks the date from manual edits while keeping formatted display. |
| Collections (`List<T>`, `T[]`) | Supported | Implements `ICollectionElementAttribute` to automatically cascade calendar pickers to array/list elements. |
