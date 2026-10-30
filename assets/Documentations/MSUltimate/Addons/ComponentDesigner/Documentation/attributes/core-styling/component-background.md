# [ComponentBackground]

> Encloses all component inspector controls inside a solid, rounded card container with custom background coloring and padding.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentBackground]` provides the foundational canvas layer for custom component cards. Injecting directly into `ComponentSlot.ContentWrapper`, it encloses all serialized fields within an elevated container styled with a solid background color (`Color`), smooth rounded corners (`BorderRadius`, defaulting to 6px), internal padding (`Padding`, defaulting to 8px), and vertical margins. It replaces Unity's default transparent background with clean dark-mode panels, paper parchment sheets, or tinted category containers.

**The Problem:**
Standard Unity component inspectors possess no unified background container; fields float across the default editor window gray background. Without container styling, multiple components stacked on a GameObject bleed together without clear visual boundaries.

**The Solution:**
Decorating components with `[ComponentBackground]`:
- **Unified Card Enclosure:** Groups all fields into a distinct, cohesive card container.
- **ContentWrapper Slot Integration:** Acts as the primary content parent, neatly holding all child fields, groups, and overlays.
- **Custom Color Branding:** Apply dark charcoal slate (`#1E293B`), deep navy (`#0F172A`), rich parchment (`#FDF6E2`), or custom department hues.
- **Configurable Ergonomics:** Easily tune inner padding and corner rounding to create compact chips or spacious dashboard cards.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBackground("#1E293B", BorderRadius = 8f, Padding = 10f)]
public class SoundEffectEmitter : MonoBehaviour
{
    public AudioClip mainAudioClip;
    public float volume = 0.8f;
    public bool loop = false;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ComponentDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Component Slot** | `ContentWrapper` (`Order = 40`) |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentBackgroundAttribute(string color)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `color` | `string` | *Required* | Hex color string for the component background (e.g. `"#1E293B"`). |

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color` | `string` | *Set via constructor* | Hex color code applied to the card body. |
| `BorderRadius` | `float` | `6f` | Corner rounding radius in pixels. |
| `Padding` | `float` | `8f` | Internal padding space between the background edge and child fields. |
| `MarginTop` | `float` | `0f` | Top margin spacing outside the card container. |
| `MarginBottom` | `float` | `0f` | Bottom margin spacing outside the card container. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#3B82F6", Width = 1.5f, Radius = 8f)]
[ComponentBackground("#0F172A", BorderRadius = 8f, Padding = 12f, MarginTop = 4f, MarginBottom = 4f)]
public class QuestObjectiveTracker : MonoBehaviour
{
    [Header("Quest Information")]
    public string questTitle = "Retrieve the Sunstone";
    public int currentProgress = 3;
    public int requiredTarget = 5;
    public bool isCompleted = false;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBorder]`** | High | Standard companion; `[ComponentBackground]` provides the fill and `[ComponentBorder]` frames the outer edge. |
| **`[ComponentHeader]`** | High | The background neatly encapsulates all fields immediately beneath the header bar. |
| **`[ComponentWatermark]`** | High | Watermarks and background overlays render directly inside this container. |
| **Layout Attributes** | High | Perfectly hosts all MSUltimate group attributes (`[BoxGroup]`, `[TabGroup]`, `[HorizontalGroup]`). |
