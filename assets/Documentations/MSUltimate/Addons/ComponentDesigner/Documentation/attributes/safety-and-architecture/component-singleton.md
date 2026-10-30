# [ComponentSingleton]

> Enforces singleton architecture by validating that only one component instance exists in the active scene and warning of duplicates.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentSingleton]` ensures architectural integrity for single-instance game managers. Placed in `ComponentSlot.BeforeBody`, it scans the active scene hierarchy during editor inspection. If exactly one instance is present, it displays an architectural badge (`BannerMessage = "Scene Singleton"`). If multiple instances are discovered, it immediately flashes a prominent warning banner (`AutoWarnDuplicates = true`), alerting developers to delete or merge extraneous copies before entering Play mode.

**The Problem:**
Audio managers, game directors, input coordinators, and save managers are designed as strict singletons. In large teams, designers often accidentally paste duplicate manager prefabs into additive sub-scenes or test levels, leading to broken event listeners, dual audio listeners, or catastrophic null reference exceptions at runtime.

**The Solution:**
Decorating manager scripts with `[ComponentSingleton]`:
- **Real-Time Scene Audit:** Automatically checks for duplicate instances across all open scene hierarchies upon selection.
- **Instant Visual Warning:** Flags duplicate instances with an unmistakable yellow/orange alert banner showing the duplicate count.
- **Architectural Badge Indicator:** Affixes a clean status badge indicating the script's intended singleton role to non-programmers.
- **Proactive Bug Prevention:** Catches accidental multi-instancing during editing hours, saving hours of runtime debugging.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentSingleton(autoWarnDuplicates: true, bannerMessage: "Game Director Singleton")]
public class GameManager : MonoBehaviour
{
    public static GameManager Instance { get; private set; }

    public int targetFrameRate = 60;
    public bool isPauseMenuOpen = false;

    private void Awake()
    {
        if (Instance != null && Instance != this)
        {
            Destroy(gameObject);
            return;
        }
        Instance = this;
        DontDestroyOnLoad(gameObject);
    }
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
| **Component Slot** | `BeforeBody` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentSingletonAttribute(bool autoWarnDuplicates = true, string bannerMessage = "Scene Singleton")
```

- `autoWarnDuplicates`: Whether to automatically scan the scene and render a warning banner if multiple instances exist.
- `bannerMessage`: Custom text badge displayed when the component is confirmed as the unique scene instance.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `AutoWarnDuplicates` | `bool` | `true` | When true, scans open scenes and warns developers if duplicate copies are detected. |
| `BannerMessage` | `string` | `"Scene Singleton"` | Text badge displayed to confirm valid single-instance status. |
| `Order` | `int` | `0` | Sequence sorting order within the target component slot. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#8B5CF6", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#160E2A", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("AUDIO BUS MASTER CONTROLLER", Subtitle = "Master Volume Routing & FMOD Mixer Matrix", BackgroundColor = "#251644", TitleColor = "#E9D5FF")]
[ComponentSingleton(AutoWarnDuplicates = true, BannerMessage = "Master Audio Bus Singleton")]
public class MasterAudioBusController : MonoBehaviour
{
    [Header("Bus Volumes")]
    [Range(0f, 1f)] public float masterVolume = 1.0f;
    [Range(0f, 1f)] public float musicVolume = 0.8f;
    [Range(0f, 1f)] public float soundEffectsVolume = 0.9f;
    [Range(0f, 1f)] public float voiceChatVolume = 0.75f;

    [Header("Mixer Snapshots")]
    public string defaultSnapshotName = "Snapshot_Exploration";
    public bool isUnderwaterMuffleActive = false;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeader]`** | High | Sits directly beneath header bars, providing clear architectural context for scene directors. |
| **`[ComponentLock]`** | High | Combine with lock attributes to safeguard singleton managers from unintended modifications. |
| **Multi-Scene Workflows** | High | Properly scans across additive scenes during multi-scene editing sessions. |
| **Inspector Controls** | High | Cleanly sits in `BeforeBody`, pushing fields downward without obstructing property bindings. |
