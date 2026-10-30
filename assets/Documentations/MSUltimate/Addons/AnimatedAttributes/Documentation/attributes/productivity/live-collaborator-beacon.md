# [LiveCollaboratorBeacon]

> Displays a pulsing multiplayer collaborator avatar badge anchored to an inspector field, signaling active editing by a remote teammate.

---

## 1. Overview & Value Proposition

**What it does:**
`[LiveCollaboratorBeacon]` brings collaborative multiplayer awareness into the Unity Inspector. It anchors a floating, pill-shaped avatar badge (`Initials`) directly to the top-right corner of the serialized property field (`right = -6, top = -6`). The badge is rendered in a custom color (`AvatarColor`) with bold typography, accompanied by a status descriptor (`StatusText`), and oscillates continuously with a gentle sinusoidal scale pulse (`Mathf.Sin(time) * 0.15f + 0.85f`) to signal active remote editing or ownership.

**The Problem:**
In multi-developer studios and distributed teams, multiple level designers, gameplay programmers, or technical artists often work on the same scenes, ScriptableObjects, or prefabs simultaneously. Without visual indicators in the editor, team members frequently overwrite each other's serialized property modifications or clash over shared assets.

**The Solution:**
Decorating shared or concurrent properties with `[LiveCollaboratorBeacon]`:
- **Real-Time Presence Indicators:** Instantly shows who is editing or assigned to a specific field via stylized user initials (`JD`, `AL`, `MS`).
- **Pulsing Animation Heartbeat:** Draws attention with a low-frequency scale pulse that operates via UI Toolkit scheduling without scene-view lag.
- **Color-Coded Teammates:** Assign distinct avatar hex colors (`AvatarColor`) per developer or department role (e.g. blue for programming, purple for art, orange for design).
- **Non-Destructive Absolute Layout:** Anchors as an overlay badge on the target property element without distorting the underlying field width or alignment.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class SharedLevelConfig : MonoBehaviour
{
    [LiveCollaboratorBeacon(initials: "AL", avatarColor: "#3B82F6")]
    public float globalGravityMultiplier = 9.81f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public LiveCollaboratorBeaconAttribute(string initials = "JD", string avatarColor = "#3B82F6")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `initials` | `string` | `"JD"` | Collaborator initials displayed inside the avatar tag. |
| `avatarColor` | `string` | `"#3B82F6"` | Hex color string for the collaborator avatar background badge. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Initials` | `string` | `"JD"` | Teammate initials rendered inside the avatar badge. |
| `AvatarColor` | `string` | `"#3B82F6"` | Hex color string for the collaborator avatar pill. |
| `StatusText` | `string` | `"Editing..."` | Status tooltip or label displayed alongside the avatar badge. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class GameEconomySharedAsset : ScriptableObject
{
    [Header("Lead Systems Designer")]
    [LiveCollaboratorBeacon(
        initials: "SK", 
        avatarColor: "#8B5CF6", 
        StatusText = "Balancing drop rates"
    )]
    public float legendaryDropRatePercent = 2.5f;

    [Header("Economy Programmer")]
    [LiveCollaboratorBeacon(initials: "AR", avatarColor: "#10B981")]
    public int baseStartingGold = 250;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Floats cleanly in the top-right corner of fields inside grouped containers. |
| `[DiffHighlightFlash]` | Stacking | Pairs with diff highlights to show which teammate altered an unsaved field. |
| `[ReadOnly]` | Supported | Can decorate read-only fields to designate developer ownership without allowing edits. |
