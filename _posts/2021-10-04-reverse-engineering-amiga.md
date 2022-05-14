---
title: "Reverse-engineering Amiga games"
categories: guide
---

All manner of secrets hide within classic video games: undiscovered cheat codes,
cut content, undocumented game mechanics, potential speedrun exploits, and
opportunities for modding or translation projects. The following guide offers
and introduction to reverse-engineering and exploring Commodore Amiga games in
particular.

1. Table of Contents
{:toc}

### Avoid duplicating effort

The first step in any reverse-engineering project should be research. It's
entirely possible that someone has already analyzed the game you're interested
in, or even better, that the original source code has been released. In some
cases the original author or company may have the source, and may be convinced
to release it.

### Disassembly

For optimal performance, nearly all commercial Amiga games were written in 68000
assembly, the closest human-readable language to the CPU's native machine code.
Just as an _assembler_ once turned the original programmer's source code into an
executable program, a tool called a _disassembler_ can recreate the source code
from the program (though with certain limitations).

Even games written in other languages like C or AMOS Basic will be reversed to
assembly language. There's no known way to reverse a compiled AMOS program back
into AMOS (and its assembly output is really ugly).

#### IRA

One of the best Amiga-specific disassemblers is the freeware tool
[IRA](https://ftp.uni-erlangen.de/aminet/dev/asm/ira.lha). This runs natively on
Amiga, but it can also be compiled for Windows, Mac and Linux, which is
recommended since it runs a lot faster.

If for example the game executable you're analyzing is named MatchPatch, run
something like this:

    ira -A -KEEPZH -NEWSTYLE -COMPAT=bi -PREPROC MatchPatch

"Preproc" attempts to work out which bytes are 68k instructions and which are
data, although it's not perfect. It creates an assembly language source file,
`MatchPatch.asm`, and a config file, `MatchPatch.cnf`. If you want to get it
more perfect, you can manually edit the .cnf to change the start and end points
of the code sections, then re-run it with -CONFIG:

    ira -A -KEEPZH -NEWSTYLE -COMPAT=bi -CONFIG MatchPatch

Identifying misidentified sections is something of an acquired skill. Signs of
code misidentified as data include the code for common instructions appearing
`DC.L` lines (e.g. `4e75`) or sometimes data areas containing labels.  Signs of
data misidentified code include a lot of `EXT_` declarations at the start of a
program, or code sections with a lot of `ORI #0` ($0000).  Strings of numbers
from hexadecimal $41 to $7A are often unidentified ASCII text. The `-A` option
is good for helping you to familiarize ourself with the numeric equivalents of
instructions.

See also this EAB thread on using IRA:
[Small IRA Tutorial](https://eab.abime.net/showthread.php?t=101408).

#### Ghidra

[Ghidra](https://ghidra-sre.org) is a powerful reverse-engineering tool released
in 2019. It can handle the the 68000 platform, and thanks to a plugin called
[ghidra_amiga_ldr](https://github.com/lab313ru/ghidra_amiga_ldr), it can
specifically handle Amiga executable files. It can also interpret disassembled
code as C, which won't give you an accurate representation of the game's source
code if it was originally written in Assembly (as most Amiga games were), but it
can give you a representation of the code in a high-level language that may aids
understanding of the program if you're more familiar with C-inspired languages
like Java.

As of May 2022, Ghidra is now my preferred tool for analyzing Amiga games. I've
written an introductory tutorial to using Ghidra for this purpose:
[Intro to Amiga reverse-engineering with Ghidra](../intro-amiga-ghidra.html).

### Introductory analysis

At this point, it becomes clear that you need to know at least the basics of
68000 assembly language. Introductory tutorials include
[MarkeyJester's 68k Tutorial](https://mrjester.hapisan.com/04_MC68/Index.html)
and redhotsonic's [Work with Motorola 68000 assembly](https://info.sonicretro.org/SCHG_How-to:Work_with_Motorola_68000_assembly).
Useful reference guides include
[NVG's 68k docs](https://oldwww.nvg.ntnu.no/amiga/MC680x0_Sections/alphabetical.HTML),
[68000 Instruction Set Summary](https://textfiles.meulie.net/programming/CARDS/68000),
and the
[68000 Programmer's Reference Manual](https://www.nxp.com/docs/en/reference-manual/M68000PRM.pdf).

The limitations of disassembly are also obvious. The true original source code
to a game contained meaningful variable names, label names, and comments, which
would make it much easier to understand the program's meaning: see the original
[MatchPatch source code](https://github.com/tetracorp/matchpatch-amiga/blob/main/MatchPatch.S.asm)
for an example of this. The assembly process usually stripped names and
comments, meaning that these will not appear in a disassembly.

However, on occasion you may get lucky and find a program with variable names
intact. This usually occurs by mistake when the programmer creates a debug build
with the symbol table enabled for testing, and forgets to disable it again when
making the final release build. Some games with this include the CD32 versions
of _Nigel Mansell's World Championship_ and _Zool 2_.

In most cases, you will have to rename labels yourself once you discover their
meaning. Find-replacing one throughout the document and looking for other
instances will let you identify related labels; e.g. once you've identified the
the variable for Score, you can look for other things for events which increase
Score.

The more elegant method is to only add variable names and comments to the `.cnf`
file, then re-run `ira`. See `ira_config.doc`. Useful directives include SYMBOL
(rename a label), LABEL (add a new label), and COMMENT and BANNER (place a
comment). The method then is to continually discover new label definitions, add
them to the configuration, re-disassemble the program with the option `-CONFIG`.

### Finding the interesting features

Even a very simple Amiga game can have thousands of lines of code, but you're
mainly interested in identifying the code locations referring to relevant game
mechanics, and these can be a good starting point to explore the function
further. Here are some things to look for:

- Standard Amiga library calls: Text strings in the game may reference library
  files, such as `graphics.library` or `dos.library`. Early on in a program you
  will see references to ABSEXECBASE ($4) followed by a jump to an offset; e.g.
  `JSR (-30,A6)`. Calls to ABSEXECBASE are offets of `exec.library`, and you
  will often see this to load other libraries with the OpenLibrary function,
  i.e. `JSR (-552,A6)`. A fullly documented list of major library offsets and
  hardware registers appears in
  [Mapping the Amiga](https://textfiles.meulie.net/programming/AMIGA/mapamiga.txt).
- File read: Calls to `dos.library` functions Open `JSR (-30,An)` and
  Read `JSR (-42,An)` will show files read from disk. This can identify memory
  locations; e.g. a file in _Heimdall 2_ called `worlds/nif2txt.dat` is probably
  part of the text for Niflheim, and wherever it reads to is a game text field
  variable.
- File write: Calls to `dos.library` Write `JSR (-48,An)` in games are almost
  always either save games or highscore files. These are critical because data
  written in save game holds the persistent game state, so we can identify the
  memory locations which hold mechanical data (inventory, character statistics,
  etc). Conversely, once you know the memory locations, you can fully document
  the save game format, and perhaps use this to write a save game viewer/editor.
- Joystick/mouse inputs: JOY0DAT ($DFF00A) and JOY1DAT ($DFF00C) are both
  two-byte Amiga values for reading the joystick and mouse ports. They're
  documented in _Mapping the Amiga_.
- Keyboard inputs: Keyboard input can be read from $BFEC01. A lot of Amiga games
  use the keyboard to type cheat codes, even if they exclusively use joysticks
  for normal game control.
- Audio: References to the four audio channels AUD0LCH to AUD3LCH ($DFF0A0 to
  $DFF0D0) identify code which makes sound effects. If you can extract the
  referenced sound effects (often raw mono audio playable in Audacity), you can
  tell what code it's in (e.g. a bullet shoot sound means you're in the bullet
  shoot code).
- Text strings: Use the IRA option `-TEXT=1` or the program `strings` to help
  find text in a program (although `strings` often finds a lot of junk).
  Certain text strings can identify file formats; e.g. "FORM" (IFF format
  header), "ILBM" (image) "8SVX" (audio). Others can identify game functions.
- Known numbers: Your game may have very specific large numbers, such as the
  purchase price of an in-game item. Round decimal numbers like 1,000 or 10,000
  tend to be variables for game elements. Bear in mind that these will probably
  appear in hexadecimal.
- Random number generator: This can lead us directly to game mechanics. Amiga
  games commonly seeded a pseudorandom number generator using the current
  position of the CRT beam. Look for references to VHPOSR ($DFF006) or VPOSR
  ($DFF004). The RNG routine also tends to use ROXR instructions to shuffle up
  the numbers. Identify the RNG routine from there, and anything referencing it
  is likely to be a game mechanic.
- VBlank wait: References to VPOSR and VHPOSR can also in a a "wait for vertical
  blank", used to wait for the 50Hz or 60Hz screen refresh before beginning the
  next frame. This can help to identify the main game loop.
- Mathematics: Look for MULU and DIVU instructions. These are sometimes used for
  game mechanics.

### Modifying the game

You can experiment by changing the code. Use a hex editor to search for a
certain series of bytes (if you used the `-A` option with `ira` each line in the
disassembly shows you the raw bytes, and certain sequences will be unique within
the file and can be used as landmarks). 

For example, suppose you see a number which is set to 3 at game start, and you
suspect this is the starting number of lives. Find it in the program binary and
hex edit it 5, then play the game again. If you start with 5 lives, you've found
the value. You can now use this to, say, give yourself a large number of lives
to cheat, or find other code which references it (e.g. life pickups, and from
there the general item pickup code, and from there the list of pickups, etc).

You can do a similar thing with emulator save states, which can be quicker than
reloading the entire game.

A more elaborate method of program modification involves reassembling the source
code. The documentation for `ira` recommends using
[vasm](http://sun.hasenbraten.de/vasm/) like so:

    vasmm68k_mot -no-opt -Fhunkexe -nosym -O MatchPatch MatchPatch.asm

In theory, this will create a functionally identical binary to the original. You
can omit `-nosym` to create a version of the binary with a symbol table, which
may aid debugging.

A particularly useful setup here is to configure your emulator to mount a folder
on the host PC as a hard disk, which the Amiga side can then launch your
modified games from directly.

### Emulator debugging

The Amiga emulator WinUAE, and derivatives like FS-UAE, include a useful
debugger which lets you freeze the emulation and read/write memory. There are
various WinUAE debugging tutorials, such as this thread 
[Basics of debugging ASM in WinUAE?](https://eab.abime.net/showthread.php?t=70007)

While the emulator is running, trigger the debugger by hitting shift-F12
(WinUAE) or F12-D (FS-UAE). You may have to first enable debugger in the
settings. In the debugger, type `?` or `h` to show a list of commands.

Search for values in memory with `s`. For example, to find a string called
"Loading" anywhere in memory, type `s "Loading" 0`, or to find the number
10,000, type `s !100000 0` or `s $186a0 0`.

Dump a section of memory as data with `m`, e.g. `m 400867EB`. Dump it as
disassembled code with `d`, e.g. `d 400867EB`. Save a chunk to disk with `S`,
e.g. `S dump.txt 400867EB $10000`.

Write into memory with `W`, e.g. `W 400867EB 10`. Write to a register with `r`,
e.g. `r D0 $00000000`.

Creat a watchpoint for when a certain memory location is accessed, with
lowercase `w`. It will automatically trigger the debugger when this occurs.  For
example, `w 1 400867EB 1`.

Return to the game with `g`.

### NDOS disks

Finding the executable file can be tricky for NDOS disks (i.e. disks using a
non-standard format, generally used by commercial games to prevent disk
copying).

One solution is to just try to disassemble the entire ADF. Another is to start
the game in an emulator, make a save state, and disassemble that. You need to
configure the emulator to make uncompressed save states first, and it's
recommended to set the emulator to have the minimum amount of RAM necessary
(usually 1MB chip with no fast RAM) to limit the size of the memory. You also
want to boot from the game disk to avoid having Workbench in your disassembly,
which will only confuse analysis.

Some games received a re-release for CDTV or CD32. These use a standard CD-ROM
format and can be read freely. Antipiracy was not a priority for CD32 games
since consumer-level CD copying was impractical in 1993.

### Packed executables

Some executables are compressed. Disassembling such a program will give the
impression of a program with a very short code section followed by a very long
data section. This might be done either to fit a larger program on a single
disk, or to obfuscate the program to make it harder for pirate groups to strip
copy-protection code.

[xfdMaster](https://ftp.uni-erlangen.de/aminet/util/pack/xfdmaster.lha) can
unpack nearly any format.

If this fails, load the program normally and disassemble from a save state or
memory dump.

### Sprite extraction

Extracting graphics from Amiga games is an entire topic in itself.

[Maptapper](https://codetapper.com/amiga/maptapper/) is the standard tool for
finding sprites and graphics in Amiga games. You can pull data directly from the
disk or from a memory dump. It can be tricky to use, but something it will do is
let you see the location of graphical data within an executable, which can help
you to make labels.

[amostools](https://github.com/kyz/amostools) may let you extract data from ABK
files.

### Disk and file analysis

Other files on the game disks often contain data such as graphics, sound,
maps, levels, and saved games. Decompress them if necessary with xfdDecrunch.

[DiskSalv](https://ftp.uni-erlangen.de/aminet/disk/salv/DiskSalv.lha) can,
occasionally, find leftover data which does not appear in the file listing. This
can occasionally find things like source code, unused game data, or fragments of
older versions of the game executable.

### Background research

A lot of Commodore Amiga games have little to no online presence today, and it
is possible that your reverse-engineering project will be the most in-depth
resource ever created on the subject. If you really want to perform the ultimate
analysis, look into other related information which you might collect for the
interest of readers.

Multiple versions of the same game may be available, including free demo
versions distributed on Amiga magazine coverdisks, bugfix releases, alternate
language versions, sequels, or ports to other platforms. Games written for Amiga
500 may have received an AGA port (A1200) or a CD release for CDTV or CD32. You
can find and compare them for differences.

Search for contemporary magazine articles at
[Amiga Magazine Rack](https://amr.abime.net) (AMR) and
[Archive.org](https://archive.org). Discover what people were saying about the
game at the time, and help your readers to understand the context that may not
be obvious today. For example, magazine articles tell us that _K240_ was
widely understood as a "god game" like _Populous_ (1989), because the current
genre of "real-time strategy" was not yet defined by _Dune II_ (1993) and
_Command & Conquer_ (1995).
