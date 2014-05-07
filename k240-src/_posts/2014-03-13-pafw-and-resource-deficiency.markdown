---
layout: post
title: "PAFW and Resource Deficiency"
categories: game-mechanics
---

### Power failure
If there is insufficient power to supply all buildings, they fail in a
specific order until supply meets usage.
All units of a building fail at the same time:
if there is only enough power for nine out of ten Mines, all Mines fail.

Only certain buildings actually cease to function when affected by
a power outage. Some fail partially, while others fail in an
unexpected manner.

|Order| Building                | Power | Fails?   |
|-----|-------------------------|-------|----------|
|  1  | Asteroid Engines        | 2-7   | Yes      |
|  2  | Ore Teleporter          | 1     | No       |
|  3  | Gravity Nullifier       | 0/4   | Yes      |
|  4  | Satellite Silo          | 0     | No       |
|  5  | Anti-Missile Pod        | 3     | Yes      |
|  6  | Seismic Penetrator      | 3     | Yes      |
|  7  | Security Centre         | 2     | No       |
|  8  | Deep Bore Mine          | 2     | Yes      |
|  9  | Mine                    | 1     | Yes      |
| 10  | Weapons Factory         | 2     | No       |
| 11  | Construction Yard       | 2     | Yes      |
| 12  | Sensor Array            | 2     | Yes      |
| 13  | Laser Turret            | 2     | Yes      |
| 14  | Plasma Turret           | 3     | Turret   |
| 15  | Photon Turret           | 5     | Turret   |
| 16  | Medical Centre          | 1     | Partial  |
| 17  | Protected Storage Tower | 4     | Turret   |
| 18  | Protected Resiblock     | 5     | Turret   |
| 19  | Repair Facility         | 0     | Yes      |
| 20  | Decontamination Filter  | 3     | Yes      |
| 21  | Screen Generator        | 7     | Yes      |
| 22  | Command Centre          | 3     | No       |
| 23  | Hydroponics             | 2     | Yes      |
| 24  | Hydration Plant         | 1     | Yes      |
| 25  | Life Support            | 2     | Yes      |
| 26  | Missile Silo            | 0     | No       |
| 27  | Landing Pad             | 0     | No       |
| 28  | Protected Env/Ctrl      | 3     | Turret   |
| 29  | Environment Control     | 0     | No       |
| 30  | Storage Tower           | 2     | No       |
| 31  | Protected Solar Matrix  | 0     | Turret   |
| 32  | Solar Matrix            | 0     | N/A      |
| 33  | Solar Generator         | 0     | N/A      |
| 34  | Solar Panel             | 0     | N/A      |
| 35  | Storage Facility        | 1     | No       |
| 36  | Power Store             | 0     | N/A      |
| 37  | Resiblock               | 2     | No       |
| 38  | Living Quarters         | 0     | No       |
| 39  | Powerplant              | 0     | N/A      |
| 40  | C.P.U.                  | 0     | No       |

### Unexpected failure modes
When Gravity Nullifier switches off due to a power outage, it does not
automatically switch itself back on when power is restored.

When Laser Turrets fail, all other turrets fail also. This includes the
turrets of Protected buildings.

Medical Centres cannot treat radiation sickness in a power outage, but
can still end a virus outbreak.

Repair Facility can still fail during a power outage even though it
consumes no power.

### Air, food and water shortages
Each colonist needs one unit of air, food and water per day. If production
is insufficient, the remaining colonists consume from stored surplus,
triggering a "resource deficiency" status and orange colour readout.

Red colour occurs when production is insufficient and there is no surplus,
leaving the remaining colonists with no air/food/water. Those colonists
are killed at the following rate each day:

| Resource | Affected colonists killed per day           |
|----------|---------------------------------------------|
| Air      | Kills all affected colonists                | 
| Food     | Kills 1/10 of affected colonists, plus one  |
| Water    | Kills 1/5 of affected colonists, plus one   |

Additionally, for each resource in the red,
[social unrest](security-and-morale.html) increases by +2
points per day.
