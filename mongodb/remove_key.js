// 4번 singer1의 likecnt를 제거하시오. ($unset 사용)

db.Artist.update({name:"singer1"},
{$unset: {likecnt:1}
}    
)

db.Artist.findOne({name:"singer1"})