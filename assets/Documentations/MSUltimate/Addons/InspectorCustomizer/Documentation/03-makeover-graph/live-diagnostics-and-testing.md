# Live Diagnostics & Real-Time Target Testing

> **Module:** MSUltimate Inspector Customizer — Makeover Graph  
> **Topic:** Graph Validation, Diagnostic Error Drawer, Live Target Pinging, and Live Comparison

---

## 1. The Real-Time Diagnostics Engine

When authoring complex procedural graphs, logic errors—such as type mismatches between ports, disconnected terminal wires, or circular dependencies—can prevent templates from compiling properly.

`MakeoverGraphWindow` includes an integrated **Diagnostics Engine** that runs continuously in the background:

```
┌────────────────────────────────────────────────────────────────────────┐
│  ▲ Diagnostics (1 Warning, 0 Errors)               [Auto-Validate: ✓]  │
├────────────────────────────────────────────────────────────────────────┤
│  ⚠️ Warning: Node 'AttributeEmitter (ProgressBar)' has unlinked 'Max'  │
│     parameter port. Using fallback default value '100.0'.              │
│  ℹ️ Info: 4 rules successfully routed to Output terminal.             │
└────────────────────────────────────────────────────────────────────────┘
```

### Diagnostic Severity Levels
- **Error (Red):** Critical failure that stops graph evaluation (e.g. no `Output` node present, invalid recursive macro loop).
- **Warning (Yellow):** Non-breaking configuration issue (e.g. an orphan condition node with no downstream connection, unlinked parameter falling back to default).
- **Info (Blue):** Performance metrics and rule execution tallies.

Clicking on any diagnostic row automatically pans and frames the offending node on the canvas.

---

## 2. Live Target Pinging & Rule Tracing

The top toolbar includes a **Live Test Target** slot:

1. Drag any GameObject or Component instance from your scene into the **Test Target** field.
2. The graph executes a simulation pass against the test component.
3. Nodes that successfully match one or more fields on the target illuminate with a green active aura.
4. Hovering over any connection wire displays a tooltip previewing the exact data passing through that connection (e.g. `Matched: "currentHealth" (float)`).

---

## 3. Instant Before-vs-After Comparison

Next to the Test Target slot, click the **Compare (`🪟`)** button:
- Instantly launches the `InspectorMakeoverCompareWindow`.
- Shows a side-by-side split screen of the test target:
  - **Left:** Default Unity Inspector presentation.
  - **Right:** The live makeover output produced by your current graph.
- Edit graph nodes or parameters on the canvas; the right column updates in real-time as you tweak values!
