# [CompareWith]

> Compares a numeric field against another serialized field in real time, displaying a relational indicator badge (Symbol, Percentage, or Ratio).

---

## 1. Overview & Value Proposition

**What it does:**
Evaluates the relationship between two numeric fields (e.g. `currentHealth` vs `maxHealth`, or `minPrice` vs `maxPrice`) in real time, drawing a live indicator badge next to the field showing comparison symbols (`<`, `>`, `==`), percentages (`80%`), or fractions (`4/5`).

**The Problem:**
When editing dependent stats (like current vs max ammo, minimum vs maximum boundaries), designers must mentally calculate the relationship between separate fields or run into inverted values where min exceeds max without noticing.

**The Solution:**
Add `[CompareWith]` to any numeric field:
- **Instant Relational Feedback:** Live badge visualizes relation instantly without writing custom editor GUI code.
- **Multiple Display Formats:** Choose between mathematical symbols (`Symbol`), completion percentage (`Percentage`), or ratio breakdown (`Ratio`).
- **Custom Accent Styling:** Match status badges to your component aesthetic via `ColorHex`.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CharacterVitals : MonoBehaviour
{
    public float maxHealth = 100f;

    [CompareWith("maxHealth", ComparisonDisplay.Percentage, "#2ecc71")]
    public float currentHealth = 75f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `float`, `int`, `double` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public CompareWithAttribute(string otherFieldName, ComparisonDisplay display = ComparisonDisplay.Symbol, string colorHex = "#f1c40f")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `otherFieldName` | `string` | *(Required)* | Name of the second field to compare against. |
| `display` | `ComparisonDisplay` | `ComparisonDisplay.Symbol` | Visual mode (`Symbol`, `Percentage`, `Ratio`). |
| `colorHex` | `string` | `"#f1c40f"` | Hex color code for the indicator badge. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `OtherFieldName` | `string` | *(Constructor)* | Name of the other field evaluated for comparison. |
| `Display` | `ComparisonDisplay` | `ComparisonDisplay.Symbol` | Visual display style (`Symbol`, `Percentage`, `Ratio`). |
| `ColorHex` | `string` | `"#f1c40f"` | Hex color string for badge background and outline. |
| `Order` | `int` | `100` | Execution priority relative to other attributes on the same member (defaults to 100). |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class ShopEconomy : MonoBehaviour
{
    [Header("Price Boundaries")]
    public int maximumSellingPrice = 500;

    [CompareWith("maximumSellingPrice", ComparisonDisplay.Ratio, "#3498db")]
    public int baseItemPrice = 250;

    [Header("Inventory Capacity")]
    public int storageCapacity = 100;

    [CompareWith("storageCapacity", ComparisonDisplay.Percentage, "#f39c12")]
    public int occupiedSlots = 82;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Badge renders cleanly inside layout group headers or rows. |
| `[ValidateInput]` | Supported | Can be combined with `[ValidateInput]` for hard validation errors on invalid ratios. |
| `[ReadOnly]` | Supported | Comparison badge continues to update even if fields are read-only. |
