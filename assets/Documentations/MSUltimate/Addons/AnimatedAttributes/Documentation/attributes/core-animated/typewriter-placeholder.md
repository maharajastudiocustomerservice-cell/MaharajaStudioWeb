# [TypewriterPlaceholder]

> Cycles animated typewriter hint phrases across empty string fields to guide data entry and clarify expected inputs.

---

## 1. Overview & Value Proposition

**What it does:**
`[TypewriterPlaceholder]` animates cycling placeholder text inside empty string input fields. When the field is empty and unfocused, it types out instructional examples or hints character-by-character, pauses, backspaces them, and types the next phrase from a designated list. As soon as the user focuses or types into the field, the animation seamlessly yields to user input.

**The Problem:**
Text fields often need context on required syntax, naming conventions, or example formats (e.g., `"item_sword_legendary"`, `"https://api.game.io/v1"`). Static placeholder text quickly becomes monotonous and easily goes unnoticed.

**The Solution:**
Applying `[TypewriterPlaceholder]` to string inputs:
- **Engaging Contextual Hints:** Cycles through multiple concrete examples to communicate formatting standards.
- **Dynamic Typing Lifecycle:** Sequentially types (`TypeSpeed`), pauses (`PauseDuration`), and backspaces (`EraseSpeed`) each phrase in a continuous loop.
- **Unobtrusive User Experience:** Immediately clears the moment the user clicks the field or enters real data.
- **Zero String Allocations in Runtime:** Runs strictly inside the editor UI Toolkit layer without generating runtime garbage.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class ItemConfig : MonoBehaviour
{
    [TypewriterPlaceholder("e.g. wp_katana_iron", "e.g. wp_staff_arcane", "e.g. wp_bow_ranger")]
    public string itemIdentifier;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `string` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public TypewriterPlaceholderAttribute(params string[] hints)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `hints` | `string[]` | `["Type here..."]` | Comma-separated or array of placeholder hint phrases to cycle through. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Hints` | `string[]` | *Constructor* | Array of placeholder hint phrases being cycled. |
| `TypeSpeed` | `float` | `0.05f` | Delay in seconds between each typed character. |
| `EraseSpeed` | `float` | `0.03f` | Delay in seconds between each erased backspace character. |
| `PauseDuration` | `float` | `1.5f` | Pause duration in seconds between finishing a phrase and backspacing it. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class LocalizationKeyDefinition : MonoBehaviour
{
    [Header("Localization Token Entry")]
    [TypewriterPlaceholder(
        "ui_menu_play_button", 
        "dialogue_act1_scene2_intro", 
        "item_potion_health_desc",
        TypeSpeed = 0.04f,
        EraseSpeed = 0.02f,
        PauseDuration = 2.0f
    )]
    public string localizationKey;

    [Header("Fallback Display Text")]
    [TypewriterPlaceholder("Start Game", "Skip Cutscene", "Restores 50 HP")]
    public string defaultEnglishText;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[ValidateNotEmpty]` | Supported | Pairs perfectly; hints show expected format while validation catches empty submissions. |
| `[BoxGroup]` | Supported | Functions cleanly inside grouped layouts and tabbed inspector containers. |
| `[TextArea]` | Supported | Works with standard text fields and multi-line text input areas. |
