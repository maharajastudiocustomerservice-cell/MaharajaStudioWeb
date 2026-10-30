# [LabelLayout]

> Advanced label and input control layout modifier providing granular control over label positioning, adaptive inline fitting, responsive auto-stacking breakpoints, and input constraints.

---

## 1. Overview & Value Proposition

**What it does:**
`[LabelLayout]` dynamically alters how field labels and their corresponding input fields are positioned, sized, and rendered in the Unity Inspector. It supports adaptive inline auto-sizing (removing awkward blank gaps), responsive auto-stacking (switching from horizontal to vertical layout below a custom width breakpoint), permanent vertical stacking, and explicit label sizing constraints.

**The Problem:**
Standard Unity Inspectors use rigid, fixed-width columns for property labels. In narrow inspector panels or multi-column layouts (`[HorizontalGroup]`, split panes, grids), this rigid width causes long labels to be brutally truncated while input fields collapse into unusable slivers. Conversely, short labels ("X", "HP", "ID") leave massive empty gaps before their input boxes.

**The Solution:**
Applying `[LabelLayout]` gives developers complete control over field ergonomics:
- **Adaptive Inline Auto-Fitting (`AdaptiveInline`):** Dynamically measures label text length and pulls the input field directly alongside it with a tight, configurable gap.
- **Responsive Auto-Stacking (`ResponsiveStack`):** Displays fields inline on wide screens, but seamlessly transitions to vertical stacking (label on top, full-width input below) whenever inspector column width drops below a configurable pixel breakpoint.
- **Always Stacked Layout (`AlwaysStacked`):** Perfect for multi-column weapon stats or telemetry tables where labels sit cleanly above full-width inputs.
- **Auto-Hide on Compact Views (`AutoHideLabel`):** Automatically hides the text label in super-narrow slots, giving 100% of the horizontal space to the input field.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CombatUnit : MonoBehaviour
{
    // Auto-sizes label to fit text without wasting horizontal space
    [LabelLayout(LabelLayoutMode.AdaptiveInline)]
    public float hp = 100f;

    // Automatically stacks vertically if column width drops below 200px
    [LabelLayout(LabelLayoutMode.ResponsiveStack, breakpoint: 200f)]
    public Vector3 spawnAnchor;
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
| **Inherited** | Yes (`Inherited = true`) |
| **UI Toolkit Compatible** | Yes (Hardware-accelerated flexbox) |
| **Performance Tier** | Tier 1 (Zero runtime cost, Editor-only layout computation) |

---

## 4. Constructors & Signatures

```csharp
// 1. Specify layout mode
public LabelLayoutAttribute(LabelLayoutMode mode = LabelLayoutMode.AdaptiveInline);

// 2. Specify layout mode and responsive width breakpoint
public LabelLayoutAttribute(LabelLayoutMode mode, float breakpoint);

// 3. Specify explicit fixed label width and optional mode
public LabelLayoutAttribute(float labelWidth, LabelLayoutMode mode = LabelLayoutMode.AdaptiveInline);
```

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Mode` | `LabelLayoutMode` | `AdaptiveInline` | Layout strategy (`Default`, `AdaptiveInline`, `ResponsiveStack`, `AlwaysStacked`, `StandardUnity`). |
| `Breakpoint` | `float` | `0f` | Width in pixels below which the field switches to vertical stacked layout. `0` inherits global setting (160px). |
| `LabelWidth` | `float` | `0f` | Explicit label width in pixels. When `0`, auto-fits to text content length. |
| `MinLabelWidth` | `float` | `0f` | Minimum allowable label width in pixels before ellipsis truncation occurs. |
| `MaxLabelWidth` | `float` | `0f` | Maximum allowable label width in pixels to prevent long text from crowding inputs. |
| `WidthPercent` | `float` | `0f` | Percentage width of the container row allocated to the label (e.g., `35f` for 35%). |
| `Gap` | `float` | `-1f` | Spacing in pixels between the label and the input field. `-1` inherits global layout setting (4px). |
| `AutoHideLabel` | `bool` | `false` | When true, hides the label entirely if column width drops below `AutoHideMinWidth`. |
| `AutoHideMinWidth` | `float` | `0f` | Pixel threshold below which the label auto-hides (default: 140px). |
| `Ellipsis` | `bool` | `true` | Whether the label displays an ellipsis (`...`) when horizontal space is constrained. |
| `InputMinWidth` | `float` | `20f` | Guaranteed minimum width in pixels for the input control to prevent squishing. |
| `InputAlignment` | `UiAlignment` | `Stretch` | Flex alignment of the input control within its allocated row space. |

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class MechWeaponLoadout : ModularMonoBehaviour
{
    [BoxGroup("Primary Rail Cannon", Box = true)]
    [HorizontalGroup("Primary Rail Cannon/Specs")]
    [LabelLayout(LabelLayoutMode.AlwaysStacked)]
    public float muzzleVelocity = 1800f;

    [HorizontalGroup("Primary Rail Cannon/Specs")]
    [LabelLayout(LabelLayoutMode.AlwaysStacked)]
    public int ammoCapacity = 45;

    [HorizontalGroup("Primary Rail Cannon/Specs")]
    [LabelLayout(LabelLayoutMode.AlwaysStacked)]
    public float heatPerShot = 12.5f;

    [BoxGroup("Responsive Energy Distribution", Box = true)]
    [InfoBox("Resize your Inspector window to watch the responsive layout adapt between inline and stacked rows!")]
    [LabelLayout(LabelLayoutMode.ResponsiveStack, breakpoint: 220f, Gap = 8f)]
    public AnimationCurve powerSpikeCurve = AnimationCurve.EaseInOut(0, 0, 1, 1);

    [LabelLayout(LabelLayoutMode.AdaptiveInline, MaxLabelWidth = 140f, Ellipsis = true)]
    public string weaponTelemetryFeedSignature = "RAIL_CORE_MK4_ALPHA_SUBSYSTEM";
}
```

---

## 7. Stacking & Compatibility Matrix

- **Layout Group Synergy:** Exceptionally powerful when paired with `[HorizontalGroup]`, `[BoxGroup]`, and `[CardGroup]` to build responsive multi-column layouts that don't clip on small screens.
- **Conditional Visibility:** Fully compatible with `[ShowIf]`, `[HideIf]`, and `[EnableIf]`. Dynamic state transitions smoothly preserve label layout styles.
- **Validation Compatibility:** Pairs seamlessly with `[ValidateRange]`, `[Required]`, and `[NotNull]`. Validation badges and alerts respect custom gap and breakpoint settings.
- **Collection Elements:** Functions on serialized elements inside `[AdvancedList]` and custom serializable classes.
