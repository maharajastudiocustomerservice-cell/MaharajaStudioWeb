# [ComponentFooter]

> Renders a sleek footer bar docked at the bottom of the component card with support for copyright/author metadata, version badges, and external documentation hyperlinks.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentFooter]` caps the bottom of component cards with professional studio metadata. Injected into `ComponentSlot.AfterContent` (`Order = 60`), it renders a structured bottom bar separated from inspector controls by an optional divider rule (`ShowDivider`). It displays informational footer text (`Text`), an optional rounded version pill (`Version`, `BadgeColor`, `BadgeTextColor`), and an optional clickable URL button (`Url`, `UrlLabel`) that launches web documentation or repository wikis directly in the system browser via `Application.OpenURL`.

**The Problem:**
Complex gameplay frameworks, third-party libraries, and internal studio tooling need version tracking and quick documentation links. Standard Unity inspectors offer no structured place to show author credits, engine versions, or docs links without cluttering serialized variable rows.

**The Solution:**
Decorating systems with `[ComponentFooter]`:
- **Integrated Version Tagging:** Displays version identifiers (e.g. `v2.4.1`) in clean badges that maintain team alignment.
- **One-Click Documentation Access:** Embeds direct URL buttons (`UrlLabel = "Wiki"`) to avoid developers searching through disconnected browser bookmarks.
- **Polished Card Framing:** Pairs with `[ComponentHeader]` to form a complete, cohesive card with rounded bottom corners (`BorderRadius`).
- **Flexible Typography & Theming:** Customize background color, divider hue, font size, and text styles.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentFooter("Developed by Maharaja Studio Core Systems", Version = "v1.4.2", Url = "https://wiki.example.com", UrlLabel = "Documentation")]
public class InventoryDatabaseManager : MonoBehaviour
{
    public int maxItemCapacity = 150;
    public bool enableCloudSaveSync = true;
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
| **Component Slot** | `AfterContent` (`Order = 60`) |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentFooterAttribute(string text)
```

- `text`: Informational string displayed in the footer bar (e.g. copyright, author, or status message).

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Text` | `string` | *(Constructor)* | Primary footer text label. |
| `Version` | `string` | `""` | Version string displayed inside a stylized pill badge (e.g. `"v2.1.0"`). |
| `BadgeColor` | `string` | `"#2A2A4E"` | Hex background color for the version badge pill. |
| `BadgeTextColor` | `string` | `"#AAAACC"` | Hex text color for the version badge pill. |
| `Url` | `string` | `""` | Web link URL. When populated, renders a clickable hyperlink button. |
| `UrlLabel` | `string` | `"Docs"` | Button display label for the external link. |
| `BackgroundColor` | `string` | `"#1A1A2E"` | Hex background color of the footer bar. |
| `TextColor` | `string` | `"#666688"` | Hex color string for footer text. |
| `FontSize` | `int` | `10` | Font size in points for footer text. |
| `FontStyle` | `FontStyle` | `FontStyle.Italic` | Font styling for footer text (`Normal`, `Bold`, `Italic`). |
| `ShowDivider` | `bool` | `true` | When true, renders a horizontal separator line above the footer bar. |
| `DividerColor` | `string` | `"#3A3A5E"` | Hex color string for the top divider line. |
| `BorderRadius` | `float` | `6f` | Bottom-left and bottom-right corner rounding in pixels. |
| `Padding` | `float` | `8f` | Internal padding in pixels surrounding footer elements. |
| `MarginTop` | `float` | `4f` | Vertical margin spacing above the footer bar. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#4338CA", Width = 1.5f, Radius = 8f)]
[ComponentHeader("QUEST STATE PIPELINE", Subtitle = "Branching Dialogue & Objective Graph", BackgroundColor = "#1E1B4B", TitleColor = "#E0E7FF")]
[ComponentFooter("Studio RPG Toolchain © 2026", Version = "v3.0.4", Url = "https://docs.studio.internal/quests", UrlLabel = "Open Manual", BackgroundColor = "#18153B", TextColor = "#818CF8", BadgeColor = "#312E81", BadgeTextColor = "#C7D2FE", BorderRadius = 8f)]
public class QuestStatePipeline : MonoBehaviour
{
    [Header("Quest Configuration")]
    public string activeQuestId = "Q_MAIN_TEMPLE_INFILTRATION";
    public int currentStageIndex = 3;
    public bool autoAdvanceOnObjectiveMet = true;

    [Header("Debug Flags")]
    public bool verboseGraphLogging = false;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeader]`** | High | Combines with `[ComponentHeader]` to create a complete inspector card frame with matching header and footer colors. |
| **`[ComponentBorder]`** | High | Matches corner radius with `BorderRadius` to produce a unified, enclosed card container. |
| **`[ComponentHelpBox]`** | High | Help boxes positioned at `ComponentPosition.Bottom` stack cleanly before the footer. |
