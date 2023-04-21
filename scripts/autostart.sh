#!/bin/sh

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & #提权
udiskie --appindicator & #自动挂载u盘
/usr/bin/prime-offload &  #optimus-manager
optimus-manager-qt & #显卡
#lxsession &
picom  --config ~/.config/qtile/config/picom.conf & #picom
fcitx5 &                   #输入法自启动
nm-applet &                #网络托盘
blueman-applet &           #蓝牙
numlockx &                 #在启动时激活 numlock
dunst -conf ~/.config/qtile/config/dunst.conf & #开启通知server
/opt/clash-for-windows-bin/cfw & #clash_for_windows
xrandr --dpi 144 &
sleep 1
feh --bg-fill --randomize ~/workspace/wallpaper/* &  #壁纸
