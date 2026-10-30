# [HierarchyMissingScriptDetector]

> Highlights GameObjects containing broken or missing MonoBehaviour scripts with an attention-grabbing hazard warning badge.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyMissingScriptDetector]` proactively monitors attached components on the GameObject and flags missing or corrupted MonoBehaviour scripts (`Component == null` references caused by deleted, renamed, or uncompiled C# scripts) with an immediate, high-visibility hazard warning badge in the Hierarchy window. It optionally renders animated or static diagonal hazard caution stripes (`ShowHazardStripe = true`).

**The Problem:**
Missing scripts (`"The associated script can not be loaded. Please fix any compile errors..."`) are notorious silent bugs in Unity. Unity provides no native warning indicator in the Hierarchy view; developers must expand every GameObject and scroll through each Inspector component stack to locate missing script placeholders. Uncaught missing scripts often trigger runtime `NullReferenceExceptions` or break automated build pipelines.

**The Solution:**
Decorating components with `[HierarchyMissingScriptDetector]`:
- **Instant Hierarchy Warning:** Spot broken scripts immediately in the scene tree without selecting each object.
- **Hazard Caution Stripes:** Draws high-contrast diagonal safety stripes (`ShowHazardStripe`) across the alert badge to catch attention.
- **Customizable Warning Colors:** Customize alert tint (`AlertColor`) to fit studio QA guidelines.
- **Continuous Scene Health:** Automatically updates as scripts are re-imported, fixed, or removed.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyMissingScriptDetector]
public class LevelRootController : MonoBehaviour
{
    public string zoneId = "Sector_04";
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
| **Render Engine** | `HierarchyMissingScriptDetectorRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyMissingScriptDetectorAttribute()
```

- Parameterless constructor defaults to active hazard caution stripes and vivid red alert coloring.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ShowHazardStripe` | `bool` | `true` | Whether to draw diagonal hazard warning stripes inside the alert badge. |
| `AlertColor` | `string` | `"#FF3838"` | Hex color code used for the hazard warning alert background and icon. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether broken script detection remains active during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row renderers. |

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

namespace ProjectZero.Core
{
    // High-level scene supervisor guarding against broken script dependencies
    [HierarchyMissingScriptDetector(
        ShowHazardStripe = true,
        AlertColor = "#FF4757",
        XOffset = 6f)]
    public class GameManager : MonoBehaviour
    {
        [Header("Runtime Subsystems")]
        public bool initializeOnAwake = true;
        public float tickRate = 60f;

        private void Awake()
        {
            if (initializeOnAwake)
            {
                // Engine startup sequence
            }
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyRequirementCheck]`** | High | Combines missing MonoBehaviour script detection with peer component requirement validation. |
| **`[HierarchyPrefabState]`** | High | Detect broken scripts on prefab instances while simultaneously auditing override states. |
| **`[HierarchyTooltip]`** | High | Display hover documentation detailing which subsystems the host GameObject relies upon. |
| **`[HierarchyNamingConvention]`** | High | Combine architectural naming rules with script integrity checks for robust QA workflows. |
