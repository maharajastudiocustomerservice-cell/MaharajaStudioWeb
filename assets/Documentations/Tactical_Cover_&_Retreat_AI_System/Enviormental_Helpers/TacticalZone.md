# Feature Guide: TacticalZone

The TacticalZone component allows you to define a large volume of space with a specific tactical purpose. It's a powerful tool for level designers to guide the AI's high-level strategy, encouraging it to choose hiding spots that align with a broader team objective or a specific combat style.

## Why Use It?

*  **Strategic Guidance:** Nudge AI to find cover in tactically advantageous areas. For example, you can create an "Overwatch" zone on a balcony to encourage sniper-type AI to hide there.
*  **Define Combat Areas:** Create "Ambush" zones in forests or "Defensive" zones around a capture point to make the AI's behavior context-aware.
*  **Improves Provider Efficiency:** The TacticalZoneProviderSO can be set to only generate candidates within a specific zone type, focusing the AI's search and improving performance.

## Setup Guide

1. Create an empty GameObject to represent your zone.
2. Add a Collider component to it (e.g., a BoxCollider or SphereCollider). This collider defines the boundaries of the zone.
3. Crucially, check the Is Trigger box on the Collider component. This prevents it from physically blocking characters.
4. Click Add Component and add the TacticalZone script.
5. In the TacticalZone component, select the desired Zone Type from the dropdown. The gizmo color in the scene will update to reflect your choice.

## Parameters

*  **zoneType (TacticalZoneType):** The tactical purpose of this area.
*  **Defensive:** Best for holding a critical position or objective.
*  **Overwatch:** Ideal for elevated positions with good sightlines (e.g., sniper nests).
*  **Ambush:** Suited for concealed areas intended for flanking or surprise attacks.
*  **FlankRoute:** Can be used to designate paths or areas that are good for repositioning.

## How It Works

The `TacticalZone` component is used by the `TacticalZoneProviderSO`. In your `HidingSettingsSO`, you add this provider and configure its Target Zone Type to match the zones you want the AI to use. When the AI searches for cover, this provider will only generate potential hiding spots inside the bounds of TacticalZones that match its target type.
