// 함수 선언
function sayHello() {
    console.log("Hello World!");
}

let res = sayHello(); //Hello World!
console.log(res) //undefined;

function getGreeting() {
    return "안녕하세요"
}
getGreeting();
getGreeting; 
// ƒ getGreeting() {
//     return "안녕하세요"
// }

//함수를 호출하지 않고 참조하게만 할 수도 있음 --> 할당 연산자와 같이 쓰일 수 있다.
const f = sayHello;
f(); //Hello World!

const o = {};
o.f = sayHello;
o.f(); //Hello World!

const arr=[1,2,3];
arr[1] = sayHello;
arr[1](); //Hello World!

