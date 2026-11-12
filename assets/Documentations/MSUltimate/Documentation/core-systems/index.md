# Core Systems Architecture

> Technical overview of MSUltimate's drawer discovery database, UI Toolkit rendering pipeline, custom collection serializers, extended types, modular windowing, and global settings.

---

## Systems Overview
- **Drawer Discovery & Reflection Caching:** Domain-reload `TypeCache` discovery via `DrawerDatabase` pairing `ModularAttribute` types to `BaseDrawer` / `ModularDrawer<T>` implementations.
- **Drawer Stacking & Layout Pipeline:** Execution order combining layout groups (`BoxGroup`, `HorizontalGroup`, `BeginTabGroup`, `BeginSplitPane`), conditionals (`ShowIf`, `EnableIf`, `ConditionExpressionEngine`), decorators, and value drawers in `ModularMonoBehaviourEditor`.
- **Custom Serializers & Extended Types:** `ISerializationCallbackReceiver` collections (`SerializableDictionary<TKey, TValue>`, `SerializableHashSet<T>`, `SerializableMatrix2D<T>`, `SerializableMatrix3D<T>`, `SerializableQueue<T>`, `SerializableStack<T>`) and extended types (`SerializableDateTime`, `SerializableNullable<T>`, `SerializableRange<T>`, `SerializableTuple<T1, T2>`, `SerializableTuple<T1, T2, T3>`, `SerializableType`).
- **Modular Windowing System:** `[ModularWindow]`, `[ShowInWindow]`, `ModularEditorWindow`, `ModularMenuEditorWindow`, `ModularMenuTree`, `ModularModalWindow`, and `ModularAssetManagerWindow`.
- **Preferences, Defaults & Setup:** Global responsive label/layout defaults (`MSUltimateLayoutSettings`), global component defaults/ignore rules (`MSUltimateComponentDefaultsSettings`), and zero-inheritance type baking (`MSUltimateSetupWizard` / `MSUltimateTypeBaker`).
