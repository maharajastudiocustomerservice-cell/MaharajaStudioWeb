# [SmartEnum]

> Enhances Enum fields with a modern searchable dropdown popup, scroll management, hover feedback, and custom color theming.

---

## 1. Overview & Value Proposition

**What it does:**
Replaces Unity's standard native enum dropdown with an advanced searchable popup selector. Designed specifically for enums with numerous entries, it provides an instant real-time search bar, maximum item height capping with smooth scrolling, and custom UI styling.

**The Problem:**
Standard Unity enum dropdowns become unmanageable when an enum exceeds 15–20 entries (such as item IDs, sound effect names, language codes, or achievement keys). The dropdown spills across the screen, requires tedious manual scrolling, and offers no search filtering.

**The Solution:**
Add `[SmartEnum]` to any enum field:
- **Instant Search Bar:** Filter through dozens or hundreds of enum members by simply typing keywords.
- **Scroll Capping:** Restricts the popup list height via `MaxVisibleItems` (default 15) to keep the inspector clean and manageable.
- **Theme Customization:** Custom button colors, hover states, border widths, and corner radii.
- **Collection Element Friendly:** Supports `List<MyEnum>` elements with automatic full-width cell formatting.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public enum AudioCueType
{
    Footstep_Grass, Footstep_Stone, Footstep_Water, Footstep_Metal,
    Sword_Swing_Light, Sword_Swing_Heavy, Sword_Parry, Shield_Block,
    Spell_Fireball, Spell_FrostNova, Spell_LightningBolt, Spell_Heal,
    UI_ButtonClick, UI_WindowOpen, UI_Error, UI_RewardFanfare
}

public class SoundEmitter : MonoBehaviour
{
    [SmartEnum]
    public AudioCueType defaultCue = AudioCueType.Sword_Swing_Light;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any `enum` type |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public SmartEnumAttribute()
```

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `AllowSearch` | `bool` | `true` | Displays a search input bar at the top of the popup menu. |
| `MaxVisibleItems` | `int` | `15` | Maximum number of items visible before enabling scrollbars. |
| `ButtonColor` | `string` | `null` | Hex background color for the selector button. |
| `TextColor` | `string` | `null` | Hex text color for the active choice label. |
| `HoverColor` | `string` | `null` | Hex highlight color applied when hovering over the selector. |
| `ShowLabel` | `bool` | `true` | Whether to display the inspector property label row. |
| `DropdownHeight` | `float` | `0f` | Explicit pixel height for the dropdown popup (`0` = auto). |
| `ButtonHeight` | `float` | `0f` | Explicit pixel height for the selector button (`0` = auto). |
| `BorderColor` | `string` | `null` | Hex color code for the button border. |
| `BorderWidth` | `float` | `1f` | Border outline width in pixels. |
| `BorderRadius` | `float` | `3f` | Corner radius for the button in pixels. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public enum LanguageCode
{
    English_US, English_UK, Spanish_ES, Spanish_MX, French_FR, French_CA,
    German_DE, Italian_IT, Portuguese_BR, Russian_RU, Japanese_JP,
    Korean_KR, Chinese_Simplified, Chinese_Traditional, Polish_PL
}

public class LocalizationSettings : MonoBehaviour
{
    [Header("Primary Application Language")]
    [SmartEnum(AllowSearch = true, MaxVisibleItems = 8, ButtonColor = "#2c3e50", HoverColor = "#34495e")]
    public LanguageCode primaryLanguage = LanguageCode.English_US;

    [Header("Fallback Language Chain")]
    [SmartEnum]
    public List<LanguageCode> fallbackLanguages = new List<LanguageCode>
    {
        LanguageCode.English_UK,
        LanguageCode.Spanish_ES
    };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Popup window aligns dynamically to the inspector layout without clipping. |
| `[ShowIf]` | Supported | Functions as an ideal driver for conditional inspector logic. |
| `[ReadOnly]` | Supported | Displays the current selection while disabling popup interaction. |
| `ICollectionElement` | Supported | Auto-hides element labels when rendered inside collection tables or lists. |
