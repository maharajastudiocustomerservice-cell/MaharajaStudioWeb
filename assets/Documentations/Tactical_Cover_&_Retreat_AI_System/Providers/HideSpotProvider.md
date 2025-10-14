# Provider: Hide Spot Provider (Base Class)
HideSpotProviderSO is not a functional provider itself. It is an abstract base class that serves as the template for all other provider assets.

## How It Works
The Hiding System is designed to be modular. Instead of having a single, monolithic way of finding hiding spots, it uses a collection of smaller, specialized `"providers."` Each provider is a ScriptableObject that knows one specific way to generate a list of potential hiding spots (candidates).

`The HideSpotProviderSO class defines the contract that every provider must follow. It contains a single abstract method:`
`public abstract void GenerateCandidates(in HidingContext ctx, List<CandidateInfo> results);`
*  **HidingContext ctx:** A struct containing all the information the provider might need, such as the agent's position, player locations, and system settings.
*  **List<CandidateInfo> results:** The list that the provider must add its generated candidate spots to.
By inheriting from this class, you can create your own custom logic for finding cover, which will seamlessly plug into the main hiding system alongside the built-in providers.

## Setup
`To create a new, custom provider:`
`Create a new C# script.`
`Make the class inherit from HideSpotProviderSO.`
Add the [CreateAssetMenu] attribute to allow you to create instances of it in the Unity Editor.
Implement the GenerateCandidates method with your custom logic for finding spots.
Create an instance of your new provider asset via the `Assets -> Create menu.`
Drag your new provider asset into the Providers array in your HidingSettingsSO.

## Use Cases
*  **System Extensibility:** The primary use is to allow developers to extend the hiding system with novel techniques for finding cover without modifying the core system code.
*  **Project-Specific Logic:** You can create providers tailored to the unique mechanics of your game. For example, a provider that finds hiding spots in magical portals, under brush, or in areas designated by a special trigger volume.

## Performance
As a base class, it has no performance impact. The performance of a provider is entirely dependent on the logic implemented in its GenerateCandidates method.