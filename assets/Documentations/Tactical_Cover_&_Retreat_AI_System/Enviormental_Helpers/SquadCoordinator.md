# Service & Component: SquadCoordinator

The **`SquadCoordinator`** manages multi-agent coordination, spot conflict prevention, dynamic fireteam splitting, tactical military maneuvers, and collective threat memory across squads.

---

## Why Use It?

* **No Friendly Fire / Cover Conflicts:** Prevents multiple AI units from trying to claim or sprint to the same hiding spot simultaneously (`IsSpotReserved`).
* **Dynamic Fireteams:** Automatically divides squads into base-of-fire suppressors and flanking elements (`AssignFireteams`).
* **Tactical Maneuvers:** Coordinates synchronized orders such as `SuppressAndFlank`, `BoundingOverwatch`, `TacticalFallBack`, and `HoldPerimeter`.
* **Shared Threat Memory:** When one scout spots a player or hears gunfire, the entire squad is instantly alerted with the target's coordinates (`BroadcastSquadThreat`).
* **Leadership Succession:** Automatically promotes the next living squad member to Leader if the commander falls in combat.

---

## Setup Guide

1. Place an empty GameObject named `[SquadCoordinator]` in your scene and attach `SquadCoordinator`.
2. On your AI characters, set the `squadName` string on each `TacticalAgent` (e.g. `"AlphaTeam"`).
3. Agents automatically register with the `SquadCoordinator` on spawn and claim spots on cover arrival.

---

## Public API Reference

```csharp
namespace MaharajaStudio.TacticalAI.Helper
```

### 1. Fireteam & Maneuver APIs

#### `AssignFireteams`
Splits a squad into a base-of-fire suppression element and a flanking maneuver element.

```csharp
public void AssignFireteams(
    string squadID, 
    out List<TacticalAgent> suppressors, 
    out List<TacticalAgent> flankers
)
```

#### `ExecuteManeuver`
Commands an entire squad to coordinate and execute a tactical military maneuver against a target threat.

```csharp
public void ExecuteManeuver(
    string squadID, 
    TacticalSquadManeuver maneuver, 
    Transform targetThreat
)
```

**Maneuver Types:**
* **`TacticalSquadManeuver.SuppressAndFlank`**: Base-of-fire units pin the target while flankers search with offensive, wide-angle profiles.
* **`TacticalSquadManeuver.BoundingOverwatch`**: Alternating movement: one fireteam holds/covers while the other advances.
* **`TacticalSquadManeuver.TacticalFallBack`**: Coordinated retreat to safer defensive positions with desperate safety overrides.
* **`TacticalSquadManeuver.HoldPerimeter`**: Squad fans out to defensive cover surrounding an area.

---

### 2. Shared Threat Memory APIs

#### `BroadcastSquadThreat`
Broadcasts a spotted enemy or gunfire location to all squad members, updating their threat lists.

```csharp
public void BroadcastSquadThreat(string squadID, Transform threat, Vector3 lastSeenPosition)
```

#### `GetSharedThreatPosition`
Retrieves the collective memory of a target's last known coordinates for a given squad.

```csharp
public Vector3? GetSharedThreatPosition(string squadID, Transform threat)
```

#### `ClearSharedThreats`
Clears the shared threat table for a specific squad.

```csharp
public void ClearSharedThreats(string squadID)
```

---

### 3. Spot Reservation & Membership APIs

* **`ClaimSpot(string squadID, TacticalAgent agent, Vector3 position)`**: Claims a cover position for an agent.
* **`ReleaseSpot(string squadID, TacticalAgent agent)`**: Frees the claimed cover position.
* **`IsSpotReserved(string squadID, Vector3 candidatePos, TacticalAgent askingAgent)`**: Checks if another teammate is already pathing to or occupying this coordinate.
* **`GetLeader(string squadID)`**: Returns the active leader of the squad.
* **`GetSquadMembers(string squadID)`**: Returns a read-only list of all living agents in the squad.
* **`ClearAll()`**: Resets all internal tables (useful for unit testing or scene reloads).

---

## Integration Example: Fire & Maneuver

```csharp
using UnityEngine;
using MaharajaStudio.TacticalAI.Helper;

public class SquadLeaderBrain : MonoBehaviour
{
    [SerializeField] private string squadID = "AlphaTeam";
    [SerializeField] private Transform playerTarget;

    public void OnEngageEnemy()
    {
        // Issue coordinated pincer maneuver
        SquadCoordinator.Instance.ExecuteManeuver(
            squadID, 
            TacticalSquadManeuver.SuppressAndFlank, 
            playerTarget
        );
    }
}
```
