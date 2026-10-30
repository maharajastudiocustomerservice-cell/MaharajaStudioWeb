# [KeyPad]

> Transforms string, integer, and float fields into an interactive, visual on-screen keypad or keyboard with tactile themes and custom keymaps.

---

## 1. Overview & Value Proposition

**What it does:**
Adds a clickable on-screen keypad (like a numpad or calculator) directly below numeric or text fields.

**The Problem:**
Typing puzzle codes, safe passcodes, PIN numbers, or calculator inputs into generic text boxes doesn't feel like building a game. It is slow for quick testing and makes door/security systems hard to preview the way a player would experience them.

**The Solution:**
Add `[KeyPad]` above any `string`, `int`, or `float` field or property:
- **Tactile On-Screen Input:** Tap numbers and letters using an interactive visual keypad right in the Inspector.
- **Multiple Layouts:** Choose between `Numpad`, `Calculator`, `Phone`, `Qwerty`, and `Custom` layouts with one setting.
- **Visual Themes:** Switch styles between `Default`, `Dark`, `Light`, `Neumorphism`, and retro `Hacker` themes.
- **Custom Keypads:** Define custom grids of rows and keys with simple pipe and comma notation (`"1,2,3|4,5,6|7,8,9|C,0,OK"`).
- **Optional Digital Display Screen:** Display an LCD-style digital value readout above the keypad.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class SecurityDoor : MonoBehaviour
{
    [KeyPad(KeyPadLayout.Numpad, Theme = KeyPadTheme.Dark)]
    public string doorPasscode = "1234";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Field | AttributeTargets.Property` |
| **Supported Types** | `string`, `int`, `float`, `double`, `long`, `short`, `byte`, `uint`, `ulong` |
| **Collection Interface** | `ICollectionElementAttribute` (On-Demand Collapsible Toggle) |
| **Collection Cascading** | Full (`List<T>`, `T[]`, `AdvancedList<T>`, `SerializableDictionary<K, V>`) |
| **Allow Multiple** | `false` |
| **Inherited** | `true` |
| **Build Overhead** | Editor-only (Zero runtime build overhead / stripped in builds) |
| **Minimum Unity** | Unity 6 (6000.x)+ |

---

## 4. Constructors & Signatures

```csharp
public KeyPadAttribute(KeyPadLayout layout = KeyPadLayout.Numpad)
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Layout` | `KeyPadLayout` | `KeyPadLayout.Numpad` | Keypad arrangement (`Numpad`, `Calculator`, `Qwerty`, `Phone`, `Custom`). |
| `Theme` | `KeyPadTheme` | `KeyPadTheme.Default` | Visual skin (`Default`, `Dark`, `Light`, `Neumorphism`, `Hacker`). |
| `CustomKeys` | `string` | `""` | Custom key matrix string separated by `|` (rows) and `,` (keys). |
| `ButtonHeight` | `float` | `30f` | Height of individual key buttons in pixels. |
| `Spacing` | `float` | `4f` | Grid gap between keys in pixels. |
| `BorderRadius` | `float` | `4f` | Corner rounding radius of buttons and container in pixels. |
| `BackgroundColor` | `string` | `""` | Hex background color for the keypad container. |
| `ButtonColor` | `string` | `""` | Custom hex color for normal key faces. |
| `TextColor` | `string` | `""` | Custom hex color for button text labels. |
| `AccentColor` | `string` | `""` | Custom hex color for action keys (`AC`, `Enter`, Backspace). |
| `ShowDisplayScreen` | `bool` | `false` | Renders a top calculator-style LED digital readout screen. |

---

## 6. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class TerminalPuzzleLock : MonoBehaviour
{
    [Serializable]
    public class VaultTerminalNode
    {
        public string nodeName = "Sub-Level Alpha Lock";

        [KeyPad(KeyPadLayout.Numpad, Theme = KeyPadTheme.Dark)]
        public int passcode = 4321;
    }

    [BoxGroup("Cyberpunk Access Terminal", Box = true)]
    [KeyPad(
        layout: KeyPadLayout.Calculator,
        Theme = KeyPadTheme.Hacker,
        ButtonHeight = 32f,
        ShowDisplayScreen = true,
        AccentColor = "#00FF66"
    )]
    [Tooltip("Target PIN code required to unlock containment bay.")]
    public int accessPin = 7421;

    [BoxGroup("Security Terminals (Inside Class)")]
    public VaultTerminalNode primaryNode = new VaultTerminalNode();

    [BoxGroup("Direct Collection Cascading")]
    [InfoBox("[KeyPad] renders an on-demand '⌨' toggle button beside each collection row to prevent vertical layout bloat.", InspectorMessageType.Info)]
    [KeyPad(KeyPadLayout.Numpad, Theme = KeyPadTheme.Dark)]
    public int[] sectorPasscodes = new int[] { 1024, 2048, 4096 };

    [KeyPad(KeyPadLayout.Phone, Theme = KeyPadTheme.Light)]
    public List<string> emergencyHotlines = new List<string> { "911-001", "911-002" };
}
```

---

## 7. Stacking & Compatibility Matrix

- **Grouping:** Centers elegantly inside `[BoxGroup]` and `[CardGroup]`.
- **Custom Keymaps:** When `Layout = KeyPadLayout.Custom`, pass a string such as `"1,2,3|4,5,6|7,8,9|C,0,OK"` to author bespoke control pads.
- **Immediate Binding:** Clicking keys updates the serialized property immediately and commits standard Undo snapshots.

### Collection Cascading Matrix

| Collection Type | Cascading Behavior | Presentation Mode |
| :--- | :---: | :--- |
| `int[]`, `float[]` | **Supported** | Renders inline property field with compact `⌨` on-demand expansion button per row. |
| `List<string>` | **Supported** | Full QWERTY or Phone keypad available on-demand per collection entry. |
| `AdvancedList<T>` | **Supported** | Fully compatible with reorderable lists and batch actions. |
| `SerializableDictionary<K, V>` | **Supported** | Cascades to dictionary value elements matching numeric or string types. |
| Nested `[Serializable]` Classes | **Supported** | Embedded fields within class instances render independent keypads or toggles. |
