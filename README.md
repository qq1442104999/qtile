- 管理用户目录的工具
sudo pacman -S xdg-user-dirs
xdg-user-dirs-update

2）vim /etc/pacman.conf尾部添加
[archlinuxcn]
SigLevel = Never
Server = https://mirrors.ustc.edu.cn/$repo/$arch

顺便开启
[multilib]
Include = /etc/pacman.d/mirrorlist

sudo pacman -Syyu
sudo pacman -S yay

3） sudo pacman -S yay git wget

4)安装Xorg
sudo pacman -S xorg xorg-server xorg-apps xorg-xinit
sudo pacman -S xf86-video-amdgpu amd显卡驱动
sudo X -configure

5）sudo pacman -S konsole dolphin

6）安装qtile
yay -S qtile qtile-extras
pacman -S libpulse

7)安装字体
yay -S wqy-microhei
yay -S ttf-wps-fonts
yay -S ttf-material-design-icons
yay -S ttf-joypixels
yay -S ttf-dejavu
ttf-jetbrains-mono
adobe-source-han-sans-cn-fonts
adobe-source-han-serif-otc-fonts
noto-fonts-cjk
8）sudo pacman -S docker
sudo systemctl start docker
sudo systemctl enable docker
9）chsh -s /usr/bin/zsh
10)系统剪贴板 xclip
11)安装v2raya
docker run -d \
--restart=always \
--privileged \
--network=host \
--name v2raya \
-e V2RAYA_ADDRESS=0.0.0.0:2017 \
-v /lib/modules:/lib/modules \
-v /etc/resolv.conf:/etc/resolv.conf \
-v /etc/v2raya:/etc/v2raya \
mzz2017/v2raya
12）picom
