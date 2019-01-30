db.Artist.find().skip(3)
db.Artist.find().sort({likecnt: 1, name: -1})
db.Artist.find().limit(5)
db.Singer.find({}, {_id:0}).sort({name: -1}).limit(5)
