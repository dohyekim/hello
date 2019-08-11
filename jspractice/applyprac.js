const bruce = { name : 'Bruce' };
const moon = { name : 'Byul'};

// greet()은 어떤 객체에도 연결되지 않았지만 this를 사용합니다.
function greet() {
	console.log(`Hello, I'm ${this.name}!`)
	return `Hello, I'm ${this.name}!`
}

greet(); //Hello, I'm undefined!
// call은 this를 특정 값으로 지정할 수 있습니다.
greet.call(bruce); //Hello, I'm Bruce!

greet.call(moon); //Hello, I'm Byul!


// 함수 호출시 call을 사용하고 this로 사용할 객체를 넘기면 해당 함수가 주어진 객체의 메서드인 것처럼 사용할 수 있습니다.
// call의 첫 번째 매개변수는 this로 사용할 값이고, 매개변수가 더 있으면 그 매개변수는 호출하는 함수로 전달됩니다.

function update(birthYear, occupation) {
	this.birthYear = birthYear;
	this.occupation = occupation;
	console.log(`${this.name}은 ${this.birthYear}년에 태어났고 ${this.occupation}입니다.`)
}

update.call(bruce, 1949, 'singer'); //bruce = {name:'Bruce', birthYear:1949, occupation:'singer'}
update.call(moon, 1992, 'performer');

// call은 매개변수를 직접 받지만, apply는 매개변수를 배열로 받습니다.
update.apply(bruce, [1955, 'actor']);
update.apply(moon, [1992, 'singer']);


//# 3
const arr = [2,3,-5,6,16];
const maxarr = Math.max(arr)
const minarr = Math.min(arr)

console.log(`max >> ${maxarr}, min >> ${minarr}`) //max >> NaN, min >> NaN

// Math.min과 Math.max는 매개변수를 받아 그중 최솟값과 최댓값을 반환합니다. 이때 apply를 사용하면 기존 배열을 이들 함수에 바로 넘길 수 있습니다.
const appmin = Math.min.apply(null, arr);
const appmax = Math.max.apply(null, arr);


console.log(`max >> ${appmin}, min >> ${appmax}`) //max >> -5, min >> 16


//#4 확산연산자
const newBruce = [1940, 'martial artist'];
update.call(bruce, ...newBruce) //Bruce은 1940에 태어났고 martial artist입니다.


// #5 update 메소드는 this값이 중요하기 때문에 call을 사용해줘야 하지만 
// min/max함수는 this값이 상관없기 때문에 바로 확산 연산자를 사용할 수 있습니다.
const a = Math.min(...arr);
const b = Math.max(...arr); 
console.log(`max >> ${a}, min >> ${b}`); //max >> -5, min >> 16


// bind는 함수의 this값을 영구히 바꿉니다. 

const updateBruce = update.bind(bruce); // this는 이제 영원히 bruce가 됨.

updateBruce(1904, "actor"); //Bruce은 1904에 태어났고 actor입니다.
updateBruce.call(moon, 1970, 'king'); //Bruce은 1970에 태어났고 king입니다. 

// 즉, bind를 사용한 함수는 call/apply 혹은 다른 bind와 함께 사용할 수 없다.
console.log(moon); //{ name: 'Byul', birthYear: 1992, occupation: 'singer' } moon은 변하지 않았습니다,.

const updateBruce1949 = update.bind(bruce, 1949);
updateBruce1949("singer, songwriter"); //Bruce은 1949에 태어났고 singer, songwriter입니다.
const updateByul1992 = update.bind(moon, 1992, 'rapper');
updateByul1992(); //Byul은 1992년에 태어났고 rapper입니다.




















