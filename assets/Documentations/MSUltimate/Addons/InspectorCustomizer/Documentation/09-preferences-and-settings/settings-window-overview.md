# Settings Window & Configuration Overview

> **Module:** MSUltimate Inspector Customizer — Preferences & Settings  
> **Topic:** The 8-Category Split-View Settings Window, Engine Configuration, and Automation Options

---

## 1. Opening the Settings Hub

The central configuration workspace for Inspector Customizer is accessible via:  
**`Tools > Maharaja Studio > MSUltimate > Inspector Customizer > Inspector Customizer Settings`**.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  Inspector Customizer Settings                                                         │
├──────────────────────┬─────────────────────────────────────────────────────────────────┤
│  NAVIGATION          │  ⚙️ GENERAL PREFERENCES & AUTOMATION                             │
│  • General ◄──       │  Configure live editing triggers, debouncing, and automation.   │
│  • ComponentDefaults │  ─────────────────────────────────────────────────────────────  │
│  • Makeover          │  CARD 1: ⚡ AUTO-UPDATE TRIGGERS                                 │
│  • Privacy           │  Inspector Updates: [ LiveDebounced ▼ ]                         │
│  • AI Profiles       │  Hierarchy Updates: [ OnlyHierarchyAttributes ▼ ]               │
│  • Presets           │  Component Updates: [ OnlyComponentAttributes ▼ ]               │
│  • Catalog           │  Debounce Delay (ms): [ 300           ]                         │
│  • About             │  ─────────────────────────────────────────────────────────────  │
│                      │  CARD 2: 💾 PERSISTENCE & WORKFLOW                               │
│                      │  [✓] Auto-Save Profile on Edit                                  │
│                      │  [✓] Live In-Memory Preview                                     │
│                      │  [ ] Auto-Explore Code Attributes on Load                       │
│                      │  ─────────────────────────────────────────────────────────────  │
│                      │  CARD 3: 🔍 MEMBER DISCOVERY & VISIBILITY SCOPE                  │
│                      │  Scope Preset: [ Standard ▼ ]                                   │
│                      │  [✓] Serialized Fields      [✓] Public Methods                  │
│                      │  [ ] Private Fields         [ ] Private Methods                 │
│                      │  [ ] Backing Fields         [✓] Inherited Members               │
└──────────────────────┴─────────────────────────────────────────────────────────────────┘
```

---

## 2. Comprehensive Breakdown of All 8 Categories

### 2.1 Category 1: `General`
- **Auto-Update Triggers:**
  - `Inspector Updates`: Controls inspector redraw behavior (`LiveDebounced` for smooth debounce, `Immediate` for instant redraw on every keystroke, or `ManualOnly`).
  - `Hierarchy Updates`: Controls scene hierarchy redraws (`OnlyHierarchyAttributes` to update only when hierarchy attributes change, `Always`, or `ManualOnly`).
  - `Component Updates`: Controls class-level header/card styling updates (`OnlyComponentAttributes`, `Always`, or `ManualOnly`).
  - `Debounce Delay (ms)`: Controls throttle slider delay (50ms to 1000ms, default: `300ms`) for smooth parameter dragging without editor stutter.
- **Persistence & Workflow:**
  - `Auto-Save Profile on Edit`: When enabled, any card edit automatically writes to the profile asset on disk.
  - `Live In-Memory Preview`: Enables instant reflection preview in active inspectors before disk saves.
  - `Auto-Explore Code Attributes on Load`: When enabled, scans and imports code-defined attributes when selecting a component. If disabled (recommended), import manually via the `🔍 Explore` button in the toolbar so cleared attributes are not continuously re-imported.
- **Tooltips & Documentation:**
  - `Show Attribute Header Tooltips`: Displays attribute class summaries in card headers.
  - `Show Constructor / Parameter Tooltips`: Displays parameter descriptions inside cards.
- **Member Discovery & Visibility Scope:**
  - `Scope Preset`: Quickly toggle between `Standard` (clean view of serialized fields, public methods, and decorated properties) and `PowerUser` (unrestricted view of private fields, compiler backing fields, and parameterized methods).
  - Individual checkboxes for granular discovery customization.

---

### 2.2 Category 2: `ComponentDefaults`
Visual management of project-wide default component attributes and multi-condition exclusion rules:
- **Card 1: Master Activation & Scope:** Master switch (`EnableDefaultComponentAttributes`), target scopes (`Apply to MonoBehaviours`, `Apply to ScriptableObjects`), and safety guards (`Ignore Unity Built-Ins`, `Ignore UPM Package Assemblies`, `Ignore Abstract Base Classes`, and `[NoDefaultAttributes]` opt-out support).
- **Card 2: Default Attributes Manager:** Deck of default class-level attributes applied to all qualifying components in the project.
- **Card 3: Granular Ignore Rules Engine:** 7 built-in rules plus custom criteria (`Namespace`, `AssemblyName`, `BaseType`, `DerivedFromClass`, `SpecificType`, `AttributePresent`, `ScriptPath`, `HasAnyMSUltimateAttribute`).
- **Card 4: Live Component Rule Tester:** Interactive drag-and-drop test slot to verify whether any component passes or gets ignored in real time.

---

### 2.3 Category 3: `Makeover`
Configures the algorithmic intelligence engine that powers 1-Click Makeovers and the Makeover Graph:
- **Intelligence Engine Passes:** Studio defaults for Relational Field Pairing (`MakeoverRelationalPairing`), Dynamic Companion Max Binding (`MakeoverDynamicCompanionBinding`), Progressive Disclosure Cascades (`MakeoverToggleCascades`), and Action Toolbar Generation (`MakeoverActionToolbar`).
- **Conflict Policy & Automation:** Default Conflict Resolution (`Skip`, `Replace`, `Duplicate`), Auto-Detect Match Threshold (slider 10% to 90%, default: `40%`), Auto-Open Live Compare Preview (`MakeoverAutoOpenCompare`), and Prompt to Bake to C# after Makeover (`MakeoverPromptBakeAfterApply`).
- **Library Shortcuts:** Buttons to open the Template & Recipe Manager, Rebuild Built-in Presets, or Reveal the Templates Folder in the Project browser.

---

### 2.4 Category 4: `Privacy`
The **Studio Privacy & Data Shield**:
- **Zero Source Code Guarantee:** Strictly prevents method bodies, physics math, shaders, and private gameplay algorithms from leaving your workstation.
- **Allowed Member Types:** Toggles to include field names, field types, public fields, serialized private fields, action methods, doc comments, and existing attributes.
- **Documentation in Prompts:** Toggles to include attribute summaries and parameter documentation (with token cost warnings).
- **Exclusion Patterns & Caps:** Configurable wildcard filter (e.g. `m_*, _internal*, *BackingField`) and safety max members cap (`MaxMembersLimit`).
- **AST Schema Filter Settings:** Options to strip doc comments, strip private field names, or obfuscate type identifiers before AI dispatch.
- **Telemetry Toggle:** Option to disable all anonymous analytics.

---

### 2.5 Category 5: `AIProfiles`
Manages AI backend configurations:
- Switch active AI profiles (`Studio Default`, `Local Offline`, `Enterprise Proxy`).
- Select provider (`OpenAI`, `Anthropic`, `Gemini`, `Ollama`, `Groq`, `Mistral`, `OpenRouter`, `Custom`).
- Configure Model IDs, API Keys, Endpoint URLs, Temperature, and Max Token budgets.
- **Test Connection Button:** Validates authentication and network latency.

---

### 2.6 Category 6: `Presets`
Manages the prompt engineering library used by the AI Decorator:
- Aesthetic presets: *RPG Character & Combat*, *Vehicle Physics Rig*, *Sci-Fi Ballistics*, *Audio Soundscape*, *Clean Minimalist*, *Game Dashboard*.
- Customize positive directives, negative prompts, and system prompt mode (*Studio Default*, *User-Defined*, *Combined*).
- Manage few-shot reference scripts and image mockups.

---

### 2.7 Category 7: `Catalog`
The attribute permissions filter for AI generation:
- Choose which attributes from Core and Addons are permitted for use during AI layout generation.
- Disable experimental or unapproved attributes across your team.

---

### 2.8 Category 8: `About`
- Installed package version and changelog summary.
- Offline documentation links.
- **Reset to Factory Defaults:** Button to restore all settings, presets, and ignore rules to their original state.
