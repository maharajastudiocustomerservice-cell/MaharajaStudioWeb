# [HideLabel]

> Hides the property name label, allowing the input field, slider, or preview to expand across the full row width.

---

## 1. Overview & Value Proposition

**What it does:**
Removes the standard text label prefix from a field or property so the editor control spans the entire width of the inspector.

**The Problem:**
In standard Unity, every serialized field reserves 40% to 50% of the inspector width on the left solely for its variable name. For large text fields, curve editors, visual previews, or compact inline sub-properties, this wasted label space squishes the actual input control into a cramped right column.

**The Solution:**
Add `[HideLabel]` to any field or property:
- **Maximum Input Space:** Sliders, text areas, curve graphs, and progress bars utilize 100% of the available inspector width.
- **Clean Embedded Forms:** When placing fields inside self-explanatory box groups or titled sections, redundant labels are eliminated.
- **Array & List Cleanliness:** Hides repetitive `Element 0`, `Element 1` labels in collections when paired with list element attributes.
- **Seamless Visual Stacking:** Perfect for pairing with `[Title]` or `[Header]` where the section headline already explains what the input represents.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class QuestDescription : MonoBehaviour
{
    [Header("Quest Briefing Note")]
    [HideLabel]
    [TextArea(4, 10)]
    public string detailedBriefing;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public HideLabelAttribute()
```

*This attribute has no constructor parameters.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Order` | `int` | `0` | Execution rendering order in the property modifier pipeline. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class LevelEnvironmentSettings : MonoBehaviour
{
    [Title("Day / Night Lighting Curve", "Defines ambient light multiplier across a 24-hour cycle")]
    [HideLabel]
    public AnimationCurve ambientLightOverDay;

    [Header("Broadcast Announcement")]
    [HideLabel]
    [TextArea(3, 6)]
    public string serverAnnouncementText;

    [Header("Global Danger Level")]
    [HideLabel]
    [ProgressBar(0, 100, ColorHex = "#e74c3c")]
    public float worldThreatLevel = 65f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[ProgressBar]` | Supported | Allows progress bars to span edge-to-edge across the inspector card. |
| `[Title]` / `[Header]` | Recommended | Pairs naturally: use the header as the description and let the input expand below. |
| `[BoxGroup]` | Supported | Functions seamlessly inside grouped cards and tab containers. |
| `[SuffixLabel]` | Supported | Suffix unit remains docked on the far right while the input claims the left space. |
