# Introduction to Advanced Console System

The **Advanced Console System** is a professional, high-performance logging and debugging suite built specifically for the Modular Editor Attributes package. It acts as a centralized hub that aggregates logs, warnings, and errors from various subsystems (like Validation, HistoryTrack, and LiveTrack) as well as your custom user code.

## Why Advanced Console?
Unity's built-in console is great for basic logging but often falls short when dealing with complex projects, requiring advanced filtering, real-time analytics, or proactive alerts. The Advanced Console System bridges this gap by offering:

- **Unified Log Registry**: A single source of truth for all system events.
- **Rich Context**: Every log entry can hold stack traces, context snapshots, tags, and quick-action buttons.
- **Visual Analytics**: A timeline heatmap gives you a bird's-eye view of error density and system health over time.
- **Proactive Rules**: Configure rules to automatically pause the editor or show popups when specific error thresholds are met.
- **Team Collaboration**: Add user notes to log entries, bookmark critical logs, and save/export log sessions to share with your team.
- **Runtime Support**: An in-game IMGUI overlay console allows you to monitor logs and execute custom commands directly in your built game.

## Key Features

### 1. The Advanced Console Window (UI Toolkit)
A highly optimized, dark-themed editor window built using UI Toolkit. It features:
- **Advanced Filtering**: Filter by severity, source (User, Validation, LiveTrack, etc.), channels, and tags.
- **Smart Search**: Supports both standard text matching and Regex.
- **Sidebar Navigation**: Quickly toggle channels, sources, and active alert rules.
- **Detail Panel**: Inspect selected logs to instantly view full stack traces, variable values at the time of the log (Context Snapshots), and execute Quick Actions (e.g., healing a player).

### 2. Runtime Overlay Console
Press the backtick (`` ` ``) key during Play Mode or in a built application to bring up an unobtrusive overlay console.
- Captures Unity's internal `Debug.Log`.
- Offers built-in commands like `help`, `fps`, `time_scale`, and `clear`.
- Fully supports custom mapped commands using the `[ConsoleCommand]` attribute.

### 3. Deep Integration
The Advanced Console automatically captures events from other Modular Editor Attributes systems:
- **Validation Engine**: Automatically logs validation errors and warnings.
- **HistoryTrack**: Logs field value changes.
- **LiveTrack**: Logs upper/lower bound alerts.

---
**Next Step:** See [Getting Started](Getting-Started.md) to integrate the console into your workflow.
