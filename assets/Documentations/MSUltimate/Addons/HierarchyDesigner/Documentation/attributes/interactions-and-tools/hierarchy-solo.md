# [HierarchySolo]

> Renders a solo toggle button directly on the hierarchy row to isolate the entity by hiding scene siblings and restoring them on toggle.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchySolo]` adds a DAW-style "Solo" toggle button (`"S"`) directly on the hierarchy row of GameObjects. Driven by `HierarchySoloRenderer`, clicking the button isolates the selected GameObject by temporarily deactivating all of its sibling GameObjects. It caches the original active states of all siblings in an internal session dictionary. Clicking the button a second time toggles solo mode off, instantly restoring every sibling back to its exact prior active/inactive state.

**The Problem:**
When working on lighting, VFX, physics prefabs, or complex environment clusters, surrounding objects clutter the Scene View and occlude the entity being tweaked. Manually turning off 20 sibling objects, tweaking the target, and then remembering which siblings were originally active and which were inactive is tedious and error-prone.

**The Solution:**
Decorating components with `[HierarchySolo]`:
- **Single-Click Solo Isolation:** Instantly isolate any GameObject from its siblings with a single click in the hierarchy.
- **Accurate State Restoration:** Caches the original state of each sibling, ensuring deactivated debug props remain inactive when solo mode ends.
- **Visual Yellow Active State:** Active solo buttons glow in vibrant yellow (`ActiveColor = "#FFD32A"`), making isolated objects unmistakable.
- **Root or Child Scope:** Works cleanly on root scene entities or nested children inside complex prefab hierarchies.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchySolo]
public class LightingHeroFixture : MonoBehaviour
{
    public Light keyLight;
    public Light fillLight;
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
| **Render Engine** | `HierarchySoloRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchySoloAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ActiveColor` | `string` | `"#FFD32A"` | Hex color of the solo button badge when solo isolation is active. |
| `InactiveColor` | `string` | `"#485460"` | Hex color of the solo button badge when solo isolation is inactive. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the solo button remains visible and interactive in Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchySolo(ActiveColor = "#FACC15", InactiveColor = "#334155", XOffset = 6f)]
public class HeroVfxRig : MonoBehaviour
{
    [Header("VFX Particle Systems")]
    public ParticleSystem auraParticles;
    public ParticleSystem groundSparks;
    public float emissionMultiplier = 1.0f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchySceneViewPing]`** | High | Combine solo isolation with SceneView framing to immediately zoom in on the isolated object. |
| **`[HierarchyActiveButton]`** | High | Use active buttons for persistent GameObject toggles and `HierarchySolo` for temporary auditioning. |
| **`[HierarchyLock]`** | High | Lock objects to prevent editing and solo them to inspect their appearance without distractions. |
| **Sibling Scope** | High | Isolates immediate transform siblings (or root scene siblings if the object is at root level). |
