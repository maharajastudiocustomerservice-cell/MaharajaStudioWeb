# Welcome to the Tactical AI Hiding System!

This asset is a powerful, flexible, and performance-oriented framework for creating intelligent stealth and cover-based AI. It's built on a simple philosophy: **You are in control.**

Instead of a black box that takes over your characters, this system acts as an intelligent service. Your AI's brain (like a Behavior Tree or State Machine) asks the question, *"Where is the best place to hide right now?"*, and this system provides the answer.

### Core Features

*   **Data-Driven AI Personality**: Define complex behaviors not in code, but in ScriptableObjects. Create cautious snipers, aggressive flankers, and sneaky assassins simply by mixing and matching components.
*   **High Performance by Design**: The asynchronous, multithreaded core uses Unity's Job System and Burst Compiler to run complex calculations on background threads, leaving your main thread free for smooth gameplay.
*   **Extensible & Customizable**: Don't like how the AI evaluates cover? Write your own custom Scorer. Need the AI to recognize a unique type of cover in your game? Write your own custom Provider.
*   **Environment-Aware**: Use optional helper components to tag your scene with tactical information. Designate cover nodes, danger zones (`Hazards`), strategic areas (`TacticalZones`), and even soft cover like smoke (`VolumetricCover`).
*   **Dynamic Behavior**: Use the `SearchProfile` API to change an AI's "mood" or tactics on the fly in response to game events like taking damage or receiving a squad command.

### Key Concepts at a Glance

*   **`EnemyHider`**: The main MonoBehaviour component you add to your AI. It's the central brain.
*   **`HidingSettings`**: A ScriptableObject that acts as the AI's "Rulebook" or "Personality," defining how it thinks.
*   **Providers**: ScriptableObjects that **find** potential hiding spots (e.g., "look behind obstacles").
*   **Scorers**: ScriptableObjects that **rate** those spots (e.g., "spots far from the player are better").

Ready to begin? Let's get your first AI hiding in under 10 minutes.

**➡️ Next: [Getting Started Guide](2-Getting-Started.md)**


