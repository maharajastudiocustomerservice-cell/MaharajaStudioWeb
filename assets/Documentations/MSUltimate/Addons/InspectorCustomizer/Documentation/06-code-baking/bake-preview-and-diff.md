# Bake Code Preview Window & Diff Review

> **Module:** MSUltimate Inspector Customizer — Code Baking  
> **Topic:** The BakeCodePreviewWindow, Syntax Highlighter, Compact View, and Mode Toggles

---

## 1. Anatomy of the BakeCodePreviewWindow

The `BakeCodePreviewWindow` provides a modern, interactive code review modal dialog before any file on disk is modified:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  Bake to Code: HeroController.cs                                                       │
│  Path: Assets/Scripts/Characters/HeroController.cs                                     │
│  Status: 4 Added, 1 Updated, 0 Removed, 3 Preserved                                    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  BAKE MODE:                                                                            │
│  [ Both (Recommended) ]      [ Override ]      [ Code Only ]                           │
│  Description: "Code attributes remain active. Profile attributes update matching types."│
├────────────────────────────────────────────────────────────────────────────────────────┤
│  VIEW MODE & CONTROLS:                                                                 │
│  [ 📄 Script Diff View ]   [ 🗂️ Card Deck View ]                                       │
│  [✓] Show Line Numbers     [✓] Compact Mode (Diff Only)          [ 📋 Copy Code ]      │
├────────────────────────────────────────────────────────────────────────────────────────┤
│   24 │      [SerializeField]                                                           │
│   25 │  +   [ComponentHeader("WARRIOR HERO")]                                        │
│   26 │  +   [ComponentBorder(Color = "#4FC3F7", Glow = true)]                          │
│   27 │      public class HeroController : MonoBehaviour                                │
│   28 │      {                                                                          │
│   29 │  +       [BoxGroup("Vitality Telemetry")]                                       │
│   30 │  +       [ProgressBar(0f, 100f, ColorHex = "#33CC66", DynamicMaxValueMember = "maxHealth")]│
│   31 │  ~       [Tooltip("Current hit points of the character")]                       │
│   32 │          public float currentHealth = 100f;                                     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [ Cancel ]                                                      [ Confirm Bake & Save]│
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Interactive Controls & Display Options

### 2.1 Mode Selector Buttons
You can switch the reconciliation mode directly inside the preview window:
- **`Both (Recommended)`:** Merges profile overrides into the C# script. Code attributes on other members remain untouched.
- **`Override`:** Pure clean-room mode. Overrides all custom inspector attributes on the component with the exact profile stack.
- **`Code Only`:** Suppresses profile overrides and preserves existing C# attributes.

### 2.2 View Tabs: Script Diff vs. Card Deck
- **`Script Diff View`:** Embeds the `MSUltimateCodeViewerElement` syntax highlighter showing the exact C# file with color-coded syntax (keywords, strings, numbers, types, and comments).
- **`Card Deck View`:** Switches to a compact list of cards detailing each affected member and the attributes being added or modified.

### 2.3 Compact Mode Toggle (`[✓] Compact Mode`)
When baking scripts that are 2,000+ lines long, scanning through hundreds of lines of unchanged code is tedious:
- Enabling **Compact Mode** automatically collapses unchanged methods and properties.
- It displays only the decorated members with 3 lines of surrounding context padding, letting you review all diffs in seconds!

### 2.4 Copy Code Clipboard Action
Clicking **`📋 Copy Code`**:
- Copies the complete, reconstructed C# source code—including new `using` directives and indented attributes—to your system clipboard.
- The button temporarily animates to `"✓ Copied!"` to provide immediate tactile feedback.

---

## 3. Reconciliation Actions Color Legend

The preview window color-codes every attribute change:

| Symbol & Color | Action Name | Meaning |
| :---: | :--- | :--- |
| **`+` (Green)** | **`Added`** | New attribute from the profile being injected into the C# script. |
| **`~` (Yellow)** | **`Updated`** | Attribute already existed in code; its parameter values are being updated to match the profile. |
| **` ` (White)** | **`Preserved`** | Existing code attribute preserved without any changes. |
| **`-` (Red)** | **`Removed`** | Attribute existed in code but is being stripped (active only in `EditorOverride` mode). |

---

## 4. Confirming & Reverting

- **Confirm Bake & Save:** Atomically writes the file to disk via temporary buffers. Unity triggers an asset re-import and compiles the changes.
- **Cancel:** Closes the modal with zero disk modifications.
- **Undo After Bake:** If you change your mind immediately after baking, pressing `Ctrl+Z` in Unity reverts the file on disk before compilation completes.
