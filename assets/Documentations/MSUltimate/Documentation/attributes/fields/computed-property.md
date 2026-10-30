# [ComputedProperty]

> Evaluates a mathematical formula referencing other fields and displays the computed live result in the Inspector.

---

## 1. Overview & Value Proposition

**What it does:**
Evaluates mathematical expressions referencing other fields (such as `health * 0.15 + armor`) and displays the calculated result in real time.

**The Problem:**
Tuning derivative gameplay values (like effective HP, DPS, critical damage output, or move speed multipliers) forces developers to either write runtime property getters or manually calculate numbers on a calculator during inspector tweaking.

**The Solution:**
Add `[ComputedProperty]` to any field:
- **Live Formula Evaluation:** Dynamically computes mathematical expressions using variable names directly.
- **Instant Designer Feedback:** Tweak variables (e.g. `baseDamage` and `attackSpeed`) and immediately see the computed result update.
- **Custom Display Label & Colors:** Style the computed row with custom labels and hex text colors.
- **Zero Runtime Memory Cost:** Calculated strictly in the editor GUI layer without modifying serialized object state.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class RPGCombatStats : MonoBehaviour
{
    public float baseDamage = 45f;
    public float attackSpeed = 1.6f;

    [ComputedProperty("baseDamage * attackSpeed", label: "Damage Per Second (DPS)", colorHex: "#2ecc71")]
    public float damagePerSecondPreview;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any numeric field or property |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComputedPropertyAttribute(
    string formula, 
    string label = "Computed", 
    string colorHex = "#aaaaaa", 
    bool showFormula = false)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `formula` | `string` | *(Required)* | Formula string to evaluate referencing other field names. |
| `label` | `string` | `"Computed"` | Display label for the computed output row. |
| `colorHex` | `string` | `"#aaaaaa"` | Hex color string for the calculated value text. |
| `showFormula` | `bool` | `false` | If `true`, displays the formula expression alongside the result. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Formula` | `string` | *(Required)* | Mathematical formula expression string. |
| `Label` | `string` | `"Computed"` | Row display label text. |
| `ColorHex` | `string` | `"#aaaaaa"` | Result value font color hex. |
| `ShowFormula` | `bool` | `false` | Displays formula text beside calculated number. |
| `Order` | `int` | `100` | Execution rendering order in decorator pass. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CharacterSurvivability : MonoBehaviour
{
    [Header("Base Defensive Attributes")]
    public float maxHealth = 1200f;
    public float armorRating = 85f;

    [Header("Computed Effective Metrics")]
    [ComputedProperty("maxHealth * (1 + armorRating / 100)", label: "Effective Health Pool", colorHex: "#3498db", showFormula = true)]
    public float effectiveHealth;

    [ComputedProperty("(armorRating / (armorRating + 100)) * 100", label: "Damage Reduction %", colorHex: "#e67e22")]
    public float damageReductionPercent;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Renders neatly inside boxed attribute groups. |
| `[SuffixLabel]` | Supported | Suffix measurement unit docks alongside computed readout. |
| `[ReadOnly]` | Complementary | Computed properties are naturally read-only displays. |
