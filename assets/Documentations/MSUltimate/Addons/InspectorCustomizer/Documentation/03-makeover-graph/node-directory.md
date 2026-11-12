# Makeover Graph 30-Node Reference Directory

> **Module:** MSUltimate Inspector Customizer — Makeover Graph  
> **Topic:** Exhaustive Reference Manual for All 30 Node Archetypes, Ports, and Execution Rules

---

## 1. Node Archetype Index

The Makeover Graph execution engine provides 30 specialized node types classified into 7 functional domains:

```
Makeover Graph Taxonomy (30 Nodes)
├── 1. Core & Terminals (4)        ──► SimpleRule, Output, MacroInput, MacroOutput
├── 2. Conditions & Filters (7)    ──► ConditionScope, ConditionType, ConditionName, ConditionAttribute,
│                                      ConditionAccess, ConditionValueCompare, ConditionInterfaceOrGeneric
├── 3. Logic & Flow Control (4)    ──► LogicGate, ValueBranch, MemberPriority, Reroute
├── 4. Emitters & Layout Actions (4)─► AttributeEmitter, AttributeReplacer, GroupWrapper, ApplyRecipe
├── 5. Relational Queries (2)      ──► QuerySiblingField, RegexExtractor
├── 6. Math & Data Processing (7)  ──► ValueExtractor, TypeConverter, ConstantValue, MathOperation,
│                                      ColorToHex, RangeRemap, StringFormatter
└── 7. Variables & Subgraphs (2)   ──► BlackboardProperty, Macro
```

---

## 2. Category 1: Core & Terminals

### 2.1 `SimpleRule`
- **Enum Type:** `MakeoverNodeType.SimpleRule`
- **Purpose:** A compound 1-click rule node encapsulating scope, type matcher, name pattern, and attribute action into a single compact node. Eliminates the need to wire multiple condition gates for standard matching.
- **Ports:**
  - `Scope In` *(Input, Capacity: Single, Type: object)*: Optional incoming member signal.
  - `Execute Out` *(Output, Capacity: Multi, Type: Rule)*: Connects to `Output` or downstream layout nodes.
- **Exposed Parameters:**
  - `Target Scope`: `Any`, `Field`, `Method`, `Class`.
  - `Type Filter`: `Any`, `ExactType`, `Numeric`, `Text`, `Boolean`, `Color`, `Enum`, `SubclassOf`, `ArrayOrList`, `UnityObject`.
  - `Name Match`: `Contains`, `StartsWith`, `EndsWith`, `Wildcard` (e.g. `*health`), `Regex`.
  - `Action`: Attribute to apply and parameter fields.
- **Example Scenario:** Match all fields ending in `Speed` of type `Numeric`, and apply `[Range(0f, 20f)]`.

---

### 2.2 `Output`
- **Enum Type:** `MakeoverNodeType.Output`
- **Purpose:** The mandatory terminal collector of every Makeover Graph. Aggregates all upstream layout rules, resolves conflict priorities, and emits the final layout plan to `InspectorProfile`.
- **Ports:**
  - `Rules In` *(Input, Capacity: Multi, Type: Rule)*: Multi-wire terminal port receiving rules from all emitters.
- **Exposed Parameters:**
  - `Conflict Strategy`: `Skip` (keep existing), `Replace` (override existing), `Duplicate` (add multiple instances).
- **Wiring Rule:** Every valid Makeover Graph must contain exactly one `Output` terminal.

---

### 2.3 `MacroInput`
- **Enum Type:** `MakeoverNodeType.MacroInput`
- **Purpose:** Declares an incoming input boundary pin inside a reusable Subgraph Macro (`.msmakomacro`).
- **Ports:**
  - `Pin Out` *(Output, Capacity: Multi, Type: User-Defined)*: Routes the incoming data to internal macro nodes.
- **Exposed Parameters:**
  - `Pin Name`: The display label of the input port when viewed from the parent graph.
  - `Pin Type`: `Member`, `Float`, `Int`, `String`, `Boolean`, `Color`, `Generic`.

---

### 2.4 `MacroOutput`
- **Enum Type:** `MakeoverNodeType.MacroOutput`
- **Purpose:** Declares an outgoing result boundary pin inside a Subgraph Macro (`.msmakomacro`).
- **Ports:**
  - `Pin In` *(Input, Capacity: Single, Type: User-Defined)*: Receives calculated rule data from internal macro nodes.
- **Exposed Parameters:**
  - `Pin Name`: The display label of the output port on the Macro node in parent graphs.

---

## 3. Category 2: Conditions & Filters

### 2.5 `ConditionScope`
- **Enum Type:** `MakeoverNodeType.ConditionScope`
- **Purpose:** Evaluates whether an inspected member matches a target C# declaration scope.
- **Ports:**
  - `Condition Out` *(Output, Capacity: Multi, Type: bool)*: Emits `true` if member matches scope.
- **Exposed Parameters:**
  - `Scope`: `Any`, `Field`, `Method`, `Class`.
- **Example Scenario:** Restrict downstream attribute emission strictly to methods before applying `[Button]`.

---

### 2.6 `ConditionType`
- **Enum Type:** `MakeoverNodeType.ConditionType`
- **Purpose:** Filters members based on their reflected C# data type.
- **Ports:**
  - `Condition Out` *(Output, Capacity: Multi, Type: bool)*: Emits `true` when data type satisfies filter.
- **Exposed Parameters:**
  - `Type Filter`: `Any`, `ExactType`, `Numeric` (int/float/double), `Text` (string), `Boolean`, `Color`, `Enum`, `SubclassOf`, `ArrayOrList`, `UnityObject`.
  - `Type Argument`: Text input for exact type names (e.g. `UnityEngine.Transform` or `AudioClip`).

---

### 2.7 `ConditionName`
- **Enum Type:** `MakeoverNodeType.ConditionName`
- **Purpose:** Evaluates the member's identifier against substring, wildcard, or regular expression patterns.
- **Ports:**
  - `Condition Out` *(Output, Capacity: Multi, Type: bool)*: Emits `true` on match.
  - `Match String` *(Output, Capacity: Multi, Type: string)*: Emits the matched substring or pattern.
- **Exposed Parameters:**
  - `Match Kind`: `Contains`, `StartsWith`, `EndsWith`, `Wildcard` (e.g. `min*`, `*_data`), `RegexPattern`.
  - `Pattern`: String pattern to match against.

---

### 2.8 `ConditionAttribute`
- **Enum Type:** `MakeoverNodeType.ConditionAttribute`
- **Purpose:** Checks whether a member already possesses or lacks an attribute.
- **Ports:**
  - `Condition Out` *(Output, Capacity: Multi, Type: bool)*: Emits `true` if condition passes.
- **Exposed Parameters:**
  - `Mode`: `HasAttribute` or `LacksAttribute`.
  - `Attribute Type`: Assembly-qualified attribute type name (e.g. `UnityEngine.SerializeField` or `MaharajaStudio.MSUltimate.Runtime.ReadOnlyAttribute`).

---

### 2.9 `ConditionAccess`
- **Enum Type:** `MakeoverNodeType.ConditionAccess`
- **Purpose:** Evaluates access modifiers and serialization state.
- **Ports:**
  - `Condition Out` *(Output, Capacity: Multi, Type: bool)*.
- **Exposed Parameters:**
  - `Access Scope`: `Any`, `Public`, `NonPublicSerialized`, `Protected`, `Property`, `Internal`.
- **Example Scenario:** Match private fields that are serialized (`[SerializeField] private float _stamina;`) to style them with progress bars.

---

### 2.10 `ConditionValueCompare`
- **Enum Type:** `MakeoverNodeType.ConditionValueCompare`
- **Purpose:** Compares the live edit-time or default value of a field against target constants.
- **Ports:**
  - `Value In` *(Input, Capacity: Single, Type: string/numeric)*: Optional value to compare.
  - `Condition Out` *(Output, Capacity: Multi, Type: bool)*.
- **Exposed Parameters:**
  - `Operator`: `Equals`, `NotEquals`, `GreaterThan`, `LessThan`, `GreaterOrEqual`, `LessOrEqual`, `IsNull`, `IsNotNull`.
  - `Target Value`: Target constant string or number (e.g. `0`, `100`, `null`).

---

### 2.11 `ConditionInterfaceOrGeneric`
- **Enum Type:** `MakeoverNodeType.ConditionInterfaceOrGeneric`
- **Purpose:** Evaluates whether a member implements a specific interface or is a generic collection container.
- **Ports:**
  - `Condition Out` *(Output, Capacity: Multi, Type: bool)*.
- **Exposed Parameters:**
  - `Generic Constraint Kind`: `AnyInterface`, `AnyGenericCollection`, `List`, `Dictionary`, `HashSet`, `Array`.
  - `Interface Name`: Interface string (e.g. `IDamageable` or `ISerializable`).

---

## 4. Category 3: Logic & Flow Control

### 2.12 `LogicGate`
- **Enum Type:** `MakeoverNodeType.LogicGate`
- **Purpose:** Combines multiple boolean condition signals into a single output.
- **Ports:**
  - `A` *(Input, Capacity: Single, Type: bool)*.
  - `B` *(Input, Capacity: Single, Type: bool)*.
  - `Result` *(Output, Capacity: Multi, Type: bool)*.
- **Exposed Parameters:**
  - `Operation`: `AND`, `OR`, `NOT` (evaluates `A` only), `XOR`.

---

### 2.13 `ValueBranch`
- **Enum Type:** `MakeoverNodeType.ValueBranch`
- **Purpose:** Ternary signal selector (If-Else routing).
- **Ports:**
  - `Condition In` *(Input, Capacity: Single, Type: bool)*: Evaluation gate.
  - `True In` *(Input, Capacity: Single, Type: object)*: Routed if condition is true.
  - `False In` *(Input, Capacity: Single, Type: object)*: Routed if condition is false.
  - `Selected Out` *(Output, Capacity: Multi, Type: object)*.
- **Example Scenario:** If `hasShield` is true, route `#00AAFF` (Cyan) to progress bar color; else route `#FF4444` (Red).

---

### 2.14 `MemberPriority`
- **Enum Type:** `MakeoverNodeType.MemberPriority`
- **Purpose:** Modifies the visual vertical display priority and sorting order of matched members.
- **Ports:**
  - `Member In` *(Input, Capacity: Single, Type: Member)*.
  - `Member Out` *(Output, Capacity: Multi, Type: Member)*.
- **Exposed Parameters:**
  - `Priority Offset`: Integer sorting weight (e.g. `-100` pushes member to the top of the inspector, `+100` pushes to the bottom).

---

### 2.15 `Reroute`
- **Enum Type:** `MakeoverNodeType.Reroute`
- **Purpose:** Ultra-compact inline wire knot to route connections cleanly around other nodes without canvas clutter.
- **Ports:**
  - `In` *(Input, Capacity: Single, Type: generic)*.
  - `Out` *(Output, Capacity: Multi, Type: generic)*.
- **Special Feature:** Automatically inherits and propagates the exact port data type of connected incoming edges.

---

## 5. Category 4: Emitters & Layout Actions

### 2.16 `AttributeEmitter`
- **Enum Type:** `MakeoverNodeType.AttributeEmitter`
- **Purpose:** Generates any MSUltimate attribute dynamically. Dynamically synthesizes input ports for all reflected parameters of the chosen attribute!
- **Ports:**
  - `Condition In` *(Input, Capacity: Single, Type: bool)*: Controls whether the attribute emits.
  - Dynamic Parameter Ports (e.g. `Min`, `Max`, `Color`, `Label`).
  - `Rule Out` *(Output, Capacity: Multi, Type: Rule)*: Connects to `Output` or group wrappers.
- **Exposed Parameters:**
  - `Attribute Dropdown`: Selection of all 444+ MSUltimate attributes.

---

### 2.17 `AttributeReplacer`
- **Enum Type:** `MakeoverNodeType.AttributeReplacer`
- **Purpose:** Finds an existing legacy attribute on a member and swaps it with an MSUltimate attribute while migrating parameter values.
- **Ports:**
  - `Condition In` *(Input, Capacity: Single, Type: bool)*.
  - `Rule Out` *(Output, Capacity: Multi, Type: Rule)*.
- **Exposed Parameters:**
  - `Source Attribute`: Attribute to find (e.g. `UnityEngine.HeaderAttribute`).
  - `Replacement Attribute`: Attribute to replace with (e.g. `MaharajaStudio.MSUltimate.Runtime.FoldingHeaderAttribute`).
  - `Transfer Matching Values`: Automatically copies string labels and values across.

---

### 2.18 `GroupWrapper`
- **Enum Type:** `MakeoverNodeType.GroupWrapper`
- **Purpose:** Encloses all incoming matched members into an MSUltimate layout grouping container.
- **Ports:**
  - `Rules In` *(Input, Capacity: Multi, Type: Rule)*: Rules to enclose inside the group.
  - `Title In` *(Input, Capacity: Single, Type: string)*: Dynamic title of the group.
  - `Header Color In` *(Input, Capacity: Single, Type: Color)*: Accent color.
  - `Group Out` *(Output, Capacity: Multi, Type: Rule)*: Connects to `Output`.
- **Exposed Parameters:**
  - `Group Archetype`: `BoxGroup`, `BeginTabGroup`, `FoldoutGroup`, `HorizontalGroup`.
  - `Static Group Title`: Fallback title string.

---

### 2.19 `ApplyRecipe`
- **Enum Type:** `MakeoverNodeType.ApplyRecipe`
- **Purpose:** Stamps an entire `InspectorAttributeRecipe` compound bundle onto matched members.
- **Ports:**
  - `Condition In` *(Input, Capacity: Single, Type: bool)*.
  - `Rule Out` *(Output, Capacity: Multi, Type: Rule)*.
- **Exposed Parameters:**
  - `Recipe Asset`: Reference to an `InspectorAttributeRecipe` ScriptableObject.

---

## 6. Category 5: Relational Queries & Extractors

### 2.20 `QuerySiblingField`
- **Enum Type:** `MakeoverNodeType.QuerySiblingField`
- **Purpose:** Relational query engine that searches the declaring class for companion fields matching stem patterns.
- **Ports:**
  - `Member In` *(Input, Capacity: Single, Type: Member)*.
  - `Sibling Found` *(Output, Capacity: Multi, Type: bool)*: True if companion exists.
  - `Sibling Name` *(Output, Capacity: Multi, Type: string)*: Name of matched companion.
  - `Stem Base` *(Output, Capacity: Multi, Type: string)*: Common root name (e.g. `"Speed"` from `"minSpeed"` and `"maxSpeed"`).
- **Exposed Parameters:**
  - `Pairing Stem`: `MinMax` (`min*` $\rightarrow$ `max*`), `StartEnd` (`start*` $\rightarrow$ `end*`), `CurrentMax` (`current*` $\rightarrow$ `max*`), `Dimension` (`width`/`height`).

---

### 2.21 `RegexExtractor`
- **Enum Type:** `MakeoverNodeType.RegexExtractor`
- **Purpose:** Parses member names with regular expression capture groups to generate dynamic labels, group titles, or category tags.
- **Ports:**
  - `Member In` *(Input, Capacity: Single, Type: Member)*.
  - `Is Matched` *(Output, Capacity: Multi, Type: bool)*.
  - `Group 1` *(Output, Capacity: Multi, Type: string)*: Captured group 1.
  - `Group 2` *(Output, Capacity: Multi, Type: string)*: Captured group 2.
- **Exposed Parameters:**
  - `Regex Pattern`: e.g. `^(?<cat>[^_]+)_(?<name>.+)$`.

---

## 7. Category 6: Math & Data Processing

| Node | Type Enum | Input Ports | Output Ports | Parameters & Operation |
| :--- | :--- | :--- | :--- | :--- |
| **`ValueExtractor`** | `ValueExtractor` | `Member In` | `Value Out` (object) | Reads live edit-time field value from the inspected component instance. |
| **`TypeConverter`** | `TypeConverter` | `Value In` | `Converted Out` | Casts values between `String`, `Int`, `Float`, `Color`, `Hex`, and `Bool`. |
| **`ConstantValue`** | `ConstantValue` | None | `Value Out` | Outputs a constant primitive (`Int`, `Float`, `String`, `Bool`, `Color`). |
| **`MathOperation`** | `MathOperation` | `A` (float), `B` (float) | `Result` (float) | Operations: `Add`, `Subtract`, `Multiply`, `Divide`, `Min`, `Max`, `Clamp`. |
| **`ColorToHex`** | `ColorToHex` | `Color In` (Color) | `Hex Out` (string) | Converts `UnityEngine.Color` to `#RRGGBB` or `#RRGGBBAA` string format. |
| **`RangeRemap`** | `RangeRemap` | `Value`, `InMin`, `InMax`, `OutMin`, `OutMax` | `Result` (float) | Linearly remaps a float from `[InMin, InMax]` to `[OutMin, OutMax]`. |
| **`StringFormatter`**| `StringFormatter` | `Arg0`, `Arg1`, `Arg2` | `Formatted Out` | Tokenized string formatting (e.g. `"{0} ({1})"`). |

---

## 8. Category 7: Variables & Subgraphs

### 2.29 `BlackboardProperty`
- **Enum Type:** `MakeoverNodeType.BlackboardProperty`
- **Purpose:** References an exposed variable from the graph's Blackboard dock.
- **Ports:**
  - `Value Out` *(Output, Capacity: Multi, Type: dynamic based on variable type)*.
- **Exposed Parameters:**
  - `Property Identifier`: The name of the Blackboard variable.

---

### 2.30 `Macro`
- **Enum Type:** `MakeoverNodeType.Macro`
- **Purpose:** Reusable Subgraph Macro referencing a `.msmakomacro` asset. Encapsulates complex multi-node networks into a single, clean node.
- **Ports:**
  - Dynamically generated from the internal `MacroInput` and `MacroOutput` pins within the referenced macro asset.
- **Exposed Parameters:**
  - `Macro Asset`: Reference to the `MakeoverMacroAsset` ScriptableObject.
