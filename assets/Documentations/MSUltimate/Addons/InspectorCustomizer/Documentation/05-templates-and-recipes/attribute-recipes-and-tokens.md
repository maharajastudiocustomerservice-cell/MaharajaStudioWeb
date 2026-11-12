# Attribute Recipes & Dynamic String Tokens

> **Module:** MSUltimate Inspector Customizer — Templates & Recipes  
> **Topic:** Authoring Compound Recipes, Built-in Recipe Catalog, and Dynamic Token Interpolation

---

## 1. What is an Attribute Recipe?

An **Inspector Attribute Recipe** (`InspectorAttributeRecipe`) is a ScriptableObject asset that stores an ensemble of multiple pre-configured attributes meant to be stamped onto any field, method, or class as a single reusable bundle.

### The Real-World Problem Solved
Styling a gameplay parameter like `health` often requires stacking 4 to 5 separate attributes:
```csharp
[BoxGroup("Vitality")]
[ProgressBar(0f, 100f, ColorHex = "#FF3344", Height = 22)]
[Tooltip("Current hit points of the character")]
[InfoBox("Critical: Low Health!", InspectorMessageType.Warning)]
```
Having to re-select and re-tune these 4 attributes across 20 different character scripts is tedious and prone to formatting inconsistencies.

With an **Attribute Recipe**, you bundle this entire stack once into an asset named `Polished Health Bar`. You can then stamp all 4 attributes onto any field with 1 click from the `AttributePickerWindow` or the **Member Context Menu**!

---

## 2. Dynamic String Token Interpolation

Hardcoding titles or labels inside recipes makes them brittle. Inspector Customizer includes an **Interpolation Token Engine** that dynamically replaces tokens at the exact millisecond the recipe is stamped onto a member:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  TOKEN IDENTIFIER   INTERPOLATED VALUE               EXAMPLE FOR 'currentHealth'       │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  {Name}             Title-Cased Space-Split Name     "Current Health"                  │
│  {RawName}          Exact C# Identifier              "currentHealth"                   │
│  {Type}             C# Data Type Name                "Single" (or "float")             │
│  {Class}            Declaring Class Identifier       "HeroController"                  │
│  {Category}         Target Layout Group / Category   "Combat"                          │
│  {Namespace}        Declaring Namespace              "Game.Characters"                 │
│  {Assembly}         Declaring Assembly Definition    "Assembly-CSharp"                 │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2.1 Concrete Example of Dynamic Token Expansion
Suppose you create a recipe named `Collapsible Parameter Card` with two attributes:
- **Attribute 1:** `[BoxGroup("{Class} • {Name}")]`
- **Attribute 2:** `[Tooltip("Tracks {Name} ({Type}) on {Class} in {Namespace}")]`

When stamped onto `moveSpeed (float)` on `HeroController`:
- **BoxGroup evaluates to:** `"HeroController • Move Speed"`
- **Tooltip evaluates to:** `"Tracks Move Speed (Single) on HeroController in Game.Characters"`

---

## 3. Built-in Recipe Catalog

Inspector Customizer ships with 9 pre-tuned attribute recipes ready for production use:

| Recipe Name | Category | Primary Stack Applied | Ideal Use Case |
| :--- | :---: | :--- | :--- |
| **`Polished Health Bar`** | Presentation | `[ProgressBar]` | Player and enemy hit points. |
| **`Shield Barrier Bar`** | Presentation | `[ProgressBar]` | Defensive shields and energy barriers. |
| **`Mana Energy Bar`** | Presentation | `[ProgressBar]` | Magic, spell energy, and stamina pools. |
| **`Stamina Gauge Bar`** | Presentation | `[ProgressBar]` | Sprint and dodge stamina gauges. |
| **`Overheat Warning Bar`** | Presentation | `[ProgressBar]` | Weapon heat, engine temperature. |
| **`Audio Normalized Slider`**| Audio | `[CustomRange]` | Volume levels, sound effects buses. |
| **`Action Trigger Button`** | Actions | `[Button]` | Debug reset methods, spawn buttons. |
| **`Collapsible Section`** | Layout | `[Foldout]` | Advanced developer settings. |
| **`MultiAttributeField`** | Utility | `[BeginTabGroup]`, `[Title]`, `[CustomSlider]`, `[DeltaTracker]`, `[FieldBookmark]`, `[LabelWidth]` | Multi-attribute telemetry fields. |

---

## 4. Authoring Custom Recipes Step-by-Step

### Method A: Creating from the Unity Project Window
1. Right-click in the Project browser $\rightarrow$ **`Create > Maharaja Studio > MSUltimate > Inspector Customizer > Attribute Recipe`**.
2. Name the asset (e.g. `Recipe_WeaponSlot.asset`).
3. Open `TemplateRecipeManagerWindow` $\rightarrow$ switch to the **Recipes** tab.
4. Click **Add Attribute** to build your stack, using dynamic tokens in string fields.

### Method B: Saving Directly from an Existing Member Stack
1. Style any field in `InspectorCustomizerWindow` until it looks perfect.
2. In the right column header, click **`[MemberMenu ▼] > 💾 Save Stack as Custom Recipe...`**.
3. Choose a name and category.
4. **Done!** The stack is instantly saved into your project's recipe library and appears in all attribute pickers.
