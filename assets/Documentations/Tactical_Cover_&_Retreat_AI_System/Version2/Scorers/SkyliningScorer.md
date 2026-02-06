# Scorer: Skylining (Silhouette)

**`SkyliningScorerSO`** is a visual camouflage scorer. It detects "Skylining"—a tactical error where a soldier stands on a ridge or roof and is silhouetted against the bright sky, making them an easy target.

## How It Works

This scorer checks the *background* of the candidate spot from the enemy's perspective.

1.  **Reverse Raycast:** It calculates the direction from the Enemy -> Candidate Spot.
2.  **Background Check:** It casts a ray starting *from* the candidate spot and continuing along that direction (away from the enemy).
3.  **Analyze Hit:**
    * **Hit:** If the ray hits geometry (a wall, a mountain, a tree), it means the agent has a "Backstop." They will blend in with the background. (Score 1.0).
    * **No Hit:** If the ray hits nothing, it means the background is the Skybox. The agent is skylined. (Score = `Skylining Penalty`).

## Parameters

* **Background Check Distance**: How far behind the agent to check for geometry (e.g., 20m).
* **Skylining Penalty**: The score received if skylined (0.0 = Reject, 1.0 = Ignore).

## Use Cases

* **Ridge Safety**: Prevents AI from standing on the very top of a hill; encourages them to move slightly down the reverse slope (Military Crest).
* **Rooftops**: AI will avoid standing on the very edge of a roof where they stick out against the sky.

## Performance and Dependencies

* **Thread Safety:** **Main Thread Only**. Uses Physics Raycasts.
* **Cost:** Moderate. One raycast per candidate.