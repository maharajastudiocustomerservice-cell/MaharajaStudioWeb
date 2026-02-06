# Provider: Vantage Point

**`VantagePointProviderSO`** is designed to find positions that offer a height advantage, such as balconies, rooftops, or hilltops. It is essential for "Hunting" behaviors where the AI wants to acquire targets from a superior position.

## How It Works

This provider searches for NavMesh positions that are significantly higher than the agent's current location.

1.  **Biased Sampling:** It generates random search points but specifically biases the Y-coordinate upwards by adding a random value between `Min Height Advantage` and half the range.
2.  **Height Check:** It samples the NavMesh at these elevated coordinates. If a valid point is found, it verifies that the point's Y-position is indeed higher than the agent's current Y-position by the required amount.
3.  **View Check:** To ensure the high ground is actually useful (and not just a high shelf inside a closet), it casts a ray forward/down from the point. If the ray hits nothing for a short distance, it assumes the point has a clear view overlooking an area.

## Parameters

* **Min Height Advantage**: The minimum height difference required above the agent's current Y position for a point to be considered a vantage point.

## Use Cases

* **Snipers**: AI snipers will naturally seek out rooftops or towers using this provider.
* **Ambushers**: Melee units might wait on a ledge to drop down on the player.
* **Scouting**: A squad leader might move to high ground to get a better view of the battlefield.

## Performance

**Good.** It uses standard NavMesh sampling with a simple height check and one raycast per candidate. It is efficient enough for general use.