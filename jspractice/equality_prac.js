const t = 5;
const s = "5";
console.log(`t === s? ${t === s}`); //t === s? false
console.log(`t !== s? ${t !== s}`); //t !== s? true

console.log(`t === Number(s)? ${t === Number(s)}`); //t === Number(s)? true
console.log(`t !== Number(s)? ${t !== Number(s)}`); //t !== Number(s)? false

const a = { name : "an object" };
const b = { name : "an object" };
console.log(`a === b? ${a === b}`); //a === b? false
console.log(`a !== b? ${a !== b}`); //a !== b? true

// 숫자비교
console.log(`NaN === NaN? ${NaN === NaN}`); //NaN === NaN? false 
console.log(`NaN == NaN? ${NaN == NaN}`); //NaN == NaN? false

// 문자열 병합
console.log(3 + 5 + "8"); // 88
console.log("3" + 5 + 8); //"358"

// 단축평가 (||)
const skipIt = true;
let x = 0;
const result = skipIt || x++;
console.log(`x=?? ${x}`) //x=?? 0

const doIt = false;
let y = 0;
const res = doIt || y++;
console.log(`y=?? ${y}`) //y=?? 1

//피연산자가 불리언이 아닌 경우 반환값
const ff = false;
let z = 0;
const res2 = ff && z++;
console.log(`res2=?? ${res2}`) //result=?? false

const tt = true;
let ll = 0;
const res3 = tt && ll++;
console.log(`res3=?? ${res3}`) //res3=?? 0

// suppliedOptions가 객체이면 suppliedOptions를 리턴하고 아니면 기본값을 리턴
// const options = suppliedOptions || { name : "default" }

// 쉼표 연산자
let o = 0, p = 10, q;
q = (o++, p++)
console.log(`q=?? ${q}`) //q=?? 10

// 할당 연산자
const nums = [3,5,15,7,5];
let n, i=0;
// n이 먼저 할당 받은 후 표현식 전체가 그 값으로 평가되므로 숫자로 비교할 수 있다.
while ((n = nums[i]) < 10 && i++ < nums.length) {
    console.log(`Number less than 10: ${n}`);
    //15는 조건을 충족하지 못하므로 이때 loop를 빠져나옴
}
console.log(`Number greater than 10 found: ${n}.`); //15
console.log(`${nums.length - i - 1} numbers remain.`);

// Number less than 10: 3
// Number less than 10: 5
// Number greater than 10 found: 15.
// 2 numbers remain.

// 해체 할당 (destructuring assignment)
const obj = { bb : 2, cc : 3, dd : 4};

const {aa, bb, cc} = obj;
console.log(`aa=? ${aa}\nbb=? ${bb}\ncc=? ${cc}`);
//dd는 ReferenceError;
// aa=? undefined
// bb=? 2
// cc=? 3

// 할당만 할 수 있지만 그럴 경우에는 괄호 필수
// Error !!  {aa,bb,cc} = obj;
// 동작 !! ({aa,bb,cc} = obj);

// 배열 해체 할당
const arr = [1,2,3];
let [xx,yy] = arr;
console.log(`xx=? ${xx}\nyy=? ${yy}`); 
// xx=? 1
// yy=? 2
// zz // ReferenceError;

// 확장 연산자를 사용하면 남은 요소를 버리지 않고 새로운 배열에 할당할 수 있다. (반드시 맨 마지막에!!)
const arr2 = [1,2,3,4,5];
let [oo, pp,qq, ...rest] = arr2;
console.log(`oo=?${oo}  pp=?${pp}   qq=?${qq}`) 
//oo=?1  pp=?2   qq=?3 
console.log(rest) //[ 4, 5 ]

let nn = 5, mm = 10;
[nn, mm] = [mm,nn];
console.log(nn) //10
console.log(mm) //5

