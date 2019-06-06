1. onchange
2. onselect
3. onsubmit
4. onload
5. onfocus
6. onblur



1. transition：过度
2. transform：3d
3. 设置值的操作

```html
// 闭合标签
innerText
innerHTML
// 表单控件
inputText.value = '123';
<input type='text' placeholder='请输入密码'>
```

## 今日内容

jquery

bootstrap(twitter)

bootCDN(前端，在线外接资源)

vue：没有html结构（ssr、nuxt）



### 1. jQuery

#### 1.1 简介

1. **html文档遍历和操作**、**事件处理**、**动画**和**Ajax**
   - **操作**：获取节点元素、属性、样式、类名、节点对象创建删除添加和替换
2. 基于面向对象、封装**大量方法**到对象(长度属性)
3. **js包含jQery**(write less，do more)

#### 1.2 jquery的使用

1. jquery.js(开发) / jquery.min.js(生产)
   - 生产环境会对代码优化
   - jquery.min.js代码文件大小会进行压缩
   - 严格模式和非严格模式(this指向问题)

```js
// 非严格模式
function fn(){
  // this是window
  console.log(this);
}
// 严格模式
function fn(){
  'use strict';
  // this是undifinded
  console.log(this);
}
```

2. **基础选择器**

```js
console.dir($);                           // jquery包含大量方法的对象
console.log($('#box'));                   // jquery对象，伪数组
console.log($('#box')[0]);                // jquery对象转节点对像
var box = document.getElementById('box'); // js对象
$(box)；                                  // js转jq对象
```

3. **后代选择器**
   - 没有值代表没有获取到

```js
console.log($('.box>p'))                  // 子代选择器，jquery对象
console.log($('.box>p')[1])               // js对象
console.log($('input[type=text]'));       // 属性选择器
```

4. **绑定事件**
   - **样式操作是css方法**
   - **$('#box.active').click(function(){})**
   - **绑定事件中的this指向当前的对象**

```js
$('#box.active').click(function(){
  // this指向当前js节点对象
  console.log(this);
  // 样式操作
  this.style....
  // js转换为jq，操作样式,不会覆盖
  $(this).css('color', 'red');
  $(this).css('font-size'(或使用驼峰), '20px');
 	// 或使用对象传值，遍历对象进行赋值
  $(this).css({'color':'red', 'font-size':40});
 	console.log($(this).css('color'));
});
```

- 样式修改之**css()**

```js
// 单独设置样式。不同种类的样式不会覆盖
$(this).css('font-size', '40px');
$(this).css('color','lightblue');
// 共同设置样式
$(this).css({
  'font-size':'40px',
  'color':'red',
})
// 获取属性值
console.log($(this).css('color'));\
```

5. **过滤选择器**

```js
// eq,gt,lt，odd，even，first，last
console.log($('ul li')[1];                        // js对象
console.log($('ul li:eq(1)'));                    // jq对象
console.log($('ul li:gt(1)'));                    // 。。。
console.log($('ul li:lt(1)'));                    // 。。。
console.log($('ul li:odd'));                      // 。。。
console.log($('ul li:even'));                     // 。。。
console.log($('ul li:first'));                    // 。。。
console.log($('ul li:last'));                     // 。。。
```

6. **筛选选择器**

- **find**、**children**、**parent**

```js
// 选中后代所有的span/a .find()
console.log($('ul').find('span'));
console.log($('ul').find('a'));
// 选中子代中的元素
console.log($('ul').children());
// parent(), document-html-body-...
console.log($('span').parent());
// 
console.log($('ul li').eq(1));
// siblings(),实现选项卡，排他性
console.log($('li').addClass('active').siblings('button').removeClass('active'));
// 当前点击元素索引
var index = $(this).index();
$('p').eq($(this).index()).addClass('active').siblings('p').removeClass('active')
```

- **链式编程**

```js
console.log($('span').parent().parent().parent().parent().parent());
```

7. **选项卡**

- **let可以把this限制在局部作用域中**

```js
// 选项卡方法一
for (var i = 0; i < btns.length; i++){
  btns[i].index = i;
  btns[i].onclick = function(){
    for (var j = 0; j < btns.length; j++){
      // console.log(this);
      btns[j].className = '';
      p[j].className = '';
    }
    this.className = 'active';
    p[this.index].className = 'active';
  }	
}
// 选项卡方法二
for (let i = 0; i < btns.length; i++){
  btns[i].onclick = function(){
    for (var j = 0; j < btns.length; j++){
      btns[j].className = '';
      p[j].className = '';
    }
    this.className = 'active';
    p[i].className = 'active';
  }
}
```

8. **jq实现选项卡**

```js
<!DOCTYPE html>
<html>
		<head>
        <meta charset="utf-8">
        <title>jq实现选项卡</title>
        <style type="text/css">
          	button.active{
              color: red;
            }
            p{
              display: none;
            }
            p.active{
              display: block;
            }
				</style>
		</head>
<body>
    <button class="active">热门</button>
    <button>电脑影音</button>
    <button>电脑</button>
    <button>家电</button>
    <p class="active">热门</p>
    <p>电脑影音</p>
    <p>电脑</p>
    <p>家电</p>

    <script type="text/javascript" src="js/jquery.js"></script>
    <script type="text/javascript">
        console.log($('button'));
        $('button').click(function(){
            // 处理点击的选项卡
            console.log($(this));
            $(this).addClass('active').siblings('button').removeClass('active');
            // 获取当前对象的索引
            console.log(($(this).index()));
            $('p').eq($(this).index()).addClass('active').siblings('p').removeClass('active');
    });
    </script>

	</body>
</html>
```

### 2. 动画

- **$('#btn').text('显示')**：修改btn的text内容为显示

#### 2.1 show/hide(毫秒数)

```js
$('#button').click(function(){
  // $('#box').show(2000);
  if($(this).text() === '显示'){
    
    $('#box').show(2000 function(){
      $('#button').text() === '隐藏');
    });
  })else{
    $(this).text() === '显示');
    $('#box').hide(2000);
  }
```

#### 2.2 slideDown/Up(毫秒)

```js
// 在开启定时器时，需要先停止之前的定时器
$('#box').stop().toggle(2000);
$('#box').slideDown(2000);
$('#box').slideUp(2000); 
```

#### 2.3 fadeIn/Out(毫秒)

```js
$('#box').fadeIn(2000);
$('#box').fadeOut(2000);
// 动画不支持背景色，需要插件支持
$('#box').animater([params], speed, callback);
```

#### 2.4 toggle(毫秒, 回调函数)

```js
$('#box').toggle(2000, function(){});
```

#### 2.5 自定义动画

```html
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        div {
            position: absolute;
            left: 20px;
            top: 30px;
            width: 100px;
            height: 100px;
            background-color: green;
        }
    </style>
    <script src="js/jquery.js"></script>
    <script>
        jQuery(function () {
            $("button").click(function () {
                var json = {"width": 500,
					"height": 500, 
					"left": 300, 
					"top": 300, 
					"border-radius": 100};
					
                var json2 = {
                    "width": 100,
                    "height": 100,
                    "left": 100,
                    "top": 100,
                    "border-radius": 100,
                    "background-color": "red"
                };

                //自定义动画
				$("div").animate(json, 1000, function () {
                    $("div").animate(json2, 1000, function () {
                        alert("动画执行完毕！");
                    });
                });

            })
        })
    </script>
</head>
<body>
<button>自定义动画</button>
<div></div>
</body>
</html>
```

























