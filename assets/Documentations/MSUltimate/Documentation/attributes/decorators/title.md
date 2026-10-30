# [Title]

> Displays a prominent section title with optional subtitle, typography styling, background colors, and underline separators.

---

## 1. Overview & Value Proposition

**What it does:**
Renders a bold, stylish title banner with an optional subtitle directly above a field, property, or button to introduce major inspector sections.

**The Problem:**
Unity's default `[Header]` attribute only provides small text with no subtitle support, no background cards, and no alignment options. Breaking complex components into clear, magazine-quality visual modules is impossible with built-in attributes alone.

**The Solution:**
Add `[Title]` to any field, property, or method:
- **Two-Tier Headline:** Supports primary `Title` and secondary descriptive `Subtitle` in a single attribute.
- **Visual Underline Separator:** Optional dividing underline for clean section separation.
- **Card & Banner Modes:** Customize background colors, borders, corner radius, and padding.
- **Flexible Positioning:** Place above methods, fields, or set `AboveGroup = true` to render outside parent group containers.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class LevelManager : MonoBehaviour
{
    [Title("Dungeon Generation", "Controls procedural room placement and seed rules")]
    public int dungeonSeed = 1337;

    [Title("Enemy Spawning", Subtitle = "Wave timing and encounter density", TextColor = "#e67e22")]
    public float waveInterval = 30f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property | Method` |
| **Supported Types** | Any serializable field, property, or method |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public TitleAttribute(string title, string subtitle = null)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `title` | `string` | *(Required)* | Primary section heading text string. |
| `subtitle` | `string` | `null` | Secondary descriptive text displayed beneath the title. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Title` | `string` | *(Required)* | Primary heading text. |
| `Subtitle` | `string` | `null` | Secondary subtitle text. |
| `Bold` | `bool` | `true` | Renders title in bold font weight. |
| `Alignment` | `UiAlignment` | `UiAlignment.Left` | Title alignment (`Left`, `Center`, `Right`). |
| `FontSize` | `int` | `14` | Title font size in pixels. |
| `TextColor` / `TitleColor` | `string` | `null` | Hex text color string. |
| `BackgroundColor` | `string` | `null` | Banner background color hex. |
| `BorderColor` | `string` | `null` | Border outline color hex. |
| `BorderWidth` | `float` | `0f` | Border line thickness in pixels. |
| `BorderRadius` | `float` | `3f` | Corner rounding radius in pixels. |
| `ShowSeparator` | `bool` | `true` | Renders underline separator beneath title. |
| `FullWidth` | `bool` | `false` | Stretches banner edge-to-edge across container. |
| `AboveGroup` | `bool` | `false` | Renders outside and above parent layout groups. |
| `Order` | `int` | `0` | Execution priority relative to other decorator attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class WorldAtmosphereController : MonoBehaviour
{
    [Title("Sky & Celestial Lighting", "Configures ambient sun intensity and horizon fog scattering", 
           FontSize = 16, TextColor = "#1abc9c", BackgroundColor = "#16a08522", ShowSeparator = true)]
    public Color sunLightColor = Color.white;
    public float fogDensity = 0.02f;

    [Title("Weather Simulation Matrix", "Dynamic rain and thunder probabilities", TextColor = "#3498db")]
    [Range(0f, 1f)]
    public float rainIntensity = 0.5f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Header]` | Alternative | Use `[Title]` for major section headlines with subtitles; use `[Header]` for compact sub-headers. |
| `[BoxGroup]` | Supported | Set `AboveGroup = true` to headline the group from outside the box border. |
| `[HideScript]` | Recommended | Pairs well at the top of a class to replace the default Script row with a branded title. |
