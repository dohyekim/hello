const message = function() {
    const secret = "I'm a secret!";
    return `The secret is ${secret.length} characters long.`;
}

secret = "Hello"
let a = message();
console.log(a) //The secret is 13 characters long.

// const message = (function() {
//     const secret = "I'm a secret!";
//     return `The secret is ${secret.length} characters long.`;
// })();
// // let a = message(); //TypeError: message is not a function
// console.log(message) //The secret is 13 characters long.

// //message에 담긴 건 이제 함수가 아님.


let f;
{
    let o = {note:'Safe'};
    f = function() {
        return o;
    }
}
let oRef = f();
console.log(oRef) //{ note: 'Safe' }
oRef.note = "Not So Safe After All" 
console.log(oRef) //{ note: 'Not So Safe After All' }

