# Provider: Tactical Zone

`TacticalZoneProviderSO` is a provider that generates candidate hiding spots within specific, designer-placed volumes called `Tactical Zones.` This allows for a high degree of control over the AI's positioning, guiding it to use areas intended for specific tactical purposes.

## How It Works

This system requires designers to place TacticalZone components on GameObjects with colliders in the scene. Each zone is assigned a type (e.g., Overwatch, Ambush, Defensive).
The TacticalZoneProviderSO asset is configured to look for a specific TacticalZoneType. When it runs, it queries the central TacticalZoneRegistry to find all zones of that type within the agent's search radius.
For each matching zone, the provider generates a number of random points within the zone's collider bounds. It then finds the closest valid point on the NavMesh for each random sample. These valid NavMesh points become the candidate hiding spots.
This effectively lets a designer say, "When you are in a defensive state, find cover inside one of these designated defensive areas."

## Setup

1. `Create an empty GameObject in your scene to act as the zone.`
2. `Add a collider component (e.g., BoxCollider). Mark it as a Trigger.`
3. `Add the new TacticalZone component to this GameObject.`
4. `In the TacticalZone component, set the Zone Type to the desired tactical purpose (e.g., Defensive).`
5. `Adjust the size and position of the collider to cover the tactical area. A gizmo will show the zone's color and type in the Scene view.`
6. `Create an instance of the TacticalZoneProviderSO asset in your project files.`
7. `In the provider asset's Inspector, set the Target Zone Type to match the zones you want it to find.`
8. `Add this provider asset to the Providers list in your HidingSettingsSO.`

## Use Cases

*  **Designer-Controlled Encounters:** The primary use case. Force AI snipers to use sniper nests, or ensure ambushing enemies hide in designated ambush locations.
*  **Controlling Flow of Combat:** Guide the AI to fall back to specific, pre-defined defensive lines or to use flanking routes that you have explicitly laid out.

## Performance 

Since it only samples within a few known zones instead of the entire world, it can be more performant than wide-area environmental scanners if used correctly.