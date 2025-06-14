---
title: "Intro to 68k assembly language"
categories: guide
---

The following is a brief summary of 68000 assembly language. I'm not an expert
at 68k assembly myself, but I felt a need for a simple guide explaining the
basics to people learning the language for the first time, who may be baffled by
the highly technical language used by some documents on the topic. A further
reading list appears at the end of the article who wish to learn in more detail.

1. Table of Contents
{:toc}

### Introduction

According to [The Art of War](https://www.gutenberg.org/ebooks/132), all warfare
is based on deception. When our forces are weaker than the enemy, we must make
him think we are stronger (so that he will not attack us); when we are stronger,
we must make him think we are weaker (so that he underestimates us), and so on.
By these means, the enemy's plans will be predicated on inaccurate information,
leading to incorrect deductions, resulting in his failure.

All programming is based on truth. The smallest possible unit of a computer's
memory is the bit, which has only two possible states: 1 (meaning true), and 0
(meaning false). If we set a bit to 1, it remains 1 until we set it to 0; if we
set it to 0, it remains 0 until we set it to 1.

All data which can be stored in a computer's memory is ultimately composed of
bits. Traditionally, they are arranged into groups of eight bits, known as
bytes. Each byte can therefore contain any one of 2<sup>8</sup> different
combinations, or 256 possible values, such as a number between 0 and 255.
Bytes, or combinations of bytes, represent all data which can be stored in a
computer's memory.

Computer programs are comprised of instructions, which are also represented as
bytes. Each instruction used by the 68000 CPU consists of at least two bytes,
and is represented by a text-based syntax known as _assembly language_, which is
converted into 68000 bytecode with software known as an _assembler_.

### Your programming environment

Most people learning 68000 assembly nowadays do so for one of two reasons.

If you have to learn it for a university class, you have probably been assigned
a 68k simulator tool such as
[EASy68K](https://web.archive.org/web/20220721133417/http://www.easy68k.com/)
or [BSVC](https://github.com/BSVC/bsvc). Use that and follow the documentation
for those tools.

If not, it's probably because you want to program for a computer system which
used the 68000-series CPU, or analyze code written for such a system. Usually,
that means games for the Commodore Amiga, Sega Mega Drive/Genesis, Atari ST, or
another computer of the 1980s to mid-1990s era. Reaktor's
[Crash course to Amiga assembly programming](https://www.reaktor.com/blog/crash-course-to-amiga-assembly-programming/)
describes configuring an Amiga emulator with a development environment for
[vasm](https://web.archive.org/web/20220627163104/http://sun.hasenbraten.de/vasm/),
an up-to-date assembler.

### The CPU

The 68000 CPU has seven data registers, referred to as D0 to D7, each of which
can be used to store a 32-bit value; i.e. four bytes.

It also has seven address registers, A0 to A7, which also store 32-bit values,
except that these are for storing the addresses of locations in memory. A7 is
also referred to as SP, the Stack Pointer.

There is the program counter, PC, which stores the address of the current
instruction being executed; essentially, the location of the current line of the
program in memory.

Finally, there is the condition code register (CCR), which contains five bits
used as "flags" to represent "condition codes", or important information about
the last instruction which executed. Each is "set" (i.e. set to 1) if certain
conditions are met; otherwise, set to 0:

X
: Extend.

N
: Negative. Set if the result of the last calculation is negative, meaning
specifically that the most significant bit (i.e. leftmost bit) is set to 1. For
example, if a byte is `0000 0000` (i.e. decimal value of 0) and you subtract
one, it will set the byte to `1111 1111` (i.e. 255 or -1) and set the N flag.

Z
: Zero. Set if the result is zero.

V
: Overflow. Set if the result is too big to fit in the value; e.g. trying to
store a number larger than 255 in a byte.

C
: Carry.

### Addresses and labels

Each byte of memory is referred to by a numeric location, known as its address.
The very first byte in memory is referred to by the address `$0000 0000`, the
second is `$0000 0001`, and so on.

Any line in a program can be prefixed with a label, which can be used throughout
the program as a convenient synonym for that location in memory. This works much
like variable names in high-level languages. For example:

```
START:
    ADDQ.L  #1,SCORE
    RTS
SCORE:
    DC.L    $00000000
END
```

### Instructions

There are many instructions, of which the most common and important are detailed
below. Once you get the hang of these, it should be easy to look up any
unfamiliar codes in various sources of documentation (see "further reading").

Many instructions are suffixed with a size, determining how much data they
operate on. For a standard 68000 CPU, this can be `.B` (byte), `.W` (word,
meaning two bytes) or `.L` (long, meaning four bytes). You may also see `.S`
(short), also meaning one byte.

Instructions can also be written in lowercase, and are typically indented with
one tab.

#### ADD

Add two numbers. One value is a data register; the other can be a memory
location or a register. It takes the numbers from each location, adds them, and
stores them in the second location.

For example, to add the value currently in data register D1 to the four-byte
value referred to by the label SCORE:

```
    ADD.L   D1,SCORE
``` 

Or, to add SCORE to data register D1:

```
    ADD.L   SCORE,D1
``` 

Or, add two registers:

```
    ADD.L   D0,D1
```

Or add to the number stored in an address register:

```
    ADD.L   D0,(A1)
```

Or do the same and increment the address register by the operand size afterward:

```
   ADD.L    D0,(A1)+
```

Or refer to the address by an offset, such as to add D0 to the value held ten
bytes after the address held in A1:

```
    ADD.L   D0,(10,A1)
```

#### ADDA

Like ADD or ADDI, but the second value is an address register.

```
    ADDA.L  D1,A1
    ADDA.L  #$00000140,A1
```

#### ADDI

"Add immediate". Like ADD, but adds a raw number, rather than taking the number
given in a memory location. Note that the prefix "#" refers to a decimal number,
while the prefix "#$" refers to a hexadecimal number. For example, suppose you
want to add 100 to "SCORE", and add 1 to D0:

```
    ADDI.L  #100,SCORE
    ADDI.L  #1,D0
```

#### ADDQ

"Add quick". Like ADDI, but only adds a number from 1 to 8. The advantage is
that it's faster. Useful for things like incrementing by one. For example, to
add 10 the memory address A0 in two steps:

```
    ADDQ.L  #8,A0
    ADDQ.L  #2,A0
```

#### AND

Performs a logical AND operation on the two values, and stores it in the second
value. An AND operation compares each bit and sets the resulting bit to 1 if
both bits are true; otherwise, sets the bit to 0. Useful if you're working on
bit-based data; e.g. to save memory, some games would store multiple pieces of
true/false data as individual bits, and computer graphics code also uses this.
Like with ADD, either value can be a register or an address.

The Python equivalent is the `&` operator.

#### ANDI

Like AND, but give an immediate value.

#### ASL

Arithmetic shift left. Essentially multiplies the value by 2<sup>n</sup>. The
first value is the number of times shifted, and the second is a data register.
The Python equivalent is `<<`. For example, to multiply the value in D0 by
2<sup>4</sup> (16), equivalent to D0 << 4:

```
    ASL.W  #4,D0
```

#### ASR

Arithmetic shift right. Like ASL but essentially divides by 2<sup>n</sup>,
discarding remainders. Equivalent to Python `>>` operator. For example, quickly
divide by two:

```
    ASR.W  #1,D0
```

#### Bcc

Branch based on condition code ("cc"). An important instruction which fulfils
the function of things like "if" statements in high-level languages. The "cc" is
replaced with a two-letter condition code. It checks if the specified condition
code is true, and skips ahead to the specified address if it is true, otherwise,
it continues as normal.

For example, this code tests if D0 and D1 are equal (the CMP instruction), which
will set the Z flag if true. BEQ checks for the Z flag. If set, the program
skips to `_CORRECT`. Otherwise, it continues from the ADDQ line.

```
    CMP.L   D0,D1
    BEQ.S   _CORRECT
_INCORRECT:
    ADDQ.L  #1,D0
    RTS
_CORRECT:
    RTS
```

The main forms of this instruction:

BEQ
: Branch if equal to zero (Z set). Often used in conjunction with TST or
CMP. BEQ can also be thought of as "branch if equal", since for example `CMP.L
D0,D1` will set Z if both are equal, thus causing a subsequent BEQ to branch.

BNE
: Branch if not equal (Z unset). Inverse of BEQ.

BMI
: Branch if minus (N set).

BPL
: Branch if positive (N unset). Zero counts as positive.

BGT
: Branch if greater than zero.

BLT
: Branch if less than zero.

BGE
: Branch if greater than or equal to zero.

BLE
: Branch if less than or equal to zero.

#### BRA

Unconditional branch. Like Bcc but always branches regardless of condition
codes.

#### BSR

Branch Subroutine. Adds to the address of the next instruction to the stack,
then branches. The main use of this is that when the program next encounters a
RTS (return) instruction, it returns to pick up where it left off.

```
    MOVE.B  #100,D0
    BSR.W   _RandInt  ; a subroutine defined elsewhere
; program continues here after running _RandInt
    BEQ.L   _Explode
```

#### CLR

Clear. Sets the specified value to zero.

```
    CLR.L  D0
    CLR.L  SCORE
```

For efficiency reasons, you will sometimes see alternative means used to clear a
register or address, such as subtracting it from itself or MOVEQ #0.

#### CMP

Compare. Subtracts the first value from the second value. However, it doesn't
store the result or change the values. It only sets the condition codes. The
first parameter is a register or address, while the second parameter must be a
data register. For example:

```
    CMP.L  D0,D1
    BEQ.S  _EQUAL
    BRA.S  _NOT_EQUAL
```

#### CMPA

CMP but the second value is an address.

#### CMPI

CMP but the first value is an immediate value, i.e. a raw number.

```
    CMPI.L  #0,LIVES
    BEQ.S   _GAMEOVER
```

#### DBcc

Decrement and branch until the condition code is set or the counter reaches
below zero. Fulfils a similar function to for loops or while loops in high-level
languages.

The first parameter is a data register which holds the counter, and the second
is an offset which it will branch to. Each time the instruction is executed, it
decreases the counter by one. It then branches to the offset, unless either the
condition code is set, or the counter has just been reduced to -1. The condition
codes are the same as for Bcc, but often you see this as DBF or DBRA, which
means the loop will continue until the counter reaches -1.

For example, this code will run `_SpawnEnemy` 4 times:

```
    MOVEQ  #3,D7
_Loop:
    BSR    _SpawnEnemy
    DBF    D7,_Loop
```

Note that whatever you set the counter to, it will run 1 time more than that
number, since it runs through the section one time before it reaches the DBF. In
the example above, it will run once with D7 equal to 3, 2, 1, then 0. Only 

#### DIVS

Division (signed).

#### DIVU

Division (unsigned).

#### JMP

Jump. Like a branch, but takes an address rather than an 16-bit offset, allowing
you to jump to code farther than 32 KB away. In practice, since you specify both
addresses and offsets as labels when writing assembly, BRA and JMP appear to
work the same way.

#### JSR

Jump Subroutine. Same as BSR.

#### LEA

Load Equivalent Address. Loads the address of the first value into the second
value, which is an address register.

```
    LEA     SCORE,A1
    MOVE.L  (A1),D0
    RTS
SCORE:
    DC.L    #$00000000  ; whatever the address of this is, it's loaded into A1
```

#### MOVE

An important instruction to copy data from one register or address to another
register or address.

```
    MOVE.L  D0,D1
    MOVE.L  SCORE,D0
```

#### MOVEA

MOVE but the second value is an address register.

#### MOVEQ

Move Quick. Like MOVE, but the first value is an 8-bit number, and the second is
a data register. Good for moving small numbers efficiently. The result is always
a Long. Sometimes used as an alternative to `CLR`.

```
    MOVEQ.L  #0,D0
```

#### MULS

Multiply signed.

#### MULU

Multiply unsigned.

#### NEG

Get the negative version of the number by subtracting itself from zero. The
value given is an address or data register.

#### NOP

No Operation. An instruction which does nothing. Useful when hex editing an
executable where you need to delete some instructions but you have to keep
everything else at the same address as usual. In hexadecimal, it's written
`4e71`.

#### OR

Like AND, but logical OR instruction. Takes two values in registers or
addresses, ORs them together, and stores the result in the second value.  OR
compares both input values for each bit, and if either has a 1, the output has a
1, otherwise it's a 0. Equivalent to the Python `|` operator.

#### ORI

OR Immediate. However, when you see this in a disassembly, it's usually an error
where data has been misidentified as code. This is because the bytes `0000 0000`
disassemble to `ORI.B #$00,D0`.

```
    ORI.B  #$00,D0  ; 0: 00000000   ; usually incorrect
    DC.L   #$00000000               ; usually correct
    DS.L   1                        ; same
```

#### RTS

Return. Equivalent to a "return" in Python or other languages. Returns to where
the last JSR or BSR left off.

#### Scc

Set byte to "true" if condition code is true, "false" otherwise. In this case,
setting a byte to "true" means setting all its bits to a 1, which is also
equivalent to 255 unsigned or -1 signed; false sets all bits to 0, meaning 0.
The counter-intuitive result, then is that true and false are -1 and 0 instead
of 1 and 0.

You will often see this as `ST` or `SF` (set if true / set if false). ST always
sets the byte to true, i.e. all bits set to 1. SF always sets the byte to false,
or zero.

```
    SF  Lives
```

#### SUB

Subtract. Like ADD but for subtraction. Takes two values, either of which can be
an address or data register. Subtracts the first number from the second number
and stores the result in the second number.

```
    SUB.L  D0,D1  ; D1 = D1 - D0
```

A trick to set a value to zero is to subtract it from itself:

```
    SUB.L  D0,D0
```

#### SUBA

SUB but the second value is an address.

#### SUBI

SUB but the first value is an immediate number.

```
   SUBI.L   #1,LIVES   ; lose 1 life
```

#### SUBQ

SUBQ (Subtract Quick) is like SUBI but only subtracts a number from 1 to 8, so
it's slightly faster.

#### TST

Test. Compare a value with zero and set the condition codes accordingly (N if
negative, Z if zero). Mainly used in conjunction with BEQ or BNE to branch
depending on whether the byte is zero, i.e. false.

```
    MOVEQ  #0,D0
    TST.B  D0
    BEQ.S   _Zero   ; this branch will always be taken
```

### Further reading

- [How Machine Language Works](https://www.youtube.com/watch?v=HWpi9n2H3kE) (YouTube)
- [Bowen's 68000 Summary Card](https://textfiles.vistech.net/programming/CARDS/68000)
- [MarkeyJester's Motorola 68000 Beginner's Tutorial](https://mrjester.hapisan.com/04_MC68/)
- [m68k-instructions-documentation](https://github.com/prb28/m68k-instructions-documentation)
- [68k.hax.com](https://web.archive.org/web/20160416075724/http://68k.hax.com/)
- [MC680x0 Reference 1.1](https://oldwww.nvg.ntnu.no/amiga/MC680x0_Sections/index.HTML)
- [Motorola M68000 Family Programmer's Reference Manual](https://www.nxp.com/docs/en/reference-manual/M68000PRM.pdf) (PDF)
- [Crash course to Amiga assembly programming](https://www.reaktor.com/blog/crash-course-to-amiga-assembly-programming/)
- [How to Work with Motorola 68000 assembly](https://info.sonicretro.org/SCHG_How-to:Work_with_Motorola_68000_assembly)
- [Tutorials of The Complete Amiga 68000 Assembly Hardware Programming & Development Course](https://www.youtube.com/playlist?list=PL-i3KPjyWoghwa9ZNAfiKQ-1HGToHn9EJ) (YouTube)
- [MatchPatch](https://github.com/tetracorp/matchpatch-amiga), a contemporary
  example of a game written in 68k asm released in 1990
