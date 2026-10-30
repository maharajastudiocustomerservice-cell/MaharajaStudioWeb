# [ButtonConditional]

> Conditionally enables or disables an Inspector-drawn method action button based on runtime states, compound C#-style inline expressions, parameterized method validators, or engine state macros.

---

## 1. Overview & Value Proposition

**What it does:**
Greys out and disables an Inspector `[Button]` when a condition is not met (such as only allowing execution in Play Mode, or requiring prerequisite setup).

**The Problem:**
In standard Unity, Inspector buttons are either always clickable or not drawn at all. Clicking a "Fire Cannon" button when the game is not playing, or clicking "Spawn Boss" when a boss is already active, throws `NullReferenceException` errors, corrupts test data, and frustrates designers.

**The Solution:**
Add `[ButtonConditional]` to your method alongside `[Button]`:
- **Safe Method Triggering:** Automatically greys out the button when conditions are unsatisfied.
- **Inline C#-Style Expressions:** Enable buttons based on compound formulas (e.g. `[ButtonConditional("$isArenaActive && $currentEnemyCount == 0")]`) without writing dummy boolean properties.
- **Engine State Guard:** Ensure buttons can only be pressed in Play Mode using `[ButtonConditional("@isPlayMode")]`.
- **Parameterized Methods:** Gate buttons behind role or parameter checks (`[ButtonConditional("HasRole('Developer')")]`).
- **Custom Disabled Styling:** Configure disabled opacity (`DisabledOpacity = 0.35f`) and disabled background color tinting (`DisabledColor = "#333333"`).
- **Clear User Guidance:** Prevents accidental clicks and invalid gameplay states during testing.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class TurretLauncher : MonoBehaviour
{
    public bool hasAmmunition = true;

    // 1. Basic Boolean Condition
    [Button("Fire Turret")]
    [ButtonConditional(nameof(hasAmmunition))]
    public void FireTurret()
    {
        Debug.Log("Fired rocket!");
    }

    // 2. Play Mode Only Action Button
    [Button("Simulate Overload")]
    [ButtonConditional("@isPlayMode")]
    public void SimulateOverload()
    {
        Debug.Log("Overload simulated!");
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Method` |
| **Supported Types** | Methods decorated with `[Button]` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes (Native VisualElement binding with zero-polling reactivity) |

---

## 4. Constructors & Parameters

```csharp
public ButtonConditionalAttribute(string condition)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `condition` | `string` | *(Required)* | The name of a boolean member, parameterized method (`Check('A')`), engine macro (`@isPlayMode`), or inline expression (`$ammo > 0`). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Condition` | `string` | *(Required)* | Condition string or expression evaluated to enable the button. |
| `DisabledOpacity` | `float` | `0.5f` | Visual opacity applied to the button element when disabled (`0.0f` to `1.0f`). |
| `DisabledColor` | `string` | `null` | Optional hex color tint applied to the disabled button background (e.g. `"#444444"`). |
| `Order` | `int` | `0` | Execution priority relative to other attributes. |

---

## 6. Production-Grade Example

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class BossArenaManager : ModularMonoBehaviour
{
    [Flags]
    public enum ArenaFlags
    {
        None = 0,
        SafeZone = 1 << 0,
        CombatZone = 1 << 1,
        AdminLock = 1 << 2
    }

    [Header("Arena State")]
    public ArenaFlags arenaState = ArenaFlags.CombatZone;
    public bool isArenaActive = true;
    public int currentEnemyCount = 0;
    public float arenaManaReserves = 100f;
    public string designerRole = "Tester";

    // 1. Compound Inline C# Expression (No helper property needed!)
    [Button("Spawn Wave", colorHex: "#E67E22")]
    [ButtonConditional("$isArenaActive && $currentEnemyCount == 0")]
    public void TriggerReinforcements()
    {
        currentEnemyCount += 5;
        Debug.Log("[BossArena] Wave spawned!");
    }

    // 2. Play Mode Guard: Cannot execute physics simulation in edit mode
    [Button("Detonate Core Shockwave", colorHex: "#E74C3C")]
    [ButtonConditional("@isPlayMode")]
    public void DetonateShockwave()
    {
        Debug.Log("[BossArena] Shockwave detonated in Play Mode!");
    }

    // 3. Expression with Resource Threshold
    [Button("Refill Mana Fountains", colorHex: "#3498DB")]
    [ButtonConditional("$arenaManaReserves < 50")]
    public void RefillMana()
    {
        arenaManaReserves = 100f;
        Debug.Log("[BossArena] Mana refilled!");
    }

    // 4. Parameterized Method Validator
    [Button("Purge All Enemies (Dev Cheat)", colorHex: "#9B59B6")]
    [ButtonConditional("HasPermission('Admin')")]
    public void PurgeEnemies()
    {
        currentEnemyCount = 0;
        Debug.Log("[BossArena] Dev Purge complete!");
    }

    public bool HasPermission(string role)
    {
        return designerRole == role;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Button]` | Companion Attribute | Placed on the same method to draw and conditionally control the button. |
| `[ShowIf]` / `[HideIf]` | Alternative | Use `[ShowIf]` on a method to hide the button entirely; use `[ButtonConditional]` to keep it visible but greyed out. |
| `[BoxGroup]` | Supported | Buttons inside box groups and foldouts inherit group layout and conditional interactivity. |
