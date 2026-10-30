# 8. Scene and Assets

These specific tools help developers visualize and manage the complex relationship between project files, internal prefabs, active scenes, and window directories.

### `[Asset3DPreview]`
Renders a deeply interactive 3D preview of the assigned asset structure (Mesh, Prefab, ParticleSystem, VFX, Material) directly in the Inspector above the field label! 
Supports orbit dragging, zooming, animation playback, lighting simulation, distance fog, gradient backgrounds, wireframe toggles, and a fully constructed toolbar panel.

### `[SceneReference]`
Provides a safer, cleaner workflow than directly dragging Unity `SceneAssets`. Natively extracts the final built-index and paths, guaranteeing build-safety.

### `[ManageableAsset]`
A global script. Place this attribute on a standalone `ScriptableObject` class definition to natively register it with the bespoke 'Modular Asset Manager Window'. 
The Asset Manager automatically discovers, catalogues, and explicitly allows fast, beautiful CRUD operations on all project assets of this specific type simultaneously.

### `[AssetSelector]`
Renders a custom mini-window overlay, overriding standard object field circles to visually select project-specific objects utilizing thumbnail injections and deep sorting. 

### `[AssetOnly]` / `[SceneObjectOnly]`
Guarantees drag-and-drop reference locations, preventing developers from assigning local hierarchy objects to global project-wide script configurations securely.

### `[TypeFilter(System.Type type)]`
Restricts object assignment (e.g., `GameObject`, `ScriptableObject`, or `Component` fields) down to a strict `System.Type` or `interface` contract. Prevents incorrect assignment and enhances inspector validation.

### `[CreateAsset]`
Adds a convenient, stylized UI button inside an empty reference slot that dynamically boots generic `ScriptableObject` generation logic based on the strongly typed attribute requirements, instantly saving the file, updating the database, and mapping the newly-minted component back into the empty reference slot correctly.

### `[SceneQuery]`
Automatically searches the Scene or Hierarchy recursively to locate missing references or validate dependency injections when standard attributes fail, leveraging tag dictionaries and deep recursive type lookups on-demand inside the Unity Editor pipeline!

### `[DropableArea]`
Creates a visually distinct, customizable drag-and-drop target in the inspector. Ideal for quickly appending items to lists or making it easier to drag objects into a single explicit field. 
Supports rich customization of background colors, hover state colors, border radiuses, and icon injections.
Can enforce strict drop requirements via `AcceptedTypes` or `AllowSceneObjects` limits. Includes support for dynamic `OnDropCallback` method invocations when items are successfully dropped!
