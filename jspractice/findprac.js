const arr = [{"id":5, "name":"Judith"}, {"id":7, "name":"Francis"}];
const f = arr.find( o => o.id ===5); //매개변수가 하나인 경우 (o)에서 () 생략 가능
const uf = arr.find( o => o.id === 2);

console.log(f, uf) //{ id: 5, name: 'Judith' } undefined

const arr2 = [1,17,16,5,4,16,10,3,49];
const f2 = arr2.find((x, i) => i > 2 && Number.isInteger(Math.sqrt(x)));
console.log(f2) //4