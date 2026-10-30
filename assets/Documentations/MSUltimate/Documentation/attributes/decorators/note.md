# [Note]

> Renders an expandable note callout attached to a field with optional in-place editing, icons, and card styling.

---

## 1. Overview & Value Proposition

**What it does:**
Attaches a clean, non-intrusive textual note or collapsible info card directly beneath an inspector field, with optional inline editing.

**The Problem:**
Standard HelpBoxes and InfoBoxes take up substantial vertical screen space even when closed. When designing complex systems, developers want subtle, toggleable notes or scratchpads where designers can read or update instructions without cluttering the main inspector layout.

**The Solution:**
Add `[Note]` to any field or property:
- **Collapsible or Inline:** Expandable note toggle button keeps inspectors compact and clutter-free.
- **In-Place Live Editing:** Set `AllowEdit = true` so designers can edit note messages directly in the Inspector.
- **Custom Card Styling:** Fully style borders, background tint, padding, typography, and button icons.
- **Zero Build Footprint:** Stripped automatically in player builds with no runtime overhead.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class SkillTreeConfig : MonoBehaviour
{
    [Note("Unlocking this node grants +15% Fire Damage to all spells.")]
    public int fireMasteryLevel = 1;

    [Note("Tuning in progress: verify base DPS before build cutoff.", AllowEdit = true, ButtonColor = "#f39c12")]
    public float balanceDpsTarget = 145f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **Interfaces** | `ICollectionElementAttribute` |
| **UI Toolkit Compatible** | Yes |

### Collection Cascading Behavior

| Target Placement | Cascades to Elements? | Behavior / Notes |
| :--- | :---: | :--- |
| `List<T>`, `T[]` (Default) | No | Attaches the note toggle button to the collection foldout container header. |
| `List<T>`, `T[]` (`ApplyToElements = true`) | **Yes** | Displays a note toggle button beside each individual collection item row. |
| `SerializableDictionary<K, V>` | Opt-In | Can cascade to key/value rows when `ApplyToElements = true`. |

---

## 4. Constructors & Parameters

```csharp
public NoteAttribute(string defaultMessage, string colorHex = null)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `defaultMessage` | `string` | *(Required)* | Default note message content. |
| `colorHex` | `string` | `null` | Hex color string for the note button/badge. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Message` | `string` | *(Required)* | Note body text. |
| `AllowEdit` | `bool` | `false` | If `true`, allows editing the note message in-place inside the inspector. |
| `ApplyToElements` | `bool` | `false` | When `true`, cascades note callout buttons down to individual collection element rows. |
| `ButtonText` | `string` | `""` | Text label for the note toggle button. |
| `Icon` | `string` | `"d_console.infoicon"` | Built-in Unity icon name for the note button. |
| `ButtonColor` / `ColorHex` | `string` | `""` | Hex background color for the note toggle button. |
| `TextColor` | `string` | `""` | Hex text color for the button label. |
| `BackgroundColor` | `string` | `"#00000033"` | Hex background color for the expanded note card. |
| `BorderColor` | `string` | `"#888888"` | Hex border outline color for the note card. |
| `BorderWidth` | `float` | `1f` | Border outline line thickness in pixels. |
| `BorderRadius` | `float` | `3f` | Corner rounding radius in pixels. |
| `FontSize` | `float` | `12f` | Font size for the note text message. |
| `Alignment` | `UiAlignment` | `UiAlignment.Left` | Text alignment within the note card. |
| `Padding` | `float` | `8f` | Internal padding in pixels inside the note card. |
| `FullWidth` | `bool` | `false` | Stretches note edge-to-edge across the inspector card. |
| `AboveGroup` | `bool` | `false` | Renders above parent layout group boundaries. |
| `Order` | `int` | `0` | Execution priority relative to other decorator attributes. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class WorldGeneratorConfig : MonoBehaviour
{
    [Header("Biome Distribution")]
    [Note("Seed 0 uses random entropy from system clock.", ButtonColor = "#3498db")]
    public int worldSeed = 42;

    [Note("Designer Scratchpad: Remember to test performance on low-end mobile.", AllowEdit = true, ButtonColor = "#e67e22", BackgroundColor = "#2c3e5066")]
    public float waterLevelHeight = 12.5f;

    [Header("Generation Biomes")]
    [Note("Check terrain generation seed weights", "#10B981", ApplyToElements = true)]
    public List<string> activeBiomeNames = new List<string> { "Temperate Forest", "Volcanic Ridge", "Arctic Tundra" };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[InfoBox]` | Alternative | Use `[InfoBox]` for permanent visible callouts; use `[Note]` for compact toggleable notes. |
| `[BoxGroup]` | Supported | Nests cleanly within groups and tabs. |
| `[DetailedInfoBox]` | Alternative | Use `[DetailedInfoBox]` for full markdown documentation sections. |
| Collections (`List<T>`, `T[]`) | Supported | Attaches to container by default; opt-in element cascading via `ApplyToElements = true`. |

