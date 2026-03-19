# User Interface Reference

A complete reference for every button, field, and panel in **Scriptable Studio Pro v3.0**.

---

## Main Window

The Main Window is the central hub for managing ScriptableObjects. It is divided into:
- **Toolbar** (top)
- **Sidebar** (left)
- **Right Pane** — contains the Pill Strip *(new)*, grid, and toolbar

---

### 1. Main Toolbar (Top)

| Element | Description |
|:---|:---|
| **Mode Selector** | Switches between **Create Mode** (new assets) and **Edit Mode** (modify existing assets). |
| **Presets** | Opens the **Preset Manager** to save or load window configurations. |
| **Open Details** | Opens the **Detail Panel** for the first selected instance, using the native drawing system. |
| **Reset All** | **[CAUTION]** Wipes all current window data, clears caches, and resets to defaults. Shows a confirmation dialog. |
| **🐞 (Validate)** | Opens the **Validation Window** to run rule-based checks on your data. |
| **⚙ (Settings)** | Opens the **Settings Window** to configure visuals, shortcuts, AI defaults, native drawn types, and workflow preferences. |
| **Refresh** | Forces a full reload of all ScriptableObject types and assets from the project. |
| **Assemblies** | Opens the **Assembly Selector** to control which assemblies the tool searches for types. |
| **Favorites Only** | Toggles a filter to show only types marked as Favorite. |
| **Formula Mode** | Toggles **Formula Mode**, showing raw formula strings in grid cells instead of evaluated values. |
| **? (Help)** | Opens the **Formula Help Window** with a cheat sheet of functions and operators. |
| **Naming:** | Quick-access field to set the **Naming Pattern** for new assets (e.g., `{TYPE}_{ii}`). |
| **Naming Help (?)** | Opens a popup explaining available naming wildcards. |

---

### 2. Sidebar (Left Pane)

| Element | Description |
|:---|:---|
| **Search Bar** | Filters the type list by name. Supports fuzzy matching. |
| **Type List** | All valid `ScriptableObject` types in your project. Click to select and view. |
| **Checkboxes** | Check a type to include it in **Batch Creation** or show it as a Pill. |
| **★ (Favorite)** | Star a type to keep it accessible under **Favorites Only** mode. |
| **Selection Strip** | Colored left strip on the active type row. |

#### Sidebar Footer — Create Mode

| Element | Description |
|:---|:---|
| **Mode** | Folder creation mode: **Default**, **Single Subfolder**, **Subfolder Per Type**. |
| **Folder Name** | Subfolder name / pattern (active only when a subfolder mode is selected). |
| **Ask for Location** | Prompts a file dialog on each Create click to choose the destination. |
| **Ping Folder** | Highlights created files in the Project window after generation. |
| **Create Assets** | Generates `.asset` files for all checked types in the list. |

#### Sidebar Footer — Edit Mode

| Element | Description |
|:---|:---|
| **Import All** | Loads all `.asset` files of the selected type from the project into the grid. |
| **Import Selected** | Loads only assets currently selected in the Project window. |
| **Update Linked Assets** | Saves changes made to linked assets back to disk. |

---

### 3. Pill Strip — Right Pane *(New in v3.0)*

Appears at the top of the right pane when two or more types are checked in the sidebar.

| Element | Description |
|:---|:---|
| **Pills** | One pill per checked type. **Left-click** to switch the grid to that type's data. |
| **Pill Drag** | **Right-click + drag** a pill to reorder it within the strip. |
| **▼ / ▲ Button** | Collapses / expands the pill strip. The pill height is configurable in **Settings › Visuals**. |
| **Pill Color** | Configurable in Settings: Fixed color, Randomized per type, or custom palette. |

---

### 4. Grid Area (Right Pane)

| Element | Description |
|:---|:---|
| **Type Name Header** | Displays the name of the currently selected type. |
| **Count Field** | *(Create Mode only)* How many instances to initially create. |
| **AI Window Button** | Opens the **AI Asset Architect** window. |
| **Import/Export Button** | Opens the **Data Manager** for CSV/JSON/SQL/Google Sheets. |
| **Smart Fill Button (✨)** | Opens **Smart Fill** for selected cells. |
| **Grid View** | The spreadsheet. **Rows** = instances, **Columns** = fields. |
| **Action Menu (⋮)** | Per-row context menu: Duplicate, Delete, Reset, Insert Above/Below, Copy, Paste. |
| **Column Header (right-click)** | Per-column options: Sort, Smart Rename, Set Name from Field. |

---

## Detail Panel

Accessed via **Open Details** from the toolbar, or by clicking a field name that opens a focused view.

The Detail Panel renders fields using the **v3.0 Native Drawing System**:

### Native Drawing Logic

| Check | Result |
|:---|:---|
| Type has `CustomPropertyDrawer` | Rendered with its native Unity drawer |
| Type name is in **Settings › Native Drawn Types** | Rendered with its native Unity drawer |
| Type name contains "SerializableDictionary" | Rendered with its native Unity drawer |
| Type is in `UnityEngine.Localization.*` | Rendered with its native Unity drawer |
| Otherwise | Rendered with the tool's built-in recursive field builder |

### Field Types in the Built-in Builder

| Category | Supported Types |
|:---|:---|
| **Primitives** | `int`, `float`, `double`, `long`, `bool`, `string`, `char`, `decimal` |
| **Unsigned / Small Int** | `uint`, `byte`, `sbyte`, `short`, `ushort`, `ulong` |
| **Unity Math** | `Vector2`, `Vector3`, `Vector4`, `Vector2Int`, `Vector3Int`, `Quaternion`, `Rect`, `Bounds` |
| **Unity Visual** | `Color`, `Gradient`, `AnimationCurve` |
| **Unity Reference** | `LayerMask`, `UnityEngine.Object` (any subtype), `Sprite`, `Texture2D`, `AudioClip` |
| **Enums** | Any C# enum type |
| **Collections** | `List<T>`, `T[]` (any element type, including custom structs) |
| **Structs / Classes** | Any `[Serializable]` struct or class (shown in collapsible foldout) |

### Prefab & Model Card

When a `GameObject` reference is assigned:
- **Preview thumbnail** from `AssetPreview`.
- **Component tags** (up to 3, with overflow count).
- **⚡ Spawn** button — instantiates the prefab in the scene.
- **Edit / Ping** button — opens Prefab Mode or highlights in Project window.
- **Inline Inspector** toggle — embeds a full Unity Inspector for the referenced object.

### Detail Panel Toolbar

| Element | Description |
|:---|:---|
| **Search Bar** | Filter visible fields by name |
| **Previous / Next** | Navigate between instances without closing the panel |
| **Undo / Redo** | The custom undo stack applies here as well |

---

## AI Asset Architect Window

Accessed via the **AI** button in the right pane toolbar.

### Engine Selection
- **Profile**: Select a saved AI profile (e.g., "OpenAI Default", "Gemini Creative").
- **Model**: Choose the specific model (e.g., `gpt-4o`, `gemini-2.0-flash`).

### Context
- **Game Name**: Grounds the AI in your project's identity.
- **Theme / Vibe**: Keywords such as "Cyberpunk" or "Dark Fantasy".
- **Global Lore**: A free-text "bible" about factions, history, rules.
- **Generate Names**: Let the AI invent creative names.
- **Naming Pattern**: Override the naming pattern for AI-generated assets.

### Style Reference
- **Use Previous Outputs**: Feed the last N assets as style examples for consistency.
- **Drag & Drop Zone**: Drop existing assets to teach the AI your preferred data style.

### Refinement
- **Extra Instructions**: Specific prompt additions (e.g., "All fire element, use negative damage for bosses").
- **Negative Prompt**: Things the AI should strictly avoid.

### Field Configuration (Right Column)
- **Field List**: Toggle which fields the AI populates.
- **Field Notes**: Per-field instructions (e.g., for `Weight`: "Keep between 10 and 50 kg").

---

## Settings Window

Opened via the **⚙** button in the main toolbar.

### 1. Visuals
- **Row Height / Font Size**: Adjust grid density.
- **Pill Height**: Height of each pill in the Pill Strip. *(New in v3.0)*
- **Pill Color Mode**: Fixed, Randomized, or Custom palette. *(New in v3.0)*
- **Detail Panel Docking**: Position the Detail Panel at the **Bottom** or **Right** of the screen.
- **Grid Lines**: Toggle visible grid lines.
- **Colors**: Customize selection color, row alternation, and background.

### 2. Workflow
- **Auto-Refresh on Focus**: Keeps the window in sync with project changes.
- **Reset on Create**: Unchecks types after creation.
- **Link Dragged Assets**: When dragging a `.asset` file into the window, auto-links it to the "Existing Reference" field in Create Mode.

### 3. Defaults
- **Naming & Folders**: Global defaults for naming patterns and folder modes.
- **Initialization**: Default counts and toggle states on window open.

### 4. Native Drawn Types *(New in v3.0)*
A list of fully-qualified type names that should always use the native property drawer in the Detail Panel.
- Add types that are not auto-detected (e.g., obscure third-party serializers without a recognized `CustomPropertyDrawer`).
- Format: `Namespace.ClassName` or `Namespace.ClassName\`1` for generic type definitions.

### 5. Shortcuts
- **Action List**: Select an action (e.g., "Delete Instance", "Duplicate").
- **Virtual Keyboard**: Click keys to rebind. Supports `Ctrl`, `Shift`, `Alt` modifiers.

### 6. AI Integration
- **Template Manager**: Create, edit, and delete AI connection profiles.
- **API Keys**: Securely enter API keys for OpenAI and Google Gemini.

---

## Import / Export Window

Accessed via the **Import/Export** button in the right pane.

### Format Selection
CSV, JSON, SQL, or Google Sheets.

### Import Tab
- **Replace Toggle**: Wipe existing rows before importing.
- **Drag & Drop**: Drop a `.csv`, `.json`, or `.sql` file to parse it immediately.
- **Google Sheets URL**: Download CSV from a published Sheet URL.
- **Paste & Import**: Paste clipboard data from Google Sheets.

### Export Tab
- **Save as...**: Exports current grid data to a file.
- **Copy to Clipboard**: For Google Sheets format; copies TSV for direct paste.

---

## Validation Window

Accessed via the **🐞** icon in the main toolbar.

| Element | Description |
|:---|:---|
| **Type Selector** | Choose which type to validate |
| **Rule List** | Add, remove, and configure validation rules |
| **Run Validation** | Execute all rules against current instances |
| **Results List** | Shows failing instances with field name, current value, and violated rule |
| **Ping Asset** | Highlights the failing asset in the Project window |
