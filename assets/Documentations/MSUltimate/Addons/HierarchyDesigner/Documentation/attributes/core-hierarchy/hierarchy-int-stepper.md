# [HierarchyIntStepper]

> Injects interactive increment and decrement stepper buttons on the hierarchy row to tune numeric variables with single clicks.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyIntStepper]` brings micro-parameter adjustment controls directly into the scene tree. Rendered by `HierarchyIntStepperRenderer`, it displays a pair of interactive minus (`-`) and plus (`+`) stepper buttons (`ButtonWidth = 16f`, `ButtonColor = "#2A3340"`) flanking a central numeric value readout (`ValueFormat = "{0:F0}"`). Clicking either button alters the underlying numeric field by a defined increment (`Step = 1f`), automatically clamped between bounds (`MinValue`, `MaxValue`), with full Undo history in Edit Mode.

**The Problem:**
Tuning integer quantities across multiple entities—such as adjusting enemy spawn counts, coin values, waypoint sequence numbers, or inventory stack sizes—requires selecting each GameObject and typing into Inspector text boxes. Fine-tuning values across adjacent objects is slow and repetitive.

**The Solution:**
Decorating numeric fields with `[HierarchyIntStepper]`:
- **Single-Click Micro Tuning:** Increment or decrement counts in seconds directly from the hierarchy row.
- **Embedded Live Value Readout:** Displays the current numeric state between the stepper buttons (`ValueWidth = 32f`, `ShowValue = true`).
- **Defensive Value Clamping:** Constrain values within safe numeric ranges (`MinValue`, `MaxValue`) to prevent out-of-bounds errors.
- **Complete Undo Integration:** Every button click registers with Unity's Undo system, making experimentation completely risk-free.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class SpawnerWaveManager : MonoBehaviour
{
    [HierarchyIntStepper(Step = 1f, MinValue = 1f, MaxValue = 20f)]
    public int currentWaveNumber = 1;

    public float enemyHealthScale = 1.2f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyIntStepperRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyIntStepperAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Step` | `float` | `1f` | Numeric delta added or subtracted per click. |
| `MinValue` | `float` | `float.MinValue` | Minimum allowed value for defensive clamping. |
| `MaxValue` | `float` | `float.MaxValue` | Maximum allowed value for defensive clamping. |
| `ShowValue` | `bool` | `true` | Whether to display the numeric value label between stepper buttons. |
| `ValueFormat` | `string` | `"{0:F0}"` | C# string format applied to the numeric label. |
| `ValueColor` | `string` | `"#DDDDDD"` | Hex text color of the numeric value readout. |
| `ButtonColor` | `string` | `"#2A3340"` | Hex background color of the `+` and `-` stepper buttons. |
| `ButtonTextColor` | `string` | `"#88AACC"` | Hex color of the button symbol glyphs. |
| `ButtonWidth` | `float` | `16f` | Width in pixels of each stepper button. |
| `ValueWidth` | `float` | `32f` | Width in pixels of the central value display label. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin. |
| `UndoLabel` | `string` | `"Step Field Value"`| Transaction label recorded in the Unity Undo stack. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the stepper buttons remain active in Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class DungeonLootChest : MonoBehaviour
{
    [Header("Chest Treasure Level")]
    [Tooltip("Tune loot tier directly in the hierarchy; clamped between level 1 and 10.")]
    [HierarchyIntStepper(
        Step = 1f, 
        MinValue = 1f, 
        MaxValue = 10f, 
        ValueFormat = "Lv.{0:F0}", 
        ButtonColor = "#1E293B", 
        ButtonTextColor = "#38BDF8", 
        ValueColor = "#F8FAFC", 
        ValueWidth = 40f, 
        XOffset = 6f)]
    public int chestLootTier = 1;

    [Header("Drop Chances")]
    public float rareItemProbability = 0.15f;
    public bool isMimicChest = false;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyActiveButton]`**| High | Position the stepper widget to the left of the power button using `XOffset = 26f`. |
| **Supported Types** | High | Works seamlessly with `int`, `float`, `double`, `short`, and `byte` numeric field types. |
| **Undo Stack** | High | Fully registers with `Undo.RecordObject` and calls `EditorUtility.SetDirty`. |
| **Play Mode Tuning** | High | Values can be stepped live during gameplay testing without pausing the game. |
