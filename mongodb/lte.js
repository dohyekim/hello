 db.Artist.update({name:"singer4"}, {
         $pull: {albums: {$lte:103}} 
 })

db.Artist.findOne({name:"singer4"})