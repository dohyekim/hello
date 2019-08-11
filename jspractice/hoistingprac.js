f(); //fffffff

function f() {
	console.log('fffffff');
}

dd(); //ReferenceError: dd is not defined
let dd = function() {
	console.log('dddddddd');
}

// 즉, 변수에 할당한 함수표현식은 hoisting 대상이 아닙니다.

// let으로 선언한 변수는 선언하기 전까지는 존재하지 않는다.

if (typeof x === "undefined") {
	console.log("x doesn't exist or is undefined;");
} else {
	console.log(`${x}`)
} //ReferenceError: x is not defined

let x = 5;