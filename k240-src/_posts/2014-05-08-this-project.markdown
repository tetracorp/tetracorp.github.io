---
layout: post
title: "About This Project"
categories: about
---

Exploring K240 is a project to disassemble and decipher the undocumented
game mechanics of K240, the space exploration game released on
Commodore Amiga in 1994.

### Why explore K240?
K240 was one of my favourite Amiga games of all time. Despite a heavy
game manual, many of the game's underlying rules or mechanics were a
complete mystery to the player. How much damage does each weapon do?
How many hit points does each building have?

Twenty years later, this project sets out to find those answers.

### What can we learn?
The biggest questions this projects seeks to answer:

1. How does ship combat work? (How do ships choose their targets, how
much damage does each weapon deal, and what effect have hardpoints like
Deflector and Warp Generator?)
2. How does ground combat work? (How much damage does each weapon do,
how does fire spread, how many hit points does each building have,
and how does Vortex operate?)
3. How do missiles work? (What is their damage and effect?)
4. How do colonies operate? (What affects population growth, what effect does
radiation have, what effect does population have,?)
5. How do buildings work? (What hitpoints do each building have, what
effect does each building have?)
6. How do aliens differ? (What are their tactics and  AI routines, do
aliens play by the same rules as Terrans regarding cost and mining,
what are the stats of their ships, missiles and buildings, and how does
each alien differ? Does fire really affect Swixarans more, and why do
abandoned Ore Eater colonies explode?)
7. What are the differences between K240 v1.886 and the bug-fixed version
K240 v2.000?

### How to explore K240?
I began by running the main game executable through an Amiga disassembly
program called IRA, which turns an Amiga executable file into 68000
assembly language.

The result is difficult to understand since it's over 40,000 lines of
low-level code and has no comments or even variable names. Some useful
approaches have helped to make sense of the code:

1. Searching for known numbers or strings, such as game text or the
known price of a ship. This makes it easy to zero in on code relating
to certain functions.
2. Find-replacing variable names throughout the code and adding comments
once a fuction has been understood. This sometimes makes other parts clearer.
3. Identifying the random number generator function. This is typically
used to "roll dice" or simulate chance, and makes it very easy to zero
in on game rules.
4. Identifying system calls to the AmigaOS functions, particularly
Open(), Read() and Write(). By identifying what parts of memory are
written and read by the save game function, we can tell the entirety
of what holds the current game state. We can also tell how the alien
data files are stored based on how they're read into memory.

Another useful tool is WinUAE, which has a built-in debugger and can
generate save states during a game.
