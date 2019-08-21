// 생활 코딩 참고했다.

function outer() {
    function inner() {
        let title = "coding everybody!";
        console.log(title)
    };
    inner();
}

outer(); //coding everybody!

function outer2() {
    let title = "coding everybody!";
    return function() {
        console.log(title);
    }
}
let inner = outer2(); //이때 inner변수에는 function() {console.log(title)}가 담긴다!
inner(); //coding everybody! //title은 외부함수(outer2)의 지역변수에 접근 가능


function factory_movie(title) {
    return {
        get_title : function() {
            return title;
        },
        set_title : function(_title) {
            title = _title;
        },
    }
}

ghost = factory_movie('Ghost in the Shell');
matrix = factory_movie('Matrix');
console.log(ghost.get_title()); //Ghost in the Shell
console.log(matrix.get_title()); //Matrix

matrix.set_title('매트릭스');
console.log(matrix.get_title()); //매트릭스

//이제 밖에서 title이라는 변수를 써도 factor_movie 안의 logic에는 영향을 미치지 않는다.

let title = "엑시트";
console.log("title >>", title); //title >> 엑시트
console.log(ghost.get_title()); //Ghost in the Shell


