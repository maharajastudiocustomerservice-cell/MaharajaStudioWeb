# Tactical AI 3.0: Environment & Agent Scene Validator

The **Environment & Agent Validator** is a built-in diagnostic and auto-repair suite introduced in **Tactical AI 3.0**. It inspects your active scene, agents, settings assets, and environment helpers in milliseconds to prevent silent configuration failures, dead scorers, missing services, and authoring mismatches.

---

## 🌟 Key Highlights

* **Automatic Scene & Agent Diagnosis**: Scans all active `TacticalAgent` components, environment helpers (`CoverNode`, `TacticalZone`, `Hazard`, `VolumetricCover`, `CoverMetadata`), and scene geometry in milliseconds.
* **Smart Grouped View**: Aggregates duplicate issues across multiple agents into a single summary card (e.g. 20 agents missing an occluder mask or sharing unbaked NavMesh are grouped into 1 card with expandable object chips).
* **One-Click Auto-Fix All**: Safe, undo-supported repairs (`Ctrl+Z`) for missing scene services, agent self-occlusion, layer mismatches, and stopping distance conflicts.
* **Direct Documentation Links**: Every diagnostic card provides a `📖 Doc` button taking you directly to the relevant fix instructions.
* **CI / Test Automation**: Easily run `TacticalAIValidationScanner.ScanScene()` in unit tests or build preflight checks.

---

## 🚀 Quick Access

You can open the Scene Validator at any time via:

1. **Top Menu Bar**: 
   * `Tools > Maharaja Studio > Tactical Cover And Retreat AI > Environment Validator`
2. **TacticalAgent Inspector**:
   * Select any GameObject with a `TacticalAgent` component.
   * Click the **"Open Environment Validator"** or **"Inspect in Validator"** button in the header toolbar.
3. **Quick Start Guide**:
   * Open `Tools > Maharaja Studio > Tactical Cover And Retreat AI > Quick Start Guide`.
   * Click **"Validate Scene & Agents"**.

---

## 🖥️ Interface Overview

```
 ┌────────────────────────────────────────────────────────────────────────────┐
 │ Tactical AI — Environment & Agent Validator            [📖 Docs] [⚡ Auto-Fix All] [🔍 Scan]│
 ├────────────────────────────────────────────────────────────────────────────┤
 │  [ 12 ] Agents    [ 34 ] Helpers    [ 0 ] Errors    [ 2 ] Warnings    [ 5 ] Suggestions │
 ├────────────────────────────────────────────────────────────────────────────┤
 │  [🔍 Search issues...              ]  [ ⊞ Grouped View ]  [ ☰ All Items ]  │
 │  [ All (7) ]  [ Errors (0) ]  [ Warnings (2) ]  [ Suggestions (5) ]  [ Clean (18) ]│
 ├────────────────────────────────────────────────────────────────────────────┤
 │ 🟡 WARNING  [Service Dependency]  (12 Objects Affected)                    │
 │ Missing SuppressionService In Scene                                        │
 │ Active agents use SuppressionPressureScorerSO, but no service is present.  │
 │ 💡 Recommendation: Create a SuppressionService in the scene.               │
 │ [▼ View 12 Affected Objects]                           [📖 Doc] [⚡ Fix All 12] │
 └────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔍 The 7 Diagnostic Categories

### 1. Scene Environment
* **NavMesh Unbaked (`env_navmesh_unbaked`)**: Detects missing baked NavMesh triangulation. Without NavMesh, pathfinding and sampling fail completely.
* **Light Probes Missing (`env_lightprobes_missing`)**: Flags when agents use `LightProbeScorerSO` or `DarknessScorerSO` in a scene without baked light probes.
* **Directional Light Missing (`env_dirlight_missing`)**: Warns when `ShadowProviderSO` is active without a directional light to cast shadows.

### 2. Agent Setup
* **Missing Settings Asset (`no_settings`)**: Detects agents without a `TacticalAISettingsSO` assigned.
* **Missing NavMeshAgent (`no_navmeshagent`)**: Detects agents missing navigation locomotion. Has a **⚡ Quick-Fix** to automatically attach one.
* **Self-Occlusion Hazard (`self_occlusion`)**: Flags when an agent's layer is accidentally included in its own `occluderMask`. Has a **⚡ Quick-Fix** to strip the agent's layer.
* **Stopping Distance Exceeds Repath Tolerance (`stopping_dist_mismatch`)**: Detects when stopping distance prevents completing arrival. Has a **⚡ Quick-Fix** to sync values.
* **Empty Players List (`no_players`)**: Warns when no enemy target is assigned at edit time.

### 3. Service Dependencies (Version 3.0 Services)
* **Missing SuppressionService (`suppression_missing`)**: Required by `SuppressionPressureScorerSO`. Has a **⚡ Quick-Fix** to spawn the service GameObject.
* **Missing SquadCoordinator (`squad_coordinator_missing`)**: Required when `SquadName` is assigned on an agent. Has a **⚡ Quick-Fix** to spawn the coordinator.
* **Missing ThreatMapService (`threat_map_missing`)**: Required for predictive danger heatmaps. Has a **⚡ Quick-Fix** to spawn the service.

### 4. Provider Dependencies
* **CoverNodeProvider With Zero Nodes (`prov_covernode_empty`)**: Detects when `CoverNodeProviderSO` is active but 0 scene `CoverNode` components exist.
* **TacticalZoneProvider With Zero Zones (`prov_tacticalzone_empty`)**: Detects when `TacticalZoneProviderSO` is active but 0 zones are authored.

### 5. Scorer Dependencies & Optimization
* **Zero-Weight Scorers (`scorer_zero_weight`)**: Catches dead scorers configured with `0.0` weight wasting search cycles. Has a **⚡ Quick-Fix** to restore default weight.
* **ZoneControlStateScorer With Zero Zones (`zone_scorer_no_zones`)**: Warns when zone control scorers have no zones to score.

### 6. Semantic Compatibility
* **Stance Scorer on Untagged Providers (`stance_scorer_unsupported`)**: Verifies that providers supply `CoverPointFlags` when using stance/posture scorers.
* **Path Max Distance Smaller Than Search Radius (`path_too_short`)**: Prevents agents discarding valid cover points discovered at search boundaries. Has a **⚡ Quick-Fix** to enlarge path distance.

### 7. Orphaned Scene Authoring
* **Unused CoverNodes (`orphan_covernodes`)**: Alerts designers that authored `CoverNode` components exist in the scene but no active agent queries them.
* **Unused TacticalZones (`orphan_zones`)**: Alerts designers that `TacticalZone` components are placed but no agents query zones.
* **Solid TacticalZone Collider (`zone_col_not_trigger`)**: Flags when a zone collider is solid rather than a trigger. Has a **⚡ Quick-Fix** to set `isTrigger = true`.

---

## ⚡ One-Click Auto-Fix & Safe Undo

1. Click **⚡ Fix** on any card to resolve that specific issue.
2. Click **⚡ Auto-Fix All** in the header to repair all detected issues at once.
3. Every operation is batched into Unity's Undo stack — press `Ctrl+Z` to undo at any time.

---

## 🛠️ Automated CI / Build Script Validation

```csharp
using UnityEngine;
using UnityEditor;
using MaharajaStudio.TacticalAI.Editor.Validation;

public static class BuildValidator
{
    public static bool CheckActiveScene()
    {
        ValidationReport report = TacticalAIValidationScanner.ScanScene();
        if (report.totalErrors > 0)
        {
            Debug.LogError($"[Build Failed] Active scene has {report.totalErrors} validation error(s)!");
            return false;
        }
        return true;
    }
}
```

---

## 📚 See Also

* [What's New in Version 3.0](WhatsNew_v3.0.md)
* [General Scene Validator Guide](../SceneValidatorGuide.md)
* [Getting Started Guide](../Getting-Started.md)
