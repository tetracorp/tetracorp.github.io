---
layout: post
title: "PAFW and Resource Deficiency"
---

### Powerplant quirks
The Powerplant does not work as described in the manual. Due to a bug,
Asteros un-mined depletes at a rate of 1 per four days even if no
Powerplants are built. It produces 32Mw as long as there is at least one
un-mined Asteros, but cannot use mined ore from storage.

It produces no power without Asteros. Although the manual claims the
Powerplant produces 8MW/day, this appears to be a mis-reading of the
game code. The C.P.U. produces 8MW/day.

A random event can cause a Powerplant to explode, increasing a colony's
radiation. Strangely, Asteroid Engines also produce radiation if they
explode due to random event.

### Power failure
If there is insufficient power to supply all buildings, they fail in a
specific order of preference.

### Air, food and water shortages
Each colonist needs one unit of air, food and water per day. If production
is insufficient, the remaining colonists consume from stored surplus,
triggering "resource deficiency" and orange colour readout.

Red colour occurs when production is insufficient and there is no surplus,
leaving the remaining colonists with no air/food/water. Those colonists
without any food are killed at the following rate each day:

| Air   | Kills all affected colonists                     | 
| Food  | Kills 1/10 of affected colonists, plus one more  |
| Water | Kills 1/5 of affected colonists, plus one more   |

Additionally, for each resource in the red, social unrest increases by +2
points per day.
