# **Tactical AI 2.0: Upgrade Guide**

This guide outlines the steps required to upgrade your project from `MaharajaStudio.HidingSystem` (v1.x) to `MaharajaStudio.TacticalAI` (v2.0).

> **⚠️ Important:** Before upgrading, **back up your project**.
> While the included `[MovedFrom]` attributes handle asset serialization (Inspector references) automatically, **API changes in your custom scripts will require manual updates.**

---

## **1. Namespace Changes**

The entire namespace structure has been refactored to reflect the system's evolution into a complete "Tactical AI" suite.

**Global Find & Replace:**
Perform the following Find & Replace operations in your entire solution:

| Old Namespace | New Namespace | Description |
| --- | --- | --- |
| `MaharajaStudio.HidingSystem` | `MaharajaStudio.TacticalAI` | Root namespace change. |
| `MaharajaStudio.HidingSystem.Core` | `MaharajaStudio.TacticalAI.Core` | Core systems (Agent, Settings, Sync/Async logic). |
| `MaharajaStudio.HidingSystem.Providers` | `MaharajaStudio.TacticalAI.Providers` | *Note: HidingSystem.providers moved to TacticalAI.Provider.* |
| `MaharajaStudio.HidingSystem.Scorer` | `MaharajaStudio.TacticalAI.Scorer` | *Note: HidingSystem.Scorer  moved to TacticalAI.Scorer.* |
| `MaharajaStudio.HidingSystem.Helper` | `MaharajaStudio.TacticalAI.AllHelper` | Helper components like `CoverNode`. |
| `MaharajaStudio.HidingSystem.HidingProfiler` | `MaharajaStudio.TacticalAI.Profiling` | Performance metrics and debugging. |

> **Tip:** If you have files using both Providers and Scorers, you will likely need to add **both** new namespaces:
> ```csharp
> using MaharajaStudio.TacticalAI.Providers;
> using MaharajaStudio.TacticalAI.Scorer;
> 
> ```
> 
> 

---

## **2. Component & Class Renames**

Several core classes have been renamed to better represent their expanded functionality.

| Old Class Name | New Class Name | Functionality |
| --- | --- | --- |
| `EnemyHider` | `TacticalAgent` | The main component attached to your AI GameObject. |
| `HidingSettingsSO` | `TacticalAISettingsSO` | The configuration asset. |
| `HideSpotProviderSO` | `TacticalSpotProviderSO` | Base class for all Providers. |
| `HideSpotScorerSO` | `TacticalScorerSO` | Base class for all Scorers. |

### **Example Code Update**

**Old Code (v1.x):**

```csharp
using MaharajaStudio.HidingSystem;

public class MyAI : MonoBehaviour
{
    private EnemyHider _hider;

    void Start() {
        _hider = GetComponent<EnemyHider>();
        _hider.GetTopNHidingSpotsAsync(5);
    }
}

```

**New Code (v2.0):**

```csharp
using MaharajaStudio.TacticalAI; // 1. Namespace changed

public class MyAI : MonoBehaviour
{
    private TacticalAgent _agent; // 2. Class renamed

    void Start() {
        _agent = GetComponent<TacticalAgent>();
        _agent.GetTopNHidingSpotsAsync(5);
    }
}

```

---

## **5. New Features Setup (Optional)**

Tactical AI 2.0 includes several new systems you can opt-in to use.

### **5.1 Squad Coordination**

To prevent agents from stealing each other's cover or bunching up:

1. Add a **`SquadCoordinator`** component to a manager GameObject in your scene.
2. In your `TacticalAgent` inspector, assign the `SquadCoordinator` reference.
3. Set the **Squad Name** (agents with the same Squad Name will coordinate).
4. Add the **`SquadReservationScorerSO`** to your Settings asset.

### **New Providers **

These enable new search behaviors like flanking, squad formations, and room clearing.

* **`PincerFormationProviderSO`**: Generates points opposite to the average position of allies (surrounding the target).
* **`FlankPointProviderSO`**: Specifically generates points at the rear and sides of the target.
* **`CornerEdgeProviderSO`**: Scans for vertical edges to find "tactical leaning" or peek spots.
* **`AdvanceCoverProviderSO`**: Finds cover in a cone moving *towards* a target (for leapfrogging/pushing).
* **`ChokePointProviderSO`**: Identifies constricted areas (hallways, bridges) for ambushes.
* **`RoomClearanceProviderSO`**: Generates a "pie slice" arc around corners for gradual room entry.
* **`SquadFormationProviderSO`**: Generates points based on a formation shape (Wedge, Line, V) relative to a squad leader.
* **`VantagePointProviderSO`**: Finds high ground or edge positions overlooking open areas (good for hunting).

---

### **New Scorers **

These allow the AI to evaluate spots based on much more complex tactical criteria.

**Offensive & Aggressive**

* **`PlayerPathPredictionScorerSO`**: Predicts where the player will be in the future (avoids "ghost" targets).
* **`AggressiveLOSScorerSO`**: Rewards spots that have a clear shot at the target (for attackers).
* **`HighGroundScorerSO`**: Rewards being vertically higher than the target.
* **`RearAttackScorerSO`**: Rewards spots behind the target (1.0 = behind, 0.0 = front).
* **`PushForwardScorerSO`**: Rewards spots that are physically closer to the target than the current position.
* **`ZoneControlScorerSO`**: Rewards spots that have Line of Sight to a specific objective ID.

**Survival & Defensive**

* **`EscapeRouteScorerSO`**: Checks if the spot allows for further retreat (avoids dead ends).
* **`PlayerGazeScorerSO`**: Penalizes spots the player is currently looking at or aiming towards.
* **`WallHuggingScorerSO`**: Encourages staying close to geometry (avoids open fields).
* **`SkyliningScorerSO`**: Penalizes spots where the agent is silhouetted against the skybox.
* **`FatalFunnelScorerSO`**: Detects and penalizes narrow doorways or choke points.
* **`BulletPenetrationScorerSO`**: Penalizes cover that is too thin (e.g., plywood vs concrete).
* **`ExposureVolumeScorerSO`**: Calculates how "exposed" a spot is to the open world (samples surrounding rays).
* **`CoverClusterScorerSO`**: Rewards spots that have *other* cover objects nearby (backup cover).

**Squad Coordination**

* **`SquadReservationScorerSO`**: **Essential.** Prevents agents from picking spots claimed by squadmates.
* **`LineOfFireScorerSO`**: Prevents hiding in the crossfire between an ally and the target.
* **`MuzzleDisciplineScorerSO`**: Ensures agents don't walk/stand immediately in front of an ally's gun.
* **`SquadSeparationScorerSO`**: Prevents allies from bunching up too closely (< 3m).
* **`SectorWatchScorerSO`**: Rewards facing directions that allies are *not* currently watching (flank security).

**Utility & Environmental**

* **`RepetitionPenaltyScorerSO`**: Penalizes spots the agent has recently used (forces rotation).
* **`LightProbeScorerSO`**: Uses Unity Light Probes to detect actual darkness/shadows at the spot.
* **`CasualtyAversionScorerSO`**: Avoids areas where allies have recently died ("The Cursed Earth").
* **`AudioStimulusScorerSO`**: Attracts AI towards recent sounds in the `StimulusRegistry`.
* **`StalemateBreakerScorerSO`**: Forces a flank if the agent has been stuck in cover too long.

---

**Tactical AI 2.0** introduces a robust suite of debugging and profiling tools. These are completely new additions designed to help you visualize AI decision-making and optimize performance.

You can access these tools via the Unity Editor menu (paths defined in the scripts):

* **Debugger:** `Window/Analysis/Tactical Cover And Retreat AI/Tactical Decision Inspector Pro`
* **Profiler:** `Window/Analysis/Tactical Cover And Retreat AI/Tactical AI Profiler`

---

### **1. Tactical Debugger**

**Source:** `TacticalDebuggerWindow.cs`, `VisualContextDrawer.cs`

This tool provides real-time visual feedback in the Scene View, allowing you to "see what the AI sees." It visualizes the generated candidates, their scores, and the reasoning behind the selection.

**Key Features:**

* **Live Candidate Visualization:** Draws all candidate spots generated during a search.
* **Color Coding:** Spots are colored on a gradient from **Red** (Eliminated Score) to **Green** (Valid Score).
* **Best Spot:** Highlighted with a distinct Yellow pulse.


* **Scorer Filtering:** You can filter the visualization to see scores from specific categories (e.g., only show "Defensive" scores vs. "Offensive" scores) to debug specific behaviors.
* **Detailed Inspection:** Clicking or hovering over a candidate spot in the Scene View displays a breakdown of exactly how each scorer contributed to its final score.
* **Raycast Visualization:** Draws lines representing visibility checks, cover height checks, and invalid paths (Red lines for failed checks, Green for success).

**How to use:**

1. Open the window (`Window/Analysis/Tactical Cover And Retreat AI/Tactical Decision Inspector Pro`).
2. Select an AI Agent in the hierarchy (or lock the window to a specific agent).
3. Trigger a search (`RetreatToHide`).
4. The Scene View will populate with the debug context.

---

### **2. Hiding Profiler**

**Source:** `TacticalAIProfiler.cs`, `TacticalAIProfilerWindow.cs`

A dedicated performance analysis tool that records every search request ("Session") to help you optimize your settings and scorers. It separates Main Thread time from Job/Burst time.

**Key Metrics Tracked:**

* **Timeline View:** A history of recent search requests, showing their Success/Fail status and total duration.
* **Performance Breakdown:**
* **Total Duration:** Wall-clock time for the entire request.
* **Generation Time:** How long providers took to generate points.
* **Scoring Time:** Time spent calculating scores (separated into Main Thread vs. Burst Jobs).
* **Pathing Time:** Time spent calculating NavMesh paths.


* **Provider Cost:** Shows how many candidates each Provider generated and how many milliseconds it took.
* **Scorer Cost:** Shows which Scorers are the most expensive performance-wise, helping you identify optimization targets.
* **Failure Analysis:** If a search fails, the profiler records the exact reason (e.g., `NoCandidates`, `AllCandidatesDisqualified`).

**How to use:**

1. Open the window (`Window/Analysis/Tactical Cover And Retreat AI/Tactical AI Profiler`).
2. Ensure "Record" is toggled on in the window toolbar.
3. Run your game. The profiler automatically captures any `TacticalAgent` running a search.

## **6. Troubleshooting Common Upgrade Issues**

**Q: My agents aren't moving anymore.**

* **A:** Check if `EnemyHider` was replaced by `TacticalAgent`. Ensure your `NavMeshAgent` is active and `RetreatToHide()` is being called.

**Q: "NoCandidatesGenerated" Failure.**

* **A:**
1. Check `Search Radius` in settings.
2. Check `NavMeshAreaMask` includes the area the agent is standing on.
3. Ensure your Providers (e.g., `CoverNodeProvider`) have valid data or cover objects nearby.



**Q: "AllCandidatesDisqualified" Failure.**

* **A:**
1. Your scorers might be too strict. Disable strict scorers like `ProximityPenalty` or `PathSafety` temporarily.
2. Check `PathSafetyOverride` in your Settings—if set to `0.0`, *any* visibility on the path causes failure. Try `0.5` or `0.8`.
3. If using `SquadReservationScorer`, ensure you have a `SquadCoordinator` in the scene.



**Q: I get "The type or namespace name 'HidingSystem' could not be found".**

* **A:** You missed a namespace update. Replace `using MaharajaStudio.HidingSystem;` with `using MaharajaStudio.TacticalAI;`.