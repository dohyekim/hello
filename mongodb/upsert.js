db.Artist.find()


for (let i = 1; i <= 10; i++){
                                db.Artist.update( {name:"singer" + i},
                                                    {$inc: {likecnt : 1}},
                                                    false, true
                                    )
}
    
    
//     //1번 
// db.createCollection("Artist")
// for (let i = 0; i < 100; i++){
//     db.Artist.insert({name:'singer'+i, company: 'company'+i, likecnt: i+1 })
// }



