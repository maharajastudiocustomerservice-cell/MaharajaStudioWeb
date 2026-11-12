# Adding & Editing Attributes Visually

> **Module:** MSUltimate Inspector Customizer — Editor Windows  
> **Topic:** The AttributePicker Window, Attribute Card Lifecycle, Parameter Reflection, Stack Ordering, and Code Attribute Exploration

---

## 1. The Attribute Discovery & Selection Pipeline

Visual inspector customization begins by selecting a member in `InspectorCustomizerWindow` and clicking the green **`+ Add Attribute`** button (or pressing `Ctrl+Shift+A`). This launches the dedicated **`AttributePickerWindow`**, which indexes all 444+ MSUltimate attributes across Core and all installed Addons.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  🔍 Search attributes... (e.g. 'Slider', 'Header', 'HideIf', 'Progress')               │
│  Scope: [All] [Field] [Method] [Class]                    [x] Keep Open On Selection   │
├──────────────────────┬─────────────────────────────────────────────────────────────────┤
│  NAV SECTIONS        │  ProgressBar                                                    │
│  ★ Quick Access      │  Namespace: MaharajaStudio.MSUltimate.Runtime                   │
│  ★ Recents           │  Target: Field | AllowMultiple: False | Inherited: True         │
│  ─────────────────── │  Renders numeric values (int, float, double) as customizable,   │
│  MODULES             │  animated visual progress bars with dynamic colors and borders. │
│  • Core: Fields      │  Parameters: Min (float), Max (float), Color (Color), Height    │
│  • Core: Decorators  │  ─────────────────────────────────────────────────────────────  │
│  • Core: Layouts     │  MinMaxSlider                                                   │
│  • AnimatedAttributes│  Two-handled dual-slider for Vector2 range selection.           │
│  • ComponentDesigner │  Parameters: MinValue (float), MaxValue (float), ShowInputs     │
│  • ValidationModule  │  ─────────────────────────────────────────────────────────────  │
│  • ToolBox-Vol1      │  CustomSlider                                                   │
│                      │  Enhanced numeric slider with min, max, and step increments.     │
└──────────────────────┴─────────────────────────────────────────────────────────────────┘
```

### 1.1 AttributePicker Navigation & Controls
- **Debounced Live Search:** Text search executes with a 150ms debounce, matching attribute names, aliases, descriptions, and parameter names.
- **Scope Filter Bar:** Restricts visible attributes to only those compatible with the currently selected member:
  - `Field`: Shows field-level presenters, formatters, and validators (`[ProgressBar]`, `[Range]`, `[MinMaxSlider]`).
  - `Method`: Shows method action attributes (`[Button]`, `[ButtonGroup]`, `[IconButton]`).
  - `Class`: Shows component-level frame and card stylers (`[ComponentHeader]`, `[ComponentBorder]`, `[ComponentBackground]`).
- **Favorites & Star Pinning (`★`):** Click the star icon next to any attribute in the catalog to pin it into the **Quick Access** drawer. Favorites persist in developer `EditorPrefs`.
- **Keep Open On Selection Toggle:** When enabled, selecting an attribute does not close the picker window. This enables rapid attribute stacking (e.g. clicking `[BoxGroup]`, `[LabelStyle]`, and `[ProgressBar]` in rapid succession).

---

## 2. Anatomy of an Attribute Card in the Deck

When an attribute is added to a member, it instantiates as a draggable **Attribute Card** inside the right-hand column:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ ☰  [ProgressBar]                                  [^] [v]  [👁]  [⋮]  [✕]              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  __ctor_min_Single:       [ 0.0          ]                                             │
│  __ctor_max_Single:       [ 100.0        ]                                             │
│  SliderColor:             [ ■ #33CC66    ]                                             │
│  Height:                  [ 22           ]                                             │
│  ShowPercentage:          [✓]                                                          │
│  MaxMember:               [ maxHealth    ]  (Dynamic ceiling companion)                │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2.1 Card Header Controls
| Control Icon | User Action | Detailed Operational Behavior |
| :---: | :--- | :--- |
| **`☰`** | **Drag Handle** | Click and drag vertically to smoothly reorder attribute execution priority. The underlying drawer pipeline renders attributes in top-to-bottom stack sequence. |
| **`[^]` / `[v]`** | **Nudge Order** | Move the attribute up or down by one slot without dragging. |
| **`[👁]`** | **Mute / Disable Toggle** | Sets `IsDisabled = true`. The attribute remains stored in the profile but is completely bypassed by `ModularMonoBehaviourEditor` during draw-time. Perfect for A/B testing visual styles. |
| **`[⋮]`** | **Attribute Options Menu** | Opens the comprehensive **Card Context Menu** (see Section 2.2). Also triggers on right-clicking the card header. |
| **`[✕]`** | **Remove Attribute** | Permanently deletes the attribute override from the member profile with full Unity Undo tracking. |

### 2.2 The Card Options Menu (`[⋮]`)
Right-clicking any card header or clicking the `[⋮]` button opens a context menu with 10 powerful utilities:

1. **`📋 Copy Attribute`:** Copies this individual attribute, its type, and all configured parameter values to the internal single-attribute clipboard.
2. **`📄 Copy C# Code`:** Formats this single attribute into runnable C# code (e.g. `[ProgressBar(0f, 100f, SliderColor = "#33CC66", Height = 22)]`) and copies it to the system clipboard.
3. **`📋 Paste Parameter Values`:** Pastes copied parameter values from another attribute of the same type without altering other attributes on the member (disabled if clipboard is empty).
4. **`🔄 Reset to Default Values`:** Reflects the default constructor and property parameters of the attribute type and overwrites all values with factory defaults.
5. **`🌐 Apply to All Other Fields`:** Clones this exact attribute configuration onto *every other field* on the target component in a single click (available on field-level attributes).
6. **`👥 Apply to All {N} Selected Members`:** When multi-member selection is active (`Ctrl+Click` / `Shift+Click`), clones or updates this attribute across all currently selected members simultaneously.
7. **`🔇 Mute Attribute` / `🔊 Unmute Attribute`:** Toggles `IsDisabled = true/false` on this single attribute, temporarily bypassing it during drawing without removing configured values.
8. **`⧉ Duplicate`:** Creates an exact clone of the attribute card in the stack (supported on attributes allowing multiple instances).
9. **`💾 Save Attribute as Recipe...`:** Saves this configured attribute and its parameters directly into your project's recipe library as a new `InspectorAttributeRecipe` ScriptableObject.
10. **`✕ Remove Attribute`:** Deletes the override from the profile with full Undo tracking.

*(Note: Vertical execution order in the stack is adjusted directly using the card drag handle `☰` or the nudge buttons `[^]` and `[v]` in the card header).*

---

## 3. Reflection-Driven Parameter Controls

Every parameter exposed by an attribute's constructors and public properties is automatically rendered using strongly typed UI Toolkit elements:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  PARAMETER TYPE        UI TOOLKIT ELEMENT RENDERED        SPECIAL CAPABILITIES         │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  int, long             IntegerField                       Direct typing, label drag    │
│  float, double         FloatField                         Decimal formatting           │
│  string                TextField                          Token replacement ({Name})   │
│  bool                  Toggle                             Checkbox switch              │
│  Color                 ColorField                         HDR color, Alpha, Hex input  │
│  Color32               ColorField                         Hex and 32-bit color bounds  │
│  Vector2               Vector2Field                       Dual float "X, Y" inputs     │
│  Vector3               Vector3Field                       Triple float "X, Y, Z" inputs│
│  Array (string[], etc) TextField (Multi-Delimiter)        Splits on , ; | > › /        │
│  Enum                  EnumField                          Dropdown of all named values │
│  Enum [Flags]          MaskField / EnumFlagsField         Multi-bitmask selection      │
│  AnimationCurve        CurveField                         Interactive curve editor     │
│  Condition String      TextField + Autocomplete Dropdown  Scans sibling boolean fields │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 3.1 Constructor Arguments vs. Named Properties
In C#, attributes accept two kinds of inputs:
1. **Positional Constructor Arguments:** Passed into the constructor (e.g. `new ProgressBarAttribute(0f, 100f)`).
   - In Inspector Customizer, these keys are encoded with the prefix `__ctor_<paramName>_<TypeName>` (e.g. `__ctor_min_Single`, `__ctor_max_Single`).
   - Changing constructor values automatically validates against the attribute's constructor signature.
2. **Named Optional Properties:** Assigned via object initializer syntax (e.g. `SliderColor = "#FF0000"`, `Height = 24`).
   - In Inspector Customizer, these keys match the exact C# property name.
   - When a named property matches its default value, it is drawn in subtle text; modified properties highlight with an active tint.

### 3.2 Dynamic Condition Autocomplete
When editing conditional attributes (`[ShowIf]`, `[HideIf]`, `[EnableIf]`, `[DisableIf]`, `[ButtonConditional]`):
- Instead of forcing you to remember and type the exact casing of boolean fields, clicking the condition text field opens a **live autocomplete popup**.
- The popup lists all `bool` and `enum` fields present on the inspected component.
- Selecting a field inserts its exact identifier into the parameter field, eliminating runtime reflection typos.

---

## 4. Code Attribute Exploration (`ExploreCodeAttributes`)

When opening an existing project where attributes were previously authored in C# code, you do not need to re-enter them manually.

The **Explore Code Attributes** feature automatically scans the target C# script and imports all declared attributes into your visual customizer deck:

```
[Target C# Script]
public class HeroController : MonoBehaviour
{
    [BoxGroup("Stats")]
    [ProgressBar(0, 100)]
    public float health = 100f;
}
         │
         ▼ Click 'Explore Code Attributes' Toolbar Button
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  EXPLORATION SUMMARY: Imported 2 attributes from C# code.                              │
│  • health: [BoxGroup("Stats")]                                                         │
│  • health: [ProgressBar(0, 100)]                                                       │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 4.1 Exploration Rules & Integrity
- **Extracts Exact Parameter Values:** `AttributeExtractor` parses both constructor arguments and named properties from compiled assembly reflection metadata.
- **De-duplication Protection:** If an attribute of the same type already exists in the profile, exploration checks frequency counts to prevent unwanted duplicates.
- **Full Scope Coverage:**
  - Class-level styling attributes (`[ComponentHeader]`, `[ComponentBorder]`).
  - Serialized fields and inspectable properties (`[ShowInInspector]`).
  - Methods decorated with `[Button]` or `[ButtonGroup]`.
- **Non-Destructive:** Code attributes are copied into the profile asset; the original C# script is **not** modified until you explicitly trigger **Bake to Code**.

---

## 5. Undo & Redo System Integration

Every action taken in `InspectorCustomizerWindow` is fully registered with Unity's native `Undo` engine:
- Adding, removing, or reordering attribute cards creates an undo entry (`Ctrl+Z`).
- Modifying color pickers, sliders, text fields, or toggle switches records undo states.
- Reverting an undo step instantly repaints both the Customizer window and the active Unity Inspector window simultaneously.
