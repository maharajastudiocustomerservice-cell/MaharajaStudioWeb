# [HierarchyGlow]

> Renders an ambient glow halo or pulsating neon border highlighting high-priority entities in the hierarchy.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyGlow]` surrounds high-priority GameObjects with an atmospheric, glowing neon border or halo directly within the Hierarchy window. Driven by `HierarchyGlowRenderer`, it utilizes `HierarchyDrawUtilities.DrawGlowHalo` to project a soft, feathered ambient border (`GlowColor = "#9B59B6"`). It supports live sinusoidal pulsation (`Pulse = true`) with customizable speed (`PulseSpeed = 2.0f`) and intensity multipliers (`Intensity = 1.0f`), creating an unmissable beacon for mission-critical objects.

**The Problem:**
In large hierarchies with hundreds of objects, finding the active Player controller, the level exit trigger, a vital singleton manager, or a critical bug-tracking target requires scanning text line by line. Standard highlight colors can look flat or blend into regular selections.

**The Solution:**
Decorating components with `[HierarchyGlow]`:
- **Ambient Neon Halo:** Surrounds the row with a feathered, glowing border that immediately draws developer focus.
- **Pulsating Beacon Effect:** Smoothly pulses in opacity over time using sinusoidal real-time math.
- **Fully Customizable Styling:** Configure glow color, halo intensity, pulse state, and frequency.
- **Class or Field Scope:** Apply at the class level for whole-row glowing or on specific fields.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyGlow(GlowColor = "#00FFAA", Intensity = 1.2f, Pulse = true)]
public class QuestObjectiveTarget : MonoBehaviour
{
    public string objectiveId = "FIND_RELIC";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class`, `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyGlowRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyGlowAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `GlowColor` | `string` | `"#9B59B6"` | Hex color of the ambient glow halo. |
| `Intensity` | `float` | `1.0f` | Intensity multiplier for the glow halo effect. |
| `Pulse` | `bool` | `true` | Whether the glow pulses periodically in opacity over time. |
| `PulseSpeed` | `float` | `2.0f` | Speed multiplier of the periodic pulse wave. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the glow halo remains visible during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyGlow(
    GlowColor = "#EF4444", 
    Intensity = 1.5f, 
    Pulse = true, 
    PulseSpeed = 3.0f)]
public class CriticalBossSpawner : MonoBehaviour
{
    [Header("Spawner Properties")]
    public GameObject bossPrefab;
    public bool isEncounterTriggered = false;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyGlassmorphism]`** | High | Place glow effects behind frosted glass panels for stunning cyber/futuristic aesthetics. |
| **`[HierarchyBookmark]`** | High | Combine bookmark ribbons with ambient glow to create prominent visual landmarks. |
| **`[HierarchyStatusDot]`** | High | Use pulsing glow for critical alerts (e.g. low health, missing references, active boss fight). |
| **Repaint Hook** | High | Renders during IMGUI repaint; does not intercept clicks or alter selection logic. |
