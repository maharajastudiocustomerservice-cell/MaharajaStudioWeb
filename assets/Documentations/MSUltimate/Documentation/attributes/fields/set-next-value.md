# [SetNextValue]

> Automatically assigns sequential numbers, auto-incremented counters, or collection index formulas upon creation, with an inline step button (⏭).

---

## 1. Overview & Value Proposition

**What it does:**
Automatically seeds sequential, incremental, or list-index-driven numbers and formatted string codes when a new component is added, an asset is created, or a new item is inserted into a List/Array. Includes an inline ⏭ step button right in the Inspector to advance to the next value at any time.

**The Problem:**
Creating lists of sequential game data—such as quest IDs (`"Quest_001"`, `"Quest_002"`), dialogue line numbers, inventory slot identifiers, or audio channel indexes—requires tedious manual entry. Designers frequently make typos or duplicate IDs, leading to corrupted save files and progression bugs.

**The Solution:**
Add `[SetNextValue]` to numeric or string fields:
- **Automatic Auto-Increment:** New list items or components automatically receive the next counter value (`StartValue + Step`).
- **Formatted Strings:** Formats integers into strings with custom prefixes, suffixes, and padding (e.g. `Prefix = "Quest_", Format = "D3"` produces `"Quest_001"`, `"Quest_002"`).
- **Collection Index Binding:** When placed inside a List or Array, automatically mirrors element indices via `(Index * Step + StartValue)`.
- **Custom Source Members:** Pulls sequential values from a custom generator method or cycles through a predefined array.
- **Manual Step Button:** Click the inline ⏭ button to increment to the next sequence value on demand.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class QuestNode : MonoBehaviour
{
    [SetNextValue("Quest_", startValue: 1, step: 1, format: "D3")]
    public string questIdentifier = "Quest_001";

    [SetNextValue(10, step: 5)]
    public int baseExpReward = 10;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `int`, `float`, `double`, `string` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public SetNextValueAttribute()
public SetNextValueAttribute(string prefix, int startValue = 1, int step = 1, string format = "")
public SetNextValueAttribute(int startValue, int step = 1)
public SetNextValueAttribute(string sourceMember)
public SetNextValueAttribute(Type staticType, string sourceMember)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `prefix` | `string` | `""` | Optional string prepended to the generated value. |
| `startValue` | `int` | `1` | Starting numerical sequence number. |
| `step` | `int` | `1` | Increment added for each sequential step. |
| `format` | `string` | `""` | Number formatting pattern (e.g. `"D2"`, `"D3"`, `"000"`). |
| `sourceMember` | `string` | `null` | Member name providing next value or collection to cycle. |
| `staticType` | `Type` | `null` | Type declaring the static generator member. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `StartValue` | `int` | `1` | Starting counter number for the sequence. |
| `Step` | `int` | `1` | Increment delta added per generation. |
| `Prefix` | `string` | `""` | String prepended to formatted results. |
| `Suffix` | `string` | `""` | String appended to formatted results. |
| `Format` | `string` | `""` | Numerical format specification (e.g. `"D3"`). |
| `SequenceKey` | `string` | `null` | Shared sequence counter key across multiple components. |
| `UseCollectionIndex` | `bool` | `true` | Derives value from list item index inside collections. |
| `SourceMember` | `string` | `null` | Name of method or collection member providing values. |
| `StaticType` | `Type` | `null` | Declaring type for static source member. |
| `Overwrite` | `bool` | `false` | If `true`, overwrites existing non-empty values upon reset. |
| `OnlyOnCreation` | `bool` | `true` | Only runs automatic assignment during creation or reset. |
| `ShowNextButton` | `bool` | `true` | Renders inline ⏭ step button beside the field. |
| `ButtonTooltip` | `string` | `"Step to next sequential value"` | Tooltip text on the ⏭ step button. |
| `Order` | `int` | `0` | Execution priority in modifier pipeline. |

---

## 6. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

[Serializable]
public class DialogueEntry
{
    [SetNextValue("Line_", startValue: 1, step: 1, format: "D2")]
    public string lineId;

    [TextArea(2, 4)]
    public string spokenText;
}

public class DialogueScript : MonoBehaviour
{
    [Header("Sequential Chapter Setup")]
    [SetNextValue("CH_", startValue: 100, step: 10, format: "D3")]
    public string chapterCode;

    [Header("Indexed Dialogue Lines")]
    public List<DialogueEntry> dialogueLines = new List<DialogueEntry>();
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Inline step button fits neatly alongside text boxes inside groups. |
| `[ReadOnly]` | Supported | Keeps the field read-only to manual typing while allowing ⏭ button increments. |
| `[ShowIf]` | Supported | Sequencer pauses updates while parent field is hidden. |
| `ICollectionElement` | Supported | Auto-populates incremental values when adding elements in lists and arrays with per-cell step buttons. |
| `ICollectionBatch` | Supported | Sequences all elements across multiple pages using collection indexing on load / additions, and provides a header `⏭` button to re-sequence the entire collection. |
