
// singer4의 albums에 105번을 제거하시오.

var a = db.Artist

a.update({name:"singer4"},
            {
                $pull:{albums:105}
            })
            
a.findOne({name:"singer4"})
