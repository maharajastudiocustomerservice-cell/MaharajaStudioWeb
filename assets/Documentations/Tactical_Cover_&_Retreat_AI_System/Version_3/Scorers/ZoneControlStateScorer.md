# Scorer: Zone Control State Scorer

**`ZoneControlStateScorerSO`** scores candidate hiding spots based on the dynamic control state of the `TacticalZone` they fall inside. It enables squad roles to prioritize secure friendly territory or push aggressively into contested combat areas.

---

## How It Works

1. **Volume Matching:** Identifies if a candidate position is enclosed within any registered `TacticalZone` bounds.
2. **State Evaluation:** Reads the zone's active `ZoneControlState`:
   * `FriendlyControlled`: Controlled exclusively by allied units.
   * `HostileControlled`: Occupied exclusively by opposing units.
   * `Contested`: Multiple opposing teams are inside the zone simultaneously.
   * `Unoccupied`: No agents currently inside.
3. **Veto Rules:** Can strictly veto (`-Infinity`) spots in hostile or contested zones, preventing vulnerable units from running into enemy-held territory.

---

## Inspector Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `preferredState` | `ZoneControlState` | `FriendlyControlled` | The zone control state this AI role actively favors. |
| `preferredScore` | `float` (0-1) | `1.0` | Score awarded when a candidate is inside a zone matching `preferredState`. |
| `friendlyScore` | `float` (0-1) | `0.8` | Score awarded for friendly controlled zones when not preferred. |
| `contestedScore` | `float` (0-1) | `0.4` | Score awarded for contested zones. |
| `unoccupiedScore` | `float` (0-1) | `0.5` | Score awarded for unoccupied zones. |
| `hostileScore` | `float` (0-1) | `0.0` | Score awarded for enemy-held zones. |
| `outsideZoneScore`| `float` (0-1) | `0.5` | Baseline score when candidate is outside all tactical zones. |
| `vetoHostileZones`| `bool` | `false` | If true, candidates inside hostile zones return `-Infinity`. |
| `vetoContestedZones`| `bool` | `false` | If true, candidates inside contested zones return `-Infinity`. |

---

## Archetype Presets

### Defensive Sniper / Medic
* `preferredState`: `FriendlyControlled` (Score: `1.0`)
* `vetoHostileZones`: `true`
* `vetoContestedZones`: `true`

### Aggressive Breacher / Rusher
* `preferredState`: `Contested` (Score: `1.0`)
* `friendlyScore`: `0.3`
* `vetoHostileZones`: `false`
