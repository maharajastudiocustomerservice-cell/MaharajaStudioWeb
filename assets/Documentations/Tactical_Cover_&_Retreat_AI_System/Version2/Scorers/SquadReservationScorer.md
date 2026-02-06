# Scorer: Squad Reservation

**`SquadReservationScorerSO`** is a critical coordination scorer that prevents multiple agents from trying to claim the exact same hiding spot. It acts as the bridge between the individual agent's search and the central `SquadCoordinator`.

## How It Works

This is a **Binary Disqualifier**. It does not output a gradient score; it either accepts a spot or strictly forbids it.

1.  **Check Coordinator:** It first verifies that a `SquadCoordinator` is assigned and accessible.
2.  **Query Reservation:** It asks the coordinator: *"Is this specific position already reserved by someone else in my squad?"*.
3.  **Result:**
    * **Negative Infinity:** If the spot is reserved, it returns `float.NegativeInfinity`. This creates an immediate "Veto," ensuring this spot is removed from the candidate list regardless of how good its other scores are.
    * **1.0:** If the spot is free, it returns a passing score.

## Parameters

* *None.* This scorer relies entirely on the external logic of the `SquadCoordinator` system.

## Use Cases

* **Stacking Prevention**: Essential for any game with multiple AI agents. Without this, the "best" cover point (e.g., the only concrete wall) would attract every single AI unit, causing them to clip inside each other.

## Performance and Dependencies

* **Thread Safety:** **Main Thread Only**. This scorer is **not** Burst compatible because it must access the `SquadCoordinator` class (a standard C# class) to check dynamic dictionaries and lists.
* **Requirement:** The `HidingContext` must have a valid reference to `squadCoordinator` and `requestingAgent`.