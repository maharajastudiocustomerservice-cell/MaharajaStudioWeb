# Scorer: Height Difference

`HeightDifferenceScorerSO` scores a candidate based on its vertical distance from the agent, discouraging movement to different floors or extreme heights unless the spot is significantly better in other ways.

## How It Works

This scorer introduces a preference for the AI to stay on its current vertical plane. It calculates the absolute difference in the `Y-axis` value between the agent's current position and the candidate spot's position.
The scoring is inversely proportional to this height difference:
A spot on the same level (height difference is zero) receives a perfect score of 1.0.
As the vertical distance increases, the score decreases linearly.
If the height difference exceeds the maxAcceptableHeightDifference, the score becomes 0.0.
This acts as a penalty for vertical movement, meaning a spot on another floor must be significantly better in other aspects (like visibility, safety, etc.) to overcome this penalty and be chosen.

## Parameters

*  **Max Acceptable Height Difference:** The maximum vertical distance the AI will consider before the score drops to zero. This should typically be set to a value slightly greater than the height of a single floor in your level (e.g., 4-5 meters).

## Use Cases

*  **Controlling Vertical Movement:** Its primary use is to prevent AI from erratically running up and down stairs or jumping off ledges just because a spot is slightly better. It promotes more deliberate and logical movement.
*  **Improving Performance:** By penalizing distant vertical spots, it can indirectly favor closer, more relevant hiding locations, potentially reducing the need for long and complex pathfinding calculations.
*  **Defining Agent Behavior:** You could give different AI types different settings. A nimble, spider-like robot might have a high maxAcceptableHeightDifference, while a heavy ground soldier would have a very low one.

## Performance
This scorer is extremely fast. It only involves a few floating-point subtractions and divisions (Mathf.Abs). Its performance impact is virtually zero, making it a safe and effective scorer to add to any configuration.