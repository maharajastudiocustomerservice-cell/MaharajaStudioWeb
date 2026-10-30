# Core Concepts

Understanding the foundational pieces of the Advanced Console System allows you to leverage its full potential for debugging and analytics.

## 1. ConsoleLogEntry
Every event in the console is a `ConsoleLogEntry`. It holds significantly more data than a standard Unity log:
- **Severity**: Trace, Debug, Info, Warning, Error, Critical.
- **Source**: User, Validation, HistoryTrack, LiveTrack, System.
- **Channel**: A string used to group logs (e.g., "Network", "Physics", "AI").
- **Tags**: An array of strings for granular filtering.
- **TargetObject**: A reference to the specific Unity Object (GameObject, ScriptableObject) that spawned the log. Clicking "Select Object" in the UI pings this object.
- **ContextSnapshot**: A dictionary of string key-value pairs representing variables at the exact moment the log occurred.
- **Actions**: A list of clickable buttons (`ConsoleAction`) embedded in the log detail view.

## 2. ConsoleLogManager (Registry)
The `ConsoleLogManager` is the static singleton that routes and stores all logs.
- It maintains a **circular buffer** of up to 10,000 logs by default to prevent memory leaks.
- It handles computing **Collapse Hashes**. If consecutive logs match by message and context, they are collapsed into a single entry with a badge count.
- It provides APIs to run complex queries, filter logs, and manage **Sessions**.

## 3. Log Sessions & Exporting
You can take snapshots of the console's current state.
- **Start New Session**: Resets the active view into a new logical block (useful when testing a specific feature).
- **Save Session**: Stores the current log buffer into memory.
- **Compare Sessions**: API available to diff two sessions and find unique or recurring errors.
- **Export**: Export the current filtered view to **CSV** or **JSON** for external analysis or to attach to bug reports.

## 4. ConsoleRuleEngine
The Rule Engine evaluates every incoming log against a list of `ConsoleLogRule` definitions. 
A rule consists of:
- **Conditions**: Min severity, specific source, regex pattern match, or occurring *X times* within *Y seconds*.
- **Actions**: Show an Editor popup, pause the Editor immediately, or escalate the console log.

*Example*: If 5 `Network` errors happen in 1 second, the rule can automatically pause the Unity Editor so you can inspect the exact frame it failed.

## 5. Timeline Heatmap
Located just under the toolbar, the timeline converts the timestamps and severities of all logs in your current session into a stacked bar chart. 
- **Green**: Info logs.
- **Yellow**: Warning logs.
- **Red**: Error/Critical logs.
If your game suddenly stutters, you can look at the heatmap to see if a red "burst" of errors occurred at that exact moment.
