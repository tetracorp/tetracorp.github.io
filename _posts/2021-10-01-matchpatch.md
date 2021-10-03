---
title: "Match Patch (1990)"
categories: amiga
---

__Match Patch__ is a Commodore Amiga game released in 1990. It is a public
domain platformer about shooting enemies with bullets of the matching type.

1. Table of Contents
{:toc}

### Cheats

There are two built-in cheat codes in Match Patch.

- At the title screen, hold left and press fire to skip to level 10.
- At the title screen, hold right and press fire to reduce the number of points
  needed to earn a new life from 20,000 to 10,000.

There appear to be no references in the code to read from the keyboard, so it's
likely that these are the only two cheats in the game.

If the game is still too difficult, you can hack the game to start with 99 lives:

- Decompress MatchPatch with xfdDecrunch (xfdMaster from Aminet)
- Use a hex editor to change the bytes at 0x327 and 0x2129 from "03" to "63".

### Documentation

Since the game is generally distributed without any documentation, some of the
game mechanics may not be immediately clear.

Your goal is to clear the screen of enemies before time runs out. There are five
enemy types, and each can only be killed by bullets of its own type. (Fire beats
fire, ice beats ice... this is opposite to modern game design thinking, perhaps
because this was 1990 and Pok&eacute;mon wasn't invented yet.)

Shooting an enemy with the wrong type will just transform them into the next
enemy type that isn't the bullet you have. (Sometimes this is still a good idea,
because some enemy types have more predictable movement, so they're safer.
Better Stone than Fire.)

There are holes in the floor of each map with arrows of the various enemy types.
When an enemy falls down it, it changes into that type and re-enters from the
top of the screen again. When you fall down it, your bullet changes to that
type.

If you hold the fire button when you fall down a hole, it will change the hole's
enemy type to the next one. You can use this to your advantage by, say, turning
all holes into a nice predictable type like Stone. However, when you re-emerge
from the top of the screen, your weapon will be whatever the hole was before you
changed it, and you'll have to fall back through it again if you want to have
bullets for the new type. Changing types on multiple holes is time-consuming,
and you have a time limit.

The wine glass increases your range. The light switch lets your bullet pass
through enemies and potentially hit multiple enemies with one shot. (It doesn't
kill all Light type enemies, even though that would make sense...) If you die,
you lose these powerups. The effects of the other powerups are described if you
wait at the title screen.

You receive a bonus life for every 20,000 points.

There are 24 different levels. When you reach level 25, it just loops around to
level 1 again. The game seems to continue indefinitely until you run out of
lives, at which point you enter the high score chart. The high scores aren't
saved between plays&mdash;Match Patch doesn't load `dos.library`, which contains
the standard file load/safe functions. (It only loads `graphics.library`, and
only to copy bytes 38-41 (decimal) from the library, which is read once at new
game start, I'm not sure what for.)

The game doesn't seem to run well on A1200. This is a problem you saw less after
the A1200 was released in October 1992 and it became common to make sure games
were forwardly-compatible with the new system.

### History of development and release

According to a date on the title screen, Match Patch was created in 1990 by
someone known only as "SD", who provided both ideas and code. The high score
chart also credits the game's program, code, graphics, and sound to this SD.

    ; 250000 -*------*-
    ; 225000  MATCH    
    ; 200000     PATCH 
    ; 175000 -*------*-
    ; 150000  PROGRAM  
    ; 125000  CODE,    
    ; 100000  GRAPHICS,
    ;  75000  SOUND   
    ;  50000     BY    
    ;  25000     SD.   
    ;      0 ..........

The name "SD" is never actually shown to the player on the high score chart,
since it's the last entry shown, you need to beat it to make an entry, and the
game only shows you the high score chart when you make an entry.

Match Patch was distributed widely in two popular sources: the CU Amiga Magazine
coverdisk #22 for the December 1991 issue, compiled by Martin Rayner; and the
Assassins Games compilation disk #20, where it has the file date of 2 April
1991, and the disk itself is dated 2 September 1992. CU #22 was also
redistributed by Public Domain disk companies under the title "21 Games". Match
Patch does not appear to have been uploaded to Aminet.

It is compressed with xfdMaster and has a filesize of 71,364 bytes, not doubt to
fit better on the disk (although this is still a significant 7.9% of an Amiga
disk, so Match Patch takes up more than the average of 21 Games). Uncompressed,
Match Patch is 206,712 bytes. You can decompress it with xfdDecrunch (xfdMaster
should be available on Aminet). It's unknown whether Martin Rayner compressed
it, or it was already compressed. A lot of games on CU22 are packed with XFD,
but then it's a coincidence that ASI20's later release has Match Patch dated
earlier than CU22 (although Amiga file dates were often inaccurate due to the
lack of a real-time clock in the basic models).

On both CU22 and ASI20, the game is distributed without documentation. This
makes it difficult to know who the author is, or even to verify that the game is
public domain. Content has been falsely distributed as Public Domain before,
including [Dungeons of Avalon](https://tetracorp.github.io/dungeons-of-avalon/)
and even CU22 itself.

It's a reasonable assumption that the game was written in assembly language,
rather than something like AMOS Basic (which produces awful code when
disassembled). The whole game is one standalone file, except that it calls on
the Amiga's `graphics.library`, and the uncrunched version requires
`explode.library` due to being packed with XFD.

You can see some IFF file headers for IFF 8SVX audio files in the code, with the
following comment:

    Recorded with PERFECT SOUND from SunRize Industries.  (409) 846-1311

It appears to reference the 
[Perfect Sound](https://bigbookofamigahardware.com/bboah/product.aspx?id=1128)
sampler cartridge, which was released
in [three revisions](http://amiga.resource.cx/exp/perfectsound) in 1986, 1987,
and 1988. The author likely created all the game's sounds by themself.
