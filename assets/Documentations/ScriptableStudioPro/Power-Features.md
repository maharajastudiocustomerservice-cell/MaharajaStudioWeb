# Power Features

Unlock the full potential of **Scriptable Studio Pro** with these advanced tools.

---

## Formulas

Just like in Excel, you can calculate values dynamically using formulas.

- **Syntax**: Start any numeric or string field with `=`.
- **References**: Use `[FieldName]` to reference other fields in the same row.
- **Operators**: `+`, `-`, `*`, `/`, `^` (power), `%` (modulo).

### Examples

```
=[Level] * 100             → Sets value to Level × 100
=[Strength] + [Agility]    → Sums two stats
=[BaseDamage] * (1 + [BonusMultiplier])
```

> [!NOTE]
> Formulas are evaluated when you press Enter or click the **Refresh** button. The result is written back to the field as a concrete value.

### Formula Mode

Toggle **Formula Mode** in the main toolbar to display raw formula strings in the grid cells instead of their evaluated results, making batch formula editing easier.

---

## Smart Fill

Auto-complete sequences of data across multiple rows in seconds.

1. Select a range of cells (vertical or horizontal, or an entire column).
2. Click the **✨ Smart Fill** button in the toolbar.
3. Choose a pattern based on the field type:

### Numeric Modes

| Mode | Description |
|:---|:---|
| **Linear** | 1, 2, 3, 4... (standard arithmetic progression) |
| **Incremental** | Start at X, add Y each step |
| **Random Range** | Random value between Min and Max |
| **Multiplier** | Multiply the previous value by X each step |
| **Curve** | Use an `AnimationCurve` to define the distribution |

### String Modes

| Mode | Description |
|:---|:---|
| **Pattern** | Use `{i}` (index) and `{old}` (current value) — e.g., `Item_{i}` → Item_1, Item_2... |
| **Search & Replace** | Bulk replace text within the selection |
| **Prefix / Suffix** | Add text to the start or end of each value |
| **GUID** | Generate unique identifiers for each row |

### Other Modes

| Mode | Description |
|:---|:---|
| **Boolean Pattern** | e.g., `TF` = True, False, True... |
| **Boolean Random** | Random true/false per row |
| **Color Gradient** | Blend between two colors across the selection |
| **Color Random** | Random color per row |

### Universal Type Support *(v3.0)*

Smart Fill now correctly initializes and applies values for **all primitive types** supported by the new parser:
- `uint`, `byte`, `sbyte`, `short`, `ushort`, `ulong`, `decimal`, `char`
- These types are clamped to their valid range automatically.

---

## Smart Rename

Rename hundreds of assets instantly based on their own data.

1. Ensure you are in **Edit Mode** (file names are affected).
2. Right-click on the **column header** of the field you want to use as the name source (e.g., `ItemName`).
3. Select **"Set Name from 'ItemName'"**.
4. The asset filenames update to match the field values immediately.

---

## Import / Export

Move data between Unity and external tools.

### Supported Formats

| Format | Direction | Notes |
|:---|:---|:---|
| **CSV** | Import / Export | Standard comma-separated values. Handles quoted fields. |
| **JSON** | Import / Export | Field-name keyed data. |
| **SQL** | Export | Generates `INSERT INTO` statements for database tools. |
| **Google Sheets** | Import / Export | Copy/paste via clipboard (TSV) or direct URL import. |

### Import Tab

- **Replace Toggle**: Wipes existing rows before importing if checked.
- **Drag & Drop**: Drop a `.csv`, `.json`, or `.sql` file onto the Import window to parse it immediately.
- **Google Sheets (URL)**: Paste a published CSV link to download directly.
- **Google Sheets (Clipboard)**: Copy cells in Sheets → click **Paste & Import**.

### Export Tab

- **Save as...**: Exports the current grid data to a file of the chosen format.
- **Copy to Clipboard**: For Google Sheets, copies TSV data for direct paste into a spreadsheet.

---

## Undo / Redo

The tool features a **custom undo stack** that is completely independent of Unity's standard undo system. This gives it far better performance and reliability for batch operations.

| Shortcut | Action |
|:---|:---|
| `Ctrl + Z` / `Cmd + Z` | Undo |
| `Ctrl + Y` / `Cmd + Shift + Z` | Redo |

### What is Tracked

- Individual value changes in the grid and detail panel.
- Row additions, removals, and reordering.
- Drag-and-drop batch operations.
- Naming pattern changes.
- And more

---

## Validator

Catch data problems before they ship, using the advanced **Validation Window**.

Open it via the **🐞 (Validate)** button in the main toolbar.

### Rule Types

| Rule Type | Description |
|:---|:---|
| **Built-in** | Detect null references, empty strings, out-of-range values |
| **Formula** | Write custom expressions (e.g., `[Health] > 0 && [MaxHealth] >= [Health]`) |
| **Regex** | Pattern-match string fields (e.g., asset IDs must match `^[A-Z]{3}_\d{4}$`) |

Each failing instance is listed with its field name, value, and rule that was violated.

---

## Native Drawn Types *(New in v3.0)*

This is a **Settings** feature, surfaced here because it directly affects power users working with custom types.

The tool maintains a list of **Native Drawn Types** — fully-qualified type names that are always rendered using Unity's built-in property drawer in the Detail Panel, bypassing the tool's own field builder.

The list is in **Settings › Native Drawn Types**. You can add any type here by its fully-qualified name (e.g., `MyNamespace.MyCustomWrapper`).

**Auto-detection** handles most cases: any type with a `CustomPropertyDrawer`, any `SerializableDictionary`, and all `UnityEngine.Localization.*` types are detected automatically without any configuration.

---