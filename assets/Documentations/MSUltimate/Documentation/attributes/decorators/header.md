# [Header]

> Renders a customizable section header with custom typography, background colors, borders, and separator lines.

---

## 1. Overview & Value Proposition

**What it does:**
Creates visual section headers above inspector fields and buttons with full control over font size, colors, alignments, and dividing lines.

**The Problem:**
Unity's built-in `[Header]` attribute is rigid: it only renders small, unstyled grey text, cannot be centered, cannot have custom colors, doesn't support dividers or background banners, and cannot be placed above buttons or properties.

**The Solution:**
MSUltimate's `[Header]` provides rich styling:
- **Typography & Font Sizing:** Customize font size, bold weight, and text color using clean hex codes.
- **Visual Dividers:** Optional horizontal line separator beneath the header for clean sectioning.
- **Card & Banner Styles:** Set background colors, corner radius, and border colors to turn headers into stylish category banners.
- **Flexible Alignment:** Align text left, center, or right.
- **Target Flexibility:** Works on fields, properties, and method buttons.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CharacterSheet : MonoBehaviour
{
    [Header("Core Attributes", FontSize = 15, TextColor = "#3498db")]
    public int strength = 18;
    public int agility = 14;

    [Header("Magical Resonance", Bold = true, ShowSeparator = true, BackgroundColor = "#2c3e50")]
    public float manaPool = 250f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Method | Property` |
| **Supported Types** | Any serializable field, property, or method |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public HeaderAttribute(string text)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `text` | `string` | *(Required)* | Header title text to display. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Text` | `string` | *(Required)* | Header title text string. |
| `FontSize` | `int` | `14` | Font size in pixels. |
| `Alignment` | `UiAlignment` | `UiAlignment.Left` | Alignment of text within header row (`Left`, `Center`, `Right`). |
| `Bold` | `bool` | `true` | Renders title text in bold font weight. |
| `TextColor` | `string` | `null` | Hex text color (e.g. `"#E74C3C"`). |
| `BackgroundColor` | `string` | `null` | Hex background banner color behind header. |
| `BorderColor` | `string` | `null` | Hex border outline color. |
| `BorderWidth` | `float` | `0f` | Border line thickness in pixels. |
| `BorderRadius` | `float` | `3f` | Corner rounding radius in pixels. |
| `ShowSeparator` | `bool` | `true` | Renders a subtle horizontal divider line under the text. |
| `Padding` | `float` | `5f` | Inner padding in pixels. |
| `MarginTop` | `float` | `4f` | Top margin spacing in pixels. |
| `MarginBottom` | `float` | `4f` | Bottom margin spacing in pixels. |
| `Width` | `float` | `0f` | Fixed width in pixels (`0f` auto-fits container). |
| `Wrap` / `WordWrap` | `bool` | `true` | Enables text word wrapping for longer descriptions. |
| `FullWidth` | `bool` | `false` | Stretches banner across entire inspector width. |
| `AboveGroup` | `bool` | `false` | Renders the header outside and above parent layout groups. |
| `Order` | `int` | `0` | Execution priority relative to other decorator attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class GameAudioDirector : MonoBehaviour
{
    [Header("Atmospheric Audio", FontSize = 16, TextColor = "#1abc9c", Alignment = UiAlignment.Center, BackgroundColor = "#16a08522", ShowSeparator = true)]
    public AudioClip windAmbience;
    public AudioClip rainfallLoop;

    [Header("Dynamic Mixing Matrix", FontSize = 14, Bold = true, MarginTop = 12f)]
    [Range(0f, 1f)] public float masterVolume = 1f;
    [Range(0f, 1f)] public float ambientBus = 0.8f;

    [Header("Live Operations", TextColor = "#e67e22")]
    [Button("Stop All Sounds")]
    public void StopAll()
    {
        // Stop audio logic
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Title]` | Complementary | Use `[Title]` for top-level component headlines, and `[Header]` for section separators. |
| `[BoxGroup]` | Supported | Set `AboveGroup = true` to render header before group border. |
| `[ShowIf]` | Supported | Header shows or hides dynamically alongside target fields. |
| `[Button]` | Supported | Fully supported directly above method buttons. |
