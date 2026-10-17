# Technical Architecture

This document provides a technical overview of the Tactical Cover & Retreat AI System's architecture. It is intended for developers who want to understand how the system works internally or wish to extend it with custom logic.

## Core Architecture: The Facade Pattern

The system is designed around the **Facade** pattern. The `EnemyHider` MonoBehaviour acts as a simple, high-level interface (a "facade") that conceals the more complex underlying logic. This provides a clean separation of concerns:

1.  **The User (You)**: Interacts exclusively with the `EnemyHider` component. You are responsible for deciding *when* the AI should hide and calling the public API (e.g., `hider.RetreatToHide()`).
2.  **The Facade (`EnemyHider`)**: Manages the state for a single AI (e.g., its target list, settings asset, cancellation tokens). When one of its methods is called, it gathers all the necessary data into a `HidingContext` object.
3.  **The Core Logic (`Async/SynchronousHidingSystemCore`)**: These are static classes that contain the pure, stateless logic for finding a hiding spot. They take the `HidingContext`, run the providers and scorers, and return the result. They have no knowledge of GameObjects or scenes.

This design makes the system robust, predictable, and easy to integrate into any existing AI framework, such as a Behavior Tree or a Finite State Machine.

## Data Flow

The data flows in a clear sequence when you call `RetreatToHide()`:

1.  **`EnemyHider`** assembles the `HidingContext`. This is a struct that packages up all the necessary data for the search: the agent's position, the player list, the ally list, the `HidingSettingsSO`, visibility services, etc.
2.  The context is passed to the appropriate static core method (`SynchronousHidingSystemCore.TryFindBestSpot` or `AsyncHidingSystemCore.FindBestSpotAsync`).
3.  **Inside the Core**:
    a. The `Core` iterates through the list of **Providers** from the `HidingSettingsSO`, calling `GenerateCandidates()` on each. All returned points are aggregated into a single master list.
    b. For each point in the master list, the `Core` iterates through the list of **Scorers**.
    c. Each `Scorer` evaluates the spot by calling its `Score()` method. The returned score is multiplied by its corresponding **weight** from the `HidingSettingsSO` and added to a total score for that spot.
    d. A scorer returning `float.NegativeInfinity` immediately disqualifies a candidate.
4.  The spot with the highest final score is selected.
5.  The `Core` returns the best spot (or a failure state) back to the `EnemyHider`.
6.  **`EnemyHider`** receives the result. If successful, it invokes the `OnSearchSuccess` event and either moves the NavMeshAgent itself or passes the result to a custom `ICombatAction` handler. If failed, it invokes `OnSearchFailed`.

## Extensibility: The `ICombatAction` Interface

A key point of extension is the **`ICombatAction`** interface. By default, after finding a spot, `EnemyHider` will simply move the NavMeshAgent to the destination. However, you can provide your own implementation of `ICombatAction` to define custom behavior.

This allows you to create more sophisticated actions, such as:

*   Moving to the spot and then peeking around cover.
*   Moving to the spot and entering a special "suppressive fire" animation.
*   Moving to the spot and throwing a grenade at the player's last known position.

**To use it:**
1.  Create a new C# script that implements the `ICombatAction` interface.
2.  Implement the `Execute(HidingSpot spot, Vector3? lastKnownPlayerPosition)` method with your custom logic.
3.  Attach this script to a GameObject and assign that GameObject to the `Combat Action Game Object` field on the `EnemyHider` component.

The `EnemyHider` will automatically detect this component and call your `Execute` method instead of its own default `MoveToSpot` logic.