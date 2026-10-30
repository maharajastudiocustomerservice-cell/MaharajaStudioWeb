# [HierarchyActiveButton]

> Draws an interactive clickable power toggle button directly on the hierarchy row to enable or disable GameObjects with one click.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyActiveButton]` embeds a fast active/inactive toggle switch directly onto the right edge of a GameObject's hierarchy row. Driven by `HierarchyActiveButtonRenderer`, it displays an interactive visibility or power icon (`Size = 14f`) that toggles `go.SetActive(!isActive)` upon clicking. The icon dynamically updates between active (`ActiveIcon = "d_scenevis_visible_hover"`) and inactive states (`InactiveIcon = "d_scenevis_hidden_hover"`), complete with custom color tinting (`InactiveColor = "#FF6B6B"`). It records full Unity Undo operations in Edit Mode and executes instantly during Play Mode testing.

**The Problem:**
Toggling GameObjects on and off is one of the most frequent actions in Unity level design and debugging. Without an inline button, developers must select the GameObject in the Hierarchy, shift their gaze and mouse over to the Inspector, click the tiny checkbox in the top-left corner, and then return to the Hierarchy.

**The Solution:**
Decorating components with `[HierarchyActiveButton]`:
- **Single-Click Activation:** Turn entities on or off instantly from the Hierarchy without selecting them or moving your cursor to the Inspector.
- **Clear Visual State Feedback:** Inactive objects stand out clearly with distinct red-tinted hidden icons (`#FF6B6B`).
- **Complete Undo Integration:** In Edit Mode, all toggles register with Unity's Undo stack (`Undo.RecordObject`) and mark scenes dirty for seamless saving.
- **Play Mode Responsive:** Works fluidly during Play Mode gameplay sessions to toggle spawners, lights, and UI canvases in real time.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyActiveButton]
public class AmbientLightingGroup : MonoBehaviour
{
    public Light[] streetLamps;
    public float ambientIntensity = 1.2f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyActiveButtonRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyActiveButtonAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ActiveIcon` | `string` | `"d_scenevis_visible_hover"` | Built-in Unity icon name rendered when the GameObject is active. |
| `InactiveIcon` | `string` | `"d_scenevis_hidden_hover"` | Built-in Unity icon name rendered when the GameObject is deactivated. |
| `ActiveColor` | `string` | `""` | Optional hex color tint applied to the icon when active. |
| `InactiveColor` | `string` | `"#FF6B6B"` | Hex color tint applied to the icon when deactivated (defaults to warning red). |
| `Size` | `float` | `14f` | Icon button width and height in pixels. |
| `XOffset` | `float` | `2f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `UndoLabel` | `string` | `"Toggle Active State"` | Undo transaction description registered in Edit Mode. |
| `IsActiveInPlayMode`| `bool` | `true` | Whether the toggle button remains visible and interactive in Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyActiveButton(
    ActiveIcon = "d_winbtn_mac_max", 
    InactiveIcon = "d_winbtn_mac_close", 
    InactiveColor = "#EF4444", 
    Size = 14f, 
    XOffset = 4f)]
public class WaveSpawnerController : MonoBehaviour
{
    [Header("Spawner Configuration")]
    public GameObject enemyPrefab;
    public int enemiesPerWave = 12;
    public float waveIntervalSeconds = 25f;

    [Header("Telemetry")]
    public int currentWaveNumber = 1;
    public bool isSpawningActive = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyIcon]`** | High | Place `HierarchyActiveButton` on the far right (`XOffset = 2f`) and status icons closer to the text. |
| **`[HierarchyHighlight]`** | High | Toggling off dims the background row, visually confirming that the GameObject is inactive. |
| **Multi-Object Selection** | High | Clicking the button acts exclusively on the target GameObject without altering current selection. |
| **Undo Stack** | High | Fully integrated with Unity `Undo.RecordObject` to allow effortless `Ctrl+Z` rollbacks. |
