
const x = 3;

function f() {
	console.log(`In f(), x >> ${x};`)
	// console.log(`In f(), y >> ${y};`) //y is not defined
}

{
	const y = 4;
	f(); //In f(), x >> 3; 
	//함수 f는 자신이 정의될 때 접근할 수 있었던 식별자에는 여전히 접근할 수 있지만, 
	//호출할 때 스코프에 있는 식별자에는 접근할 수 없습니다.
}

// block scope
console.log('before block');

{
	console.log('inside block');
	const z = 3;
	console.log(z); // 3
}

// console.log(`outside block; x = ${z}`) //ReferenceError: z is not defined

let globalFunc;
console.log(typeof(globalFunc)) //undefined]\

{
	let blockVar = 'a';
	globalFunc = function () {
		console.log(blockVar);
	}
}

globalFunc //a

//globalFunc는 블록 안에서 값을 할당받았습니다. 이 블록 스코프와 그 부모인 전역 스코프가 클로저를 형성합니다.
// globalFunc()를 어디서 호출하든, 이 함수는 클로저에 들어있는 식별자에 접근할 수 있습니다.
// closure : 함수가 특정 스코프에 접근할 수 있도록 의도적으로 그 스코프에서 정의하는 것.


let ff;
{
	let o = {note:'Safe'};
	ff = function() {
		return o
	}
}
let oRef = ff();
console.log(oRef.note); //Safe 접근 가능
oRef.note = "Not so safe after all!"
console.log(oRef.note); //Not so safe after all!


// IIFE

// 1. 익명의 함수를 만듭니다.
const msg = function() {
	const secret = "I'm a secret!";
	return `The secret is ${secret.length} characters long.`;
}
msg()

// 함수를 선언하고 동시에 실행합니다.
const message = (function() {
	const secret = "I'm a secret!";
	return `The secret is ${secret.length} characters long.`;
})();

console.log(message); //The secret is 13 characters long.

a; //ReferenceError: a is not defined













