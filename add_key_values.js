// singer1의 문서에 아래 노래(hitsongs) 2곡을 추가하시오.


db.Artist.update( {name:"singer1"},
                    {
                        $set: {hitsongs: [
                                        {title:"24/7", albumId:1},
                                        {title:"222", albumId:2}
                                        ]
                    }})
                    
                    
db.Artist.findOne({name:"singer1"})