# Scorer: Casualty Aversion

**`CasualtyAversionScorerSO`** is a high-level survival scorer that allows the AI to "learn" from the battlefield. It penalizes hiding spots that are near locations where allies have recently died, simulating the realization that an area is "zeroed-in" or compromised.

## How It Works

This scorer acts as a dynamic "Fear Map" generator.

1.  **Fetch Data:** It retrieves a list of recent death locations from the global `CasualtyRegistry`.
2.  **Distance Check:** For every candidate spot, it checks the distance to the nearest known casualty.
3.  **Score:**
    * **1.0 (Safe):** If the spot is outside the `Fear Radius` of all dead bodies.
    * **Gradient Penalty:** If the spot is inside the radius, the score drops linearly.
    * **0.0 (Dangerous):** If the spot is exactly where an ally died.

## Parameters

* **Fear Radius**: The radius (in meters) around a corpse that is considered "cursed" or dangerous.

## Use Cases

* **Anti-Lemming Behavior**: Prevents a line of AI agents from running to the exact same cover point one by one and getting shot by the same sniper.
* **Dynamic Flanking**: As direct approaches become littered with casualties, the "negative score" pushes the AI naturally toward flanking routes that haven't been tried yet.

## Performance and Dependencies

* **Thread Safety:** **Main Thread Only**. Accesses the `CasualtyRegistry`.
* **Cost:** Low. Uses simple distance-squared checks against a usually small list of recent deaths.