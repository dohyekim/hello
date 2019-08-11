const arr = [5,7,12,21,5];
const a = arr.some( x => x%2 === 0); //true
const b = arr.some( x => Number.isInteger(Math.sqrt(x))); //false

const arr2 = [3,9,17,1,13]; 
const c = arr2.some( x => x%2 === 0); //false
const d = arr2.some( x => Number.isInteger(Math.sqrt(x))); //true

console.log(a,b,c,d)
