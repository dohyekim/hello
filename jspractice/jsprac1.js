
//#1
const act = (name="hong", age="22") => {
	console.log(`${name}은 ${age}살입니다.`)
}

act();


//#2
const af = ii => ii  * ii;
console.log("af=", af(3));


//#3
let jdata = {
	id: 123,
	age: 45,
	name: `aaa`
};

let {id, age} = jdata;
console.log(`QQQ>> id=${id}, age=${age}`);

//#4
let [a,c] = [123, 456, 777];
console.log(`QQQ>> a=${a}, c=${c}`) //QQQ>> a=123, c=456

//#5
let i1 = 123,
		i2 = 456;
let iii = {i2, i1};
console.log(typeof(iii)) // object
let jstr = JSON.stringify(iii); // object > string
console.log(typeof(jstr)) // string
console.log(`QQQ>>> iii=${jstr}`) //QQQ>>> iii={"i2":456,"i1":123}
console.log(`${iii}[i1]`) //[object Object][i1]
console.log(iii[i1]) //undefined
console.log(iii) //{ i2: 456, i1: 123 }
console.log(`${jstr}[i1]`) //{"i2":456,"i1":123}[i1]

//#6
const score = {
	i2,
	i1,
	sum() {
		console.log(`sum is ${i2 + i1}`); 
	}
};

console.log("s3>",score.sum()); // sum is 579
																//s3> undefined

//#7
let nums1 = [1,2,3],
		nums2 = [4,5,6],
		arrnum = [...nums1, ...nums2],
		ntharr = [nums1, nums2],

		[first, ...rest] = arrnum,
		[last] = nums2.reverse();

console.log(arrnum) //[ 1, 2, 3, 4, 5, 6 ]
console.log(ntharr) //[ [ 1, 2, 3 ], [ 6, 5, 4 ] ]
console.log(first) //1
console.log(last)  //6
console.log(...rest) //2 3 4 5 6

console.log(rest.join(`, `)); //2, 3, 4, 5, 6


//#8
const nnum = (...args) => {
	let [start, ...remains] = args;
	console.log("start>>", start, "," ,remains.reverse());
} 

nnum(1,2,3,4,5);
// start>> 1 , [ 5, 4, 3, 2 ]

let jtt = {
	...jdata,
	i1
};

console.log(JSON.stringify(jtt)) // {"id":123,"age":45,"name":"aaa","i1":123}
console.log(jtt) // { id: 123, age: 45, name: 'aaa', i1: 123 }

//#9 class

class Product {
	constructor(id, name) { // 생성자 함수 
		this.id = id;
		this.name = name;
	}

	print () {
		console.log(`${this.id}:${this.name}`);
	}
}


const prod1 = new Product(1, `p1`) 
console.log(prod1.print()); // 1:p1 undefined
prod1.print(); //1:p1


class Ball extends Product { // Ball이 Product 상속
	constructor(id, name) {
		super(id, name || `ball`) // name이 없으면 ball
	}
	print () {
		super.print();
	}
}

const prod2 = new Ball(2);
console.log("prod2>>", prod2.print()); //2:ball prod2>> undefined
prod2.print() //2:ball


//#10

export const print = (msg) => log(msg); // 선택해서 가져올 때

export const log = (s) => console.log(s);

export default Product; // export default: 통째로 다 가져올 때

import { print, log } from './out.js';
import { print, log } from './out';
import P from 'product';
import P from 'product.js';

let p = new P(123); // Product(123)






















































































