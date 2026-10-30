# [StepProgressor]

> Renders a multi-step milestone progress strip with glowing connectors, node badges, and interactive step selection.

---

## 1. Overview & Value Proposition

**What it does:**
`[StepProgressor]` transforms discrete integers or Enum stages into a modern multi-stage milestone stepper. It renders connected circular step nodes (`StepSize`) linked by illuminated connector bars. Completed stages illuminate in `ActiveColor`, unreached stages rest in `InactiveColor`, and the currently active node pulses with an ambient aura (`PulseGlowColor`). Users can click or scrub across milestone nodes to change active steps interactively.

**The Problem:**
Tutorial flows, quest objectives, crafting pipelines, and onboarding phases are sequential state machines. Standard enum dropdowns or raw integer fields provide no geographic representation of where the entity currently sits within the larger progression sequence.

**The Solution:**
Decorating integer or Enum progress fields with `[StepProgressor]`:
- **Visual Milestone Flow:** Clearly illustrates sequence completion from initial step to finale.
- **Current Step Pulse Glow:** Emphasizes the currently active milestone with a breathing aura (`PulseGlowColor`).
- **Interactive Step Selection:** Click directly on milestone node circles (`IsEditable = true`) to advance or rewind states.
- **Custom Stage Titles:** Provide human-readable stage descriptions via `StepLabels`.
- **Collection Cascading:** Implements `ICollectionElementAttribute` for quest tracker lists or multi-character tutorial logs.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class QuestProgress : MonoBehaviour
{
    [StepProgressor(totalSteps: 5, activeColor: "#3B82F6")]
    public int currentQuestPhase = 2;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `Enum`, `int`, `byte`, `short`, `long`, `float` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Collection Element Support** | Yes (`ICollectionElementAttribute`) |

---

## 4. Constructors & Parameters

```csharp
public StepProgressorAttribute(int totalSteps = 4, string activeColor = "#3B82F6")

public StepProgressorAttribute(
    string dynamicTotalStepsMember, 
    string activeColor = "#3B82F6"
)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `totalSteps` | `int` | `4` | Total number of milestone steps rendered in the progress strip. |
| `dynamicTotalStepsMember` | `string` | — | Name of a member returning dynamic milestone count. |
| `activeColor` | `string` | `"#3B82F6"` | Hex color string for completed/active milestone nodes and connectors. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `TotalSteps` | `int` | `4` | Total milestone step count. |
| `DynamicTotalStepsMember` | `string` | `null` | Name of a member returning dynamic milestone count. |
| `ActiveColor` | `string` | `"#3B82F6"` | Hex color string for completed/active steps. |
| `InactiveColor` | `string` | `"#334155"` | Hex color string for unreached future steps. |
| `PulseGlowColor` | `string` | `"#60A5FA"` | Hex color string for the active step pulsating glow. |
| `StepSize` | `float` | `14f` | Diameter in pixels of milestone node circles. |
| `DrawInputField` | `bool` | `true` | Whether to draw the standard serialized property field beside or above the strip. |
| `ShowInputField` | `bool` | `true` | Alias for `DrawInputField`. |
| `IsEditable` | `bool` | `true` | Whether clicking milestone nodes adjusts the active step. |
| `Interactive` | `bool` | `true` | Alias for `IsEditable`. |
| `CustomLabel` | `string` | `null` | Optional label displayed beside the step progressor. |
| `ShowValue` | `bool` | `true` | Whether to display step index numbers inside nodes. |
| `StepLabels` | `string[]` | `null` | Optional array of custom milestone titles (e.g., `["Start", "Infiltrate", "Extract"]`). |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public enum MissionState
{
    Briefing = 0,
    Infiltration = 1,
    Sabotage = 2,
    Extraction = 3,
    Debrief = 4
}

public class CampaignMission : MonoBehaviour
{
    [Header("Mission Stepper Progression")]
    [StepProgressor(
        totalSteps: 5, 
        activeColor: "#10B981", 
        PulseGlowColor = "#34D399",
        InactiveColor = "#1E293B",
        StepSize = 16f,
        CustomLabel = "MISSION PHASE",
        StepLabels = new string[] { "Briefing", "Infiltrate", "Sabotage", "Extract", "Complete" }
    )]
    public MissionState activePhase = MissionState.Sabotage;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Aligns cleanly inside narrative trackers or objective containers. |
| `[EditorSoundEffect]` | Stacking | Triggers mechanical switch clicks whenever users jump between milestone steps. |
| Arrays & Lists | Supported | Implements `ICollectionElementAttribute` for lists of tutorial chapters or quest chains. |
