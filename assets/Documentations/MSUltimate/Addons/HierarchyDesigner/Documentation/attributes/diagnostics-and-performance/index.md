# Diagnostics & Performance Attributes

> In-hierarchy real-time performance telemetry: audio VU meters, component icon strips, draw call material tracking, event hook auditing, light intensity telemetry, asset memory profiling, and polygon budgets.

---

## Attribute Directory (7 Attributes)
| Attribute | Target | Description | Status |
| :--- | :--- | :--- | :---: |
| [**`[HierarchyAudioMonitor]`**](hierarchy-audio-monitor.md) | `Class, Field` | Displays an animated VU volume meter and play/mute toggle button in the hierarchy. | ✅ Complete |
| [**`[HierarchyComponentIcons]`**](hierarchy-component-icons.md) | `Class` | Renders a horizontal strip of mini component icons for attached components with hover tooltips. | ✅ Complete |
| [**`[HierarchyDrawCallTracker]`**](hierarchy-draw-call-tracker.md) | `Class` | Analyzes submesh and material counts, flagging potential batch-breaking setups with an alert badge. | ✅ Complete |
| [**`[HierarchyEventHookTracker]`**](hierarchy-event-hook-tracker.md) | `Field, Class` | Audits UnityEvent listener counts on the hierarchy row, flagging empty or broken callback hooks. | ✅ Complete |
| [**`[HierarchyLightVisualizer]`**](hierarchy-light-visualizer.md) | `Class` | Displays a light type icon, color swatch, and intensity badge for Light components. | ✅ Complete |
| [**`[HierarchyMemoryTracker]`**](hierarchy-memory-tracker.md) | `Class, Field` | Displays estimated RAM and VRAM asset footprint on the hierarchy row with alert badges. | ✅ Complete |
| [**`[HierarchyPolyCount]`**](hierarchy-poly-count.md) | `Class` | Inspects mesh renderers and displays vertex or triangle counts on the hierarchy row. | ✅ Complete |
