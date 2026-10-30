# [ModularWindow]

> Configures window titles, icons, default dimensions, min/max limits, utility docking flags, and customizer toolbars for ModularEditorWindow and ModularMenuEditorWindow subclasses.

---

## 1. Overview & Value Proposition

**What it does:**
Decorates custom `EditorWindow` subclasses that inherit from `ModularEditorWindow` or `ModularMenuEditorWindow`. Automatically configures tab headers, icon textures, default opening dimensions, min/max boundary constraints, floating utility behavior, and an integrated layout customizer toolbar button.

**The Problem:**
Creating custom Unity editor windows normally requires boilerplate C# code to configure window minimum sizes, icons, title content, and dimensions, usually spread across static `ShowWindow` menu methods and `OnEnable` handlers.

**The Solution:**
Add `[ModularWindow]` to any modular editor window class:
- **Declarative Window Setup:** Specify titles, icons, and dimensions in a clean single attribute.
- **Enforced Min/Max Constraints:** Guarantees windows cannot be resized below functional UI limits.
- **Utility Window Mode:** Flag `IsUtility = true` for floating, always-on-top modal tools.
- **Built-in Customizer Hook:** Toggle `ShowCustomizerButton = true` to inject the MSUltimate Layout Customizer directly into the window's toolbar.

---

## 2. Quick Start

```csharp
using UnityEditor;
using MaharajaStudio.MSUltimate.Runtime.Windowing;

[ModularWindow("Quest Database", "d_CustomTool", width: 900f, height: 600f, ShowCustomizerButton = true)]
public class QuestDatabaseWindow : EditorWindow
{
    // Window content logic
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Class` |
| **Supported Types** | Subclasses of `EditorWindow`, `ModularEditorWindow`, `ModularMenuEditorWindow` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ModularWindowAttribute(string title = null)
public ModularWindowAttribute(string title, string icon, float width = 800f, float height = 550f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `title` | `string` | `null` | Window title displayed in the tab header. |
| `icon` | `string` | `null` | Optional Unity built-in icon identifier (e.g. `"SettingsIcon"`). |
| `width` | `float` | `800f` | Default opening window width in pixels. |
| `height` | `float` | `550f` | Default opening window height in pixels. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Title` | `string` | *(Constructor)* | Window title text in the tab bar. |
| `Icon` | `string` | *(Constructor)* | Unity editor icon name for the window tab. |
| `DefaultWidth` | `float` | `800f` | Default width in pixels when opened. |
| `DefaultHeight` | `float` | `550f` | Default height in pixels when opened. |
| `MinWidth` | `float` | `350f` | Minimum allowed width limit. |
| `MinHeight` | `float` | `250f` | Minimum allowed height limit. |
| `MaxWidth` | `float` | `0f` | Maximum width limit (`0` = unconstrained). |
| `MaxHeight` | `float` | `0f` | Maximum height limit (`0` = unconstrained). |
| `IsUtility` | `bool` | `false` | Whether to open as a floating utility window (always on top). |
| `ShowCustomizerButton` | `bool` | `false` | Injects the 'Customize Layout' button into the window toolbar. |

---

## 6. Production-Grade Example

```csharp
using UnityEditor;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.Windowing;

[ModularWindow(
    title: "Audio Mixer Workbench", 
    icon: "AudioMixerController Icon", 
    width: 1000f, 
    height: 700f
)]
public class AudioMixerWorkbenchWindow : EditorWindow
{
    [MenuItem("Tools/Audio/Mixer Workbench")]
    public static void Open()
    {
        GetWindow<AudioMixerWorkbenchWindow>();
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `ModularEditorWindow` | Native Integration | Automatically read and initialized during window instantiation. |
| `ShowCustomizerButton` | Supported | Integrates with MSUltimate Inspector Customizer addon presets. |
| UI Toolkit | Supported | Full support for modern UI Toolkit editor window hierarchies. |
