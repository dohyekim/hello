let currentTempC=22.5;
let targetTempC; //undefined
let tempC, room1 = "conference_room_a", room2 = "conference_room_b"; 
// undefined, conference_room_a, conference_room_b

const ROOM_TEMP_C = 21.5, MAX_TEMP_C = 30;
// 상수 이름에는 보통 대문자와 밑줄만 사용


let room3 = "lobby";
let currentRoom = room3;
console.log(`room3 >>>>>>>>> ${room3}`) //lobby
// console.log(`${currentRoom} = ${conference_room_a}`) 
//ReferenceError: conference_room_a is not defined

//immutability

let str = "hello"; // str을 "hello"로 초기화
str = "world"; // 다시 새로운 불변값 "world"를 할당받음

//backtick
console.log(`New in ES6: \` strings.`) //New in ES6: ` strings.

let interpolation = '문자열 채우기'
console.log(`New in ES6: ${interpolation}`) //New in ES6: 문자열 채우기

//여러줄 문자열
const multiline = "line1\
line2"
console.log(multiline) //line1line2

const multiline2 = "line1\nline2"
console.log(multiline2) 
//line1
// line2


const multiline3 = `line1
line2`;
console.log(multiline3) 
// line1
// line2

const multiline4 = `line1
	line2
		line3`
console.log(multiline4) 

// line1
// 	line2
// 		line3
         


//Symbol

const RED = Symbol("The color of a sunset!")
console.log("RED>>>", RED, "type??????", typeof(RED)); 
//RED>>> Symbol(The color of a sunset!) type?????? symbol

const ORANGE = Symbol("The color of a sunset!")


console.log(RED === ORANGE) //false, symbol은 유일!

//객체

const obj = {};
console.log("type>>>", typeof(obj)); // type>>> object

obj.color = 'Yellow';
console.log(obj["color"]) //Yellow
console.log(obj.color) //Yellow
console.log(obj['food']); //undefined
console.log(obj.food); //undefined

obj["not an identifier"] = 3;
console.log(obj["not an identifier"]) //3


const SIZE = Symbol()
obj.SIZE = 8;
console.log(obj.SIZE) //8

console.log(obj)
//{ color: 'Yellow', 'not an identifier': 3, SIZE: 8 }

obj.color = 'Blue'
console.log(obj)
//{ color: 'Blue', 'not an identifier': 3, SIZE: 8 }

const sam1 = {
	name : 'Sam',
	age : 4
};

const sam2 = { name : 'Sam', age : 4};

const sam3 = {
	name: 'Sam',
	classification: {
		kingdom : 'Anamalia',
		phylum : 'Chordata',
		class : 'Mamalia',
		order : 'Carnivoria',
		family : 'Felidae',
		subfamily : 'Felinae',
		genus : 'Felis',
		species : 'catus',
	}
};

console.log(sam1 === sam2) //false 프로퍼티는 똑같지만 다른 객체
// 원시값: 값이 숫자 3인 두 변수는 같은 원시 값을 가리킴
console.log(sam3.classification.class) //Mamalia

//객체에 함수 추가
sam3.speak = function() {
	console.log("Meow!")
	return "Meow!"
}


sam3.speak() //Meow

console.log(sam3)
// { name: 'Sam',
//   classification:
//    { kingdom: 'Anamalia',
//      phylum: 'Chordata',
//      class: 'Mamalia',
//      order: 'Carnivoria',
//      family: 'Felidae',
//      subfamily: 'Felinae',
//      genus: 'Felis',
//      species: 'catus' },
//   speak: [Function] }
delete sam3.speak;

console.log(sam3)
// { name: 'Sam',
//   classification:
//    { kingdom: 'Anamalia',
//      phylum: 'Chordata',
//      class: 'Mamalia',
//      order: 'Carnivoria',
//      family: 'Felidae',
//      subfamily: 'Felinae',
//      genus: 'Felis',
//      species: 'catus' } }

const s = "hello";
console.log(s.toUpperCase()) //HELLO, p.95 참고

const d = "hello";
d.rating = 3
console.log(d.rating) //undefined, 왜냐하면 임시 객체는 즉시 파괴


//Array

//값 덮어쓰기!

const arr = ['a','b','c'];
arr[2]='z'
console.log(arr) //[ 'a', 'b', 'z' ]

arr[10] = 'c'
console.log(arr) //[ 'a', 'b', 'z', <7 empty items>, 'c' ]

arr[5] = 'v'
console.log(arr) //[ 'a', 'b', 'z', <2 empty items>, 'v', <4 empty items>, 'c' ]


// Date

const now = new Date();
console.log(now); //2019-08-11T07:41:50.257Z

const newYearsDay = new Date(2019,0,1);
// 월은 0부터 시작!
console.log(newYearsDay); //2018-12-31T15:00:00.000Z

const yourBirthday = new Date(1990,1,20,14,20); //1990-02-20T05:20:00.000Z
console.log(yourBirthday);

console.log(yourBirthday.getFullYear()); // 1990
console.log(yourBirthday.getMonth()); //1
console.log(yourBirthday.getDate()); //20
console.log(yourBirthday.getDay()); //2( 0: 일요일) 화요일
console.log(yourBirthday.getHours()); //14
console.log(yourBirthday.getMinutes()); //20
console.log(yourBirthday.getSeconds()); //0
console.log(yourBirthday.getMilliseconds()); //0



//str to number

const numStr = '33.3';
const num = Number(numStr);
console.log("num>>>>>>>", num, "type??????", typeof(num)); 
//num>>>>>>> 33.3 type?????? number
// Number 객체의 인스턴스가 아니다

const numStr2 = 'aaa';
const num2 = Number(numStr2);
console.log("num>>>>>>>", num2, "type??????", typeof(num2)); 
//num>>>>>>> NaN type?????? number

const aaa = parseInt("17 volts", 10); //17
console.log(aaa)

const bbb = parseInt("3a", 16); //58
console.log(bbb)

const ccc = parseFloat("15.5kph"); //15.5
console.log(ccc)


// date to number

const ddd = new Date();
const ts = ddd.valueOf(); //UTC 1970.1.1 자정으로부터 몇 밀리초가 지났는지 나타내는 숫자
console.log(ts, typeof(ts)) //1565510145703 'number'

//boolean to number
const eee = true;
const n = eee ? 1 : 0;
console.log(`value n >> ${n}, type of n >>>, ${typeof(n)}, type of eee>>>>, ${typeof(eee)}`)
//value n >> 1, type of n >>>, number, type of eee>>>>, boolean


// date to string
console.log(toString(yourBirthday)); //[object Undefined]

const arr2 = [1,true,'hello'];
console.log(arr2.toString()); //"1,true,hello"

//to boolean
const fff = 0;
const f1 = !fff;
const f2 = !!fff;
const f3 = Boolean(fff);

console.log(`f1>> ${f1}, f2>> ${f2}, f3>> ${f3}`)
//f1>> true, f2>> false, f3>> false

// call by reference / call by value
let v1 = 1; // 원본
let v2 = v1; //v2 는 1일 뿐 v1이 아니다.
v1 = 2; // 원본 값을 바꿈
console.log(v2) //1, v2의 값은 그대로

v1 === 2
console.log(`v1>>> ${v1}`, v1 === 2) //v1>>> 2 true

function change(a) {
	a = 5;
}

v1 = 3;
change(v1);
console.log(v1); //3

// call by reference ( 원본이 바뀌면 사본도 바뀜, 왜냐하면 객체를 복사/전달할 때 객체를 가리키고 있다는 사실을 복사/전달하기 때문)
let ro = { a : 1 };
let rp = ro; // rp와 ro는 같은 주소값!!
ro.a = 2;
console.log(rp) //{ a: 2 }


let ro2 = { a : 1 };
let rp2 = ro2;
console.log(rp2 === ro2) //true
ro2.a = 100000000000; // 얘는 값을 수정한 것
console.log(rp2); //{ a: 100000000000 }

ro2 = { a : 2 }; // 얘는 수정이 아닌 다른 것을 참조하는 
console.log(rp2 === ro2) //false
console.log(rp2); //{ a: 1 }

let rq = { a : 1 };
console.log(rq === { a:1 }) //false, 변수와 객체는 일치하지 않는다. 변수가 그 객체 자체가 되는 것이 아니고
// 그 객체의 주소값을 참조하고있을 뿐 ( 객체를 가리키고 있을 뿐 )이므로
