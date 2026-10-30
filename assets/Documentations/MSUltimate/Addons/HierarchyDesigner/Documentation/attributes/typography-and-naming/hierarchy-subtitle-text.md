# [HierarchySubtitleText]

> Renders a secondary subtext or live field value subtitle next to the GameObject name in the hierarchy.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchySubtitleText]` renders a secondary sub-label directly beside or beneath the GameObject name in the Unity Hierarchy window. It supports either static secondary text (`StaticSubtitle = "LOD 0"`) or dynamic live reflection binding to a component field (`FieldName = "currentScore"` or `FieldName = "currentState"`), formatted through a customizable string template (`Format = "↳ {0}"`).

**The Problem:**
Developers frequently need quick visibility into secondary properties—such as the active state machine state, current AI target, pool capacity, or prefab variation—without constantly selecting objects and digging through Inspector tabs.

**The Solution:**
Decorating components with `[HierarchySubtitleText]`:
- **Live Reflection Binding:** Automatically queries the specified field (`FieldName`) on the component and formats its value in real time.
- **Static Subtitle Fallback:** Allows quick static descriptive tags (`StaticSubtitle = "Main Canvas"`) when dynamic reflection is not required.
- **Customizable Format Templates:** Supports custom template prefixes and symbols (`Format = "↳ {0}"`, `"[{0}]"`, `":: {0}"`).
- **Muted Subtext Styling:** Rendered in a refined muted tone (`TextColor = "#718093"`) with italic styling so it complements rather than overshadows the main object name.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchySubtitleText(FieldName = "currentState", Format = "↳ [{0}]", TextColor = "#94A3B8")]
public class EnemyAIStateController : MonoBehaviour
{
    public string currentState = "Patrol";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class` \| `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchySubtitleTextRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchySubtitleTextAttribute()
```

- Standard parameterless constructor. Subtitle source, format template, and text color are configured via object initializers.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Format` | `string` | `"↳ {0}"` | String format template used to render the subtitle value. |
| `FieldName` | `string` | `""` | Optional name of a component field to read live values from via reflection. |
| `StaticSubtitle` | `string` | `""` | Static subtitle string displayed when `FieldName` is empty. |
| `TextColor` | `string` | `"#718093"` | Hex color string for the subtitle text. |
| `Italic` | `bool` | `true` | Whether to render the subtitle characters in italics. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether subtitle values update and remain visible during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row decorations. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchySubtitleText(
    FieldName = "allocatedUnits", 
    Format = "↳ active: {0}/100", 
    TextColor = "#38BDF8", 
    Italic = true)]
public class SpawnPoolManager : MonoBehaviour
{
    [Header("Pool Statistics")]
    public int allocatedUnits = 42;
    public float respawnFrequency = 1.5f;
    public bool isPoolExhausted = false;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyPrefixBadge]`** | High | Combines front-side discipline badges (`[AI]`) with back-side live subtitles (`↳ Patrol`). |
| **`[HierarchyTooltip]`** | High | Displays complete component configuration breakdown on hover. |
| **`[HierarchyIcon]`** | High | Displays component icons at the far right without overlapping the subtitle. |
| **`[HierarchyTextColor]`** | High | Pairs cleanly: main name uses `[HierarchyTextColor]` while secondary info uses `[HierarchySubtitleText]`. |
