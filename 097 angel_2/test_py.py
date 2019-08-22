import jieba

a = '我要给源源打电话'
b = '我要给圆圆打电话'
c = '我要给元元打电话'

resa = jieba.cut(a)
resb = jieba.cut(b)
resc = jieba.cut(c)
print(list(resa))
resaa = jieba.cut_for_search(a)
print(list(resaa))

from pypinyin import lazy_pinyin, TONE, TONE2, TONE3

pya = lazy_pinyin(a, TONE)
pyb = lazy_pinyin(b, TONE2)
pyc = lazy_pinyin(c, TONE3)
print(pya)
print(pyb)
print(pyc)
