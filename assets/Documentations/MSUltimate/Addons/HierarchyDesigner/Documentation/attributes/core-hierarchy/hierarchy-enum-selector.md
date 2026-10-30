# [HierarchyEnumSelector]

> Injects an inline dropdown popup menu directly on the hierarchy row to pick any enum value with direct random access.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyEnumSelector]` brings full dropdown popup navigation directly into the Scene Hierarchy. Rendered by `HierarchyEnumSelectorRenderer`, it draws an elegant dropdown box widget (`Width = 80f`, `BadgeColor = "#1E2B3A"`, `TextColor = "#7AAFCC"`) on the hierarchy row displaying the current enum value. Clicking the widget opens Unity's native context popup menu listing all declared enum members, allowing developers to jump directly to any desired state with full Undo support.

**The Problem:**
While `[HierarchyEnumCycler]` is ideal for enums with 2 to 4 options, enums with 6, 10, or 20 values (such as Weapon Type, Sound Channel, Animation Phase, or Monster Archetype) become frustrating to cycle through sequentially one click at a time.

**The Solution:**
Decorating extensive enum fields with `[HierarchyEnumSelector]`:
- **Direct Random Access:** Open a full dropdown menu with one click and pick any enum state immediately.
- **Sleek Embedded Widget:** Formatted as a subtle inline selector with rounded corners and clear typography.
- **Native Context Menu Integration:** Uses standard Unity `GenericMenu` popups familiar to all developers.
- **Complete Undo Integrity:** Value changes register instant Undo records in Edit Mode and update live variables during Play Mode.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public enum WeaponType { Pistol, Shotgun, AssaultRifle, SniperRifle, RocketLauncher, PlasmaCannon }

public class WeaponPickupEntity : MonoBehaviour
{
    [HierarchyEnumSelector(Width = 85f, BadgeColor = "#1E293B", TextColor = "#94A3B8")]
    public WeaponType currentWeapon = WeaponType.AssaultRifle;

    public int initialAmmoCapacity = 30;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyEnumSelectorRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyEnumSelectorAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `BadgeColor` | `string` | `"#1E2B3A"` | Hex background color of the dropdown selector widget. |
| `TextColor` | `string` | `"#7AAFCC"` | Hex text color of the active enum value inside the widget. |
| `BorderRadius` | `float` | `3f` | Corner rounding radius in pixels for the selector background. |
| `Width` | `float` | `80f` | Total width in pixels allocated to the dropdown widget. |
| `Height` | `float` | `0f` | Widget height in pixels, or `0f` to auto-match row height. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin. |
| `UndoLabel` | `string` | `"Select Enum Value"` | Transaction label registered in the Unity Undo stack. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the enum dropdown selector remains active in Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public enum AudioBusChannel { Master, Music, Ambience, SoundEffects, Dialogue, UI, Cinematic }

public class AmbientAudioEmitter : MonoBehaviour
{
    [Header("Mixer Routing")]
    [Tooltip("Select routing channel directly from the Hierarchy dropdown.")]
    [HierarchyEnumSelector(
        Width = 90f, 
        BadgeColor = "#172554", 
        TextColor = "#93C5FD", 
        BorderRadius = 3f, 
        XOffset = 6f)]
    public AudioBusChannel routingChannel = AudioBusChannel.Ambience;

    [Header("Emitter Audio")]
    public AudioClip ambientClip;
    [Range(0f, 1f)] public float volume = 0.75f;
    public bool isLooping = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyActiveButton]`**| High | Place selector to the left of the active power button using `XOffset = 26f`. |
| **`[HierarchyIcon]`** | High | Pair with category icons to distinguish audio emitters from visual props. |
| **Broad Enum Collections** | High | Recommended over `[HierarchyEnumCycler]` when the enum has 5 or more member values. |
| **Undo Stack** | High | Fully integrated with Unity `Undo.RecordObject` to allow effortless `Ctrl+Z` rollbacks. |
