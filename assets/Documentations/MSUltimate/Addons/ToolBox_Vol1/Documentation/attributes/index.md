# ToolBox Vol. 1 Attributes

> Integration attributes binding code fields, methods, and classes directly to the ToolBox window profilers, runtime console, and tracking systems.

---

## Attribute Directory (4 Attributes)

| Attribute | Target | Tool System | Description | Status |
| :--- | :--- | :--- | :--- | :---: |
| [**`[ConsoleCommand]`**](console-command.md) | `Method` | Advanced Console | Registers static C# methods as invokable developer commands in the runtime console. | ✅ Complete |
| [**`[HistoryTrack]`**](history-track.md) | `Field, Property` | History Track | Records discrete field mutations, author usernames, and values into an undo timeline. | ✅ Complete |
| [**`[TrackLifetime]`**](track-lifetime.md) | `Class` | Lifetime Track | Tracks instance lifecycle events, allocations, and object pooling to detect memory leaks. | ✅ Complete |
| [**`[LiveTrack]`**](live-track.md) | `Field, Property` | Live Track | Overlays real-time sparkline telemetry graphs, running statistics, and threshold alarms. | ✅ Complete |
