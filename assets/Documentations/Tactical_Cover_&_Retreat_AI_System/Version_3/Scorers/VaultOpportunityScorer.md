# Scorer: Vault Opportunity Scorer

**`VaultOpportunityScorerSO`** evaluates candidate hiding spots based on whether the obstacle has the `CoverPointFlags.Vaultable` bit flag. It enables mobile, aggressive AI units to prioritize cover they can mantle over during combat.

---

## How It Works

* **Bitmask Inspection:** Inspects `candidate.HasFlag(CoverPointFlags.Vaultable)`.
* **Zero-Allocation:** Unmanaged, instantaneous bitwise evaluation.
* **Strict Mode (`requireVaultableOnly`):** Can be configured to veto non-vaultable cover (`-Infinity`), forcing the agent to only pick agile traversal spots.

---

## Inspector Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `vaultableScore` | `float` (0-1) | `1.0` | Score awarded to candidate spots that can be vaulted over. |
| `nonVaultableScore` | `float` (0-1) | `0.2` | Score awarded to static, high or non-vaultable walls. |
| `requireVaultableOnly` | `bool` | `false` | If true, non-vaultable spots are rejected (`-Infinity`). |

---

## Archetype Presets

### Shotgun Flanker / Rusher
* `vaultableScore`: `1.0`
* `nonVaultableScore`: `0.1`
* Encourages AI to path to low barriers where it can immediately execute `TacticalAgent.CanVaultCover()` to hop over and flank enemies.
