# Telemetry & Visualizers Attributes

> Runtime badges: bitmask LED matrices, live AnimationCurve waveforms, delta rate of change indicators, radial progress rings, rolling sparklines, state machine transition trails, and coordinate vector displays.

---

## Attribute Directory (7 Attributes)
| Attribute | Target | Description | Status |
| :--- | :--- | :--- | :---: |
| [**`[HierarchyBitmask]`**](hierarchy-bitmask.md) | `Field, Property` | Displays bitmask or flags enum fields as a compact row of LED matrix dots on the hierarchy row. | ✅ Complete |
| [**`[HierarchyCurveVisualizer]`**](hierarchy-curve-visualizer.md) | `Field` | Renders a live mini waveform curve in the hierarchy row for AnimationCurve fields with playhead evaluation. | ✅ Complete |
| [**`[HierarchyDeltaTracker]`**](hierarchy-delta-tracker.md) | `Field, Property` | Observes and displays real-time rate of change indicators for numeric fields on the hierarchy row. | ✅ Complete |
| [**`[HierarchyRadialGauge]`**](hierarchy-radial-gauge.md) | `Field, Property` | Renders a circular radial donut progress ring for percentages, stamina, heat, or charges. | ✅ Complete |
| [**`[HierarchySparkline]`**](hierarchy-sparkline.md) | `Field, Property` | Renders a live rolling mini sparkline graph of historic numeric values directly on the hierarchy row. | ✅ Complete |
| [**`[HierarchyStateSnapshot]`**](hierarchy-state-snapshot.md) | `Field, Property` | Displays a real-time sliding history breadcrumb of finite state transitions during Play Mode. | ✅ Complete |
| [**`[HierarchyVectorDisplay]`**](hierarchy-vector-display.md) | `Field, Property` | Formats Vector2 or Vector3 coordinates into a compact badge on the hierarchy row with magnitude info. | ✅ Complete |
