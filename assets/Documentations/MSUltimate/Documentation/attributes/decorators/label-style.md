# [LabelStyle]

> Comprehensive visual styling decorator for property labels, providing typography, badge pills, icons, and hover effects.

---

## 1. Overview & Value Proposition

**What it does:**
Transforms standard grey property labels with custom colors, typography (bold, italic, font size), badges, pill backgrounds, and icons.

**The Problem:**
In standard Unity, all field labels look identical. You cannot emphasize primary stats, highlight deprecated fields, color-code system tiers, or attach identifying icons without building dedicated custom editor drawers for each MonoBehaviour.

**The Solution:**
Add `[LabelStyle]` to any field:
- **Typography & Font Controls:** Adjust font size, bold weight, italics, letter spacing, uppercase, and text colors.
- **Badge & Pill Chips:** Render rounded pill or rectangular badge containers behind labels with custom backgrounds and borders.
- **Icon Integration:** Place built-in Unity editor icons or custom sprites directly before or after label text.
- **Collection Cascading:** Automatically styles elements inside lists, arrays, and serialized dictionaries.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class PlayerAttributes : MonoBehaviour
{
    [LabelStyle(colorHex: "#e74c3c", bold: true)]
    public float maxHealth = 100f;

    [LabelStyle("d_Favorite", "#f39c12")]
    public int starRank = 5;
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

---

## 4. Constructors & Parameters

```csharp
public LabelStyleAttribute()
public LabelStyleAttribute(string colorHex)
public LabelStyleAttribute(int fontSize)
public LabelStyleAttribute(string colorHex, int fontSize)
public LabelStyleAttribute(string colorHex, bool bold, bool italic = false)
public LabelStyleAttribute(string colorHex, int fontSize, bool bold, bool italic = false)
public LabelStyleAttribute(string icon, string colorHex, IconAlignment iconAlignment = IconAlignment.Left)
public LabelStyleAttribute(string icon, string colorHex, bool bold, IconAlignment iconAlignment = IconAlignment.Left)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `colorHex` | `string` | `null` | Hex text color (e.g. `"#FF5555"`, `"cyan"`). |
| `fontSize` | `int` | `0` | Font size in pixels (`0` uses default). |
| `bold` | `bool` | `false` | Renders label in bold font weight. |
| `italic` | `bool` | `false` | Renders label in italic font style. |
| `icon` | `string` | `null` | Built-in Unity icon name or asset path. |
| `iconAlignment` | `IconAlignment` | `IconAlignment.Left` | Alignment of the icon relative to the label (`Left`, `Right`). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ColorHex` / `TextColor` | `string` | `null` | Hex text color string. |
| `FontSize` | `int` | `0` | Font size in pixels. |
| `Bold` | `bool` | `false` | Bold font weight toggle. |
| `Italic` | `bool` | `false` | Italic font style toggle. |
| `Alignment` | `UiAlignment` | `UiAlignment.Left` | Text alignment within the label column. |
| `Prefix` | `string` | `null` | Text prepended before the label (e.g. `"[CFG] "`). |
| `Suffix` | `string` | `null` | Text appended after the label (e.g. `" (req)"`). |
| `Tooltip` | `string` | `null` | Hover tooltip text override. |
| `BackgroundColor` | `string` | `null` | Hex background color behind the label (badge style). |
| `BorderColor` | `string` | `null` | Hex border outline color. |
| `BorderWidth` | `float` | `0f` | Border outline thickness in pixels. |
| `BorderRadius` | `float` | `0f` | Rounded corner radius in pixels. |
| `Padding` | `float` | `0f` | Internal padding within the badge. |
| `Icon` | `string` | `null` | Icon identifier or sprite path. |
| `IconColor` | `string` | `null` | Hex color tint for the icon image. |
| `IconSize` | `float` | `0f` | Explicit icon dimension in pixels (`0` scales with font). |
| `HoverColor` | `string` | `null` | Text color on mouse hover. |
| `HoverBackgroundColor` | `string` | `null` | Background color on mouse hover. |
| `Order` | `int` | `0` | Execution priority relative to other field modifier attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class NetworkCharacterConfig : MonoBehaviour
{
    [LabelStyle(colorHex: "#e74c3c", bold: true, Prefix = "[CRITICAL] ")]
    public float respawnTimer = 15f;

    [LabelStyle(colorHex: "#3498db", BackgroundColor = "#1a365d", BorderRadius = 10f, Padding = 4f)]
    public float networkSyncRate = 60f;

    [LabelStyle("d_Settings", "#2ecc71", bold: true, Tooltip = "Core AI Behavior Tree selector")]
    public TextAsset behaviorTreeAsset;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[SuffixLabel]` | Supported | Pairs cleanly with suffix units docked on the right. |
| `[BoxGroup]` | Supported | Renders inside group cards without breaking grid layouts. |
| `[ReadOnly]` | Supported | Preserves custom typography and badge styles on read-only fields. |
