# Prompt Directives & System Prompt Engineering

> **Module:** MSUltimate Inspector Customizer — AI Decorator  
> **Topic:** Directive Tuning, System Prompt Modes, and Few-Shot Context References

---

## 1. System Prompt Modes

Inside `AIDecoratorModalWindow`, the **System Prompt Mode** controls how instructions are constructed before being passed to the LLM:

| Mode | Behavior & Recommended Usage |
| :--- | :--- |
| **`Studio Default (Secret & Recommended)`** | Uses Maharaja Studio's proprietary system prompt, fine-tuned specifically for MSUltimate attributes, layout hierarchy, and UI Toolkit color theory. Delivers the most balanced, professional AAA results. |
| **`User-Defined (Replace Studio Prompt)`** | Completely overrides the system prompt with your custom studio directives. Ideal for enterprise studios with their own strict UI design guidelines. |
| **`Combined (Studio Default + User Directives)`** | Appends your custom team rules onto the Studio Default prompt. Great for enforcing studio conventions (e.g. *"Always use our studio color palette: #00FFCC and #1E1E2E"*). |

---

## 2. Built-in AI Layout Presets (`AIPreset`)

Inspector Customizer includes 6 built-in layout presets that configure tailored positive directives, negative prompt constraints, and allowed attribute subsets:

| Preset Name | Identifier | Primary Directives & Strategy | Allowed Attributes Focus |
| :--- | :--- | :--- | :--- |
| **`Modern Tabs & Controls`** | `preset_modern_tabs` | Groups fields into 2–4 clean horizontal tabs with smooth sliders, resource bars, action buttons, and validation tags. | Tabs, SplitPane, BoxGroup, Sliders, ProgressBars, Buttons, Validation. |
| **`Clean Foldouts`** | `preset_clean_foldouts` | Organizes complex components into collapsible foldout sections for modular subsystems (Physics, Audio, FX). | Foldout, FoldoutGroup, VerticalGroup, HorizontalGroup, InfoBoxes. |
| **`Compact Pro`** | `preset_compact_pro` | Maximizes screen efficiency with side-by-side companion fields, compact boxes, and split panes without large headers. | BoxGroup, BeginHorizontal, SplitPane, ToolbarToggle, CompactSliders. |
| **`Validation & Safety Focus`** | `preset_validation_safety` | Emphasizes defensive game development: missing reference warnings, range clamping, and null checks. | Required, HighlightIfNull, ValidateInput, ClampWarning, InfoBox. |
| **`Minimalist & Subtle`** | `preset_minimalist` | Keeps the inspector clean and familiar using subtle section titles and clean sliders without heavy boxes or loud colors. | Title, Header, Space, CustomSlider, ToggleLeft, ReadOnly. |
| **`Full Studio Suite`** | `preset_all_core` | Unlocks the complete MSUltimate Core attribute library (zero addon attributes required) for maximum design freedom. | All 155 Core MSUltimate attributes. |

---

## 3. Crafting Effective Directives

The **Positive Prompt** and **Negative Prompt** fields let you steer the AI with plain English on top of your chosen preset.

### Recommended Prompt Patterns

#### Pattern A: Aesthetic Theme Steering
> *"Create a Cyberpunk dark neon aesthetic. Wrap core stats into a glassmorphism card. Use hot pink (#FF007F) for health, electric cyan (#00F0FF) for shields, and neon yellow for stamina."*

#### Pattern B: Layout Organization & Grouping
> *"Organize the fields into three clean tabs: 'General', 'Combat', and 'Audio'. Place min/max damage into a horizontal group. Put all debug toggles into a collapsed foldout named 'Developer Debug'."*

#### Pattern C: Progressive Disclosure & Conditions
> *"Only show 'shieldRechargeRate' and 'shieldBreakDelay' when 'hasShield' is true. Group all weapon ammo properties into an ammo box group."*

### Negative Prompts
You can specify negative directives to prevent unwanted styles:
- *"Do not use animated text effects."*
- *"Do not wrap single fields in individual boxes."*
- *"Avoid bright red headers; use subtle dark gray (#2A2A3A)."*

---

## 4. Few-Shot Context References

To achieve 100% style consistency across your entire project, the AI Decorator supports **Few-Shot Reference Injection**:

### 1. Script Examples
- Click **Add Script Example** and pick an existing C# script in your project that already has your preferred inspector styling.
- The AI examines how you styled that component and mirrors the exact same attribute patterns, group structures, and naming conventions on your new target script!

### 2. Screenshot & Image References
- For vision-capable models (Claude 3.5 Sonnet, GPT-4o, Gemini 1.5 Pro), click **Add Image Example**.
- Select a UI mockup or screenshot of an inspector you love.
- The AI analyzes the visual hierarchy and color tones from the image and applies matching MSUltimate attributes!
