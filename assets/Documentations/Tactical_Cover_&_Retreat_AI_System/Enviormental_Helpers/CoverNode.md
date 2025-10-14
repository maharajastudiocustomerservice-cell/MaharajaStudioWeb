# Feature Guide: CoverNode

The `CoverNode` component is a simple and direct way for level designers to manually place a high-quality, explicit hiding spot in the world. It gives you precise, pixel-perfect control over where an AI can take cover, ensuring that tactically important locations are always available for the AI to use.

## Why Use It?

*  **Designer Control:** Guarantees that specific locations are always considered as potential cover, overriding procedural generation.
*  **Tactical Precision:** Perfect for creating specific flanking routes, ambush points, or defensive strongholds.
*  **Reliability:** Ensures that cover is available even in complex or geometrically noisy environments where automatic providers might struggle.
*  **Intelligence:** When used with the DirectionalCoverNodeProviderSO, the AI can intelligently select only the nodes that provide cover relative to the current threat direction.

## Setup Guide

1. In your scene, create a new Empty GameObject at the exact position where you want the AI to stand.
Select the new GameObject and click Add Component. Search for CoverNode and add the script.
2. In the Scene View, you will now see a cyan arrow gizmo originating from your GameObject. This arrow represents the direction of safety. An AI at this spot is considered "in cover" when the threat is behind them (and the arrow points away from the wall/cover).
3. Adjust the Cover Direction vector in the Inspector, or simply rotate the GameObject itself, to orient the cover correctly. The arrow should point away from the physical object that provides cover.

## Parameters

*  **coverDirection (Vector3):** This vector defines the direction an agent should be facing to be considered "in cover." It's visualized by the cyan arrow in the editor. The DirectionalCoverNodeProviderSO uses this to check if the node is a valid hiding spot from the current threat.

## Best Practices

*  **Placement:** Position the CoverNode slightly away from the wall or object providing cover. This ensures the NavMesh Agent has enough space to stand without clipping into the geometry.
*  **Use with Directional Provider:** For the best results, use the DirectionalCoverNodeProviderSO in your HidingSettings. This provider will intelligently filter the nodes, selecting only those whose coverDirection is pointing away from the player, resulting in much more believable AI behavior.