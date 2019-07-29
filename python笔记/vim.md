# 1. Simply Editing

## 1.1 Changing Text

- 删除不同长度的文本，并进入插入模式

```python
c			# 改变指定个数的词
cw		# 从当前光标位置之后改变一个单词
c2b		# 从当前光标位置之前改变2个单词
c$		# 从当前光标位置到行末
c0		# 从当前光标位置到行头
cc		# 替换当前行
C			# 从当前光标位置到行末
```

## 1.2 Characters

```python
rW		# 把光标当前位置后的一个字符替换为 W
8s		# 删除光标后 8 个字符，并进入插入模式
2S		# 删除光标所在行及之后的行(2行)，并进入插入模式
R			# 进入replace模式，类似于键盘上的 insert 键功能
3~		# 光标后3个字符，大小写转换
3x		# 删除3个字符
```

## 1.3 Deleting Text

```python
d2w		 # 删除光标后的 2 个单词
			 # 删除单词的一部分，包括空格
de		 # 删除单词的一部分，不包括空格
dE		 # 删除单词的一部分，不包括空格，包括标点符号
d$		 # 删除当前行的光标之后的内容
d0		 # 删除当前行的光标之前的内容
D			 # 从光标位置删除至行尾
2dd		 # 删除 2 行(类似cc作用于整行)
```

- 撤销

```python
u
U			# 撤销一行的所有编辑
```

## 1.4 Moving Text

```python
e				# 移动到单词结尾
```



```python
2p			# put，粘贴 2 次
xp			# 调换两个字符的顺序
```

## 1.5 Copying Text

- yank 和 deltete 使用同一**buffer**(上限9个)
- p 命令最多能调用9个

```python
y				# 复制
yw
y$
4yy/4Y	# 复制4行
```

```python
.				# 重复执行上次命令
```

## 1.6 插入方式

```python
A($a)		# 从行末追加数据
a				# 从当前光标后追加数据
I				# 从当前行首插入数据
i				# 从当前位置插入数据
O				# 从光标的上一行插入空行
o				# 从光标的下一行插入空行
s				# 删除一个字符并进入插入模式
S				# 删除到行末并进入插入模式
R				# 进入替换模式
25a*-		# 追加25对*-
50i*		# 插入50个*
ea			# 在单词结尾追加
3J			# 合并下 2 行到本行
```

## 1.7 小结

- **Table 1-1 Edit commands**

| Text object                          | Change     | Delete     | Copy       |
| ------------------------------------ | ---------- | ---------- | ---------- |
| 􏰻􏰊􏰆 􏰐􏰈􏰗One world                     | cw         | dw         | Yw         |
| Tow worlds, not counting punctuation | 2cw or c2W | 2dW or d2W | 2yW or y2W |
| Three words back                     | 3cb or c2b | 3db or d3b | 3yb or y3b |
| One line                             | cc         | dd         | yy or Y    |
| To end of line                       | c$ or C    | d$ or D    | y$         |
| Single character                     | r          | x or X     | yl or yh   |
| Five characters                      | 5s         | 5x         | 5yl        |

- **Table 2-2 Movement**

| Movement                            | Commands |
| ----------------------------------- | -------- |
| To first character of next line     | +        |
| To first character of previous line | -        |
| To end of world                     | e or E   |
| Forward by word                     | w or W   |
| Backword by word                    | b or B   |
| To end of line                      | $        |
| To beginning of line                | 0        |

- **Table 2-3 Other operations**

| Operations                       | Commands |
| -------------------------------- | -------- |
| Place text from butter           | P or p   |
| Start vi, open file if specified | vi file  |
| Save edits, quit file            | ZZ       |
| No saving of edits, quit file    | :q!      |

- **Table 2-4 Text creation and manipulation commands**

| Editing aciton                               | Commands |
| -------------------------------------------- | -------- |
| Insert text at current position              | i        |
| insert text at beginning of line             | I        |
| Append text at current position              | a        |
| Append text at beginning of line             | A        |
| Open new line below cursor for new text      | o        |
| Open new line above cursor for new           | O        |
| Delete line and substitute text              | S        |
| Overstrike existing characters with new text | R        |
| Join current and next line                   | J        |
| Toggle case                                  | ~        |
| Repeat last action                           | .        |
| Undo last change                             | u        |
| Restore line to original state               | U        |

# 2. Moving Around in a Hurry

| Movement                                                     | Command   |
| ------------------------------------------------------------ | --------- |
| Scroll forward one screen                                    | ^F        |
| Scroll backward one screen                                   | ^B        |
| Scroll forward half screen                                   | ^D        |
| Scroll backward half screen                                  | ^U        |
| Scroll forward one line                                      | ^E        |
| Scroll backward one line                                     | ^Y        |
| Move current line to top of screen and scroll                | z / Enter |
| Move current line to center of screen and scroll             | z. / zz   |
| Move current line to bottom of screen and scroll             | z-        |
| Redraw the screen                                            | ^L        |
| Move to home-the top line of screen                          | H         |
| Move to home-the middle line of screen                       | M         |
| Move to home-the bottom line of screen                       | L         |
| Move to first character of next line                         | + / Enter |
| Move to first character of previous line                     | -         |
| Move to first nonblank character of current line             | ^         |
| Move to column n of current line                             | n\|       |
| Move to end of word                                          | e         |
| Move to end of word(ignore punctuation)                      | E         |
| Move to beginning of current sentence                        | (         |
| Move to beginning of next sentence                           | )         |
| Move to beginning of current paragraph                       | {         |
| Move to beginning of next paragraph                          | }         |
| Move to beginning of current section                         | [[        |
| Move to beginning of next section                            | ]]        |
| 搜索相关                                                     | 命令      |
| Search forward for pattern                                   | /pattern  |
| Search backward for pattern                                  | ?pattern  |
| Repeat last search                                           | n         |
| Repeat last search in opposite direction                     | N         |
| Repeat last search forward                                   | /         |
| Repeat last serach backward                                  | ?         |
| Move to next occurrence of x in current line                 | fx        |
| Move to previous occurrence of x in current line             | Fx        |
| Move to just before next occurrence of  x in current line    | tx        |
| Move to just before previous occurrence of  x in current line | Tx        |
| Repeat previous find command in same direction               | ;         |
| Repeat previous find command in opposite direction           | ,         |
| Go to given line n                                           | nG        |
| Go to end of file                                            | G         |
| Return to previous mark of context                           | ``        |
| Return to beginning of line containing previous mark         | ''        |
| Show current line(not a movement command)                    | ^G        |

#4. Beyond the Basic

-  **Tabel 4-1 More editing commands􏰝􏰆􏰖􏰓􏰈 􏰱􏰲􏰳􏰘 􏰨􏰄􏰏􏰈 􏰈􏰇􏰒􏰍􏰒􏰁􏰐 􏰃􏰄􏰅􏰅􏰆􏰁􏰇􏰔􏰝􏰆􏰖􏰓􏰈 􏰱􏰲􏰳􏰘** 􏰨􏰄􏰏􏰈 􏰈􏰇􏰒􏰍􏰒􏰁􏰐 􏰃􏰄􏰅􏰅􏰆􏰁􏰇􏰔

| Change    | Delete    | Copy     | Form cursor to...         |
| --------- | --------- | -------- | ------------------------- |
| cH        | dH        | yH       | Top of screen             |
| cL        | dL        | yH       | Bottom of screen          |
| c+        | d+        | y+       | Next line                 |
| c5\|      | d5\|      | y5\|     | Column 5 of current line  |
| 2c)       | 2d)       | 2y)      | Second sentence following |
| c{        | d{        | y{       | Previous paragraph        |
| c/pattern | d/pattern | y/patter | Pattern                   |
| cn        | dn        | yn       | Next pattern              |
| cG        | dG        | yG       | End of file               |
| c13G      | d13G      | y13G     | Line number 13            |

## 4.1 Options when staring vi

- 指定位置打开文件

```nginx
# 光标在行首
# 打开文件
$ vi file
# 打开文件，定位光标到 n 行
$ vi +n file
# 打开文件，定位光标到尾行
$ vi + file
# 打开文件到第一次匹配行
$ vi +/pattern file
# pattern中包含空格，必须使用引号
$ vim +/'- F' test.md 
or vim +/-\ F test.md
```

- Read-Only Mode

```nginx
$ vim -R file
or view filevim 
```

- Recovering a Buffer

```nginx
# 展示system已经保存的文件
$ ex -r 
or vi -r
# 恢复test文件
$ vi -r test
```

- Making Use of Buffers

```nginx
使用数字id表示保存删除文本，即9次
使用字符id表示保存copy文本，即a-z26次
```

- Recovering Deletions

```nginx
# type "，倒叙标识删除顺序
"2p
# 挨个查看删除内容，直到出现目标文本
"1pu.u.u etc
```

- Yanking to Named Buffers

```nginx
# 复制当前文本到 buffer d
"dyy
# 复制the next 7 line to buffer a
"a7yy
```

```nginx
# 在光标前粘贴 buffer d 中的内容
"dp
# 在光标前粘贴 buffer a 中的内容
"ap
```

```nginx
# 删除 buffer a 中的 5行内容
"a5dd 
```

- 如果使用 buffer name 的大写字母，复制或删除的文本将会追加到当前buffer中，可以选择移动或复制

```nginx
# 从当前光标删除到当前橘子结尾并保存到buffer z中
"zd)
# 移动 2 句
2)
# 追加 next senten到 buffer z中
"Zy)
```

- Marking Your Place


















