# 3. Decorators & Visual Aids

These attributes help you clarify and visually annotate your fields with hints, warnings, titles, spacers, and custom formatting.

### `[Header(string name)]`
Adds a large, styled header line above the field.

### `[Title(string text, string subtitle)]`
A more advanced header that supports subtitles, custom sizing, formatting, and alignment.

### `[Note(string message)]` / `[InfoBox(string message)]`
Adds a help box or descriptive note above or below the field. Highly configurable to visually distinct colors like 'Info', 'Warning', or 'Error'. 
Useful for explaining complex or destructive configurations to the user.

### `[MSSpace(float height)]`
A custom space attribute that safely applies vertical pixel spacing above fields, but correctly handles ModularMonoBehaviourEditor method rendering and groups compared to Unity's native `[Space]`.

### `[HideLabel]`
Hides the inspector prefix label for a field, making it take up the entire row width.

### `[LabelText(string text)]`
Overrides the displayed prefix label for a property with the provided custom text. Useful for making variable names more human-readable in the Inspector without changing the underlying code.

### `[RichTextLabel(string text)]`
Provides a rich text prefix label, allowing for dynamic coloring, bolding, and formatting using Unity's subset of HTML styling tags (e.g. `<b>`, `<i>`, `<color=red>`).

### `[ToolTip(string text)]`
Adds a custom tooltip that displays whenever the user hovers their mouse over the property label or field within the inspector.

### `[GUIColor(float r, float g, float b, float a)]` / `[GUIColor(string hexColor)]`
Tints the background GUI color of a specific field in the Inspector. Accepts either RGBA float values or HTML hex color strings (e.g., "#FF0000").

### `[SuffixLabel(string label)]`
Appends a small contextual label to the far right of the field (e.g. "px", "sec", or "meters") to help document expected units.

### `[LabelWidth(float width)]`
Explicitly overrides the prefix label width for the target field, with responsive shrinking and ellipsis when space is constrained.

### `[LabelLayout(LabelLayoutMode mode, float breakpoint = 0f)]`
Controls how the field label and input control adapt in narrow windows and multi-column layouts:
- `AdaptiveInline`: Compact content-fitted label with a tight 4px gap. Eliminates empty dead space.
- `ResponsiveStack`: Automatically stacks vertically (label on top, full width input below) when width drops below the breakpoint (default 160px).
- `AlwaysStacked`: Always places label on top, giving 100% width to the input field.
- `StandardUnity`: Native Unity fixed-width alignment.
Can also be set globally in `Preferences > Maharaja Studio > Inspector Layout` or at group level via `[HorizontalGroup(LayoutMode = ...)]`.

### `[Indent(int amount)]`
Forces a field to indent by the specified amount, overriding standard nesting.

### `[Button(string label)]`
Marks a method with a clickable UI Button in the Inspector. Supports rich layouts, colors, custom height, alignments, and icons.

### `[ToolBarToggle]`
Renders boolean and enum fields as interconnected Toolbar buttons instead of traditional checkboxes or dropdowns. 

### `[ConfirmationDialog(string title, string message)]`
Forces a confirmation popup when a field is changed or a button method is clicked. Important for destructive operations.

### `[CopyPaste]`
Injects quick "Copy" and "Paste" context menu buttons adjacent to a serialized field, allowing users to deeply copy objects or arrays without navigating custom copy/paste workflows.

### `[ColorPalette]`
Enhances the Unity Color picker with presets from project-wide color schemes and palettes.
### `[SemanticVersion]`
Applied to a `string` field. Formats the string visually into three separate integer blocks (Major.Minor.Patch) natively in the Inspector, complete with tiny up arrows `▲` to quickly bump version numbers without tedious string typing.

### `[HighlightIfNull(string hexColor)]`
If the assigned Object reference field remains `null`, the field outline vigorously pulses in neon color (default red, customizable via hex string) natively in the Inspector, grabbing the designer's attention to fill required dependencies before encountering runtime Exceptions.

### `[VisualDataChart(ChartType type, float height, string hexColor)]`
Automatically draws a gorgeous, native UI Toolkit mini bar chart evaluating an array of numbers (`int[]` or `float[]`) directly in the inspector. Updates smoothly in real-time as you tweak the underlying collection elements!

### `[TimeSpanSlider(float minSeconds, float maxSeconds)]`
The underlying variable in code remains a `float` (seconds), but the Inspector renders a slider alongside a dynamically formatted string element that automatically evaluates the seconds into easily human-readable time spans (e.g., "1h 30m" or "45s").

### `[LayerMaskToggles]`
Renders default Unity `LayerMask` dropdowns explicitly as a grid of pill-shaped toggle buttons instead of a multi-select menu. It allows the developer to instantly see and intuitively manipulate exactly which layers are enabled/disabled at a glance without ever opening a dropdown!

---

### `[ComputedProperty(string formula, string label, string colorHex, bool showFormula)]`
Renders a live, read-only calculated value row derived from a formula string using other serialized fields as variables (e.g. `"health * 0.15 + armor"`). Evaluated via reflection + arithmetic at editor time. Great for displaying compound stats without writing extra properties.

### `[IconButton(string iconName, string methodName, string tooltip, float buttonSize, bool showAtRight)]`
Injects a tiny icon-only action button inline alongside the field. Uses Unity's built-in icon names (e.g. `"d_Refresh"`, `"d_Search Icon"`). Invokes the named method on click. Stacks with any other attributes.

### `[DeltaTracker(string colorHex, int decimals, bool alwaysShow)]`
Tracks a numeric field's value at Edit Mode and shows how much it drifted after the Play Mode session ends. Renders a colored `Δ +X.XX` badge beside the value, giving immediate regression insight after gameplay tuning.

### `[AutoFill(SearchScope scope, string tag, bool overwrite, bool showBadge)]`
When a serialized object reference is empty (or `overwrite` is true), the Editor automatically hunts for a matching component using `Self`, `Children`, `Parent`, or `Scene` scope. Shows a ✔/**⚠** badge indicating whether the auto-fill succeeded.

### `[RandomSeedGenerator(int historySize, string chipColor, bool useUnityRandom)]`
Added to any `int` field used as a procedural RNG seed. Adds a 🎲 dice button to generate a fresh cryptographic random seed, and stores the last `historySize` seeds as clickable pill-chips (persisted via `EditorPrefs`) so you can rapidly re-apply seed values you liked.

---

### `[Breadcrumb(params string[] path)]`
Renders a styled breadcrumb navigation trail above the field (e.g. `Systems › Combat › Damage`). Helps designers orient themselves within massive scripts with 50+ fields by providing contextual categorization.

### `[FieldCooldown(float cooldownSeconds, string colorHex, string message)]`
After a field value is changed, the field becomes temporarily greyed-out and non-editable for the specified duration, with a countdown progress bar and optional message. Prevents accidental rapid modifications to sensitive fields.

### `[LinkedField(string otherFieldName, LinkMode mode, bool startLinked)]`
Chains two numeric fields together with a 🔗/🔓 lock toggle. When linked, editing one field automatically mirrors the value to the other. Supports `Proportional`, `Additive`, and `Mirror` link modes.

### `[FieldBookmark(string groupName)]`
Adds a ⭐ star toggle icon next to the field, marking it as a bookmarked/important field. The star acts as a visual indicator for designers to identify the most critical fields in large inspectors.

### `[CompareWith(string otherFieldName, ComparisonDisplay display, string colorHex)]`
Draws a live visual comparison indicator between two numeric fields showing `▲ Greater`, `▼ Less`, `═ Equal`, a percentage ratio, or a direct ratio. Updates automatically when either value changes.

### `[UnitConverter(string fromUnit, string toUnit, float conversionFactor, int decimals)]`
Displays a read-only inline conversion next to a numeric field (e.g. meters → feet, kg → lbs). The raw data stays in the original unit; the converted value is display-only for designer convenience.

### `[EditCounter(string colorHex, bool persistent)]`
Tracks and displays how many times a field has been modified during the current editor session (or persistently across sessions via `EditorPrefs`). Shows a `✏️ N` badge to identify over-tweaked fields.

### `[ClampWarning(float softMin, float softMax, string message, string colorHex)]`
Unlike `[Range]` which hard-clamps, this allows any value but shows a pulsing amber `⚠` warning with a message when the value exceeds the soft recommended range. Respects creative freedom while preventing accidental extremes.

---

### `[StatusLight(float greenThreshold, float yellowThreshold, bool invertDirection, float lightSize)]`
Adds a tiny colored LED dot (🟢🟡🔴) next to a numeric field that changes color based on value thresholds. Use `invertDirection` to flip the logic for values where lower is better (e.g., latency).

### `[FieldTag(string tagName, string colorHex, string textColorHex)]`
Injects a small colored pill badge (like GitHub issue labels) inline next to the field. Supports stacking multiple tags on one field via `AllowMultiple`. Perfect for classifying fields as `"Experimental"`, `"Legacy"`, `"Performance"`.

### `[MiniMap(float mapSize, float range, string dotColorHex, string gridColorHex, bool showCoordinates)]`
For `Vector2` or `Vector3` fields — draws a tiny 2D grid map below the field with crosshair lines and a colored dot showing the position in world space. Updates in real-time as values change.

### `[ToggleLeft(string label)]`
For `bool` fields — moves the checkbox to the left side of the label instead of Unity's default right-side placement. Optionally overrides the label text.

### `[FieldTimestamp(string colorHex, bool showRelative)]`
Displays a small timestamp showing when the field was last modified (e.g., `"edited 2h ago"` or `"edited 14:30 Mar 05"`). Persisted in `EditorPrefs` per-user. Helps teams track stale or recently-changed values.

---

### `[OnValueChanged(string methodName)]`
Triggers a method automatically whenever the field's value is modified in the Inspector.

**Properties:**
- `MethodName`: The method to invoke. Can be `Method()`, `Method(T newValue)`, or `Method(T oldValue, T newValue)`.
- `IncludeUndo`: (bool) Whether to trigger on Undo/Redo operations. Default: `true`.

---

### `[ButtonGroup]`
Groups several methods into a horizontal row of styled buttons.

**Properties:**
- `GroupName`: Unique ID for the button row.
- `ButtonHeight`: Height of the buttons in pixels.
- `Style`: `Normal`, `Flat`, `Outlined`, `Ghost`.
- `Alignment`: `Left`, `Center`, `Right`, `Expand`.
