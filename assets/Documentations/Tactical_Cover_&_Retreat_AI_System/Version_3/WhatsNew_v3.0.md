# Tactical AI 3.0: What's New & Release Notes

Tactical AI Version 3.0 represents a major evolutionary leap: bridging the gap between the **Search Phase** (choosing where to hide, introduced in v1 and expanded in v2/v2.5) and the **Execution Phase** (how agents actually behave, crouch, peek, flank, and coordinate once in cover).

---

## 🌟 Highlights of Version 3.0

```
                                       Tactical AI 3.0
         ┌───────────────────────────────────┼───────────────────────────────────┐
         ▼                                   ▼                                   ▼
 [ Combat & Locomotion Execution ]   [ Synchronized Squad Maneuvers ]    [ Environment & Agent Validator ]
 • DesiredStance & Auto Posture      • Dynamic Fireteam Splitting        • Automated Scene Diagnosis
 • TryGetBestPeekDirection           • Synchronized Squad Commands       • Smart Grouped View
 • Proactive Flank Warnings          • Shared Hivemind Threat Memory     • One-Click Auto-Fix All
 • Obstacle Vault / Mantle Checks    • 3 New Strategic Scorers           • Direct In-Editor Doc Links
```

---

## 1. ⚔️ TacticalAgent: Execution & Combat Query APIs

Previously, `TacticalAgent` focused on pathfinding to a chosen spot. Version 3.0 adds combat execution queries so your agents can dynamically react from within cover:

* **Stance Recommendation (`DesiredStance` & `OnStanceChangeRequired`)**: Automatically signals your animator whether the agent must crouch, stand, or is versatile based on `CoverPointFlags`.
* **Smart Peek Direction (`TryGetBestPeekDirection`)**: Evaluates whether left or right cover corners offer clear line-of-sight to the player without exposing the agent's core mass.
* **Proactive Flank Warnings (`IsFlanked` & `GetCoverFlankAngle`)**: Warns the AI when enemies cross its cover line (>90° angle), enabling smart scrambles before taking damage.
* **Obstacle Vaulting (`CanVaultCover`)**: Validates if low cover can be hopped over and computes the exact landing coordinate on the NavMesh.
* **Live Suppression Meter (`SuppressionLevel` & `IsSuppressed`)**: Real-time 0.0–1.0 agent suppression level with automatic incoming gunfire integration and decay.

---

## 2. 🛡️ SquadCoordinator: Synchronized Maneuvers & Fireteam Splitting

Building upon the squad formations and reservation system introduced in Version 2.0, Version 3.0 adds active tactical squad commands and dynamic fireteams:

* **Dynamic Fireteam Splitting (`AssignFireteams`)**: Automatically divides any squad into a base-of-fire suppression element and a flanking maneuver element.
* **Tactical Maneuver Orders (`ExecuteManeuver`)**: Issues synchronized squad commands:
  * `TacticalSquadManeuver.SuppressAndFlank`: Pincer attack where suppressors pin the target while flankers maneuver wide.
  * `TacticalSquadManeuver.BoundingOverwatch`: Alternating leap-frog advances.
  * `TacticalSquadManeuver.TacticalFallBack`: Coordinated emergency retreat.
  * `TacticalSquadManeuver.HoldPerimeter`: Fans out into defensive cover.
* **Shared Threat Memory (`BroadcastSquadThreat` & `GetSharedThreatPosition`)**: When a scout spots an enemy, the target coordinate is broadcasted across the squad.

---

## 3. 🎯 3 New Tactical Scorers

| Scorer | Category | Primary Role |
|---|---|---|
| **[`ZoneControlStateScorerSO`](Scorers/ZoneControlStateScorer.md)** | Strategic | Prioritizes spots based on whether their `TacticalZone` is `FriendlyControlled`, `Contested`, or `HostileControlled`. |
| **[`VaultOpportunityScorerSO`](Scorers/VaultOpportunityScorer.md)** | Offensive | Rewards vaultable cover for rushers, shotgunners, and aggressive flankers. |
| **[`SensoryTypeScorerSO`](Scorers/SensoryTypeScorer.md)** | Strategic | Granular sensory filtering (investigating gunshots vs. ignoring subtle footsteps). |

---

## 4. 🔍 Environment & Agent Validator Tool

Version 3.0 introduces a dedicated scene diagnostic and auto-repair window:

* **Instant Scene Scan (`TacticalAIValidatorWindow`)**: Analyzes scene geometry, NavMesh, agent configurations, service dependencies, dead scorers, and orphan authoring in milliseconds.
* **Smart Grouped View**: Aggregates duplicate issues across multiple agents into clean, actionable summary cards.
* **One-Click Auto-Fix All**: Safe undo-supported repairs for common misconfigurations (e.g. creating missing services, removing self-occluding agent layers from occluder masks, adjusting stopping distances).
* **Direct Documentation Links**: Every diagnostic card provides a `📖 Doc` button taking you directly to the relevant fix instructions.

📖 **Full Guide**: See **[Scene Validator (v3.0)](SceneValidator.md)** or **[Complete Scene Validator Guide](../SceneValidatorGuide.md)** for details on all 7 diagnostic categories and automated validation APIs.

---

## 🚀 Quick Integration: Coordinated Fire & Maneuver

```csharp
using UnityEngine;
using MaharajaStudio.TacticalAI;
using MaharajaStudio.TacticalAI.Helper;

public class SquadAssaultController : MonoBehaviour
{
    [SerializeField] private string squadName = "BravoTeam";
    [SerializeField] private Transform enemyTarget;

    public void OrderFlankAttack()
    {
        // Issue synchronized suppression and flank maneuver
        SquadCoordinator.Instance.ExecuteManeuver(
            squadName, 
            TacticalSquadManeuver.SuppressAndFlank, 
            enemyTarget
        );
    }
}
```
