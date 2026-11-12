# Batch Operations & Multi-Member Editing

> **Module:** MSUltimate Inspector Customizer — Editor Windows  
> **Topic:** Multi-Member Selection, The Batch Editing Panel, Batch Attribute Modal, and Conflict Resolution

---

## 1. Multi-Member Selection Controls

When styling complex game components with 30+ fields, customizing members one by one is slow and repetitive. Inspector Customizer includes a dedicated **Multi-Member Selection Engine**:

- **`Ctrl + Click`:** Select or deselect individual members non-contiguously.
- **`Shift + Click`:** Select a contiguous range of members in the left column.
- **Auto-Scope Detection:** The customizer inspects your selection: if all selected members are methods, the attribute picker automatically filters to method attributes; if all are fields, it filters to field attributes.

---

## 2. The Batch Editing Workspace Panel

When two or more members are selected, the right column transitions into the **Batch Editing Panel**:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  👥 Multi-Member Batch Editing (4 members selected)                                    │
│  Add attributes or wrap layout groups across all selected members simultaneously.      │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  SELECTED CHIPS:                                                                       │
│  [ 🔧 currentHealth ✕ ]  [ 🔧 maxHealth ✕ ]  [ 🔧 stamina ✕ ]  [ 🔧 mana ✕ ]           │
│                                                                                        │
│  SELECTION SHORTCUTS:                                                                  │
│  [ Select All Fields ]      [ Select All Methods ]      [ Clear Selection ]            │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  BATCH ACTIONS:                                                                        │
│  ┌──────────────────────────────────────────────────────────────────────────────────┐  │
│  │ ＋ Batch Add Attribute to All Selected...                                        │  │
│  └──────────────────────────────────────────────────────────────────────────────────┘  │
│  [ 📦 Wrap in BoxGroup... ]                      [ 📁 Wrap in Foldout... ]             │
│  [ 🔇 Mute Selected Overrides ]                  [ 🔊 Unmute Selected Overrides ]      │
│  [ ✕ Clear Overrides on Selected ]                                                     │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2.1 Interactive Selection Chips
- Each selected member appears as an individual chip badge with an icon (`🔧` for fields, `⚡` for methods, `📦` for classes).
- Clicking the small `✕` on any chip deselects that specific member without clearing your overall selection.

### 2.2 1-Click Layout Group Wrappers
- **`Wrap in BoxGroup...`:** Prompts for a group title (e.g. `"Vitality Stats"`). Immediately wraps all selected members inside a cohesive card container with a shared header.
- **`Wrap in Foldout...`:** Prompts for a foldout title and default expanded state (`true`/`false`). Wraps all selected members into a collapsible drawer.

---

## 3. The Batch Attribute Modal Window (`BatchAttributeModalWindow`)

Clicking **`＋ Batch Add Attribute to All Selected...`** opens the attribute picker. Once an attribute is selected, `BatchAttributeModalWindow` opens to configure parameters before applying:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  Batch Apply [ProgressBar] across 4 members                                            │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  Min:            [ 0.0          ]                                                      │
│  Max:            [ 100.0        ]                                                      │
│  SliderColor:    [ ■ #33CC66    ]                                                      │
│  Height:         [ 20           ]                                                      │
│  ShowPercentage: [✓]                                                                   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  Token Expansion Preview:                                                              │
│  • Label text supports dynamic tokens: {Name}, {Type}, {Class}                         │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [ Cancel ]                                                      [ Apply to All (4) ]  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

- **Single Configuration Pass:** Set sliders, colors, and flags once; parameters are distributed across all selected members.
- **Dynamic Token Expansion:** String parameters accept dynamic tokens (e.g. `{Name}`), which evaluate uniquely for each field (e.g. `"Current Health"`, `"Max Health"`).

---

## 4. Conflict Handling (`BatchConflictModalWindow`)

If any of the selected members already have the target attribute applied, Inspector Customizer launches the **Batch Conflict Modal**:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  ⚠️ Attribute Conflict Detected: 2 of 4 members already possess [ProgressBar]          │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  Member Name       Existing Attribute Config          Individual Resolution Strategy   │
│  ────────────────────────────────────────────────────────────────────────────────────  │
│  currentHealth     Min: 0, Max: 100, Color: Red       [ Replace ] [ Skip ] [ Duplicate]│
│  maxHealth         Min: 0, Max: 50, Color: Green      [ Replace ] [ Skip ] [ Duplicate]│
│  stamina           (No conflict - Clean)              Will be Added                    │
│  mana              (No conflict - Clean)              Will be Added                    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  Batch Resolve:   [ Replace All ]     [ Skip All ]     [ Duplicate All ]     [ Cancel ]│
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Resolution Strategy Details
| Strategy | Operational Behavior |
| :--- | :--- |
| **`Replace`** | Overwrites the existing attribute parameters with the new batch configuration. |
| **`Skip`** | Preserves the existing attribute on conflicting members; applies the new attribute only to clean members. |
| **`Duplicate`**| Adds a second instance of the attribute to the member (valid for attributes with `AllowMultiple = true`). |
| **`Cancel`** | Aborts the batch operation without making any changes. |

---

## 5. Cross-Member & Cross-Component Clipboard Stacks

Inspector Customizer maintains an internal attribute stack clipboard:

- **Copy Full Stack:** Select any member and click **Copy Stack** (or press `Ctrl+C`). All applied attributes, parameter keys, and values are copied.
- **Paste Stack (Append):** Select multiple target members and click **Paste Stack** (or press `Ctrl+V`). The entire attribute stack is appended onto each selected member.
- **Paste Stack (Replace):** Replaces any existing overrides with the copied stack.
- **Cross-Component Reusability:** Copy a polished stat bar stack from `PlayerStats` and paste it directly onto `EnemyStats`, `BossEntity`, or `PetCompanion`.
