# Scorer: Suppression Pressure

**`SuppressionPressureScorerSO`** is a high-stakes survival scorer that prevents AI agents from stepping into or remaining inside active incoming bullet streams and suppressive fire lanes.

```
       [ Gunfire / Incoming Cone ]
 ═══════════════════════════════════════════► (Active Bullet Stream)
               ❌ Candidate A: VETOED (-Infinity)
 
 ───────────────────────────────────────────
               ✅ Candidate B: Safe Cover (Score: 1.0)
```

## How It Works

1. Queries the scene's **[`SuppressionService`]** singleton.
2. If no `SuppressionService` exists or no active fire cones are registered, returns a baseline neutral score of `1.0`.
3. Checks if the candidate position falls within any active suppression cone (cylinder distance from the fire trajectory line).
4. **Scoring:**
   * If inside an active cone and `strictVeto` is **True**, returns `float.NegativeInfinity` to immediately disqualify the candidate.
   * If inside an active cone and `strictVeto` is **False**, returns `suppressedPenaltyScore` (e.g. `-100.0`).
   * If outside all active cones, returns `1.0`.

## Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `strictVeto` | `bool` | `true` | When true, completely rejects spots under fire (`-Infinity`). When false, allows desperate use if no other spots exist. |
| `suppressedPenaltyScore` | `float` | `-100.0` | Heavy penalty score used when `strictVeto` is disabled. |

## Use Cases

* **Reacting to Machine Gun Suppression:** Keeps AI pinned behind solid cover when an LMG or turret lays down sustained fire.
* **Sniper Bullet Tracers:** Avoids re-peeking the exact lane a high-caliber sniper just fired down.
* **Corridor Denial:** Allows players and AI alike to deny passage down hallways simply by laying down suppressing fire.

## Performance & Optimization

* **Computational Cost:** **Extremely Fast (Zero-Allocation)**. Involves simple vector dot-product and square-magnitude cylinder math against the active cone buffer in `SuppressionService`. No raycasts or memory allocations occur.
