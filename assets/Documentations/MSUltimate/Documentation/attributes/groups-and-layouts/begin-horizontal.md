# [BeginHorizontal]

> Starts an imperative horizontal layout row placing subsequent inspector fields, properties, or buttons side-by-side until closed by [EndHorizontal].

---

## 1. Overview & Value Proposition

**What it does:**
Opens an imperative horizontal layout scope in the Inspector. All subsequent serialized fields, properties, or methods decorated up until an `[EndHorizontal]` attribute are laid out horizontally in a single row or flexbox grid with customizable spacing, borders, titles, and alignments.

**The Problem:**
By default, Unity stacks every single serialized field vertically, consuming massive amounts of vertical screen space. For tight groupings of related controls—such as Min/Max bounds, paired multipliers, or a row of utility buttons—vertical stacking feels clunky and requires continuous scrolling.

**The Solution:**
Add `[BeginHorizontal]` before the first field and `[EndHorizontal]` after the last:
- **Side-by-Side Ergonomics:** Renders multiple controls in a compact horizontal row.
- **Flexbox-Style Layout:** Full control over `Gap`, `FlexGrow`, `AlignItems`, and `JustifyContent`.
- **Responsive Label Modes:** Adjust `LayoutMode` (`AdaptiveInline`, `ResponsiveStack`, `AlwaysStacked`) and `LabelWidth` to fit narrow inspector windows.
- **Card Framing & Headers:** Wrap the row in a border box (`Box = true`), add header titles (`Title`), or make it collapsible (`Collapsible = true`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class MovementSettings : MonoBehaviour
{
    [BeginHorizontal(Gap = 8f)]
    public float walkSpeed = 4.5f;

    [EndHorizontal]
    public float runSpeed = 9.0f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property | Method` |
| **Supported Types** | Any member placed within horizontal layout scopes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public BeginHorizontalAttribute()
```

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Gap` | `float` | `5f` | Horizontal spacing between child elements in the row. |
| `Box` | `bool` | `false` | Draws a framed background card around the entire horizontal group. |
| `BackgroundColor` | `string` | `null` | Hex fill color when `Box` is enabled. |
| `Padding` | `float` | `0f` | Internal padding around the row contents. |
| `FlexGrow` | `bool` | `false` | Stretches items to distribute remaining horizontal width. |
| `NoWrap` | `bool` | `false` | Prevents items from wrapping if row width is exceeded. |
| `AlignItems` | `FlexAlign`| `FlexAlign.FlexStart` | Cross-axis alignment (`Auto`, `FlexStart`, `Center`, `FlexEnd`, `Stretch`). |
| `JustifyContent` | `FlexJustify`| `FlexJustify.FlexStart`| Main-axis alignment (`FlexStart`, `Center`, `FlexEnd`, `SpaceBetween`, etc.). |
| `LabelWidth` | `float` | `0f` | Explicit width for labels within the group (`0` = default). |
| `HideLabel` | `bool` | `false` | Hides field labels to render full-width controls. |
| `Title` | `string` | `null` | Optional header title rendered above the horizontal group. |
| `TitleColor` | `string` | `null` | Hex text color for the title header. |
| `TitleBold` | `bool` | `true` | Renders title header text in bold font. |
| `Collapsible` | `bool` | `false` | Enables a toggle button to collapse/expand the entire row. |
| `BorderColor` | `string` | `null` | Hex color code for the group outline border. |
| `BorderRadius` | `float` | `0f` | Corner radius for the group card container. |
| `Order` | `int` | `0` | Drawing order priority in the inspector pipeline. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class AudioPlaybackStation : MonoBehaviour
{
    [Header("Volume & Pitch Controls")]
    [BeginHorizontal(Box = true, Gap = 10f, Padding = 6f, BorderRadius = 4f)]
    [Range(0f, 1f)]
    public float masterVolume = 0.8f;

    [Range(0.5f, 2f)]
    [EndHorizontal]
    public float playbackPitch = 1.0f;

    [Header("Quick Transport Controls (Row of Buttons)")]
    [BeginHorizontal(JustifyContent = FlexJustify.Center, Gap = 6f)]
    [Button("◀ Rewind")]
    public void Rewind() => Debug.Log("Rewind");

    [Button("▶ Play")]
    public void Play() => Debug.Log("Play");

    [Button("❚❚ Pause")]
    [EndHorizontal]
    public void Pause() => Debug.Log("Pause");
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[EndHorizontal]` | Required | Must pair with `[EndHorizontal]` to close the active row scope. |
| `[Button]` | Recommended | Essential for creating sleek horizontal toolbars and transport controls. |
| `[BoxGroup]` | Supported | Can be nested cleanly within outer box groups and foldouts. |
| `[ShowIf]` | Supported | Hiding a member inside the group dynamically contracts the row width. |
