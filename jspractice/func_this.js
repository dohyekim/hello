// 함수에 이름을 정하고 다시 변수에 할당하는 경우
const g = function f(stop) {
    if(stop) console.log(`f stopped`);
    f(true);
};

// g(false); //RangeError: Maximum call stack size exceeded

//화살표 함수는 항상 익명이다
// const f1 = function() {return "hello!";}

const f1 = () => "hello!";

// const f2 = function(name) {return `Hello, ${name}`;}

const f2 = name => `Hello, ${name}`;

// const f3 = function(a, b) {return a + b;}

const f3 = (a,b) => a+b;