# [ToolbarToggle]

> Replaces standard boolean checkboxes and enum dropdowns with connected, tactile Toolbar push-buttons.

---

## 1. Overview & Value Proposition

**What it does:**
Replaces tiny checkboxes and dropdowns with bold, tactile push-buttons that clearly show ON/OFF or active states.

**The Problem:**
Unity's default 14-pixel checkboxes are tiny, easy to miss, and lack visual punch. For important settings (like "God Mode", "Mute Audio", or "AI Active"), a small checkmark doesn't give you the quick visual confirmation you need when testing.

**The Solution:**
Add `[ToolbarToggle]` to any `bool` or `enum` field:
- **Big, Clickable Push-Buttons:** Turns checkboxes into sleek, satisfying toolbar toggle buttons.
- **Custom Colors & Icons:** Give active and inactive states distinct background colors, borders, and icons.
- **Custom Labels:** Rename options to clear terms like "ACTIVE / DISABLED" or "MUTED / UNMUTED".
- **Enum Support:** Expands enums into a horizontal segmented toolbar where you can see and click every option directly.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class GameAudioMaster : MonoBehaviour
{
    [ToolbarToggle(OnText = "ENABLED", OffText = "MUTED", OnColor = "#2ECC71", OffColor = "#E74C3C")]
    public bool masterMute = false;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Field | AttributeTargets.Property` |
| **Supported Types** | `bool`, `Enum`, `bool[]`, `List<bool>`, `SerializableDictionary<K, bool>`, `SerializableNullable<bool>` |
| **Collection Interface** | `ICollectionElementAttribute` (Automatic Element Cascading) |
| **Allow Multiple** | `false` |
| **Inherited** | `true` |
| **Build Overhead** | Editor-only (Zero runtime build overhead / stripped in builds) |
| **Minimum Unity** | Unity 6 (6000.x)+ |

---

## 4. Constructors & Signatures

```csharp
public ToolbarToggleAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `OnText` | `string` | `"ON"` | Text displayed on the button when boolean is true. |
| `OffText` | `string` | `"OFF"` | Text displayed on the button when boolean is false. |
| `OnIcon` | `string` | `""` | Built-in Unity icon name shown when active. |
| `OffIcon` | `string` | `""` | Built-in Unity icon name shown when inactive. |
| `OnColor` | `string` | `"#4CAF50"` | Active/True state background color in hex format. |
| `OffColor` | `string` | `"#F44336"` | Inactive/False state background color in hex format. |
| `TextColor` | `string` | `"#FFFFFF"` | Text color for the toggle labels. |
| `Width` | `float` | `60f` | Total width in pixels for the toggle button. |
| `Height` | `float` | `24f` | Total height in pixels for the toggle button. |
| `BorderRadius` | `float` | `4f` | Corner rounding radius of the toggle frame in pixels. |
| `FontSize` | `float` | `12f` | Font size for the button text. |
| `BorderWidth` | `float` | `0f` | Border line thickness in pixels. |
| `OnBorderColor` | `string` | `""` | Hex border color when active. |
| `OffBorderColor` | `string` | `""` | Hex border color when inactive. |
| `HoverOnBackgroundColor` | `string` | `""` | Hex background color on hover when active. |
| `HoverOffBackgroundColor`| `string` | `""` | Hex background color on hover when inactive. |
| `Tooltip` | `string` | `""` | Tooltip message shown on hover. |
| `ShowLabel` | `bool` | `true` | Whether the property name label is displayed beside the toggle. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class PostProcessingManager : MonoBehaviour
{
    [BoxGroup("Visual Fidelity", Box = true)]
    [ToolbarToggle(
        OnText = "ACTIVE", 
        OffText = "DISABLED", 
        OnColor = "#27AE60", 
        OffColor = "#7F8C8D",
        Width = 80f,
        Height = 26f
    )]
    [Tooltip("Toggles high-end volumetric bloom in the active camera viewport.")]
    public bool enableVolumetricBloom = true;

    [BoxGroup("Visual Fidelity")]
    [ShowIf(nameof(enableVolumetricBloom))]
    [Range(0f, 2f)] public float bloomIntensity = 1.0f;

    [BoxGroup("Subsystem Diagnostics", Box = true)]
    [InfoBox("Direct collection cascading via ICollectionElementAttribute.")]
    [ToolbarToggle(OnText = "PASS", OffText = "FAIL", OnColor = "#10B981", OffColor = "#EF4444", Width = 70f, Height = 22f)]
    public bool[] diagnosticChecks = new bool[] { true, true, false, true };

    [BoxGroup("Subsystem Diagnostics")]
    [ToolbarToggle(OnText = "ONLINE", OffText = "OFFLINE", OnColor = "#3B82F6", OffColor = "#64748B", Width = 80f, Height = 22f)]
    public List<bool> networkChannels = new List<bool> { true, false, true };
}
```

---

## 7. Stacking & Compatibility Matrix

- **Conditionals Driver:** Pairs exceptionally well with `[ShowIf]`—toggling the button ON/OFF immediately cascades visibility to dependent settings.
- **Grouping:** Centers cleanly inside `[BoxGroup]` and `[HorizontalGroup]`.
- **Enum Support:** When applied to enum fields, splits options into a horizontal multi-segment toolbar strip.

### Collection Cascading Matrix

| Collection / Container Type | Cascading Support | Render Target | Notes |
| :--- | :---: | :--- | :--- |
| `bool[]` | ✅ Yes | Individual array items | Each element renders with custom toggle button. |
| `List<bool>` | ✅ Yes | Individual list items | Renders responsive toggle button per list row. |
| `AdvancedList<bool>` | ✅ Yes | Individual list elements | Supports animated drag, reordering, and element toggling. |
| `SerializableDictionary<K, bool>` | ✅ Yes | Dictionary value column | Value column displays toggle button. |
| `SerializableNullable<bool>` | ✅ Yes | Inner boolean value | Active state renders toggle button. |
| `SerializableTuple<..., bool>` | ✅ Yes | Tuple boolean member | Renders toggle inside tuple column. |

