# Macros & Subgraph Architecture

> **Module:** MSUltimate Inspector Customizer — Makeover Graph  
> **Topic:** Authoring, Packaging, and Sharing Reusable Makeover Subgraphs (`.msmakomacro`)

---

## 1. What Are Makeover Macros?

As your makeover graph grows to handle hundreds of variables, repeating identical node groups (such as a 6-node network for checking numeric ranges, mapping colors, and emitting a styled progress bar) clutters the canvas.

A **Makeover Macro** (`MakeoverMacroAsset` / `.msmakomacro`) encapsulates any arbitrary subgraph into a single reusable node with custom input and output pins.

```
┌────────────────────────────────────────────────────────┐
│                   [ Macro: StatBar ]                   │
│                                                        │
│  (In) Member ───────────► [ Macro ] ────────► (Out) Rule
│  (In) BarColor                                         │
│  (In) DefaultMax                                       │
└────────────────────────────────────────────────────────┘
```

---

## 2. Creating a Macro Asset

1. In the Unity Project window, right-click $\rightarrow$ **`Create > Maharaja Studio > MSUltimate > Inspector Customizer > Makeover Macro`**.
2. Name the asset (e.g. `Macro_HealthStatBar.asset` or `Macro_HealthStatBar.msmakomacro`).
3. Double-click the macro asset to open it in `MakeoverGraphWindow`. Notice the top toolbar displays a purple **Macro Mode** badge.

---

## 3. Defining Input & Output Boundary Pins

Inside a Macro canvas:
- Add a **`MacroInput`** node:
  - Name the pin (e.g. `TargetMember` or `AccentColor`).
  - Set the data type (`Member`, `Color`, `Float`, etc.).
  - This pin will appear on the left side of the Macro node in parent graphs.
- Wire your internal logic nodes (Conditions, Math, Converters, Emitters).
- Add a **`MacroOutput`** node:
  - Name the outgoing pin (e.g. `RuleOut`).
  - Wire your final computed rule or attribute into it.
  - This pin will appear on the right side of the Macro node in parent graphs.

---

## 4. Using Macros in Parent Graphs

1. Open any standard `InspectorTemplate` in `MakeoverGraphWindow`.
2. Press `Spacebar` to open the search menu.
3. Type the name of your macro (or look under the `Macros/` category).
4. Click to instantiate the Macro node.
5. Wire your inputs and outputs. The parent graph remains neat, modular, and readable!

---

## 5. Exporting & Sharing Macros (.msmakomacro JSON)

Makeover Macros can be exported as standalone JSON files to share across team members or projects:
- Click **Export JSON** in the Macro inspector.
- A clean `.msmakomacro` file is generated.
- Other developers can import this file using **`Tools > Maharaja Studio > MSUltimate > Inspector Customizer > Template & Recipe Manager`**.
