# [Button]

> Renders an interactive, styled execution button in the Inspector that invokes C# methods with custom icons, colors, parameter input panels, and layout sizing.

---

## 1. Overview & Value Proposition

**What it does:**
Turns any regular C# method into a clickable, styled button right in the Unity Inspector.

**The Problem:**
In standard Unity, there is no built-in way to test or run a method from the Inspector. To test spawning an enemy, resetting a save file, or executing a custom action, you have to write a custom Editor script, create right-click context menus, or enter Play Mode and trigger it with keyboard shortcuts.

**The Solution:**
Add `[Button]` above any method, field, or property. It instantly generates a clean, interactive button:
- **1-Click Execution:** Run methods directly in Edit Mode or Play Mode with a single click.
- **Custom Styling:** Change button text, background colors, text colors, icons, and button height to make key actions stand out.
- **Parameter Support:** Supports methods with parameters, providing an expandable parameters panel and settings foldout.
- **Conditional Visibility & Interactivity:** Built-in `ShowIf` and `EnableIf` properties for dynamic reactivity.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class Spawner : MonoBehaviour
{
    [Button("Spawn Wave", colorHex: "#27AE60")]
    public void TriggerSpawn()
    {
        Debug.Log("Spawning wave of enemies!");
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Method | AttributeTargets.Field | AttributeTargets.Property` |
| **Allow Multiple** | `true` (Can chain multiple buttons or stack on fields/properties) |
| **Inherited** | `true` |
| **Build Overhead** | Editor-only (Zero runtime build overhead / stripped in builds) |
| **Minimum Unity** | Unity 6 (6000.x)+ |

---

## 4. Constructors & Signatures

```csharp
public ButtonAttribute(string label = null, string colorHex = null)
```

---

## 5. Properties & Customization Options

### Layout & Appearance
| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Label` | `string` | `null` | Custom button label text (defaults to method name in TitleCase). |
| `Height` | `int` | `30` | Pixel height of the button. |
| `Width` | `float` | `0f` | Fixed pixel width (`0` for auto-fill width). |
| `Alignment` | `UiAlignment` | `UiAlignment.Center` | Horizontal layout alignment (`Left`, `Center`, `Right`). |
| `FullWidth` | `bool` | `false` | Stretches button across entire inspector width. |
| `AboveGroup` | `bool` | `false` | Renders button above parent group container instead of inside it. |
| `BackgroundColor` | `string` | `null` | Hex background tint color (e.g. `"#E74C3C"`). |
| `ColorHex` | `string` | `null` | Unified alias property for `BackgroundColor`. |
| `TextColor` | `string` | `null` | Hex text color of the button label. |
| `TextSize` | `int` | `12` | Font size for button label text. |
| `Bold` | `bool` | `true` | Whether the label text is rendered in bold font. |

### Icon Styling
| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Icon` | `string` | `null` | Unity editor icon name (e.g. `"d_PlayButton"`, `"d_Refresh"`). |
| `IconSize` | `int` | `16` | Width and height of icon in pixels. |
| `IconColor` | `string` | `null` | Hex color code tint applied to button icon. |
| `IconPosition` | `IconAlignment`| `IconAlignment.Left` | Position of icon relative to label (`Left`, `Right`). |
| `Gap` | `int` | `5` | Spacing in pixels between button icon and text label. |

### Parameters Panel (for parameterized methods)
| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `SettingsIcon` | `string` | `null` | Built-in icon name for the parameter foldout settings button. |
| `SettingsIconColor` | `string` | `null` | Hex color code tint for the settings button icon. |
| `SettingsBackgroundColor` | `string` | `null` | Hex background color for the settings button. |
| `ExpandedBackgroundColor` | `string` | `null` | Hex background color for the method parameter panel. |
| `ExpandedPadding` | `float` | `10f` | Inner padding in pixels for the parameter panel. |
| `AutoExpandOnOutput` | `bool` | `true` | Automatically expands parameters panel when output or results are generated. |

### Conditional Logic
| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ShowIf` | `string` | `null` | Member name or condition controlling button visibility. |
| `EnableIf` | `string` | `null` | Member name or condition controlling whether button is clickable. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class LevelEnvironmentManager : MonoBehaviour
{
    [BoxGroup("Lighting Controls", Box = true)]
    [Button("Bake Lightmaps", colorHex: "#3498DB", Icon = "d_Lighting")]
    public void TriggerLightmapBake()
    {
        Debug.Log("[Environment] Starting asynchronous lightmap bake...");
    }

    [BoxGroup("Lighting Controls")]
    [Button("Purge Light Cache", colorHex: "#E74C3C", Height = 26)]
    public void ClearLightCache()
    {
        Debug.LogWarning("[Environment] Lightmap cache cleared.");
    }
}
```

---

## 7. Stacking & Compatibility Matrix

- **Grouping:** Pairs seamlessly inside `[BoxGroup]`, `[HorizontalGroup]`, and `[CardGroup]`. Inside horizontal groups, multiple buttons arrange side-by-side into sleek action toolbars.
- **Conditionals:** Respects `ShowIf` and `EnableIf` properties directly without needing external wrapper attributes.
- **Undo Integration:** Modifications triggered by the method are registered in Unity's Undo stack when modifying serialized properties.
