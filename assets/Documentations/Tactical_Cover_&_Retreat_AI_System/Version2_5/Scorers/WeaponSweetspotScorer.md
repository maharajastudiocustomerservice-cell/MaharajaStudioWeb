# Scorer: Weapon Sweetspot (Optimal Range Curve)

**`WeaponSweetspotScorerSO`** is an offensive/tactical scorer that evaluates candidate positions based on how closely they match the optimal engagement distance of the AI's weapon, using a mathematical Gaussian (bell-curve) distribution.

```
  Score (0.0 to 1.0)
   1.0 ┤          ╭───────╮  ◄ Optimal Range (e.g., 18m)
       │         ╭╯       ╰╮
   0.5 ┤        ╭╯         ╰╮
       │      ╭─╯           ╰─╮
   0.0 ┴──────┴───────────────┴──────── Distance (m)
             Too Close       Too Far
```

## How It Works

1. Measures Euclidean distance $d$ from the candidate position to the primary target (or last known player position).
2. Calculates the normalized score using the Gaussian probability density formula:
   $$\text{Score}(d) = \exp\left(-\frac{(d - \text{optimalRange})^2}{2 \cdot \text{standardDeviation}^2}\right)$$
3. **Behavioral Characteristics:**
   * A spot located exactly at `optimalRange` returns a perfect score of `1.0`.
   * Spots closer or farther drop off smoothly towards `0.0`.
   * Adjusting `standardDeviation` controls how strictly the AI insists on the exact sweetspot.

## Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `optimalRange` | `float` | `15.0` | The ideal combat engagement distance in meters. |
| `standardDeviation` | `float` | `10.0` | Falloff tolerance. Smaller values make the AI strictly seek this exact distance; larger values make the preference gentler. |

## Suggested Archetype Configurations

Create multiple ScriptableObject assets with distinct values:

| Weapon Archetype | `optimalRange` | `standardDeviation` | Recommended Providers |
|---|---|---|---|
| **Shotgun / Melee Rusher** | `4.0m` | `2.5m` | `AdvanceCoverProviderSO`, `FlankPointProviderSO` |
| **SMG / CQB Operator** | `8.0m` | `4.0m` | `DoorStackProviderSO`, `CornerEdgeProviderSO` |
| **Assault Rifle Grunt** | `18.0m` | `8.0m` | `AutomaticCoverProviderSO`, `CrossfireScorerSO` |
| **DMR / Sniper Rifle** | `40.0m` | `15.0m` | `ElevationAnchorProviderSO`, `VantagePointProviderSO` |

## Performance & Optimization

* **Computational Cost:** **Negligible (Pure Math)**. Only executes distance vector calculation and `Mathf.Exp`. Runs instantaneously on any thread.
