# [HierarchyBouncingText]

> Animates each character of the hierarchy label in a staggered vertical bouncing spring sequence.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyBouncingText]` calculates a sinusoidal or elastic vertical bounce displacement for each character of the GameObject's hierarchy label, applying a time-delay phase stagger between consecutive glyphs to produce a lively kinetic wave.

**The Problem:**
In playful, casual, or stylized arcade projects, standard static text labels in the Hierarchy window can feel bland. Furthermore, highlighting key interactive elements (such as bouncy platforms, power-up pickups, or celebratory loot chests) is difficult using flat colors alone.

**The Solution:**
Decorating game classes with `[HierarchyBouncingText]`:
- **Dynamic Character-by-Character Stagger:** Consecutive characters bounce with an adjustable offset delay (`Stagger = 0.2f`), creating an organic accordion wave.
- **Physical Spring Feel:** Configurable bounce height (`BounceHeight = 3.5f`) and cycle frequency (`Speed = 3.0f`) bring energetic life to key gameplay entities.
- **Vibrant Font Styling:** Supports custom hex color tinting (`TextColor = "#F1C40F"`) and bold font weight.
- **Editor-Friendly Repainting:** Smoothly repaints without hitching editor responsiveness or generating garbage allocation.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyBouncingText(TextColor = "#F1C40F", BounceHeight = 4.0f, Speed = 3.5f, Stagger = 0.25f)]
public class CoinPickup : MonoBehaviour
{
    public int coinValue = 10;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class` \| `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyBouncingTextRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyBouncingTextAttribute()
```

- Standard parameterless constructor. Spring dynamics and color settings are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `TextColor` | `string` | `"#F1C40F"` | Hex color string applied to the bouncing text characters. |
| `BounceHeight` | `float` | `3.5f` | Peak vertical bounce displacement in pixels. |
| `Speed` | `float` | `3.0f` | Bouncing oscillation speed multiplier. |
| `Stagger` | `float` | `0.2f` | Time phase delay offset between consecutive characters. |
| `Bold` | `bool` | `true` | Whether to render the bouncing characters with bold font weight. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the bounce animation continues running during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row decorations. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyBouncingText(
    TextColor = "#10B981", 
    BounceHeight = 4.5f, 
    Speed = 4.0f, 
    Stagger = 0.2f, 
    Bold = true)]
public class SpringBouncerPlatform : MonoBehaviour
{
    [Header("Bouncer Mechanics")]
    public float launchImpulse = 15.0f;
    public AudioClip bounceSfx;
    public ParticleSystem impactDust;

    private void OnTriggerEnter(Collider other)
    {
        if (other.attachedRigidbody != null)
        {
            other.attachedRigidbody.linearVelocity = Vector3.up * launchImpulse;
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyIcon]`** | High | Pair with custom object icons to emphasize animated collectibles or interactive toys. |
| **`[HierarchyTooltip]`** | High | Add rich tooltips indicating pickup point values or respawn timers. |
| **`[HierarchyTextColor]`** | Incompatible | Do not stack with other text coloring attributes as both modify the label's primary drawing pass. |
| **`[HierarchyFolder]`** | High | Can be applied to child items nested under organizational virtual folders. |
