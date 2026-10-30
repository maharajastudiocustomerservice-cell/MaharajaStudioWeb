# [AnimatedMarquee]

> Renders string fields as a continuous horizontally scrolling marquee ticker display with customizable scroll speeds, text colors, and styling.

---

## 1. Overview & Value Proposition

**What it does:**
Transforms standard string properties into a retro digital marquee ticker that continuously scrolls text horizontally across the Inspector row. Features customizable scrolling speeds (`ScrollSpeed`), high-contrast text and background colors, and internal padding.

**The Problem:**
Long string descriptions, news tickers, build metadata, or license notices get clipped or take up multiple vertical lines in standard single-line string fields.

**The Solution:**
Add `[AnimatedMarquee]` to any string field:
- **Continuous Horizontal Ticker:** Long text scrolls seamlessly without truncating or stretching inspector width.
- **Retro Digital Aesthetic:** Mimics LED billboards, stock tickers, or cyber terminal news flashes.
- **Full Speed Control:** Configure scroll rate in pixels per second.
- **Theming Flexibility:** Set custom text and background colors via hex strings.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class GameNewsTicker : MonoBehaviour
{
    [AnimatedMarquee(ScrollSpeed = 60f, TextColor = "#00FF66", BackgroundColor = "#111111")]
    public string announcementText = "SERVER UPDATE: Patch 1.4 deployed. Double XP weekend is now active across all matchmaking regions!";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `string` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public AnimatedMarqueeAttribute()
```

*Attribute initializes with standard green-on-black digital ticker styling; customize properties via object initializers.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ScrollSpeed` | `float` | `50f` | Horizontal scroll speed in pixels per second. |
| `TextColor` | `string` | `"#00FF00"` | Hex color string for the scrolling text. |
| `BackgroundColor` | `string` | `"#000000"` | Hex color string for the marquee container background. |
| `Padding` | `float` | `2f` | Internal padding in pixels around the scrolling text. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class BuildInfoDisplay : MonoBehaviour
{
    [Header("Continuous Build Telemetry")]
    [AnimatedMarquee(
        ScrollSpeed = 75f, 
        TextColor = "#f39c12", 
        BackgroundColor = "#1c2833", 
        Padding = 4f
    )]
    public string buildNotes = "BUILD 2026.10.12 - Unity 6 URP - Git: main@8f4d92 - Debug Mode Active";
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Marquee container docks neatly inside layout cards. |
| Category | PrimaryDrawer | Acts as an animated primary field drawer for string properties. |
| ReadOnly Integration | Supported | Ideal for read-only status and telemetry readouts. |
