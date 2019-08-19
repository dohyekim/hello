function avg(a,b) {
    return (a + b) / 2;
}
// a, b 는 formal argument(정해진 매개변수)
avg(5,10);
// 5, 10은 actual argument(실제 매개변수)


// 매개변수는 변수가 아닌 "값"을 할당받는다. call by value
function f(x) {
    console.log(`f 내부: x=${x}`); 
    x = 5;
    console.log(`f 내부: 할당 후의 x=${x}`);
}

let x = 3;
console.log(`f를 호출하기 전: x=${x}`); //x의 값인 3이 들어갈 것
f(x)
console.log(`f를 호출한 다음: x=${x}`); //밖의 x에는 아무런 영향 없음

// f를 호출하기 전: x=3
// f 내부: x=3
// f 내부: 할당 후의 x=5
// f를 호출한 다음: x=3


// 함수 안에서 객체를 변경하면 함수 바깥에서도 반영. call by reference
function g(p) {
    p.message = "g에서 수정함";
    p = {
        message : "새로운 객체!"
    };
    console.log(`할당 후 g 내부: p.message = "${p.message}"`)
}

let p = {
    message : "초기값"
};
console.log(`g를 호출하기 전: p.message = "${p.message}"`)

g(p);

console.log(`g를 호출한 다음:  p.message = "${p.message}"`);

// g를 호출하기 전: p.message = "초기값"
// 할당 후 g 내부: p.message = "새로운 객체!"
// g를 호출한 다음:  p.message = "g에서 수정함"

function h(x) {
    console.log(`in h: x=${x}`)
    return `in h: x=${x}`;
}
h(); //in h: x=undefined

//매개변수 해체
function getSentence({subject, verb, object}) {
    console.log(`${subject} ${verb} ${object}`);
    return `${subject} ${verb} ${object}`;
}

const q = {
    subject : "I",
    verb : "love",
    object : "Javascript",
}

getSentence(q); //I love Javascript

//확산 연산자 사용
function addPrefix(prefix, ...words) {
    const prefixedWords = [];
    for (let i = 0; i < words.length; i ++) {
        prefixedWords[i] = prefix + words[i];
    }
    console.log(prefixedWords);
    return prefixedWords;
}

addPrefix("con", "verse", "vex") //[ 'converse', 'convex' ]

