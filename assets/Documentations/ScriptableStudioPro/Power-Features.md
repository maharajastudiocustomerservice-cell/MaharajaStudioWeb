# Power Features

Unlock the full potential of **Scriptable Studio Pro** with these advanced tools.

## Formulas

Just like in Excel, you can use formulas to calculate values dynamically.

- **Syntax**: Start any text field with `=`.
- **References**: Use `[FieldName]` to reference other fields in the same row.
- **Math**: `+`, `-`, `*`, `/`, `^` (power), `%` (modulo).

### Examples
- `=[Level] * 100` -> Sets value to Level * 100.
- `=[Strength] + [Agility]` -> Sums two stats.
- `=[BaseDamage] * (1 + [Bonus])`

> [!NOTE]
> Formulas are evaluated when you press Enter or click the **Refresh** button. The result is written to the field.

## Smart Fill

Auto-complete sequences of data across multiple rows.

1. Select a range of cells (vertical or horizontal).
2. Click the **✨ Smart Fill** button in the toolbar.
3. Choose a pattern based on the field type:

### Numeric Modes
- **Linear**: 1, 2, 3, 4... (Standard progression)
- **Incremental**: Start at X, add Y each step.
- **Random Range**: Random value between Min and Max.
- **Multiplier**: Multiply previous value by X.
- **Curve**: Use an animation curve to define the value distribution.

### String Modes
- **Pattern**: Use placeholders like `{i}` (index) and `{old}` (current value).
  - Example: `Item_{i}` -> Item_1, Item_2...
- **Search & Replace**: Bulk replace text within the selection.
- **Prefix/Suffix**: Add text to the beginning or end.
- **GUID**: Generate unique IDs.

### Other Modes
- **Boolean**: **Pattern** (e.g., `TF` = True, False, True...), **Random**.
- **Color**: **Gradient** (blend between colors), **Random**.

## Smart Rename

Rename hundreds of assets instantly based on their data.

1. Ensure you are in **Create Mode** (or Edit Mode if you want to rename files).
2. Right-click on the header of the column you want to use as the name source (e.g., `ItemName`).
3. Select **Set Name from 'ItemName'**.
4. The instance names (and filenames) will update to match the value in that column.

## Import / Export

Move data between Unity and external tools.

### Supported Formats
- **CSV / JSON**: Standard formats for backup or external editing.
- **SQL**: Generate SQL INSERT statements for database integration.
- **Google Sheets**:
  - **Clipboard (Recommended)**: Copy cells in Sheets, click **Paste & Import** in the tool.
  - **URL**: Download directly from a published Google Sheet CSV link.

## Undo / Redo

The tool features a custom **Undo System** that is separate from Unity's standard undo stack for better performance and reliability.

- **Undo**: `Ctrl + Z` (Cmd + Z)
- **Redo**: `Ctrl + Y` (Cmd + Shift + Z)

It tracks:
- Value changes
- Row additions/removals
- Reordering
- Bulk operations
