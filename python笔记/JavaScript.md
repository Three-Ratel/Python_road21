##   1. javascript基础

- javascript 在网页中占据很重要的地位
- 解释型语言。与网页交互的语言
- Node.js
- html描述的网页结构、css描述网页样式、js网页交互
- **ECMA4.1(浏览器上最多)** ECMASript5.0

### 1.  js的引入方式

#### 1.1 行内

-  console.log(a)相当于print

```html
//鼠标点击后执行
<p id="" class="" onclick="console.log(2)">onclick</p>
```

#### 1.2 内嵌

- 可以写在html中的任意位置
- // 单行注释，/**/ 多行注释

```html
<script type='text/javascript'></script>
```

#### 1.3 外接

```html
<script type='text/javascript' src='js文件路径'></script>
```

### 2.  js语法(分号结束)

- 变量名是由数字、字母、下划线和$组成

#### 2.1 global 对象

- **window**

```javascript
console.log('hello world');  //window.log+tab,window是全局对象
alert('hello world');
var weather = prompt(message:'请输入今天天气');
```

#### 2.2 基本数据类型(5)

1. 基本数据类型：**栈存储**
   - number、字符串、boolean、undefined、 null

```javascript
var a = 2;             //num
var b = '2' + a;			 // string
var c = true;					 // boolean
console.log(typeof(a));
var e;                  //先声明后定义
console.log(e);         //值和类型都是undifined

var f = null;
console.log(f)					// 类型是undefiend，数值为null
console.log(typeof(f))  //空对象
```

- 如果**s**中有其他字符，则会报错NaN

```js
// str转num
var s = '123';
new_s = Number(s);
```

- 数字转换为字符串

```js
var num = 123;
new_s = num.toString();
```

#### 2.3 引用数据类型(3)

- heap存储，复杂数据类型
- **把变量置为None即销毁**
- **全局作用域、函数作用域**

1. **Array**

```js
//Array
var arr = ['henry' 'echo' 'dean'];
// 修改元素
arr[2] = 'diane';
arr.length;
```

2. **Object类型**

```javascript
//Object，定义在对象中的函数，即对象的方法
var obj = {name:'echo', age:19,
          fav:function(){
            console.log(this)
          }};
obj.fav()
```

3. **函数类型**

- 定义函数方式1

```javascript
//function,定义在对象中的函数即对象的方法,{}表示作用域，也是对象
function add(形参1, 形参2){
  var c = 2；
  return a+b;
};

console.log(add{2, 5});
```

- 函数表达式

```javascript
var add = function() {
};
```

- 自执行函数

```javascript
(function(){})();
```

#### 2.4 数字和运算符

- ++a 和 a++

```javascript
//递增、递减
var a = 1;
a += 1;
a++;
console.log(a)；
// a++ 的迷惑
var a = 4;
//先赋值后++
var c = a++;
console.log(c);
console.log(a);
// ++a 的迷惑
var a = 4;
//先++后赋值
var c = ++a;
console.log(c);
console.log(a);
```

#### 2.5 str拼接

```js
var name = 'henry', age = 19;
var str = name  + '今年是' + age + '岁';
//es6的模版string,必须是反引号
var str = `${name}今年${age}岁`; 
```

#### 2.6 array

- 解释器遇到var声明的变量，会把var声明的**变量提升**到全局变量作用域下，js文件最上方
- 函数名也会有此现象，函数中的变量没有

1. 数组的创建

```js
var arr = [1, 2, 'henry'];
// 索引取值
arr[0];
// 遍历
// 预解释，变量提升
// var c=2; 
for	(var i = 0; i < arr.length; i++){
		console.log(arr[i]);
}
```

2. **多维数组**

- 数组中包含数组的话称之为多维数组。(**数组的嵌套**)
- 可以通过将两组方括号链接在一起来访问数组中的另一个数组。

```js
arr[2][2];           //取到第二行，第二列
```

#### 2.7 流程控制

1. **与或非**

```js
&&;
||;
!;
```

2. **If…else**

```js
var score = 70;
if (score > 80){
    console.log('play');
}else if(score > 60){
    console.log('stay at home');
}else{
    console.log('study');
};
```

3. **switch**

```js
var weather = prompt('weather');
switch(weather){
  case 'nice':
    console.log('nice');
    break;
  case 'rain':
    console.log('rain');
    break;   
  default:
    console.log('bye')
    break;
}
```

4. **== 和 ===**

- == 比较的是值，与数据类型无关 2 == '2' 为true
- === 比较的是值和数据类型(即内存地址) 2 === '2' 为false

```js
// true
var a = 1 == '1';
// false
var a = 1 == 2;
var a = 1 == '1';
```

5. **循环**
   - 初始化循环变量、循环条件、更新循环变量

```js
// for循环
arr = [8, 9, 0]
for (var i = 0; i < arr.length; i++){
  
}
// while循环
var a = 1;
while (a < 100){
  console.log(a);
  a++;
}
// do...while
do{
  
}while(a < 100);
```

#### 2.8 函数

- 在Javascript中另一个基本概念是函数，它允许你在一个代码块中存储一段用于处理一个任务的代码，然后在需要的时候用一个简短的命令来调用
- 一个**函数定义**(也称为**函数声明**，或**函数语句**)由一些列的**function**关键字组成。

```js
// function也会有变量提升现象
function fun(){
  console.log(arguments);
  switch(arguments.length){
    case 2:
      console.log(2);
    	break;
    case 3:
      console.log(3);
      break;
    default:break;
  }
}
fun(1, 2);
fun(3, 4, 5);
```

- 构造函数new

```js
new Object();
new Array();
new String();
new Number();
```



### 3. js常用对象

#### 3.1 object

1. **字面量创建方式**

```js
var Person = {
    name:'henry',
    age:19,
 	fav:function(){
    console.log(this);
  }
};

Person.fav();
console.log(Person.name);
console.log(Person.age);
```

2. **点语法,set&get**

- 函数中的this不一定是widow
- **对象**和**绑定事件**中的this指向当前obj
- 全局this指向window
- 一切皆对象

```js
var obj = {};
obj.name = 'henry';
console.log(obj.name)
obj.fav = function(){
  console.log(this);            // this 指向obj对象
};
obj.fav();
console.log(this);              // this window
```

3. **es6用class来创建对象**

```js
var obj = {name:'echo'};
var name = 'henry';
function add(x, y){
  this.x = x;
  this.y = y;
  console.log(this.name);
  console.log(this);
  console.log(x);
  console.log(y);
};

add();                           // 不可以改变this指向
add.call(obj, 1, 2);             // 可以改变this指向
add.apply(null, [1, 2]);         // 可以改变this指向
console.dir(add);
```

4. **构造函数创建对象**

```js
function Point(x, y) {
  this.x = x;
  this.y = y;
}

Point.prototype.toString = function () {
  return '(' + this.x + ', ' + this.y + ')';
};

var p = new Point(1, 2);
```

#### 3.2 Array

- new关键字实例化对象
- 构造函数

1. 字面量和构造函数

```js
var obj = new Array();
console.log(obj);
```

```js
var = arr['red', 'yellow', 'green'];
```

2. **检测数组**

```js
// if 内只有一行代码是可以省略大括号
if (Array.isArray(arr))
  console.log('true');
```

#### 3.3 Array(10)

1. **join**

```js
var arr = ['red', 'green']
Array.isArray(arr);               // 判断arr是否是数组，返回true则是
arr.toString();                   // 把数组中内容取出，用逗号拼接

num = 123;
num.toString();                   // 数字转字符串
arr.join('||');                   // 以||拼接
```

2. **栈方法**

```js
push()
pop()
var val = arr.pop();              // 返回删除的内容
console.log(val);									// val是pop的返回值
console.log(arr);

console.log(arr.push('xixixi'));; // 返回值为res，最新数组长度
console.log(arr);
```

3. **unshift方法**

```js
shift()
unshift()
var val = arr.unshift('heiheihei', 'hahaha');// 往数组的前面填充内容
console.log(arr);
console.log(val);                            // 返回数组最新长度    
console.log(arr.shift());                    // 删除第一个
```

4. **splice**

```js
var names = ['henry', 'echo', 'dean'];
var val = names.splice(1, 0, 'diane');          // 在索引1位置添加
console.log(names);
console.log(val);
names.splice(1, 1);                            // 从索引1位置删除1个值
names.splice(1, 1, 'xixixi');                  // 从索引1位置替换1个
```

5. **reverse**

```js
var num = [5, 2, 3];
num.reverse();
```

6. **sort**

```js
// 会转换成字符串进行比较
a = [2,1,13,4,56,6, 'henry'];
console.log(a.sort());                       // [1, 13, 2, 4, 56, 6, "henry"]
```

7. **concat**

```js
// 数组拼接,并不改变原来值
var new_num = num.concat(1, 2, 3);
```

8. **slice**

```js
// 不会更改初始值
num = [1,2,3,4,5,4,3,2,1]
num.slice(5)                          // 索引5之后的所有值
num.slice(5,7)                        // 索引5-7 不包扩7
num.slice(-3,-1)                      // 倒数第三个到倒数第一个
num.slice(-3,-4)                      // 取不到值
```

9. **位置方法indexOf(0)**

- 返回索引
- 查不到返回-1
- lastIndexof();

```js
num = [1,2,3,4,5,4,3,2,1]
var a = num.indexOf(4);               // 3
var a = num.lastIndexOf(4);           // 5
```

10. 迭代方法

- every
- some
- filter
- map
- **forEach**

```js
// 回调函数
arr.forEach(function(item, index){
  console.log(index);
  console.log(item);
  });

function fn(){
  console.log(arguments);                 // arguments不是数组，伪数组
  for (var i = 0; i < arguments.length; i++){
    console.log(arguments[i]);
  }
}

fn(2,3,4);
fn.length;																// 形参个数                        
```

#### 3.4 string方法(11)

1. length

```js
s = 'henry';
console.log(s.length);
```

2. charAt(2);

```js
console.log(s.charAt(2));
```

3. charCodeAt(2); 字符编码

```js
console.log(s.charCodeAt(2));
```

4. concat(),继承

```js
console.log(s.concat('&echo'));
```

5. **slice(3, 7）**             
   -  索引3-7

```js
s = 'henry&echo';
s.slice(3,7);
```

6. substring(3, 7)        
   -  索引3-7

```js
s = 'henry&echo';
s.substring(3,7);
```

7. substr(3, 7)              
   - 取7个

```js
s = 'henry&echo';
s.substr(3,7);
```

8. indexof

```js
s = 'henry&echo';
s.indexof('o');                   // 数据类型要一致
```

9. lastIndexof

```js
s = 'henry&echo';
s.lastIndexOf('o');                   // 数据类型要一致
```

10. **trim**  

```js
s = '   he nry    ';
s.trim();
s.trimLeft();
s.trimRight();
s.trimEnd();
```

11. toLowerCase(), toUpperCase()

```js
s = 'henry';
s.toLowerCase();
s.toUpperCase();
```

#### 3.5 date内置对像

1. 创建日期对象

```js
var time = new Date();
```

2. getDate(): 1-31

```js
time.getDate();                           // 返回日期对象的第几天
```

3. getMonth()

```js
time.getMonth();                           // 返回月份，需要 + 1
```

4. getFullYear()

```js
time.getFullYear();
```

5. getDay():星期几的第几天，星期天是0
   - document.write(getDay());

```js
time.getDay();
```

6. getHours():0-23

```js
time.getHours();
```

7. getMinutes():0-59

```js
time.getMinutes();
```

8. getSeconds():0-59

```js
time.getSeconds();
```

9. 格式化方法 tolocalString

```js
1.time.toString();
// Sun Jun 09 2019 17:13:35 GMT+0800 (CST)
2.time.toLocaleString(); 
//6/9/2019, 5:13:35 PM
3.time.toDateString();
// "Sun Jun 09 2019"
4.time.toLocaleDateString();
// "6/9/2019"
5.time.toTimeString()
// "17:27:04 GMT+0800 (CST)"
6.time.toLocaleTimeString()
// "5:27:04 PM"
7.time.toGMTString(); 
// "Sun, 09 Jun 2019 09:27:04 GMT"
```

10. 时间综合示例

```js
var time = new Date();
console.log(time);
console.log(time.getDate());
console.log(time.getFullYear());
console.log(time.getMonth()+1);
console.log(time.getDay());
console.log(time.getHours());
console.log(time.getMinutes());
console.log(time.getSeconds());

console.log(time.toLocaleString());                 //2019/6/3 下午11:50:36
var weeks = ['星期天','星期一','星期二','星期三','星期四','星期五','星期六'];
console.log(weeks[date.getDay()]);
var day = weeks[date.getDay()];
document.write(`<a href="#">${day}</a>`)

var a =  1 < 2 ? "yes": "no";
console.log(a);
```

#### 3.6 三元运算

```js
var a = 1 > 2 ? 'yes': 'no';
```

####  3.7 定时器

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h2 id="time"></h2>
<script>
    var timeObj = document.getElementById('time');
    console.log(time);

    function getNowTime() {
        var time = new Date();
        var hour = time.getHours();
        var minute = time.getMinutes();
        var second = time.getSeconds();
        var temp = "" + ((hour > 12) ? hour - 12 : hour);
        if (hour == 0) {
            temp = "12";
        }
        temp += ((minute < 10) ? ":0" : ":") + minute;
        temp += ((second < 10) ? ":0" : ":") + second;
        temp += (hour >= 12) ? " P.M." : " A.M.";
        timeObj.innerText = temp;
    }

    setInterval(getNowTime, 20);
</script>

</body>
</html>
```

#### 3.8 字符串和数值转换(6)

1. parseInt('123.123');

```js
var s = '123';
parseInt(s);                     // 如果s中包含非数字，则只保留其数字部分，第一个字符为非数字则会报NaN
```

2. parseFloat('123.123');

```js
var s = '123.123';
parseFloat(s);
```

3. Var c = 6/0;  infinity

```js
var c = 6/0;                     // 会出现infinity
```

4. Number('123ad')

```js
Number('123d');                  // NaN: not a number
Number('123');
```

5. String(123);

```js
String(123);
```

6. toString(123);

```js
var a = 2;
a = a + '';
// 或者
a.toString();
```

#### 3.9 Math

1. Math.E
2. Math.LN10
3. min(), max()

```js
arr = [1,2,3,4,5]
var max = Math.max.apply(null, arr);
```

4. Math.ceil(), Math.floor(), Math.round():四舍五入

```js
var num = 25.7;
var num2 = 25.2;
alert(Math.ceil(num));           //26
alert(Math.floor(num));          //25
alert(Math.round(num));          //26
alert(Math.round(num2));         //25
```

5. **random** :（0-1）
   - 产生min-max之间的随机数

```js
function random(lower, upper) {
    return Math.floor(Math.random() * (upper - lower)) + lower;
}
```

#### 3.10 Global对象

- 不属于任何其他对象的属性和方法，最终都是window的属性和方法
- isNaN()、isFinite()、parseInt()以及 parseFloat()，实际上全都是 Global 对象的方法。
- Global 对象还包含其他一些方法。
- window.say

1. encodeURI(Componet)

- 一般来说，我们使用 encodeURIComponent()方法的时候要比使用 encodeURI()更多，因为在实践中更常见的是对查询字符串参数而不是对基础 URI 进行编码。

```js
var url = 'https://www.bai du.com';
var a1 = encodeURI(url);
var a2 = encodeURIComponent(url);
console.log(a1);
console.log(a2);
console.log(decodeURI(a1));
console.log(decodeURIComponent(a2))
// 使用 encodeURI()编码后的结果是除了空格之外的其他字符都原封不动，只有空格被替换成了 %20。
// 而 encodeURIComponent()方法则会使用对应的编码替换所有非字母数字字符
```

#### 3.11 window

```js
var color = "red";
function sayColor(){
    alert(window.color);
}
window.sayColor();                  // red
```

#### 3.12 示例

1. **获取随机颜色**

```js
// 获取0-256之间的随机数
function random(min, max){
	return min + Math.floor(Math.random() * max);
}
function randomColor(){
	var r = random(0, 256),
		g = random(0, 256),
		b = random(0, 256);
	return `rag(${r},${g},${b} )`;
}
var color = randomColor();
console.log(color);
```

2. **随机验证码**

```js
function creationCode(){
	var code = '';
	var code_l = 4;
	var s_code = Array(0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R', 'S','T','U','V','W','X','Y','Z');
  for (var i = 0; i < code_l; i++){
    s = s_code[random(0,37)]
    code += s;
  }
  return code;	
}
var code = creationCode();
console.log(code);
```



## 2. BOM&DOM

### 1. BOM

- browser object model
- 系统对话框
- 顶层对象是window(核心对象)

#### 1.1 alert()

```js
var a = window.alert('确定离开了')；
```

#### 1.2 confirm()

```js
// 有返回值，确定为true或取消为false
var a = window.confirm('确定删除？')；
```

#### 1.3 prompt()

```js
var a = window.promopt('今天天气怎么样？')
```

#### 1.4 定时方法(重点)

1. **一次性任务**

- setTimeout()

```js
// 延时2秒,异步、非阻塞
var i = 0;
timer = setTimeout(function(){
  console.log('hello world');
}, 2000);
// 清除定时器
clearTimeout(timer);
timer = setTimeout(function(){
  console.log('test your speed');
}, 2000);
console.log('看看阻不阻塞')
```

2. **周期性循环**

- 垃圾回收机制，这里回收不了
- 网页动画

```js
var i = 0;
timer = setInterval(function(){
  i++;
  console.log(i);
  if (i === 10){
    // 清除定时器
    clearInterval(timer);
  }
}, 1000);
```

#### 1.5 Location对象

- window中的属性
- 浏览器自带缓存和记录功能
- **hash模式：带#**
- **histroy模式：不带#**

```js
console.log(window.location);
console.log(window.location.host);
console.log(window.location.hostname);
console.log(window.location.herf);
console.log(window.location.origin);
console.log(window.location.port);
// console.log(window.location.reload());
reload: f reload();                                    // 方法
location.reload();
```

- **ajax**在不重载页面的情况下，对网页就进行操作

```js
// 刷新
setInterval(function(){
  // 一般用于测试
  // ajax用于局部刷新
  locatoin.reload();
}, 2000);
```




### 2. DOM

- document object model
- 对象：用户自定义对象、内建对象(native object)、宿主对象(window)(浏览器提供)
- node节点。元素节点（p, a, div...）
- 节点对象(元素节点(**属性节点**)(**文本节点**) (**注释节点**)) 

- **document.body  document.documentElement**

#### 2.1 获取元素节点(3)

- **window.document**

1. **通过id获取单个节点对象**

```js
var box = document.getElementById('box');
console.log(box);
console.dir(box);                                 // 查看box所有属性和方法
```

2. **通过标签获取节点对象**

- **结果为伪数组**

```js
var box = document.getElementsByTagName('div');
// 使用拍它思想，操作标签，点击任意一个改变样式，即改变类名
var li = document.getElementsByTagName('li');
			for (var i = 0; i < li.length; i++){
				// console.log(li[i]);
				// 这里的this指向当前对象
				this.onclick = function(){
					for (var j = 0; j < li.length; j++){
						this.className = '';
					}
					this.className='active-li';
				};
```

3. **通过类名获取**

```js
var lis = document.getElementsByClassName('active');
// 通过id获取时，
var box = document.getElementById('box');
console.log(box.children);
```

4. **事件**

- onclick()
- onmouseover()
- onmouseout()

#### 2.2 文档、body、html

```js
// 当前文档啊
console.log(document);
// html中的body
console.log(document.body);
// html
console.log(document.documentElement);
```

#### 2.3 样式操作

```js
// 属性全部使用驼峰式
box.style.color
box.style.backgroudColor
```

- 或者通过类名，利用索引找到具体某一个元素

```js
var box = window.document.getElementById('box');
console.log(box);
// 绑定事件
box.onmouseover = function(){
  this.style.backgroundColor = 'red';
}
box.onmouseout = function(){
  this.style.backgroundColor = 'yellowgreen';
}
```

- **flag标志**

```js
var isRed = true;
// 绑定事件
box.onclick = function(){
  if (isRed){
    this.style.backgroundColor = 'yellow';
    isRed = false;
  }else{
    this.style.backgroundColor = 'red';
    isRed = true;
  }
}
// 设置周期定时， 此时不能用this，因为this指向window
setInterval (function(){
  if (isRed){
    box.style.backgroundColor = 'yellow';
    isRed = false;
  }else{
    box.style.backgroundColor = 'red';
    isRed = true;}
},1000);
```

#### 2.4 属性设置(2)

1. **追加类**

```js
var p = window.document.getElementById('p1');
console.dir(p);
p.className += ' b';
// 会覆盖之前的类
p.className = 'b';
```

2. **设置属性方法**

```js
setAttribute(name, value);
getAttribute(name);
var p = document.getElementById('p1');
p.setAttribute('class', 'active');
// 自定义属性设置，只能在节点对象上
p.setAttribute('self', 'active'); 
// 不会显示到页面中的elements中
p.self = '123';	   
p.class;
p.title;
```

- 示例

```js
var p = window.document.getElementById('p1');
console.dir(p);
// p.className += ' b';
// p.className = 'b';
p.self = '123';			
// p.setAttribute('self', 'active'); 
isTrue = true;
p.onmouseover = function(){
  if (isTrue){
    this.className += ' b';
    isTrue = false;
  }else{
    this.className = 'a';
    isTrue = true;
  }
}
```

#### 2.5 节点操作

```js
var ul = document.getElementById('box');
// 创建节点
var li1 = document.createElement('li');
var li2 = document.createElement('li');
// 只设置文本
li1.innerText = '123';
// 设置li中的html内容
li1.innerHTML = '<a herf = ''>123</a>';
// 设置类名
l1i.setAttribute('class', 'active');
// 设置样式
li1.children[0].style.color = 'red';
li1.children[0].style.fontSize = 20px;
// 追加节点
ul.appendChild(li1);
// 在li1前插入li2
ul.insertBefore(li2, li1);
// 删除节点
ul.removeChild(li1);
```

- 示例

```js
var box = document.getElementById('box');
// 创建节点对象
var li1 = document.createElement('li');
var li2 = document.createElement('li');
// 设置节点内容和属性（2中设置内容方式）
li1.innerText = '123';
li1.innerHTML = "<a href=''>456</a>";
li1.setAttribute('class', 'active')
// 添加节点到父节点
box.appendChild(li1);
box.insertBefore(li2, li1);
// 删除孩子节点li1
box.removeChild(li1);
```

#### 2.6 遍历操作节点

```js
var data = [
  {id:1, name:'henry', age:19},
  {id:2, name:'echo', age:18},
  {id:3, name:'dean', age:28},
  {id:4, name:'oleg', age:26},
  {id:5, name:'diane', age:27}
]
for (var i = 0; i < data.length; i++){
  console.log(data[i].name);
  var li = document.createElement('li');
  li.innerHTML = `<p>${data[i].id}</p> <p>${data[i].name}</p><p>${data[i].age}</p>`;
  box.appendChild(li)
}
```

#### 2.7 示例

```js
var box = document.getElementById('imgBox');
var prev = document.getElementById('prev');
var next = document.getElementById('next');
num = 1;
next.onclick = function(){
  nextImg();
}
function nextImg(){
  if (num===4){
    num  = 1;
  }
  imgBox.src = `images/${num}.jpg`;
  num++;
}s
setInterval(function(){
  nextImg();
}, 1000);
```

### 3. 节点属性

- 在文档对象模型(DOM)中，每一个节点都是一个对象。DOM节点有三个重要的属性：

1. **nodeName**: 节点的名称
2. **nodeValue**：节点的值
3. **nodeType**: 节点的类型

#### 3.1 nodeName属性

- 节点的名称，是只读

1. 元素节点的nodeName与标签名相同
2. 属性节点的nodeName与属性的名称相同
3. **文本节点的nodeName永远是#text**
4. **文档节点的nodeName永远是#document**

#### 3.2 nodeValue属性

- 节点的值

1. **元素节点的 nodeValue 是 undefined 或 null** 
2. 文本节点的 nodeValue 是文本自身 
3. 属性节点的 nodeValue 是属性的值

#### 3.3 nodeType 属性

- 节点的类型，是只读的。

**以下常用的几种结点类型:**

| 元素类型 | 节点类型 |
| -------- | -------- |
| 元素     | 1        |
| 属性     | 2        |
| 文本     | 3        |
| 注释     | 8        |
| 文档     | 9        |

- attributes属性是获取到该节点对象上的所有属性的集合
- childNodes属性是获取到该节点对象的所有子节点的集合

#### 3.4 示例

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>节点属性</title>
</head>
<body>
    <div id="box">我是一个文本节点<!-- 我是注释 --></div>
    <script type="text/javascript">
        // 1.获取元素节点
        var divNode = document.getElementById('box');
        console.log(divNode.nodeName + '|' + divNode.nodeValue + "/" + divNode.nodeType);
        // 2.获取属性节点
        var attrNode = divNode.attributes[0];
        console.log(attrNode.nodeName + '|' + attrNode.nodeValue + "/" + attrNode.nodeType);
        // 3.获取文本节点
        var textNode = divNode.childNodes[0];
        console.log(textNode.nodeName + '|' + textNode.nodeValue + "/" + textNode.nodeType);
        // 4.获取注释节点
        var commentNode = divNode.childNodes[1];
        console.log(commentNode.nodeName + '|' + commentNode.nodeValue + "/" + commentNode.nodeType);
        // 5.文档节点
        console.log(document.nodeName + '|' + document.nodeValue + "/" + document.nodeType);
    </script>
</body>
</html>
```

1. onchange
2. onselect
3. onsubmit
4. onload
5. onfocus
6. onblur

## 3. jquery

### 1. jQuery

- bootstrap(twitter)
- bootCDN(前端，在线外接资源)
- vue：没有html结构（ssr、nuxt）

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

- id、类、标签

```js
console.dir($);                           // jquery包含大量方法的对象
console.log($('#box'));                   // jquery对象，伪数组
console.log($('#box')[0]);                // jquery对象转节点对像
var box = document.getElementById('box'); // js对象
$(box)；                                  // js转jq对象
```

3. **高级选择器**
   - 子代、后代、组合、交集
   - 没有值代表没有获取到

```js
console.log($('.box>p'))                  // 子代选择器，jquery对象
console.log($('.box>p')[1])
// 组合选择器
$('box,active')
// 交集选择器
$('div.active')
// js对象
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
  - css('color')：是获取属性
  - css({'color':'red', …}):设置属性

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
- 获取索引方法：$(选择器).index()

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

- addClass('类1 类2...')
- removeClass('类1 类2...')
- toggoleClass('类')：开关式切换类名

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

#### 2.0 操作值的方法

1. **$('#btn').text('显示')**：修改btn的text内容为显示
   - 没有参数则是获得
2. **$('#btn').html(<p>hello</p>)**
   - html()：既获得标签，又获得文本
3. **$('#btn').val()**
   - 只针对于表单控件

#### 2.1 show/hide(毫秒,回调)

- 左上角，改变宽高

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

#### 2.2 slideDown/Up(毫秒,回调)

- 卷帘门，只改变盒子的高度

```js
// 在开启定时器时，需要先停止之前的定时器
$('#box').stop().toggle(2000);
$('#box').slideDown(2000);
$('#box').slideUp(2000); 
```

#### 2.3 fadeIn/Out(毫秒,回调)

- 淡入淡出，快速显示，通过透明度控制
- opacity:0-1 透明(0)

```js
$('#box').fadeIn(2000);
$('#box').fadeOut(2000);
// 动画不支持背景色，需要插件支持
$('#box').animater([params], speed, callback);
```

#### 2.4 toggle(毫秒,回调)

- 动画开关
- **slideToggole()**

```js
$('#box').toggle(2000, function(){});
```

#### 2.5 自定义动画

- animate({样式属性},毫秒,callback())
- display中的block和none的切换

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



## 4. jquery之ajax

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
5. **ajax实现前后端分离**

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

- **ajax练习**

```js
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>ajax练习</title>
		<script src="js/jquery.js" type="text/javascript" charset="utf-8"></script>
	</head>
	<body>
		<div id="box">
			<ul  type='none'></ul>
		</div>
		<div id="content">
			<ul></ul>
		</div1>
	
		<script type="text/javascript">
			// 获取导航头
			$.ajax({
				url:'https://www.luffycity.com/api/v1/course_sub/category/list/',
				methods:'get',
				success:function(res){
					console.log(res);
					$(`<li style='font-weight:bold')>全部<\/li>`).appendTo('#box ul').attr('id', 0);
					if (res.error_no===0){
						res.data.forEach(function(item,index){
							$(`<li type='none' style='font-weight:bold')>${item.name}<\/li>`).appendTo('#box ul').attr('id', item.id);
							
						})
					}
				}
			})
			
			// 获取课程
			var sub_category = 0;
			function get_course_list(sub_category){
				$.ajax({
					url:`https:\/\/www.luffycity.com/api/v1/courses/?sub_category=${sub_category}&ordering=`,
					method:'get',
					success:function(res){
						$('#content ul').empty();
						if (res.error_no===0){
							res.data.forEach(function(item, index){
								$(`<li>${item.name}<\/li>`).appendTo('#content ul').attr('id', item.id);	
							})
						}
					}
				})
			}
			get_course_list(sub_category);
			// jq中的事件委托
			$('#box ul').on('click', 'li', function(){
				var sub_category = $(this).attr('id');
				get_course_list(sub_category);
			});
		</script>
	</body>
</html>
```

## 5. bootstrap

- 在使用bootstrap的组件时，必须先引入jquery在引入bootstrap



















