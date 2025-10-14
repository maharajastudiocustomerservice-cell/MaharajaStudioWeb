# Feature Guide: Hazard

The Hazard component allows you to designate a spherical area in your scene as dangerous. The AI system will actively avoid choosing any hiding spots that fall within the radius of a Hazard object, making the AI appear smarter and more aware of environmental dangers.

## Why Use It?

*  **Environmental Awareness:** Prevents the AI from making foolish mistakes, like hiding in a pool of fire, an acid spill, or an active minefield.
*  **Dynamic Obstacles:** Can be added at runtime to temporarily block off areas. For example, you could spawn a GameObject with a Hazard component when a grenade explodes to prevent AI from running into the blast zone.
*  **Designer-Friendly:** Provides a simple and visual way to define "no-go" zones for the AI without complex NavMesh modifications.

## Setup Guide

1. Select the GameObject in your scene that represents a dangerous area (e.g., a fire particle effect, a poison cloud).
2. Click Add Component and search for Hazard. Add the script.
3. Adjust the Radius property in the Inspector to define the size of the dangerous area.
4. When the GameObject is selected, a semi-transparent red sphere gizmo will be drawn in the Scene View, clearly visualizing the hazard's area of effect.

## Parameters

*  **radius (float):** The radius of the dangerous spherical area, measured in meters from the GameObject's transform origin.

## How It Works

The `Hazard` component works in conjunction with the `HazardAvoidanceScorerSO`. If this scorer is included in your `HidingSettingsSO`, it will perform a check for every potential hiding spot. If a spot is found to be inside the radius of any active Hazard in the scene, the scorer immediately returns a score of NegativeInfinity, which instantly disqualifies that spot from being chosen.