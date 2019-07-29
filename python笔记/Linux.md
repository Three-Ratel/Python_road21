1. 1u and 2u
2. top500.org
3. CPU：Central Processing Unit
4. DDR2：240-pin DDR 184-pin
5. Graphic Processing Unit
6. Hot swap
7. 1U = 44.45mm
8. BSD：tcp/ip, unix
9. kernel.org
10. 5.2.4：主版本号、次版本号、末版本号
11. GPL
12. aliyun
13. 密码要求：
    - 12位及其以上
    - 必须包含大写字母，小写字母，数字，特殊字符
    - 3个月或者半年更换一次

# 1. Centos简介

## 1. 虚拟机

- vmware
- virturl box(orcle)
- 作用：通过软件模拟生成硬件信息

1. 桥接：会跟主机获取同一网段ip地址
2. net：会进行地址转换

## 2. 终端

1. 图形终端：/dev/tty7
2. 虚拟终端(ctrl+alt+f1-6) /dev/tty#
3. 伪终端：/dev/pts/id
4. 物理终端
5. 设备终端
6. 串行终端

```SHELL
# chvt N 命令让你切换到前台终端 N，这与按CTRL+ALT+Fn相同。如果它不存在，则创建相应的屏幕。
# 进入tty/pts/2
chvt 2
chvt 1    # 退出
fgconsole # 查看活动虚拟控制台的总数
fgconsole --next-available # 查看下一个未分配的虚拟终端
deallocvt # 移除未使用的虚拟终端
```

```SHELL
# 查看主机地址
ifconfig
ip a/addr
# 查看终端
tty
```

- 交互式接口
- 启动终端后，在终端设备上会打开一个接口
- GUI：图形接口
- 命令行CLI：shell、powershell
- Shell
  - sh、csh、tcsh
  - ksh、bash（linux、mac上的shell）、zsh
  - 用来在linux系统上的一个接口，用来将用户的输入发送给操作系统执行，并把得到的结果输出出来

```SHELL
# 查看系统支持的shell
cat /etc/shells
# 切换shell
chsh -s /bin/bash
# 查看当前shell
echo $SHELL
# #号表示root用户
# 用户@主机名 当前目录 身份
[root@localhost /]# 
# $号表示普通用户
[henry@localhost /]$
```

## 3. 修改提示符格式

```SHELL
PS1="\[\e[1;5;41;33m\][\u@\h \W]\\$\[\e[0m\]"
\e 
\h 主机名简称
\w 当前工作目录 \t 24小时时间格式 \! 命令历史数
\u 当前用户
\H 主机名
\W 当前工作目录基名 \T 12小时时间格式
\# 开机后命令历史数
1表示字体加粗， 0表示默认字体。4表示给字体加上下划线。5表示字体闪烁。7表示用亮色突出显示，来让你的文字更加醒目
31表示字符颜色。
可选颜色：红色、绿色、黄色、蓝色、洋红、青色和白色。他们对应的颜色代码是：30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（洋红）、36（青色）、37（白色）
40表示字符背景色。可选颜色 40、41、42、43、44、45、46、47
```

```SHELL
# 查看主机信息
[root@localhost ~]# echo $PS1
[\u@\h \W]\$
# 更改用户
[root@localhost ~]# PS1="\[\e[1;30;35m\][\u@\h \W]\\$\[\e[0m\]"
# 更改用户信息的配置文件,即永久生效
# 向文件中追加信息
echo 'PS1="\[\e[1;30;35m\][\u@\h \W]\\$\[\e[0m\]"'>> /etc/profile.d/ps.sh(自定义名称,后缀必须是.sh)
```

## 4. Linux基础命令

1. 内部命令：安装完系统以后自带的命令
2. 外部命令：第三方命令，在某些地方可以直接找到执行文件

```SHELL
# 获取内部命令列表
[root@3ad30f522613 ~]# help
# 查看是命令类别
[root@3ad30f522613 ~]# type echo
echo is a shell buildin
# 查找命令的路径
which cp
# 列出所有别名
alias
# 定制、取消别名
alias ce='cd /etc'
unalias ce
# 修改 ～/.bashrc 文件，当前用户有效
echo 'alias ce='cd /etc' >> ~/.bashrc
# 所有用户生效
echo 'alias ce='cd /etc' >> /etc/bashrc
# 执行本身含义
"ls"  'ls'	\ls
# 单双引号的区别
echo "$name"  # 打印环境变量
echo '$name'	# 打印$name
```

## 5. 常用命令

### 0. 格式

```SHELL
# 选项：启用或禁用某些功能(短选项-a和长选项--all)
# 参数：命令的作用对象，一般为目录、用户等
command [options] [args...]
# 注意
1. 多个选项及参数和命令之间需要空格隔开
2. ctrl + c：取消命令执行
3. 同时执行多个命令，用分号隔开
4. 换行command + \，使用\将命令切换成多行s
```

### 1. 时间相关

```SHELL
# 显示完整时间
date 
# 显示年月日
date +%F
# 显示24小时
date +%H
# 显示12小时
date +%I
# 年月日，时分秒
data +%y
data +%m
data +%d
date +%H
data +%M
data +%S
# 星期
date +%a
date +%A
# 打印完整时间
date +%T
# 自定义格式
date +%Y-%m-%d
date +%Y-%m-%d\ %H:%M   # 可以使用\ 表示转义
# unix元年，1970.01.01 0:0:0，时间戳
date +%s
# 显示多少周
date +%W
# 显示时区
timedatectl
# 设置时区
timedatectl set-timezone Asia/Shanghai
timedatectl set-timezone UTC
timedatectl set-time 15:58:30
timedatectl set-time 20151120
timedatectl set-time '16:10:40 2015-11-20'
# 查看所有时区
timedatectl list-timezones
# 查看日历，一个月
cal
# 查看日历，当前月以及上个月和下个月
cal -3
# 显示一年日历
cal -y
# 显示2018年日历
cal -y 2018
```

```SHELL
# 将你的硬件时钟设置为本地时区
timedatectl set-local-rtc 1
# 将你的硬件时钟设置为协调世界时（UTC）
timedatectl set-local-rtc 0
```

### 2. 关机、重启

```SHELL
# 默认一分钟后关机
shutdown # 所有用户都会收到此消息
# 重启，一分钟之后
shutdown -r 
# 取消
shutdown -c
# 指定时间关机
shutdown -r now/hh:mm/+6(6分钟之后)

# 直接重启
reboot
# -p表示切断电源
reboot -p 
# 重启
init 6

# 关机
init 0
# 关机
poweroff
```

### 3. xshell

```SHELL
# 快速退出
ctrl + d 
```

## 6. yum源

```SHELL
# 配置aliyun的yum源
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
yum clean all
yum makecache
```

```nginx
# 1.使用YUM查找软件包 
yum search 
# 2.列出所有可安装的软件包 
yum list 
# 3.列出所有可更新的软件包 
yum list updates 
# 4.列出所有已安装的软件包 
yum list installed 
# 5.列出所有已安装但不在 Yum Repository 内的软件包 
yum list extras 
# 6.列出所指定的软件包 
yum list 
# 7.使用YUM获取软件包信息 
yum info 
# 8.列出所有可更新的软件包信息 
yum info updates 
# 9.列出所有已安装的软件包信息 
yum info installed 
# 10.列出所有已安装但不在 Yum Repository 内的软件包信息 
yum info extras 
# 11.列出软件包提供哪些文件 
yum provides
```

## 7. bash的快捷键

- ctrl+l 清屏，相当于clear命令
- ctrl+o 执行当前命令，并重新显示本命令
- ctrl+s 阻止屏幕输出，锁定
- ctrl+q 允许屏幕输出
- ctrl+c 终止命令
- ctrl+z 挂起命令
- ctrl+a 光标移动到行首，相当于home
- ctrl+e 光标移动到行尾，相当于end
- ctrl+xx光标在命令行首和光标之间移动
- ctrl+u 从光标处删除至命令行首
- ctrl+k 从光标处删除至命令行尾
- alt+r 删除当前整行
- alt+f 光标向右移动一个单词尾
- alt+b 光标向左移动一个单词首
- **需要注意:** alt组合键经常和其他软件冲突















