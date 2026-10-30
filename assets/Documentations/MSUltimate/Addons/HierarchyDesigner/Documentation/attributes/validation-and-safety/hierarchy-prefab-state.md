# [HierarchyPrefabState]

> Displays hierarchy indicators for Prefab variant depth, overridden property counts, and broken or disconnected instances.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyPrefabState]` renders informative prefab status telemetry directly within the Unity Hierarchy window. It visually indicates whether a GameObject is a connected prefab asset, a prefab variant, an instance with local overrides (displaying the exact number of modified properties via `ShowOverrideCount = true`), or a corrupted/disconnected instance with a missing asset reference.

**The Problem:**
In large scenes built from modular prefab kits, accidental overrides (such as position shifts, altered material assignments, or modified component values) go unnoticed until team members attempt to push updates back to the source prefab. Unity's standard hierarchy displays a faint blue icon for overrides, but provides no visibility into how many properties have diverged or whether nested child objects have disconnected.

**The Solution:**
Decorating components with `[HierarchyPrefabState]`:
- **Real-Time Override Count:** Displays the exact tally of modified serialized properties directly on the hierarchy row (e.g. `⛯ +3 Overrides`).
- **Broken Reference Alerts:** Instantly highlights disconnected or broken prefab instances in striking hazard red (`BrokenColor`), preventing lost assets before builds.
- **Custom Status Color Palette:** Separate distinct colors for healthy overrides (`OverrideColor`) and critical broken instances (`BrokenColor`).
- **Clean Level Assembly:** Keeps level design teams aware of accidental prefab modifications before staging Git commits.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyPrefabState]
public class ModularWallSegment : MonoBehaviour
{
    public Material wallMaterial;
    public bool hasDoorOpening = false;
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
| **Render Engine** | `HierarchyPrefabStateRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyPrefabStateAttribute()
```

- Parameterless constructor with default override counting enabled and balanced cyan/crimson status colors.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ShowOverrideCount` | `bool` | `true` | When true, renders a numeric badge indicating how many serialized properties are locally modified. |
| `OverrideColor` | `string` | `"#00D2D3"` | Hex color string used to render the badge for objects with local prefab overrides. |
| `BrokenColor` | `string` | `"#FF4757"` | Hex color string used to render the badge when a prefab instance is disconnected or broken. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the prefab state badge remains visible during active Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row renderers. |

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

namespace ProjectZero.Environment
{
    // Modular prop instance auditing prefab override drift across level sectors
    [HierarchyPrefabState(
        ShowOverrideCount = true,
        OverrideColor = "#00CEC9",
        BrokenColor = "#D63031",
        XOffset = 6f)]
    public class InteractiveChest : MonoBehaviour
    {
        public string lootTableId = "Tier_2_Armor";
        public bool isLocked = true;
        public int requiredKeyTier = 2;

        [Header("Visual Variant")]
        public MeshRenderer chestRenderer;
        public Color glowAccent = Color.cyan;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyTransformWarning]`** | High | Simultaneously monitor prefab property divergence and non-uniform transform scales. |
| **`[HierarchyMissingScriptDetector]`** | High | Guard against both broken prefab references and missing MonoBehaviour script links. |
| **`[HierarchyBookmark]`** | High | Bookmark key prefab kit anchors for rapid scene navigation. |
| **`[HierarchyTooltip]`** | High | Hover tooltip provides deep context on which prefab kit the entity originates from. |
