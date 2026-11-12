# SonarPingText

> `[SonarPingText]` · Target: `Field | Property` · Category: `Typography` · Assembly: `MSUltimate-AnimatedAttributes`

---

## 1. Overview & Value Proposition

In subsea naval games, deep-ocean exploration, sonar sensor arrays, or submarine simulators, static text feels detached from underwater hydroacoustics. Developers need intuitive visual cues that indicate live listening arrays, acoustic contacts, or active echo-ranging pings.

`[SonarPingText]` sweeps a bright acoustic sonar or radar pulse across field label characters. Energized letters light up with a luminous crest highlight and leave an authentic decaying phosphor trail, mirroring the sweep of a naval hydrophone or planar position indicator (PPI).

---

## 2. Quick-Start Snippet

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class SubmarineAvionics : MonoBehaviour
{
    [SonarPingText(2.5f, 22f, "#38BDF8")]
    public float SonarDepthMeters = 8450.0f;
}
```

---

## 3. Constructors & Signatures

```csharp
// Default constructor (2.5s ping interval, 22 char/s speed, sonar cyan)
public SonarPingTextAttribute();

// Parameterized constructor with custom ping interval, propagation speed, and ping color
public SonarPingTextAttribute(float pingInterval, float pingSpeed = 22f, string pingColor = "#38BDF8");
```

---

## 4. Properties & Customization Table

| Property | Type | Default Value | Description |
| :--- | :--- | :--- | :--- |
| `PingInterval` | `float` | `2.5f` | Interval between acoustic sonar pings in seconds. |
| `PingSpeed` | `float` | `22f` | Character propagation speed of the ping wave. |
| `PingColor` | `string` | `"#38BDF8"` | Acoustic ping beam highlight color at the wave crest (hex code). |
| `TrailColor` | `string` | `"#0284C7"` | Fading phosphor decay trail color (hex code). |
| `Continuous` | `bool` | `true` | When true, pings continuously on the defined interval; otherwise triggers only on hover. |

---

## 5. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class NavalSonarStation : ModularMonoBehaviour
{
    [Title("Hydroacoustic Station", "Acoustic ping sweeps and ocean trench telemetry", BackgroundColor = "#0c2d48", TextColor = "#38BDF8")]

    [BoxGroup("Acoustic Telemetry")]
    [SonarPingText(2.5f, 22f, "#38BDF8")]
    public float TrenchDepth = 10994.0f;

    [BoxGroup("Acoustic Telemetry")]
    [SonarPingText(1.8f, 28f, "#00E5FF", TrailColor = "#00527A")]
    public string ActiveSonarContact = "ACOUSTIC_BOGEY_04";

    [BoxGroup("Ocean Transponders")]
    public List<TransponderBeacon> Beacons = new List<TransponderBeacon>
    {
        new TransponderBeacon("BUOY_PACIFIC_TRENCH", "PINGING"),
        new TransponderBeacon("BUOY_ATLANTIC_RIDGE", "ECHO_LOCKED")
    };

    [Serializable]
    public class TransponderBeacon
    {
        [SonarPingText(2.0f, 22f, "#38BDF8")]
        public string BeaconName;

        public string EchoState;

        public TransponderBeacon(string name, string state)
        {
            BeaconName = name;
            EchoState = state;
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Domain | Compatibility | Notes |
| :--- | :---: | :--- |
| **`[BoxGroup]` & `[AdvancedClass]`** | Compatible | Retains clean container framing during active phosphor ping sweeps. |
| **`[ReadOnly]`** | Compatible | Operates normally on locked sensor readouts and depth coordinates. |
| **Lists (`List<TClass>`)** | Compatible | Safe segmented container prevents DOM corruption in virtualized rows. |

---

## 7. Performance & Architecture

- **Linear Wavefront Mathematics:** Computes distance from wave crest per tick without heap allocations.
- **Color Decay Falloff:** Smoothly interpolates from ping crest to phosphor trail to base inspector color.

