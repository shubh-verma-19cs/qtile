# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

import os
import subprocess
import iwlib
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
mod2 = "mod1"
terminal = "xfce4-terminal"
menu = "rofi -show drun"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])

keys = [
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "f", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    Key([mod2], "space", lazy.spawn(menu)),


    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "e", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),


    # Sound
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 5%+")),
    
    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight +10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -10")),

]

#groups = [Group(i) for i in "123456789"]

groups = []

# group_names = 'one two three four five six seven eight nine'.split()
# group_labels = ["一", "二", "三", "四", "五", "六", "七", "八", "九"]

group_names = 'one two three four five six seven'.split()
group_labels = ["🜂", "🜁", "⧋", "⧔", "⧕", "⧑", "⧒"]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            #layout=group_layouts[i].lower(),
            label=group_labels[i]
        ))

for i, name in enumerate(group_names, 1):
    keys.extend([
        Key([mod], str(i), lazy.group[name].toscreen()),
        Key([mod, 'shift'], str(i), lazy.window.togroup(name))])

#for i in groups:
#    keys.extend([
        # mod1 + letter of group = switch to group
#        Key([mod], i.name, lazy.group[i.name].toscreen(),
#            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
#        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
#            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
#    ])

layouts = [
    # layout.Columns(border_focus_stack=['#1bfcd3', '#7e93fc'], border_width=4, margin=4),
    layout.Bsp(border_focus="#81a1c1", border_normal="#434c5e", border_width=4, margin=6),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
   #  layout.RatioTile(),
   # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Iosevka Fixed Curly Semibold',
    fontsize=12,
    padding=0,
    background='#212630'
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                # widget.TextBox("", fontsize=20, margin=4,
                #     mouse_callbacks={'Button1': lazy.spawn("vim ~/.config/qtile/config.py")}),
                widget.CurrentLayoutIcon(foreground="#02fca0", scale=0.6),
                widget.CurrentLayout(fmt='[{}]',fontsize=20),
                widget.TextBox(text='|',fontsize=48, foreground="#434c5e"),
                # widget.TextBox(text=' ',fontsize=18),
                widget.GroupBox(font= 'Iosevka Fixed Curly Extra Bold', 
                    fontsize=22, 
                    highlight_method='line',
                    highlight_color=['13171e', '13171e'],
                    # block_highlight_text_color="#ffffff",
                    inactive="#414f6b",
                    active="#ebcb8b",
                    rounded="false"),
                #widget.Prompt(),
                # widget.TextBox(text=' ',fontsize=18),
                # widget.Spacer(length=bar.STRETCH),
                widget.TextBox(text='|',fontsize=48, foreground="#434c5e"),
                widget.WindowName(
                max_chars=64,
                font= 'Iosevka Fixed Curly Regular',
                fontsize=18,
                padding=8),
                widget.TextBox(text='|',fontsize=48, foreground="#434c5e"),
                # widget.Spacer(length=bar.STRETCH),
                # widget.Spacer(length=bar.STRETCH),
                widget.TextBox(text=' ',fontsize=18),
                #widget.Chord(
                #    chords_colors={
                #        'launch': ("#ff0000", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                #),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Systray(),
                widget.TextBox(text='|',fontsize=48, foreground="#434c5e"),
                widget.Clock(format=' %d-%m-%y %a', fontsize=18, foreground="#8fbcbb"),

                widget.TextBox(text='|',fontsize=48, foreground="#434c5e"),
                widget.Clock(format=' %I:%M %p', fontsize=18, foreground="#81a1c1"),

                widget.TextBox(text='|',fontsize=48, foreground="#434c5e"),
                widget.TextBox(text=' ',fontsize=18, foreground="#a3be8c"),
                widget.Battery(format='{percent:2.0%}', fontsize=20, foreground="#a3be8c"),
                widget.TextBox(text='|',fontsize=48, foreground="#434c5e"),

                widget.TextBox(text=' ',fontsize=18, foreground="#ebcb8b"),
                widget.Volume(fontsize=20, foreground="#ebcb8b"),
                widget.TextBox(text='|',fontsize=48, foreground="#434c5e"),

                widget.TextBox(text='',fontsize=18, foreground="#b48ead"),
                widget.Wlan(fontsize=20, foreground="#b48ead"),
                widget.TextBox(text='|',fontsize=48, foreground="#434c5e"),

                widget.QuickExit(fmt=' ', fontsize=20, foreground="#bf616a", timer_interval=5, countdown_format='[{} sec.]'),
            ],
            32,
            margin=6,
            background='#212630',
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
# focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "qtile"
