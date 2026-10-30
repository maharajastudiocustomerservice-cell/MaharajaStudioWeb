# [SwipeActionRow]

> Renders a mobile-style swipeable list item where dragging horizontally reveals contextual quick-action buttons such as delete, reset, or inspect.

---

## 1. Overview & Value Proposition

**What it does:**
`[SwipeActionRow]` brings ubiquitous mobile list ergonomics into the Unity Inspector. By dragging an inspector row horizontally, the foreground property field slides to reveal an underlying contextual quick-action button (`ActionButtonText`, defaulting to `"RESET"` at 65px width) styled in a designated action color (`ActionColor`, defaulting to `#EF4444` red). Clicking the revealed button executes an instant reset to default values with full Undo tracking. It also implements `ICollectionElementAttribute` for multi-item list cascading.

**The Problem:**
Managing expansive serialized lists or arrays—such as inventory slots, dialogue trees, audio clips, or waypoint nodes—often clutters each row with redundant action buttons. Having permanent "Reset" or "Remove" buttons visible on every single line makes lists visually overwhelming.

**The Solution:**
Decorating list elements or fields with `[SwipeActionRow]`:
- **Hidden Contextual Actions:** Hides destructive or utility buttons beneath the row, keeping inspector lists clean until swiped.
- **Natural Touch/Drag Physics:** Supports horizontal mouse dragging with momentum to expose or conceal action buttons.
- **Customizable Action Surface:** Configure button label (`ActionButtonText`) and background color (`ActionColor`), such as red for delete, blue for duplicate, or amber for reset.
- **Universal Collection Cascading:** Implements `ICollectionElementAttribute` to effortlessly turn standard Unity lists and arrays into swipeable item tables.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class ProfileSettings : MonoBehaviour
{
    [SwipeActionRow(actionText: "DEFAULT", actionColor: "#EF4444")]
    public string usernameNickname = "PlayerOne";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Collection Element Support** | Yes (`ICollectionElementAttribute`) |

---

## 4. Constructors & Parameters

```csharp
public SwipeActionRowAttribute(string actionText = "RESET", string actionColor = "#EF4444")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `actionText` | `string` | `"RESET"` | Label text displayed on the revealed underneath quick-action button. |
| `actionColor` | `string` | `"#EF4444"` | Hex color string for the revealed button background (defaults to Red). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ActionButtonText` | `string` | `"RESET"` | Label string displayed on the revealed action button. |
| `ActionColor` | `string` | `"#EF4444"` | Hex color string for the revealed action button. |
| `IsEditable` | `bool` | `true` | Whether the row can be interactively swiped and clicked. |
| `Interactive` | `bool` | `true` | Alias for `IsEditable`. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class QuestLogManager : MonoBehaviour
{
    [Header("Quest Objectives List")]
    [SwipeActionRow(actionText: "ABANDON", actionColor: "#DC2626")]
    public List<string> activeQuestTitles = new List<string>
    {
        "Slay the Forest Behemoth",
        "Recover 5 Starlight Crystals",
        "Deliver Message to High Sage"
    };

    [Header("Pinned Objective")]
    [SwipeActionRow(actionText: "UNPIN", actionColor: "#F59E0B")]
    public string trackedPrimaryQuest = "Slay the Forest Behemoth";
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Sliding foreground layers clip cleanly within outer box layout bounds. |
| Collections (`List<T>`) | Supported | Implements `ICollectionElementAttribute` for elegant swipeable list rows. |
| `[ReadOnly]` | Supported | Disables swiping actions when marked read-only via `IsEditable = false`. |
