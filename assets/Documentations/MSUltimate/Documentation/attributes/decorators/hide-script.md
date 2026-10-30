# [HideScript]

> Hides the default Unity "Script" reference field at the top of a MonoBehaviour or ScriptableObject Inspector.

---

## 1. Overview & Value Proposition

**What it does:**
Removes the standard grey, non-editable `Script: MyCustomComponent (MonoScript)` field row that Unity draws at the top of every inspector.

**The Problem:**
In custom tools, design dashboards, and polished asset inspectors, the default Unity `Script` field wastes vertical space, looks unpolished, and tempts non-programmer designers to drag different script files onto the object, causing broken component state.

**The Solution:**
Add `[HideScript]` to any class declaration:
- **Clean Inspector Header:** Instantly produces a streamlined, professional dashboard interface free of unnecessary engine metadata.
- **Accidental Edit Prevention:** Prevents team members from inadvertently detaching or swapping the script reference in the inspector.
- **More Vertical Screen Real Estate:** Reclaims immediate screen space at the top of the inspector for titles, status bars, and core gameplay controls.
- **Inherited Across Subclasses:** Apply to a base class to automatically keep all child component inspectors clean.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

[HideScript]
public class GameEconomyManager : MonoBehaviour
{
    public int startingGold = 1000;
    public float inflationMultiplier = 1.05f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Class` |
| **Supported Types** | Any `MonoBehaviour` or `ScriptableObject` class |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public HideScriptAttribute()
```

*This attribute has no constructor parameters.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Order` | `int` | `0` | Class-level inspector pipeline processing order. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

[HideScript]
[Title("Level Generation Hub", "Procedural dungeon layout generator and seed manager")]
public class DungeonGenerator : MonoBehaviour
{
    [Header("Generation Settings")]
    public int seed = 1337;
    public int maxRooms = 24;

    [Button("Generate Dungeon Layout", ButtonHeight = 32)]
    public void GenerateDungeon()
    {
        Debug.Log($"Generating procedural map with seed: {seed}");
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Title]` | Recommended | Start the inspector with a rich title banner without the distracting Script field above it. |
| `[GUIColor]` | Supported | Pairs with class-level GUI coloring for a completely unified component look. |
| `[BoxGroup]` | Supported | Top-level groups snap directly below the header banner. |
