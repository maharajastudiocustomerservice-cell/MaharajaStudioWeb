# 7. Conditionals and Logic

These attributes provide intelligent ways to hide, disable, or trigger custom layout and behavioral logic when field values change.

## Visibility & Disablement

### `[ShowIf(string conditionName)]` / `[HideIf]`
Conditionally hides the field or property dynamically based on another field or boolean method in the serialized object. Cleans up inspector clutter based on contexts (e.g., Only display "Walk Speed" if `canMove` equals `true`).

### `[ConditionalField(string condition, object value)]`
An advanced conditional visibility/interactivity attribute. Supports single or multiple conditions, comparison operators, value matching, disable-instead-of-hide, animated transitions, and custom disabled styling configurations. Highly flexible.

### `[ButtonConditional]`
Conditionally enables or disables an inspector-drawn `[Button]` based on the serialized system state.

### `[ReadOnly]` / `[ReadOnlyConditional]`
Locks the field from being edited in the Inspector while still drawing its current value, preventing accidental modifications of crucial or mathematically calculated inspector properties. Conditionally locked based on play-mode rules or custom logic!

### `[ShowInInspector]`
Displays a field or property in the Inspector dynamically. Can be used on inherently private fields, `[NonSerialized]` fields, and calculated C# `get {}` properties. Supports rich styling like `LabelColor`, `ValueColor`, and `BackgroundColor`.

---

## Code Inspection

### `[ShowMethod]`
Displays the actual C# source code of a method directly in the Inspector. This is incredibly useful for reviewing logic without opening a code editor.

**Features:**
- **Syntax Highlighting:** Automatically highlights keywords, types, strings, and comments.
- **Source Extraction:** Reads the `.cs` file from disk to find the method body.
- **Collapsible:** Wraps the code in a foldout to save space.

**Properties:**
- `Theme`: `Hacker`, `Light`, `Monokai`.
- `FontSize`: Customize code readability.
- `ShowLineNumbers`: (bool).

---

### `[HideMethod]`
The inverse of `ShowMethod`. It provides a button that, when clicked, reveals the source code of the decorated method. Ideal for hiding complex logic that is only occasionally reviewed.

---

## Editor Event Injection

### `[OnInspectorInit]`
Triggers a method automatically the very first time the custom Editor for the object is drawn. Useful for one-time initialization setups, fetching references automatically, or caching data without using heavy `OnValidate` calls. The target method must have zero parameters.

### `[ContextMenuItem(string name, string methodName)]`
Adds a quick-action context menu item to a specific field. When the user right-clicks the property in the Inspector, unity displays a context menu with `name`. Clicking it invokes `methodName` on the target object. Great for exposing quick utility functions (like "Randomize", "Reset", or "Generate ID") directly on the relevant data.
