# Tactical AI 2.5: What's New & Release Notes

Tactical AI Version 2.5 introduces high-fidelity ballistics awareness, tactical CQB spatial analysis, weapon-range behavioral tuning, and high-ground vantage anchor capabilities.

---

## 🌟 Highlights of Version 2.5

```
                               Tactical AI 2.5
    ┌─────────────────────────────────┼─────────────────────────────────┐
    ▼                                 ▼                                 ▼
[ Tactical CQB & Sniping ]    [ Dynamic Suppression ]       [ Weapon & 360° Security ]
• DoorStackProviderSO         • SuppressionService          • WeaponSweetspotScorerSO
• ElevationAnchorProviderSO   • SuppressionPressureScorerSO • FlankExposureRiskScorerSO
```

### 1. Dynamic Suppression & Incoming Fire Awareness
* **`SuppressionService`**: A high-performance singleton service that tracks bullet paths and suppressive fire cones in real-time with automatic temporal decay.
* **`SuppressionPressureScorerSO`**: Survival scorer that immediately penalizes or vetoes candidate spots that fall inside active bullet corridors or incoming fire lines.

### 2. Advanced CQB & High-Ground Spatial Providers
* **`DoorStackProviderSO`**: Dynamically scans geometry to locate doorway edges and choke point openings, generating "Stack Left" and "Stack Right" candidates hugged against the wall outside the fatal funnel.
* **`ElevationAnchorProviderSO`**: Identifies multi-story NavMesh surfaces with significant height advantage over targets, verifying drop-off ledges for snipers, marksmen, and overwatch units.

### 3. Weapon Range Sweetspots & 360° Flank Security
* **`WeaponSweetspotScorerSO`**: Mathematical Gaussian (bell-curve) scorer allowing you to configure precise optimal engagement ranges and falloff tolerances per weapon archetype (e.g. Shotguns, Assault Rifles, Sniper Rifles).
* **`FlankExposureRiskScorerSO`**: Radial 360° raycast scorer that measures ambient exposure. Rewards spots tucked into tight corners with minimal open sightlines and penalizes spots exposed to open flanks.

---

## 📦 New Component Summary

| Component | Category | Type | Purpose |
|---|---|---|---|
| [`DoorStackProviderSO`] | Tactical | Provider | Generates wall-hugging stack points beside doorway openings. |
| [`ElevationAnchorProviderSO`] | Tactical | Provider | Generates high-ground sniper perches overlooking targets. |
| [`SuppressionPressureScorerSO`] | Survival | Scorer | Vetoes/penalizes spots inside active gunfire streams. |
| [`WeaponSweetspotScorerSO`] | Offensive | Scorer | Evaluates distance using a tunable Gaussian weapon range curve. |
| [`FlankExposureRiskScorerSO`] | Survival | Scorer | Measures 360° radial exposure to reward deep corner protection. |
| [`SuppressionService`] | Helper/Service | MonoBehaviour | Central manager for tracking bullet trajectories and fire cones. |

---

## 🚀 Quick Integration Guide

### Setting Up Suppression in Your Scene
1. Create an empty GameObject in your scene named `[SuppressionService]`.
2. Attach the `SuppressionService` component to it.
3. In your player or weapon firing script, call:
```csharp
using MaharajaStudio.TacticalAI.Helper;

public class Weapon : MonoBehaviour
{
    public void Fire()
    {
        // ... spawn bullet or raycast ...
        
        // Notify the Tactical AI system of the incoming fire stream
        if (SuppressionService.Instance != null)
        {
            SuppressionService.Instance.RegisterSuppressiveFire(
                origin: muzzleTransform.position,
                direction: muzzleTransform.forward,
                length: 50f,      // 50m range
                radius: 1.5f,     // 1.5m danger width
                duration: 0.8f    // danger lasts 0.8 seconds
            );
        }
    }
}
```

### Configuring Weapon-Specific AI Roles
With `WeaponSweetspotScorerSO`, you can create distinct ScriptableObject assets for different AI unit roles:

* **Shotgun Rusher Asset**:
  * `Optimal Range`: `4.0`
  * `Standard Deviation`: `3.0`
* **Assault Rifle Grunt Asset**:
  * `Optimal Range`: `18.0`
  * `Standard Deviation`: `8.0`
* **Sniper Asset**:
  * `Optimal Range`: `45.0`
  * `Standard Deviation`: `15.0`
