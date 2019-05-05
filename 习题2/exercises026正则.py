#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 正则表达式练习
# 1、匹配一篇英文文章的标题 类似 The Voice Of China
import re
# ret = re.findall(r'([A-Z](?:[a-zA-z]+)?)+', 'The Voice Of China')
# print(ret)


# 2、匹配一个网址
# s = 'https://www.baidu.com http://www.cnblogs.com'
# ret = re.findall('https?://www\.\w+\.com', s)
# print(ret)


# 3、匹配年月日日期 类似 2018-12-06 2018/12/06 2018.12.06
# s = '2018-12-06 2018/12/06 2018.12.06'
# ret = re.findall('\d{4}.?\d{2}.?\d{2}', s)
# print(ret)

# 4、匹配15位或者18位身份证号
# s = '34121219990101123434121219990101123x341212199901011'
# ret = re.findall(r'\d{17}[\dXx]|\d{15}', s)
# print(ret)


# 5、从lianjia.html中匹配出标题，户型和面积，结果如下：
# [('金台路交通部部委楼南北大三居带客厅   单位自持物业', '3室1厅', '91.22平米'), ('西山枫林 高楼层南向两居 户型方正 采光好', '2室1厅', '94.14平米')]
content = """"<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div class="info clear">
	<div class="title">
		<a class="" href="https://bj.lianjia.com/ershoufang/101103186217.html" target="_blank" data-log_index="1"
		   data-el="ershoufang" data-housecode="101103186217" data-is_focus="1" data-sl="">金台路交通部部委楼南北大三居带客厅   单位自持物业</a>
		<span class="new tagBlock">新上</span></div>
	<div class="address">
		<div class="houseInfo">
            <a href="https://bj.lianjia.com/xiaoqu/1111027381816/" target="_blank" data-log_index="1" data-el="region">延静西里 </a>
            <span class="divide">/</span>3室1厅<span class="divide">/</span>91.22平米<span class="divide">/</span>南 北<span class="divide">/</span>简装<span class="divide">/</span>有电梯
        </div>
	</div>
	<div class="flood">
		<div class="positionInfo">低楼层(共15层)
            <span class="divide">/</span>1984年建板塔结合
            <span class="divide">/</span>
            <a href="https://bj.lianjia.com/ershoufang/hongmiao/" target="_blank">红庙</a></div>
	</div>
	<div class="followInfo">859人关注<span class="divide">/</span>30次带看
		<div class="timeInfo"><span class="timeIcon"></span>6天以前发布</div>
		<div class="tag"><span class="subway">近地铁</span><span class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
		<div class="priceInfo">
			<div class="totalPrice"><span>570</span>万</div>
			<div class="unitPrice" data-hid="101103186217" data-rid="1111027381816" data-price="62487"><span>单价62487元/平米</span></div>
		</div>
	</div>
</div>
<div class="info clear">
    <div class="title">
        <a class="" href="https://bj.lianjia.com/ershoufang/101103188116.html" target="_blank" data-log_index="2"
           data-el="ershoufang" data-housecode="101103188116" data-is_focus="1" data-sl="">西山枫林 高楼层南向两居 户型方正 采光好</a>
        <span class="new tagBlock">新上</span><span class="yezhushuo tagBlock">房主自荐</span></div>
    <div class="address">
        <div class="houseInfo">
            <a href="https://bj.lianjia.com/xiaoqu/1111027381123/" target="_blank" data-log_index="2" data-el="region">西山枫林三期 </a>
            <span class="divide">/</span>2室1厅<span class="divide">/</span>94.14平米<span class="divide">/</span>南<span class="divide">/</span>简装<span class="divide">/</span>有电梯
        </div>
    </div>
    <div class="flood">
        <div class="positionInfo">中楼层(共10层)
            <span class="divide">/</span>2006年建板楼
            <span class="divide">/</span>
            <a href="https://bj.lianjia.com/ershoufang/pingguoyuan1/" target="_blank">苹果园</a></div>
    </div>
    <div class="followInfo">630人关注<span class="divide">/</span>23次带看
        <div class="timeInfo"><span class="timeIcon"></span>6天以前发布</div>
        <div class="tag"><span class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
        <div class="priceInfo">
            <div class="totalPrice"><span>495</span>万</div>
            <div class="unitPrice" data-hid="101103188116" data-rid="1111027381123" data-price="52582"><span>单价52582元/平米</span></div>
        </div>
    </div>
</div>
</body>
</html>"""
ret = re.finditer('<div class="title">.*?<a class=.*?>(?P<title>.*?)</a>.*?<span.*?>.*?</div>.*<div class="address">.*?\
<span class="divide">/</span>(?P<layout>.*?)<span.*?>/</span>(?P<area>.*?)<span class="divide">.*?/div>', content, flags=re.S)

for i in ret:
    print(i.group('title'), i.group('layout'), i.group('area'))

# 6、
s = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
# 从上面算式中匹配出最内层小括号以及小括号内的表达式
# ret = re.findall('', s)
# print(ret)


# 7、从类似9-2*5/3+7/3*99/4*2998+10*568/14的表达式中匹配出乘法或除法
# ret = re.findall('\d+[*/]\d+(?:[*/]\d+){0,}', '9-2*5/3+7/3*99/4*2998+10*568/14')
# print(ret)


# 8、通读博客，完成三级菜单
# http://www.cnblogs.com/Eva-J/articles/7205734.html

# 9、大作业：计算器