# Scorer: Aggressive Line of Sight

**`AggressiveLOSScorerSO`** is an offensive scorer designed for units that need to engage the enemy. Unlike standard hiding scorers that punish visibility, this scorer strictly rewards spots that have a clear line of fire to the target.

## How It Works

This scorer performs a raycast to determine if a shot is possible from the candidate position.

1.  **Target Acquisition:** It identifies the target position using the AI's memory (`playerLastKnownPosition`). If no memory exists, it defaults to the current position of the first available player.
2.  **Origin & Aim Point:** * **Origin:** The ray starts at the candidate position raised by the `enemyEyeHeight`.
    * **Aim Point:** The ray aims at the target's position. Depending on the settings, it aims either at the **Head** (full eye height) or the **Center Mass** (half eye height).
3.  **Raycast Check:** It casts a physics ray using the `OccluderMask` defined in the settings.
    * **Clear Path:** If the ray hits nothing, the path is clear. The scorer returns **1.0**.
    * **Blocked:** If the ray hits an obstacle, the scorer returns **0.0**.

This binary scoring (All or Nothing) ensures that "Attacker" roles strictly filter out spots where they would be staring at a wall.

## Parameters

* **Require Head Visibility**: 
    * **True**: The AI checks for line of sight specifically to the target's head (at `playerEyeHeight`). Useful for Snipers or units that need a perfect shot.
    * **False**: The AI checks for line of sight to the target's center/chest. Useful for general infantry or units with splash damage.

## Use Cases

* **Snipers / Turrets**: Use this with a high weight to ensure the AI only picks spots where it can shoot the player immediately.
* **"Stand and Fight"**: Use this on a profile where the AI decides to stop retreating and start engaging.
* **Support Units**: Ensures machine gunners move to positions where they can suppress the enemy.

## Performance

**Moderate.** This scorer performs one `Physics.Raycast` for every candidate spot generated. While not overly expensive, it is heavier than simple distance checks.