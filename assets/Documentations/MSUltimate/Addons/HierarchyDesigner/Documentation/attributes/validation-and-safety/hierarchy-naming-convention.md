# [HierarchyNamingConvention]

> Enforces scene naming conventions (mandatory affixes, disallowed whitespace) and displays an alert icon on rule violations.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyNamingConvention]` enforces team and studio naming standards on GameObjects decorated with marked components. It validates that the host GameObject begins with a mandatory prefix (`Prefix`), concludes with a mandatory suffix (`Suffix`), and adheres to whitespace rules (`AllowSpaces = false`). If the GameObject name violates any rule, an eye-catching warning badge is rendered directly on the hierarchy row.

**The Problem:**
In multi-developer studios, inconsistent naming (e.g. `Light_Spot`, `SpotLight`, `spot light (1)`) breaks automated search tools, scene parsing scripts, and CI build validators. Enforcing conventions through manual code reviews or external linters creates friction and interrupts level designer workflows.

**The Solution:**
Decorating components with `[HierarchyNamingConvention]`:
- **Real-Time Visual Feedback:** Immediate visual warning badges appear in the Hierarchy window when an artist or designer creates or renames an object improperly.
- **Prefix & Suffix Validation:** Enforce prefix constraints (e.g. `Prefix = "SYS_"` or `Prefix = "UI_"`) and suffix standards (e.g. `Suffix = "_Trigger"`).
- **Whitespace Sanitation:** Set `AllowSpaces = false` to forbid spaces in GameObject names, preventing broken paths in string-based resource loaders or asset bundles.
- **Custom Alert Color:** Adjust the warning pill tint (`WarnColor`) to match warning levels across project categories.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyNamingConvention(
    Prefix = "SPAWN_",
    Suffix = "_Point",
    AllowSpaces = false)]
public class SpawnPointMarker : MonoBehaviour
{
    public int teamId = 1;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyNamingConventionRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyNamingConventionAttribute()
```

- Parameterless constructor configured via named properties (`Prefix`, `Suffix`, `AllowSpaces`, `WarnColor`, `XOffset`).

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Prefix` | `string` | `""` | Mandatory prefix string required at the beginning of the GameObject name. |
| `Suffix` | `string` | `""` | Mandatory suffix string required at the end of the GameObject name. |
| `AllowSpaces` | `bool` | `true` | When false, flags any GameObject name containing whitespace characters as a violation. |
| `WarnColor` | `string` | `"#FFA502"` | Hex color string for the naming violation warning badge. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether naming validation continues evaluating during active Play Mode. |
| `Order` | `int` | `0` | Drawing priority order relative to other hierarchy row renderers. |

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

namespace ProjectZero.Audio
{
    // Enforces audio emitter naming standard: AUD_EmitterName_Ambience
    [HierarchyNamingConvention(
        Prefix = "AUD_",
        Suffix = "_Ambience",
        AllowSpaces = false,
        WarnColor = "#E67E22")]
    public class AmbientAudioEmitter : MonoBehaviour
    {
        public AudioClip ambienceClip;
        [Range(0f, 1f)] public float volume = 0.75f;
        public float maxDistance = 25f;
    }

    // UI dialogue trigger enforcing strict UI_ prefix without trailing spaces
    [HierarchyNamingConvention(
        Prefix = "UI_",
        AllowSpaces = false,
        WarnColor = "#F1C40F")]
    public class DialoguePromptTrigger : MonoBehaviour
    {
        public string dialogueNodeKey = "Intro_Greeting";
        public bool triggerOnce = true;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyTooltip]`** | High | Hover tooltip can explain the required naming conventions to new team members. |
| **`[HierarchyNumberedSequence]`** | High | Combine naming conventions with sequential number formatting for clean sibling lists. |
| **`[HierarchyPrefixBadge]`** | High | Visually display a stylized category badge alongside convention enforcement. |
| **`[HierarchyFolder]`** | High | Keep naming conventions strictly checked within designated subfolders. |
