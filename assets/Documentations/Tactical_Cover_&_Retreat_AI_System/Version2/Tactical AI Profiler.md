# Tool: Tactical AI Profiler

**`TacticalAIProfilerWindow`** is the performance monitoring and reliability suite for the Tactical AI system. It provides millisecond-accurate breakdowns of every hiding search, helping you identify performance bottlenecks (lag spikes) and logical failures (AI getting stuck) in real-time.

It tracks every search request across the entire session, unlike the Inspector which focuses on a single snapshot.

## Accessing the Tool

1. Navigate to the top menu bar: **Window > Analysis > Tactical Cover And Retreat AI > Tactical AI Profiler**.
2. This window works best when docked at the bottom of the screen or on a secondary monitor to view the live graph.

## Core Workflow

The Profiler is divided into three functional zones: the **Toolbar** (Controls), the **Pulse Graph** (Live Performance), and the **Session Dashboard** (Deep Analysis).

### 1. The Toolbar (Controls)

* **Record**: Toggles data collection. Disable this when not debugging to save memory.
* **Clear**: Wipes all history.
* **Pause on Fail**: A critical debugging feature. If enabled, the Editor will instantly **Pause** the game the moment any AI agent fails to find a hiding spot. This allows you to immediately switch to the **Tactical Inspector** to investigate the exact state of the world when the failure occurred.
* **Filters**:
* *All / Success / Failures*: Quickly isolate problematic searches.


* **Export CSV**: Dumps the current session data to a `.csv` file for external analysis in Excel or Sheets.

### 2. The Pulse Graph (Live Monitor)

Located at the top of the window, this graph visualizes the computational cost of AI searches over time.

* **The Line**: Each peak represents a single search request.
* **The Budget Line (Yellow)**: Represents a **16ms** (60 FPS) frame budget. If peaks consistently cross this line, your AI configuration is too heavy (too many candidates, raycasts, or complex scorers).

### 3. Session Dashboard (The Deep Dive)

Clicking any entry in the **Session List** (left pane) opens the detailed dashboard (right pane) for that specific search request.

#### A. Search Overview

High-level statistics to answer "Did it work?" and "Was it fast?"

* **Status Icon**: Green (Success) or Red (Failure).
* **Quick Actions**:
* *Select Agent*: Pings the specific AI GameObject in the Hierarchy.
* *Ping Settings*: Selects the `TacticalAISettingsSO` used for this search.


* **Failure Reason**: If failed, clearly states why (e.g., `NoCandidatesGenerated`, `AllCandidatesDisqualified`, `NoValidPathFound`).

#### B. Performance Timeline (New in v2.0)

A color-coded bar chart showing exactly where the time went. This is essential for optimization.

| Segment | Color | Description | Optimization Tip |
| --- | --- | --- | --- |
| **Generation** | Blue | Time spent by Providers generating points (Grid, Cover Points). | Reduce `SearchRadius` or density. |
| **Job Setup** | Yellow | Preparing arrays for the Burst Compiler. | Typically negligible. |
| **Job Exec** | Purple | **The Burst Job**. Heavy math (Raycasts, Visibility, FOV) runs here. | Reduce `MaxRaycastHits` or simpler scorers. But it's not fully Right|
| **Scoring** | Green | Main-thread scorers (logic that cannot run in Burst). | Check custom scorers or heavy C# logic. |
| **Pathing** | Red | NavMesh path calculations to validate reachability. | Usually the most expensive part. Use coarser NavMesh. |

#### C. Candidate Spatial Map

A 2D top-down visualization of the search cluster.

* **White Dots**: All generated candidate positions.
* **Green Dot**: The final selected hiding spot.
* **Use Case**: Helps identify if your providers are generating points in the wrong place (e.g., all points generated inside a wall) or if the search radius is too small.

#### D. Scorer Breakdown

A sorted list of every scorer used, split into two critical categories for Version 2.0 optimization:

1. **Main Thread Scorers**: These run on the CPU main thread. They are flexible but expensive. Custom scorers typically appear here.
2. **Burst Job Scorers (Parallel)**: These run in the high-performance Burst Job system.
* *Note*: Burst metrics are normalized to Wall Clock time to help you understand their relative impact, even though they run in parallel.



## Smart Filtering

The Profiler can be configured to only record specific agents to avoid spam in large scenes (`TacticalAIProfiler.cs`):

* **Mode = All**: Records every agent (Default).
* **Mode = SelectionOnly**: Only records the agent currently selected in the Hierarchy.
* **Mode = Whitelist**: Only records agents manually added to the whitelist via code (`TacticalAIProfiler.WhitelistedInstanceIDs.Add(...)`).

## Profiler vs. Inspector: When to use which?

| Tool | Question it Answers |
| --- | --- |
| **Tactical Profiler** | "Why is the game lagging?" <br>

<br> "Which agent is failing to find cover?" <br>

<br> "Is the NavMesh pathing taking too long?" |
| **Tactical Inspector** | "Why did the agent pick *this* rock instead of *that* wall?" <br>

<br> "Is the player visible from this spot?" <br>

<br> "What are the exact scores for this position?" |

**Pro Tip**: Use them together. Enable **Pause on Fail** in the Profiler. When the game pauses, open the **Inspector** to analyze the specific agent that failed.