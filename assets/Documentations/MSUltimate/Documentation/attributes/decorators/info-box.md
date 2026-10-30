# [InfoBox]

> Displays an informative HelpBox banner with icons, severity levels, conditional visibility, and custom card styling.

---

## 1. Overview & Value Proposition

**What it does:**
Renders a prominent callout box (Info, Warning, Error, or custom colored card) directly above or below fields and buttons.

**The Problem:**
Complex components often require critical warnings (e.g. "Do not set below 0" or "Requires NavMesh"). Tooltips only appear on hover, and code comments are invisible in the Inspector, so designers frequently configure components incorrectly without seeing crucial instructions.

**The Solution:**
Add `[InfoBox]` to any field, property, or method:
- **Severity Icons:** Built-in standard presets for `Info`, `Warning`, `Error`, or clean borderless notes (`None`).
- **Dynamic Conditional Display:** Use `VisibleIf` to display warnings only when specific criteria or invalid values occur.
- **Card Customization:** Fine-tune background color, text color, font style, border radius, and padding.
- **Multiple Callouts:** Stack multiple info boxes on a single property to show multiple status indicators or instructions.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class SpawnerConfig : MonoBehaviour
{
    [InfoBox("Spawn radius must be larger than 5 meters to prevent entity overlap.", InspectorMessageType.Warning)]
    public float spawnRadius = 8.0f;

    [InfoBox("NavMesh baking is required for this enemy AI to pathfind.", InspectorMessageType.Info)]
    public GameObject enemyPrefab;
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
public InfoBoxAttribute(string message, InspectorMessageType type = InspectorMessageType.Info)
public InfoBoxAttribute(string message, string colorHex)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `message` | `string` | *(Required)* | Help message text displayed inside the box. |
| `type` | `InspectorMessageType` | `InspectorMessageType.Info` | Visual severity preset (`None`, `Info`, `Warning`, `Error`). |
| `colorHex` | `string` | `null` | Hex text color (sets `type` to `None` for a custom text style). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Message` | `string` | *(Required)* | Help message string. |
| `Type` | `InspectorMessageType` | `Info` | Icon and theme severity mode (`Info`, `Warning`, `Error`, `None`). |
| `VisibleIf` | `string` | `null` | Name of a boolean member controlling dynamic visibility. |
| `FontSize` | `int` | `0` | Text font size in pixels (`0` uses default). |
| `FontStyle` | `FontStyle` | `Normal` | Font style weight (`Normal`, `Bold`, `Italic`). |
| `BackgroundColor` | `string` | `null` | Hex background color behind the info box. |
| `TextColor` / `ColorHex` | `string` | `null` | Hex text color string. |
| `BorderColor` | `string` | `null` | Hex border outline color. |
| `BorderWidth` | `float` | `0f` | Border line thickness in pixels. |
| `BorderRadius` | `float` | `0f` | Corner radius rounding in pixels. |
| `MarginTop` | `float` | `5f` | Top margin spacing in pixels. |
| `MarginBottom` | `float` | `5f` | Bottom margin spacing in pixels. |
| `Padding` | `float` | `0f` | Internal padding in pixels (`0f` uses default). |
| `Width` | `float` | `0f` | Fixed width in pixels (`0f` auto-fits). |
| `Height` | `float` | `0f` | Fixed height in pixels (`0f` auto-fits). |
| `Align` | `FlexAlign` | `FlexAlign.Auto` | Flex alignment within row (`Auto`, `FlexStart`, `Center`, `FlexEnd`). |
| `FullWidth` | `bool` | `false` | Stretches callout edge-to-edge across the inspector. |
| `AboveGroup` | `bool` | `false` | Renders above parent layout group boundaries. |
| `Order` | `int` | `0` | Execution priority relative to other decorator attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class NetworkSessionSettings : MonoBehaviour
{
    public bool isDedicatedServer = false;

    [InfoBox("Client authoritative mode detected! Cheat protection will be disabled.", InspectorMessageType.Error, VisibleIf = nameof(IsClientAuthoritative))]
    public bool enableClientAuthoritativeMovement = false;

    [InfoBox("Tick rates above 60Hz significantly increase server CPU utilization.", InspectorMessageType.Warning)]
    [Range(20, 128)]
    public int simulationTickRate = 60;

    [InfoBox("Production cluster is operating normally in US-East-1.", BackgroundColor = "#16a08522", TextColor = "#1abc9c", BorderRadius = 4f)]
    public string activeClusterRegion = "us-east-1";

    private bool IsClientAuthoritative => enableClientAuthoritativeMovement && !isDedicatedServer;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[DetailedInfoBox]` | Alternative | Use `[InfoBox]` for quick inline callouts; use `[DetailedInfoBox]` for expandable rich documentation cards. |
| `[ShowIf]` | Supported | Info box hides and shows with the field when toggled by parent conditionals. |
| `[BoxGroup]` | Supported | Place inside groups or set `AboveGroup = true` to render outside. |
| `[Button]` | Supported | Place info boxes directly above action buttons to guide team usage. |
