// 무한 loop
// let n = 0;
// while(true) { n += 0.1; if (n === 0.3) break;}
// console.log(`stopped at ${n}`);
// 0.1은 이진 표현으로 정확히 나타낼 수 없는 숫자

// 해결법
let n=0;
while(true) {
	n += 0.1;
	if(Math.abs(n-0.3) < Number.EPSILON) break;
}
console.log(`stopped at ${n}`)
// Number.EPSILON : 1에 더했을 때 1과 구분되는 결과를 만들 수 있는 가장 작은 수 

function MyNumberType(n) {
  this.number = n;
}

MyNumberType.prototype.valueOf = function() {
  return this.number;
};

const object1 = new MyNumberType(4);
console.log(`object1.number ==> ${object1.number}`)

console.log(object1 + 3);

// expected output: 7

const d = new Date(); //현재 날짜
const ts = d.valueOf();
console.log(`d.valueOf() ==> ${ts}`) //1565580012215

// 단축 평가
const skipIt = true;
let x = 0;
const result = skipIt || x++;
console.log(`x ====> ${x}`)  //x ====> 0

const noskip = false;
let y = 0
const result2 = noskip || y++;
console.log(`y ====> ${y}`)  //y ====> 1

const options = suppliedOptions || { name : "Default" }
//객체는 항상(빈 객체더라도) 참 같은 값으로 평가된다.
// 따라서 만일 suppliedOptions가 객체라면 options에는 suppliedOptions가 들어갈 것이고
// 그게 아니라면 거짓 같은 값이 되어 (null / undefined...) { name : "Default" }
// 값이 들어갈 것



// 할당 연산자
let v, v0;
v = v0 = 9.8













