1. BOM:browse object model
2. **DOM**:document object model
3. html:元素对象，有属性和方法

## 回顾

1. case穿透
2. == 等于。=== 等同于（值和数据类型即内存地址）
3. 给类的父对象
4. 原型对象
5. isNan
6. isFinity

## 今日内容

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
- hash模式：带#
- histroy模式：不带#

```js
console.log(window.location);
console.log(window.location.host);
console.log(window.location.hostname);
console.log(window.location.herf);
console.log(window.location.origin);
console.log(window.location.port);
// console.log(window.location.reload());
reload: f reload()  // 方法
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

- document object modle
- 对象：用户自定义对象、内建对象(native object)、宿主对象(window)(浏览器提供)
- node节点。元素节点（p, a, div...）
- 节点对象(元素节点(**属性节点**)(**文本节点**) 注释节点)

#### 2.1 获取元素节点(3)

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
// 使用拍他思想，操作标签，点击任意一个改变样式，即改变类名
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

#### 2.2 样式操作

```js
// 属性全部使用驼峰式
box.style.color
box.style.backgroudColor
```

- 更改局部样式时，需要使用**id获取元素**对象操作

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

#### 2.3 属性设置

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

#### 2.4 节点操作

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

#### 2.5 遍历操作节点

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

#### 2.6 示例

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
}

setInterval(function(){
  nextImg();
}, 1000);
```













