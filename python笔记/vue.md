## 1. ES6的基本使用

### 1. let用法

#### 1. 变量提升

```html
<script>
	console.log(a);
    { var a = 1;}
    console.log(a);
</script>
```

#### 2. let

-   如果不使用let，`a[2]()`，使得变量 i 为局部变量
-   不存在变量提升
-   不可以重复声明

```html
!+tab键
<script>
	var a = [];
    for (let i = 0; i < 10; i++){
        a[i] = function(){
            console.log(i)
        };
    }
    a[2]();
</script>
```

### 2. const

-   const是局部作用域，不会存在变量提升，不能重复声明
-   常量不可以进行修改

```html
<script>
	console.log(a);
    { const a = 1;}
    console.log(a);
</script>
```

### 3. 模版字符串

```js
let name = "henry"
let str = `我是${name}`
```

### 4. es6的函数

```js
// es5
function add(x){
    return x
}
add(5);
// 或者
let add = functoin(x){
    return x
}
add(10)

// es6中的函数
let add2 = (x)=>{
    return x
}
// 或者
let add2 = x => x; 
console.log(add2(20))
```

```js
var person = {
    name: 'henry',
    hobby: function () {
        console.log(this);			// this 是当前对象
        console.log(this.name);
    }
};
person.hobby();

// 箭头函数
var person = {
    name: 'henry',
    hobby: ()=> {
        console.log(this);			// this 指向定义person的父级对象(上下文)
        console.log(this.name);
    }
};
person.hobby();

// 对象的单体模式
let person = {
    name:'henry',					
    hobby(){						// 等价于 hobby:function(){}
        console.log(this);			// this 指向当前对象
    }					
}
```

### 5. es6的类

-   原型 prototype 当前类的父类(继承性)

```js
function Person(name, age){
    this.name = name;
    this.age = age;
}
// 基于原型声明
Person.prototype.showName = () = >{
    console.log(this.name);
}

class Person{
    constructor(name='echo', age=19){
        this.name = name;
        this.age = age;
    }						// 不能加逗号
    showname(){
        console.log(this.name)
    }
    showage(){
        console.log(this.age)
    }
}
let v = new Person();
v.showname()
```

## 2. vue基本用法

### 1. vue介绍

-   声明式的**javascript**

#### 1. vue思想

-   数据驱动视图

#### 2. 前端的三大框架

1.  vue
    -   尤雨溪
2.  angular
    -   google公司
3.  react(高阶函数， es6)初学者不友好
    -   facebook

### 2. vue模版语法

#### 1. {{ 变量 }}

```html
<div id="app">
    {{ msg }}
    {{ 'hello' }}				<!--字符串-->
    {{ 1 + 1 }}					<!--运算-->
    {{ {'name': 'henry'} }}		<!--对象-->
    {{ 1>2? 'true' : 'false' }}	<!--三元运算-->
    <p>{{ who.split('').reverse().join('') }}</p>
	
</div>
<!--1. 引包-->
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script type="text/javascript">
	// 2. 实例化对象
    var app = new Vue({
        el: '#app',				// el即element必须是 el,绑定的标签
        data:{					// 数据对象，必须是 data 
            // 数据属性
            msg:'hello vue!'
            who: 'i am a vue app'
        },
        methods{
        	...
    	}
    })
</script>
```

#### 2. methods属性

-   所有的方法都放在 methods 对象中

```html
<div id="content">
    {{ add(2, 3) }}
</div>
<script>
    new Vue(){
        el:'#content',
        data(){
            // data 中是一个函数，要return 一个对象，可以是空对象
            return {
                msg:"<h2>henry</h2>"
            }
        },
       	methods:{
            add (x, y){
                return x + y
            }
        }
    }
</script>		
```

### 3. vue基本指令

-   使用指令系统时，值一定是**字符串格式** 


#### 1. v-text/v-html

```html
<div id="content">
    <div v-text="msg"></div>
    <div v-html="msg"></div>
</div>
</div>
<script>
    new Vue(){
        el:'#content',
        data(){
            // data 中是一个函数，要return 一个对象，可以是空对象
            return {
                msg:"<h2>henry</h2>"
            }
        }
    }
</script>		
```
#### 2. v-show

-   true则显示，false则不显示
-   只是控制样式，display属性

```html
<style>
    .box{
        height: 100px;
        width: 100px;
        background-color: red;
    }
</style>
<div id="content">
    <div class='box' v-show='isShow'></div>
    <button v-on:click='handlerClick'>隐藏</button>
</div>
<script>
    new Vue({
        el:'#content',
        data(){
            return {
                msg:"<h2>henry</h2>",
                isShow: true,
            }
        },
        methods:{
            add (x, y){
                return x + y
            },
            handlerClick(){
                console.log(this);
                this.isShow = !this.isShow
            }
        },
    })
</script>
```

#### 3. v-if

-   如果值为假，则会删除
-   为真则会添加

```html
<style>
    .box{
        height: 100px;
        width: 100px;
        background-color: red;
    }
    .box2{
        height: 100px;
        width: 100px;
        background-color: yellow;
    }
</style>
<div id="content">
    <button v-on:click='handlerClick'>隐藏</button>
    <div class='box' v-show='isShow'></div>
    <div class='box2' v-if='isShow'></div>
</div>
<script>
    new Vue({
        el:'#content',
        data(){
            return {
                msg:"<h2>henry</h2>",
                isShow: true,
            }
        },
        methods:{
            add (x, y){
                return x + y
            },
            handlerClick(){
                console.log(this);
                this.isShow = !this.isShow
            }
        },
    })
</script>
```

#### Note(4)

1.  `v-if` 是“真正”的条件渲染，因为它会确保在切换过程中条件块内的事件监听器和子组件适当地被销毁和重建。
2.  `v-if` 也是**惰性的**：如果在初始渲染时条件为假，则什么也不做——直到条件第一次变为真时，才会开始渲染条件块。
3.  相比之下，`v-show` 就简单得多——不管初始条件是什么，元素总是会被渲染，并且只是简单地基于 CSS 进行切换。
4.  一般来说，`v-if` **有更高的切换开销**，而 `v-show` **有更高的初始渲染开销**。因此，**如果需要非常频繁地切换**，则使用 `v-show` 较好；如果在**运行时条件很少改变**，则使用 `v-if` 较好。

#### 4. v-if / v-else

-   父盒子必须有绑定

```html
<div id="content">
    <div v-if="Math.random() > 0.5">
		Now you see me
    </div>
    <div v-else>
		Now you don't
	</div>
</div>
```

#### 5. v-bind / v-on

-   数据驱动，设计模式 mvvm，model view viewmodel
-   v-bind：可以绑定标签的所有属性和对象，如src、alt、href、title、id、class...
-   v-bind可以**省略不写**，v-on: 可以使用**@符号**代替
-    v-on：可以监听所有事件

```html
<style>
    .box{
        height: 100px;
        width: 100px;
        background-color: red;
    }
    .active{
        background-color: yellow;
    }
</style>
<div id="content">
    <button @click='handlerChange'></button>
    <img v-bind:src='imgSrc' v-bind:alt='msg'>
    <div class='box' :class'{active:isActive}'></div>
</div>

<script>
    new Vue({
        el:'#content',
        
        data(){
            return {
                imgSrc:'./test.jgp',
                msg:"美女",
                isActive:false,
            }
        },
        
        methods:{
            handlerChange(){
                console.log(this);
                this.isActive = !this.isActive
            }
        },
    })
</script>
```

#### 6. v-for

-   可以**遍历 list** 也可以**遍历对象**
-   需要绑定 id 或使用 index
-   v-for 的优先级最高

```html
<div id="app">
    <ul>
        <li v-for="(item, index) in data.users" :key="item.id">
            <h3>{{ item.id }}----{{ item.name }}</h3>
        </li>
    </ul>
    <!--遍历对象时，第一个时val第二个是key-->
    <div v-for="(value, key) in person">
    	{{ value }}
    </div>
</div>
<script src="./vue.js"></script>
<script>
    new Vue({
        el:'#app',
        data(){
            return{
                data:{
                    status:'ok',
                    users:[
                        {id:1, name:'henry'},
                        {id:2, name:'echo'},
                        {id:3, name:'dean'},
                    ]
                },
                person:{'name':'iris'}
            }

        },
    })
</script>
```





















