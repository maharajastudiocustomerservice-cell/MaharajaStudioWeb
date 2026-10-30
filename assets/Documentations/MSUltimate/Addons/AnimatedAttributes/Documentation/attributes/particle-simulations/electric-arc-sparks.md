# [ElectricArcSparks]

> Renders procedural branching lightning bolts and high-voltage sparks arcing across field borders on interaction or validation events.

---

## 1. Overview & Value Proposition

**What it does:**
`[ElectricArcSparks]` electrifies the inspector with procedural electric arcs and branching lightning forks. It generates dynamic lightning paths along the perimeter of the field using randomized fractal subdivision, featuring customizable branching likelihood (`BranchChance`), strike pacing intervals (`ArcInterval`), and vivid neon arc coloration (`ArcColor`).

**The Problem:**
High-energy game mechanics—such as lightning magic, power grid status, cybernetic overloads, or shields—appear static and uninspired when represented as simple numeric fields or standard sliders. Designers lack an immediate sensory cue that a property represents high voltage or unstable electrical power.

**The Solution:**
Decorating electric or energetic properties with `[ElectricArcSparks]`:
- **Procedural Fractal Lightning:** Simulates authentic branching electrical discharge across inspector element borders.
- **Controlled Strike Cadence:** Tune strike frequency (`ArcInterval`) from persistent high-voltage hums to intermittent static discharges.
- **Branching Fork Dynamics:** Adjust the probability (`BranchChance`) that secondary forks splinter off primary lightning channels.
- **Universal Decorator Binding:** Attach to fields, properties, or action buttons (`[Button]`) to simulate charging or firing high-energy weapons.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class TeslaCoil : MonoBehaviour
{
    [ElectricArcSparks(arcColor: "#00F0FF")]
    public float capacitorVoltage = 12000f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property | Method` |
| **Supported Types** | Any serializable field, property, or method |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ElectricArcSparksAttribute(string arcColor = "#00F0FF")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `arcColor` | `string` | `"#00F0FF"` | Hex color string for the procedural electric arc bolts (defaults to Electric Cyan). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ArcColor` | `string` | `"#00F0FF"` | Hex color string for the lightning channels. |
| `BranchChance` | `float` | `0.35f` | Probability (from `0f` to `1f`) for lightning forks to branch into secondary arcs. |
| `ArcInterval` | `float` | `1.5f` | Cadence interval in seconds between procedural arc strikes. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class ArcReactorSubsystem : MonoBehaviour
{
    [Header("Core Overload Voltage")]
    [ElectricArcSparks(
        arcColor: "#38BDF8", 
        BranchChance = 0.55f, 
        ArcInterval = 0.8f
    )]
    public float plasmaDischargeKilowatts = 480f;

    [Header("Manual Emergency Arc Vent")]
    [ElectricArcSparks(arcColor: "#A855F7")]
    public void DischargeSupercapacitors()
    {
        Debug.Log("High voltage manually grounded!");
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Electric arcs cling to and navigate around box group border edges. |
| `[WarningStrobe]` | Stacking | Pairs with hazard strobes to communicate severe electrical hazard states. |
| `[Button]` | Supported | Channels lightning forks across the button frame upon click. |
