//1번 
db.createCollection("Artist")
for (let i = 0; i < 100; i++){
    db.Artist.insert({name:'singer'+i, company: 'company'+i, likecnt: i+1 })
}



