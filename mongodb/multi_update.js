// Singer collection의 likecnt=1인 문서 전체를 likecnt++ 하시오.

db.Artist.find({liekcnt:1})

// singer0, singer1
db.Artist.update( {likecnt:1}, 
                  {$inc: {likecnt:1}},false, true)