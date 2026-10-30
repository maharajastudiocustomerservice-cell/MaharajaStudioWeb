# [ToggleLeft]

> Positions boolean checkboxes or modern pill switches to the left of the label with custom color accents and bold typography.

---

## 1. Overview & Value Proposition

**What it does:**
Reroutes boolean fields so that the checkbox or toggle switch is drawn on the far left, immediately preceding the label text (similar to native UI conventions in modern web and mobile apps), rather than pushed to the far right side of the inspector.

**The Problem:**
In standard Unity inspectors, checkboxes are positioned on the far right edge of the inspector window. When using wide monitors or wide inspector panes, there is a large gap between the field label on the left and the checkbox on the right, making it difficult to visually associate which checkbox belongs to which setting.

**The Solution:**
Add `[ToggleLeft]` to any boolean field:
- **Left-Aligned Checkbox:** Places the interactive toggle immediately adjacent to its label text for effortless eye tracking.
- **Modern Pill Switch Mode:** Option to render as a sleek mobile-style sliding switch (`AsSwitch = true`).
- **Accent Color Styling:** Set custom hex accent colors (`ColorHex = "#2ecc71"`) for active states.
- **Bold Label Option:** Emphasize critical flags with bold typography.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class DebugFeatures : MonoBehaviour
{
    [ToggleLeft("Enable God Mode")]
    public bool godMode = false;

    [ToggleLeft("Mute All Audio", asSwitch: true, colorHex: "#e74c3c")]
    public bool muteAudio = false;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `bool`, `bool?`, `bool[]`, `List<bool>`, `SerializableDictionary<K, bool>`, `SerializableNullable<bool>`, `SerializableTuple<..., bool>` |
| **Collection Interface** | `ICollectionElementAttribute` (Automatic Element Cascading) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ToggleLeftAttribute(string label = "", bool asSwitch = false, string colorHex = null)
public ToggleLeftAttribute(string label, string colorHex)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `label` | `string` | `""` | Label text placed directly to the right of the toggle. |
| `colorHex` | `string` | `null` | Hex color code for the active toggle/switch indicator. |
| `asSwitch` | `bool` | `false` | Renders a modern pill switch instead of a classic square checkbox. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Label` | `string` | `""` | Custom text label displayed alongside the toggle. |
| `ColorHex` | `string` | `null` | Accent color for checkmark or switch thumb when enabled. |
| `AsSwitch` | `bool` | `false` | When `true`, styles the control as a modern sliding pill switch. |
| `Bold` | `bool` | `false` | Renders the label text in bold font. |
| `Tooltip` | `string` | `null` | Tooltip displayed when hovering over the toggle row. |
| `Order` | `int` | `0` | Drawing order priority in the inspector pipeline. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class GameSettingsPanel : MonoBehaviour
{
    [BoxGroup("Graphics & Display", Box = true)]
    [ToggleLeft("Enable Post Processing", asSwitch: true, colorHex: "#3498db")]
    public bool enablePostProcessing = true;

    [ToggleLeft("Vertical Sync (V-Sync)", asSwitch: true, colorHex: "#2ecc71")]
    public bool vSyncEnabled = true;

    [BoxGroup("Developer Diagnostics", Box = true)]
    [ToggleLeft("Show FPS Overlay", Bold = true, Tooltip = "Draws real-time frame counter in upper left screen corner")]
    public bool showFpsOverlay = false;

    [BoxGroup("Subsystem Diagnostic Channels", Box = true)]
    [InfoBox("Direct collection cascading via ICollectionElementAttribute.")]
    [ToggleLeft(colorHex: "#10B981")]
    public bool[] subsystemFlags = new bool[] { true, false, true, true };

    [BoxGroup("Subsystem Diagnostic Channels")]
    [ToggleLeft(asSwitch: true, colorHex: "#3B82F6")]
    public List<bool> securityChannelSwitches = new List<bool> { true, true, false, true };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Aligns cleanly along the left margin inside card containers. |
| `[ShowIf]` | Supported | Functions as an ideal driver for conditional visibility checks. |
| `[ReadOnly]` | Supported | Disables clicking while displaying active/inactive toggle visual state. |
| `[BeginHorizontal]` | Supported | Can be nested inside horizontal button bars or compact toolbars. |

### Collection Cascading Matrix

| Collection / Container Type | Cascading Support | Render Target | Notes |
| :--- | :---: | :--- | :--- |
| `bool[]` | ✅ Yes | Individual array items | Each element renders with left checkbox or pill switch. |
| `List<bool>` | ✅ Yes | Individual list items | Renders responsive left toggle control per list row. |
| `AdvancedList<bool>` | ✅ Yes | Individual list elements | Supports animated drag, reordering, and left toggling. |
| `SerializableDictionary<K, bool>` | ✅ Yes | Dictionary value column | Value column displays left-aligned toggle or switch. |
| `SerializableNullable<bool>` | ✅ Yes | Inner boolean value | Active state renders left toggle. |
| `SerializableTuple<..., bool>` | ✅ Yes | Tuple boolean member | Renders left toggle inside tuple column. |

