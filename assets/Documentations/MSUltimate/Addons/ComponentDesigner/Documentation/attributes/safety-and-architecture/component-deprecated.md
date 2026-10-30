# [ComponentDeprecated]

> Displays a prominent obsolete warning or error banner above the component inspector indicating replacement types and planned removal milestones.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentDeprecated]` communicates architectural deprecation directly to level designers and programmers inside the Unity Editor. Injected into `ComponentSlot.BeforeBody`, it displays a styled notification banner with color-coded severity (`Severity = DeprecationSeverity.Warning` or `Error`). The banner displays a human-readable explanation message (`Message`), highlights the recommended modern replacement class (`AlternativeType`), and indicates the target version for eventual code removal (`RemovalVersion`).

**The Problem:**
Standard C# `[System.Obsolete]` attributes only produce subtle compiler warnings that are easily overlooked by designers working solely in the Unity Inspector. Teams often continue adding deprecated MonoBehaviours to new scene prefabs for months, accumulating technical debt and complicating upcoming system refactors.

**The Solution:**
Tagging legacy scripts with `[ComponentDeprecated]`:
- **Unmissable In-Editor Visibility:** Renders an eye-catching warning (amber) or error (crimson) banner directly above component fields.
- **Clear Migration Guidance:** Explicitly tells developers which alternative component to use (e.g., `"Use PlayerMovementV2 instead"`).
- **Scheduled Removal Milestones:** Sets clear expectations by displaying the upcoming game update version where the script will be deleted.
- **Zero Runtime Overhead:** Operates strictly within editor draw cycles without impacting game runtime performance.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentDeprecated(
    "This legacy movement script is deprecated. Use PlayerMovementV2 for physics-based movement.",
    alternativeType: "PlayerMovementV2",
    severity: DeprecationSeverity.Warning)]
public class LegacyPlayerController : MonoBehaviour
{
    public float walkSpeed = 5f;
    public float jumpHeight = 2f;
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
public ComponentDeprecatedAttribute(string message, string alternativeType = "", DeprecationSeverity severity = DeprecationSeverity.Warning)
```

- `message`: Detailed deprecation explanation message explaining why the script is obsolete.
- `alternativeType`: Name of the newer component class or architecture to migrate towards.
- `severity`: Alert tier (`DeprecationSeverity.Warning` for amber banner, `DeprecationSeverity.Error` for red banner).

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Message` | `string` | — | Explanation text describing the deprecation reason and migration path. |
| `AlternativeType` | `string` | `""` | Name of the replacement component type recommended for future use. |
| `RemovalVersion` | `string` | `""` | Planned game version or milestone when this component will be deleted. |
| `Severity` | `DeprecationSeverity` | `Warning` | Alert severity styling (`Warning` = Amber alert, `Error` = Crimson block). |
| `Order` | `int` | `0` | Sequence sorting order within the target component slot. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#DC2626", Width = 2f, Radius = 6f)]
[ComponentBackground("#1F0A0A", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("LEGACY WEAPON BALLISTICS (OBSOLETE)", Subtitle = "Deprecated Raycast Combat Logic", BackgroundColor = "#3B1111", TitleColor = "#FCA5A5")]
[ComponentDeprecated(
    "Raycast ballistics are no longer maintained. Migrate to BallisticsSystemV3 with predictive trajectory simulation.",
    AlternativeType = "BallisticsSystemV3",
    RemovalVersion = "v2.4.0",
    Severity = DeprecationSeverity.Error)]
public class LegacyRaycastWeaponLogic : MonoBehaviour
{
    [Header("Deprecated Gun Settings")]
    public float raycastRangeMeters = 100f;
    public int bulletDamage = 25;
    public bool isInstantHit = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeader]`** | High | Places the deprecation banner directly beneath the header title banner. |
| **`[ComponentLock]`** | High | Pair with `[ComponentLock(defaultLocked: true)]` to prevent developers from modifying deprecated scripts. |
| **`[System.Obsolete]`** | High | Works alongside C# `[Obsolete]` to provide both compiler warnings and immediate visual inspector feedback. |
| **Inspector Controls** | High | Positioned in `BeforeBody`, pushing fields downward without obstructing property bindings. |
