---
layout: post
title: "Health, Radiation and Population Growth"
categories: game-mechanics
---

### Gaining and Losing Colonists
Each colony has a 40% chance each day to gain a colonist. This is the
only way to gain workers. Population size does not affect growth rate.

Each colony has a 10% chance per day to lose one colonist. Colonists
can also be lost due to food/air/water shortages, untreated radiation,
virus outbreaks, certain alien bioweapons, desertion during civil unrest,
and sudden housing shortages caused by housing being blown up.
A colony with zero colonists left is automatically destroyed.

### Medical Centres
Medical centres have exactly two uses: to stop virus outbreaks,
and treat radiation sickness.

An outbreak can begin due to [random event](random-events.html).
Once the colony has one Medical Centre for every 100 colonists after the
first 50, the outbreak ends. Otherwise, it loses two colonists per day.
Medical Centres can end virus outbreaks even if the building is without
power.

Each Medical Centre decreases the negative effects of radiation by 10%.

### Radiation
An asteroid's radiation level increases
by 10% for every 100 un-mined Asteros, for every 2 un-mined
Traxium, and for every 1 un-mined Nexos. This is why it's possible to
lose or demolish some Radiation Filters later and remain at 0% radiation:
the ore that was causing part of the radiation has been mined out.
Radiation can also be increased by certain weapons and random events.

Each active Radiation Filter reduces radiation by 30%.

There is a percentage chance to lose a colonist to radiation sickness
each day, which increases based on the amount of radiation not negated
by Radiation Filters or treated by Medical Centres.

Radiation | Chance of losing one colonist
----------|------------------------------
       0% |   1%
      10% |  11%
      20% |  12%
      30% |  14%
      40% |  15%
      50% |  18%
      60% |  21%
      70% |  26%
      80% |  34%
      90% |  51%
     100% | 100%

### Rapidly Declining Population
The "rapidly declining population" warning triggers whenever a colony's
population drops to 30 or lower. If a reason is given (i.e. lack of food,
air or water), this means the colony is out of surplus in that resource and
may be losing colonists quickly.

If no reason is given, the most likely causes are recent housing
destruction, high radiation, or certain alien population-reducing
weapons.
