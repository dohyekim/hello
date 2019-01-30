// Singer collection의 singer1 ~ singer10 가수에 대해 likecnt가 존재하면 1증가 하고, 없으면 1로 초기화 하시오.

db.Artist.find()


for (let i = 1; i <= 10; i++){
                                db.Artist.update( {name:"singer" + i},
                                                    {$inc: {likecnt : 1}},
                                                    true
                                    )
}
    
    
//     //1번 
// db.createCollection("Artist")
// for (let i = 0; i < 100; i++){
//     db.Artist.insert({name:'singer'+i, company: 'company'+i, likecnt: i+1 })
// }



