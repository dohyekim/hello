db.food.find({})
   .projection({})
   .sort({_id:-1})
   .limit(100)
   

var cur = db.Artist.find()

var i = 0;

while (cur.hasNext()) {
    i++;
    var aaa = cur.next();
    print(aaa.name);
    if (i >20) 
        break;
}

cur.forEach ( function() {
    print(cur.next)
})