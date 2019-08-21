var arr = [];
for (var i = 0; i < 5; i++) {
    arr[i] = function() {
        return i;
    }
}

for (var index in arr) {
    console.log(arr[index]());
}

// 5 5 5 5 5

let arr = [];
for (let i = 0; i < 5; i++) {
    arr[i] = function() {
        return i;
    }
}

for (let index in arr) {
    console.log(arr[index]());
}

// 0 1 2 3 4 