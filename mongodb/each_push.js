

// singer4의 albums에 100 ~ 110 까지 $each를 사용하여 push하시오.
db.Artist.findOne({name:"singer4"})
var a = db.Artist;
for (let i = 100; i < 111; i++){
a.update({name:"singer4"}, 
            {
                $addToSet : {albums: {$each: [i]}}
            })
            
}

// 다른 방법
var a = db.Artist;
var arr = []
for (let i = 100; i < 110; i++){
                                arr.push(i)
}
a.update({name:"singer5"},
{
    $addToSet : {albums: {$each: arr}}
})

db.Artist.findOne({name:"singer5"})

// db.Artist.update({name:"singer4"},
//                     {$unset : {scores:1}})

                              




