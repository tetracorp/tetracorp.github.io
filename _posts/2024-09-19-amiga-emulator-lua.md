---
title: Scripting an Amiga emulator with Lua
categories: guide
---

FS-UAE began adding an experimental Lua scripting layer around 2013, although it
is incomplete, disabled by default, and almost completely undocumented.
Fortunately, it's possible to re-enable it and use it to write scripts to aid in
the real-time analyis of Amiga software... or just to cheat at games.

### Building FS-UAE with Lua

You will need a small amount of technical skill here, but nothing unusual for
someone who is already analyzing Amiga game code.

Grab the source code of the
[latest stable release](https://github.com/FrodeSolheim/fs-uae/releases)
of FS-UAE from GitHub - I tested this as working on version 3.1.66. Next, grab
[fs-uae-lua.diff](https://github.com/tetracorp/tetracorp.github.io/blob/main/tools/fs-uae-lua.diff),
a patch based on
[cnvogelg's pull request](https://github.com/FrodeSolheim/fs-uae/pull/60) from
2015 which adds a Lua shell. Put it in the directory with the source code and
apply it using git:

    git apply fs-uae-lua.diff

Next, follow the FS-UAE documentation on compiling for your platform, using the
`--enable-lua` directive. It should go something like this:

    ./bootstrap
    ./configure --enable-lua
    ./make

If all goes well with no errors, this will produce an executable `fs-uae`.

### Using the Lua shell

In your fs-uae configuration, set this option:

    lua_shell = 1

Run the patched `fs-uae` as normal. Open a telnet window and connect to
localhost in port 6800:

    telnet 127.0.0.1 6800

This places you in a sort of Lua interpreter window.
If you have now discovered that you need to learn Lua, please consult the
[Lua Reference Manual](https://www.lua.org/manual/5.4/).

### Loading scripts at startup

If FS-UAE was compiled with `--enable-lua`, it will load an run a file named
`default.lua` from the current working directory at startup.

It appears that the startup script and the shell are separate; i.e. functions
defined in `default.lua` aren't available in the shell, and the lua `require()`
function is also missing. However, you can still define scripts at startup which
trigger callbacks.

### FS-UAE Lua API documentation

The following function names assume you have installed the Lua shell patch.

#### Functions

fsemu.load_shader()
: 

fsemu.log()
: 

fsemu.set_frame_position_and_size()
: 

fsemu.set_scale()
: 

fsemu.set_shader()
: 

fsuae.cdrom.get_file(filename)
: 

fsuae.cdrom.get_num_drives()
: 

fsuae.cdrom.set_file(filename)
: 

fsuae.floppy.get_file(filename)
: 

fsuae.floppy.get_num_drives()
: 

fsuae.floppy.set_file(filename)
: 

fsuae.get_input_event()
: 

fsuae.get_rand_checksum()
: 

fsuae.get_save_state_number()
: 

fsuae.get_state_checksum()
: 

fsuae.send_input_event()
: 

fsuae.set_input_event()
: 

uae.exe()
: UAE remote CLI.

uae.log()
: 

uae.peek_u16(addr)
: Read 16-bit value from memory location without any side-effects.

uae.read_config()
: 

uae.read_u16(addr)
: Read 16-bit value from memory location.

uae.read_u8(addr)
: Read 8-bit value from memory location.

uae.write_config()
: 

uae.write_u16(addr, value)
: Write 16-bit value to a memory location.

uae.write_u8(addr, value)
: Write 8-bit value to a memory location.

quit()
: Quit the Lua shell.

#### Tables

uae.custom
: A table of the custom chip registers and their memory locations. For example: 

    print(string.format("$%x",uae.peek_u16(uae.custom['COLOR01'])))

#### Callbacks

Define a function by this name and and it will be called whenever the relevant
event triggers.

on_fs_emu_render_frame()
: 

on_fs_uae_input_event
: 

on_fs_uae_load_state, on_fs_uae_save_state, on_fs_uae_load_state_done, on_fs_uae_save_state_done
: Called whenever you load or save a save state.

on_fs_uae_read_input
: Only triggers for the first input handler run per frame.

on_uae_config_changed()
: 

on_uae_vsync()
: Called on vsync; i.e. once per frame.

### Uses for the scripting interface

One use is to show data in memory or custom registers. Here is a one-liner which
will dump the current palette:

    for n=0,31 do print(string.format("COLOR%02d: $%03x",n,uae.peek_u16(uae.custom['COLOR00']+n*2))) end

Unlike the real Lua interpreter, it doesn't allow you to spread over multiple
lines. You will have to use semicolons to divide statements. It's also less
fully featured than actual Lua; e.g. you can't `require()` external modules, and
the bitwise shift operators `<<` and `>>` are missing.

Another use of the Lua interface is to track variables which aren't normally
displayed on screen. For example, put this in `default.lua` to show whenever the
first character gains XP to the Adventurer class in _Knightmare_:

    xp = 0
    function on_uae_vsync()
      t = uae.peek_u16(0x18e1a)
      if not(t==xp) then
        print(string.format("Ratt gained %d XP.",t-xp))
        xp = t
      end
    end

A script like this prints to stdout (i.e. the terminal you launched fs-uae
from), but you could also display data by writing it to some on-screen value,
such as a character name or player 2 score readout.

A limitation is that you can only read memory and custom registers, not data or
address registers. For more specific abilities, use the
[FS-UAE debugger](../guide/uae-debugger-intro.html).

See also
[cnvogelg's tools](https://github.com/cnvogelg/fs-uae/tree/lua/tools),
[cnvogelg's fsuaetools](https://github.com/cnvogelg/fs-uae-tools/tree/master/fsuaetools),
and [sonnenscheinchen's emu-scripts](https://github.com/sonnenscheinchen/emu-scripts)
for some tools that mainly use the interface to create a GUI to switch disks.
These tools take the versatile approach of writing Python scripts which
interface with the Lua shell, which opens up a lot of options.
