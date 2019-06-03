// var Person = {
//     name:'henry',
//     age:19,
//  	fav:function(){
//     console.log(this);
//   }
// };
//
//
// Person.fav();
// console.log(Person.name);
// console.log(Person.age);


//
// var obj = {};
// obj.name = 'henry';
// console.log(obj.name)
// obj.fav = function(){
//   console.log(this);            // this 指向obj对象
// };
// obj.fav();
// console.log(this);              // this window



// var obj = {
//   name:'echo',
// };
// var name = 'henry';
//
// function add(x, y){
//   console.log(this.name);
//   console.log(this);
//   console.log(x);
//   console.log(y);
// };
//
//
// add();                           // 不可以改变this指向
// add.call(obj, 1, 2);            // 可以改变this指向
// add.apply(null, [1, 2]);          // 可以改变this指向
//
// console.dir(add);

// if 内只有一行代码是可以省略大括号
var arr = ['red' , 'green', 'blue', 'yellow'];
// if (Array.isArray(arr))
//   console.log('true');
//
// console.log(arr.toString());


// num = 123;
// console.log(num.toString());
// console.log(arr.join('||'));

// var val = arr.pop();
// console.log(val);
// console.log(arr);
//
// console.log(arr.push('xixixi'));;
// console.log(arr);


// var val = arr.unshift('heiheihei', 'hahaha');
// console.log(arr);
// console.log(val);
//
//
// console.log(arr.shift());



// var names = ['henry', 'echo', 'dean'];
// var val = names.splice(1, 0, 'diane');          // 在索引1位置添加
// console.log(names);
// console.log(val);
// names.splice(1, 1);                            // 从索引1位置删除1个值
// names.splice(1, 1, 'xixixi');                  // 从索引1位置替换1个

// arr.forEach(function(item, index){
//   console.log(index);
//   console.log(item);
//   });
//
// function fn(){
//   console.log(arguments);                 // arguments不是数组，伪数组
//   for (var i = 0; i < arguments.length; i++){
//     console.log(arguments[i]);
//   }
// }
// fn(2,3,4);
// fn.length;



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
console.log(weeks[time.getDay()]);
var day = weeks[time.getDay()];
document.write(`<a href="#">${day}</a>`)

var a =  1 < 2 ? "yes": "no";
console.log(a);







