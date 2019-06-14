# 说明：此教程基于redhat7 版本实现，其他版本命令会有一些差异

## 一、本地yum源的配置

```python
# 配置本地yum源
mkdir -p /media/cdrom # 建立光盘挂在目录
vim /etc/fstab # 编辑自动挂载目录
# 在末行添加
/dev/cdrom /media/cdrom iso9660 defaults 0 0	# 开机启动自动挂载
mount -a # 挂载目录中所有设备，此时可看到挂载成功提示

# 编辑yum配置文件
vim /etc/yum.repos.d/***.repo # 一般是新创建一个以.repo为结尾的文件
# 添加以下内容
[name] # yum源唯一标识符，不可重名
name = redhat7 # name可以自定义，主要区分不同yum仓库
baseurl = file:///media/cdrom # yum源路径，也可以是 http://***或ftp://***
enabled = 1 # 表示此yum源是否启用，1表示启用，0表示禁用
gpgcheck = 0 # yum源是否进行校验，1表示校验，0表示不校验
：wq # 保存退出

# yum的基本操作
yum repolist all # 列出所有仓库
yum list all # 列出仓库所有软件包
yum info 软件包名 # 查看软件包信息
yum install 软件包名 # 安装软件
yum reinstall 软件包名 # 重新安装软件包
yum updare 软件报名 # 升级软件包
yum remove 软件包名 # 移除软件包名
yum clean all # 清空所有仓库缓存
yum ckeck-update # 检查可更新的软件包
yum grouplist # 查看系统中以安装的软件包
yum groupinstall 软件包组 # 安装指定软件包组
yum groupremove 软件包组 # 删除指定软件包组
yum groupinfo 软件包组 # 查询指定的软件包组
```



## 二、使用yum安装图形化界面

````python
# 查看yum源可用软件包组
yum grouplist 
# 安装图形化界面
yum groupinstall -y "Server with GUI"
# 切换图形化界面
startx
# 设置启动模式为图形界面。
vim /etc/inittab # 会看到提示更改此文件不影响systemd，即无效。
# 先删除默认启动方式，在重新创建一个软连接，即设置默认启动为GUI
rm /etc/systemd/system/default.target
ln -sf /lib/systemd/system/graphical.target /etc/systemd/system/default.target
````



## 三、更改root用户密码

1. 开机进入启动项

![修改root用户密码1](/Users/henry/Documents/截图/Py截图/修改root用户密码1.png)

2. 按键盘的"e"件进入编辑内核模式，在Linux16 /vml**** LANG=en_US.UTF-8 后添加 rd.break。

![修改root用户密码2](/Users/henry/Documents/截图/Py截图/修改root用户密码2.png)

3. 按住ctrl + c / command + c健，会进入如下图示。

![修改root用户密码3](/Users/henry/Documents/截图/Py截图/修改root用户密码3.png)

4. mount 查看/sysroot 只有ro权限，需要重新挂载获取rw权限

![修改root用户密码4](/Users/henry/Documents/截图/Py截图/修改root用户密码5.png)

5. 必须创建.autorelabel 文件，否则会失败。
6. root 用户密码就已经更改完成。

## 四、常见命令

### 1. 文件相关

```
//file1.txt
I need to buy apples.
I need to run the laundry.
I need to wash the dog.
I need to get the car detailed.

//file2.txt
I need to buy apples.
I need to do the laundry.
I need to wash the car.
I need to get the dog detailed.

我们使用diff比较他们的不同：
diff file1.txt file2.txt

输出如下结果：
2,4c2,4
< I need to run the laundry.
< I need to wash the dog.
< I need to get the car detailed.
---
> I need to do the laundry.
> I need to wash the car.
> I need to get the dog detailed.

我们来说明一下该输出结果的含义，要明白diff比较结果的含义，我们必须牢记一点，diff描述两个文件不同的方式是告诉我们怎么样改变第一个文件之后与第二个文件匹配。我们看看上面的比较结果中的第一行 2,4c2,4 前面的数字2,4表示第一个文件中的行，中间有一个字母c表示需要在第一个文件上做的操作(a=add,c=change,d=delete)，后面的数字2,4表示第二个文件中的行。

2,4c2,4 的含义是：第一个文件中的第[2,4]行(注意这是一个闭合区间，包括第2行和第4行)需要做出修改才能与第二个文件中的[2,4]行相匹配。
接下来的内容则告诉我们需要修改的地方，前面带 < 的部分表示左边文件的第[2,4]行的内容，而带> 的部分表示右边文件的第[2,4]行的内容，中间的 --- 则是两个文件内容的分隔符号。
```

