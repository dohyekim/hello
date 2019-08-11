'use strict';
// es6 기능: 블록 스코프 변수 선언
const sentences = [
	{ subject: "Javascript", verb: 'is', object: 'great' },
	{ subject: "Elephants", verb: 'are', object: 'large'},
];

// es6 기능: 객체 분해
function say({ subject, verb, object}) {
	console.log(`${subject} ${verb} ${object}`);
}

// es6 기능: for..of
for(let s of sentences) {
	say(s);
}