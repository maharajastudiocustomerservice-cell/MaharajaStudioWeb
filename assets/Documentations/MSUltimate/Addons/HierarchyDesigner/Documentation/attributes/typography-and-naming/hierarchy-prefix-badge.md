# [HierarchyPrefixBadge]

> Prepends a styled tag pill badge in front of the GameObject hierarchy name.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyPrefixBadge]` inserts a compact, rounded pill badge (e.g. `[FX]`, `[UI]`, `[AI]`, `[AUDIO]`) directly in front of the GameObject's label in the Hierarchy window.

**The Problem:**
Developers often prefix GameObject names directly in string format (e.g. `UI_MainMenu`, `FX_Explosion`, `AI_EnemyGrunt`). This clutter pollutes GameObject strings in code, breaks string searches, and looks inconsistent if team members use different casing conventions (`[FX]`, `FX_`, `(FX)`).

**The Solution:**
Decorating components with `[HierarchyPrefixBadge]`:
- **Clean Visual Separation:** Leaves the real `gameObject.name` clean for runtime code and scripts, while displaying a polished colored badge in the editor.
- **Custom Badge Background & Text Colors:** Highlight different disciplines (e.g. blue for `[UI]`, orange for `[FX]`, purple for `[AI]`).
- **Flexible Constructors:** Instantly specify badge text directly in the attribute constructor (`[HierarchyPrefixBadge("AUDIO")]`).
- **Independent Name Styling:** Adjust badge text and object label colors independently (`BadgeTextColor`, `NameTextColor`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyPrefixBadge("AUDIO", BadgeColor = "#3B82F6")]
public class AmbiencePlayer : MonoBehaviour
{
    public AudioClip ambientLoop;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class` \| `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyPrefixBadgeRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyPrefixBadgeAttribute()
public HierarchyPrefixBadgeAttribute(string badgeText)
```

- **`badgeText`** (`string`): The text string displayed inside the pill badge (e.g. `"UI"`, `"VFX"`, `"BOSS"`).
- Parameterless constructor defaults to `"TAG"` with blue background styling (`"#3498DB"`).

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `BadgeText` | `string` | `"TAG"` | Text displayed inside the rounded pill badge. |
| `BadgeColor` | `string` | `"#3498DB"` | Hex background color of the pill badge container. |
| `BadgeTextColor` | `string` | `"#FFFFFF"` | Hex color of the text inside the badge. |
| `NameTextColor` | `string` | `"#E0E0E0"` | Hex color of the GameObject name following the badge. |
| `Bold` | `bool` | `true` | Whether to render the badge and name text in bold weight. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the badge remains visible during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row decorations. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyPrefixBadge(
    "VFX", 
    BadgeColor = "#F97316", 
    BadgeTextColor = "#FFFFFF", 
    NameTextColor = "#FED7AA", 
    Bold = true)]
public class ExplosionParticleCluster : MonoBehaviour
{
    [Header("Particle Cluster")]
    public ParticleSystem shockwaveParticles;
    public ParticleSystem debrisParticles;
    public float lifetime = 3.5f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyTooltip]`** | High | Pair with hover tooltips detailing particle count or pool allocation sizes. |
| **`[HierarchySubtitleText]`** | High | Display tag pills at the front and live performance metrics at the back. |
| **`[HierarchyFolder]`** | High | Organizes tagged entities neatly within categorized virtual folders. |
| **`[HierarchyTextColor]`** | Incompatible | `[HierarchyPrefixBadge]` handles both badge and name drawing; avoid combining with static text color attributes. |
