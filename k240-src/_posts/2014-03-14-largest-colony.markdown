---
layout: post
title: "Largest Possible Colony"
categories: fun
---

Just for fun, what's the most colonists that can fit on one asteroid?

### Limiting factors
An asteroid has a maximum of 100 buildings, even if it has more open squares.
In theory an asteroid could support 100 Resiblocks for a total of 15,000 colonists,
but those colonists would never accumulate without first satisfying their
food, air, water, medical and security requirements. Those buildings in turn have
power requirements. All this eats into the maximum number of Resiblocks we can have.

### Requirements
| Building        | Power  | Pop. supported | Cost  |
|-----------------|--------|----------------|-------|
| Resiblock       |   2 MW |            150 |  3000 |
| Life Support    |   2 MW |            500 | 13000 |
| Hydration Plant |   1 MW |            500 |  5000 |
| Hydroponics     |   2 MW |            400 |  7000 |
| Medical Centre  |   1 MW |            100 |  5000 |
| Security Centre |   2 MW |            100 |  4500 |
| Solar Matrix    | -16 MW |            -   |  5000 |

For maximum density, we'll use the Solar Matrix which generates 8 MW normally,
and the Power Amplifier blueprint which increases that to 16 MW. We'll detonate
our CPU for extra room.

We have some leeway in the medical and security buildings. The first 50 population
are exempt from their requirements, and only each full 100 after that are
required.

### A big happy colony
A 1,950 population colony requires 4 Life Support, 4 Hydration Plant,
5 Hydroponics, 19 Medical Centre, 19 Security Centre and 13 Resiblock. This
requires 105 Power, or 7 Solar Matrix. Total building count: 71.

This colony would cost 361,500 CR to establish, or 491,500 CR including the cost
of the Solar Matrix and Power Amplifier blueprints.
Without the blueprint tech, the same colony could be built with Solar Generators
for 368,500 CR and 92 buildings.

Either way, we don't need any Radiation Filters (10+ Medical Centres will treat
100% Radiation). The colony will grow to maximum capacity within about 6,500 days,
at which point it will be earning 4,000 CR per day.

But there's still room.

### The biggest, happiest colony
At a population of 2,700, the colony is almost maxed out at 99 buildings:
18 Resiblocks, 6 Life Support, 6 Hydration Plant, 7 Hydroponics,
26 Medical Centres, 26 Security Centres and 10 Solar Matrix, at a total
cost of 508,000 CR before blueprints. In exchange, a daily tax of
5,500 CR can be yours.

Such a colony will accept an extra Resiblock and raise the maximum to 2,850,
but the colony runs run short of medical and security at 2,750 and food at
2,800, which is a disaster for morale. A Living Quarters would be more
reasonable as it adds only 50 capacity, but the final 2,750th colonist would
still push security and medical over the limit.

### Forget happy
If we're willing to take some risks and sacrifice the workers' quality of
life, a colony can grow even bigger.

First, destroy all Medical Centres. This saves us 26 squares, 26MW of power
and 130,000 cash. As long as you have no Radiation and don't get a virus
outbreak, you don't need Medical Centres.

You can now build 3,800 population colony with 25 Resiblocks and one
Living Quarters, earning 7,700/day for an investment of 511,500 CR.
A 26th Resiblock instead of Living Quarters would raise that to 3,900,
but colonist #3,850 would trigger the security shortage again.

### Forget security too
If you're going to trigger security, there's no mechanical benefit to
having even one Security Center. Since our colony has 37 of them and
they each use up 2MW of power, we can grow our colony to absurd size
if we're willing to put up with constant security alert status.

A 6,600 person colony can be built using 44 Resiblocks, 14 Life Support,
14 Hydration Plants, 17 Hydroponics, and 11 Solar Matrix, at a total
cost of 558,000 (688,000 including blueprints) and earning an absurd
13,300 CR per day.

Since this setup uses 100 buildings and you can't add another colonist
here without building a Resiblock, this is the absolute maximum size of
a colony. It's not possible to destroy an air/food/water building without
dropping the output below 6,600, and destroying even one Solar Matrix
would immediately shut down all Hydration Plants at a colony with no surplus,
killing colonists at a rate of over 20% per day.

Even at the stable level of 6,000, there's a catch. Without security, the
colony will be permanently stuck at maximum level "Security Alert!"
Every 30-59 days, there is a 20% chance that one of your blueprints will
be stolen. If that blueprint is Power Amplifier, your colony's power output
immediately drops by half (176MW to 88MW). This is exactly enough to power
your Resiblocks, but everything else goes offline... including Life Support.

### In summary
2,700 is the largest colony you can safely build, assuming you spend a lot
on power blueprints. That raises to 3,800 if you ignore Medical Centres,
but your colony will lose all that population if there's a virus outbreak.
Finally, you can push the population up to 6,600 if you're willing to
endure security alerts, but you're doomed as soon as someone steals your
Power Amplifier tech.
