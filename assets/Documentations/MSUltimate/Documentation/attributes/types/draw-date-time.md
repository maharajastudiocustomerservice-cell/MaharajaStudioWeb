# [DrawDateTime]

> Customizes the visual presentation of SerializableDateTime fields with quick-set buttons for Now, Today, and Clear, plus configurable Date/Time section visibility.

---

## 1. Overview & Value Proposition

**What it does:**
Transforms complex date and time fields (`SerializableDateTime`) into a polished, user-friendly editor interface. Adds one-click quick-set action buttons ("Now", "Today", "Clear") and allows toggling date or time components on and off.

**The Problem:**
Entering dates, event timestamps, savefile creation times, or seasonal event windows in the Unity Inspector often requires manually entering year, month, day, hour, minute, and second values across multiple numeric fields, which is slow and error-prone.

**The Solution:**
Decorate any `SerializableDateTime` field with `[DrawDateTime]`:
- **Quick-Action Buttons:** Instantly stamp the current system time ("Now") or today's midnight timestamp ("Today").
- **Flexible Section Filtering:** Use `HideTime = true` for date-only calendars (e.g. daily rewards) or `HideDate = true` for time-of-day clocks.
- **Reset Support:** Fast one-click "Clear" button resets timestamps to zero/epoch.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.Types;

public class DailyEvent : MonoBehaviour
{
    [DrawDateTime(ShowNowButton = true, ShowTodayButton = true)]
    public SerializableDateTime eventStart;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `SerializableDateTime`, or collections (`SerializableDateTime[]`, `List<SerializableDateTime>`) |
| **Collection Cascading**| Supported via `ICollectionElementAttribute` (`CollectionElementRole.Element \| Key \| Value \| NullableValue \| TupleItem`) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public DrawDateTimeAttribute()
```

*This attribute uses parameterless initialization; customize its appearance via object initializer properties.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ShowNowButton` | `bool` | `true` | Shows the "Now" quick-set button to stamp the current system time. |
| `ShowTodayButton` | `bool` | `false` | Shows the "Today" button to stamp today at 00:00:00 midnight. |
| `ShowClearButton` | `bool` | `true` | Shows the "Clear / Reset" button to wipe timestamp values. |
| `HideTime` | `bool` | `false` | If true, hides hour/minute/second fields and only displays date fields. |
| `HideDate` | `bool` | `false` | If true, hides year/month/day fields and only displays time fields. |
| `Order` | `int` | `0` | Execution priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.Types;

public class QuestScheduleConfig : MonoBehaviour
{
    [Header("Seasonal Event Window (Date Only)")]
    [DrawDateTime(HideTime = true, ShowTodayButton = true)]
    public SerializableDateTime seasonStartDate;

    [Header("Daily Reset Trigger (Time Only)")]
    [DrawDateTime(HideDate = true, ShowNowButton = false)]
    public SerializableDateTime dailyResetTime;

    [Header("Live Server Maintenance Window")]
    [DrawDateTime(ShowNowButton = true, ShowClearButton = true)]
    public SerializableDateTime maintenanceTimestamp;

    [Header("Direct Collection Cascading")]
    [DrawDateTime(HideTime = true, ShowTodayButton = true)]
    [Tooltip("Cascades date-only controls with 'Today' button to every slot.")]
    public SerializableDateTime[] scheduledMaintenanceWindows;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Renders cleanly inside layout cards and foldouts. |
| `[ShowIf]` | Supported | Conditionally hide or show timestamp fields dynamically. |
| `[ReadOnly]` | Supported | Disables the quick buttons and locks timestamp inputs. |
| Collections (`List<T>`, `T[]`) | Supported | Implements `ICollectionElementAttribute` to automatically cascade date/time layout controls to collection elements. |

