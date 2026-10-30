# [LabelText]

> Overrides the inspector display label of a serialized field or property with clean custom text.

---

## 1. Overview & Value Proposition

**What it does:**
Renames the field label shown in the Inspector to any friendly string without renaming the actual C# code variable.

**The Problem:**
In standard Unity, the Inspector automatically generates labels from variable names (`m_playerMaxHealth` becomes `Player Max Health`). When variable names must follow coding conventions or acronyms, the resulting labels are cryptic, ugly, or unintuitive for designers.

**The Solution:**
Add `[LabelText]` to any field:
- **Friendly Inspector Names:** Use readable terms like `Maximum Hit Points` or `Fire Rate (Rounds/Sec)` without breaking code naming conventions.
- **Acronym & Symbol Support:** Freely include punctuation, symbols, and capitalized acronyms (e.g. `UI / HUD Scale`, `FOV Angle`).
- **Safe Refactoring:** Change designer-facing display names anytime without triggering Unity serialization resets or breaking prefab connections.
- **Lightweight Execution:** Zero runtime overhead with instantaneous editor label replacement.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class TurretController : MonoBehaviour
{
    [LabelText("Rounds Per Minute")]
    public float rpm = 600f;

    [LabelText("Max Range (Meters)")]
    public float effectiveRange = 45f;
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

### Collection Behavior

| Target Placement | Cascades to Elements? | Behavior / Architectural Rationale |
| :--- | :---: | :--- |
| `List<T>`, `T[]` (Container) | **No (By Design)** | Renames the collection foldout title in the Inspector while preserving individual item indices (`Element 0`, `Element 1`). Element cascading is deliberately rejected because overwriting all item labels with the same static text destroys row indexing. |
| Nested Class Members | N/A | When placed on fields within a `[Serializable]` class stored in a list, each row's child field correctly displays the custom label. |

---

## 4. Constructors & Parameters

```csharp
public LabelTextAttribute(string text)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `text` | `string` | *(Required)* | The display label text string to show in the inspector. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Text` | `string` | *(Required)* | Custom display label string. |
| `Order` | `int` | `0` | Field modifier pipeline processing order. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class GraphicSettings : MonoBehaviour
{
    [Header("Display Quality")]
    [LabelText("Target Resolution Scale (%)")]
    [Range(25, 200)]
    public int renderScalePercent = 100;

    [LabelText("Anti-Aliasing (MSAA Tier)")]
    public int msaaSampleCount = 4;

    [LabelText("Enable Dynamic V-Sync")]
    public bool useAdaptiveSync = true;

    [Header("Display Resolutions")]
    [LabelText("Supported Screen Resolutions")]
    public List<string> displayResolutions = new List<string> { "1920x1080", "2560x1440", "3840x2160" };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[LabelWidth]` | Recommended | Combine together when using longer custom label titles to avoid text clipping. |
| `[SuffixLabel]` | Supported | Works seamlessly with suffix measurement units. |
| `[BoxGroup]` | Supported | Renders inside group layouts and tabs without issues. |
| Collections (`List<T>`, `T[]`) | Container Only | Customizes collection container foldout label; does not cascade to child items to prevent wiping element numbers. |

