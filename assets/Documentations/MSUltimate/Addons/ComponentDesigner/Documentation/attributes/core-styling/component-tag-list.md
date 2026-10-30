# [ComponentTagList]

> Displays a horizontal row of pill-shaped categorical metadata tags above or below the component body with custom alignment and color theming.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentTagList]` categorizes components by displaying a clean row of pill-shaped metadata tags (e.g. `["COMBAT", "BOSS", "SERVER-ONLY"]`). Injected into `ComponentSlot.BeforeBody` (`Position = ComponentPosition.Top`) or `ComponentSlot.AfterBody` (`Position = ComponentPosition.Bottom`), it formats string tags with rounded container geometry (`BackgroundColor`, `TextColor`), horizontal alignment options (`Alignment` $\to$ `Left`, `Center`, `Right`), and custom margins. Because `AllowMultiple = true`, developers can position distinct tag groups at both the top and bottom of the component card.

**The Problem:**
Modern game projects classify components across multiple architectural axes (gameplay layer, network authority, asset tier, performance cost). Simple script names cannot express these multifaceted categorizations without creating confusion.

**The Solution:**
Decorating components with `[ComponentTagList]`:
- **Categorical Tag Rows:** Display any number of string tags in clean, compact pill badges using `params string[]`.
- **Top or Bottom Docking:** Position tags above fields (`ComponentPosition.Top`) or below the body (`ComponentPosition.Bottom`).
- **Flexible Alignment:** Align tags to the left, center, or right using `UiAlignment`.
- **Customizable Palettes:** Customize background and text color to match specific studio color schemes.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentTagList("COMBAT", "MELEE", "BOSS-ONLY", BackgroundColor = "#7C3AED", TextColor = "#FFFFFF")]
public class BossMeleeAttackSequencer : MonoBehaviour
{
    public float comboSlashDamage = 85f;
    public float poiseDamageImpact = 45f;
    public bool isUnblockableHeavyAttack = true;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ComponentDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Component Slot** | `BeforeBody` (if `Position = Top`) or `AfterBody` (if `Position = Bottom`) |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentTagListAttribute(params string[] tags)
```

- `tags`: Variable array of tag strings to display as pill badges (e.g. `"PHYSICS"`, `"CLIENT"`).

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Tags` | `string[]` | *(Constructor)* | Array of string tags displayed in the row. |
| `Position` | `ComponentPosition` | `ComponentPosition.Top` | Placement docking (`ComponentPosition.Top` or `ComponentPosition.Bottom`). |
| `Alignment` | `UiAlignment` | `UiAlignment.Left` | Horizontal alignment (`Left`, `Center`, `Right`). |
| `BackgroundColor` | `string` | `"#3A3A4A"` | Hex background color string for the pill badges. |
| `TextColor` | `string` | `"#DDDDDD"` | Hex text color string for the tag labels. |
| `MarginTop` | `float` | `4f` | Vertical margin spacing in pixels above the tag row. |
| `MarginBottom` | `float` | `4f` | Vertical margin spacing in pixels below the tag row. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#0284C7", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#081A26", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("AUTHORITATIVE REPLICATION BRIDGE", Subtitle = "Client-Server Snapshot Interpolation", BackgroundColor = "#0C2E42", TitleColor = "#E0F2FE")]
[ComponentTagList("SERVER-AUTHORITATIVE", "SNAPSHOT-SYNC", "DELTA-COMPRESSED", Position = ComponentPosition.Top, Alignment = UiAlignment.Left, BackgroundColor = "#0369A1", TextColor = "#F0F9FF")]
public class AuthoritativeReplicationBridge : MonoBehaviour
{
    [Header("Sync Rates")]
    public float snapshotTickRateHz = 60f;
    public int maxHistorySnapshotBuffers = 64;
    public bool enableJitterCompression = true;

    [Header("Connection Bandwidth")]
    public float maxBandwidthLimitKbps = 250f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeader]`** | High | Docked at `Top`, tags sit directly underneath the header bar as subtitle chips. |
| **`[ComponentFooter]`** | High | Docked at `Bottom`, tags complement footer credits. |
| **Multiple Instances** | High | Place architectural tags at `Top` and runtime mode tags at `Bottom`. |
