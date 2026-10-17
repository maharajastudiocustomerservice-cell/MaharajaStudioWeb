# **Tactical AI 2.5: Upgrade & Setup Guide**

This guide covers everything you need to upgrade your project to **Tactical AI v2.5** and start using the new CQB, Sniping, Suppression, and Weapon-Range features.

---

## ⚡ What's New in v2.5

Tactical AI 2.5 is **100% backwards-compatible** with existing v2.0 setups. All additions are additive and can be adopted modularly.

```
┌────────────────────────────────────────────────────────────────────────────┐
│                              NEW IN VERSION 2.5                            │
├────────────────────────────┬───────────────────────────────────────────────┤
│ Providers                  │ • DoorStackProviderSO (CQB door stacking)     │
│                            │ • ElevationAnchorProviderSO (High-ground)     │
├────────────────────────────┼───────────────────────────────────────────────┤
│ Scorers                    │ • SuppressionPressureScorerSO                 │
│                            │ • WeaponSweetspotScorerSO                     │
│                            │ • FlankExposureRiskScorerSO                   │
├────────────────────────────┼───────────────────────────────────────────────┤
│ Services                   │ • SuppressionService                          │
└────────────────────────────┴───────────────────────────────────────────────┘
```

---

## 🛠️ Step-by-Step Setup

### Step 1: Add the Suppression Service to Your Scene
To enable incoming fire and bullet stream awareness for your AI:
1. In your game scene, create an empty GameObject named `[SuppressionService]`.
2. Add the `SuppressionService` component.
3. Hook up your weapon scripts to call `SuppressionService.Instance.RegisterSuppressiveFire(...)` when firing.

```csharp
using MaharajaStudio.TacticalAI.Helper;

// When firing a weapon:
SuppressionService.Instance?.RegisterSuppressiveFire(
    origin: muzzle.position, 
    direction: muzzle.forward, 
    length: 50f, 
    radius: 1.5f, 
    duration: 0.8f
);
```

### Step 2: Create Weapon Sweetspot Assets
Right-click in your Project window:
`Create > TacticalAI > Scorers > Offensive > Weapon Sweetspot`

Create individual asset files for your weapon types:
* `Scorer_ShotgunSweetspot.asset` (`optimalRange`: `4.0`, `standardDeviation`: `2.5`)
* `Scorer_RifleSweetspot.asset` (`optimalRange`: `18.0`, `standardDeviation`: `8.0`)
* `Scorer_SniperSweetspot.asset` (`optimalRange`: `40.0`, `standardDeviation`: `15.0`)

### Step 3: Add CQB & Elevation Providers to Settings / Squad Roles
1. Select your `TacticalAISettingsSO` or `SquadRoleSO` asset.
2. Under **Providers**, add:
   * `DoorStackProviderSO` (for doorframe / choke point stacking).
   * `ElevationAnchorProviderSO` (for high-ground sniper & overwatch positions).
3. Under **Scorers**, add:
   * `SuppressionPressureScorerSO` (Weight: `2.0` - `3.0`)
   * `FlankExposureRiskScorerSO` (Weight: `1.0` - `2.0`)
   * `WeaponSweetspotScorerSO` (Weight: `1.5` - `2.5`)

---

## 🔍 Visualizing in Tactical Decision Inspector Pro

All new scorers and providers integrate directly with the **Tactical Decision Inspector Pro** window:
* `DoorStack` and `ElevationAnchor` candidate spots will appear with their dedicated provider tags.
* The **Radar Chart** and **Scorer Breakdown** table will display real-time values for `SuppressionPressure`, `WeaponSweetspot`, and `FlankExposureRisk`.
