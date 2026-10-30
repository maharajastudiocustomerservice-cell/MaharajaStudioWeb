# Conditional & Visibility Attributes Suite

> **The next-generation dynamic inspector logic framework for Unity.**
> Control the visibility, interactivity, read-only locking, and state of fields, groups, and action buttons using boolean flags, compound C#-style inline expressions, parameterized method validators, bitwise flag operations, engine state macros, and relative parent traversal.

---

## 1. Quick Decision Matrix: What to Use When

| Goal | Recommended Attribute | Visual Result | Typical Use Case |
| :--- | :--- | :--- | :--- |
| **Reveal field only when setting is enabled** | [`[ShowIf]`](show-if.md) | Collapses / expands field | Hiding secondary settings (e.g. show `burstCount` only when `fireMode == Burst`). |
| **Hide field when setting is active** | [`[HideIf]`](hide-if.md) | Completely hides field | Hiding `healthPoints` when `isInvincible` or `godMode` is toggled. |
| **Keep visible but grey out (disable editing)** | [`[EnableIf]`](enable-if.md) / [`[DisableIf]`](disable-if.md) | Greys out (read-only opacity) | Showing a locked feature with a tooltip explaining required unlock level. |
| **Dynamic read-only styling with color tint** | [`[ReadOnlyConditional]`](read-only-conditional.md) | Read-only with custom opacity & color tint | Locking weapon configs during active combat or runtime play mode. |
| **Multi-condition logic with animation & transitions** | [`[ConditionalField]`](conditional-field.md) | Fade animation + AND/OR condition arrays | Advanced setup requiring animated fade transitions and multi-condition arrays. |
| **Conditionally enable/disable Inspector buttons** | [`[ButtonConditional]`](button-conditional.md) | Greys out action button | Disabling "Respawn" when player is already alive. |

---

## 2. Supported Condition Syntax & Evaluator Capabilities

The MSUltimate conditional engine evaluates condition strings seamlessly across **all** conditional attributes (`[ShowIf]`, `[HideIf]`, `[EnableIf]`, `[DisableIf]`, `[ConditionalField]`, `[ReadOnlyConditional]`, and `[ButtonConditional]`).

You are never restricted to simple boolean fields. The engine natively supports:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        MSUltimate Condition Engine                     │
├────────────────────────────────────────────────────────────────────────┤
│  1. Simple Members        →  [ShowIf("isGrounded")]                    │
│  2. Operator Comparison   →  [ShowIf("level", 10, GreaterThanOrEqual)] │
│  3. Inline C# Expressions →  [ShowIf("$health > 50 && $shield <= 0")]  │
│  4. Parameterized Methods →  [ShowIf("HasPermission('Admin')")]        │
│  5. Bitwise Flag Masks    →  [ShowIf("flags", MyFlags.A, HasFlag)]     │
│  6. Global Engine Macros  →  [ShowIf("@isPlayMode")]                   │
│  7. Relative Traversal    →  [ShowIf("$parent.enableAdvanced")]        │
└────────────────────────────────────────────────────────────────────────┘
```

---

### Syntax 1: Simple Identifier (Field, Property, or Method)
Pass the name of any `bool` field, property (including auto-properties and expression-bodied getters), or parameterless method.

```csharp
public bool enableAdvanced;
public bool IsAlive => currentHealth > 0;
public bool CheckIsGrounded() => characterController.isGrounded;

[ShowIf("enableAdvanced")]
public float customMultiplier = 1.5f;

[ShowIf("IsAlive")]
public int ammoCount = 30;

[ShowIf("CheckIsGrounded")]
public float jumpForce = 8.5f;
```

---

### Syntax 2: Direct Comparison Operators
Compare any field or property against an explicit target value using `ConditionOperator`.

```csharp
public WeaponType weaponType = WeaponType.Ranged;
public int characterLevel = 5;

// Enum matching
[ShowIf("weaponType", WeaponType.Ranged)]
public int arrowCapacity = 40;

// Numeric relational comparison
[ShowIf("characterLevel", 10, ConditionOperator.GreaterThanOrEqual)]
public string masterPerk = "Blade Dance";
```

**Supported Operators in `ConditionOperator`:**
- `Equals` (default)
- `NotEquals`
- `GreaterThan`
- `LessThan`
- `GreaterThanOrEqual`
- `LessThanOrEqual`
- `HasFlag` (for `[System.Flags]` enum bitmasks)

---

### Syntax 3: Inline C#-Style Expressions (Mini-Parser)
Write natural compound boolean expressions directly inside the attribute string with **zero boilerplate helper properties**.

- Prefix variable names with `$` (optional if unambiguous) or use direct member names.
- Combine conditions with logical operators: `&&` (AND), `||` (OR), `!` (NOT).
- Group operations using parentheses: `(A || B) && C`.
- Compare against numbers, string literals (`'Admin'`), enum values, booleans (`true`/`false`), and `null`.

```csharp
public float health = 75f;
public float shield = 0f;
public WeaponMode weaponMode = WeaponMode.Burst;
public bool isInvincible = false;

// Compound logical expression with grouping
[ShowIf("$health > 50 && $shield <= 0")]
public string berserkAura = "Crimson Fury";

// Enum comparison inside expression
[ShowIf("$weaponMode == WeaponMode.Burst")]
public int burstCount = 3;

// Complex relational grouping with negation
[ShowIf("($health < 25 || $shield <= 0) && !$isInvincible")]
public Color lowHealthAlertColor = Color.red;
```

---

### Syntax 4: Parameterized Method Invocations
Validator methods can accept literal arguments directly from the attribute condition string. This allows a **single reusable validator method** to power dozens of fields with different parameters.

```csharp
// Single method serves multiple different fields
[ShowIf("HasPermission('Admin')")]
public string adminSecretCode = "ADM-994";

[ShowIf("HasPermission('Moderator')")]
public string banReason = "Rule violation";

[EnableIf("ValidateLevel(20, false)")]
public GameObject highTierWeaponPrefab;

// In the same class:
public bool HasPermission(string requiredRole)
{
    return currentUserRole == requiredRole;
}

public bool ValidateLevel(int minLevel, bool allowVip)
{
    return playerLevel >= minLevel || (allowVip && isVipUser);
}
```

---

### Syntax 5: Bitwise Flag Operations (`HasFlag`)
Test `[System.Flags]` bitmasks natively using `ConditionOperator.HasFlag`. Works with either enum instances or string flag names.

```csharp
[System.Flags]
public enum CombatElements
{
    None = 0,
    Fire = 1 << 0,
    Ice = 1 << 1,
    Lightning = 1 << 2,
    Void = 1 << 3
}

public CombatElements activeElements = CombatElements.Fire | CombatElements.Lightning;

// Reveals when the 'Fire' bit is set
[ShowIf("activeElements", CombatElements.Fire, ConditionOperator.HasFlag)]
public float burnDuration = 5.0f;

// Reveals when the 'Void' bit is set
[ShowIf("activeElements", CombatElements.Void, ConditionOperator.HasFlag)]
public float voidRiftMultiplier = 2.5f;
```

---

### Syntax 6: Global Context & Engine State Macros (`@` Prefixes)
Built-in engine state macros that evaluate dynamically without declaring local dummy variables.

| Engine Macro | Evaluates True When | Typical Use Case |
| :--- | :--- | :--- |
| `@isPlayMode` | `Application.isPlaying == true` | Live telemetry, frame graphs, debug buttons. |
| `@isEditor` | Running in Unity Editor | Editor-only dev settings and gizmo controls. |
| `@isPrefabStage` | Editing inside Prefab Isolation Stage | Hiding scene-specific spawn nodes when editing prefabs. |
| `@selectionCount == 1` | Exactly 1 GameObject is selected | Disabling complex drawers during multi-object editing. |
| `@isProSkin` | Unity dark theme is active | Theme-dependent styling tweaks. |

```csharp
// Only visible in Play Mode
[ShowIf("@isPlayMode")]
public string liveFpsMonitor = "60 FPS";

// Hides when editing inside Prefab Isolation stage
[HideIf("@isPrefabStage")]
public GameObject sceneSpawnAnchor;

// Disables when multi-selecting multiple objects
[EnableIf("@selectionCount == 1")]
public string uniqueAssetId = "ID-001";
```

---

### Syntax 7: Sibling & Parent Relative Traversal (`$parent` / `../`)
Modular nested classes, sub-ScriptableObjects, or polymorphic `[SerializeReference]` nodes can read conditions from their parent container.

```csharp
[System.Serializable]
public class ModularAudioSettings
{
    // Reads 'enableAudioEngine' from the parent MonoBehaviour!
    [ShowIf("$parent.enableAudioEngine")]
    public float masterVolume = 1.0f;

    // Relative parent traversal using '../' syntax
    [ShowIf("../isProLicense")]
    public string spatialAudioPreset = "Dolby Atmos 7.1";
}

public class GameSettings : ModularMonoBehaviour
{
    public bool enableAudioEngine = true;
    public bool isProLicense = false;

    public ModularAudioSettings audioSettings;
}
```

---

## 3. Developer Diagnostics & Typo Resilience (Fuzzy Matching)

In older frameworks, misspelling a condition name (e.g. `[ShowIf("isAliv")]`) causes the field to fail silently and permanently hide, forcing developers to spend hours debugging typos.

In MSUltimate:
1. If a condition member cannot be resolved, the framework calculates the **Levenshtein edit distance** against all available fields, properties, and methods on the target object.
2. It outputs an actionable warning in the Unity Console with the exact suggested correction:
   ```
   [MSUltimate] Condition member 'isAliv' not found on 'PlayerController'. Did you mean 'isAlive'?
   ```
3. Warnings are **session-deduplicated** — they log once per missing member rather than spamming the console on every frame repaint.
4. If an invalid condition is encountered, the inspector **falls back defensively** to safe rendering rather than throwing exceptions or breaking the UI.

---

## 4. Reactive Event-Driven Mode (Zero-Polling)

MSUltimate features a **zero-overhead reactive evaluation architecture**:
- **Property Tracking:** Uses UI Toolkit's native `TrackPropertyValue` on both target properties and their condition siblings. When a designer toggles a checkbox or moves a slider, the conditional element updates **on the exact same frame (0ms latency)** without waiting for an update tick.
- **ChangeEvent Listeners:** Listens to `ChangeEvent<bool>`, `ChangeEvent<string>`, `ChangeEvent<int>`, `ChangeEvent<float>`, and `ChangeEvent<Enum>`.
- **Hybrid Safety Scheduler:** A lightweight 100ms background heartbeat automatically catches external script mutations and undo/redo operations.

---

## 5. Attribute Cheat Sheet

```csharp
// 1. Basic Boolean Toggle
[ShowIf(nameof(showDetails))]

// 2. Inverted Visibility
[HideIf(nameof(isDead))]

// 3. Relational Comparison
[ShowIf(nameof(level), 20, ConditionOperator.GreaterThanOrEqual)]

// 4. Bitwise Flag
[ShowIf(nameof(role), UserRoles.Admin, ConditionOperator.HasFlag)]

// 5. Inline Compound Expression
[ShowIf("$health > 50 && $shield <= 0")]
[ShowIf("$weaponMode == WeaponMode.Burst")]
[ShowIf("($speed > 10 || $isBoosting) && !@isPlayMode")]

// 6. Parameterized Method
[ShowIf("HasPermission('Admin')")]
[EnableIf("CheckRank(5, true)")]

// 7. Engine State Macro
[ShowIf("@isPlayMode")]
[HideIf("@isPrefabStage")]

// 8. Relative Parent Traversal
[ShowIf("$parent.enableAdvanced")]
[ShowIf("../isUnlocked")]

// 9. Read-Only Interactivity
[EnableIf(nameof(isAuthorized))]
[DisableIf(nameof(isBusy))]
[ReadOnlyConditional("$health <= 0 || $isStunned")]
```

---

## 6. Complete Attribute Directory

| Attribute | Target | Primary Purpose | Full Documentation |
| :--- | :--- | :--- | :--- |
| `[ShowIf]` | `Field, Property, Method` | Displays element only when condition evaluates to true. | [Read Docs](show-if.md) |
| `[HideIf]` | `Field, Property, Method` | Hides element completely when condition evaluates to true. | [Read Docs](hide-if.md) |
| `[EnableIf]` | `Field, Property, Method` | Enables interaction when condition evaluates to true (greys out otherwise). | [Read Docs](enable-if.md) |
| `[DisableIf]` | `Field, Property, Method` | Disables interaction when condition evaluates to true (greys out). | [Read Docs](disable-if.md) |
| `[ConditionalField]` | `Field, Property, Method` | Universal condition drawer with fade animation and condition arrays. | [Read Docs](conditional-field.md) |
| `[ReadOnlyConditional]` | `Field, Property, Method` | Locks element into customizable read-only opacity and color tint. | [Read Docs](read-only-conditional.md) |
| `[ButtonConditional]` | `Method` | Dynamically enables or disables Inspector method action buttons. | [Read Docs](button-conditional.md) |
