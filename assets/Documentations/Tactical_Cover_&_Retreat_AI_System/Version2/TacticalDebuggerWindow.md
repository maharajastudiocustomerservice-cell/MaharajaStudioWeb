# Tool: Tactical Decision Inspector Pro

**`TacticalDebuggerWindow`** is the central command center for analyzing, debugging, and tuning the Tactical AI system in real-time. It moves beyond simple gizmos to provide deep, frame-by-frame forensic analysis of why the AI chooses (or rejects) specific hiding spots.

It combines a visual debugger, a data profiler, and a sandbox tuning environment into a single Editor Window.

## Accessing the Tool

1. Navigate to the top menu bar: **Window > Analysis > Tactical Cover And Retreat AI > Tactical Decision Inspector Pro**.
2. Dock the window alongside your **Scene View** for the best experience.

## Core Workflow

The Inspector is divided into two main panels: the **Control Panel** (Left) and the **Intel Feed** (Right).

### 1. Command Center (Left Panel)

This section handles agent selection and view modes.

* **Target Agent**: Selects which AI agent to inspect.
* *Smart Selector*: A searchable dropdown list of all active `TacticalAgent` components in the scene.
* **Sync with Hierarchy**: If enabled, selecting a GameObject in the Unity Hierarchy will automatically select that agent in the Inspector.


* **Focus Cam (F)**: Instantly moves the Scene View camera to look at the currently selected candidate spot.
* **Isolate View**: Hides all non-selected candidate spots in the Scene View to reduce clutter.

### 2. Heatmaps & Visualization

Instead of generic dots, Version 2.0 introduces dynamic heatmaps to visualize data directly in the scene.

* **Heatmap Overlay Modes**:
* **None**: Standard coloring (Cyan = Selected, Gold = Best).
* **TotalScore**: Gradients from Red (Low Score) to Green (High Score).
* **Visibility**: Red = Visible to player, Green = Hidden.
* **Distance**: Visualizes the distance cost gradient from the search center.


* **Visual Settings**:
* **Spot Size**: Adjusts the size of the spheres in the Scene View.
* **Draw Lines**: Toggles the connection lines between the agent and candidates.



### 3. The Intel Feed (Right Panel)

This is the "Brain" of the debugger, showing the math behind the selected spot.

* **Radar Chart**: A visual polygon chart comparing the selected spot's attributes (e.g., Safety, Distance, Cover Quality) against the agent's **Current Position**. This allows you to instantly see *why* a move is an improvement.
* **Scorer Breakdown**: A detailed list of every `TacticalScorerSO` active on the agent.
* **Raw**: The normalized score returned by the scorer (0.0 to 1.0).
* **Wgt**: The weight multiplier applied.
* **Final**: The actual contribution to the total score.
* **Interactive Hover**: Hovering over a row in this list triggers **Context Drawing** in the Scene View (see below).



## Advanced Features

### The Probe Tool

The Probe allows you to debug "hypothetical" positions.

* **Enable Probe Tool**: Creates a movable handle in the Scene View.
* **Real-time Analysis**: Drag the probe anywhere in the scene. The Inspector will calculate the score for that exact point *as if* it were a generated candidate.
* **Use Case**: Great for answering questions like "Why didn't the AI pick this obvious corner?"—drag the probe there and see exactly which scorer is penalizing it (e.g., "Too close to allies" or "Skylining").

### Sandbox Tuning

Allows you to balance AI behavior without changing ScriptableObjects or restarting the game.

* **Enable Sandbox**: Unlocks the weight sliders for all scorers.
* **Live Tweak**: Dragging a slider immediately recalculates the scores for all candidates in the current snapshot, letting you find the perfect balance (e.g., "What happens if I double the `Fear` weight?").

### History & Snapshots

The AI often moves too fast to debug in real-time.

* **Auto-Capture**: Automatically records a snapshot every time the agent performs a search.
* **Time Travel**: Use the **View Snapshot** dropdown to revisit previous searches. You can inspect the candidates, scores, and player positions exactly as they were at that moment.

## Visual Context Drawing

A standout feature of Version 2.0 is **Context Sensitive Debugging**. When you hover over a specific Scorer in the **Intel Feed**, the Scene View draws debug info specific to *that* logic.

| Scorer Type | Visual Output (On Hover) |
| --- | --- |
| **Visibility** | Draws lines from the candidate to every player's eyes (Green=Hidden, Red=Visible). |
| **FOV** | Renders the players' view cones and checks if the candidate falls inside them. |
| **Prediction** | Draws yellow "Ghost" spheres showing where the AI predicts the player will be in `X` seconds, and lines checking visibility to that future point. |
| **Crossfire** | Draws lines to all allies and calculates the triangulation angle to the target. |
| **Ambush** | Draws a line to the "Last Known Position" of the target to verify ambush lines of sight. |
| **Cover Height** | Rays are cast vertically or towards the threat to visualize if the cover is tall enough. |
| **Proximity** | Draws Red "Danger" and "Disqualification" discs around enemies. |

## Filtering & Veto Analysis

When thousands of spots are generated, finding why a specific one failed is hard. The **Filters** section helps isolate data:

* **Veto Mode**:
* *Show All*: Standard view.
* *Valid Only*: Hides failed spots.
* *Vetoed Only*: Shows ONLY spots that failed.


* **Filter by Provider**: Isolate spots generated by `GridProvider` vs `CoverPointProvider`.
* **Filter by Veto Scorer**: Select a specific scorer (e.g., `ProximityPenalty`) to see only the spots *that specific scorer* rejected.

## Performance Note

The **Tactical Decision Inspector Pro** performs deep analysis, including re-running scoring logic synchronously to gather debug data. While highly optimized, it is intended for use in the Editor.

* **Impact**: Moderate CPU usage when "Auto-Capture" is on.
* **Recommendation**: Disable "Auto-Capture" or close the window when profiling performance or playtesting high-speed combat scenarios.