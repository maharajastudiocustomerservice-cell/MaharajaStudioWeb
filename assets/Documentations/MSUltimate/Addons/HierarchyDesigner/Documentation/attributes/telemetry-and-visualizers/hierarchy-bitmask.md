# [HierarchyBitmask]

> Displays bitmask or flags enum fields as a compact row of LED matrix dots directly on the hierarchy row.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyBitmask]` renders an intuitive horizontal matrix of miniature LED status dots directly on the hierarchy row for integer or bitmask flags fields. Driven by `HierarchyBitmaskRenderer`, it checks each bit up to `BitCount` (default 8) and paints active high bits with vibrant illuminated colors (`ActiveColor = "#00FFAA"`) and inactive low bits with dim slate dots (`InactiveColor = "#34495E"`).

**The Problem:**
Reading binary flag states, collision layers, capability bits, or active perk masks in Unity requires decoding raw integers (e.g. `23` or `0x17`) or opening multi-selection enum dropdowns in the Inspector. When inspecting multiple AI agents or network clients, comparing which entities have specific flags set is tedious.

**The Solution:**
Decorating integer or enum flag fields with `[HierarchyBitmask]`:
- **Miniature LED Matrix Row:** View up to 32 individual bits as a row of illuminated dots right on the hierarchy row.
- **Instant Visual Pattern Recognition:** Immediately distinguish bit patterns across entities without mental decimal-to-binary conversion.
- **Configurable Dimensions & Colors:** Customize active/inactive colors, dot diameter (`DotSize = 4f`), and spacing.
- **Zero Overhead in Builds:** Runs purely within editor GUI rendering without allocations.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[System.Flags]
public enum EntityCapabilities
{
    CanMove = 1 << 0,
    CanAttack = 1 << 1,
    CanFly = 1 << 2,
    Invulnerable = 1 << 3
}

public class CombatEntity : MonoBehaviour
{
    [HierarchyBitmask(BitCount = 4, ActiveColor = "#10B981", InactiveColor = "#334155")]
    public EntityCapabilities capabilities = EntityCapabilities.CanMove | EntityCapabilities.CanAttack;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Field`, `Property` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyBitmaskRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyBitmaskAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `BitCount` | `int` | `8` | Number of bits (1 to 32) to display in the LED matrix. |
| `ActiveColor` | `string` | `"#00FFAA"` | Hex color for set (high / 1) bits. |
| `InactiveColor` | `string` | `"#34495E"` | Hex color for unset (low / 0) bits. |
| `DotSize` | `float` | `4f` | Diameter in pixels of each LED bit dot. |
| `Spacing` | `float` | `2f` | Spacing in pixels between adjacent LED dots. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the bitmask display remains visible during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class NetworkPermissions : MonoBehaviour
{
    [Header("Security Masks")]
    [HierarchyBitmask(
        BitCount = 8, 
        ActiveColor = "#38BDF8", 
        InactiveColor = "#1E293B", 
        DotSize = 5f, 
        Spacing = 2.5f, 
        XOffset = 6f)]
    public byte securityFlags = 0b00101101;

    public int clientId = 1042;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyStatusDot]`** | High | Use status dots for single boolean states and bitmasks for multi-bit flags. |
| **`[HierarchyVectorDisplay]`** | High | Place vector badges and bitmask matrices side-by-side using offset spacing. |
| **Integral Types** | High | Works directly with `byte`, `sbyte`, `short`, `int`, `uint`, `long`, and `[Flags]` Enums. |
| **Repaint Hook** | High | Evaluated on repaint; does not intercept mouse clicks or modify selection. |
