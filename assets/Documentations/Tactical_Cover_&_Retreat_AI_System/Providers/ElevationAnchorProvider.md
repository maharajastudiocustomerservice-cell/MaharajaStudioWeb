# Provider: Elevation Anchor (Sniper & Overwatch)

**`ElevationAnchorProviderSO`** generates high-ground tactical candidate positions with a significant vertical advantage over the enemy (such as rooftops, catwalks, second-story balconies, and elevated watchtowers).

```
   [ AI Sniper ]
       ●  ══════════════ (Rooftop / Balcony Ledge)
       │ ╲
       │  ╲ High-Ground Line of Sight
       │   ╲
       │    ▼
  ═════╧═════════════════════
         [ Target / Player ]
```

## How It Works

1. **Vertical Sampling Expansion:** Unlike standard horizontal sampling, this provider searches along the Y-axis (`agentPosition.y + minElevationAdvantage` up to `searchRadius`) to find multi-story NavMesh layers.
2. **Elevation Advantage Verification:** Ensures the candidate point's altitude is at least `minElevationAdvantage` meters above the target's current (or last known) altitude.
3. **Ledge Edge Raycast Test (Optional):** When `requireLedgeEdge` is enabled, casts a ray downward from just in front of the candidate. If the ray falls a long distance before hitting ground, it confirms the candidate is perched right at a dramatic drop-off or overlook.

## Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `minElevationAdvantage` | `float` | `3.0` | Minimum vertical height difference (in meters) required above the target. |
| `requireLedgeEdge` | `bool` | `true` | When true, rejects gradual slopes or stairways and only accepts spots directly overlooking a ledge or railing drop-off. |

## Use Cases

* **Designated Marksmen & Snipers:** Guides long-range units to naturally ascend stairs or ladders to overlook arenas.
* **Overwatch Roles:** Heavy gunners seeking suppressive sightlines over open courtyards or objective capture zones.
* **Vertical Arenas:** Essential in multi-story urban environments, warehouses, industrial plants, and canyon maps.

## Performance & Optimization

* **Computational Cost:** **Light**. NavMesh sampling with vertical random offsets followed by a single downward raycast if ledge validation is enabled.
