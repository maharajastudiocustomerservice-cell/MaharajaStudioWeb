# Provider: Door Stack Points (CQB Breach)

**`DoorStackProviderSO`** is a specialized tactical provider designed for Close Quarters Battle (CQB) environments. It dynamically detects doorways, archways, and narrow choke points, generating "stack-up" candidate points on the walls immediately adjacent to the opening.

```
                   [ Doorway Opening ]
       Wall                 |                 Wall
 ═════════════════          |          ═════════════════
   [ Stack Left ]           |            [ Stack Right ]
         ●                  |                  ●
                            ▼
                     (Fatal Funnel)
```

## How It Works

Instead of placing agents directly in the doorway center ("the fatal funnel"), this provider ensures agents take up preparatory positions alongside the doorframe:

1. **Environmental Sampling:** Samples random candidate positions across the NavMesh within `EffectiveSearchRadius`.
2. **Wall Proximity Detection:** Performs a sphere cast from each sample against the `EffectiveOccluderMask` to identify nearby solid walls and retrieve their surface normals.
3. **Gap / Opening Scanning:** Steps incrementally along the wall surface perpendicular to the normal. When the ray stops hitting the wall and encounters open space, it identifies the doorframe edge.
4. **Stack Offset Placement:** Projects a point offset outward from the edge along the wall (`stackOffset`) and slightly back along the wall normal (`0.5m`).
5. **NavMesh Validation:** Projects the computed stack point back onto the NavMesh and attaches the wall normal as the candidate's cover normal.

## Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `maxDoorwayWidth` | `float` | `3.0` | Maximum width of a passage to be considered a doorway or breach opening. |
| `stackOffset` | `float` | `1.0` | Distance in meters from the doorframe edge to place the stack point. |
| `raycastDepth` | `float` | `2.0` | Forward/backward depth tolerance when searching for initial wall geometry. |

## Use Cases

* **Room Clearing / CQB Breaching:** Allows fireteams to stack up outside a room before rushing in or throwing flashbangs/grenades.
* **Corridor & Corner Clearing:** Keeps AI against walls when turning sharp corridor bends rather than exposing themselves in the center.
* **Coordinated Squad Entries:** Combined with `SquadReservationScorerSO`, two squad members will naturally take opposite sides of the door (Stack Left & Stack Right).

## Performance & Optimization

* **Computational Cost:** **Low to Moderate**. Performs a short series of raycasts along detected walls only when near occluding geometry.
* **LOD Awareness:** Respects `GetCandidateCount(ctx)` and scales with LOD distance bands defined in your `TacticalAISettingsSO`.
