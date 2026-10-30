# [HierarchyEventHookTracker]

> Audits UnityEvent listener counts on the hierarchy row, flagging empty or broken callback hooks with rich tooltips.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyEventHookTracker]` inspects serialized `UnityEvent` fields on the GameObject and displays a diagnostic listener badge directly on the hierarchy row. Driven by `HierarchyEventHookTrackerRenderer`, it audits every persistent listener hook:
- **Valid Connections:** Displays the active listener count in green (`ValidColor = "#27AE60"`) (e.g. `"[2 evt]"`).
- **Broken / Missing Targets:** Immediately turns red (`BrokenColor = "#C0392B"`) and alerts with `"❌ broken"` if any listener target object is null or its bound method is missing.
- **Empty Listeners:** Alerts with orange/amber badge (`EmptyColor = "#D35400"`) when no callbacks are wired (`WarnIfEmpty = true`).
- **Rich Diagnostic Tooltips:** Hovering over the badge displays a multi-line breakdown of every connected target and method name (e.g., `✔ AudioManager.PlaySfx()`, `❌ MISSING TARGET / METHOD`).

**The Problem:**
Broken UnityEvents are notorious causes of silent bugs in gameplay logic (UI buttons that don't trigger events, triggers that don't open doors, health callbacks that fail to report deaths). Because broken events do not throw compile-time errors, developers only discover them during manual play sessions.

**The Solution:**
Decorating event-driven components with `[HierarchyEventHookTracker]`:
- **Immediate Broken Event Detection:** Catch missing targets and renamed method references directly in the Hierarchy.
- **Empty Callback Warnings:** Identify unhooked events before shipping or testing scenes.
- **Class or Field Targeting:** Can be placed directly on a `UnityEvent` field or on the class declaring `EventFieldName`.
- **Multi-Event Stacking:** Apply multiple attributes to monitor distinct events (e.g., `onClicked`, `onHover`, `onCancel`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using UnityEngine.Events;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class InteractionTrigger : MonoBehaviour
{
    [HierarchyEventHookTracker]
    public UnityEvent onInteracted;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Field`, `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyEventHookTrackerRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyEventHookTrackerAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `EventFieldName` | `string` | `""` | Optional target `UnityEvent` field name when applied at the class level. |
| `WarnIfEmpty` | `bool` | `true` | Displays a warning badge if zero persistent listeners are wired to the event. |
| `ValidColor` | `string` | `"#27AE60"` | Hex color of the badge when all configured listeners are valid and wired. |
| `EmptyColor` | `string` | `"#D35400"` | Hex color of the badge when no listeners are assigned. |
| `BrokenColor` | `string` | `"#C0392B"` | Hex color of the badge when a listener has a missing target or missing method. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the event tracker badge remains visible during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using UnityEngine.Events;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyEventHookTracker(EventFieldName = nameof(onDamageTaken), WarnIfEmpty = false, XOffset = 6f)]
[HierarchyEventHookTracker(EventFieldName = nameof(onDeath), WarnIfEmpty = true, XOffset = 70f)]
public class DamageableEntity : MonoBehaviour
{
    [Header("Event Callbacks")]
    public UnityEvent<float> onDamageTaken;
    public UnityEvent onDeath;

    public float maxHealth = 100f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **Multiple Instances** | High | `AllowMultiple = true`. Use differing `XOffset` values to monitor multiple events on the same entity. |
| **`[HierarchyFieldAlert]`** | High | Pair event hook trackers with field alerts to validate both events and reference fields. |
| **`[HierarchyStatusDot]`** | High | Use status dots for live operational state and event hook trackers for architectural callback wiring. |
| **`UnityEvent` Subclasses** | High | Compatible with parameterless `UnityEvent` and generic events (`UnityEvent<T>`, etc.). |
