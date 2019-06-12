1. jQuery ui
2. jquery 插件：jq22.com
3. svg矢量图：扇形图、折线图。。。
4. 响应式：移动端开发，display：flex
5. less(插件)和sass(mac自带)是css升级版：前端工具
6. 异步模块加载：cmd、amd
7. 脚手架：yeoman
8. 饿了吗：vue。 知乎：react
9. 服务器渲染：服务器读取html文件返回给浏览器。适合做seo
10. MPA：multible pages application
11. url：路由地址、不同路由
12. **路由1 — 函数1** 视图函数(功能)
13. Django：**socket+html+sql**
14. MTV(model template viewdef). MVC(model(sql) view(前端) control(服务器))
15. 设计模式：23/21
16. 技术团队，前端、后台工程师

## 今日内容

1. jQuery插件
2. bootstrap框架(twitter)
   1. 基本使用
   2. 全局的css
   3. 组件
   4. bootstrap插件

### 1. jquery插件

1. jquery树，主要是文件夹树

### 2. bootstrap

1. char.js
2. **hero:搭建自己的博客**
3. **layoutit：栅格**
4. 副文本编辑器
5. 基于jquery实现
6. 全局css样式：栅格系、表格、表单、按钮、图片、辅助类
7. Normalize.css 重置样式库
8. `.container` 类用于固定宽度并支持响应式布局的容器。
9. .container-fluid
10. 栅格系统：最多12列，列偏移
    - 使用封装好的类
11. 排版
12. 中心内容
13. Marked text：内联文本标签
14. 对齐：
15. 表格
16. 状态类：active悬停、success绿、info蓝、waring黄、danger红
17. &times；

## 1. jQuery的插件

```css
https://www.jq22.com
```

## 2. bootstrap

### 1. 移动设备优先

- bootstrap是移动设备优先的
- 为了确保适当的绘制和触屏缩放，需要在 `<head>` 之中**添加 viewport 元数据标签**。

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

- 还可以针对移动端，把网页设置成禁止缩放

```html
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
```

### 2. 排版与链接

1. Normalize.css 是bootstrap提供的重置样式库

### 3. 布局容器

1. bootstrap提供页面和栅格系统的.container容器。
2. bs提供了两个，注意不能互相嵌套

- .container用于固定宽度支持响应式布局的容器

```html
<div class="container">
  ...
</div>
```

- .container-fluid用于100%宽度，占据全部视口(viewport) 的容器

### 4. 栅格系统

#### 4.1 简介

- Bootstrap 提供了一套响应式、移动设备优先的流式栅格系统，随着屏幕或视口（viewport）尺寸的增加，系统会自动分为最多12列。
- 包含了易于使用的预定义类，还有强大的[mixin 用于生成更具语义的布局。

1. 用于通过一系列的行(row)与列(col)的组合来创建页面布局。
2. “行（row）”必须包含在 `.container` （固定宽度）或 `.container-fluid` （100% 宽度）中，以便为其赋予合适的排列（aligment）和内补（padding）。
3. 通过“行（row）”在水平方向创建一组“列（column）”。
4. 你的内容应当放置于“列（column）”内，并且，只有“列（column）”可以作为行（row）”的直接子元素。
5. 类似 `.row` 和 `.col-xs-4` 这种预定义的类，可以用来快速创建栅格布局。Bootstrap 源码中定义的 mixin 也可以用来创建语义化的布局。
6. 通过为“列（column）”设置 `padding` 属性，从而创建列与列之间的间隔（gutter）。通过为 `.row` 元素设置负值 `margin` 从而抵消掉为 `.container` 元素设置的 `padding`，也就间接为“行（row）”所包含的“列（column）”抵消掉了`padding`。
7. 负值的 margin就是下面的示例为什么是向外突出的原因。在栅格列中的内容排成一行。
8. 栅格系统中的列是通过指定1到12的值来表示其跨越的范围。例如，三个等宽的列可以使用三个  `.col-xs-4` 来创建。
9. 如果一“行（row）”中包含了的“列（column）”大于 12，多余的“列（column）”所在的元素将被作为一个整体另起一行排列。
10. 栅格类适用于与屏幕宽度大于或等于分界点大小的设备 ， 并且针对小屏幕设备覆盖栅格类。 因此，在元素上应用任何 `.col-md-*` 栅格类适用于与屏幕宽度大于或等于分界点大小的设备 ， 并且针对小屏幕设备覆盖栅格类。 因此，在元素上应用任何 `.col-lg-*` 不存在， 也影响大屏幕设备。

### 5. 排版

1. 在标题内还可以包含 `<small>` 标签或赋予 `.small` 类的元素，可以用来标记副标题。

```html
<h1>h1. Bootstrap heading <small>Secondary text</small></h1>
```

2. 中心内容，通过添加 .lead 类可以让段落突出显示

```html
<p class="lead">hello world, hello html</p>
<p>hello world, hello html</p>
```

3. 内联文本元素

```html
You can use the mark tag to <mark>highlight</mark> text.
```

4. 对于被删除的文本使用 `<del>` 标签。

```html
<del>This line of text is meant to be treated as deleted text.</del>
```

5. 对于没用的文本使用 `<s>` 标签。

```html
<s>This line of text is meant to be treated as no longer accurate.</s>
```

6. 额外插入的文本使用 `<ins>` 标签。

```html
<ins>This line of text is meant to be treated as an addition to the document.</ins>
```

7. 为文本添加下划线，使用 `<u>` 标签。

```html
<u>This line of text will render as underlined</u>
```

8. 使用 `<small>` 标签包裹，其内的文本将被设置为父容器字体大小的 85%。
   - 行内元素赋予 `.small` 类以代替任何 `<small>` 元素。

```html
<small>This line of text is meant to be treated as fine print.</small>
```

9. 通过增加 font-weight 值强调一段文本。

```html
<strong>rendered as bold text</strong>
```

10. 用斜体强调一段文本

```html
<em>rendered as italicized text</em>
```

11. 通过文本对齐类，可以简单方便的将文字重新对齐。

```html
<p class="text-left">Left aligned text.</p>
<p class="text-center">Center aligned text.</p>
<p class="text-right">Right aligned text.</p>
<p class="text-justify">Justified text.</p>
<p class="text-nowrap">No wrap text.</p>
```

12. 改变大小写

```html
<p class="text-lowercase">Lowercased text.</p>
<p class="text-uppercase">Uppercased text.</p>
<p class="text-capitalize">Capitalized text.</p>
```

13. 基本缩略语

```html
<abbr title="attribute">attr</abbr>
<abbr title="HyperText Markup Language" class="initialism">HTML</abbr>
```

14. 地址

```html
<address>
  <strong>Full Name</strong><br>
  <a href="mailto:#">first.last@example.com</a>
</address>
```

15. 引用样式

```html
<blockquote>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
  <footer>Someone famous in <cite title="Source Title">Source Title</cite></footer>
</blockquote>

<blockquote class="blockquote-reverse">
  ...
</blockquote>
```

### 6. 表格

1. 为任意 `<table>` 标签添加 `.table` 类可以为其赋予基本的样式 — 少量的内补（padding）和水平方向的分隔线。
2. 通过 `.table-striped` 类可以给 `<tbody>` 之内的每一行增加斑马条纹样式。
3. 添加 `.table-bordered` 类为表格和其中的每个单元格增加边框。
4. 通过添加 `.table-hover` 类可以让 `<tbody>` 中的每一行对鼠标悬停状态作出响应。
5. 通过添加 `.table-condensed` 类可以让表格更加紧凑，单元格中的内补（padding）均会减半。

```html
<table class="table table-类名">
  ...
</table>
```

#### 6.1 状态类

- 通过这些状态类可以为**行**或**单元格**设置颜色。

| Class      | 描述                                 |
| :--------- | :----------------------------------- |
| `.active`  | 鼠标悬停在行或单元格上时所设置的颜色 |
| `.success` | 标识成功或积极的动作                 |
| `.info`    | 标识普通的提示信息或动作             |
| `.warning` | 标识警告或需要用户注意               |
| `.danger`  | 标识危险或潜在的带来负面影响的动作   |

```html
<!-- On rows -->
<tr class="active">...</tr>
<tr class="success">...</tr>
<tr class="warning">...</tr>
<tr class="danger">...</tr>
<tr class="info">...</tr>

<!-- On cells (`td` or `th`) -->
<tr>
  <td class="active">...</td>
  <td class="success">...</td>
  <td class="warning">...</td>
  <td class="danger">...</td>
  <td class="info">...</td>
</tr>
```

#### 6.2 响应式表格

- 将任何 `.table` 元素包裹在 `.table-responsive` 元素内，即可创建响应式表格，其会在小屏幕设备上（小于768px）水平滚动。当屏幕大于 768px 宽度时，水平滚动条消失。

```html
<div class="table-responsive">
  <table class="table">
    ...
  </table>
</div>
```

### 7.  表单

- 单独的表单控件会被自动赋予一些全局样式。所有设置了 **.form-control** 类的 <input>、<textarea>和 <select> 元素都将被默认设置宽度属性为 `width: 100%;`。 将 `label` 元素和前面提到的控件包裹在 **.form-group** 中可以获得最好的排列。

```html
<form>
  <div class="form-group">
    <label for="exampleInputEmail1">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" placeholder="Email">
  </div>
  <div class="form-group">
    <label for="exampleInputPassword1">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
  </div>
  <div class="form-group">
    <label for="exampleInputFile">File input</label>
    <input type="file" id="exampleInputFile">
    <p class="help-block">Example block-level help text here.</p>
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox"> Check me out
    </label>
  </div>
  <button type="submit" class="btn btn-default">Submit</button>
</form>
```

- 不要将表单组直接和输入框组混合使用。建议将输入框组嵌套到表单组中使用。

#### 7.1 内联表单

1. 为 `<form>` 元素添加 **.form-inline** 类可使其内容左对齐并且表现为 **inline-block** 级别的控件。**只适用于视口（viewport）至少在 768px 宽度时（视口宽度再小的话就会使表单折叠）。**
2. 宽度。在内联表单，我们将这些元素的宽度设置为 `width: auto;`，因此，多个控件可以排列在同一行。
3. 一定要添加label标签
   - 如果你没有为每个输入控件设置 `label` 标签，屏幕阅读器将无法正确识别。
   - 对于这些内联表单，你可以通过为 `label` 设置 `.sr-only` 类将其隐藏。
   - 还有一些辅助技术提供label标签的替代方案，比如 `aria-label`、`aria-labelledby` 或 `title` 属性。如果这些都不存在，屏幕阅读器可能会采取使用 `placeholder` 属性，如果存在的话，使用占位符来替代其他的标记，但要注意，这种方法是不妥当的。

```html
<form class="form-inline">
  <div class="form-group">
    <label class="sr-only" for="exampleInputEmail3">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail3" placeholder="Email">
  </div>
  <div class="form-group">
    <label class="sr-only" for="exampleInputPassword3">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword3" placeholder="Password">
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox"> Remember me
    </label>
  </div>
  <button type="submit" class="btn btn-default">Sign in</button>
</form>
```

- form-group、form-control、sr-only、input-group、btn-primary、input-group-addon

```html
<form class="form-inline">
  <div class="form-group">
    <label class="sr-only" for="exampleInputAmount">Amount (in dollars)</label>
    <div class="input-group">
      <div class="input-group-addon">$</div>
      <input type="text" class="form-control" id="exampleInputAmount" placeholder="Amount">
      <div class="input-group-addon">.00</div>
    </div>
  </div>
  <button type="submit" class="btn btn-primary">Transfer cash</button>
</form>
```

#### 7.2 水平排列的表单

- 通过为表单添加 **.form-horizontal** 类，并联合使用 Bootstrap 预置的栅格类，可以将 label 标签和控件组水平并排布局。这样做将改变 **.form-group** 的行为，使其表现为栅格系统中的行（row），因此就无需再额外添加 **.row** 了。

```html
<form class="form-horizontal">
  <div class="form-group">
    <label for="inputEmail3" class="col-sm-2 control-label">Email</label>
    <div class="col-sm-10">
      <input type="email" class="form-control" id="inputEmail3" placeholder="Email">
    </div>
  </div>
  <div class="form-group">
    <label for="inputPassword3" class="col-sm-2 control-label">Password</label>
    <div class="col-sm-10">
      <input type="password" class="form-control" id="inputPassword3" placeholder="Password">
    </div>
  </div>
  <div class="form-group">
    <div class="col-sm-offset-2 col-sm-10">
      <div class="checkbox">
        <label>
          <input type="checkbox"> Remember me
        </label>
      </div>
    </div>
  </div>
  <div class="form-group">
    <div class="col-sm-offset-2 col-sm-10">
      <button type="submit" class="btn btn-default">Sign in</button>
    </div>
  </div>
</form>
```

### 8. 被支持的控件

- 表单布局实例中展示了其所支持的标准表单控件。
- 文本域:支持多行文本的表单控件。可根据需要改变 `rows` 属性。

```html
<textarea class="form-control" rows="3"></textarea>
```

### 9. 下拉列表(select)

```html
<select class="form-control">
  <option>1</option>
  <option>2</option>
  <option>3</option>
  <option>4</option>
  <option>5</option>
</select>
```

- 对于标记了 `multiple` 属性的 `<select>` 控件来说，默认显示多选项。

```html
<select multiple class="form-control">
  <option>1</option>
  <option>2</option>
  <option>3</option>
  <option>4</option>
  <option>5</option>
</select>
```

### 10. 静态控件

- 如果需要在表单中将一行纯文本和 `label` 元素放置于同一行，为 `<p>` 元素添加 `.form-control-static`类即可。

### 11. 全局css中的类名

```css
.container 固定宽度容器
.container-fluid 100%宽度的容器
 栅格系统
.row
.col-lg- .col-md- .col-sm- .col-xs

文本颜色
text-muted
text-primary
text-success
text-danger
text-waring
text-info

背景颜色
bg-primary
bg-success
....

按钮
btn btn-default
btn btn-link
btn btn-success
btn btn-primary
....

对齐
.text-left
.text-right
.text-center
.text-justify 两端对齐 适应于英文

图片设置
.img-rounded
.img-circle
.img-thumbnail 

三角符号
.caret
关闭按钮
<button type="button" class="close" aria-label="Close"><span aria-hidden="true">&times;</span></button>
显示和隐藏内容
show/hidden

快速浮动
.pull-left 左浮动
.pull-right 右浮动
清除浮动
.clearfix
内容块居中
.center-block


表格
给table添加.table的类。默认给表格赋予少量的内补和边框
.table-striped 条纹状的
.table-bordered 带边框
.table-hover 状态类

表单
form
每组表单控件都会添加一个.form-group类中，表单控件通常都由.form-control
```

## 3. 组件

### 1. 组件(html+)化开发

- 全局组件：不管哪个页面，始终不变如：导航栏
- 局部组件

**字体图标使用注意**

1. 字体图标：不要和其他组件混合使用，嵌套一个span标签，font-awesome(字体图标)
2. 图标类不能和其它组件直接联合使用。它们不能在同一个元素上与其他类共同存在。应该创建一个嵌套的 `<span>` 标签，并将图标类应用到这个 `<span>` 标签上。
3. 图标类只能应用在不包含任何文本内容或子元素的元素上。可以把它们应用到按钮、工具条中的按钮组、导航或输入框等地方。

### 2. 下拉菜单和按钮

#### 1.下拉菜单

- **类.dropdown/up, divider(分割线)，dropdown-toggle**
- 将下拉菜单触发器和下拉菜单都包裹在 **.dropdown** 里，或者另一个声明了 `position: relative;` 的元素。然后加入组成菜单的 HTML 代码。
- 通过为下拉菜单的父元素设置 **.dropup** 类，可以让菜单向上弹出（**默认是向下弹出的**）。

```html
<div class="dropdown">
  <button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
    Dropdown
    <span class="caret"></span>
  </button>
  <ul class="dropdown-menu" aria-labelledby="dropdownMenu1">
    <li><a href="#">Action</a></li>
    <li><a href="#">Another action</a></li>
    <li><a href="#">Something else here</a></li>
    <!--分割符-->
    <li role="separator" class="divider"></li>
    <li><a href="#">Separated link</a></li>
  </ul>
</div>
```

#### 2. 按钮组

- 当为 `.btn-group` 中的元素应用工具提示或弹出框时，必须指定 `container: 'body'` 选项，这样可以避免不必要的副作用（例如工具提示或弹出框触发时，会让页面元素变宽和/或失去圆角）。

1. **类为.btn-group, 还有各种颜色类：btn-defalut(primary, info, success, warning, danger)**

```html
<div class="btn-group" role="group" aria-label="...">
			<button type="button" class="btn btn-default">Left</button>
			<button type="button" class="btn btn-primary">Middle</button>
			<button type="button" class="btn btn-success">Right</button>
</div>
```

2. **按钮工具栏，在.btn-toolbar中内嵌.btn-group**
3. 只要给 `.btn-group` 加上 `.btn-group-*` 类，就省去为按钮组中的每个按钮都赋予尺寸类了，如果包含了多个按钮组时也适用。(btn-group-lg/sm/xs)
4. 想要把下拉菜单混合到一系列按钮中，只须把 `.btn-group` 放入另一个 `.btn-group` 中。

```html
<div class="btn-group" role="group" aria-label="...">
		<button type="button" class="btn btn-warning">Right</button>
		<button class="btn btn-info dropdown-toggle" type="button" data-toggle="dropdown">
			  Dropdown<span class="caret"></span>
		</button>
				<ul class="dropdown-menu dropdown-menu-right" aria-labelledby="dropdownMenu1">
            <li class="disabled"><a href="#">Action</a></li>
            <li><a href="#">Another action</a></li>
            <li><a href="#">Something else here</a></li>
            <!--分割符-->
            <li role="separator" class="divider"></li>
            <li><a href="#">Separated link</a></li>
				</ul>
		</button>
</div>
```

- 垂直排列 .btn-group-vertical

```html
<div class="btn-group-vertical" role="group" aria-label="...">
  ...
</div>
```

5. 两端对齐排列的按钮组
   - 让一组按钮拉长为相同的尺寸，填满父元素的宽度。对于按钮组中的按钮式下拉菜单也同样适用。

6.  **btn-group-justified**
   - 为了将 `<button>` 元素用于两端对齐的按钮组中，**必须将每个按钮包裹进一个按钮组中**

7. 单按钮下拉菜单
   - 按钮尺寸类 **btn-lg/sm/xs**

```html
<div class="btn-group">
		<button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
			Action <span class="caret"></span>
		</button>
		<ul class="dropdown-menu">
			<li><a href="#">Action</a></li>
			<li><a href="#">Another action</a></li>
			<li><a href="#">Something else here</a></li>
			<li role="separator" class="divider"></li>
			<li><a href="#">Separated link</a></li>
		</ul>
</div>
```

8. 分裂式按钮

```html
<div class="btn-group">
		<button type="button" class="btn btn-danger">Action</button>
		<button type="button" class="btn btn-danger dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
			<span class="caret"></span>
			<span class="sr-only">Toggle Dropdown</span>
		</button>
		<ul class="dropdown-menu">
			<li><a href="#">Action</a></li>
			<li><a href="#">Another action</a></li>
			<li><a href="#">Something else here</a></li>
			<li role="separator" class="divider"></li>
			<li><a href="#">Separated link</a></li>
		</ul>
</div>
```

9. 向上弹出式菜单
   - 给父元素添加 `.dropup` 类就能使触发的下拉菜单朝上方打开。

```html
<div class="btn-group dropup">
  <button type="button" class="btn btn-default">Dropup</button>
  <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    <span class="caret"></span>
    <span class="sr-only">Toggle Dropdown</span>
  </button>
  <ul class="dropdown-menu">
    <!-- Dropdown menu links -->
  </ul>
</div>
```

### 3. 输入框组

- 通过在文本输入框 `<input>` 前面、后面或是两边加上文字或按钮，可以实现对表单控件的扩展。为 `.input-group` 赋予 `.input-group-addon` 或 `.input-group-btn` 类，可以给 `.form-control` 的前面或后面添加额外的元素。
- 不支持在输入框的单独一侧添加多个额外元素（.input-group-addon 或 .input-group-btn）。
- 我们不支持在单个输入框组中添加多个表单控件。

#### 3.1 input-group

```html
<div class="input-group">
  <input type="text" class="form-control" placeholder="Recipient's username" aria-describedby="basic-addon2">
  <span class="input-group-addon" id="basic-addon2">@example.com</span>
</div>
```

#### 3.2 input-group-lg/sm

- 为 .input-group 添加相应的尺寸类，其内部包含的元素将自动调整自身的尺寸。不需要为输入框组中的每个元素重复地添加控制尺寸的类。
- **没有xs尺寸**

```html
<div class="input-group input-group-sm">
	  <input type="text" class="form-control" placeholder="Recipient's username" aria-describedby="basic-addon2">
	  <span class="input-group-addon" id="basic-addon2">@example.com</span>
</div>
```

#### 3.3 input-group-addon

- 可以将多选框或单选框作为额外元素添加到输入框组中。

```html
<div class="row">
  <div class="col-lg-6">
    <div class="input-group">
      <span class="input-group-addon">
        <input type="checkbox/radio" aria-label="...">
      </span>
      <input type="text" class="form-control" aria-label="...">
    </div><!-- /input-group -->
  </div>
</div>
```

#### 3.4 input-group-btn

- 为输入框组添加按钮需要额外添加一层嵌套，不是 `.input-group-addon`，而是添加 `.input-group-btn` 来包裹按钮元素

```html
<div class="row">
	  <div class="col-lg-6">
      <div class="input-group">
        <span class="input-group-btn">
        <button class="btn btn-default" type="button">Go!</button>
        </span>
        <input type="text" class="form-control" placeholder="Search for...">
      </div>
	  </div>
</div>
```

- 在一侧加入多个按钮

```html
<div class="input-group">
  <div class="input-group-btn">
    <!-- Buttons -->
  </div>
  <input type="text" class="form-control" aria-label="...">
</div>
```

### 4. 导航

- Bootstrap 中的导航组件都依赖同一个 **.nav** 类，状态类也是共用的。改变修饰类可以改变样式。
- 不要将 role 属性添加到 `<ul>` 上，因为这样可以被辅助设备（残疾人用的）上被识别为一个真正的列表。

#### 4.1 nav-taels

- 注意 `.nav-tabs` 类依赖 `.nav` 基类。

```html
<ul class="nav nav-tabs">
  <li role="presentation" class="active"><a href="#">Home</a></li>
  <li role="presentation"><a href="#">Profile</a></li>
  <li role="presentation"><a href="#">Messages</a></li>
</ul>
```

#### 4.2 nav-pills

- 胶囊式

```html
<ul class="nav nav-pills">
  <li role="presentation" class="active"><a href="#">Home</a></li>
  <li role="presentation"><a href="#">Profile</a></li>
  <li role="presentation"><a href="#">Messages</a></li>
</ul>
```

#### 4.3 nav-stacked

- 胶囊是标签页也是可以垂直方向堆叠排列的。只需添加 `.nav-stacked` 类。

```html
<ul class="nav nav-pills nav-stacked">
  ...
</ul>
```

#### 4.4 .nav-justified

- 已经弃用

```html
<ul class="nav nav-tabs nav-justified">
  ...
</ul>
<ul class="nav nav-pills nav-justified">
  ...
</ul>
```

#### 4.5 .disabled

- 对任何导航组件（标签页、胶囊式标签页），都可以添加 `.disabled` 类，从而实现**链接为灰色且没有鼠标悬停效果**。

```html
<li role="presentation" class="disabled"><a href="#">Profile</a></li>
```

### 5. 导航条

- 务必使用 `<nav>` 元素，或者，如果使用的是通用的 `<div>` 元素的话，务必为导航条设置 `role="navigation"` 属性，这样能够让使用辅助设备的用户明确知道这是一个导航区域。

#### 5.1 示例

```html
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="#">Brand</a>
    </div>
    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li class="active"><a href="#">Link <span class="sr-only">(current)</span></a></li>
        <li><a href="#">Link</a></li>
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="#">Action</a></li>
            <li><a href="#">Another action</a></li>
            <li><a href="#">Something else here</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">Separated link</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">One more separated link</a></li>
          </ul>
        </li>
      </ul>
      <form class="navbar-form navbar-left">
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Search">
        </div>
        <button type="submit" class="btn btn-default">Submit</button>
      </form>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="#">Link</a></li>
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="#">Action</a></li>
            <li><a href="#">Another action</a></li>
            <li><a href="#">Something else here</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">Separated link</a></li>
          </ul>
        </li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
```

#### 5.2 .navbar-brand

- navbar-primary/Info/warning/danger
- navbar-header
- 图标

```html
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">
        <img alt="Brand" src="...">
      </a>
    </div>
  </div>
</nav>
```

#### 5.3 .navbar-form

- `.navbar-form` 和 `.form-inline` 的大部分代码都一样，内部实现使用了 mixin。
- navbar-collapse
- 如果你没有为输入框添加 `label` 标签，屏幕阅读器将会遇到问题。对于导航条内的表单，可以通过添加 `.sr-only` 类隐藏 `label` 标签。

```html
<form class="navbar-form navbar-left" role="search">
  <div class="form-group">
    <input type="text" class="form-control" placeholder="Search">
  </div>
  <button type="submit" class="btn btn-default">Submit</button>
</form>
```

#### 5.4 .navbar-btn

- 对于不包含在 `<form>` 中的 `<button>` 元素，加上 `.navbar-btn` 后，可以让它在导航条里垂直居中。

```html
<button type="button" class="btn btn-default navbar-btn">Sign in</button>
```





**Bootstrap 的所有 JavaScript 插件都依赖 jQuery**

1. data-toggle都是与bootstrap插件有关
2. data-target：目标模态
3. data-dismass：关闭
4. 模态框
5. 监听页
6. collapse
7. carousel
8. 弹出框
9. 标签页
10. Index2/ demo









