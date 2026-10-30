# [RichTextLabel]

> Overrides the property label with custom text supporting Unity rich-text markup tags for colors and formatting.

`Package: MSUltimate Core` `Targets: Field | Property` `AllowMultiple: False` `Inherited: True` `Performance: Zero Runtime Cost (Editor Visual Only)`

---

## 1. Overview & Value Proposition

**What it does:**
Renders field labels using full Unity rich-text HTML-like markup tags (such as `<b>`, `<i>`, `<color=#FF0000>`, or `<size=14>`).

**The Problem:**
Standard Unity inspector labels only support plain text. You cannot highlight specific words in a sentence, change color on a per-word basis, or make a crucial keyword bold while keeping the rest regular without writing custom editor code.

**The Solution:**
Add `[RichTextLabel]` to any field:
- **Rich-Text Markup Support:** Use standard Unity tags like `<color=#3498db><b>Mana</b></color> Cost` directly in the label string.
- **Word-Level Highlighting:** Colorize and style individual words independently.
- **Dynamic Formatting:** Combine font size tags, bold, italics, and custom hex codes in a single label.
- **Zero Runtime Overhead:** Parsed directly within the UI Toolkit decorator pass with instant editor rendering.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class SpellData : MonoBehaviour
{
    [RichTextLabel("<color=#3498db><b>Mana</b></color> Cost")]
    public float manaCost = 50f;

    [RichTextLabel("<color=#e74c3c>Critical</color> Multiplier (<i>x2.5</i>)")]
    public float critMult = 2.5f;
}
```

---

## 3. Constructors & Parameters

```csharp
public RichTextLabelAttribute(string text)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `text` | `string` | *(Required)* | Label text string containing Unity rich-text markup tags. |

---

## 4. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Text` | `string` | *(Required)* | Custom rich-text formatted string. |
| `Order` | `int` | `1` | Early decorator pipeline processing order. |

---

## 5. Production-Grade Example

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using Header = MaharajaStudio.MSUltimate.Runtime.HeaderAttribute;

namespace MaharajaStudio.MSUltimate.Example
{
    public class RichTextLabelExample : ModularMonoBehaviour
    {
        [Title("Network Security Coordinator", "Rich-text tags embedded directly into property labels")]
        [InfoBox("Use [RichTextLabel] to inject standard Unity HTML-style rich-text tags (<b>, <i>, <color>, <size>) directly into inspector labels for instant visual hierarchy.", InspectorMessageType.Info)]

        [Header("Security Rules & Thresholds")]
        [RichTextLabel("<b><color=#EF4444>[CRITICAL]</color></b> Firewall Rule Enforcement")]
        [Tooltip("Bold red tag highlighting a vital security toggle.")]
        public bool enforceFirewall = true;

        [RichTextLabel("<i>Server Latency Threshold</i> (<color=#22C55E>ms</color>)")]
        [Range(20f, 500f)]
        public float latencyWarningMs = 150f;

        [RichTextLabel("<size=13><b><color=#38BDF8>TLS Encryption Cipher</color></b></size>")]
        public string cipherSuite = "AES_256_GCM_SHA384";

        [RichTextLabel("<b><color=#F59E0B>⚠ Maintenance Mode Active</color></b>")]
        public bool isMaintenanceMode = false;

        [Title("Nested Class Showcase")]
        public ClusterNodeSlot primaryNode = new ClusterNodeSlot
        {
            nodeIdentifier = "US-EAST-ALPHA-01",
            listeningPort = 8443
        };

        [Header("Failover Nodes Collection")]
        public ClusterNodeSlot[] failoverNodes = new ClusterNodeSlot[]
        {
            new ClusterNodeSlot { nodeIdentifier = "EU-WEST-BRAVO-02", listeningPort = 8443 },
            new ClusterNodeSlot { nodeIdentifier = "AP-SOUTH-CHARLIE-03", listeningPort = 8443 }
        };

        [Serializable]
        public class ClusterNodeSlot
        {
            [RichTextLabel("<b><color=#818CF8>Node Identifier</color></b>")]
            public string nodeIdentifier;

            [RichTextLabel("<color=#34D399>Listening Port</color>")]
            public int listeningPort;
        }

        [Title("Interactive Simulation")]
        [Button("Simulate Cluster Handshake", BackgroundColor = "#2563EB", TextColor = "#FFFFFF")]
        private void SimulateHandshake()
        {
            string firewallStatus = enforceFirewall ? "<color=#22C55E>ACTIVE</color>" : "<color=#EF4444>DISABLED</color>";
            Debug.Log($"<color=#38BDF8>[RichTextLabelExample]</color> <b>Firewall:</b> {firewallStatus} | <b>Latency:</b> {latencyWarningMs}ms | <b>Primary Node:</b> {primaryNode.nodeIdentifier}:{primaryNode.listeningPort}");
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[SuffixLabel]` | Supported | Pairs cleanly with suffix units. |
| `[BoxGroup]` | Supported | Functions inside group layouts without breaking formatting tags. |
| `[ShowIf]` / `[HideIf]` | Supported | Hides or shows the rich-text label dynamically based on conditions. |
| `[ValidateNotNull]` | Supported | Combines rich-text styling with inline validation indicators. |

---

## 7. Collection Cascading & Custom Serializer Discipline

| Context / Architecture | Support | Behavior & Guidelines |
| :--- | :---: | :--- |
| **Collection Header Label** | Supported | Overrides the root collection container foldout label with rich text markup. |
| **Element-Level Cascading** | **Rejected by Design** | Element cascading is deliberately rejected because overriding row labels with identical text obliterates collection indexing (`Element 0`, `Element 1`). |
| **Nested Serializable Classes** | Supported | Custom class fields inside collections (`List<T>`, `T[]`) can each declare their own distinct `[RichTextLabel]` tags. |
| **Custom Serializers** | Supported | Compatible with `SerializableDictionary<K, V>`, `AdvancedList<T>`, and `SerializableTuple<...>`. |
