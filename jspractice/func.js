
function f1() {
	return "hello";
}

const f1 = function() {
	return "hello";
}

const f1 = () => "hello"

const f2 = function(name) { return `Hello, ${name}!`;}

const f2 = (name) => `Hello, ${name}!`;

const f3 = function(a,b) { return a + b; }

const f3 = (a,b) => a + b;

// arrow function은 익명 함수만 생성 가능
// 이름 있는 함수를 선언하고 싶으면 일반적인 function 선언을 사용하면 된다.