# Configuration

Customize **Scriptable Studio Pro** to fit your workflow.

## General Settings

Access settings via `Tools > Scriptable Studio Pro > Settings`.

### Folder Rules
- **Default Folder Mode**:
  - *Root*: Saves all assets in the root of the selected folder.
  - *Type Subfolder*: Creates a subfolder for each type (e.g., `.../Items/`, `.../Enemies/`).
- **Ping Folder**: If enabled, Unity will highlight the folder after creating assets.

### Naming Patterns
Define how new assets are named by default.
- **Pattern**: `{TYPE}_{i}`
- **Placeholders**:
  - `{TYPE}`: The class name.
  - `{i}`: Incrementing number (1, 2, 3).
  - `{ii}`: Two-digit number (01, 02, 03).
  - `{iii}`: Three-digit number (001, 002, 003).

### Other Settings
- **Visuals**: Toggle **Grid Lines** or **Assembly Names** (e.g., `[Assembly-CSharp]`).
- **Workflow**: Enable **Link Dragged Assets** to automatically assign references when dragging assets into Create Mode.
- **Safety**:
  - **Confirm Deletion**: Toggle the warning dialog when removing rows.
  - **Max Undo Objects**: Limit the undo history size (default 1000) for performance.

## Shortcuts

Customize hotkeys for common actions.

1. Go to `Scriptable Studio Pro > Setting > Shortcuts`.
2. The **Visual Keyboard** shows all current bindings.
3. Select an action from the list on the left.
4. Click a key on the virtual keyboard to rebind.
5. Use the **CTRL / SHIFT / ALT** toggles to add modifiers.

**Defaults:**
- `Ctrl+S`: Save / Create Assets
- `Ctrl+D`: Duplicate Row
- `Delete`: Remove Row
- `F2`: Rename Row(Edit mode only)

## AI Configuration

See [AI Assistant](AI-Assistant.md) for details on configuring AI providers.
