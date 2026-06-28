# Script Event FX Node

The **Script Event FX Node** triggers custom code callbacks, invokes scripting methods, or broadcasts messages at specific timeline points. This allows you to integrate custom game logic (such as deducting player mana on a spellcast frame, calling a custom combat script, or toggling collision scripts on a weapon collider).

---

## Inspector Parameter Reference

Configure the Script Event properties in the details panel:

### Event Tag & Target Context

* **Script Event Tag**: A string identifier representing this event type. Your game logic scripts can listen for this specific tag to execute custom code when the event fires.
* **Context Target Mode**: Defines which GameObject receives the scripting callback:
  * **Root**: Sends the event to the character's root GameObject.
  * **Custom Bone**: Sends the event to a specific socket bone.
* **Custom Context Human Bone**: If **Context Target Mode** is set to custom bone, selects a standard Humanoid bone target.
* **Custom Context Bone Name**: Manual bone path input if the character is non-humanoid.

### Parameter Payloads

* **Parameters**: A list of key-value parameters passed along with the script trigger. You can add, delete, and define arguments directly on the timeline:
  * **Key**: The name of the parameter variable (e.g. `DamageAmount` or `IsCritical`).
  * **Type**: The variable type (**String**, **Int**, **Float**, **Bool**).
  * **Value**: The value passed to the receiving script.

### Method Invocation (Unity SendMessage)

You can invoke specific component methods directly:
* **Use SendMessage**: If checked, utilizes Unity's standard `SendMessage` API to invoke a function.
* **SendMessage Method**: Enter the exact name of the C# function/method to execute (e.g., `OnSpellCast` or `TriggerVisualExplosion`). The runtime will look for any active script component containing this method name on the target context GameObject and execute it.
