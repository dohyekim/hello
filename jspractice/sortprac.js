const arr = [{"name":"Suzanne"}, {"name":"Jim"}, {"name":"Trevor"}, {"name":"Amanda"}];

arr.sort(); //arr은 바뀌지 않습니다.
arr.sort( (a,b) => a.name > b.name);
console.log(arr)
// [ { name: 'Amanda' },
//   { name: 'Jim' },
//   { name: 'Suzanne' },
//   { name: 'Trevor' } ]

arr.sort( (a,b) => a.name < b.name);
console.log(arr)
// [ { name: 'Trevor' },
//   { name: 'Suzanne' },
//   { name: 'Jim' },
//   { name: 'Amanda' } ]