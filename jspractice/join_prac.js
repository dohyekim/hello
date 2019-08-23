const arr = [1, null, "hello", "world", true, undefined];
delete arr[3];
arr.join();
console.log(arr) //[ 1, null, 'hello', <1 empty item>, true, undefined ]
console.log(arr.join()) //1,,hello,,true,

const attrs = ["Nimble", "Perceptive", "Generous"];
const html = '<ul><li>' + attrs.join("</li><li>") + "</li><ul>";
console.log(html) //<ul><li>Nimble</li><li>Perceptive</li><li>Generous</li><ul>

 
 
