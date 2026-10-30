# [ComponentTooltip]

> Assigns a global hover tooltip to the component card background, displaying contextual guidance and architectural summaries.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentTooltip]` attaches a component-level hover tooltip description to the entire component inspector card. Injected into `ComponentSlot.BeforeBody`, it binds the specified guidance text (`Tooltip`) to the component root container. When developers hover their cursor over the background or header of the component card, Unity displays a clean tooltip popover containing component instructions, prerequisites, or operational warnings.

**The Problem:**
Standard Unity `[Tooltip]` attributes operate strictly at the serialized field level. Documenting global component responsibilities, setup requirements, or lifecycle contracts requires inserting lengthy comments or bulky help boxes that occupy permanent vertical space.

**The Solution:**
Decorating components with `[ComponentTooltip]`:
- **Card-Wide Hover Guidance:** Reveal comprehensive component documentation upon cursor hover without consuming layout space.
- **Clean Inspector Ergonomics:** Keeps the inspector interface clean while ensuring architectural advice is always one hover away.
- **Simple Setup:** Configure via a single constructor parameter (`string tooltip`).
- **Zero Input Interference:** Native UI Toolkit tooltip integration does not block pointer clicks, drags, or field interactions.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentTooltip("Governs global dynamic weather cycles. Requires a WeatherPreset ScriptableObject assigned before entering Play mode.")]
public class GlobalWeatherSystemDirector : MonoBehaviour
{
    public float timeOfDayHours = 14.5f;
    public float rainIntensity = 0.0f;
    public bool isDynamicCycleEnabled = true;
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
| **Component Slot** | `BeforeBody` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentTooltipAttribute(string tooltip)
```

- `tooltip`: Guidance or documentation string displayed when hovering over the component card.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Tooltip` | `string` | *(Constructor)* | Explanatory tooltip text string displayed on hover. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#4338CA", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#0F0E24", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("PROCEDURAL DUNGEON GENERATOR", Subtitle = "BPS Room Carving & Graph Solver", BackgroundColor = "#191740", TitleColor = "#E0E7FF")]
[ComponentTooltip("Generates multi-floor BSP dungeon layouts at runtime. Ensure RoomPrefabs collection contains at least 3 valid rooms.")]
public class ProceduralDungeonGenerator : MonoBehaviour
{
    [Header("Generation Parameters")]
    public int dungeonFloorSeed = 1337;
    public int totalRoomCount = 24;
    public int maxCorridorBranchLength = 6;

    [Header("Baking")]
    public bool bakeNavMeshOnGenerationComplete = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeader]`** | High | Tooltip displays when hovering over header bars or card backdrops. |
| **`[ComponentHelpBox]`** | High | Use `[ComponentTooltip]` for auxiliary instructions to keep help boxes reserved for critical warnings. |
| **Inspector Controls** | High | Works alongside field-level tooltips without conflict. |
