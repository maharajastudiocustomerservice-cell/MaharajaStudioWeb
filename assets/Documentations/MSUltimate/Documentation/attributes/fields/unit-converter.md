# [UnitConverter]

> Displays live converted physical units (meters to feet, km/h to mph, Celsius to Fahrenheit) inside a sleek badge beside numeric fields.

---

## 1. Overview & Value Proposition

**What it does:**
Renders a live, real-time conversion badge next to any numeric serialized field (`float`, `double`, `int`). Supports popular physical presets (e.g. `MetersToFeet`, `CelsiusToFahrenheit`, `SecondsToMinutes`, `RadiansToDegrees`) or custom conversion formulas with multiplier factors and offsets.

**The Problem:**
Game engines predominantly use the metric system (meters, kilograms, seconds, radians). However, many designers, artists, and international team members think in imperial units (feet, miles, pounds, degrees, Fahrenheit). Continuously calculating conversions externally slows down balancing and leads to incorrect scale parameters.

**The Solution:**
Add `[UnitConverter]` to any numeric field:
- **Instant Live Preview:** As you scrub or edit a value in meters, the badge instantly updates to display the equivalent in feet.
- **Predefined Presets:** 13+ built-in presets covering distance, velocity, mass, temperature, angles, time, and data size.
- **Custom Conversion Factors:** Define custom units and formulas (`conversionFactor`, `offset`, `decimals`) for fantasy currencies, stamina rates, or bespoke metrics.
- **Sleek Pill Badge Display:** Renders the converted output inside a modern rounded pill badge with customizable colors.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class VehiclePhysics : MonoBehaviour
{
    [UnitConverter(UnitPreset.KilometersToMiles)]
    public float topSpeedKmH = 240f; // Displays ~149.13 mi in inspector badge

    [UnitConverter(UnitPreset.MetersToFeet)]
    public float vehicleLengthMeters = 4.8f; // Displays ~15.75 ft
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `float`, `double`, `int`, `long` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public UnitConverterAttribute()
public UnitConverterAttribute(UnitPreset preset, int decimals = 2)
public UnitConverterAttribute(string fromUnit, string toUnit, float conversionFactor, float offset = 0f, int decimals = 2)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `preset` | `UnitPreset` | `UnitPreset.Custom` | Built-in physical conversion algorithm. |
| `decimals` | `int` | `2` | Number of decimal places to format in the badge. |
| `fromUnit` | `string` | *(Required)* | Label representing input unit (e.g. `"m"`). |
| `toUnit` | `string` | *(Required)* | Label representing converted output unit (e.g. `"ft"`). |
| `conversionFactor`| `float` | *(Required)* | Multiplication factor applied to the source value. |
| `offset` | `float` | `0f` | Additive offset applied after scaling (e.g. `32f` for Fahrenheit). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Preset` | `UnitPreset` | `UnitPreset.Custom` | Selected preset mode (`MetersToFeet`, `KilogramsToPounds`, etc.). |
| `FromUnit` | `string` | `null` | Display unit symbol for the input field. |
| `ToUnit` | `string` | `null` | Display unit symbol for the converted badge. |
| `ConversionFactor`| `float` | `1f` | Multiplier applied during mathematical conversion. |
| `Offset` | `float` | `0f` | Additive offset applied after factor multiplication. |
| `Decimals` | `int` | `2` | Number of decimal places rendered in the output. |
| `ColorHex` | `string` | `null` | Hex color code for the badge background and text. |
| `AsBadge` | `bool` | `true` | If `true`, styles the converted value as a rounded pill badge. |
| `Order` | `int` | `0` | Drawing order priority in the inspector pipeline. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class EnvironmentalSim : MonoBehaviour
{
    [Header("Temperature Sim")]
    [UnitConverter(UnitPreset.CelsiusToFahrenheit, ColorHex = "#e74c3c")]
    public float ambientTemperatureCelsius = 32.5f;

    [Header("Atmospheric Density")]
    [UnitConverter(UnitPreset.KilogramsToPounds)]
    public float airMassPerCubicMeter = 1.225f;

    [Header("Custom Currency Conversion")]
    // 1 Gold Coin = 100 Silver Coins
    [UnitConverter(fromUnit: "Gold", toUnit: "Silver", conversionFactor: 100f, decimals: 0, ColorHex = "#f1c40f")]
    public int startingGoldCoins = 25;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Converted pill badge integrates seamlessly into card containers. |
| `[ShowIf]` | Supported | Updates badge calculations only when the field is visible. |
| `[ReadOnly]` | Supported | Displays conversion badge cleanly next to read-only fields. |
| `ICollectionElement` | Supported | Compatible with arrays and lists of numeric values. |
