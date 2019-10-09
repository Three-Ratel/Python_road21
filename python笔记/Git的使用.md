

## 1. Git基础

### 1. 简介

-   Git是用于代码托管工具。
-   开发前因后果：2002 Linux kernel 项目开发使用商业版的BitKeeper 版本控制系统（VSC）管理项目程序，但与开发BK的公司关系决裂，免费版本开始收费，促使Linux开发者自己开发新的代码托管工具。尤其是Linus Torvalds（Linux之父）等，为创建一个快速、简单、多并发、像Linux一样高效管理大型项目，而研发的开源代码管理工具。

```python
# Maxos会有内置git，不需要单独安装，Windows需要下载安装。
# git 全局命令
git --version # 查看git版本号，安装后查看
git clone url	# 供其他终端使用
```

#### 1.Git 三种状态

- Working Directory ：本地工作目录，**工作区**
- Staging Area：添加文件，用于commit前，**暂存区**
- .git directory(Repository)：本地仓库，存储commit数据，**版本库**

![git文件可能的状态图](/Users/henry/Documents/截图/Py截图/git文件可能的状态图.png)

#### 2. 基本概念

- Committed 表示数据已经安全存储到本地数据库中（本质是标记版本号git commit -m "版本号"）
- Modified 表示已经修改的文件，但没有进行Commit
- Staged 表示已经标记一个修改过的文件当前版本，下次commite上传（本质就是git add 文件名）

#### 3. Git基本工作流程

- 在working tree中修改文件
- Committed 表示数据已经安全存储到本地数据库中
- Modified 表示已经修改的文件，但没有进行Commit
- Staged 表示已经标记一个修改过的文件当前版本，下次commite使用

#### 4. Git配置文件

-   Git可以更改config文件，自定义化主题。Git配置文件可能存储到三个位置：

1.  /etc/gitconfig file: 全局配置文件
2. ~/.gitconfig or ~/.config/git/config file:本地存储个人账号
3.  .git/config：本地git仓库路径中的文件，包含初始化，上传，下载的配置

```python
# 配置全局账号
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
# --global参数只能设置一个账号，如果使用多个账号，需要省略此参数
```

```python
# 自定义编辑器（for mac）
git config --global core.editor emacs
# （for windows）
git config --global core.editor "'C:/Program Files (x86)/Notepad++/notepad++.exe' -multiInst -nosession"
```

```python
# 查看git配置
git config --list
# 查看用户名
git config user.name
```

#### 5. Git建立仓库的两种方法

-   本地建立新git 仓库（repository ）

```python
# for mac
cd /User/henry/***  # 进入本地文件夹（即将进行托管的文件夹）
git init # 进行git 初识化，同时会生成本地仓库（.git/）目录
git add 文件名（.） # 添加到staging area
git status # 查看git 信息，此时可看到已添加到staging area的文件以及为添加的文件
git commit -m '提示符' # 对文件进行标记，利于区分
git remote add henry https://gitee.com/***/***.git  # 关联到码云账户
git push -u henry master # 推送到码云，会提示输入密码

# for windows
进入待托管的文件夹，右击鼠标，打开git bash here
其余步骤同mac
```

-   如果已经使用过git 可以使用clone 命令

```python
# for example
# 如果想重命名直接在url后添加文件名，也可省略表示默认文件名
git clone https://gitee.com/***/***  (文件名) 
```

#### Note

-   git 不仅支持http协议，还支持ssh 传输协议

### 2. 常见报错及处理

#### 1. 报错1

```python
# 原因：本地仓库为空
error: src refspec master does not match any.
error: failed to push some refs to 'https://gitee.com/***/***.git'

# 解决方案
git add 文件名 或（.全部文件）
git commit -m "版本名"
```

#### 2. 报错2

```python
# 原因：本地与托管平台数据不一致，常是由在托管平台删除导致
! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'https://gitee.com/***/***.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
  
# 解决方案
git pull henry master  				# 强制把远端数据与本地数据同步
git push -u origin master			# 重新推送即可

# 如果上述步骤不生效，还提示错误，可使用
git push origin master -f 			# -f 表示强制上传，不建议经常使用
```
### 3. 本地仓库文件状态

1.  本地仓库中的任意文件只有两种状态：tracked （追踪）或者untracked（待追踪）。
2.  untracked的文件，git不会进行托管，只有tracked的文件才能push到remote（远端）。
3.  tracked文件可以有3种状态：unmodified（第一次clone后）, modified（本地修改的文件）或者staged（add的文件）。

![git三种状态](/Users/henry/Documents/截图/Py截图/git三种状态.png)

### 4. 删除remote端文件

- 先在Working Directory（本地），删除要删除的文件

```python
# 告知 git， 要删除的文件 
git rm filename
# 查看文件状态
git status 
# git 已经检测到用户删除的文件
```


![删除remote端文件1](/Users/henry/Documents/截图/Py截图/删除remote端文件1.png)


```python
# 做标记
git commit -m 'test'
git push origin master
# commit历史阻止pull命令
git pull origin master --allow-unrelated-histories
```

![删除remote端文件2](/Users/henry/Documents/截图/Py截图/删除remote端文件2.png)

### 5. 强制同步（慎用）

```python
# 本步骤，主要针对于小白，无法解决远端和本地同步问题
1. git add .
2. git commit -m 'test'
3. git push origin master -f 
```

#### Note

1.  **第3步表示强制让remote端于local同步**
2.  **这样会用local端刚push的数据完全覆盖remote 端**


### 6. 忽略指定文件

-   在使用git的过程中，我们为了省事经常会使用 git add . 添加所有文件，但是有一些 . 的文件会同时被 track 到，这个时候我们就需要使用选择性忽略。

#### 1. 配置

1.  打开本地git 项目仓库，Mac/Linux用户可以在terimal中打开项目文件夹，windows用户在项目文件夹中打开Bash。
2.  vim .gitingore
3.  添加需要忽略的文件

#### 2. 效果展示

-   配置 .gitignore 前的Working Directory状态

![git 忽略前的状态](/Users/henry/Documents/截图/Py截图/git 忽略前的状态.png)

-   配置 .gitignore 文件

![git 忽略的文件](/Users/henry/Documents/截图/Py截图/git 忽略的文件.png)

-   配置 .gitignore 后的Working Directory状态

![git忽略后的状态](/Users/henry/Documents/截图/Py截图/git忽略后的状态.png)

-   设置好.gitignore 文件后，下次就可以任性的使用git add . 的操作了。

### 7. 文件管理

#### 1. 版本回滚

当我们本地文件误删或者更改后，想恢复之前的状态，如果已经进行commit，可以通过命令进行回滚

- 查看提交记录
- commit id 不用完全写完，git会自动寻找，但也不能太短，必须唯一

```python 
# 可以查看到commit的id以及自己添加的标记
git log 
# 数据进行回滚到指定的commit记录
git reset --hard commit的id号
HEAD is now at 83b0afe append GPL
# 查看操作记录
git reflog
# 回退版本后，想取消回滚操作
git reset --hard HEAD^
```

#### 2. 工作区和暂存区

- 工作区(Working Directory)：当前git仓库的目录
- 版本库(Repository)
  1. 工作区有一个隐藏目录**.git**，这个不算工作区，而是Git的版本库。
  2. Git的版本库里存了很多东西，其中最重要的就是称为**stage（或者叫index）的暂存区**，还有Git为我们自动创建的第一个分支**master**，以及指向maste的一个**指针**叫**HEAD**。

```python
# 把要提交的所有修改放到暂存区（Stage）
git add 文件名/. 
# 查看暂存区的状态
git status
# 一次性把暂存区的所有修改提交到分支。
git commit -m '标记'
# 推送到remote端
git push origin master
```

- 查看工作区和版本库里面最新版本的区别

```python
git diff HEAD -- 文件名
```

- 查看当前工作区状态

```python
git status
```

- Git会告诉你，`git checkout -- file`可以丢弃工作区修改

```python
# 在stage之前使用
git checkout -- 文件名
# -- 很重要，如果没加表示切换分支
```

- 把暂存区的修改撤销掉（unstage），重新放回工作区

```python
# 在stage之后使用
git reset HEAD <file>
```

- 删除文件

- git checkout其实是用版本库里的版本替换工作区的版本，无论工作区是修改还是删除，都可以“**一键还原**”。

```python
git rm test.txt
git commit -m 'del test'
```

- 查看更改

```python
git diff
```

## 2. 分支管理

### 1. 分支

#### 1. 分类

1.  主分支：默认是 master
2.  开发功能：一般是 dev
3.  修复bug：一般是 bug

#### 2. 功能

-   环境的隔离

### 2. 修复bugs

#### 1. 创建切换分支

```python
git branch							# 查看当前所有分支
git branch dev						# 创建 dev 分支
git checkout dev					# 切换到 dev 分支
git branch bug						# 创建 bug 分支
git checkout bug					# 切换 bug 分支，修复bugs
```

#### 2. 合并分支

-   需要切换到目标的分支后再合并

```python
git checkout master
git merge bug						# 合并 bug 分支，到 master 分支
git branch -d bug					# 删除 bug 分支
```

#### 3. 回到dev分支

-   冲突的解决

```python
git checkout dev
git add .
git commit -m '开发完毕'
git checkout master					# 切换到 master 分支准备合并dev
git merge dev						# 此时会发生冲突，需要手动解决冲突
git add .
...
```

### 3. 工作流

至少有两个分支：master 和 dev 分支

-   dev 用于开发新功能
-   master 是正式版，线上运行的代码

## 3. github的使用

-   gitlab 自己搭建仓库







## 附录：

### 1. 团队协同开发流程

1. 分支：master dev 每个人
2. 个人在个人分支上开√发
3. 开发完成后，推送到自己的分支
4. 创建pull request 合并到dev分支
5. leader 审核代码，接收合并
6. dev 合并到 merge上
