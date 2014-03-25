---
layout: post
title: "Random Events"
categories: game-mechanics
---

Random events can occur, such as a solar flare increasing radiation on all
asteroids or a survey discovering more ore deposits than previously thought.

The first random event to occur in a game is ignored and the manual protection code
request appears in its place. The next random event will occur randomly
between 10 and 39 days later. Each random event after that will occur
between 4 and 60 days after one another, with a small chance of a 255
day wait instead.

If you have no Transporter, the random event is always "The Empire has sent
you a new Transporter". Otherwise, it is chosen at random, with a 1 in 24
chance of each, except for three events which have a 1 in 12 chance.

### None
Nothing happens.

### Magnetic Storm
All ships cannot move for 158-198 days.

### Scout Breakup
Goes through all ships until it finds a Scout, then scraps it.

### Radiation Leak
Radiation increases by 10% on one asteroid.

### Solar Flare
Radiation increases by 10% on all asteroids.

### Freak Sensor Scan
Goes through all asteroids and reveals the first alien asteroid it
finds, awarding a bonus of 10,000 CR. The Swixaran asteroid cloaking
device renders it immune to this effect. You do not need a Sensor Array
to generate a freak sensor scan.

### Survey: More Ore (double chance)
Adds a random amount of every ore to a random asteroid. It can never
add Traxium or Nexos.

| Ore        | Amount |
|------------|--------|
| Selenium   |  0-199 |
| Asteros    |  0-199 |
| Barium     |  0-199 |
| Crystalite |   0-99 |
| Quazinc    |   0-49 |
| Bytanium   |   0-49 |
| Korellium  |   0-19 |
| Dragonium  |    0-9 |

### Survey: Less Ore
Reduces the amount of each ore at a random asteroid by a random amount,
to a minimum of zero. It never reduces Traxium or Nexos. This event can occur
at an asteroid which already has no ore left, but it cannot reduce the ore
below zero and cannot retroactively remove ore that has already been mined.

| Ore        | Amount |
|------------|--------|
| Selenium   |   0-99 |
| Asteros    |   0-99 |
| Barium     |   0-99 |
| Crystalite |   0-49 |
| Quazinc    |   0-24 |
| Bytanium   |   0-24 |
| Korellium  |    0-9 |
| Dragonium  |    0-4 |

### Powerplant Burnout
A Powerplant at a random asteroid explodes. Radiation increases 10%.

### Gravitational Anomaly (Asteroid Engine Burnout)
An Asteroid Engine at a random asteroid explodes. Radiation increases 10%
for some reason, as with Powerplant burnout.

### Pressure Valve Failure
Air surplus reduces to zero. Only a problem if you don't have enough
Life Support for your population.

### Ruptured Pipeline
Water surplus reduces to zero. There's no "food reduces to zero" event.

### Computer Control Station Failure
Power surplus reduces to zero.

### Gravitational Vortex
All asteroids change speed and direction.

### Virus Outbreak
If a random asteroid has insufficient Medical Centres (one for every
full 100 colonists after the first 50), the colony suffers a virus outbreak.
It loses two colonists per day until there are enough Medical Centres for
the population level.

### Ore Bribe
You receive 10,000 to 100,000 CR. Your ore shipments are actually irrelevant:
the size of bonus received and your chance of receiving another bribe are
completely random.

### (unknown event) (double chance)
Currently unknown.

### Reinforcements (double chance)
Receive 5-10 ships randomly chosen from the following types:
Assault Fighter, Combat Eagle, Scoutship, Destructor, Terminator. The ships
are outfitted with random hardpoints, but cannot have Static Inducer or
Warp Generator, and the first hardpoint on each ship is always a weapon.

### Meteor Shower
A shower of 5-19 meteors is scheduled for a random asteroid. It behaves like
a missile strike. Meteors deal 30 damage, three times as much as Explosive
missiles.

### Fixed Ore Prices
Between 2 and 5 times, a random ore is fixed in price for 2-5 years each.
If the random number generator picks the same ore more than once, the
duration does not stack.

### New Transporter
Receive a new Transporter. The hardpoints are always random, but cannot
include Static Inducer or Warp Generator. The first hardpoint is always
a weapon, which is why Transporters often seem to arrive with a ridiculous
configuration like two Lasers or a Laser and a Napalm Orb.
