# 60-Second Quick Start Guide

> **Module:** MSUltimate Inspector Customizer — Getting Started  
> **Topic:** Step-by-Step Walkthrough: Your First Inspector Customization

---

## 1. Prerequisites
- Unity 6 (6000.x) or newer installed.
- `MSUltimate` Core and `MSUltimate-InspectorCustomizer` imported into your project.

---

## 2. Option A: The 10-Second Magic Makeover

The fastest way to transform any plain component inspector:

1. In your Unity Scene, select any GameObject with a MonoBehaviour (for example, a character controller or combat script).
2. Right-click the component's header bar in the Inspector window.
3. Select **`MSUltimate > ⚡ Magic Makeover (1-Click Auto-Detect)`**.

```
[Inspector Header Context Menu]
├── Reset
├── Remove Component
├── Move Up / Down
└── MSUltimate
    ├── ⚡ Magic Makeover (1-Click Auto-Detect)   ◄── CLICK HERE
    ├── 🎨 Open Inspector Makeover Wizard...
    ├── 🪟 Live Compare (Before vs After)...
    ├── 📋 Apply Preset >
    └── 🗑️ Clear Customizer Overrides
```

**Result:** The engine inspects your component's fields, calculates pattern compatibility with built-in templates, and applies the optimal layout (headers, sliders, progress bars, and foldout groups) in real-time.

---

## 3. Option B: Visual Step-by-Step Customization

Follow this walkthrough to visually customize fields and methods manually:

### Step 1: Open the Inspector Customizer Window
Go to the Unity top menu bar:
**`Tools > Maharaja Studio > MSUltimate > Inspector Customizer > Inspector Customizer`**  
*(Or press `Ctrl+Alt+I` if configured).*

### Step 2: Select Your Target Component
- Drag any GameObject, Component, or ScriptableObject into the **Target Object** field at the top left.
- *Alternatively:* Click the **Type Picker** icon to browse and pick any C# class or POCO data struct across your project.

### Step 3: Select a Member to Customize
In the left column:
- Click **Component** to add class-level card styling (`[ComponentHeader]`, `[ComponentBorder]`).
- Click **Fields** to view serialized variables. Click on any field (e.g. `currentHealth` or `moveSpeed`).

### Step 4: Add an Attribute
1. In the right column, click the green **`+ Add Attribute`** button.
2. The **Attribute Picker** window opens. Type `ProgressBar` into the search field.
3. Click `ProgressBar`. A new attribute card appears in your deck.

### Step 5: Adjust Parameter Values Live
- Notice the parameter fields inside the card: `Min`, `Max`, `Color`.
- Change `Max` to `100` and pick a vibrant color using the color picker.
- Look at your Unity Inspector window: **The field instantly renders as a live progress bar!** No script compilation required.

### Step 6: Save Your Profile
- Inspector Customizer automatically creates and saves an `InspectorProfile` asset into `Assets/InspectorProfiles/{TargetTypeName}.asset` (or your project's configured profile repository under `{MSUltimateRoot}/Profiles/`).
- All team members who pull your project will see the styled inspector automatically.

---

## 4. Reverting or Clearing Overrides

To remove customizer overrides and restore the default inspector:
- Right-click the component header $\rightarrow$ **`MSUltimate > 🗑️ Clear Customizer Overrides`**.
- Or inside `InspectorCustomizerWindow`, select the member and click the trash can icon on the attribute card.
