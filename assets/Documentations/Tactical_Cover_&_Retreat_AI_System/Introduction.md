# Introduction to the Tactical Cover & Retreat AI System

Welcome to the Tactical Cover & Retreat AI System for Unity! This asset is a powerful and highly customizable solution for creating intelligent and dynamic stealth AI. It provides a robust framework for finding and evaluating hiding spots, allowing your AI to make smart decisions based on the current tactical situation.

At its core, the system is designed as a **data-driven state machine helper**. You, the developer, remain in full control of your AI's logic (e.g., in your Behavior Trees or FSMs). This asset provides the tools to answer the crucial question: "Where is the best place to hide right now?"

## Core Design Philosophy

*   **You Are in Control**: The system does not take over your AI. It acts as a service. You call it when you need it, and it returns the best hiding spot based on your configuration.
*   **Component-Based Facade**: The primary entry point is the `EnemyHider` MonoBehaviour. You attach this to your AI, configure it, and call its public API (like `RetreatToHide()`) from your own scripts.
*   **Data-Driven Behavior**: AI behavior is defined not in code, but in `HidingSettings` ScriptableObjects. By mixing and matching different **Providers** and **Scorers**, you can create unique AI personalities without writing a single line of new code.

## Key Concepts

*   **`EnemyHider`**: The main MonoBehaviour you add to your AI. It acts as the "brain" and the primary interface to the whole system.
*   **`HidingSettings`**: A ScriptableObject asset that holds the rules for hiding. This is where you define *what* makes a good hiding spot.
*   **Providers**: ScriptableObjects that generate a list of potential hiding spots. For example, a provider might find all dark areas or all locations behind obstacles.
*   **Scorers**: ScriptableObjects that evaluate the hiding spots found by the providers. Each scorer assigns a score based on a specific criterion, such as distance from the player, visibility, or path safety.
*  **Environmental Helpers:** `(Optional but very powerful)` Components you add to your scene to provide more tactical information to the AI. This includes CoverNode (manual cover spots), Hazard (danger zones), TacticalZone (strategic areas), and VolumetricCover (soft cover like smoke).
*   **`ICombatAction`**: An interface that allows you to write your own custom logic for what to do *after* a hiding spot has been found, such as peeking around cover or firing a weapon.

This documentation will guide you through setting up the system, explain what each component does, and provide recipes for common use cases. Let's get started!