const arr = ["b","c","d"];
arr.push("e")
console.log(arr); //[ 'b', 'c', 'd', 'e' ]


arr.pop();
console.log(arr); //[ 'b', 'c', 'd' ]
arr.pop(1);
console.log(arr); //[ 'b', 'c' ]

arr.unshift("a");
console.log(arr); //[ 'a', 'b', 'c' ]

arr.shift();
console.log(arr); //[ 'b', 'c' ]

const arr2 = [1,2,3];
console.log(arr2.concat(4,5,6)); //[ 1, 2, 3, 4, 5, 6 ]
console.log(arr2); //[ 1, 2, 3 ]


console.log(arr2.concat([4,5,6])); //[ 1, 2, 3, 4, 5, 6 ]
console.log(arr2); //[ 1, 2, 3 ]

console.log(arr2.concat([4,5],6)); //[ 1, 2, 3, 4, 5, 6 ]
console.log(arr2); //[ 1, 2, 3 ]

console.log(arr2.concat([4,[5,6]])); //[ 1, 2, 3, 4, [ 5, 6 ] ]
console.log(arr2); //[ 1, 2, 3 ]

// slice

const arr3 = [1,2,3,4,5];
console.log(arr3.slice(3)); //[ 4, 5 ]
console.log(arr3.slice(2,4)); //[ 3, 4 ]
console.log(arr3.slice(-2)); //[ 4, 5 ]
console.log(arr3.slice(1,-2)); //[ 2, 3 ]
console.log(arr3.slice(-2,-1)); //[ 4 ]

console.log(arr3) //[ 1, 2, 3, 4, 5 ]

//splice : 제거된 요소를 return한다!
const arr4 = [1,5,7];
console.log(arr4);  //[ 1, 5, 7 ]
console.log(arr4.splice(1,0,2,3,4)); //[]
console.log(arr4); //[ 1, 2, 3, 4, 5, 7 ]
console.log(arr4.splice(5,0,6)); //[]
console.log(arr4); //[ 1, 2, 3, 4, 5, 6, 7 ]
console.log(arr4.splice(1,2)); //[ 2, 3 ]
console.log(arr4); //[ 1, 4, 5, 6, 7 ]
console.log(arr4.splice(2,1,'a','b')); //[ 5 ]
console.log(arr4); //[ 1, 4, 'a', 'b', 6, 7 ]

// copyWithin
const arr5 = [1,2,3,4];
console.log(arr5.copyWithin(1,2)); //[ 1, 3, 4, 4 ]
console.log(arr5); //[ 1, 3, 4, 4 ]
console.log(arr5.copyWithin(2,0,2)); //[ 1, 3, 1, 3 ]
console.log(arr5); //[ 1, 3, 1, 3 ]
console.log(arr5.copyWithin(0,-3,-1)); //[ 3, 1, 1, 3 ]
console.log(arr5); //[ 3, 1, 1, 3 ]

//fill

const arr6 = new Array(5).fill(1);
console.log(arr6); //[ 1, 1, 1, 1, 1 ]
console.log(arr6.fill("a")); //[ 'a', 'a', 'a', 'a', 'a' ]
console.log(arr6); //[ 'a', 'a', 'a', 'a', 'a' ]
console.log(arr6.fill("b",1)); //[ 'a', 'b', 'b', 'b', 'b' ]
console.log(arr6); //[ 'a', 'b', 'b', 'b', 'b' ]
console.log(arr6.fill("c",2,4)); //[ 'a', 'b', 'c', 'c', 'b' ]
console.log(arr6); //[ 'a', 'b', 'c', 'c', 'b' ]
console.log(arr6.fill(5.5,-4)); //[ 'a', 5.5, 5.5, 5.5, 5.5 ]
console.log(arr6); //[ 'a', 5.5, 5.5, 5.5, 5.5 ]
console.log(arr6.fill(0,-3,-1)); //[ 'a', 5.5, 0, 0, 5.5 ]
console.log(arr6); //[ 'a', 5.5, 0, 0, 5.5 ]

//reverse
const arr7 = [1,2,3,4,5];
arr7.reverse()
console.log(arr7) //[ 5, 4, 3, 2, 1 ]

arr7.sort();
console.log(arr7); //[ 1, 2, 3, 4, 5 ]

const arr8 = [
    {name: "Suzanne"},
    {name: "Jim"},
    {name: "Trevor"},
    {name: "Amanda"},
]
arr8.sort();
console.log(arr8);
// [ { name: 'Suzanne' },
//   { name: 'Jim' },
//   { name: 'Trevor' },
//   { name: 'Amanda' } ]

arr8.sort((a,b) => a.name > b.name);
console.log(arr8);
// [ { name: 'Amanda' },
//   { name: 'Jim' },
//   { name: 'Suzanne' },
//   { name: 'Trevor' } ]

arr8.sort((a,b) => a.name[1] > b.name[1]);
console.log(arr8);
// [ { name: 'Jim' },
//   { name: 'Amanda' },
//   { name: 'Trevor' },
//   { name: 'Suzanne' } ]

const o = {name:1}
const p = {name:1}
console.log(o===p) //false

const a1 = [1,2]
const a2 = [1,2]
console.log(a1===a2) //false

const t = true
const t1 = true
console.log(t === t1) //true

const arr9 = [1,5,"a",o,true,6,[1,2],9];
console.log(arr9.indexOf({name:1})); //-1
console.log(arr9.indexOf(o)); //3
console.log(arr9.indexOf([1,2])); //-1
console.log(arr9.lastIndexOf(true,3)); //-1
console.log("!!!!!!!!!!!",arr9.lastIndexOf(true,4)); //4
console.log(arr9.lastIndexOf(5,4)); //1
console.log(arr9.indexOf(true,3)); //4
