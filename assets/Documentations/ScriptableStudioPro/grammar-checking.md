# Grammar Checking

The Grammar Checking feature in Scriptable Studio Pro allows you to quickly proofread, spell-check, and fix grammatical errors across your ScriptableObject string fields directly within the editor. It is powered by **LanguageTool**, an advanced, open-source proofreading software.

This tool is designed to review hundreds of items in a batch, presenting the issues in an easy-to-read review panel where you can selectively apply or ignore corrections.

## Quick Overview

1. **Setup Provider**: Follow the `setup-grammar-providers.md` guide to start your local Docker server or connect to the LanguageTool Cloud.
2. **Create a Profile**: Create a Grammar Profile (`Create > Scriptable Studio Pro > Grammar > Grammar Profile`) and assign it in **Settings > Grammar Services**.
3. **Open the Grammar Window**: Select the rows you want to check in the main grid, and click the **📝 Grammar Check** button in the toolbar.
4. **Scan & Apply**: Click **Check Grammar** to scan the fields, review the suggestions, and click **Apply** to fix typos instantly!

---

## Grammar Check Window

This window is your main interface for scanning strings and reviewing suggestions.

### Left Pane: Setup & Scope

- **Profile**: Select the Grammar Profile to use for this session. The badge will indicate if you are connecting to a local Docker container or the cloud.
- **Fields to Check**: Only fields of type `string` are displayed here. Check the fields you want the tool to scan (e.g., `description`, `dialogue`).
- **Options**:
  - **Skip Empty Fields**: Ignores empty or null fields, saving processing time.
- **Scope**: Choose whether to scan only the **Selected Items** or **All Items** in the grid.

### Right Pane: Results & Review

When you click **Check Grammar**, the tool scans all selected fields in parallel. The results are displayed in the right pane.

- **Clean Rows**: Rows with no grammar issues are collapsed into a small `✓ No issues` badge to save space.
- **Issue Rows**: If issues are found, they are displayed as a card.
  - **Context**: A preview of the original text is shown.
  - **Suggestions**: Each grammar issue gets its own row.
    - **Category Badge**: Shows the type of issue (e.g., `TYPO`, `GRAMMAR`, `STYLE`).
    - **Highlight**: The misspelled or incorrect word is highlighted in red.
    - **Replacement**: The suggested fix is shown in green. If there are multiple suggestions, a dropdown menu is provided.
  - **Apply / Skip**: You can click **Apply** to stage the fix, or **Skip** to ignore it. You can undo a staged fix at any time before closing the window.

### Bottom Bar

- **Apply All Suggestions**: Automatically stages the top replacement for every single issue found across all rows.
- **Check Grammar**: Starts the scanning process.

> [!NOTE]
> **Safety and Undo**
> Staging a fix using "Apply" immediately updates the string in memory and registers it with Unity's Undo system. If you make a mistake, you can simply press `Ctrl+Z` (or `Cmd+Z`) in the main editor to revert the changes.
