# [HierarchyMonospaceCodeText]

> Displays the hierarchy label in a retro monospace terminal style within a rounded background box.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyMonospaceCodeText]` formats the GameObject's hierarchy row to resemble a retro developer terminal command. It encases the name inside a dark command box (`BackgroundColor = "#1A1E24"`), adds an optional terminal prompt prefix (`Prefix = "$ "`), renders code in phosphorescent green/cyan (`CodeColor = "#00FFAA"`), and outlines the pill with a subtle border (`BorderColor = "#2C3E50"`).

**The Problem:**
Backend developer systems, network managers, analytics dispatchers, or debug test harnesses often look out of place when decorated like game art assets. Standard Unity hierarchy labels don't distinguish low-level code infrastructure from in-game visual props.

**The Solution:**
Decorating developer-centric systems with `[HierarchyMonospaceCodeText]`:
- **Terminal Shell Aesthetics:** Transforms the label into a code console badge with monospace font styling.
- **Configurable Prompt Prefix:** Prepend standard shell prompts like `"$ "`, `"> "`, or `"root# "` directly in front of the name.
- **Embedded Container Box:** Renders an elegant background container with rounded edges and an optional border outline (`ShowBorder = true`).
- **Developer Clarity:** Signals to artists and level designers that the GameObject is a critical system script rather than an interactive game entity.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyMonospaceCodeText(CodeColor = "#00FFAA", Prefix = "$ ", ShowBorder = true)]
public class NetworkSocketDispatcher : MonoBehaviour
{
    public int port = 7777;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class` \| `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyMonospaceCodeTextRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyMonospaceCodeTextAttribute()
```

- Standard parameterless constructor. Colors, borders, and prompt prefixes are set via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `CodeColor` | `string` | `"#00FFAA"` | Hex color string for the monospace terminal text. |
| `BackgroundColor` | `string` | `"#1A1E24"` | Hex color string for the background container pill box. |
| `Prefix` | `string` | `"$ "` | Terminal command prompt prefix prepended to the name. |
| `ShowBorder` | `bool` | `true` | Whether to draw an outline border around the background box. |
| `BorderColor` | `string` | `"#2C3E50"` | Hex color string for the outline border. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether monospace terminal styling remains active during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row decorations. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyMonospaceCodeText(
    CodeColor = "#38BDF8", 
    BackgroundColor = "#0F172A", 
    Prefix = "> run ", 
    ShowBorder = true, 
    BorderColor = "#334155")]
public class AnalyticsPipelineWorker : MonoBehaviour
{
    [Header("Telemetry Backend")]
    public string endpointUrl = "https://telemetry.studio.com/v1";
    public int bufferFlushThreshold = 50;
    public bool isBufferingEvents = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyTooltip]`** | High | Display connection ports, API endpoints, or commit hashes in rich tooltips on hover. |
| **`[HierarchyActiveToggle]`** | High | Pair with active state toggles to easily turn background services on/off. |
| **`[HierarchyLock]`** | High | Lock critical infrastructure GameObjects against accidental movement in the SceneView. |
| **`[HierarchyTextColor]`** | Incompatible | Do not stack with standard text color attributes as monospace styling replaces the label container. |
