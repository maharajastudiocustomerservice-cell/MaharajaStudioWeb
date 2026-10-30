# [StaggerCascade]

> Animates fields or list items cascading into view sequentially with an automatic staggered delay and cubic ease-out slide-in motion.

`Package: MSUltimate-AnimatedAttributes` `Targets: Field | Property` `AllowMultiple: False` `Inherited: True` `Performance: High (Hardware-Accelerated UI Toolkit Transforms)`

---

## 1. Overview & Value Proposition

**What it does:**
`[StaggerCascade]` introduces choreographed arrival motion to inspector fields, tabs, or expanded list items. When a decorated element mounts to the panel (via initial display or parent foldout expansion), its initial opacity is set to zero (`opacity = 0`) and offset downward by a configurable pixel delta (`SlideOffset`, defaulting to 20px). Using an incremental element counter, each successive field or collection element row is assigned a progressive delay (`index * CascadeDelay`), then transitions smoothly into place using a hardware-accelerated cubic ease-out curve ($t = 1 - (1 - \text{progress})^3$) over `ItemDuration` (defaulting to 300ms).

**The Problem:**
When opening foldouts, switching tab groups, or expanding collection lists, dense inspectors instantly flood the screen with dozens of controls simultaneously. This visual pop lacks organic pacing, feels rigid, and makes it harder for designers to parse complex configuration screens.

**The Solution:**
Decorating sequential fields or collections with `[StaggerCascade]`:
- **Choreographed Domino Wave:** Progressively reveals fields or collection items one after another using automated sequential index calculations.
- **Collection Element Cascading:** Implements `ICollectionElementAttribute` so array and list items cascade gracefully into view in a staggered waterfall sequence.
- **Natural Cubic Ease-Out:** Employs a physics-like decelerating trajectory ($t = 1 - (1 - p)^3$) that slides upward smoothly to rest.
- **Adjustable Spatial Offset:** Configurable slide distance (`SlideOffset`) allowing subtle 10px slips or dramatic 40px stage entrances.
- **Zero Ongoing Overhead:** The internal UI Toolkit scheduler automatically shuts down as soon as each individual item reaches 100% progress (`progress >= 1f`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class SkillTreeConfig : MonoBehaviour
{
    [StaggerCascade(cascadeDelay: 50f, slideOffset: 25f)]
    public string primarySkillName = "Meteor Shower";

    [StaggerCascade(cascadeDelay: 50f, slideOffset: 25f)]
    public float baseDamage = 120f;

    [StaggerCascade(cascadeDelay: 50f, slideOffset: 25f)]
    public float manaCost = 45f;
}
```

---

## 3. Constructors & Parameters

```csharp
public StaggerCascadeAttribute(float cascadeDelay = 40f, float slideOffset = 20f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `cascadeDelay` | `float` | `40f` | Delay in milliseconds added per sequential item index. |
| `slideOffset` | `float` | `20f` | Vertical pixel offset from which the element slides up into place. |

---

## 4. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `CascadeDelay` | `float` | `40f` | Delay in milliseconds applied incrementally per item index. |
| `SlideOffset` | `float` | `20f` | Initial downward pixel offset prior to sliding in. |
| `ItemDuration` | `float` | `300f` | Duration in milliseconds for each item to fade and slide in. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 5. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

namespace MaharajaStudio.MSUltimate.AnimatedAttributes.Sample
{
    public class StaggerCascadeExample : ModularMonoBehaviour
    {
        [Title("StaggerCascade Attribute Showcase", "Sequential staggered cascade animation")]
        [InfoBox("StaggerCascade calculates automatic incremental delays for consecutive fields or list entries, producing an elegant cascading waterfall entrance.", InspectorMessageType.Info)]

        [BoxGroup("1. Standalone Staggered Cascade Group")]
        [StaggerCascade(cascadeDelay: 40f, slideOffset: 20f, ItemDuration = 300f)]
        public int heroCombatPowerRating = 18450;

        [StaggerCascade(cascadeDelay: 80f, slideOffset: 20f, ItemDuration = 300f)]
        public string elementalAffinity = "Radiant Celestial Holy Fire";

        [StaggerCascade(cascadeDelay: 120f, slideOffset: 20f, ItemDuration = 300f)]
        public float maxManaCapacity = 2400f;

        [BoxGroup("2. Inside Class Demonstration")]
        public TalentTreeNode primaryTalent = new TalentTreeNode();

        [BoxGroup("3. Cascade Skill Bar Manifest")]
        [InfoBox("StaggerCascade cascades to collection elements, giving each entry an index-based staggered delay.", InspectorMessageType.Info)]
        [StaggerCascade(cascadeDelay: 40f, slideOffset: 15f)]
        public int[] hotbarAbilityIds = new int[] { 101, 102, 103, 104, 105 };

        public List<TalentTreeNode> activeTalentBuild = new List<TalentTreeNode>
        {
            new TalentTreeNode { branchName = "Pyromancy Mastery", pointsSpent = 25 },
            new TalentTreeNode { branchName = "Cryomancy Barrier", pointsSpent = 15 },
            new TalentTreeNode { branchName = "Chronomancy Haste", pointsSpent = 40 }
        };

        [Serializable]
        public class TalentTreeNode
        {
            public string branchName = "Ascendant Archmage";

            [StaggerCascade(cascadeDelay: 50f, slideOffset: 15f)]
            public int pointsSpent = 35;
        }

        [BoxGroup("4. Staggered Cascade Controls")]
        [Button("Allocate +5 Talent Points Across Build", BackgroundColor = "#38BDF8", TextColor = "#082F49")]
        public void AllocatePoints()
        {
            heroCombatPowerRating += 500;
            primaryTalent.pointsSpent += 5;
            for (int i = 0; i < activeTalentBuild.Count; i++)
            {
                activeTalentBuild[i].pointsSpent += 2;
            }
            Debug.Log($"<color=#38BDF8>[StaggerCascade]</color> Points allocated! Hero Power Rating: {heroCombatPowerRating}.");
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` / `[TabGroup]` | Supported | Excellent pairing; triggers a cascading domino reveal when the parent tab or foldout is opened. |
| `[ShowIf]` / `[EnableIf]` | Supported | Animates gracefully when the field transitions from hidden to revealed state. |
| `[ElasticPopIn]` | Avoid | Both alter `translate`/`scale` simultaneously during mounting; choose either elastic pop-in or cascade slide. |
| Validation Attributes | Supported | Fully compatible with `[Required]`, `[Range]`, and `[NotNull]`. |

---

## 7. Collection Cascading & Custom Serializer Discipline

| Context / Architecture | Support | Behavior & Guidelines |
| :--- | :---: | :--- |
| **Collection Element Cascading** | Supported (`ICollectionElementAttribute`) | Cascades down to individual collection rows (`int[]`, `string[]`, `List<T>`), staggering each row's entrance animation by `index * CascadeDelay`. |
| **Target Element Roles** | Supported | `CollectionElementRole.Element`, `Value`, `NullableValue`, `TupleItem`. |
| **Direct Collections** | Supported | Operates on direct primitive arrays (`int[]`, `float[]`), object lists, and enum arrays. |
| **Nested Serializable Classes** | Supported | Fully animates fields inside child items and structs declared within lists. |
| **Custom Serializers** | Supported | Seamlessly integrates with `AdvancedList<T>`, `SerializableDictionary<K, V>`, and `SerializableTuple<...>`. |
