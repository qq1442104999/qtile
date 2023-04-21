#-----------------------------------------------------------------------------------------------------
from libqtile import bar, layout, qtile, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import backlight, Spacer

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

import os
import subprocess
#------------------------------------------------------------------------------------------------------
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/scripts/autostart.sh")
    subprocess.Popen([home])

@lazy.function
def float_to_front(qtile):
   # logging.info("bring floating windows to front")
    for group in qtile.groups:
        for window in group.windows:
            if window.floating:
                window.cmd_bring_to_front()

@lazy.function
def minimize(qtile):
    for window in qtile.current_group.windows:
        if window.minimized:
            window.minimized = False
            window.cmd_focus()

@hook.subscribe.client_managed
def _screen1(window):
    wm_class = window.window.get_wm_class()
    w_name = window.window.get_name()
    if wm_class == ["Steam", "Steam"]:
        if w_name == "好友列表":
            window.kill()
        elif w_name == "Steam - 新闻":
            window.kill()
#------------------------------------------------------------------------------------------------------
mod = "mod4"
terminal = "st"

keys = [
    # 在窗口间切换 
    Key([mod], "h", lazy.layout.left()), 
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()), 
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "Tab", lazy.layout.next()),
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),

    # 移动窗口 
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()), 

    # 窗口缩小/放大
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()), 
    Key([mod, "control"], "j", lazy.layout.grow_down(),lazy.layout.grow()),
    Key([mod, "control"], "k", lazy.layout.grow_up(),lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),

    #堆栈模式
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
    ),
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "space", lazy.next_layout()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "d", lazy.spawn("rofi -show run")),
    Key(
        [mod], "t",
        lazy.window.toggle_floating(), 
        lazy.window.center(),
        #screen = window.group.screen
        #window.floating = True
        #window.tweak_float( 
        #                   x=int(screen.width / 10), 
        #                   y=int(screen.height / 10), 
        #                   w=int(screen.width / 1.2),
        #                   h=int(screen.height / 1.2),
        #),
    ),                                          
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "x", 
        lazy.window.toggle_minimize(), 
        lazy.layout.next(),
        ),
    Key([mod], "z", minimize),
    Key([mod, "shift"], "f", lazy.group.setlayout("max")),
    Key([mod], "a", float_to_front),
    Key([mod], "c", lazy.spawn("google-chrome-stable")),
    Key([mod], "F1", lazy.spawn("dolphin")),
    Key([mod], "F2", lazy.spawn("konsole")),
    #Key([mod], "Escape", lazy.spawn("fcitx5-remote -c")),
    
    #背光
    Key( 
        [], 
        "XF86MonBrightnessUp", 
        lazy.spawn("brightnessctl set +5%")
    ), 
    Key( 
        [], 
        "XF86MonBrightnessDown", 
        lazy.spawn("brightnessctl set 5%-")
    ), 
    
    #音量
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("amixer set Master 5%+")
    ),

    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("amixer set Master 5%-")
    ),
]

#------------------------------------------------------------------------------------------------------------
groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

#-------------------------------------------------------------------------------------------------------------
def init_layout_theme():
    return {"margin":5,
            "border_width":2,
            "border_focus": "#5e81ac",
            "border_normal": "#4c566a",
           }

layout_theme = init_layout_theme()

layouts = [
    layout.MonadTall(
        **layout_theme,
        ratio = 0.6,
        ),
    layout.Max(**layout_theme),
    #layout.Tile(**layout_theme),
]

#-------------------------------------------------------------------------------------------------------------
def init_colors():
    return [
            ["00000000","00000000"], # color 0 | 透明
            ["#000000", "#000000"], # color 1 | 黑色
            ["#FFFFFF", "#FFFFFF"], # color 2 | 白色
            ["#4C566A", "#4C566A"], # color 3 | 灰色
            ["#BF616A", "#BF616A"], # color 4 | 红色
            ["#D08770", "#D08770"], # color 5 | 橙色
            ["#EBCB8B", "#EBCB8B"], # color 6 | 黄色
            ["#A3BE8C", "#A3BE8C"], # color 7 | 绿色
            ["#B48EAD", "#B48EAD"], # color 8 | 紫色
            ["#8FBCBB", "#8FBCBB"], # color 9 | 青色
            ["#88C0D0", "#88C0D0"], # color 10 | 水色
            ["#81A1C1", "#81A1C1"], # color 11 | 蓝色
            ["#5E81AC", "#5E81AC"], # color 12 | 海军
            ["#363636"], # color 13
           ]
colors = init_colors()

my_font = "JetBrainsMono Nerd Font Mono"

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)

extension_defaults = widget_defaults.copy()


def init_widgets_list(secondar=False):
    def init_decor(width=0):
        return {
            "decorations": [
                RectDecoration(
                    use_widget_background = True,
                    #line_width = 2,
                    #line_colour = colors[2],
                    colour = colors[0],
                    radius = [7,7,7,7],
                    filled = True,
                    padding_y = 4,
                    padding_x = 0,
                    group = True,
                    clip = True,
                    extrawidth = width,
                ),
            ],
        }
    decor = init_decor()
    systray_decor = init_decor(width=5)

    widgets_list = [
        widget.Spacer(length=5),
        widget.CurrentLayoutIcon(
            background = colors[4],
            scale = 0.5,
            **decor,
            ),
        widget.GroupBox(
            background = colors[4],
            font = my_font,
            fontsize = 13,
            **decor
            ),
        widget.Spacer(length=5),
        widget.TaskList(
            border = colors[2],
            borderwidth = 4,
            unfocused_border = colors[4],
            foreground = colors[1],
            font = my_font,
            fontsize = 20,
            highlight_method = "block",
            icon_size = 20,
            margin_y = 1,
            margin_x = 3,
            padding_y = 0,
            padding_x = 5,
            spacing = 5,
            max_title_width = 200,
            theme_path="/usr/share/icons/Papirus-Dark",
            theme_mode = "preferred",
            ),
        widget.Chord(
            chords_colors={
            "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
            ),
        widget.Systray(
            background = "00000000",
            icon_size = 22,
            padding = 5,
            **systray_decor,
            ),
        widget.Spacer(length=5),
        widget.Net(
            background = colors[12],
            foreground = colors[1],
            font = my_font,
            fontsize = 18,
            format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}',
            prefix="M",
            **decor
            ),
        widget.Spacer(length=10),
        widget.Image(
                filename="~/.config/qtile/assets/bar_icons/gpu.svg",
                background = colors[11],
                colour= colors[1],
                mask = True,
                padding = 4,
                margin_y = 8,
                adjust_y = 0,
                adjust_x = 0,
                mouse_callbacks={
                    "Button1": 
                    lazy.spawn("st -e watch -n2 nvidia-smi")
                },
                **decor
                ),
        widget.NvidiaSensors(
            foreground = colors[1],
            background = colors[11],
            font = my_font,
            fontsize = 18,
            format='{temp}°C',
            padding = 0,
            mouse_callbacks={
                "Button1": 
                lazy.spawn("st -e watch -n2 nvidia-smi")
            },
            **decor
            ),
        #widget.Image(
        #    filename="~/.config/qtile/assets/bar_icons/cpu.svg",
        #    background = colors[11],
        #    colour = colors[1],
        #    mask = True,
        #    margin_y = 9,
        #    padding = 0,
        #    adjust_x = 0,
        #    adjust_y = 0,
        #    mouse_callbacks={
        #        "Button1": 
        #        lazy.spawn("st -e btop")
        #    },
        #    **decor
        #    ),
        widget.CPU(
            foreground = colors[1],
            background = colors[11],
            font = my_font,
            fontsize = 18,
            format="{load_percent:2.0f}%",
            padding = 3,
            mouse_callbacks={
                "Button1": 
                lazy.spawn("st -e btop")
            },
            **decor
            ),
        #widget.Image(
        #    filename="~/.config/qtile/assets/bar_icons/memory.svg",
        #    background = colors[11],
        #    colour = colors[1],
        #    mask = True,
        #    margin_y = 8,
        #    padding = 5,
        #    adjust_x = 6,
        #    adjust_y = 0,
        #    mouse_callbacks={
        #        "Button1": 
        #        lazy.spawn("st -e btop")
        #    },
        #    **decor
        #    ),
        widget.Memory(
            foreground = colors[1],
            background = colors[11],
            font = my_font,
            fontsize = 18,
            format="{MemUsed:2.0f}{mm}",
            measure_mem='G',
            padding = 0,
            mouse_callbacks={
                "Button1": 
                lazy.spawn("st -e btop")
            },
            **decor
            ),
        widget.Spacer(length=10),
        widget.Volume(
            background = colors[12],
            font = my_font,
            fontsize = 15, 
            emoji = True,
            padding = 2,
            **decor
            ),
        widget.Volume(
            background = colors[12],
            foreground = colors[1],
            fontsize = 18,
            **decor
            ),
        widget.TextBox(
            background = colors[12],
            foreground = colors[1],
            font = my_font,
            fontsize = 25,
            text = "󱠂",
            padding = 0,
            **decor
            ),
        widget.Backlight(
            background = colors[12],
            foreground = colors[1],
            backlight_name = "intel_backlight",
            font = my_font,
            fontsize = 18,
            **decor
            ),
        widget.Spacer(length=10),
        widget.BatteryIcon(
            background = colors[10],
            scale = 1,
            update_interval = 3,
            theme_path = "/home/wang/.config/qtile/assets/battery_icons",
            **decor
            ),
        widget.Battery(
            background = colors[10],
            foreground = colors[1],
            font = my_font,
            fontsize = 18,
            update_interval = 3,
            format = "{char}{percent:2.0%}",
            **decor
            ),
        widget.Spacer(length=10),
        widget.TextBox(
            background = colors[10],
            foreground = colors[1],
            font = my_font,
            fontsize = 20,
            text = "",
            padding = 3,
            **decor
            ),
        widget.Clock(
            background = colors[10],
            foreground = colors[1],
            font = my_font,
            fontsize = 18,
            format = "%m/%d",
            **decor
            ),
        #widget.AnalogueClock(
        #         background = colors[10],
        #        margin = 5,
        #        padding = 0,
        #        hour_size = 2,
        #        hour_length = 0.55,
        #        hour_colour = colors[5],
        #        minute_size = 2,
        #        minute_length = 0.55,
        #        minute_colour = colors[1],
        #        face_border_colour=colors[6],
        #        face_shape='circle',
        #        face_border_width=2,
        #        update_interval=1,
        #        adjust_y=2,
        #        adjust_x=2,
        #        **decor
        #        ),
        widget.Clock(
            background = colors[10],
            foreground = colors[1],
            font = my_font,
            fontsize = 28,
            format = "%I:%M",
            **decor,
            ),
        widget.Spacer(length=5),
    ]
    return widgets_list
widgets_list = init_widgets_list()

def init_screens():
    return [Screen(top=bar.Bar(widgets_list,30,opacity=1,background=colors[0]))]

screens = init_screens()
            
#------------------------------------------------------------------------------------------------------------------------------
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

#------------------------------------------------------------------------------------------------------------------------------
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = True
cursor_warp = True
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="lxappearance"), 
        Match(wm_class="Pavucontrol"), 
        Match(wm_class="kvantummanager"), 
        Match(wm_class="blueman-manager"), 
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


#@lazy.function
#def float_to_front(qtile):
#    """
#     Bring all floating windows of the group to front
#    """
#    global floating_windows
#    floating_windows = []
#    for window in qtile.currentGroup.windows:
#        if window.floating:
#            window.cmd_bring_to_front()
#            floating_windows.append(window)
#    floating_windows[-1].cmd_focus()

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
