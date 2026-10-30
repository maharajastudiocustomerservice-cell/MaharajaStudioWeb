# [ComponentHeaderButton]

> Adds clickable action buttons directly inside the component header bar to invoke MonoBehaviour methods with custom labels, icons, and colors.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentHeaderButton]` turns component header bars into interactive command dashboards. Injected into `ComponentSlot.BeforeContent`, it embeds high-priority action buttons directly alongside or below the component header title. Each button specifies a target method name (`MethodName`), custom display label (`Label = "Execute"`), emoji/icon glyph (`Icon = "⚡"`), color tint (`Color = "#3B82F6"`), and pinned side alignment (`Position = HeaderButtonPosition.Right` or `Left`). Because `AllowMultiple = true`, developers can declare multiple header buttons side by side.

**The Problem:**
Triggering runtime or editor routines—such as respawning enemies, testing loot rolls, baking procedural dungeons, or resetting save data—usually forces developers to scroll through dozens of fields to locate bottom buttons or clutter code with custom editor scripts.

**The Solution:**
Decorating components with `[ComponentHeaderButton]`:
- **Immediate Top-Level Access:** Critical operational triggers sit prominently at the very top of the component header for instant single-click execution.
- **Multiple Button Stacking:** Place multiple utility buttons (`AllowMultiple = true`) across left and right header docks.
- **Visual Distinction & Icons:** Support expressive icons (e.g. ⚡, 🔄, 🎯, 💾) and rich button tints to communicate action purpose and severity.
- **Non-Destructive Method Invocation:** Safely dispatches reflection calls onto the underlying MonoBehaviour target with full Undo and dirtying support.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentHeaderButton("RebuildDungeon", Label = "Rebuild", Icon = "🔄", Color = "#10B981")]
[ComponentHeaderButton("ClearMonsters", Label = "Purge", Icon = "💀", Color = "#EF4444")]
public class DungeonRoomGenerator : MonoBehaviour
{
    public int dungeonSeed = 1337;
    public int monsterSpawnCap = 25;

    public void RebuildDungeon()
    {
        Debug.Log("Rebuilding procedural dungeon with seed: " + dungeonSeed);
    }

    public void ClearMonsters()
    {
        Debug.Log("Purging all active room monsters.");
    }
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
| **Component Slot** | `BeforeContent` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentHeaderButtonAttribute(string methodName, string label = "Execute", string icon = "⚡", string color = "#3B82F6")
```

- `methodName`: Name of the public or private method on the target MonoBehaviour to execute.
- `label`: Text title displayed on the button surface.
- `icon`: Unicode glyph or emoji displayed preceding the label text.
- `color`: Hex color string for the button background accent.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MethodName` | `string` | — | Target method name on the MonoBehaviour to invoke when clicked. |
| `Label` | `string` | `"Execute"` | Human-readable action label text displayed on the button. |
| `Icon` | `string` | `"⚡"` | Leading icon glyph or emoji symbol (e.g., `"⚡"`, `"🎯"`, `"🔄"`, `"💾"`). |
| `Tooltip` | `string` | `""` | Informational tooltip displayed upon hovering over the button. |
| `Color` | `string` | `"#3B82F6"` | Hex background accent color for the button. |
| `Position` | `HeaderButtonPosition` | `HeaderButtonPosition.Right` | Horizontal dock alignment in the header bar (`Right` or `Left`). |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#0284C7", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#081A2C", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("ORBITAL DROP POD LAUNCHER", Subtitle = "Tactical Reinforcement System", BackgroundColor = "#0E2A47", TitleColor = "#E0F2FE")]
[ComponentHeaderButton("DeployPod", Label = "Launch Pod", Icon = "🚀", Color = "#0284C7", Position = HeaderButtonPosition.Right, Tooltip = "Deploys a pod to the selected coordinates.")]
[ComponentHeaderButton("AbortLaunch", Label = "Abort", Icon = "🛑", Color = "#DC2626", Position = HeaderButtonPosition.Right, Tooltip = "Aborts active launch sequence.")]
public class OrbitalDropPodLauncher : MonoBehaviour
{
    [Header("Targeting Telemetry")]
    public Vector3 targetLandingCoords = new Vector3(120f, 0f, -45f);
    public float dropVelocityMach = 4.2f;
    public int payloadInfantryCount = 6;

    public void DeployPod()
    {
        Debug.Log($"[LAUNCH] Launching drop pod toward {targetLandingCoords} at Mach {dropVelocityMach}!");
    }

    public void AbortLaunch()
    {
        Debug.LogWarning("[ABORT] Drop pod launch sequence aborted by operator.");
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeader]`** | High | Buttons integrate seamlessly into header toolbars alongside titles and badges. |
| **`[ComponentHeaderButton]` Stacking** | High | Multiple buttons stack cleanly side by side; use colors (e.g., green for primary, red for destructive) to guide users. |
| **`[ComponentPresetManager]`** | High | Coexists harmoniously with preset toolbars in the top control area. |
| **Inspector Controls** | High | Dispatches method execution cleanly without disturbing active serialized property values. |
