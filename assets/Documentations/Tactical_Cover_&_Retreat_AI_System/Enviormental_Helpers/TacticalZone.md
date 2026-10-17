# Feature Guide: TacticalZone

The `TacticalZone` component allows level designers to designate volumes of space for specific tactical purposes (Defensive, Overwatch, Ambush, FlankRoute). It provides dynamic occupancy tracking, squad control states, and designated room entry/choke points.

## Why Use It?

* **Strategic Guidance:** Nudge AI to find cover in tactically advantageous areas (e.g., an "Overwatch" zone on a balcony for snipers).
* **Live Occupancy Tracking:** Automatically tracks all `TacticalAgent` occupants entering and exiting the zone.
* **Squad Control States:** Dynamically computes whether an area is friendly, enemy-controlled, or contested.
* **Choke Points & Ingress:** Author doorways, hallways, and breach points for coordinated team clearance.
* **Integrates with Providers:** Used by `TacticalZoneProviderSO` to constrain cover generation to specific areas.

## Setup Guide

1. Create an empty GameObject to represent your zone.
2. Add a Collider component (e.g., `BoxCollider` or `SphereCollider`) and check **Is Trigger**.
3. Attach the `TacticalZone` script.
4. Select the desired **Zone Type** from the dropdown (`Defensive`, `Overwatch`, `Ambush`, `FlankRoute`).
5. (Optional) Assign **Choke Points** (doorways, entry portals) in the inspector.

## Parameters & Properties

| Property | Type | Description |
|---|---|---|
| `zoneType` | `TacticalZoneType` | The strategic purpose of the area (`Defensive`, `Overwatch`, `Ambush`, `FlankRoute`). |
| `ControlState` | `ZoneControlState` | Current control status: `Unoccupied`, `FriendlyControlled`, `HostileControlled`, or `Contested`. |
| `Occupants` | `IReadOnlyList<TacticalAgent>` | Read-only list of all active agents currently positioned inside the zone. |
| `ChokePoints` | `IReadOnlyList<Transform>` | Designated entry/exit points, doorways, and breach choke points. |

## Public API

```csharp
namespace MaharajaStudio.TacticalAI.Helper
```

### Methods
* **`RegisterOccupant(TacticalAgent agent)`**: Manually registers an agent inside the zone and updates control state. (Called automatically by trigger colliders).
* **`UnregisterOccupant(TacticalAgent agent)`**: Manually removes an agent from the zone.
* **`UpdateControlState(string friendlySquadName = null)`**: Re-evaluates squad affiliations of occupants to update `ControlState`.
* **`AddChokePoint(Transform point)`** / **`RemoveChokePoint(Transform point)`**: Runtime management of doorway/corridor choke points.

### Events
* **`OnAgentEnteredZone (Action<TacticalAgent>)`**: Fires when an AI agent enters the zone volume.
* **`OnAgentExitedZone (Action<TacticalAgent>)`**: Fires when an agent departs the zone volume.
* **`OnControlStateChanged (Action<ZoneControlState>)`**: Fires when the zone transitions between Unoccupied, Friendly, Hostile, or Contested.

## Gameplay Scripting Example

```csharp
using UnityEngine;
using MaharajaStudio.TacticalAI.Helper;

public class ZoneDefenseController : MonoBehaviour
{
    [SerializeField] private TacticalZone objectiveZone;

    void OnEnable()
    {
        objectiveZone.OnControlStateChanged += HandleZoneStateChanged;
    }

    void OnDisable()
    {
        objectiveZone.OnControlStateChanged -= HandleZoneStateChanged;
    }

    private void HandleZoneStateChanged(ZoneControlState state)
    {
        if (state == ZoneControlState.Contested)
        {
            Debug.LogWarning("Objective zone is contested! Reinforcements requested.");
        }
        else if (state == ZoneControlState.HostileControlled)
        {
            Debug.LogError("Objective lost to hostile forces!");
        }
    }
}
```
