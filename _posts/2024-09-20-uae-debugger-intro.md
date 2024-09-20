---
title: Introduction to the UAE debugger
categories: guide
---

The UAE (WinUAE, FS-UAE) debugger is a useful tool for understanding what's
happening in an Amiga program. It can also be used to cheat at games by giving
yourself unlimited lives or something. This articles provides a basic
introduction to its use.

### Enabling the debugger

The debugger is disabled by default, and must be enabled in settings. In FS-UAE,
add this line to your config file:

    console_debugger = 1

This will require you to restart the emulator.

During play, you can switch to the debugger at any point. Depending on the
emulator, the keypress is `F12+Shift`, `F12+End`, or `F12+D`. This will pause
the emulation and open the debugger either in a separate GUI window (WinUAE) or
the console window that you launched the emulator from.

### Commands

This article will list only some of the main commands.

#### g - Resume

The command `g` will resume the emulation.

#### ? - Help

Another important command, this will show a list of commands.

#### s - Search

Search for the location of text or data in memory. Suppose for example that you
want to find the address of a character name in memory. Put it in quote marks
like so:

    s "RATT"

Alternatively, to search for numbers, prefix them with `!` for decimal or `$`
for hexadecimal. You will also want to include a second for start address, which
can be 0. Suppose you're searching for your current score of 48456:

    s !48456 0

#### C - Cheat

A limitation of `s` is that for small numbers like single digits, you are likely
to find several thousand entries. "C" is useful for this. Suppose you have 5
lives:

    C !5

It will find every "5" in memory, which may be hundreds. Now type `g`, lose one
life, and switch to the debugger again:

    C !4

This will find every one of the previous search results which has now changed to
the new value. You can keep doing this 

#### W  - Write

Uppercase W is used to write values into memory. Useful to give yourself 99
lives, change text, or something. The first parameter is the address, and the
rest are bytes or text.

For example, maybe I want to re-name the main character. First, find the address
of the character's name:

    s "RATT"

Then update it:

    W $18dd0 "DAVE"

Perhaps Dave is hungry, so I put a rabbit pie (code `$29`) in his inventory:

    W $18e3e 00 29

#### m - Memory dump

Read the data at a given address. First parameter is the address, second
parameter is the number of lines at 16 bytes per line.

    m $18dd0 1

#### d - Disassemble

Memory dump, but show the bytes decoded as 68k assembly instructions.

#### w - Watch

Lowercase "w" sets a watchpoint at memory. The program will automatically stop
and switch to the debugger whenever the specified memory is accessed. This is
very useful when you know what memory location holds the data you're interested,
and you want to find out what code accesses it. It can also be used to stop when
code execution reaches a certain address.

For example, set watchpoint 1 to see when the 4 bytes at memory location 0x18dd0
are read or written to:

    w 1 $18dd0 4

Or to trigger only when it's written to:

    w 1 $18dd0 4 W

To clear the watchpoint, just set it with no parameters:

    w 1

If you're writing your own assembly language program, one way to trigger the
debugger intentionally is to write it, like so:

    clr.w $100

Then in the debugger:

    w 1 100 4

#### t - Step through instructions

Step one instruction forward at a time.

#### r - Show registers

This will show the current state of the data registers, address registers,
CPU flags, program counter, etc.
