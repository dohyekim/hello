// 2번 singer1의 문서에 albums 키를 추가하시오.(변수 사용 - save()) albums = [1, 2, 3]

var art = db.Artist.findOne({name:"singer1"})
art.albums = [1,2,3]
db.Artist.save(art)
db.Artist.find()