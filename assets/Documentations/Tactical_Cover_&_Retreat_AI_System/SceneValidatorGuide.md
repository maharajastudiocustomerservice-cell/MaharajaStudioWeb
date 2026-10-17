# Tactical AI — Environment & Agent Scene Validator Guide

The **Environment & Agent Validator** is a built-in diagnostic and auto-repair suite designed to eliminate silent setup errors, missing runtime dependencies, dead scorers, and authoring mismatches across your scene and AI agents.

Whether you are configuring your very first agent or debugging a complex multi-squad encounter with custom zones and suppression, the validator ensures your tactical setup is production-ready with one click.

---

## 🚀 Quick Access

You can open the Scene Validator at any time via three convenient entry points:

1. **Top Menu Bar**: 
   * `Tools > Maharaja Studio > Tactical AI > Windows > Environment & Agent Validator`
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

### 1. Header Toolbar
* **📖 Documentation**: Opens this documentation guide directly in Unity or your default browser.
* **⚡ Auto-Fix All**: Executes all available safe quick-fixes across every detected issue in one single, fully undoable transaction (`Ctrl+Z`).
* **🔍 Scan Scene**: Re-runs a full scene analysis on demand. (Scanning completes in just a few milliseconds).

### 2. Summary Grid
Displays real-time counters categorized by diagnostic status:
* **Agents**: Count of active `TacticalAgent` components detected in the scene.
* **Helpers**: Count of tactical environment components (`CoverNode`, `TacticalZone`, `Hazard`, `VolumetricCover`, `CoverMetadata`, etc.).
* **Errors (🔴)**: Critical failures that will cause search failure, throw exceptions, or leave agents stranded.
* **Warnings (🟡)**: Degraded behaviors (e.g., dead scorers with 0 weight, missing scene services where fallback logic executes).
* **Suggestions (💡)**: Authoring optimizations, performance recommendations, or orphaned objects placed in the scene but never used.
* **Clean (🟢)**: Confirmed checks that passed validation successfully.

### 3. Smart Filter Toolbar
* **Search Field**: Instantly filters diagnostic findings by object name, title, description, or recommendation text.
* **View Toggle**:
  * **⊞ Grouped (Default)**: Aggregates identical issues across multiple agents into a single summary card. For instance, if 30 agents lack a `SuppressionService`, you get 1 clean card instead of 30 repetitive rows.
  * **☰ All Items**: Displays an itemized, flat list of every individual diagnostic finding.
* **Severity Filter Pills**: Filter view by `All`, `Errors`, `Warnings`, `Suggestions`, or `Clean (Passed)`.

---

## 🔍 Diagnostic Categories & Rules

The Scene Validator performs in-depth checks across **7 core categories**:

---

### 1. Scene Environment

Checks foundational scene geometry, navigation surfaces, and lighting required for AI decision-making.

#### <a id="env-navmesh-unbaked"></a>🔴 NavMesh Is Not Baked in Scene (`env_navmesh_unbaked`)
* **Problem**: The active scene has no baked Unity NavMesh geometry.
* **Impact**: Pathfinding, obstacle raycasting, candidate spot sampling, and path safety calculations will immediately fail.
* **Fix**: Open `Window > AI > Navigation` (or use a `NavMeshSurface` component) and click **Bake**.

#### <a id="env-lightprobes-missing"></a>🟡 Light Probes Missing (`env_lightprobes_missing`)
* **Problem**: One or more active agents use `LightProbeScorerSO` or `DarknessScorerSO`, but the scene contains zero baked Light Probes.
* **Impact**: Light-based stealth scorers cannot query local ambient irradiance and will fall back to unbaked ambient color.
* **Fix**: Place a `Light Probe Group` in the scene and bake lighting via `Window > Rendering > Lighting`.

#### <a id="env-dirlight-missing"></a>🟡 Directional Light Missing (`env_dirlight_missing`)
* **Problem**: An agent uses `ShadowProviderSO`, but no active Directional Light exists in the scene.
* **Impact**: The shadow provider cannot calculate shadow cast projections.
* **Fix**: Add a Directional Light to your scene.

---

### 2. Agent Setup

Validates individual `TacticalAgent` component assignments and layer configurations.

#### <a id="no-settings"></a>🔴 Missing Tactical AI Settings (`no_settings`)
* **Problem**: The `TacticalAgent` has no `TacticalAISettingsSO` assigned to its `Settings` slot.
* **Impact**: The agent has no brain or rules; calling `RetreatToHide()` will throw a warning and fail.
* **Fix**: Right-click in Project view > `Create > TacticalAI > Tactical AI Settings`, configure it, and assign it to the agent.

#### <a id="no-navmeshagent"></a>🔴 Missing NavMeshAgent (`no_navmeshagent`)
* **Problem**: The agent has no `NavMeshAgent` assigned or attached.
* **Impact**: The AI cannot pathfind or traverse the scene to reached cover.
* **⚡ Quick-Fix Available**: Automatically adds a `NavMeshAgent` component to the GameObject.

#### <a id="self-occlusion"></a>🔴 Self-Occlusion Hazard (`self_occlusion`)
* **Problem**: The agent's GameObject layer is included in its own `Settings.occluderMask`.
* **Impact**: When the agent checks visibility to an enemy, its own collider blocks line-of-sight raycasts, causing the agent to falsely believe it is already hidden when standing in plain sight.
* **⚡ Quick-Fix Available**: Automatically strips the agent's layer from the `occluderMask`.

#### <a id="no-players"></a>🟡 Empty Target/Players List (`no_players`)
* **Problem**: The `players` list on `TacticalAgent` is empty at edit time.
* **Impact**: The agent cannot evaluate visibility, threat distance, or flanking angles unless a target is assigned dynamically via script before calling `RetreatToHide()`.
* **Fix**: Assign your player transform in the Inspector, or call `agent.SetSinglePlayerTarget(target)` in your startup code.

#### <a id="stopping-dist-mismatch"></a>🟡 Stopping Distance Exceeds Repath Tolerance (`stopping_dist_mismatch`)
* **Problem**: The `NavMeshAgent.stoppingDistance` is greater than `TacticalAISettingsSO.repathTolerance`.
* **Impact**: The agent may halt before reaching the exact calculated cover coordinate and fail to complete its arrival event.
* **⚡ Quick-Fix Available**: Automatically adjusts `stoppingDistance` to match `repathTolerance`.

---

### 3. Service Dependencies

Ensures modern high-fidelity world services required by advanced scorers and squad controllers are present.

#### <a id="suppression-missing"></a>🟡 Missing SuppressionService (`suppression_missing`)
* **Problem**: An agent uses `SuppressionPressureScorerSO`, but no `SuppressionService` exists in the scene.
* **Impact**: The scorer cannot evaluate bullet fire vectors or incoming suppression intensity and awards 0 score.
* **⚡ Quick-Fix Available**: Instantly spawns a configured `[SuppressionService]` GameObject in the scene.

#### <a id="squad-coordinator-missing"></a>🟡 Missing SquadCoordinator (`squad_coordinator_missing`)
* **Problem**: An agent has a non-empty `SquadName` assigned, but no `SquadCoordinator` is present.
* **Impact**: Squad maneuvers (`SuppressAndFlank`, `BoundingOverwatch`), fireteam splitting, and shared threat memory cannot function.
* **⚡ Quick-Fix Available**: Instantly creates a `[SquadCoordinator]` manager in the scene.

#### <a id="threat-map-missing"></a>🟡 Missing ThreatMapService (`threat_map_missing`)
* **Problem**: Agents query threat heatmaps or future target velocity, but `ThreatMapService` is missing.
* **⚡ Quick-Fix Available**: Spawns the required service in the active scene.

---

### 4. Provider Dependencies

Validates that environment-dependent providers have corresponding authoring data in the scene.

#### <a id="prov-covernode-empty"></a>🔴 CoverNodeProvider With Zero Scene Nodes (`prov_covernode_empty`)
* **Problem**: An agent's settings includes `CoverNodeProviderSO`, but the scene contains 0 `CoverNode` components.
* **Impact**: The provider will find 0 candidate points, causing search starvation.
* **Fix**: Place `CoverNode` components on obstacles in your scene, or add an automatic provider like `AutomaticCoverFinderProviderSO` or `NavMeshRingProviderSO`.

#### <a id="prov-tacticalzone-empty"></a>🔴 TacticalZoneProvider With Zero Scene Zones (`prov_tacticalzone_empty`)
* **Problem**: An agent uses `TacticalZoneProviderSO`, but no `TacticalZone` volumes exist in the scene.
* **Impact**: Provider produces 0 candidate spots.
* **Fix**: Add a `TacticalZone` with a trigger collider to mark tactical combat zones.

---

### 5. Scorer Dependencies & Zero-Weight Checks

Detects dead scorers that waste CPU cycles without influencing AI behavior.

#### <a id="scorer-zero-weight"></a>💡 Zero Weight Scorer (`scorer_zero_weight`)
* **Problem**: A scorer has a `weight` of `0.0`.
* **Impact**: The scorer runs its evaluation algorithm every search cycle, but multiplies the result by zero, wasting CPU time.
* **⚡ Quick-Fix Available**: Sets weight to `1.0` or allows removing the unused scorer.

#### <a id="zone-scorer-no-zones"></a>🟡 ZoneControlStateScorer With Zero Scene Zones (`zone_scorer_no_zones`)
* **Problem**: `ZoneControlStateScorerSO` is configured, but there are no `TacticalZone` components in the scene.
* **Impact**: The scorer always returns a neutral default score.
* **Fix**: Author tactical zones or remove the scorer from settings.

---

### 6. Semantic Data Compatibility

Ensures spot providers produce the metadata needed by scorers and execution APIs.

#### <a id="stance-scorer-unsupported"></a>🟡 Stance Scorer On Untagged Providers (`stance_scorer_unsupported`)
* **Problem**: An agent uses `StanceMatchScorerSO` or `PosturePreferenceScorerSO`, but only uses providers that generate raw points without posture tags (`CoverPointFlags.CrouchCover` / `StandCover`).
* **Impact**: Spot evaluation cannot differentiate between low cover and high cover.
* **Fix**: Use `CoverNodeProviderSO` with authored metadata or `BehindObstacleProviderSO` with height detection enabled.

#### <a id="path-too-short"></a>🟡 Path Max Distance Smaller Than Search Radius (`path_too_short`)
* **Problem**: `pathMaxDistance` is set smaller than `searchRadius`.
* **Impact**: Valid cover spots discovered at the edge of the search radius will be discarded as "too far" during path evaluation.
* **⚡ Quick-Fix Available**: Sets `pathMaxDistance` to `searchRadius * 1.5f`.

---

### 7. Orphaned Scene Authoring

Identifies authoring components placed into the scene by level designers that are completely unused by active agents.

#### <a id="orphan-covernodes"></a>💡 Unused CoverNodes In Scene (`orphan_covernodes`)
* **Problem**: The scene contains `CoverNode` components, but no active agent has a `CoverNodeProviderSO` in its settings.
* **Impact**: Hand-placed cover nodes will be ignored; agents will only use procedural sampling.
* **Recommendation**: Add `CoverNodeProviderSO` to agent settings, or clean up unused nodes.

#### <a id="orphan-zones"></a>💡 Unused TacticalZones In Scene (`orphan_zones`)
* **Problem**: `TacticalZone` components are placed, but no agents query zones or use zone scorers.
* **Recommendation**: Add `ZoneControlStateScorerSO` to allow agents to favor friendly-controlled zones.

#### <a id="zone-col-not-trigger"></a>🟡 TacticalZone Collider Is Solid (`zone_col_not_trigger`)
* **Problem**: A `TacticalZone` GameObject has a Collider that does not have `isTrigger` enabled.
* **Impact**: The zone will physically block characters and physics projectiles instead of acting as an area detector.
* **⚡ Quick-Fix Available**: Checks `isTrigger = true` on the zone collider.

---

## ⚡ One-Click Auto-Fix Engine

The Validator includes an intelligent auto-repair system:

1. **Individual Quick-Fix (`⚡ Fix: ...`)**:
   * Located in the footer of any fixable issue card.
   * Resolves the specific issue for that object immediately.
2. **Auto-Fix All (`⚡ Auto-Fix All (X)`)**:
   * Located in the header toolbar.
   * Repaires all detected issues across all agents simultaneously.
3. **Full Undo/Redo Support**:
   * Every fix is registered through Unity's `Undo` system.
   * Press `Ctrl+Z` (or `Cmd+Z` on macOS) to instantly revert all changes if desired.

---

## 🛠️ Scripting & CI/CD Automated Validation

You can execute validation programmatically in unit tests, editor build pipelines, or pre-commit hooks to ensure broken scenes never make it into production builds:

```csharp
using UnityEngine;
using UnityEditor;
using MaharajaStudio.TacticalAI.Editor.Validation;

public static class BuildPreflightChecks
{
    [MenuItem("Tools/Build/Validate Active Scene")]
    public static bool ValidateSceneForBuild()
    {
        ValidationReport report = TacticalAIValidationScanner.ScanScene();

        Debug.Log($"Scan completed in {report.scanDurationMs:F2}ms with {report.totalErrors} error(s) and {report.totalWarnings} warning(s).");

        if (report.totalErrors > 0)
        {
            foreach (var item in report.items)
            {
                if (item.severity == ValidationSeverity.Error)
                {
                    Debug.LogError($"[Validation Failed] {item.title}: {item.description} (Target: {item.contextName})");
                }
            }
            return false;
        }

        return true;
    }
}
```

---

## 📚 Further Reading

* [Getting Started Guide](Getting-Started.md) — Step-by-step first agent setup.
* [Setup Guide for Designers](For_Designers/Setup_Guide.md) — Non-programmer setup workflows.
* [What's New in Tactical AI 3.0](Version_3/WhatsNew_v3.0.md) — Detailed release notes and API additions.
