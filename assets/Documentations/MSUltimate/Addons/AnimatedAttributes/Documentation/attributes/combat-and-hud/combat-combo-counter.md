# [CombatComboCounter]

> Displays an arcade combo counter with animated rank badges (SSS to C) and hit-shake feedback on numeric combat fields.

---

## 1. Overview & Value Proposition

**What it does:**
`[CombatComboCounter]` transforms numeric combo fields into an arcade-style combo visualizer. Each combo increment triggers a visceral screen-shake displacement (`ShakeStrength`) and dynamically updates an animated arcade tier rank badge (from `C` up to `SSS` rank). It includes timeout decay indicators (`TimeoutSeconds`) and supports interactive increment clicking and dragging.

**The Problem:**
Tuning combat flow—such as combo timeouts, rank thresholds, and hit-counter multipliers—in character action games requires testing how combo states feel and escalate during rapid combat sequences.

**The Solution:**
Decorating hit-counter properties with `[CombatComboCounter]`:
- **Dynamic Arcade Rank Badges:** Automatically calculates and transitions badges (`C`, `B`, `A`, `S`, `SS`, `SSS`) based on current hits.
- **Hit-Shake Physics:** Vibrates the combo widget with physical impact displacement on every hit registered.
- **Decay Timeout Tracking:** Monitors inactivity decay intervals before the combo streak drops.
- **Collection Cascading:** Implements `ICollectionElementAttribute` for tracking party combo chains or multi-character hits.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class CharacterCombat : MonoBehaviour
{
    [CombatComboCounter(timeout: 4.0f, maxCombo: 999)]
    public int currentHitStreak = 42;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `int`, `float`, `double`, `short`, `long`, `byte` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Collection Element Support** | Yes (`ICollectionElementAttribute`) |

---

## 4. Constructors & Parameters

```csharp
public CombatComboCounterAttribute(float timeout = 3.0f, int maxCombo = 999)

public CombatComboCounterAttribute(string dynamicMaxComboMember, float timeout = 3.0f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `timeout` | `float` | `3.0f` | Inactivity duration in seconds before the combo chain resets. |
| `maxCombo` | `int` | `999` | Maximum combo hits displayable and clamped on the widget. |
| `dynamicMaxComboMember` | `string` | — | Name of a member providing a dynamic max combo hit cap. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `TimeoutSeconds` | `float` | `3.0f` | Seconds before inactivity resets the combo streak to zero. |
| `ShakeStrength` | `float` | `4.0f` | Pixel shake displacement offset on combo hit updates. |
| `MaxCombo` | `int` | `999` | Upper combo clamp limit. |
| `DynamicMaxComboMember` | `string` | `null` | Member name returning dynamic upper combo cap. |
| `DrawInputField` | `bool` | `true` | Whether to draw the standard serialized property input field. |
| `ShowInputField` | `bool` | `true` | Alias for `DrawInputField`. |
| `IsEditable` | `bool` | `true` | Whether clicking the badge increments hits or dragging scrubs values. |
| `Interactive` | `bool` | `true` | Alias for `IsEditable`. |
| `ShowRankBadge` | `bool` | `true` | Whether to display animated arcade rank badges (SSS, S, A, B, C). |
| `CustomLabel` | `string` | `null` | Optional label prefix rendered beside the combo counter widget. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class ActionPlayerCombat : MonoBehaviour
{
    [Header("Arcade Combo Multiplier")]
    [CombatComboCounter(
        timeout: 4.5f, 
        maxCombo: 500, 
        ShakeStrength = 6.0f, 
        ShowRankBadge = true, 
        CustomLabel = "HITS"
    )]
    public int playerComboCount = 85;

    [Header("Air Juggle Hits")]
    [CombatComboCounter(timeout: 2.0f, maxCombo: 50, ShakeStrength = 3.0f)]
    public int aerialJuggleStreak = 12;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Badges fit cleanly into character action boxes or HUD layout groups. |
| `[EditorSoundEffect]` | Stacking | Stack with sound attributes to play satisfying mechanical ticks on hit increases. |
| Arrays & Lists | Supported | Implements `ICollectionElementAttribute` for team combo arrays or coop meters. |
