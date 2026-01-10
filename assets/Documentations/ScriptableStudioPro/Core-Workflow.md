# Core Workflow

This page details the primary interface and workflows of **Scriptable Studio Pro**.

## The Main Interface

The window is divided into three main sections:
1. **Sidebar (Left)**: Lists all `ScriptableObject` types in your project.
2. **Grid (Center)**: The main workspace where you edit data.
3. **Toolbar (Top)**: Mode selection and global tools.

## Working with the Grid

The grid is the heart of the tool. It displays your assets in a spreadsheet-like view.

### Sorting & Filtering
- **Sort**: Click any column header to sort ascending/descending.
- **Filter**: Use the search bar to filter rows.
  - **Simple Text**: `Sword` matches any item with "Sword" in the name.
  - **Advanced Syntax**:
    - **Logical**: `&&` (AND), `||` (OR). Example: `[Cost] < 50 && [Type] == "Fire"`.
    - **Comparison**: `==`, `!=`, `>`, `<`, `>=`, `<=`, `:` (contains).
    - **Nested Fields**: `[Stats.Health] > 100` or `[Inventory[0]] == "Potion"`.
    - **Special**: `[Model] == {null}` to find missing references.

### Reordering
- Drag and drop rows by their index number (far left column) to reorder them.
- **Note**: Reordering works in both Create and Edit modes. In Edit Mode, it changes the order in the list but doesn't affect file names unless you rename them.

### Bulk Editing
You can edit multiple cells at once:
1. Select multiple rows (Ctrl/Cmd + Click or Shift + Click).
2. Edit a value in *any* of the selected rows.
3. The change will apply to **all** selected rows.

## Context Menu Actions

Right-click on any row (or the index number) to access powerful actions:

- **Ping Asset**: Highlights the file in the Project window.
- **Copy/Paste Values**: Copy data from one instance to another.
- **Duplicate Row**: Creates an exact copy of the selected instance.
- **Smart Rename**: (Edit Mode) Renames the instance based on a string field (e.g., "Set Name from 'ItemName'").
- **Insert Row Above/Below**: Adds a blank row at a specific position.

## Create Mode vs. Edit Mode

### Create Mode
- **Purpose**: Rapidly creating *new* assets.
- **Behavior**: Data exists only in memory.
- **Save**: You must click **Create Assets** to write files to disk.
- **Naming**: Files are named based on the **Naming Pattern** (e.g., `{TYPE}_{#}`).

### Edit Mode
- **Purpose**: Managing *existing* assets.
- **Behavior**: Changes are written to the asset files when **Update Linked Assets** pressed.
- **Import**: Use the **Import** buttons to load assets into the grid.
  - **Import All**: Loads every asset of this type found in the project.
  - **Import Selected**: Loads only the assets currently selected in the Project window.
  - **Save**: You must click **Update Linked Assets** to write files to disk.
