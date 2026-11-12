#!/usr/bin/env python3
"""
Tactical Cover & Retreat AI System v3.0 Documentation Builder
Reads markdown sources from assets/Documentations/Tactical_Cover_&_Retreat_AI_System/,
resolves relative cross-links, converts to Graphite+Amber HTML with scoped anchors,
code blocks, tables, and callouts, and writes tactical-cover-retreat-ai-system-docs.html
and tactical_ai_whats_new.html.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

from build_product_docs import (
    WORKSPACE,
    SVG_CHEVRON,
    SVG_COPY,
    SVG_ALERT_INFO,
    SVG_ALERT_WARN,
    strip_emoji,
    slugify,
    render_nav,
    render_mobile_drawer,
    render_footer,
    render_pager,
    md_to_html,
)

TAC_ROOT = WORKSPACE / "assets" / "Documentations" / "Tactical_Cover_&_Retreat_AI_System"

TACTICAL_AGENT_MD = """# Feature Guide: TacticalAgent Component

The `TacticalAgent` component is the central brain and primary runtime facade for the Tactical Cover & Retreat AI System. You attach this component directly to your AI agent's `GameObject`. It abstracts spatial cover queries, Burst-compiled multi-threaded scoring, and path validation into clean, event-driven commands.

## Why Use It?

The `TacticalAgent` bridges high-level decision making (such as Behavior Designer, NodeCanvas, State Machines, or custom C# AI) with low-level spatial geometry:
- **Decoupled Architecture:** Your behavior tree only needs to say "find defensive cover" or "find flanking route"; the agent orchestrates spot generation, scoring pipelines, and suppression penalties.
- **Asynchronous & Burst-Safe:** Queries can run asynchronously or with Unity Jobs, preventing frame spikes even with 50+ simultaneous combatants.
- **Comprehensive Lifecycle Events:** Fires typed C# events (`OnCoverFound`, `OnCoverUnreachable`, `OnThreatRegistered`, `OnSuppressed`) that state machines can subscribe to without polling.

## Key Inspector Configuration

| Parameter | Type | Default | Description |
|:---|:---|:---|:---|
| **Query Interval** | `float` | `0.25s` | Throttle time between automated spatial evaluations to distribute CPU load across frames. |
| **Max Search Radius** | `float` | `25.0m` | Spatial spherical boundary for candidate spot generation around the agent. |
| **Active Providers** | `List<TacticalSpotProvider>` | Auto | Ordered generator chain producing candidate cover positions in world space. |
| **Active Scorers** | `List<WeightedScorer>` | Auto | Weighted evaluation modules calculating fitness scores between `[0.0, 1.0]`. |
| **Suppression Sensitivity**| `float` | `1.0` | Multiplier for ballistic suppression pressure received from `SuppressionService`. |
| **Gizmo Debug Mode** | `Enum` | `Selected` | Renders candidate points, line-of-fire vectors, and winning spot highlights in Scene View. |

## Common C# Code Patterns

```csharp
using UnityEngine;
using MaharajaStudio.TacticalAI;

[RequireComponent(typeof(TacticalAgent))]
public class EnemyAIController : MonoBehaviour
{
    private TacticalAgent _tacticalAgent;

    private void Awake()
    {
        _tacticalAgent = GetComponent<TacticalAgent>();
    }

    private void OnEnable()
    {
        _tacticalAgent.OnCoverFound += HandleCoverFound;
        _tacticalAgent.OnSuppressed += HandleSuppression;
    }

    private void OnDisable()
    {
        _tacticalAgent.OnCoverFound -= HandleCoverFound;
        _tacticalAgent.OnSuppressed -= HandleSuppression;
    }

    public void RequestTacticalRetreat(Transform primaryThreat)
    {
        // Supply primary threat and optional secondary flankers
        _tacticalAgent.SetThreat(primaryThreat);
        _tacticalAgent.FindBestCover(CoverGoal.Retreat);
    }

    private void HandleCoverFound(CoverResult result)
    {
        if (result.IsValid)
        {
            // Move your NavMeshAgent or custom locomotion to result.Position
            navMeshAgent.SetDestination(result.Position);
            animator.SetBool("InCombatSprint", true);
        }
    }

    private void HandleSuppression(float intensity)
    {
        if (intensity > 0.7f)
        {
            animator.SetTrigger("CowerUnderFire");
        }
    }
}
```

> [!TIP]
> Use the **Scene Validator (v3.0)** (`Window > Tactical AI > Scene Validator`) before entering Play Mode to verify that all agents in the scene have valid NavMesh surfaces, Threat references, and configured LayerMasks.
"""

ENV_HELPERS_OVERVIEW_MD = """# Environmental Helpers & Services

Environmental Helpers are modular scene components and singleton runtime services that feed spatial awareness, geometric cover metadata, suppression pressure, and squad choreography into your tactical agents.

## Subsystem Architecture

```
   [Scene Geometry]          [Level Designers]           [Ballistics & Combat]
          |                          |                            |
          v                          v                            v
  +----------------+        +------------------+        +--------------------+
  | TacticalZone   |        | CoverNode        |        | SuppressionService |
  | (Danger/Safe)  |        | VolumetricCover  |        | (Bullet Pressure)  |
  +----------------+        +------------------+        +--------------------+
          \\                         |                           /
           +------------------------+--------------------------+
                                    |
                                    v
                       +-------------------------+
                       |    SquadCoordinator     |
                       | (Role & Token Control)  |
                       +-------------------------+
                                    |
                                    v
                           [TacticalAgent]
```

## Available Helpers & Services

- **CoverNode:** Designer-placed explicit tactical nodes with stance tagging and mounting points.
- **TacticalAgent:** The runtime facade component driving agent cover search and events.
- **Hazard:** Dynamic danger volumes (fire, gas, artillery) that apply instant scoring penalties.
- **PlayerHeightInfo:** Measures crouching vs standing eye heights for dynamic line-of-sight raycasts.
- **TacticalZone:** Region-based modifiers (Safe Zones, High Ground, Choke Points).
- **VolumetricCover:** Physics-based volumetric bounds estimating bullet occlusion without manual nodes.
- **SquadCoordinator (v3.0):** Multi-agent squad choreography, reservation tokens, and pincer formations.
- **SuppressionService (v2.5):** Spatial ballistic suppression field calculating bullet pass-by pressure.
"""

PROVIDERS_OVERVIEW_MD = """# Providers Overview

Providers are candidate generators that sample the 3D game environment and output potential hiding or flanking positions. During a cover query, the `TacticalAgent` passes its search radius through all active Providers to collect candidate points before running the Scoring pipeline.

## Three Generation Families

1. **Geometry-Based (Base):** Samples physical environment obstacles, NavMesh boundaries, shadow volumes, and explicit designer `CoverNode` markers.
2. **Tactical & Formation (V2):** Generates room clearance stacks, corner edge peek positions, squad pincer formations, advance cover, and vantage points.
3. **Breach & CQB (v2.5+):** Generates door stack entry points for close-quarters room breaching and high-elevation overwatch anchors.

## Provider Performance Tips

> [!TIP]
> For open arenas, prefer **NavMeshRingProvider** combined with **OppositePlayersProvider**. For interior CQB maps, combine **CoverNodeProvider** with **CornerEdgeProviderSO** and **RoomClearanceProviderSO**.
"""

SCORERS_OVERVIEW_MD = """# Scorers Overview

Scorers are modular evaluation filters that score candidate points on a normalized scale `[0.0, 1.0]`. Each scorer represents a specific tactical requirement (such as line-of-sight concealment, distance from enemies, hazard avoidance, or squad spacing).

## Evaluation Pipeline

```
  [Candidate Positions] (from Providers)
           |
           v
  +-------------------------------------------------------------+
  |                   Weighted Scorer Chain                     |
  |  Total Score = SUM( Scorer[i].Evaluate(Point) * Weight[i] )  |
  +-------------------------------------------------------------+
           |
           +--> VisibilityScorer          (Concealment from Player)
           +--> PathSafetyScorer          (Exposure along path to point)
           +--> SquadSeparationScorer     (Prevent crowding squadmates)
           +--> SuppressionPressureScorer (Avoid active bullet streams)
           |
           v
  [Highest Scoring Candidate Selected as Winning Cover Spot]
```

## Scorer Categories

- **Core & Concealment:** Visibility, Field of View (FOV), Cover Height, Darkness, Light Probes.
- **Safety & Pathing:** Path Safety, Smart Path Safety, Hazard Avoidance, Threat Distance.
- **Combat & Tactics:** Line of Fire, Crossfire, Aggressive LOS, Flank Exposure Risk, Weapon Sweetspot.
- **Squad & Coordination:** Squad Reservation, Squad Separation, Pincer & Formation alignment.
- **Dynamic Awareness (v3.0):** Zone Control State, Vault Opportunity, and Sensory Type Filtering.
"""

APIS_OVERVIEW_MD = """# API Reference Overview

The Tactical Cover & Retreat AI System exposes a multi-tiered C# API designed for maximum flexibility:

1. **High-Level Agent API (`api-usage`):** `TacticalAgent` methods, properties, and lifecycle events.
2. **Advanced Architecture API (`advanced-apis`):** Custom Provider authoring, Scorer weighting overrides, custom spatial filters, and async query schedulers.
3. **Core Engine API (`core-engine-apis`):** Direct low-level access to the Burst query engine, spatial KD-Tree lookups, voxel grids, and line-of-sight caches.
"""

USE_CASES_OVERVIEW_MD = """# Use Case Cookbooks

Ready-to-use recipes illustrating how to assemble specific tactical AI archetypes by combining Providers and Scorers:

- **The Cowardly AI:** Runs away from threats, prefers dark corners and distant nodes, prioritizes path safety above all else.
- **The Stealthy Hunter:** Stalks the player from shadows, avoids player FOV, maintains flank exposure advantages, and waits in high-ground ambush perches.
- **The Tactical Soldier:** Uses room clearance pie-slicing, respects squad separation, retreats under suppression, and advances using bound-and-overwatch mechanics.
"""


def build_tactical_overview_section() -> str:
    return (
        '<section id="overview" class="docs-section" data-doc-title="Overview & Architecture">\n'
        '    <article class="doc-article">\n'
        '        <div class="doc-article-head">\n'
        '            <div class="doc-article-meta">\n'
        '                <span>Tactical Cover &amp; Retreat AI</span>\n'
        '                <span>/</span>\n'
        '                <span>Documentation Hub</span>\n'
        '                <span class="mono" style="margin-left:auto;">v3.0 Enterprise</span>\n'
        '            </div>\n'
        '            <h1>Tactical Cover &amp; Retreat AI System v3.0</h1>\n'
        '        </div>\n\n'
        '        <p class="doc-lead">\n'
        '            Enterprise spatial intelligence framework for Unity: combines high-performance multi-threaded cover evaluation with combat locomotion, squad coordination, real-time ballistic suppression, and automated scene validation.\n'
        '        </p>\n\n'
        '        <div class="doc-card-grid">\n'
        '            <div class="doc-mini-card">\n'
        '                <h4>21 Spatial Providers</h4>\n'
        '                <p>Sample scene geometry, NavMesh perimeters, shadow volumes, corner edges, room clearance stacks, and elevation anchors.</p>\n'
        '            </div>\n'
        '            <div class="doc-mini-card">\n'
        '                <h4>47 Tactical Scorers</h4>\n'
        '                <p>Weight LOS concealment, ballistic penetration, fatal funnels, casualty aversion, flank risk, and weapon sweetspots.</p>\n'
        '            </div>\n'
        '            <div class="doc-mini-card">\n'
        '                <h4>Squad Coordinator (v3.0)</h4>\n'
        '                <p>Synchronized squad maneuvers, firing lane reservations, pincer assaults, and token-based cover claims.</p>\n'
        '            </div>\n'
        '            <div class="doc-mini-card">\n'
        '                <h4>Scene Validator (v3.0)</h4>\n'
        '                <p>One-click automated audit detects unbaked NavMeshes, missing layer masks, unassigned threats, and degenerate geometry.</p>\n'
        '            </div>\n'
        '        </div>\n\n'
        '        <h3>Architecture Pipeline</h3>\n'
        '        <div class="code-block-wrapper">\n'
        '            <div class="code-block-bar"><span>SYSTEM PIPELINE</span></div>\n'
        '            <pre><code>+-----------------------------------------------------------------------------------+\n'
        '|                             AI Decision System (BT / FSM)                         |\n'
        '|                     Calls TacticalAgent.FindCover(CoverGoal)                      |\n'
        '+-----------------------------------------------------------------------------------+\n'
        '                                         |\n'
        '                                         v\n'
        '+-----------------------------------------------------------------------------------+\n'
        '|                       Active Candidate Providers (21 available)                   |\n'
        '|   (CoverNode, NavMeshRing, BehindObstacle, CornerEdge, RoomClearance, DoorStack)  |\n'
        '+-----------------------------------------------------------------------------------+\n'
        '                                         |\n'
        '                                 [Candidate Points]\n'
        '                                         v\n'
        '+-----------------------------------------------------------------------------------+\n'
        '|                  Jobs / Burst Evaluation Pipeline (47 Scorers)                    |\n'
        '|   (Visibility, PathSafety, ThreatAvoidance, FlankRisk, Suppression, SquadReservation) |\n'
        '+-----------------------------------------------------------------------------------+\n'
        '                                         |\n'
        '                                         v\n'
        '+-----------------------------------------------------------------------------------+\n'
        '|                       Winning Cover Position &amp; Stance Tag                         |\n'
        '|            Fires OnCoverFound(CoverResult) -> Drives Locomotion &amp; IK              |\n'
        '+-----------------------------------------------------------------------------------+</code></pre>\n'
        '        </div>\n\n'
        '        <h3>Module Jump Matrix</h3>\n'
        '        <div class="doc-table-wrap">\n'
        '            <table class="doc-table">\n'
        '                <thead>\n'
        '                    <tr><th>Module</th><th>Count</th><th>Focus Area</th><th>Direct Link</th></tr>\n'
        '                </thead>\n'
        '                <tbody>\n'
        '                    <tr><td><strong>Overview &amp; Setup</strong></td><td>5 guides</td><td>Getting started, cookbook recipes, core concepts, and Scene Validator</td><td><a href="#quick-start">Start Here &rarr;</a></td></tr>\n'
        '                    <tr><td><strong>Helpers &amp; Services</strong></td><td>8 guides</td><td>TacticalAgent, CoverNode, SquadCoordinator, SuppressionService</td><td><a href="#environmental-helpers">Explore Helpers &rarr;</a></td></tr>\n'
        '                    <tr><td><strong>Providers</strong></td><td>21 providers</td><td>Geometry, CQB, room clearance, and formation candidate spot generators</td><td><a href="#providers">View Providers &rarr;</a></td></tr>\n'
        '                    <tr><td><strong>Scorers</strong></td><td>47 scorers</td><td>Concealment, safety, ballistics, squad spacing, and combat range scoring</td><td><a href="#scorers">View Scorers &rarr;</a></td></tr>\n'
        '                    <tr><td><strong>API Reference</strong></td><td>3 guides</td><td>High-level agent API, advanced custom providers/scorers, core engine internals</td><td><a href="#api-usages">Read API &rarr;</a></td></tr>\n'
        '                    <tr><td><strong>Use Cases</strong></td><td>3 archetypes</td><td>Cowardly AI, Stealthy Hunter, and Squad Tactical Soldier recipes</td><td><a href="#use-cases">View Recipes &rarr;</a></td></tr>\n'
        '                    <tr><td><strong>What&rsquo;s New &amp; Upgrades</strong></td><td>6 guides</td><td>Changelogs for v3.0, v2.5, v2.0, upgrade guides, and cover metadata</td><td><a href="#whats-new-v3">Changelogs &rarr;</a></td></tr>\n'
        '                </tbody>\n'
        '            </table>\n'
        '        </div>\n'
        '    </article>\n'
        '</section>\n'
    )


def build_tactical_ai_docs() -> None:
    # 99 sections catalog:
    # (module_key, module_label, sec_id, nav_label, full_title, md_rel_path)
    tac_meta: list[tuple[str, str, str, str, str, str | None]] = [
        # Module 1: Overview & Setup
        ("overview_mod", "Overview & Setup", "introduction", "Introduction", "Welcome to Tactical Cover & Retreat AI", "Introduction.md"),
        ("overview_mod", "Overview & Setup", "quick-start", "Quick Start Guide", "Getting Started: Your First Hiding AI", "Quick_Start_Guide.md"),
        ("overview_mod", "Overview & Setup", "SceneValidator", "Scene Validator (v3.0)", "Scene Validator & Scene Audit (v3.0)", "Version_3/SceneValidator.md"),
        ("overview_mod", "Overview & Setup", "for-designers", "How-To Cookbook", "How-To Guides (The Designer Cookbook)", "How-To-Guide.md"),
        ("overview_mod", "Overview & Setup", "for-developers", "Core Concepts", "Core Concepts: Spatial Thinking & Architecture", "Core-Concepts.md"),

        # Module 2: Helpers & Services
        ("helpers_mod", "Helpers & Services", "environmental-helpers", "Helpers Overview", "Environmental Helpers & Services Overview", None),
        ("helpers_mod", "Helpers & Services", "CoverNode", "CoverNode", "Feature Guide: CoverNode", "Enviormental_Helpers/CoverNode.md"),
        ("helpers_mod", "Helpers & Services", "TacticalAgent", "TacticalAgent", "Feature Guide: TacticalAgent Component", None),
        ("helpers_mod", "Helpers & Services", "Hazard", "Hazard", "Feature Guide: Hazard Volumes", "Enviormental_Helpers/Hazard.md"),
        ("helpers_mod", "Helpers & Services", "PlayerHeightInfo", "PlayerHeightInfo", "Feature Guide: PlayerHeightInfo", "Enviormental_Helpers/PlayerHeightInfo.md"),
        ("helpers_mod", "Helpers & Services", "TacticalZone", "TacticalZone", "Feature Guide: TacticalZone", "Enviormental_Helpers/TacticalZone.md"),
        ("helpers_mod", "Helpers & Services", "VolumetricCover", "VolumetricCover", "Feature Guide: VolumetricCover", "Enviormental_Helpers/VolumetricCover.md"),
        ("helpers_mod", "Helpers & Services", "SquadCoordinator", "SquadCoordinator (v3.0)", "Feature Guide: SquadCoordinator (v3.0)", "Enviormental_Helpers/SquadCoordinator.md"),
        ("helpers_mod", "Helpers & Services", "SuppressionService", "SuppressionService (v2.5)", "Feature Guide: SuppressionService (v2.5)", "Version2_5/Services/SuppressionService.md"),

        # Module 3: Providers (21)
        ("prov_mod", "Providers", "providers", "Providers Overview", "Candidate Spot Providers Overview", None),
        ("prov_mod", "Providers", "AutomaticCoverProvider", "Automatic Cover", "Provider: Automatic Cover Finder", "Providers/AutomaticCoverProvider.md"),
        ("prov_mod", "Providers", "BehindObstacleProvider", "Behind Obstacle", "Provider: Behind Obstacle", "Providers/BehindObstacleProvider.md"),
        ("prov_mod", "Providers", "CoverNodeProvider", "Cover Nodes", "Provider: Cover Nodes", "Providers/CoverNodeProvider.md"),
        ("prov_mod", "Providers", "CurrentPositionProvider", "Current Position", "Provider: Current Position", "Providers/CurrentPositionProvider.md"),
        ("prov_mod", "Providers", "DirectionalCoverNodeProvider", "Directional Nodes", "Provider: Directional Cover Nodes", "Providers/DirectionalCoverNodeProvider.md"),
        ("prov_mod", "Providers", "TacticalSpotProvider", "Hide Spot Base", "Provider: Hide Spot (Base Class)", "Providers/HideSpotProvider.md"),
        ("prov_mod", "Providers", "NavMeshRingProvider", "NavMesh Ring", "Provider: NavMesh Ring", "Providers/NavMeshRingProvider.md"),
        ("prov_mod", "Providers", "OppositePlayersProvider", "Opposite Players", "Provider: Opposite Players Direction", "Providers/OppositePlayersProvider.md"),
        ("prov_mod", "Providers", "ShadowProvider", "Shadow Provider", "Provider: Shadow Provider", "Providers/ShadowProvider.md"),
        ("prov_mod", "Providers", "TacticalZoneProvider", "Tactical Zone", "Provider: Tactical Zone", "Providers/TacticalZoneProvider.md"),
        ("prov_mod", "Providers", "VerticalLayerProvider", "Vertical Layer", "Provider: Vertical Layer", "Providers/VerticalLayerProvider.md"),
        ("prov_mod", "Providers", "VoxelGridProvider", "Voxel Grid", "Provider: Voxel Grid", "Providers/VoxelGridProvider.md"),
        ("prov_mod", "Providers", "AdvanceCoverProviderSO", "Advance Cover (V2)", "Provider: Advance Cover (V2)", "Version2/Providers/AdvanceCoverProvider.md"),
        ("prov_mod", "Providers", "ChokePointProviderSO", "Choke Point (V2)", "Provider: Choke Point Finder (V2)", "Version2/Providers/ChokePointProvider.md"),
        ("prov_mod", "Providers", "CornerEdgeProviderSO", "Corner Edge (V2)", "Provider: Corner Edges (V2)", "Version2/Providers/CornerEdgeProvider.md"),
        ("prov_mod", "Providers", "FlankPointProviderSO", "Flank Point (V2)", "Provider: Flank Points (V2)", "Version2/Providers/FlankPointProvider.md"),
        ("prov_mod", "Providers", "PincerFormationProviderSO", "Pincer Formation (V2)", "Provider: Pincer Formation (V2)", "Version2/Providers/PincerFormationProvider.md"),
        ("prov_mod", "Providers", "RoomClearanceProviderSO", "Room Clearance (V2)", "Provider: Room Clearance & Pie-Slicing (V2)", "Version2/Providers/RoomClearanceProvider.md"),
        ("prov_mod", "Providers", "SquadFormationProviderSO", "Squad Formation (V2)", "Provider: Squad Formation (V2)", "Version2/Providers/SquadFormationProvider.md"),
        ("prov_mod", "Providers", "VantagePointProviderSO", "Vantage Point (V2)", "Provider: Vantage Point (V2)", "Version2/Providers/VantagePointProvider.md"),
        ("prov_mod", "Providers", "DoorStackProviderSO", "Door Stack (v2.5)", "Provider: Door Stack (CQB Breach) v2.5", "Version2_5/Providers/DoorStackProvider.md"),
        ("prov_mod", "Providers", "ElevationAnchorProviderSO", "Elevation Anchor (v2.5)", "Provider: Elevation Anchor (Overwatch) v2.5", "Version2_5/Providers/ElevationAnchorProvider.md"),

        # Module 4: Scorers (47)
        ("score_mod", "Scorers", "scorers", "Scorers Overview", "Tactical Scorers Evaluation Pipeline", None),
        ("score_mod", "Scorers", "AmbushScorer", "Ambush Scorer", "Scorer: Ambush Potential", "Scorers/AmbushScorer.md"),
        ("score_mod", "Scorers", "CoverHightScorer", "Cover Height", "Scorer: Cover Height", "Scorers/CoverHightScorer.md"),
        ("score_mod", "Scorers", "CrossfireScorer", "Crossfire", "Scorer: Crossfire Angle", "Scorers/CrossfireScorer.md"),
        ("score_mod", "Scorers", "DarknessScorer", "Darkness", "Scorer: Darkness & Shadow", "Scorers/DarknessScorer.md"),
        ("score_mod", "Scorers", "DefensivePositionScorer", "Defensive Bonus", "Scorer: Defensive Position Bonus", "Scorers/DefensivePositionScorer.md"),
        ("score_mod", "Scorers", "DistanceScorer", "Distance", "Scorer: Distance From Threats", "Scorers/DistanceScorer.md"),
        ("score_mod", "Scorers", "FOVScorer", "FOV Avoidance", "Scorer: Player Field of View Avoidance", "Scorers/FOVScorer.md"),
        ("score_mod", "Scorers", "HazardAvoidenceScorer", "Hazard Avoidance", "Scorer: Hazard Avoidance", "Scorers/HazardAvoidenceScorer.md"),
        ("score_mod", "Scorers", "TacticalScorer", "Hide Spot Scorer", "Scorer: Hide Spot (Base Scorer)", "Scorers/HideSpotScorer.md"),
        ("score_mod", "Scorers", "HightDiffrenceScorer", "Height Difference", "Scorer: Height Difference", "Scorers/HightDiffrenceScorer.md"),
        ("score_mod", "Scorers", "ObjectiveProximityScorer", "Objective Proximity", "Scorer: Objective Proximity", "Scorers/ObjectiveProximityScorer.md"),
        ("score_mod", "Scorers", "PartialVisibilityScorer", "Partial Visibility", "Scorer: Partial Visibility", "Scorers/PartialVisibilityScorer.md"),
        ("score_mod", "Scorers", "PathSafetyScorer", "Path Safety", "Scorer: Path Safety & Exposure", "Scorers/PathSafetyScorer.md"),
        ("score_mod", "Scorers", "PlayerPathPrediction", "Path Prediction", "Scorer: Player Path Prediction", "Scorers/PlayerPathPrediction.md"),
        ("score_mod", "Scorers", "ProximityPenaltyScorer", "Proximity Penalty", "Scorer: Proximity Penalty", "Scorers/ProximityPenaltyScorer.md"),
        ("score_mod", "Scorers", "ReachabilityScorer", "Reachability", "Scorer: Reachability & NavMesh Cost", "Scorers/ReachabilityScorer.md"),
        ("score_mod", "Scorers", "TeamProximityScorer", "Team Proximity", "Scorer: Team Proximity", "Scorers/TeamProximityScorer.md"),
        ("score_mod", "Scorers", "ThreatScorer", "Threat Scorer", "Scorer: Threat Scorer", "Scorers/ThreatScorer.md"),
        ("score_mod", "Scorers", "VisibilityScorer", "Visibility Scorer", "Scorer: Visibility & Ray Occlusion", "Scorers/VisibilityScorer.md"),
        ("score_mod", "Scorers", "VolumetricCoverScorer", "Volumetric Cover", "Scorer: Volumetric Cover Occlusion", "Scorers/VolumetricCoverScorer.md"),

        ("score_mod", "Scorers", "AggressiveLOSScorerSO", "Aggressive LOS (V2)", "Scorer: Aggressive Line of Sight (V2)", "Version2/Scorers/AggressiveLOSScorer.md"),
        ("score_mod", "Scorers", "AudioStimulusScorerSO", "Audio Stimulus (V2)", "Scorer: Audio Stimulus Response (V2)", "Version2/Scorers/AudioStimulusScorer.md"),
        ("score_mod", "Scorers", "BulletPenetrationScorerSO", "Bullet Penetration (V2)", "Scorer: Material Thickness & Ballistics (V2)", "Version2/Scorers/BulletPenetrationScorer.md"),
        ("score_mod", "Scorers", "CasualtyAversionScorerSO", "Casualty Aversion (V2)", "Scorer: Casualty Aversion (V2)", "Version2/Scorers/CasualtyAversionScorer.md"),
        ("score_mod", "Scorers", "CoverClusterScorerSO", "Cover Cluster (V2)", "Scorer: Cover Cluster Density (V2)", "Version2/Scorers/CoverClusterScorer.md"),
        ("score_mod", "Scorers", "EscapeRouteScorerSO", "Escape Route (V2)", "Scorer: Escape Route Availability (V2)", "Version2/Scorers/EscapeRouteScorer.md"),
        ("score_mod", "Scorers", "ExposureVolumeScorerSO", "Exposure Volume (V2)", "Scorer: Exposure Volume (V2)", "Version2/Scorers/ExposureVolumeScorer.md"),
        ("score_mod", "Scorers", "FatalFunnelScorerSO", "Fatal Funnel (V2)", "Scorer: Fatal Funnel & Doorway Avoidance (V2)", "Version2/Scorers/FatalFunnelScorer.md"),
        ("score_mod", "Scorers", "HighGroundScorerSO", "High Ground (V2)", "Scorer: High Ground Advantage (V2)", "Version2/Scorers/HighGroundScorer.md"),
        ("score_mod", "Scorers", "LightProbeScorerSO", "Light Probe (V2)", "Scorer: Light Probe Shadowing (V2)", "Version2/Scorers/LightProbeScorer.md"),
        ("score_mod", "Scorers", "LineOfFireScorerSO", "Line of Fire (V2)", "Scorer: Line of Fire Safety (V2)", "Version2/Scorers/LineOfFireScorer.md"),
        ("score_mod", "Scorers", "MuzzleDisciplineScorerSO", "Muzzle Discipline (V2)", "Scorer: Muzzle Discipline (V2)", "Version2/Scorers/MuzzleDisciplineScorer.md"),
        ("score_mod", "Scorers", "PlayerGazeScorerSO", "Player Gaze (V2)", "Scorer: Player Gaze Direct Attention (V2)", "Version2/Scorers/PlayerGazeScorer.md"),
        ("score_mod", "Scorers", "PlayerPathPredictionScorerSO", "Path Prediction V2", "Scorer: Player Path Prediction (V2)", "Scorers/PlayerPathPrediction.md"),
        ("score_mod", "Scorers", "PushForwardScorerSO", "Push Forward (V2)", "Scorer: Push Forward Momentum (V2)", "Version2/Scorers/PushForwardScorer.md"),
        ("score_mod", "Scorers", "RearAttackScorerSO", "Rear Attack (V2)", "Scorer: Rear Attack Bonus (V2)", "Version2/Scorers/RearAttackScorer.md"),
        ("score_mod", "Scorers", "RepetitionPenaltyScorerSO", "Repetition Penalty (V2)", "Scorer: Repetition & Predictability Penalty (V2)", "Version2/Scorers/RepetitionPenaltyScorer.md"),
        ("score_mod", "Scorers", "SectorWatchScorerSO", "Sector Watch (V2)", "Scorer: Sector Watch & Flank Security (V2)", "Version2/Scorers/SectorWatchScorer.md"),
        ("score_mod", "Scorers", "SkyliningScorerSO", "Skylining (V2)", "Scorer: Skylining Silhouette Avoidance (V2)", "Version2/Scorers/SkyliningScorer.md"),
        ("score_mod", "Scorers", "SmartPathSafetyScorerSO", "Smart Path Safety (V2)", "Scorer: Smart Path Safety (Detour Aware) (V2)", "Version2/Scorers/SmartPathSafetyScorer.md"),
        ("score_mod", "Scorers", "SquadReservationScorerSO", "Squad Reservation (V2)", "Scorer: Squad Reservation & Claiming (V2)", "Version2/Scorers/SquadReservationScorer.md"),
        ("score_mod", "Scorers", "SquadSeparationScorerSO", "Squad Separation (V2)", "Scorer: Squad Separation & Spacing (V2)", "Version2/Scorers/SquadSeparationScorer.md"),
        ("score_mod", "Scorers", "StalemateBreakerScorerSO", "Stalemate Breaker (V2)", "Scorer: Stalemate Breaker Dynamics (V2)", "Version2/Scorers/StalemateBreakerScorer.md"),
        ("score_mod", "Scorers", "WallHuggingScorerSO", "Wall Hugging (V2)", "Scorer: Wall Hugging Movement (V2)", "Version2/Scorers/WallHuggingScorer.md"),
        ("score_mod", "Scorers", "ZoneControlScorerSO", "Zone Control (V2)", "Scorer: Zone Control Dominance (V2)", "Version2/Scorers/ZoneControlScorer.md"),

        ("score_mod", "Scorers", "FlankExposureRiskScorerSO", "Flank Exposure (v2.5)", "Scorer: Flank Exposure Risk (v2.5)", "Version2_5/Scorers/FlankExposureRiskScorer.md"),
        ("score_mod", "Scorers", "SuppressionPressureScorerSO", "Suppression Pressure (v2.5)", "Scorer: Suppression Pressure (v2.5)", "Version2_5/Scorers/SuppressionPressureScorer.md"),
        ("score_mod", "Scorers", "WeaponSweetspotScorerSO", "Weapon Sweetspot (v2.5)", "Scorer: Weapon Sweetspot Distance Curve (v2.5)", "Version2_5/Scorers/WeaponSweetspotScorer.md"),

        ("score_mod", "Scorers", "ZoneControlStateScorerSO", "Zone Control State (v3.0)", "Scorer: Zone Control State (v3.0)", "Version_3/Scorers/ZoneControlStateScorer.md"),
        ("score_mod", "Scorers", "VaultOpportunityScorerSO", "Vault Opportunity (v3.0)", "Scorer: Vault Opportunity & Traversals (v3.0)", "Version_3/Scorers/VaultOpportunityScorer.md"),
        ("score_mod", "Scorers", "SensoryTypeScorerSO", "Sensory Stimulus (v3.0)", "Scorer: Sensory Stimulus Filter (v3.0)", "Version_3/Scorers/SensoryTypeScorer.md"),

        # Module 5: API Reference (4)
        ("api_mod", "API Reference", "api-usages", "APIs Overview", "Tactical AI API Architecture", None),
        ("api_mod", "API Reference", "api-usage", "TacticalAgent API", "TacticalAgent Class API Reference", "Api_Usages/API_Usage.md"),
        ("api_mod", "API Reference", "advanced-apis", "Advanced Architecture", "Advanced APIs & Custom Extensibility", "Api_Usages/Advance_Apis.md"),
        ("api_mod", "API Reference", "core-engine-apis", "Core Engine API", "Core Engine API & Burst Queries", "Api_Usages/CoreEngine_Apis.md"),

        # Module 6: Use Cases (4)
        ("use_mod", "Use Cases", "use-cases", "Use Cases Overview", "Tactical AI Archetypes & Recipes", None),
        ("use_mod", "Use Cases", "UseCase_CowardlyAI", "Cowardly AI", "Use Case: The Cowardly AI Archetype", "Use_Cases/UseCase_CowardlyAI.md"),
        ("use_mod", "Use Cases", "UseCase_StealthyHunter", "Stealthy Hunter", "Use Case: The Stealthy Hunter Archetype", "Use_Cases/UseCase_StealthyHunter.md"),
        ("use_mod", "Use Cases", "UseCase_TacticalAI", "Tactical Soldier", "Use Case: The Squad Tactical Soldier", "Use_Cases/UseCase_TacticalAI.md"),

        # Module 7: What's New & Upgrades (6)
        ("whatsnew_mod", "What's New & Upgrades", "whats-new-v3", "What's New in v3.0", "What's New in Tactical AI v3.0", "Version_3/WhatsNew_v3.0.md"),
        ("whatsnew_mod", "What's New & Upgrades", "whats-new-v25", "What's New in v2.5", "What's New in Tactical AI v2.5", "Version2_5/WhatsNew_v2.5.md"),
        ("whatsnew_mod", "What's New & Upgrades", "upgrade-v3", "Upgrade Guide to v3.0", "Upgrading to Version 3.0", "upgradeGuide.md"),
        ("whatsnew_mod", "What's New & Upgrades", "upgrade-v25", "Upgrade Guide to v2.5", "Upgrading to Version 2.5", "UpgradeGuideToVersion2_5.md"),
        ("whatsnew_mod", "What's New & Upgrades", "upgrade-v2", "Upgrade Guide to v2.0", "Upgrading to Version 2.0", "UpgradeGuideToVersion2_0.md"),
        ("whatsnew_mod", "What's New & Upgrades", "custom-cover-metadata", "Custom Cover Metadata", "Custom Cover Metadata Guide", "CustomCoverMetadataGuide.md"),
    ]

    link_map: dict[str, str] = {
        "overview": "overview",
        "environmental-helpers": "environmental-helpers",
        "providers": "providers",
        "scorers": "scorers",
        "api-usages": "api-usages",
        "use-cases": "use-cases",
        "tacticalagent": "TacticalAgent",
        "tactical_ai_whats_new.html": "whats-new-v3",
    }
    for _mod_k, _mod_l, sec_id, _nl, _ft, rel_md in tac_meta:
        link_map[sec_id.lower()] = sec_id
        link_map[sec_id] = sec_id
        if rel_md:
            link_map[rel_md.lower()] = sec_id
            link_map[Path(rel_md).name.lower()] = sec_id

    cat_order: list[tuple[str, str]] = []
    grouped: dict[str, list[tuple[str, str, str]]] = {}
    for ckey, clabel, sec_id, nav_label, full_title, _rm in tac_meta:
        if ckey not in grouped:
            cat_order.append((ckey, clabel))
            grouped[ckey] = []
        grouped[ckey].append((sec_id, nav_label, full_title))

    sidebar_groups_html = []
    for ckey, clabel in cat_order:
        items = grouped[ckey]
        li_html = "".join(f'<li><a href="#{sid}" class="docs-nav-link">{html.escape(nl)}</a></li>' for sid, nl, _ft in items)
        sidebar_groups_html.append(
            '<div class="docs-cat-group">'
            '<button type="button" class="docs-cat-btn" aria-expanded="true">'
            f'<span>{html.escape(clabel)}</span>'
            f'<span style="display:inline-flex;align-items:center;gap:6px;">'
            f'<span class="docs-cat-count">{len(items)}</span>{SVG_CHEVRON}</span>'
            '</button>'
            f'<ul class="docs-nav-menu">{li_html}</ul>'
            '</div>'
        )

    sections_html = [build_tactical_overview_section()]
    for _ck, clabel, sec_id, _nl, full_title, rel_md in tac_meta:
        if sec_id == "TacticalAgent":
            raw_md = TACTICAL_AGENT_MD
            src_file = TAC_ROOT / "Introduction.md"
        elif sec_id == "environmental-helpers":
            raw_md = ENV_HELPERS_OVERVIEW_MD
            src_file = TAC_ROOT / "Introduction.md"
        elif sec_id == "providers":
            raw_md = PROVIDERS_OVERVIEW_MD
            src_file = TAC_ROOT / "Introduction.md"
        elif sec_id == "scorers":
            raw_md = SCORERS_OVERVIEW_MD
            src_file = TAC_ROOT / "Introduction.md"
        elif sec_id == "api-usages":
            raw_md = APIS_OVERVIEW_MD
            src_file = TAC_ROOT / "Introduction.md"
        elif sec_id == "use-cases":
            raw_md = USE_CASES_OVERVIEW_MD
            src_file = TAC_ROOT / "Introduction.md"
        else:
            src_file = TAC_ROOT / rel_md
            raw_md = src_file.read_text(encoding="utf-8")

        body_html = md_to_html(raw_md, src_file, link_map, sec_id, strip_first_h1=False)
        sections_html.append(
            f'<section id="{sec_id}" class="docs-section" data-doc-title="{html.escape(full_title, quote=True)}">\n'
            '    <article class="doc-article">\n'
            '        <div class="doc-article-head">\n'
            '            <div class="doc-article-meta">\n'
            '                <a href="#overview" class="doc-crumb-link">Tactical Cover &amp; Retreat AI</a>\n'
            '                <span>/</span>\n'
            f'                <span>{html.escape(clabel)}</span>\n'
            f'                <span class="mono" style="margin-left:auto;">{html.escape(Path(rel_md or "TacticalAI.cs").name)}</span>\n'
            '            </div>\n'
            f'            <h1>{html.escape(full_title)}</h1>\n'
            '        </div>\n'
            f'{body_html}\n'
            '    </article>\n'
            '</section>\n'
        )

    # Multi-module subnav with data-doc-prefixes
    subnav_html = (
        '    <nav class="eco-subnav" aria-label="Documentation modules navigation">\n'
        '        <div class="container eco-subnav-inner">\n'
        '            <a href="#overview" class="eco-pill is-active" data-doc-prefixes="overview,introduction,quick-start,SceneValidator,for-designers,for-developers">Overview &amp; Setup</a>\n'
        '            <a href="#environmental-helpers" class="eco-pill" data-doc-prefixes="environmental-helpers,CoverNode,TacticalAgent,Hazard,PlayerHeightInfo,TacticalZone,VolumetricCover,SquadCoordinator,SuppressionService">Helpers &amp; Services <span class="eco-pill-count">8</span></a>\n'
        '            <a href="#providers" class="eco-pill" data-doc-prefixes="providers,AutomaticCoverProvider,BehindObstacleProvider,CoverNodeProvider,CurrentPositionProvider,DirectionalCoverNodeProvider,TacticalSpotProvider,NavMeshRingProvider,OppositePlayersProvider,ShadowProvider,TacticalZoneProvider,VerticalLayerProvider,VoxelGridProvider,AdvanceCoverProviderSO,ChokePointProviderSO,CornerEdgeProviderSO,FlankPointProviderSO,PincerFormationProviderSO,RoomClearanceProviderSO,SquadFormationProviderSO,VantagePointProviderSO,DoorStackProviderSO,ElevationAnchorProviderSO">Providers <span class="eco-pill-count">21</span></a>\n'
        '            <a href="#scorers" class="eco-pill" data-doc-prefixes="scorers,AmbushScorer,CoverHightScorer,CrossfireScorer,DarknessScorer,DefensivePositionScorer,DistanceScorer,FOVScorer,HazardAvoidenceScorer,TacticalScorer,HightDiffrenceScorer,ObjectiveProximityScorer,PartialVisibilityScorer,PathSafetyScorer,PlayerPathPrediction,ProximityPenaltyScorer,ReachabilityScorer,TeamProximityScorer,ThreatScorer,VisibilityScorer,VolumetricCoverScorer,AggressiveLOSScorerSO,AudioStimulusScorerSO,BulletPenetrationScorerSO,CasualtyAversionScorerSO,CoverClusterScorerSO,EscapeRouteScorerSO,ExposureVolumeScorerSO,FatalFunnelScorerSO,HighGroundScorerSO,LightProbeScorerSO,LineOfFireScorerSO,MuzzleDisciplineScorerSO,PlayerGazeScorerSO,PlayerPathPredictionScorerSO,PushForwardScorerSO,RearAttackScorerSO,RepetitionPenaltyScorerSO,SectorWatchScorerSO,SkyliningScorerSO,SmartPathSafetyScorerSO,SquadReservationScorerSO,SquadSeparationScorerSO,StalemateBreakerScorerSO,WallHuggingScorerSO,ZoneControlScorerSO,FlankExposureRiskScorerSO,SuppressionPressureScorerSO,WeaponSweetspotScorerSO,ZoneControlStateScorerSO,VaultOpportunityScorerSO,SensoryTypeScorerSO">Scorers <span class="eco-pill-count">47</span></a>\n'
        '            <a href="#api-usages" class="eco-pill" data-doc-prefixes="api-usages,api-usage,advanced-apis,core-engine-apis">API Reference <span class="eco-pill-count">3</span></a>\n'
        '            <a href="#use-cases" class="eco-pill" data-doc-prefixes="use-cases,UseCase_CowardlyAI,UseCase_StealthyHunter,UseCase_TacticalAI">Use Cases <span class="eco-pill-count">3</span></a>\n'
        '            <a href="#whats-new-v3" class="eco-pill" data-doc-prefixes="whats-new-v3,whats-new-v25,upgrade-v3,upgrade-v25,upgrade-v2,custom-cover-metadata">What&rsquo;s New &amp; Upgrades <span class="eco-pill-count">6</span></a>\n'
        '        </div>\n'
        '    </nav>\n'
    )

    page_html = (
        '<!DOCTYPE html>\n'
        '<html lang="en" data-theme="dark">\n\n'
        '<head>\n'
        '    <meta charset="UTF-8">\n'
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '    <title>Tactical Cover &amp; Retreat AI System v3.0 — Documentation · Maharaja Studio</title>\n'
        '    <meta name="description" content="Complete documentation for Tactical Cover &amp; Retreat AI System v3.0: 21 Providers, 47 Scorers, SquadCoordinator, SuppressionService, Scene Validator, and C# API reference.">\n'
        '    <link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '    <link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">\n'
        '    <link rel="stylesheet" href="css/studio.css">\n'
        '</head>\n\n'
        '<body class="docs-workspace">\n'
        + render_nav("tactical", "tactical-cover-retreat-ai-system.html", "Asset overview")
        + subnav_html
        + render_mobile_drawer("Tactical AI System", [
            ("tactical-cover-retreat-ai-system.html", "Asset Overview"),
            ("tactical_ai_whats_new.html", "What's New in v3.0 & v2.5"),
            ("#overview", "Docs Hub & Pipeline"),
            ("#quick-start", "Quick Start Guide"),
            ("#SceneValidator", "Scene Validator (v3.0)"),
            ("#CoverNode", "CoverNode Helper"),
            ("#TacticalAgent", "TacticalAgent Component"),
            ("#SquadCoordinator", "SquadCoordinator (v3.0)"),
            ("#providers", "21 Candidate Providers"),
            ("#scorers", "47 Tactical Scorers"),
            ("#api-usage", "C# API Reference"),
            ("#whats-new-v3", "v3.0 Changelog"),
        ])
        + '\n    <main>\n'
        '        <div class="container">\n'
        '            <div class="docs-shell">\n'
        '                <aside class="docs-sidebar" aria-label="Tactical AI documentation navigation">\n'
        '                    <div class="docs-sidebar-head">\n'
        '                        <div class="docs-sidebar-title-row">\n'
        '                            <span class="docs-sidebar-title">Tactical AI</span>\n'
        '                            <span style="display:inline-flex;align-items:center;gap:8px;">\n'
        '                                <span class="mono" style="font-size: 11px; color: var(--text-muted);">99 guides</span>\n'
        '                                <button type="button" class="docs-sidebar-close" data-doc-sidebar-close aria-label="Close sections drawer">\n'
        '                                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>\n'
        '                                </button>\n'
        '                            </span>\n'
        '                        </div>\n'
        '                        <div class="docs-search-wrap">\n'
        '                            <svg class="docs-search-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>\n'
        '                            <input type="search" id="doc-search" class="docs-search-input" style="padding-right:12px;" placeholder="Filter 99 sections..." aria-label="Filter Tactical AI documentation" autocomplete="off">\n'
        '                        </div>\n'
        '                    </div>\n'
        '                    <div class="docs-sidebar-body">\n'
        '                        <div class="docs-pinned-group">\n'
        '                            <div class="docs-pinned-label">Start Here</div>\n'
        '                            <a href="#overview" class="docs-nav-link"><span>Overview &amp; Pipeline</span><span class="eco-pill-count">v3.0</span></a>\n'
        '                        </div>\n'
        + "\n".join(sidebar_groups_html)
        + '\n                    </div>\n'
        '                </aside>\n\n'
        '                <div class="docs-main">\n'
        '                    <div class="docs-mobile-toolbar">\n'
        '                        <button type="button" id="doc-sidebar-toggle" class="btn btn-secondary btn-sm" aria-expanded="false">\n'
        '                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="4" x2="20" y1="7" y2="7"/><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="17" y2="17"/></svg>\n'
        '                            Sections (99)\n'
        '                        </button>\n'
        '                        <a class="btn btn-secondary btn-sm" href="tactical-cover-retreat-ai-system.html">Asset Overview</a>\n'
        '                    </div>\n\n'
        + "\n".join(sections_html)
        + render_pager()
        + '                </div>\n'
        '            </div>\n'
        '        </div>\n'
        '    </main>\n\n'
        + render_footer("tactical-cover-retreat-ai-system.html", "Tactical Cover & Retreat AI System v3.0")
        + '    <script src="js/studio.js"></script>\n'
        '</body>\n\n'
        '</html>\n'
    )

    out_path = WORKSPACE / "tactical-cover-retreat-ai-system-docs.html"
    out_path.write_text(page_html, encoding="utf-8")
    print(f"Wrote {out_path.relative_to(WORKSPACE)} (99 sections)")


def build_tactical_ai_whats_new() -> None:
    v3_md = (TAC_ROOT / "Version_3" / "WhatsNew_v3.0.md").read_text(encoding="utf-8")
    v25_md = (TAC_ROOT / "Version2_5" / "WhatsNew_v2.5.md").read_text(encoding="utf-8")
    v2_md = (TAC_ROOT / "UpgradeGuideToVersion2_0.md").read_text(encoding="utf-8")

    link_map = {
        "tactical-cover-retreat-ai-system-docs.html": "tactical-cover-retreat-ai-system-docs.html",
        "quick-start": "tactical-cover-retreat-ai-system-docs.html#quick-start",
        "scenevalidator": "tactical-cover-retreat-ai-system-docs.html#SceneValidator",
        "scenevalidatorguide.md": "tactical-cover-retreat-ai-system-docs.html#SceneValidator",
        "../scenevalidatorguide.md": "tactical-cover-retreat-ai-system-docs.html#SceneValidator",
        "scenevalidator.md": "tactical-cover-retreat-ai-system-docs.html#SceneValidator",
        "squadcoordinator": "tactical-cover-retreat-ai-system-docs.html#SquadCoordinator",
        "tacticalagent": "tactical-cover-retreat-ai-system-docs.html#TacticalAgent",
        "suppressionservice": "tactical-cover-retreat-ai-system-docs.html#SuppressionService",
        "scorers/zonecontrolstatescorer.md": "tactical-cover-retreat-ai-system-docs.html#ZoneControlStateScorerSO",
        "scorers/vaultopportunityscorer.md": "tactical-cover-retreat-ai-system-docs.html#VaultOpportunityScorerSO",
        "scorers/sensorytypescorer.md": "tactical-cover-retreat-ai-system-docs.html#SensoryTypeScorerSO",
        "zonecontrolstatescorer.md": "tactical-cover-retreat-ai-system-docs.html#ZoneControlStateScorerSO",
        "vaultopportunityscorer.md": "tactical-cover-retreat-ai-system-docs.html#VaultOpportunityScorerSO",
        "sensorytypescorer.md": "tactical-cover-retreat-ai-system-docs.html#SensoryTypeScorerSO",
    }

    v3_html = md_to_html(v3_md, TAC_ROOT / "Version_3" / "WhatsNew_v3.0.md", link_map, "v3", strip_first_h1=False)
    v25_html = md_to_html(v25_md, TAC_ROOT / "Version2_5" / "WhatsNew_v2.5.md", link_map, "v25", strip_first_h1=False)
    v2_html = md_to_html(v2_md, TAC_ROOT / "UpgradeGuideToVersion2_0.md", link_map, "v2", strip_first_h1=False)

    page_html = (
        '<!DOCTYPE html>\n'
        '<html lang="en" data-theme="dark">\n\n'
        '<head>\n'
        '    <meta charset="UTF-8">\n'
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '    <title>What\'s New in Tactical AI (v3.0 &amp; v2.5) — Maharaja Studio</title>\n'
        '    <meta name="description" content="Changelog and architecture notes for Tactical Cover &amp; Retreat AI System: v3.0 synchronized squads, combat locomotion, and v2.5 dynamic suppression.">\n'
        '    <link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '    <link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">\n'
        '    <link rel="stylesheet" href="css/studio.css">\n'
        '</head>\n\n'
        '<body>\n'
        + render_nav("tactical", "tactical-cover-retreat-ai-system.html", "Asset overview")
        + render_mobile_drawer("Tactical AI Release Notes", [
            ("tactical-cover-retreat-ai-system.html", "Asset Overview"),
            ("tactical-cover-retreat-ai-system-docs.html", "Full Documentation (99 guides)"),
            ("#v3", "Version 3.0 Highlights"),
            ("#v25", "Version 2.5 Highlights"),
            ("#v20", "Version 2.0 Archive"),
        ])
        + '\n    <main class="page-content">\n'
        '        <header class="page-header">\n'
        '            <div class="container text-center">\n'
        '                <div class="hero-breadcrumb" style="justify-content: center; margin-bottom: 12px;">\n'
        '                    <a href="tactical-cover-retreat-ai-system.html">Tactical AI</a>\n'
        '                    <span>/</span>\n'
        '                    <span class="mono" style="color: var(--accent-text);">Release Notes</span>\n'
        '                </div>\n'
        '                <h1>What&rsquo;s New in Tactical AI</h1>\n'
        '                <p class="hero-sub" style="max-width: 680px; margin: 0 auto 20px;">\n'
        '                    Major architectural additions: v3.0 Combat Locomotion, Synchronized Squads, Scene Validator, and v2.5 Ballistic Suppression.\n'
        '                </p>\n'
        '                <div style="display: flex; gap: 12px; justify-content: center; flex-wrap: wrap;">\n'
        '                    <a href="tactical-cover-retreat-ai-system-docs.html" class="btn btn-primary">Open Full Documentation (99 Guides)</a>\n'
        '                    <a href="tactical-cover-retreat-ai-system.html" class="btn btn-secondary">Asset Overview</a>\n'
        '                </div>\n'
        '            </div>\n'
        '        </header>\n\n'
        '        <div class="container" style="max-width: 960px; margin: 40px auto 80px;">\n'
        '            <div style="display: flex; gap: 10px; margin-bottom: 32px; flex-wrap: wrap;">\n'
        '                <a href="#v3" class="eco-pill is-active">v3.0 Combat &amp; Squads</a>\n'
        '                <a href="#v25" class="eco-pill">v2.5 Suppression &amp; CQB</a>\n'
        '                <a href="#v20" class="eco-pill">v2.0 Architecture Archive</a>\n'
        '            </div>\n\n'
        '            <section id="v3" style="margin-bottom: 60px;">\n'
        '                <div style="padding: 6px 12px; background: var(--accent-soft); border: 1px solid var(--accent-line); border-radius: var(--radius-sm); display: inline-flex; align-items: center; gap: 8px; margin-bottom: 16px;">\n'
        '                    <span class="mono" style="font-weight: 600; color: var(--accent-text); font-size: 13px;">VERSION 3.0 RELEASE</span>\n'
        '                    <span style="font-size: 12px; color: var(--text-muted);">&middot; Major Feature Release</span>\n'
        '                </div>\n'
        f'{v3_html}\n'
        '            </section>\n\n'
        '            <hr style="border: 0; border-top: 1px solid var(--hairline-strong); margin: 60px 0;">\n\n'
        '            <section id="v25" style="margin-bottom: 60px;">\n'
        '                <div style="padding: 6px 12px; background: var(--bg-raised); border: 1px solid var(--hairline); border-radius: var(--radius-sm); display: inline-flex; align-items: center; gap: 8px; margin-bottom: 16px;">\n'
        '                    <span class="mono" style="font-weight: 600; color: var(--text-primary); font-size: 13px;">VERSION 2.5 RELEASE</span>\n'
        '                    <span style="font-size: 12px; color: var(--text-muted);">&middot; Ballistic Suppression Update</span>\n'
        '                </div>\n'
        f'{v25_html}\n'
        '            </section>\n\n'
        '            <hr style="border: 0; border-top: 1px solid var(--hairline-strong); margin: 60px 0;">\n\n'
        '            <section id="v20" style="margin-bottom: 60px;">\n'
        '                <div style="padding: 6px 12px; background: var(--bg-raised); border: 1px solid var(--hairline); border-radius: var(--radius-sm); display: inline-flex; align-items: center; gap: 8px; margin-bottom: 16px;">\n'
        '                    <span class="mono" style="font-weight: 600; color: var(--text-secondary); font-size: 13px;">VERSION 2.0 ARCHIVE</span>\n'
        '                    <span style="font-size: 12px; color: var(--text-muted);">&middot; Burst Pipeline Migration</span>\n'
        '                </div>\n'
        f'{v2_html}\n'
        '            </section>\n'
        '        </div>\n'
        '    </main>\n\n'
        + render_footer("tactical-cover-retreat-ai-system.html", "Tactical Cover & Retreat AI System v3.0")
        + '    <script src="js/studio.js"></script>\n'
        '</body>\n\n'
        '</html>\n'
    )

    out_path = WORKSPACE / "tactical_ai_whats_new.html"
    out_path.write_text(page_html, encoding="utf-8")
    print(f"Wrote {out_path.relative_to(WORKSPACE)}")


if __name__ == "__main__":
    build_tactical_ai_docs()
    build_tactical_ai_whats_new()

