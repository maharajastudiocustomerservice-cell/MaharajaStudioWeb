# [ComponentBlueprint]

> Restyles the component inspector as a CAD architectural engineering blueprint complete with drafting grid paper and technical title blocks.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentBlueprint]` transforms the inspector into an authentic technical drafting schematic. Injected into `ComponentSlot.BodyWrapper`, it themes the component with technical millimeter grid paper across three distinct drafting styles (`Style = BlueprintStyle.CyanGrid`, `NavyEngineering`, or `GraphWhite`). The bottom or header of the panel features an authentic engineering title block displaying the subsystem title (`Title = "SYSTEM BLUEPRINT"`), document drawing code (`DrawingCode = "DWG-0842-REV1"`), and technical drafting scale (`Scale = "SCALE 1:1"`).

**The Problem:**
Procedural level generators, building construction systems, vehicle chassis editors, and mechanical physics assemblies lose their architectural precision when presented in generic Unity gray forms. Level architects and mechanics designers miss the feeling of reviewing authentic engineering schematics and construction blueprints.

**The Solution:**
Decorating construction, procedural, and architectural components with `[ComponentBlueprint]`:
- **Authentic Drafting Grid Styles:** Choose between classic Prussian Cyan, deep Navy Engineering, or clean Graph White paper styles.
- **Formal Engineering Title Block:** Displays project schematics, revision numbers, and drawing codes in a professional engineering stamp.
- **Chalk & White Drafting Typography:** Automatically formats labels with crisp technical monospaced styling for maximum technical clarity.
- **Full Control Usability:** Wraps the component seamlessly in `BodyWrapper` while delegating all pointer and mouse wheel interactions directly to nested fields.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBlueprint("MODULAR HABITAT MODULE", "DWG-104-REV2", BlueprintStyle.CyanGrid)]
public class HabitatModuleBlueprint : MonoBehaviour
{
    public float moduleLengthMeters = 12.5f;
    public float internalPressureAtm = 1.0f;
    public int maximumCrewCapacity = 8;
    public bool isAirlockPressurized = true;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ComponentDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Component Slot** | `BodyWrapper` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentBlueprintAttribute(string title = "SYSTEM BLUEPRINT", string drawingCode = "DWG-0842-REV1", BlueprintStyle style = BlueprintStyle.CyanGrid)
```

- `title`: Primary engineering project title displayed inside the title block stamp.
- `drawingCode`: Official document revision string (e.g. `"DWG-0842-REV1"`).
- `style`: Drafting aesthetic preset (`BlueprintStyle.CyanGrid`, `BlueprintStyle.NavyEngineering`, or `BlueprintStyle.GraphWhite`).

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Title` | `string` | `"SYSTEM BLUEPRINT"` | Project or module name printed in the engineering title block. |
| `Style` | `BlueprintStyle` | `BlueprintStyle.CyanGrid` | Color and grid style preset (`CyanGrid`, `NavyEngineering`, `GraphWhite`). |
| `DrawingCode` | `string` | `"DWG-0842-REV1"` | Schematic drawing identifier and revision code. |
| `Scale` | `string` | `"SCALE 1:1"` | Drafting scale ratio stamped on the engineering block. |
| `Order` | `int` | `0` | Sequence sorting order within the target component slot. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBlueprint(
    Title = "HEAVY EXCAVATOR CHASSIS SCHEMATIC",
    DrawingCode = "DWG-CHASSIS-8802-C",
    Scale = "SCALE 1:25",
    Style = BlueprintStyle.NavyEngineering)]
public class HeavyExcavatorChassisSchematic : MonoBehaviour
{
    [Header("Chassis Frame Dimensions")]
    public float wheelbaseLengthMm = 4500f;
    public float trackGaugeMm = 2800f;
    public float groundClearanceMm = 650f;

    [Header("Hydraulic System Tolerances")]
    public float maxOperatingPressureBar = 350f;
    public float boomCylinderStrokeMm = 1850f;
    public bool isAuxiliaryHydraulicLoopInstalled = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeaderButton]`** | High | Place technical actions (e.g. "Validate Dimensions", "Export CAD") directly alongside the blueprint block. |
| **`[ComponentPresetManager]`** | High | Manages schematic variants and blueprint configurations cleanly within the drawing shell. |
| **Technical Fields & Arrays** | High | Dimension measurements, vectors, and bounding boxes fit naturally inside the blueprint layout. |
| **Inspector Controls** | High | Full support for all property drawers and foldouts within the blueprint drawing frame. |
