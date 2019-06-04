// sort方法
// a = [2,1,13,4,56,6, 'henry'];
// for (var i = 0; i < a.length; i++){
// 	var s_i = (a[i].toString()).charCodeAt(0);
// 	console.log(a[i].toString());
// 	console.log(s_i);
// }
// console.log(a.sort());
// console.log(a.sort());

// var url = 'https://www.bai du.com';
// var a1 = encodeURI(url);
// var a2 = encodeURIComponent(url);
// console.log(a1);
// console.log(a2);
// console.log(decodeURI(a1));
// console.log(decodeURIComponent(a2))
// 



// var color = 'red';
// function test(){
// 	alert(window.color);
// }
// test();


// 获取随机颜色
// 获取0-256之间的随机数
function random(min, max){
	return min + Math.floor(Math.random() * max);	
}
// 
// function randomColor(){
// 	var r = random(0, 256),
// 		g = random(0, 256),
// 		b = random(0, 256);
// 	return `rag(${r},${g},${b} )`;
// }
// 
// var color = randomColor();
// console.log(color);
// 




// 随机验证码
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










