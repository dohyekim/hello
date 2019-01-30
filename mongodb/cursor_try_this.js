var cur = db.Artist.find()
var i = 0; 
while(cur.hasNext()) {
    i++;
    var s = cur.next()
    if (i % 5 == 0){
    s.likecnt= 100;
    db.Artist.save(s)
    }    




// for each가 더 쉽다.
var i = 0;
cur.forEach(s => {
    i++
    if (i %  5 ==0){
        s.likecnt = 20;
        db.Artist.save(s)
    }
})

db.Artist.find({likecnt:20}, {name:1, likecnt:1, _id:0})