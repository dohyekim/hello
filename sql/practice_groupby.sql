-- 1) 과목별 담당 교수명
select prof.name, sub.name
from Subject sub inner join Prof prof on sub.prof = prof.id; 
-- * Main이 되는 table이 왼쪽에 가는 게 좋음

-- 2) 과목별 학생수

-- 3) 역사 과목의 학생 목록

-- 3) 역사 과목의 학생 목록 (테이블 두 개가 한 번, 나머지 하나까지 두 번 조인 됨. 여러 개의 join)

-- 4) 국어 과목을 듣는 서울 거주 학생 목록

-- 5) 역사 과목을 수강중인 지역별 학생수

-- 6) 과목별 수강중인 지역별 학생수

-- 7) 서울에 거주하는 과목별 남녀 학생수 ( group by 에서 sub.id와 stu.gender로 했기 때문에 select할 때도 sub.name보다는 sub.id를 해주는 게 좋다)
-- clustered index인(disk에 쓰인 물리적인 index인) 동시에 (primary key)니까 unique하기까지 함 -> 컴퓨터 입장에서 group/ordering할 때 이미 순서대로 정렬된(sorted) 거(즉 index)에서 뚝 잘라오면 엄청 편하니까
-- 반드시 clustered일 필요는 없음. index면 OK( 다만 clustered index가 갑일 뿐..)
-- 실제로 다른 db에서는 sub.name이 안 됨 --> 이름을 보고 싶다면 group함수를 쓰자 (min(sub.name) or max(sub.name)
-- group by sub.name이 아닌 sub.id인 이유는 group by나 order by는 index를 타는 게 좋기 때문이다. gender는 index가 없으니까 앞에 나온 애라도 index 쥐어주면 좋다.
select min(sub.name) subject_name, 
				 (case stu.gender
				  when 1 then '남자'
						 else '여자' end) as 'gender', count(*) as 'num of students'
from Enroll en inner join Student stu on en.student = stu.id
			   inner join Subject sub on en.subject = sub.id
where stu.address = '서울'
group by sub.id, stu.gender
order by subject_name asc, stu.gender desc;
-- 여기도 order by sub.name asc하지 말고 min/max함수를 건 걸 쓰자.
-- 7) 7번 답에 대한 case 연습

select sub.name, (case when stu.gender = 1 then '남자'
					   when stu.gender = 0 then '여자' end) as '성별', count(*) as '학생수'
from Enroll en inner join Student stu on en.student = stu.id
			   inner join Subject sub on en.subject = sub.id
group by sub.id, stu.gender
order by sub.name asc, stu.gender desc;

-- 8) show index from
show index from Student;
show index from Subject;
show index from Enroll;

-- 9) insert ignore into (primary key를 중복시키기)  --> ctrl shift enter 헀을 때 에러가 나도 무시, Try~except랑 비슷
insert into Test(id, name) values (2, '김이수');
insert into Test(id, name) values(3, '김박수');
insert ignore into Test(id, name) values (22, '김한수');
-- > primary key가 중복되면 아무것도 하지 말아주세요.
replace into Test(id, name) values (23, '김별수');
insert into Test(id, name) values (31, '김굴수');
replace into Test(id, name) values (23, '김팔수');
select * from Test;