// singer4의 albums에 [107, 109]를 제거하시오.
db.Singer.update({name: 'singer3'}, {$pull: {albums: { $in: [107,109] }  }})