# [ReadOnlyConditional]

> Conditionally locks a serialized field or property to read-only mode with custom styling based on runtime states, compound C#-style inline expressions, parameterized method validators, or engine state macros.

---

## 1. Overview & Value Proposition

**What it does:**
Makes a field read-only (locked from user modification) when a condition evaluates to true, while applying customizable opacity and color tinting to communicate the locked state clearly.

**The Problem:**
Standard `[ReadOnly]` attributes are static: a field is either permanently locked or permanently editable. In real-world game development, fields often start editable during design setup and must lock down once procedural generation runs, once network synchronization starts, or during runtime Play Mode.

**The Solution:**
Add `[ReadOnlyConditional]` to your fields:
- **Dynamic Lock State:** Switch between editable and locked based on game state, flags, or method return values.
- **Accidental Edit Guard:** Protect vital variables (like random seeds or world anchors) from accidental modification during Play Mode using `[ReadOnlyConditional("@isPlayMode")]`.
- **Inline C#-Style Expressions:** Lock fields when arbitrary formulas evaluate to true (e.g. `[ReadOnlyConditional("$characterHealth <= 0 || $isStunned")]`).
- **Parameterized Methods:** Re-use a single validator to lock fields based on role or privilege arguments (`[ReadOnlyConditional("IsRoleRestricted('Guest')")]`).
- **Visual Styling:** Fully control locked field opacity (`DisabledOpacity = 0.4f`) and background hex color tinting (`DisabledColor = "#FFA726"`).
- **Supports Inversion:** Pass `inverse: true` to make the field editable *only* when the condition is met.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class MatchManager : MonoBehaviour
{
    public bool isMatchLive;

    // 1. Basic Boolean Dynamic Locking
    [ReadOnlyConditional(nameof(isMatchLive))]
    public int maxTeamScore = 50;

    // 2. Play Mode Automatic Lock
    [ReadOnlyConditional("@isPlayMode")]
    public string worldSeedKey = "SEED-PROC-994";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property | Method` |
| **Supported Types** | Any serializable field or property |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes (Native VisualElement binding with zero-polling reactivity) |

---

## 4. Constructors & Parameters

```csharp
public ReadOnlyConditionalAttribute(string condition)
public ReadOnlyConditionalAttribute(string condition, bool inverse)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `condition` | `string` | *(Required)* | Name of the member, parameterized method (`Check('A')`), engine macro (`@isPlayMode`), or inline expression (`$health <= 0`). |
| `inverse` | `bool` | `false` | When true, inverts the logic (field is read-only when condition evaluates to false). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Condition` | `string` | *(Required)* | Name of the condition member or expression to evaluate. |
| `Inverse` | `bool` | `false` | Inverts the read-only condition. |
| `DisabledOpacity` | `float` | `0.5f` | Visual opacity applied to the field when locked (`0.0f` to `1.0f`). |
| `DisabledColor` | `string` | `null` | Hex color tint applied to the background when locked (e.g. `"#FF5555"` or `"#334455"`). |
| `Order` | `int` | `0` | Execution priority relative to other attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class ProceduralWorldGenerator : ModularMonoBehaviour
{
    [Header("Generator State")]
    public bool isWorldGenerated = false;
    public float playerHealth = 100f;
    public bool isFrozen = false;
    public string userRank = "Guest";

    // 1. Basic Boolean Dynamic Lock
    [ReadOnlyConditional(nameof(isWorldGenerated))]
    public int randomSeed = 948102;

    // 2. Lock with Custom Opacity and Color Tinting
    [ReadOnlyConditional(nameof(isWorldGenerated), DisabledOpacity = 0.4f, DisabledColor = "#455A64")]
    public Vector3 terrainExtents = new Vector3(500, 100, 500);

    // 3. Compound Inline C# Expression
    [ReadOnlyConditional("$playerHealth <= 0 || $isFrozen")]
    [InfoBox("Player Incapacitated: Input configuration locked!")]
    public string assignedAttackAction = "Slash Attack";

    // 4. Parameterized Method Validator
    [ReadOnlyConditional("IsRestrictedRole('Guest')")]
    public string administrativeOverrideToken = "OVERRIDE-SECRET-01";

    // 5. Engine Macro: Automatically lock during runtime play
    [ReadOnlyConditional("@isPlayMode")]
    [InfoBox("Play Mode Lock: Locked while running in Play Mode to prevent desync.")]
    public int maxAllowedConnections = 32;

    public bool IsRestrictedRole(string role)
    {
        return userRank == role;
    }

    [Button("Generate World")]
    public void BuildWorld()
    {
        isWorldGenerated = true;
    }

    [Button("Reset Generator")]
    public void ResetGenerator()
    {
        isWorldGenerated = false;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[ReadOnly]` | Dynamic Alternative | Standard `[ReadOnly]` is permanent; `[ReadOnlyConditional]` is dynamic. |
| `[EnableIf]` / `[DisableIf]` | Complementary | EnableIf disables the field control; ReadOnlyConditional allows text selection while preventing edits. |
| `[BoxGroup]` | Supported | Groups and cards respect read-only state of child members. |
| `[Button]` | Supported | Can lock action buttons dynamically. |
| `[InfoBox]` | Supported | Pair with info alerts to describe why fields are locked. |
