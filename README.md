# 这是一个readme
# 初来乍到，请多关照

---------- win10的pycharm中terminal是指为oh my zsh ----------
# 使用ubuntu终端（在win store中下载）安装zsh，如果失败请直接安装oh my zsh
sudo apt install zsh
# 替换默认shell为zsh
chsh -s $(which zsh)
# 重启ubuntu终端，查看当前shell
echo $SHELL
# 如果上边的zsh命令失败，请直接执行下方命令
sh -c "$(https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/master/tools/install.sh)"
# pycharm中setting修改terminal的shell path为C:\Windows\System32\bash.exe

