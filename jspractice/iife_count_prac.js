const f = (function() {
    let count=0;
    return function() {
        console.log("now count>>>", count)

        return `I have been called ${++count} time(s).`;
    }
})();

// console.log(f) //[Function]
console.log(f()); //I have been called 1 time(s).
console.log(f());


const g = function() {
    let count=0;
    return function() {
        return `I have been called ${++count} time(s).`;
    }
};
console.log(g) // [Function:g]
console.log(g()); //[Function]
console.log(g()()); //I have been called 1 time(s).
console.log(g()()); //I have been called 1 time(s).
console.log(g()()); //I have been called 1 time(s).

(function() {
    console.log("Hello")
})();

(function(name) {
    console.log(`My name is ${name}`)
})('Beatrice');