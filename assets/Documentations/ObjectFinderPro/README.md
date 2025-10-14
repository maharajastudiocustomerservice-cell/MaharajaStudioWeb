# Object Finder Tool

The Object Finder tool helps you locate GameObjects and Assets within your Unity project. It provides various filtering options, asynchronous searching to prevent editor freezes, and the ability to scope searches to specific folders.

## Main Window: Object Finder Pro

To open the tool, go to **Tools > Maharaja Studio > Object Finder Pro** in the Unity menu.

### 1. Search Bar & Execution

*  **Search Field (Top):** This is the primary input for your search queries. The behavior of this field changes based on the selected search mode below.
*  **Search / Cancel Button:** Manually starts or cancels the current search operation.
*  **Auto Search (Toggle):** When enabled, a search is automatically performed a moment after you stop typing in the search field, providing a more interactive experience.
*  **Fuzzy Search (Toggle):** Enables a powerful, typo-tolerant search. For example, a search for "plyr" can find "Player". Results are sorted by relevance. This is mutually exclusive with Smart Search and Exact Match.
*  **Exact Match (Toggle):** When enabled, the search will only return items whose names are an exact, case-insensitive match to the search query. This is mutually exclusive with Fuzzy and Smart Search.

### Smart Search

When the `Use Smart Search` toggle is enabled, the main search bar becomes a powerful, multi-faceted query field, allowing for more precise and complex searches using special keywords and intelligent name matching.

*   **How it Works:** When enabled, the tool parses your query for special keywords. Active filters are displayed as "pills" below the search bar, which can be clicked to remove them. This mode overrides the individual filter fields (Type, Tag, Layer, etc.) if the corresponding keyword is used.
*  **Autocomplete:** The search field provides autocomplete suggestions for keywords, component names (comp(Light)), and even public properties (comp(Light).intensity:), speeding up complex queries.

*   **Keyword Filtering:** Use the following keywords followed by a colon (`:`) to apply specific filters directly from the search bar:
    *   `type:` - Filters by asset type. Example: `t:Material`
    *   `tag:` - Filters by GameObject tag. Supports comma-separated values for OR logic `(e.g., tag:Player,Enemy)`.    For tags with spaces, use quotes: `tag:"UI Element"`.
    *   `layer:` - Filters by GameObject layer. Also supports comma-separated values. Example: `layer:UI`
    *   `script:` - Filters by attached script name. Example: `script:PlayerController`
    *   `active:` - Filters by active state. Example: `active:true`
    *   `comp(ComponentName).propertyName:value` - Filters GameObjects by the value of a public component property. Supports operators `>, <, >=, <=`. Example: `comp(Light).intensity:>5`

*   **Numeric Filtering:**
        `polycount:`, `memsize:`, `texwidth:`, `childcount:` - Use with operators `(>, <, =, etc.)` to filter by metrics. Units like `kb` and `mb` are supported for `memsize.` Example: `memsize:>=5mb`

*   **Acronym Matching:** The name search is "smart" and can match acronyms from PascalCase or camelCase names.
    *   Example: A search for `pc` or `pcon` can match a script named `PlayerController`.
    *   Example: `uts` can match `UltimateTestingScript`.

*   **Undo/Redo:** The search field supports Undo (Ctrl/Cmd+Z) and Redo (Ctrl/Cmd+Y).


### 2. Core Filter Options

These options help you narrow down your search results:

*   **Search In:** Determines where the tool looks for objects.
    *   **Both:** Searches both the current open Scene(s) and the Project assets.
    *   **Scene:** Searches only in the currently open and loaded Scene(s).
    *   **Project:** Searches only within the project's asset folders (respects folder selections if defined via the 'Select Search Folders...' button; otherwise, searches all project assets).
    *   **Unloaded Scene:** Allows you to search within a specific scene file that is not currently loaded. You'll need to assign a SceneAsset to the `Project Scene to Search` field that appears when this option is selected.
    *   **In Root GameObject:** Confines the search to a specific GameObject and its children. An object field will appear to assign the root object.


*   **Use Smart Search (Toggle):** When enabled, the main search bar becomes a powerful, multi-faceted query field. See the "Smart Search" section above for details.

*   **Filter Only Active GO (Toggle):** (Applies to GameObjects) When checked, results will only include GameObjects that are active in the hierarchy (`activeInHierarchy == true`).

*   **Asset Type:** Filters results by a specific type.
    *   **Any:** Searches for all types.
    *   Specific types include: `GameObject`, `Prefab`, `Material`, `Texture`, `Script`, `SceneAsset`, `ScriptableObject`, `AudioClip`, `AnimationClip`, `Font`, `Shader`.

*   **Tag Filter:** (Applies to GameObjects) Enter a Unity Tag to find GameObjects with that specific tag. Leave empty for no tag filtering.

*   **Layer Filter:** (Applies to GameObjects) Select a Unity Layer to find GameObjects on that specific layer. Defaults to "Everything".

*   **Script Filter:**
    *   For GameObjects (in Scene or Prefabs): Enter the name of a script (e.g., `MyPlayerController`) to find GameObjects that have this script attached as a component.
    *   For Project Assets: If searching for `Script` asset types, this filters by script name. For `ScriptableObject` assets, this filters by the ScriptableObject's class name.

### 3. Search Behavior & Performance

*   **Search Asynchronously (Toggle):**
     When checked (default), searches run in the background to prevent the Unity editor from freezing. A progress bar will be displayed for long operations. 

*   **Instant Results:**
     Search results now appear in the list in real-time as they are found, rather than waiting for the entire search to complete.
        

*   **Select Search Folders... (Button):**
    *   **Purpose:** Opens the **Folder Selection Window** (see section below).
    *   **Functionality:** Allows you to define a specific set of project folders to search within when the "Search In" option is set to "Project". This significantly speeds up project searches if you know where your target assets are located.

*   **Per-Project Settings:**
    *   **Note:** Your search history, favorites, and selected folder settings are saved on a per-project basis. This means you can have different saved settings for each of your Unity projects.

*   **First-Time Caching:**
     The very first time you search for a component in a project, the tool may take a moment to cache all available component types. Subsequent searches will be significantly faster.

### 4. Results Area

*   **High-Performance List:**
     Found items are displayed in a virtualized list, ensuring smooth performance even with thousands of results.
*   **Selection:**
    *   Click an item to select it. This will also attempt to ping it in the Project window or Hierarchy.
    *   The selected item's details and a preview (if available) will appear in the right-hand panel.
*   **Select All (Button):** Selects all items currently visible in the results list in the Unity editor's selection.

### Results Filter Bar

*   **Purpose:** After a search completes, a new filter bar appears above the results. This allows you to dynamically filter the *currently displayed results* without performing a new search.
*   **Usage:** Simply type in the text field to instantly hide any results that do not contain your filter text. This is useful for quickly narrowing down a large set of results.
*   **Clear Button:** The 'X' button on the right of the filter bar will clear the filter text, showing all the original search results again.

### 5. Other Controls & Features

*   **Frame in Scene View (Toggle):** If a GameObject from a scene is selected in the results, and this toggle is active, the Scene View will attempt to frame that GameObject.
*   **Sort By (Dropdown):** Allows sorting of results by various criteria:
    *   `Relevance`: The default sort order.
    *   `Name`: Sorts alphabetically by name.
    *   `Memory Size`: Sorts by estimated memory usage (largest first).
    *   `Complexity`: Sorts by complexity (e.g., vertex count for meshes, largest first).
    *   `Scene First`: Groups all scene objects before project assets.
    *   `Project First`: Groups all project assets before scene objects.
*   **Performance Filters (Toggles):**
    *   `Filter Large Textures`: Filters for textures considered large by area or memory.
    *   `Filter High Poly Meshes`: Filters for meshes with a high polygon count.
*   **History & Favorites (Buttons):**
    *   `History`: Shows a list of recent searches. Clicking an item re-applies that search.
    *   `Favorites`: Shows a list of saved favorite searches.
    *   `Save Favorite`: Saves the current search configuration (query, filters, options) as a favorite.
    *   `Settings (Gear Icon):` Opens the new Settings Window.
*   **Preview and Stats Panel (Right Side):** Displays a preview (for textures, materials, etc.) and detailed statistics for the selected result item.
*   **Frame in Scene View (Toggle):**
     If active, selecting a GameObject from the results will frame it in the Scene View, accurately encompassing the object and all its children.

### 6. Multi-Component Filter

This powerful feature allows you to find GameObjects that have a specific set of components attached.

*   **Enable Filter (Toggle):**
    *   Located at the top of this section, labeled "Filter by All Components Below:".
    *   Check this box to activate the multi-component filter. When active, only GameObjects that possess *all* components added to the list below will appear in search results (in addition to other active filters like name, tag, layer, etc.). Enabling this filter will disable the 'Advanced: Filter by Component Signature' (both "Exact Match" and "Find References to Instance" modes).
    *   This toggle will automatically uncheck itself if the list of components to filter by becomes empty.
    *   If this filter is active, it takes precedence over the single "Script Filter" field for filtering GameObjects by components. The single "Script Filter" will still apply to finding script assets themselves in the project.

*   **Components List Area:**
    *   Displays the components currently added to the filter.
    *   Each component is shown as a label with its name.
    *   **Removing a Component:** Each listed component has a small **'X'** button to its right. Click this 'X' to remove the component from the filter list. The search results will update automatically.

*   **Add Component Filter (Button):**
    *   Clicking this button opens the **Component Selector Window**.

*   **Drag and Drop Scripts:**
    *   You can drag `MonoScript` files (i.e., your C# script assets) directly from Unity's Project window onto the "Components:" list area in the Object Finder.
    *   If the script represents a valid `UnityEngine.Component`, it will be added to the component filter list.

#### Component Selector Window

This window helps you find and select components to add to the filter.


*   **Opening:** Opened via the "Add Component Filter" button in the Object Finder.
*   **Search Components (Text Field):** Type here to filter the list of available components by name or namespace.
*   **Component List:** Displays all available components in your project, grouped by namespace or category (e.g., "Mesh", "Physics", "UI", or custom script namespaces).
    *   Click on a component name in this list to select it.
    *   Upon selection, the Component Selector Window will close, and the chosen component will be added to the filter list in the main Object Finder window.
*   **Close Button:** Closes the Component Selector Window without selecting a component.

**How it Affects Search:**

When the "Filter by All Components Below:" toggle is checked and one or more components are in the list:
*   For **Scene** searches: Only GameObjects that have *every single component* from your list will be shown.
*   For **Project** searches (when Asset Type is `GameObject` or `Prefab`): Only Prefabs that have *every single component* from their root GameObject will be shown.
*   This filter works in conjunction with all other active filters (name, type, tag, layer, folder scope).

---

## Folder Selection Window

This window allows you to specify which project folders the Object Finder should include when performing searches with the "Project" scope. This can significantly speed up searches and help you target specific areas of your project.

*  **Folder Tree View:** Displays a hierarchical view of your project's Assets and Packages folders. Use checkboxes to select which folders to include in searches.
*  **Search Top-Level Folders Only (Toggle):** When checked, the search will only include assets directly inside the selected folders, ignoring sub-folders.
*  **Quick Actions:** Use the Select Visible and Deselect Visible buttons to act on the currently filtered list of folders.
*  **Undo/Redo:** Undo and redo changes to your folder selections.
*  **Keyboard Navigation:** The folder tree and buttons are navigable via the keyboard. 
Enter = Select/Deselect folders, UpArrow/DownArror = Move selection, Left Arrow = Expand Folder, Right Arrow = Collaps folder

### Opening the Window

Click the **"Select Search Folders..."** button in the main Object Finder window to open the Folder Selection Window.

### Purpose

By default, a "Project" scope search in the Object Finder looks through all folders in your "Assets" directory and relevant "Packages". The Folder Selection Window lets you narrow this down. If you select specific folders, only those folders (and their subfolders, by default) will be searched when the "Project" scope is active.

If no folders are explicitly selected in this window (meaning the list is empty after applying), or if you select only the root "Assets" folder, the Object Finder will search the entire "Assets" directory and relevant standard package locations by default when the 'Project' scope is active.

### UI Elements and Usage

*   **Search Folders (Text Field):**
    *   Type here to filter the list of folders displayed in the tree view below. This helps you quickly find a specific folder in large projects.
    *   The filter is case-insensitive and matches against folder names.
        [GIF/Screenshot showing the folder search field filtering the tree would be beneficial here.]

*   **Search Top-Level Folders Only (Toggle):**
    *   When this is checked, the search will only include assets directly inside the selected folders, ignoring any sub-folders.
    *   When unchecked (default), the search is recursive and will include assets in all sub-folders of the selected folders. and also the parent folder of the selected folder.

*   **Folder Tree View:**
    *   **Structure:** Displays a hierarchical view of your project's `Assets` folder. It also lists folders from other project packages (e.g., those installed via the Package Manager from registries, git URLs, or local/embedded packages). The tool attempts to discover these packages and their browsable subfolders. If a package does not appear as expected, ensure it's correctly installed and recognized by Unity's Package Manager.
    *   **Checkboxes:** Each folder in the tree has a checkbox.
        *   **Select/Deselect:** Check a box to include that folder in the search scope. Uncheck it to exclude.
        *   **Parent/Child Behavior:**
            *   Checking a parent folder's box will automatically check all its child folders.
            *   Unchecking a parent folder's box will automatically uncheck all its child folders.
            *   Checking a child folder's box will ensure all its parent folders up to the root are also checked.
            *   Unchecking a child folder will cause its parent to become unchecked *only if all other direct children of that parent are also unchecked*. (Note: Unchecking a child folder makes its direct parent eligible to be unchecked if all of that parent's other children are also unchecked. It doesn't automatically uncheck the parent unless this condition is met.)
    *   **Folder Icons:** Standard Unity folder icons are displayed for easier visual identification.

*   **Refresh Button:**
    *   **Purpose:** Rescans your project directory structure.
    *   **Usage:** Click this if you have recently added, removed, or renamed folders in your project outside of this tool, and you want the tree view to reflect these changes. Your current selections are attempted to be preserved on the rescanned folder structure.

*   **Select Visible / Deselect Visible Buttons:**
    *   **Purpose:** These buttons allow you to quickly select or deselect all folder checkboxes that are currently visible in the folder tree view.
    *   **Usage:**
        *   `Select Visible`: Checks all visible folder checkboxes. If a folder search filter is active, this applies only to the folders that match the filter and are currently displayed.
        *   `Deselect Visible`: Unchecks all visible folder checkboxes, subject to the same filtering considerations.
    *   **Behavior:** These actions respect the parent/child propagation rules (e.g., selecting a visible parent will also select its children, even if some children were filtered out of view). These bulk actions are registered as single steps in the Undo/Redo history.

*   **Undo / Redo Buttons:**
    *   **Purpose:** Allow you to undo or redo changes made to folder selections *during the current session in this window*.
    *   **Usage:** If you accidentally check or uncheck a folder, use "Undo" to revert. "Redo" will reapply an undone action.

*   **Apply Button:**
    *   **Purpose:** Confirms your current folder selections and applies them to the Object Finder tool.
    *   **Usage:** After making your desired selections, click "Apply". The Folder Selection Window will close, and the Object Finder will now use these selected folders for any subsequent "Project" scope searches. These selections are also persisted across Unity editor sessions.

*   **Cancel Button:**
    *   **Purpose:** Closes the Folder Selection Window without applying any changes made to the folder selections during the current session.
    *   **Usage:** If you opened the window but decide not to change the current folder scope, click "Cancel".

### 7. Advanced: Filter by Component Signature

This advanced filter allows you to find GameObjects that precisely match the component "signature" (the exact set and number of components) of a template GameObject, or to find all references to a specific component instance.


*   **Purpose:**
    *   **Signature Match:** Useful for finding GameObjects that are configured with an identical set of components as a reference object, ignoring other differences like component values or hierarchy position.
    *   **Find References:** A powerful tool for locating all GameObjects, Prefabs, and ScriptableObjects that have a direct reference to a specific component instance or even the template GameObject asset itself.

*   **Template GameObject (ObjectField):**
    *   Drag a GameObject from your scene or a Prefab asset from the Project window into this field.
    *   Once a GameObject is assigned, its components will be listed below in the "Template Components" area.
    *   Assigning a new GameObject will replace the current template and update the component list.
    *   Clearing this field (setting it to None) will clear the component list and disable this filter.

*   **Enable Signature Filter (Exact Match) (Toggle):**
    *   Check this box to activate the signature filter.
    *   When active, search results will only include GameObjects that have the exact same types and number of components as currently listed in the "Template Components" area.
    *   This filter, when enabled, takes precedence over the general "Multi-Component Filter" and the single "Script Filter" for component-based matching of GameObjects/Prefabs. It is also mutually exclusive with the "Find References" mode.
    *   The toggle will automatically disable if no template GameObject is assigned or if the list of signature components becomes empty (e.g., by removing all components).

*   **Find References to Selected Component Instance (Toggle):**
    *   **Purpose:** When checked, this mode allows you to select a specific component instance from the "Template Components" list below and search for all other GameObjects, Prefabs, and ScriptableObjects in your project/scene that hold a direct reference to that exact instance.
    *   **Activation:** To use this mode, first drag a GameObject to the "Template GameObject" field. Then, select one of its components from the "Template Components" list that appears (or the "GameObject" entry itself). Finally, check this toggle and perform a search.
    *   **Mutual Exclusivity:** Enabling this mode will automatically disable the "Enable Signature Filter (Exact Match)" mode, and vice-versa. You can use one or the other, but not both simultaneously.
    *   If no template GameObject is assigned, this toggle cannot be effectively enabled.

*   **Template Components (Scrollable List):**
    *   Displays components derived from the "Template GameObject". Its behavior depends on the active advanced filter mode:
        *   **When "Enable Signature Filter (Exact Match)" is active:** Lists component *types*. You can remove types from this list using the 'X' button to refine the signature to match. Re-dragging the template GameObject resets this list to its original state.
        *   **When "Find References to Selected Component Instance" is active:** Lists the template `GameObject` itself, followed by all of its actual component *instances* (e.g., "BoxCollider (ID: 12345)"). Click on an instance in this list to select it as the target for the reference search. Only one instance can be the target at a time. The selected component instance will be visually highlighted in the list. The 'X' buttons are not active in this mode for this list.


*   **How it Affects Search:**
    *   **When "Enable Signature Filter (Exact Match)" is active** and there's a valid list of signature components:
        *   The tool searches for GameObjects (in scenes or as Prefabs in the project) that have *exactly* the same set of component types as listed, and the *same number* of components. The order of components on the target GameObject does not matter.
        *   For example, if your signature list is `[Transform, BoxCollider, Rigidbody]`, a GameObject with only `[Transform, BoxCollider]` will NOT match. A GameObject with `[Transform, BoxCollider, Rigidbody, AudioSource]` will also NOT match.
    *   **When "Find References to Selected Component Instance" is active:**
        *   The tool searches all applicable GameObjects (in scenes or prefabs) and **ScriptableObjects**.
        *   It looks for any serialized field or property that directly references the *exact `GameObject` or component instance* you selected from the template.
        *   **Results Display:** Results are shown in the format: `Found In Asset/Object > Referencing Component/Script > Field Name`.
        *   Clicking a result will ping the GameObject or Asset that *contains* the reference.
        *   The main search text field will filter these reference path results. The tool is also robust in handling stale references (e.g., if a scene is unloaded), and will prompt you to reload the scene if necessary.

*   **Saving and Loading (History/Favorites):**
    *   The list of component type names for the signature filter, the name of the template GameObject (if assigned), and its asset path (if it was a prefab) are saved with search presets.
    *   The state of the "Find References to Selected Component Instance" toggle is also saved with presets.
    *   When loading a preset:
        *   The component types for the signature are restored.
        *   The "Find References..." toggle state is restored.
        *   If the template GameObject was an asset and can still be found at its saved path, it will be re-linked in the `ObjectField`. Otherwise, the filter will still work based on the saved component types (for signature match mode), but the `ObjectField` might be empty.
        *   For "Find References" mode, the *specific component instance* you selected as the target is **not** saved directly (due to the volatility of instance IDs). You will need to **re-select the specific component instance** from the "Template Components" list before performing the reference search again. A message might appear in the results area prompting you to select a component instance if the mode is active but no target is chosen.


## Settings Window
Accessible via the gear icon in the main window, the Settings Window allows for deep customization.
### General Tab
*   **Default Preset:** Set the current search configuration as the default preset that loads when the Object Finder window is first opened.
*   **Load Last Preset on Startup:** If enabled, the tool will automatically load the last search you performed when it starts up, overriding the default preset.
*   **Max History Items:** Control how many recent searches are saved in the history.
*   **Highlight Color:** Customize the highlight color used for keyboard navigation in the results list.
### Features Tab
Enable or disable entire feature sections (Multi-Component Filter, Advanced Filters, Custom Filters) from the main window's UI. This is useful for simplifying the interface if you don't use certain advanced features.
### Manage Presets Tab
View your lists of Favorites and History.
*   **Rename Presets:** Click on any favorite preset's name to rename it directly within the settings window.
*   **Clear History:** A button to clear all saved search history items.
### Help Tab
Provides quick reference guides and information about the tool's features.