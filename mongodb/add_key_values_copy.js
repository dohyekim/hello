// singer1의 문서에 아래 노래(hitsongs) 2곡을 추가하시오.


db.Artist.update( {name:"singer1"},
                    {
                        $set: {hitsongs: [
                                        {title:"24/7", albumId:1},
                                        {title:"222", albumId:2}
                                        ]
                    }})
                    
                    
var a = db.Artist.findOne({name:"singer2"})                    

a.hitsongs = [
    {title:"11/11", albumId:3},
    {title:"22/22", albumId:4}
    ] 
db.Artist.save(a)

db.Artist.findOne({name:"singer2"})
