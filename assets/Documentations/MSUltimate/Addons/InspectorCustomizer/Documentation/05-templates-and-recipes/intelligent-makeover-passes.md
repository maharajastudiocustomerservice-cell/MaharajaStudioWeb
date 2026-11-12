# Intelligent Makeover Passes

> **Module:** MSUltimate Inspector Customizer — Templates & Recipes  
> **Topic:** Automated Heuristic Passes: Relational Pairing, Dynamic Binding, Toggle Cascades, and Toolbars

---

## 1. Overview of Intelligent Makeover Passes

When evaluating an `InspectorTemplate`, the template engine executes four **Intelligent Makeover Passes** before or after evaluating individual matching rules:

```
[Template Execution Engine]
         │
         ├───► Pass 1: Relational Companion Pairing
         │     (Pairs min*/max* into HorizontalGroups or MinMaxSliders)
         │
         ├───► Pass 2: Dynamic Companion Binding
         │     (Binds ProgressBar Max values to companion max fields)
         │
         ├───► Pass 3: Progressive Toggle Cascades
         │     (Wires boolean switches to conditionally hide child fields)
         │
         └───► Pass 4: Action Toolbar Synthesis
               (Organizes parameterless methods into interactive button bars)
```

Each pass can be toggled on or off per template via checkboxes in `InspectorTemplate` or in the Makeover Wizard.

---

## 2. Pass 1: Relational Companion Pairing

- **Setting:** `EnableRelationalPairing = true`
- **Behavior:** Scans the target component for companion field pairs based on naming patterns:
  - `minDamage` and `maxDamage`
  - `startColor` and `endColor`
  - `innerRadius` and `outerRadius`
- **Result:** Instead of rendering them as separate, disconnected vertical rows, the engine automatically wraps them inside a side-by-side `HorizontalGroup("Damage Range")` or converts float pairs into a single `[MinMaxSlider]`.

---

## 3. Pass 2: Dynamic Companion Binding

- **Setting:** `EnableDynamicCompanionBinding = true`
- **Behavior:** Whenever a progress bar attribute is applied to a field (e.g. `currentMana`), the engine searches for an associated ceiling field (`maxMana` or `totalMana`).
- **Result:** It automatically sets `ProgressBar.MaxMember = "maxMana"` instead of a hardcoded constant (`100`). At runtime, when character stats or player levels increase, the progress bar's maximum range automatically scales with the game's actual data.

---

## 4. Pass 3: Progressive Toggle Cascades

- **Setting:** `EnableToggleCascades = true`
- **Behavior:** Detects boolean toggle switches that govern feature subsystems (e.g. `hasShield`, `useGravity`, `enableAudioFX`).
- **Result:** Automatically injects conditional visibility attributes (like `[ConditionalField("hasShield")]` or `[ShowIf("hasShield")]`) onto related child parameters (`shieldCapacity`, `rechargeDelay`, `shieldColor`).
- **Impact:** Cluttered inspectors with 50+ fields collapse into clean, progressive interfaces where advanced settings only appear when their master feature toggle is enabled.

---

## 5. Pass 4: Action Toolbar Synthesis

- **Setting:** `EnableActionToolbar = true`
- **Behavior:** Scans the target component for parameterless `public` or `private` methods (e.g. `Respawn()`, `TriggerExplosion()`, `ResetSensors()`, `ClearCache()`).
- **Result:** Automatically adds `[Button]` attributes to these methods and groups them horizontally using `[ButtonGroup("Actions")]` at the bottom of the inspector. Developers and testers get 1-click debug actions in both Edit Mode and Play Mode without writing custom editor buttons.
