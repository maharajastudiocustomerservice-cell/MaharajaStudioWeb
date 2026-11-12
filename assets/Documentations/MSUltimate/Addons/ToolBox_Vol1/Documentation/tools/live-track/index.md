# Live Track Manual

> Autonomous real-time variable telemetry, multi-scale oscilloscopes, and in-SceneView floating HUDs for Unity runtime diagnostics.

## Access & Launch
- **Menu Path:** `Tools > Maharaja Studio > MSUltimate > ToolBox Vol 1 > LiveTrack Dashboard`

---

## Capabilities & Workflows

### 1. Autonomous Background Sampling Engine
- **Decoupled from Inspector:** Telemetry sampling runs continuously in the background across all active scene objects via `LiveTrackRegistry`. Objects continue streaming data even when unselected or when the Inspector is viewing another GameObject.
- **Scene-Wide Auto-Discovery:** Discovers all MonoBehaviours decorated with `[LiveTrack]` automatically upon window focus or scene changes.

### 2. Multi-Scale Y-Axis Display Modes
- **Combined Mode (Absolute):** Global shared scale for comparing metrics with identical units (e.g., Vector3 components or multiple temperature sensors).
- **Normalized Mode (0% – 100%):** Per-series dynamic normalization, allowing simultaneous comparison of wildly mismatched orders of magnitude (e.g., Turbine RPM `0 - 8000`, Throttle `0.0 - 1.0`, and Heat `70 - 110°C`) without curve flattening.
- **Stacked Lanes Mode (DAW / Profiler Style):** Splits the dashboard into dedicated horizontal oscilloscope lanes, giving each variable its own unoccluded waveform track.
- **Interactive Cursor Inspection Card:** Hover over any point on the graph timeline to inspect an instant floating card listing the exact numeric values of all active series at that timestamp.

### 3. Floating In-SceneView Telemetry HUD
- **In-Context Monitoring:** Renders sleek, semi-transparent HUD cards directly above GameObjects in the SceneView via `SceneView.duringSceneGui`.
- **Live Status & Sparklines:** Displays current values, threshold warning badges (pulsing red/orange on alert), and a 10-second compact sparkline waveform.
- **Pinning & Selection Modes:** Enable `ShowInSceneView = true` on any `[LiveTrack]` attribute to pin HUDs permanently in SceneView, or toggle the toolbar button to display HUDs for selected objects.

### 4. Full C# Property & Method Support
- **Computed Properties:** Place `[LiveTrack]` directly onto computed C# properties (e.g. `public float SpeedKmh => rb.linearVelocity.magnitude * 3.6f;`).
- **Seamless Inspector & Dashboard Integration:** Renders sparklines, statistics, and alert thresholds identically for both serialized fields and dynamic properties.
