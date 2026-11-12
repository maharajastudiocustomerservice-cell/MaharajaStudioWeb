# MSUltimate Ecosystem & Edition Comparison Guide

> **Welcome to the MSUltimate Architecture.**  
> Built natively for **Unity 6 (6000.x)+** across Universal (URP), High Definition (HDRP), and Built-in (BiRP) Render Pipelines.

---

## 1. Overview & Ecosystem Vision

**MSUltimate** is a modular, enterprise-grade Unity Editor enhancement suite designed to transform the Unity Inspector, Scene Hierarchy, and development toolchain into a fast, beautiful, and deeply structured production environment.

Built from the ground up on Unity's modern **UI Toolkit** (with seamless IMGUI fallback), MSUltimate eliminates per-frame layout recalculations, delivers buttery-smooth 120 FPS+ inspector scrolling, and introduces zero garbage collection (GC) or build bloat to your standalone game builds.

To accommodate solo indie developers, specialized teams, and large studios alike, MSUltimate is distributed across three primary paths:
1. **MSUltimate Core (Community Edition):** A generous, 100% free foundational inspector engine for qualifying indie creators.
2. **MSUltimate Core (Pro Edition):** Full C# source code access to the core engine with no revenue restrictions.
3. **6 Specialized Standalone Addons:** Individual, decoupled expansion modules covering animated attributes, component styling, hierarchy design, automated validation, visual inspector customization, and advanced developer tooling (`ToolBox Vol. 1`).
4. **MSUltimate Pro (Full Collection):** The flagship all-in-one bundle containing the entire ecosystem—Core, all 6 Addons, 4 developer tools, complete C# source code, and the centralized test suite (573 test files / 3,275 test methods / 6,115 test cases) at a massive bundle discount.

---

## 2. Master Package Comparison Matrix

The table below provides a comprehensive feature and licensing breakdown across every package in the MSUltimate ecosystem:

| Package Name | Price (USD) | Primary Domain | Attributes | Source Code | Tests Included | Included Addons | Licensing Tier |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **MSUltimate Core (Community)** | **FREE** | Core Inspector & Serializers | 156+ | Obfuscated DLL | — | — | Custom Free EULA (<$200K Rev) |
| **MSUltimate Core (Pro)** | **$149.99** | Unrestricted Core Engine | 156+ | Full C# Source | — | — | Standard Unity EULA (Per-Seat) |
| **MSUltimate - Animated Attributes** | **$29.99** | Micro-Interactions & VFX | 99 *(101 classes)* | Full C# Source | — | Standalone | Standard Unity EULA (Per-Seat) |
| **MSUltimate - Component Designer** | **$29.99** | Branded Inspector Cards | 74 *(75 classes)* | Full C# Source | — | Standalone | Standard Unity EULA (Per-Seat) |
| **MSUltimate - Hierarchy Designer** | **$29.99** | Scene Hierarchy Window | 82 *(83 classes)* | Full C# Source | — | Standalone | Standard Unity EULA (Per-Seat) |
| **MSUltimate - Validation Module** | **$29.99** | Project Scanning & Fixes | 39 | Full C# Source | — | Standalone | Standard Unity EULA (Per-Seat) |
| **MSUltimate - Inspector Customizer** | **$39.99** | Non-Destructive Styler & Baker | Templates & Graph | Full C# Source | — | Standalone | Standard Unity EULA (Per-Seat) |
| **MSUltimate - ToolBox Vol. 1** | **$44.99** | 4 Developer Power Tools | 4 + Tools | Full C# Source | — | Standalone | Standard Unity EULA (Per-Seat) |
| **MSUltimate Pro (Full Collection)** | **$299.99** | Complete Master Ecosystem | **454+** *(463 classes)* | **Full C# Source** | **6,115 Cases** | **ALL 6 Addons** | **Standard Unity EULA (Per-Seat)** |

---

## 3. Detailed Package Breakdown

### 🆓 MSUltimate Core (Community Edition)
*The modern inspector standard for every indie developer.*

- **Price:** Free
- **Format:** Precompiled, high-performance obfuscated DLLs.
- **Audience:** Solo developers, students, educators, and indie game studios with gross annual revenue under $200,000 USD.
- **Key Capabilities:**
  - **156+ Core Attributes:** Complete access to layout groups (`[BoxGroup]`, `[BeginTabGroup]` / `[EndTabGroup]`, `[BeginSplitPane]` / `[EndSplitPane]`), smart conditionals (`[ShowIf]`, `[EnableIf]`), buttons (`[Button]`, `[ToolbarToggle]`), specialized pickers (`[MinMaxSlider]`, `[ValueDropdown]`), in-scene 3D handles, and reactive callbacks (`[OnValueChanged]`).
  - **Custom Serializers:** Native Unity serialization for `SerializableDictionary<TKey, TValue>`, `SerializableHashSet<T>`, `SerializableMatrix2D<T>`, `SerializableMatrix3D<T>`, `SerializableQueue<T>`, and `SerializableStack<T>` via `ISerializationCallbackReceiver`.
  - **Extended Data Types:** Integrated visual drawers for `SerializableNullable<T>`, `SerializableDateTime`, `SerializableRange<T>`, `SerializableTuple<T1, T2>` / `SerializableTuple<T1, T2, T3>`, and `SerializableType`.
  - **Modular Window System:** Turn any class or ScriptableObject into a standalone, dockable editor window with tree-based menus (`ModularMenuEditorWindow`) and modal dialogs.
  - **Zero Boilerplate Collection Cascading:** Decorate items inside `List<T>`, arrays `T[]`, and dictionaries seamlessly.

---

### 💎 MSUltimate Core (Pro Edition)
*Unrestricted core power for commercial game studios.*

- **Price:** $149.99
- **Format:** 100% Clean, modular C# Source Code.
- **Audience:** Studios and professional teams requiring uncompiled source access for custom engine extensions, internal tooling integrations, and source control auditing.
- **Key Capabilities:**
  - Everything included in the Community Edition.
  - **Full C# Source Code:** Direct access to all core drawers, layout processors, and reflection engines.
  - **No Revenue Ceilings:** Fully commercial license with zero financial thresholds or upgrade obligations.
  - **Dedicated Engineering Support:** Direct email support with core framework architects.

---

### 👑 MSUltimate Pro (Full Collection)
*The complete AAA development suite at maximum bundle savings.*

- **Price:** $299.99 *(Over $350 in combined standalone value)*
- **Format:** Complete C# Source Code for Core and ALL 6 Official Addons.
- **Audience:** Professional studios, technical artists, and tool developers who want the definitive, all-in-one Unity authoring environment.
- **What's Included:**
  - **MSUltimate Core (Pro):** Full source code for all 156+ core attributes, serializers, types, and window systems.
  - **All 6 Official Addons:** Animated Attributes, Component Designer, Hierarchy Designer, Validation Module, Inspector Customizer, and ToolBox Vol. 1.
  - **454+ Concrete Attributes (463 Total Attribute Classes):** Exhaustive coverage across Core and Addons.
  - **4 Standalone Developer Tools:** Advanced Console, History Track, Object Lifetime Tracker, and Live Track.
  - **Centralized Test Suite:** 573 test files containing 3,275 `[Test]`/`[UnityTest]` methods (6,115 total test cases including `[TestCase]`) verifying attribute lifecycles, UI Toolkit visual tree safety, and collection cascading.
  - **VIP Priority Support:** Direct channel access for fast issue resolution and roadmap feature requests.

---

## 4. The 6 Standalone Addons (A La Carte Modules)

Each official Addon is engineered to be 100% decoupled—it can be purchased and imported individually to solve a specific development challenge without requiring the full suite:

```
MSUltimate Ecosystem
 ├── Core Framework (Free Community or Pro Source)
 │    │
 │    ├── [Visuals]     ───► MSUltimate - Component Designer
 │    ├── [Motion]      ───► MSUltimate - Animated Attributes
 │    ├── [Structure]   ───► MSUltimate - Hierarchy Designer
 │    ├── [Integrity]   ───► MSUltimate - Validation Module
 │    ├── [Customizing] ───► MSUltimate - Inspector Customizer
 │    └── [Diagnostics] ───► MSUltimate - ToolBox Vol. 1
```

### 1. 🚀 MSUltimate - Animated Attributes ($29.99)
- **Focus:** Micro-interactions, animated telemetry, and sensory feedback.
- **Content:** 99 concrete attributes (101 attribute classes including base contracts) across 12 runtime categories (13 documentation folders).
- **Highlights:** Dynamic combat HUD meters (`[BossHealthBar]`, `[ManaShieldBubble]`, `[CombatComboCounter]`), sci-fi data visualizers (`[HexGridMatrix]`, `[HologramFlicker]`, `[SonarPingWave]`), particle simulations (`[ParticleBurst]`, `[ElectricArcSparks]`), and kinetic typography (`[GlitchChopText]`, `[NeonSignFlicker]`).

### 2. 🎭 MSUltimate - Component Designer ($29.99)
- **Focus:** AAA MonoBehaviour Inspector card aesthetics and branded component presentation.
- **Content:** 74 concrete attributes (75 attribute classes including `ComponentAttribute`) across 7 categories.
- **Highlights:** Styled component borders and backgrounds (`[ComponentBorder]`, `[ComponentBackground]`, `[ComponentColorStrip]`), atmospheric VFX (`[ComponentParticles]`, `[ComponentAuroraEffect]`, `[ComponentCircuitFlow]`), header controls (`[ComponentHeader]`, `[ComponentHeaderButton]`), and genre themes (`[ComponentBlueprint]`, `[ComponentSciFiHUD]`, `[ComponentRPGStatCard]`).

### 3. 🌳 MSUltimate - Hierarchy Designer ($29.99)
- **Focus:** Complete organizational overhaul of the Unity Scene Hierarchy window.
- **Content:** 82 concrete attributes (83 attribute classes including `HierarchyAttribute`) across 8 categories.
- **Highlights:** Virtual colored folders (`[HierarchyFolder]`), branching tree connector lines (`[HierarchyTreeBranch]`), live hierarchy telemetry widgets (`[HierarchyAudioMonitor]`, `[HierarchyLightVisualizer]`, `[HierarchyComponentIcons]`, `[HierarchyEventHookTracker]`), active/lock toggles (`[HierarchyActiveButton]`, `[HierarchyLock]`), component counters, and performance badges (`[HierarchyDrawCallTracker]`, `[HierarchyPolyCount]`, `[HierarchyMemoryTracker]`).

### 4. 🔍 MSUltimate - Validation Module ($29.99)
- **Focus:** Real-time data integrity and project-wide asset/scene scanning.
- **Content:** 39 validation attributes + dedicated `ValidationWindow` + `ValidationCLI` + extensible `IValidationRule` / `IDeepValidationRule` pipelines.
- **Highlights:** Real-time field assertions (`[ValidateComponent]`, `[ValidateAssetPath]`, `[ValidateNotNull]`, `[ValidateRange]`, `[ValidateTextureSize]`), paired with a project-wide scan window that detects broken object/asset/prefab/shader/event references and offers 1-click auto-fix for supported deep rules (missing scripts, empty GameObjects, disabled root objects, abnormal scale, missing AudioSource clips, non-convex MeshColliders, unnecessary raycast targets, and useless lights).

### 5. 🎨 MSUltimate - Inspector Customizer ($39.99)
- **Focus:** Non-destructive visual inspector styling, Makeover Graph, AI Decorator, and C# code baking.
- **Content:** `InspectorCustomizerWindow`, 30-node `MakeoverGraphWindow`, `AIDecoratorModalWindow`, `TemplateRecipeManagerWindow`, `ComponentDefaultsWindow`, `InspectorMakeoverCompareWindow`, and `AttributeCodeBaker`.
- **Highlights:** Apply, reorder, and tune MSUltimate attributes visually via `InspectorProfile` assets with zero script changes, author node-based makeover rules and `.msmakomacro` subgraphs, generate layouts with Multi-LLM AI + local privacy scrubbing, preview live before/after diffs, and bake overrides cleanly back into C# source code.

### 6. 🧰 MSUltimate - ToolBox Vol. 1 ($44.99)
- **Focus:** High-throughput developer diagnostics and runtime telemetry.
- **Content:** 4 standalone tools + 4 tracking attributes (`[ConsoleCommand]`, `[HistoryTrack]`, `[TrackLifetime]`, `[LiveTrack]`).
- **Highlights:**
  - **Advanced Console:** High-speed log filtering, rule alerts, callstack analysis, runtime UI Toolkit overlay, and `[ConsoleCommand]` console commands.
  - **History Track:** Timeline-based Undo/Redo state inspection, variable change diffs, and Play Mode tweak committing.
  - **Object Lifetime Tracker:** Allocation tracking, dangling C# reference hunting, scene teardown leak detection, and GameObject lifecycle auditing.
  - **Live Track:** In-SceneView floating telemetry HUD and multi-scale oscilloscope variable graphs.

---

## 5. Which Edition Should You Choose?

```
┌────────────────────────────────────────────────────────┐
│             What best describes your project?          │
└──────────────────────────┬─────────────────────────────┘
                           │
         ┌─────────────────┴─────────────────┐
         ▼                                   ▼
[Indie / Solo / Student]           [Commercial Studio / Team]
         │                                   │
         ▼                                   ▼
Gross revenue under $200K?         Need full source code or all tools?
   ├─ YES ──► MSUltimate Core (Community)    ├─ Core only ──► MSUltimate Core (Pro)
   └─ NO  ──► MSUltimate Core (Pro)          └─ Everything──► MSUltimate Pro (Full Collection)
                                                     │
                                       (Want only specific features?)
                                                     ▼
                                       Specific Standalone Addon
                                       (Hierarchy, Validation, etc.)
```

### Choose **MSUltimate Core (Community)** if:
- You are an indie developer, hobbyist, student, or startup with under $200K USD annual revenue.
- You want an immediate, massive upgrade to the default Unity Inspector with zero financial investment.
- You want 156+ battle-tested attributes, custom serializers, and windowing tools in a clean, drop-in DLL package.

### Choose **MSUltimate Core (Pro)** if:
- Your studio earns more than $200K USD annually or requires uncompiled C# source code.
- You need to customize drawer internals or integrate private tooling hooks into your internal engine pipeline.
- You only need the foundational inspector framework and serializers without the extra styling or diagnostics addons.

### Choose **MSUltimate Pro (Full Collection)** if:
- You want the complete, ultimate development experience with all 454+ attributes, 6 addons, and 4 developer tools.
- You want continuous integration (CI) safety backed by the official **573-file / 6,115-case automated test suite**.
- You want maximum cost efficiency (saves over $100 compared to buying packages individually).

### Choose **Individual Addons** if:
- You already have an established inspector workflow, but specifically need hierarchy organization (`Hierarchy Designer`), scene validation (`Validation Module`), or advanced diagnostics (`ToolBox Vol. 1`).

---

## 6. Technical Specifications & Requirements

- **Unity Editor Version:** **Unity 6 (6000.x) and newer**.
- **Render Pipelines:** 100% compatible with Universal Render Pipeline (URP), High Definition Render Pipeline (HDRP), and Built-in Render Pipeline (BiRP).
- **Runtime Platforms:** Windows, macOS, Linux, iOS, Android, WebGL, Xbox, PlayStation, Nintendo Switch. (All editor tooling code is editor-only and automatically stripped from runtime player builds).
- **Architecture:** Native UI Toolkit with IMGUI compatibility layer. Zero runtime Garbage Collection (GC) allocations.

---

## 7. Licensing & Fair Use Summary

- **Community Edition:** Free to use for commercial and non-commercial games by creators and studios with annual gross revenues and funding below $200,000 USD under our dedicated Custom License. If your revenue or capital funding exceeds this threshold, upgrading to a Pro license is required.
- **Pro Editions & Addons:** Governed by the **standard Unity Asset Store End User License Agreement (EULA) on a per-seat basis** (one license required per developer seat utilizing the software in your studio), with no gross revenue ceilings or royalty obligations.
- **Redistribution Policy:** Redistribution, sublicensing, decompilation, reverse engineering, or hosting on public repositories is strictly prohibited across all editions.

---

*Need help deciding or have questions about custom studio licensing? Reach out to our team at **maharajastudiocustomerservice@gmail.com** or join our **Discord Community**.*

