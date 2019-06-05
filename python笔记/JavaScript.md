## 1. javascript基础

- javascript 在网页中占据很重要的地位
- 解释型语言。与网页交互的语言
- Node.js
- html描述的网页结构
- css描述网页样式
- js网页交互
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
var obj = {name:'echo', age:19;
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
var c = a++;                 //先赋值后++
console.log(c);
console.log(a);
// ++a 的迷惑
var a = 4;
var c = ++a;                 //先++后赋值
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

```js
var arr = [1, 2, 'henry'];
//索引取值
arr[0];
//遍历
//预解释，变量提升
// var c=2; 
for	(var i = 0; i < arr.length; i++){
		console.log(arr[i]);
}
```

2. **多维数组**

- 数组中包含数组的话称之为多维数组。(数组的嵌套)
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

- 函数中的this不一定widow
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

- **es6用class来创建对象**

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

- 构造函数创建对象

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

3. unshift方法

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
- lastindexof();

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

9. lastindexof

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

#### 3.5 data内置对像

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
time.toString();                          // "Tue Jun 04 2019 09:23:58 GMT+0800 (中国标准时间)"
time.toLocaleString();                    //"2019/6/4 上午9:23:58
time.toDateString();                       // "Tue Jun 04 2019"
time.toLocaleDateString();                 //"2019/6/4"
time.toGMTString();                        //"Tue, 04 Jun 2019 01:23:58 GMT"
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

- 更改局部样式时，需要使用**id获取元素**对象操作
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

#### 1.nodeName属性

- 节点的名称，是只读

1. 元素节点的nodeName与标签名相同
2. 属性节点的nodeName与属性的名称相同
3. **文本节点的nodeName永远是#text**
4. **文档节点的nodeName永远是#document**

#### 2.nodeValue属性

- 节点的值

1. **元素节点的 nodeValue 是 undefined 或 null** 
2. 文本节点的 nodeValue 是文本自身 
3. 属性节点的 nodeValue 是属性的值

#### 3.nodeType 属性

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

#### 4. 示例

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





















