# [ComponentFantasyParchment]

> Restyles the component inspector as an antique fantasy scroll with weathered parchment paper tones, ornate filigree borders, and an authentic royal wax seal.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentFantasyParchment]` immerses the component inspector in an authentic high-fantasy roleplaying aesthetic. Injected into `ComponentSlot.BodyWrapper`, it wraps the inspector card in textured antique parchment paper across three historical tone presets (`Tone = ParchmentTone.WeatheredGold`, `AncientSepia`, or `DarkGrimoire`). The card features illuminated calligraphic header typography (`Title = "Ancient Scroll"`), ornate filigree corner flourishes, and an optional dimensional crimson wax seal stamp (`ShowWaxSeal = true`, `SealText = "SEALED"`).

**The Problem:**
Spellbooks, ancient quest journals, sacred scrolls, potion recipes, and medieval kingdom edicts look disconnected when displayed inside sterile gray modern inspector panes. Game designers and narrative writers miss the immersive tactile feel of weathered parchment when balancing spells or crafting quest parameters.

**The Solution:**
Decorating fantasy assets with `[ComponentFantasyParchment]`:
- **Historical Paper Tonality:** Choose between golden calfskin vellum, antique tea-stained sepia, or ominous dark leather grimoire paper.
- **Dimensional Wax Seal Stamp:** Embeds an embossed royal or arcane seal in the top corner with customizable stamped insignia text.
- **Illuminated Calligraphy Styling:** Automatically adjusts labels and header typography to match medieval manuscripts without sacrificing readability.
- **Non-Obtrusive Wrapper:** Encapsulates the entire component inside `BodyWrapper` while delegating pointer events directly to input fields and foldouts.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentFantasyParchment("Scroll of Dragon Breath", ParchmentTone.WeatheredGold, "ROYAL")]
public class DragonBreathSpellScroll : MonoBehaviour
{
    public int manaCost = 85;
    public float fireConeRadiusMeters = 14f;
    public float burnDurationSeconds = 6.5f;
    public bool requiresDragonBloodReagent = true;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ComponentDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Component Slot** | `BodyWrapper` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentFantasyParchmentAttribute(string title = "Ancient Scroll", ParchmentTone tone = ParchmentTone.WeatheredGold, string sealText = "SEALED")
```

- `title`: Medieval manuscript title displayed in ornate header typography.
- `tone`: Paper palette preset (`ParchmentTone.WeatheredGold`, `ParchmentTone.AncientSepia`, or `ParchmentTone.DarkGrimoire`).
- `sealText`: Capitalized text insignia stamped into the embossed wax seal.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Title` | `string` | `"Ancient Scroll"` | Header title text rendered in medieval manuscript calligraphy. |
| `Tone` | `ParchmentTone` | `WeatheredGold` | Parchment material tone preset (`AncientSepia`, `WeatheredGold`, `DarkGrimoire`). |
| `SealText` | `string` | `"SEALED"` | Short text or monogram stamped into the wax seal face. |
| `ShowWaxSeal` | `bool` | `true` | Whether to display the embossed dimensional wax seal stamp in the top corner. |
| `Order` | `int` | `0` | Sequence sorting order within the target component slot. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentFantasyParchment(
    Title = "EDICT OF THE SUN EMPEROR", 
    Tone = ParchmentTone.WeatheredGold, 
    SealText = "IMPERIAL", 
    ShowWaxSeal = true)]
public class ImperialQuestDecree : MonoBehaviour
{
    [Header("Quest Objectives")]
    public string questTargetRegion = "Cinder Peak Caldera";
    public int requiredWyvernBounties = 3;
    public int imperialGoldBounty = 5000;

    [Header("Lore & Authenticity")]
    [TextArea(3, 6)]
    public string proclamationText = "By decree of His Radiant Majesty Aurelius, let the champion who slays the ash wyverns claim lordship over the western caldera.";
    public bool isSignedByGrandInquisitor = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeaderButton]`** | High | Buttons integrate smoothly onto the parchment margin to test or sign decrees. |
| **`[ComponentGildedGold]`** | High | Pairs naturally with gilded gold leaf borders for royal fantasy artifacts. |
| **`[ComponentSound]`** | High | Add leather rustle or quill ink audio feedback on interaction. |
| **Inspector Controls** | High | Seamlessly wraps all serialized fields without clipping or event blocking. |
