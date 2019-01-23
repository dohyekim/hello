김도혜(Dohye Kim) [10:06 AM]
column 명ㅇ이 key가 되고 값이 value가 되는 json이 row에 들어감 (  row = document = objects )

table = collection (schema가 없음. 즉 column이나 type 등이 없는 table임) 왜냐하면 어차피 json이니까

김도혜(Dohye Kim) [10:59 AM]
replicate : 여기서는 분산이라는 뜻(sharding)

김도혜(Dohye Kim) [11:04 AM]
db.collection.update({key: value}, jsonData}

{key:value}가 where인 셈, key:value인 곳을 jsonData하게 바꾼다
32bit number : 4byte number ==> 작은 소수점, int

(보통 소수점은 8byte이지만 작은 float은 32에 넣어준다는 뜻)

김도혜(Dohye Kim) [11:11 AM]
_id: 내가 주는 거 아님. nonggo db가 주는 거

김도혜(Dohye Kim) [11:43 AM]
s = "12345"
stack 영역 : 가까운 공간, s, &12 (거실에 밭 둘 순 없음)
heap 영역 : 먼 공간, "12345" 가변하기 쉬운 곳 (운동장ㅇ에 밭 만들기)

capped: true,    # fixed size --> heap에 두지 않고 한 데 묶어두겠다 (heap은 따로 떨어져있음)
max: 100000 --> 10만개까지 만들겠다

{"name" : "aa"}

autoIndex: true --> 이 테이블을 자주 읽을텐데 id로 찾기는 너무 어려우니까 name이라는 key로 찾아볼테니 index로 해줘
mysql의 blob: binary type 이지만 이미지를 박지는 않는다 너무 크니까)
BSON 이미지의 주소를 넣는다! 이미지 그대로 박으면 너무 큼. row의 max는 4MB
bulk insert --> mysql의 executemany
지금 bson의 사이즈가 얼만큼 있는지 알고 싶다면 -->Object.bsonsize("title: '', singer:'') ==> 하면 byte단위로 나옴. 45로 나오는데 그 이유는 id 등도 있기 때문, {}는 byte 수를 알기 쉽지 않다. 키 value 쌍이기 때문에

김도혜(Dohye Kim) [11:56 AM]
db.Song.drop() : 완전히 지우고 싶을 때
db.Song.remove({}) : 지워도 색인은 남음
