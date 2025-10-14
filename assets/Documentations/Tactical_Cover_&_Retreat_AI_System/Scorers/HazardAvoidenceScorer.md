# Scorer: Hazard Avoidance

`HazardAvoidanceScorerSO` prevents the AI from choosing hiding spots inside known environmental dangers, such as fires, poison clouds, or the blast radius of a grenade.

## How It Works

This system relies on Hazard components being placed on objects that represent a threat. Any GameObject with a Hazard component will register itself with a central HazardRegistry when it becomes active.
The HazardAvoidanceScorer queries this registry to get a list of all active hazards. For each candidate hiding spot, it checks the distance to every hazard.
If the candidate's position is within the defined radius of any Hazard object, the scorer returns float.NegativeInfinity. This instantly and absolutely disqualifies the spot, forcing the AI to look for cover elsewhere. This is a critical self-preservation behavior.

## Setup

On any GameObject that represents a danger (e.g., a fire particle system, a grenade prefab), add the new Hazard component.
Adjust the Radius property on the Hazard component to match the area of effect of the danger. A red gizmo in the Scene view will help you visualize this area.
Create an instance of the HazardAvoidanceScorerSO asset in your project files.
Add this scorer asset to the Scorers list in your HidingSettingsSO. It is highly recommended to give this scorer a high weight (e.g., 5.0) to ensure its decisions are always prioritized.

## Use Cases

*  **Dynamic Dangers:** Essential for making AI react to dynamic events like grenades, molotovs, or artillery strikes.
*  **Persistent Hazards:** Prevents AI from unintelligently pathing through fires, acid pools, or other static level hazards when looking for cover.
*  **Enhanced Believability:** Stops the AI from making immersion-breaking mistakes, making them feel more aware and intelligent.