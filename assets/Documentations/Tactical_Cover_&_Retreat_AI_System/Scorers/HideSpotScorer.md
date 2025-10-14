# Scorer: Hide Spot Scorer (Base Class)

`HideSpotScorerSO` is not a functional scorer itself. It is an abstract base class that serves as the template for all other scorer assets.

## How It Works

The `Hiding System's` evaluation process is modular. It doesn't use a single, hard-coded method for judging hiding spots. Instead, it uses a list of specialized "scorers." Each scorer is a ScriptableObject that implements one specific way of evaluating a candidate spot and returning a numerical score.
The HideSpotScorerSO class defines the contract that every scorer must follow. It contains a single abstract method:
`public abstract float Score(in HidingContext ctx, in CandidateInfo candidate);`

*  **HidingContext ctx:** A struct containing all the information the scorer might need, such as player locations, the agent's own position, system settings, etc.
*  **CandidateInfo candidate:** The potential hiding spot being evaluated.
return float: The scorer must return a floating-point number. By convention, higher scores are better. A score of float.NegativeInfinity will instantly disqualify the candidate. Scores are typically normalized between 0.0 and 1.0.
By inheriting from this class, you can create your own custom logic for evaluating cover, which will then be seamlessly integrated into the main system by adding it to the Scorers list in your HidingSettingsSO.

## Setup

`To create a new, custom scorer:`
`Create a new C# script.`
`Make the class inherit from HideSpotScorerSO.`
`Add the [CreateAssetMenu] attribute to allow you to create instances of it in the Unity Editor.`
`Implement the Score method with your custom logic.`
`Create an instance of your new scorer asset via the Assets -> Create menu.`
`Drag your new scorer asset into the Scorers list in your HidingSettingsSO and assign it a weight.`

## Use Cases

System Extensibility: The primary purpose is to allow developers to easily extend the AI's decision-making logic without altering the core system code.
Project-Specific AI Behavior: You can create scorers tailored to your game's unique mechanics. For example:
* A scorer that prefers spots near health packs.
* A scorer that avoids areas with hazardous materials.
* A scorer that gives a bonus to spots with a view of a mission objective.

## Performance

As a base class, it has no performance impact. The performance of any given scorer is entirely dependent on the complexity of the logic implemented within its Score method.