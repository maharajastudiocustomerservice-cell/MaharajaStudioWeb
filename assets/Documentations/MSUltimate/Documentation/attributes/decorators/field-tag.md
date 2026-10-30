# [FieldTag]

> Injects a colored badge chip directly beside a field label to mark category, network authority, or safety tier.

---

## 1. Overview & Value Proposition

**What it does:**
Attaches a clean pill badge (like `[Server]`, `[Client]`, `[WIP]`, or `[Audio]`) next to a field's name.

**The Problem:**
In team environments, designers and engineers often wonder which properties are synchronized over the network, which are client-only, or which are experimental work-in-progress. Plain variable names or comments are easy to overlook.

**The Solution:**
Add `[FieldTag]` to any property:
- **Instant Category Recognition:** Tag variables with clear visual tags like `Server`, `Client`, `Critical`, or `Deprecated`.
- **Custom Color Palettes:** Set background and text colors to match your studio's tag system (e.g. red for Server, blue for Client).
- **Stack Multiple Tags:** Attach more than one tag to a single property (e.g. `[Network]` + `[Server]`).
- **Clean Alignment:** Aligns neatly next to the property label without pushing inputs off-screen.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class NetworkPlayer : MonoBehaviour
{
    [FieldTag("Server-Only", colorHex: "#E74C3C")]
    public float trueHealth = 100f;

    [FieldTag("Client-Local", colorHex: "#3498DB")]
    public float smoothedHealth = 100f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public FieldTagAttribute(string tagName, string colorHex = "#3498db", string textColorHex = "#ffffff")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `tagName` | `string` | *(Required)* | The label text displayed inside the badge pill. |
| `colorHex` | `string` | `"#3498db"` | Background hex color of the badge chip. |
| `textColorHex` | `string` | `"#ffffff"` | Text font hex color. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `TagName` | `string` | *(Required)* | Badge text string. |
| `ColorHex` | `string` | `"#3498db"` | Tag background color. |
| `TextColorHex` | `string` | `"#ffffff"` | Tag text color. |
| `Order` | `int` | `0` | Execution priority relative to other attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class MultiplayerLobbyConfig : MonoBehaviour
{
    [Header("Network Synchronization")]
    [FieldTag("RPC", colorHex: "#9B59B6")]
    [FieldTag("Authority", colorHex: "#E67E22")]
    public string hostAddress = "192.168.1.10";

    [FieldTag("Local Only", colorHex: "#2ECC71")]
    public bool enableDebugOverlay = true;

    [FieldTag("Experimental", colorHex: "#F1C40F", textColorHex: "#000000")]
    public bool useLagCompensationV2;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[SuffixLabel]` | Supported | Pair together with suffix tags on the right and category tags on the left. |
| `[BoxGroup]` | Supported | Functions normally inside group containers. |
| `[ReadOnly]` | Supported | Badges remain clearly visible on read-only properties. |
