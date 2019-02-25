from collections import namedtuple

Song = namedtuple('Song', 'songno title likecnt')
print("\nSong\n---> ",Song) # <class '__main__.Song'> 하지만 class랑은 다름 왜냐하면 상속이나 모듈화가 안 되기 때문에.


s1 = Song(123, '만남', 100)
s2 = Song(songno=222, title='강남스타일', likecnt=200)
s3 = Song._make([333, 'radio ga ga', 201])
s2 = s2._replace(likecnt=190)

d1 = s3._asdict()

print("\ns\n---> ")
for s in [s1, s2, s3]:
    print(s)

print("\nd1\n--->", d1)
