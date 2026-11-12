# Makeover Graph Overview & Canvas Navigation

> **Module:** MSUltimate Inspector Customizer — Makeover Graph  
> **Topic:** Visual Node Graph Architecture, GraphView Canvas, Blackboard, and Controls

---

## 1. Visual Node Graph Architecture

The **Makeover Graph** (`Tools > Maharaja Studio > MSUltimate > Inspector Customizer > Makeover Graph Editor`) is a visual logic execution environment built on Unity's UI Toolkit `GraphView`. It allows developers and technical artists to design procedural layout templates that automatically inspect components and apply rich attributes based on patterns, sibling relationships, and data types.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  Template: [RPG Character & Combat ▼] [New] [Save]    Live Target: [WarriorHero] [⚡]  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐                                                                      │
│  │ BLACKBOARD   │   ┌───────────────────┐        ┌───────────────────┐                 │
│  │ HeaderColor  │   │ ConditionType     │        │ GroupWrapper      │                 │
│  │ #FF3344      │   │ • Type: Float     │───────►│ • Group: Stats    │───┐             │
│  │ GroupName    │   └───────────────────┘        └───────────────────┘   │             │
│  │ "Combat"     │                                                        │             │
│  └──────────────┘   ┌───────────────────┐        ┌───────────────────┐   │ ┌─────────┐ │
│                     │ ConditionName     │        │ AttributeEmitter  │   └►│ Output  │ │
│  ┌──────────────┐   │ • Pattern: *health│───────►│ • ProgressBar     │────►│ Terminal│ │
│  │ STICKY NOTE  │   └───────────────────┘        └───────────────────┘     └─────────┘ │
│  │ Combat HUD   │                                                                      │
│  └──────────────┘                                                                      │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  ▲ Diagnostics (0 Errors, 0 Warnings)                    [Auto-Validate: ✓] [Compare]  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Opening & Creating Graphs

- **From Menu:** `Tools > Maharaja Studio > MSUltimate > Inspector Customizer > Makeover Graph Editor`.
- **From Asset:** Double-click any `InspectorTemplate` (`.asset`) or `MakeoverMacroAsset` (`.msmakomacro` / `.asset`) in the Project browser.
- **From Customizer Window:** Click the **Makeover Graph** button in the top toolbar of `InspectorCustomizerWindow`.

---

## 3. Canvas Navigation & Controls

| Action | Control Shortcut |
| :--- | :--- |
| **Pan Canvas** | Hold `Middle Mouse Button` or `Alt + Left Click` and drag. |
| **Zoom Canvas** | `Mouse Scroll Wheel` (supports zoom range from 15% to 200%). |
| **Open Node Search Menu** | Press `Spacebar` or right-click anywhere on the empty canvas. |
| **Frame All Nodes** | Press `A` or click the **Frame All** toolbar icon. |
| **Delete Selected** | Press `Delete` or `Backspace`. |
| **Duplicate Selected** | Press `Ctrl + D`. |
| **Box Select** | Left-click and drag across multiple nodes or edges. |

---

## 4. Blackboard Variables Dock

The **Blackboard** panel (toggleable via the top toolbar) lets you declare dynamic variables exposed to downstream nodes:

- **Supported Variable Types:** `Float`, `Int`, `String`, `Boolean`, `Color`.
- **Usage in Graph:** Drag any Blackboard property directly onto the canvas to create a `BlackboardProperty` node. Wire this node into parameter ports on `AttributeEmitter` or `GroupWrapper`.
- **Benefit:** Change a color or group name once on the Blackboard, and all connected emitters update across the entire graph.

---

## 5. Sticky Notes & Grouping

- **Sticky Notes:** Right-click $\rightarrow$ **Add Sticky Note**. Document sections of your graph with customizable title headers, body text, and color themes (`Classic`, `Cyan`, `Dark`, `Teal`, `Orange`, `Purple`).
- **Graph Scope Groups:** Select multiple nodes and press `Ctrl + G` to enclose them in a resizable, labeled group box.

---

## 6. Live Test Target & Diagnostic Drawer

The top-right toolbar provides a **Live Test Target** object field:
- Drag any GameObject or Component into this slot.
- The graph highlights in real-time which nodes match fields on the test target.
- Clicking the **Compare (`🪟`)** button opens `InspectorMakeoverCompareWindow` to see the live before-and-after result immediately!
- The collapsible **Diagnostics Drawer** at the bottom validates connection types, warns of circular dependencies, and identifies orphan unlinked nodes.
