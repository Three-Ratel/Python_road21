1. 属性操作
   - **attr / removeattr**
   - prop / removeprop
2. 文档操作
   - 增删改查
3. 事件
4. ajax()
5. jq插件
6. jq22.com

### 1. 属性操作

#### 1.1 attri/removeAttr

- setAttribute/get...
- **只能获取标签上的属性**

```js
// 文档加载jq中
$(document).ready(function(){$('p')});
// 文档加载完成后，调用回调函数，无覆盖现象
jQuery(function(){});
$(function(){
  $('p').attr('title', 'henry');
  $('p').attr({'title':'henry',
              'color':'red'});
  // 获得属性,需要一个属性名
  $('p').attr('title');
  // 移除(一个或多个)
  $('p').removeAttr('title id a');
})；

// js中使用,js中的事件有覆盖现象
window.onload = function(){
  console.log(222);
};
window.onload = function(){
  console.log(111);
}
```

#### 1.2 prop/removeProp

- 只能在**对象内部**可以看到（console中）
- 用于input
- 获取当前**对象的属性**

```js
$(function(){
  $('input[type=radio]').eq(0).prop('checked');
$('input[type=radio]').eq(0).prop('type');
// 只能操作标签上的属性
$('input[type=radio]').eq(0).attr('a'， 1);
// 可以操作对象内部的属性
$('input[type=radio]').eq(0).prop('type');  
});
```

#### 1.3 h5

- jq22.com

```js
<h2>视频</h2>
<video width="" height="" controls="controls">
  <source src="知乎.mp4" type="video/mp4"></source>
</video>
// controls表示播放按钮
<h2>音频</h2>
<audio src="海贼王%20-%20ビンクスの酒(独唱).mp3" controls="controls">音频</audio>
```

### 2. 文档方法

#### 2.1 插入

1. append

- 父元素.append(子元素)；
- 通常谁调用返回值就是那个对象

```js
$('#box').append('henry');
// 追加一个标签
$('#box').append('<h2>echo</h2>');
$('#box').append(js对象);
// 如果参数是jq对象相当于移动操作
$('#box').append(jq对象);
```

2. appendTo

- 子元素.appendTo(父元素)；

```js
$('<a href="">百度一下  </a>').appendTo('#box');
// 链式编程思想，可以直接修改样式
$('<a href="">百度一下  </a>').appendTo('#box').css('yellow');
```

3. prepend

- 前置添加
- 用户最新数据的插入(博客园)

```js
$('#box').prepend('<h2>echo</h2>');
```

4. prependTo

- 前置添加

```js
$('<a href="">百度一下  </a>').prependTo('#box');
```

5. before/after

```js
$('h2'）.before('henry');
```

6. insertBefore/After

```js
$('<a href="">百度一下  </a>').insertBefore('h2');
```

#### 2.2 替换

- replace
- 创建一个标签并替换

```js
$('#box ul').replaceWith('<a href="">百度一下</a>');
// .replaceAll()和.replaceWith()功能类似，但是目标和源相反。
$('<a href="">百度一下</a>').replaceAll('#box ul');
```

#### 2.3 删除

- remove
- 既移除标签又移除事件

```js
// 删除
$('button').click(function(){
    alert(111);
    $(this).css('color', 'red');
    $('#box').append($(this).remove());
})

```

#### 2.4 detach

- 保留事件

```js
// 不删除事件
$('button').click(function(){
    alert(111);
    $(this).css('color', 'red');
    $('#box').append($(this).detach());
})
```

#### 2.5 清空

```js
$('#box').empty();
$('#box').html('');
```

### 3. 事件

#### 3.1 click()

- 单击事件

#### 3.2 dblclick()

- 双击事件
- **解决单双击的冲突问题**
- setTimeout

#### 3.3 mousedown()/up()

- 鼠标按下/弹起触发事件

#### 3.4 mouseover()/out()

- 父元素设置，会波及到自元素
- 鼠标穿过父元素和子元素都会调用

```js
$('#box').mouseover(function(){
  console.log('进来了');
})
$('#box').mouseout(function(){
  console.log('出去了');
})
```

```js
// mouseover的传播效应
$('#box').mouseover(function(){
  console.log('进来了');
  $('#child').stop().slideDown(1000);
})
$('#box').mouseout(function(){
  console.log('出去了');
  $('#child').stop().slideUp(1000);
})
```

#### 3.5 mouseenter()/leave()

- 鼠标移入、移出事件
- 只对绑定元素有效
- 使用动画时，**先使用stop()**在使用动画

```js
// mouseenter
$('#box').mouseenter(function(){
  console.log('进来了');
  $('#child').stop().slideDown(1000);
})
$('#box').mouseleave(function(){
  console.log('出去了');
  $('#child').stop().slideUp(1000);
})
```

#### 3.6 合成事件

```js
$('#box').hover(function(){
  
},function(){})
```

#### 3.7 聚焦和失焦

```js
// 默认加载页面，聚焦
$('input[type=text]').focus();
// 聚焦事件
$('input[type=text]').focus(function(){
  console.log('聚焦了');
})
// 失焦事件
$('input[type=text]').blur(function(){
  console.log('失焦了');
})
```

#### 3.8 键盘按下

- **e**为jQuery对像，称为jq事件对象
- keyCode为按键的code

```js
$('input[type=text]').keydown(function(e){
  console.log(e.keyCode);
  switch (e.keyCode){
    	case 8:
      	$(this).val('');
     		break;
    	default:
      	break;
  }
})
```

#### 3.9 change

- 表单元素发生改变

#### 3.10 select

#### 3.11 submit

- 表单提交事件，默认的表单提交会优先响应
- sumit会触发form中的action行为
- **preventDefault**

```js
// 阻止默认事件方法1
<a href='javascript:void(0);'>;
<a href='javascript:;'>;
<form action='javascript:;'>;

// 阻止默认事件方法2
<script type="text/javascript">
    $('form').submit(function(e){
        e.preventDefault();
        console.log('11111');
 	 	})
</script>
```

### 4. ajax的使用

1. 绑定事件需要等待响应后
2. 请求头/体
3. 响应头/体
4. XHR

#### 4.1 ajax的使用

```js
// ajax，只针对与当前页面的局部进行刷新
var name = $('input[type=text]').val();
var pwd = $('input[type=password]').val();
$.ajax({
  url:'',
  method:'post';
  data:{
    a:name,
    b:pwd
	},
  success:function(res){
  	// {data:200}
  	if (res.data==200){
      setTimeout(function(){
        windown.open('网址', '_self')
      },3000)
    }
	}
});
```

#### 4.2 ajax实例

```js
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<script src="js/jquery.js" type="text/javascript" charset="utf-8"></script>
	</head>
	<body>
		<div id="box">
		</div>
		
		<script type="text/javascript">
			$(function(){
				$.ajax({
					url:'https://api.apeland.cn/api/banner/',
					methods:'get',
					success:function(res){
						console.log(res);
            // 根据响应中的data，判断响应是否成功，以及就数据进行操作
						if (res.code === 0 ){
							var name = res.data[0].name;
							var cover = res.data[0].cover;
							$('#box').append(`<img src=${cover} alt=${name}>`);
						}
					},
          // 出现错误时的操作
					err:function(err){
						console.log(err);
					},
					
				})
			})
		</script>
		
	</body>
</html>

```



























1. 数据库中没bool值
2. tinyint(1) / tinyint(0)

