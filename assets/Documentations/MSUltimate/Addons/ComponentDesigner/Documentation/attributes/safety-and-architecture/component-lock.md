# [ComponentLock]

> Adds an interactive padlock header toggle that locks all inspector fields into read-only mode to prevent accidental edits.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentLock]` safeguards critical configuration components against inadvertent modifications during playtesting and level building. Injected into `ComponentSlot.BodyWrapper`, it adds an interactive padlock toggle button to the component header. When locked (`DefaultLocked = true`), the entire property tree is made strictly read-only, graying out input controls and displaying a protective status banner (`LockMessage = "Component Locked (Read-Only)"`, `ShowLockBanner = true`).

**The Problem:**
Core game managers—such as physics gravity constants, network server addresses, audio bus master routing, and monetization product IDs—are calibrated once and rarely need editing. Team members clicking through inspector hierarchies frequently modify numbers or drag incorrect assets by mistake, creating insidious production bugs.

**The Solution:**
Protecting mission-critical components with `[ComponentLock]`:
- **One-Click Inspector Freeze:** Instantly switches all fields within the component into an unmodifiable, read-only state.
- **Header Padlock Toggle:** An intuitive lock icon (`🔒` / `🔓`) in the component header allows authorized developers to unlock and edit values with a single intentional click.
- **Protective Warning Banner:** Renders a distinct banner across the inspector indicating that fields are safely guarded.
- **Non-Destructive Wrapper:** Operates at the UI Toolkit container level, ensuring underlying serialized data remains completely intact.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentLock(defaultLocked: true, lockMessage: "Master Server Network Settings Locked")]
public class MasterNetworkCoordinator : MonoBehaviour
{
    public string productionServerIp = "192.168.1.100";
    public int networkPort = 7777;
    public string encryptionHandshakeSecret = "SEC-84920-ALPHA";
    public bool isSslEncryptionMandatory = true;
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
public ComponentLockAttribute(bool defaultLocked = false, string lockMessage = "Component Locked (Read-Only)")
```

- `defaultLocked`: Whether the inspector initializes in the locked read-only state upon first selection.
- `lockMessage`: Text banner displayed across the component body while locked.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `DefaultLocked` | `bool` | `false` | When true, inspector fields are locked into read-only mode upon startup. |
| `LockMessage` | `string` | `"Component Locked (Read-Only)"` | Banner message displayed when the padlock is engaged. |
| `ShowLockBanner` | `bool` | `true` | Whether to display the visual status notification banner above locked fields. |
| `Order` | `int` | `0` | Sequence sorting order within the target component slot. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#D97706", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#1A1208", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("GLOBAL ECONOMY CALIBRATION", Subtitle = "Protected Gold & Premium Gem Rates", BackgroundColor = "#26190C", TitleColor = "#FDE68A")]
[ComponentLock(DefaultLocked = true, LockMessage = "Economy constants locked to prevent accidental tuning changes.", ShowLockBanner = true)]
public class GlobalEconomyConstants : MonoBehaviour
{
    [Header("Currency Multipliers")]
    public float goldDropRateMultiplier = 1.0f;
    public int premiumGemsPerLevelUp = 5;
    public float auctionHouseTaxRatePercent = 0.05f;

    [Header("Transaction Caps")]
    public int maxDailyTransactionLimit = 50000;
    public bool isAntiFraudTelemetryActive = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeader]`** | High | Embeds the padlock icon directly into the header bar opposite the title. |
| **`[ComponentDeprecated]`** | High | Combine both attributes to lock legacy components and guide users to new replacements. |
| **`[ReadOnly]` Fields** | High | Locking applies globally across the container, reinforcing per-field read-only attributes. |
| **Inspector Controls** | High | Disables pointer events on fields when locked while preserving copy-to-clipboard functionality. |
