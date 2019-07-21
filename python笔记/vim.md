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
| Open new line above cursor for new text      | O        |
| Delete line and substitute text              | S        |
| Overstrike existing characters with new text | R        |
| Join current and next line                   | J        |
| Toggle case                                  | ~        |
| Repeat last action                           | .        |
| Undo last change                             | u        |
| Restore line to original state               | U        |

# 2. Moving Around in a Hurry



