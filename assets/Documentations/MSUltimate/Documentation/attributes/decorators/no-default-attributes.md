# [NoDefaultAttributes]

> Explicitly opts out a MonoBehaviour or ScriptableObject class from receiving global default component attributes.

---

## 1. Overview & Value Proposition

**What it does:**
`[NoDefaultAttributes]` is a class-level decorator that instructs the MSUltimate inspector pipeline to completely bypass all project-wide default component attributes (such as auto-injected `[HideScript]`, `[Searchable]`, or default theme headers) for the decorated class and its subclasses.

**The Problem:**
In large projects, teams often configure global default attributes in `Preferences > Maharaja Studio > Default Component Attributes` to ensure a consistent, modern UI across all gameplay scripts without adding boilerplate attributes to hundreds of classes. However, certain specialized components—such as low-level network drivers, third-party engine wrappers, diagnostic benches, or raw debug tools—need to remain completely free of injected decorations and retain only their explicitly declared code layout.

**The Solution:**
Add `[NoDefaultAttributes]` to the class declaration:
- **Instant Exemption:** The component is immediately shielded from all globally injected default component attributes.
- **Explicit Authoring Preservation:** Only attributes directly declared on the class or its fields in C# are rendered.
- **Subclass Inheritance:** Inherited by default across child classes, allowing entire inheritance trees (e.g. low-level transport classes) to stay exempted.
- **Zero Runtime Overhead:** Implemented as a lightweight metadata attribute with compile-time reflection caching and zero garbage generation.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

[NoDefaultAttributes]
public class LowLevelNetworkTransport : MonoBehaviour
{
    public int listenPort = 7777;
    public int maxConnections = 64;
    public bool enableRawSockets = true;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Class | Struct` |
| **Supported Types** | Any `MonoBehaviour` or `ScriptableObject` class or struct |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes (`Inherited = true`) |
| **UI Toolkit Compatible** | Yes |
| **Performance Tier** | Tier 1 (Zero Runtime Cost) |

---

## 4. Constructors & Parameters

```csharp
public NoDefaultAttributesAttribute()
```

*This attribute has no constructor parameters.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Order` | `int` | `0` | Inspector processing priority order. |

---

## 6. Production-Grade Example

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

[NoDefaultAttributes]
[AddComponentMenu("Game/Diagnostics/Dedicated Server Telemetry")]
public class DedicatedServerTelemetry : ModularMonoBehaviour
{
    [Title("Raw Telemetry Pipeline", "Exempt from project-wide default component attributes")]
    [InfoBox("This component is marked with [NoDefaultAttributes]. Even when global defaults (like auto-HideScript or default headers) are enabled project-wide, this inspector renders exactly as authored without automatic injections.", InspectorMessageType.Info)]

    [Header("Network Socket Configuration")]
    public string serverAddress = "127.0.0.1";
    public int serverPort = 8080;
    public bool useTcpNoDelay = true;

    [Header("Buffer Endpoints")]
    public string[] activeEndpoints = new string[]
    {
        "/api/v1/telemetry",
        "/api/v1/heartbeat",
        "/api/v1/metrics"
    };

    [Header("Payload Protocol (Nested Class Showcase)")]
    public PacketSchema packetSchema = new PacketSchema("BinaryProtobuf", 1024);

    [Serializable]
    public class PacketSchema
    {
        public string encodingName;
        public int maxPayloadBytes;

        public PacketSchema(string encoding, int maxBytes)
        {
            encodingName = encoding;
            maxPayloadBytes = maxBytes;
        }
    }

    [Title("Diagnostic Actions")]
    [Button("Verify Exemption Status", ButtonHeight = 30)]
    public void VerifyExemption()
    {
        Debug.Log($"<color=#38BDF8>[Telemetry]</color> Running standalone without global default attribute injection. Port: {serverPort}");
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Title]` | Recommended | Pairs cleanly with explicit titles and headers without automatic injection interference. |
| `[BoxGroup]` | Supported | Explicit field layout groups render exactly as declared. |
| `[HideScript]` | Supported | Can still be explicitly added if script hiding is specifically desired for this individual component. |
| **Inspector Customizer** | Overridable | Specific per-type Inspector Customizer profiles can still explicitly apply virtual attributes if desired. |
| **Ignore Rules Engine** | Integrated | Recognized automatically by the MSUltimate Component Defaults settings engine as a priority rule. |
