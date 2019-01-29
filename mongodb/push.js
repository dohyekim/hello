// Singer collection의 singer3에 albums에 10을 push 하시오.
db.Artist.findOne({name:"singer3"})
db.Artist.update({name:"singer3"},
                {
                    $push: {albums:10}
                }
)

