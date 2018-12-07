



select * from Subject;
-- 1) 과목별 담당 교수명

select s.*, p.name as 'Prof name' from Subject s inner join Prof p on s.prof = p.id;

-- 2) 과목별 학생수
select e.subject, max(s.name), count(*) as '학생수'
	from Enroll e inner join Subject s on e.subject=s.id
	group by subject;
    
-- 3) 역사 과목의 학생 목록
select s.name
	from Enroll e inner join Student s on e.student = s.id
    where e.subject = 1;
    
-- 3) 역사 과목의 학생 목록 (테이블 두 개가 한 번, 나머지 하나까지 두 번 조인 됨. 여러 개의 join)
select sub.name, s.name
	from Enroll e inner join Student s on e.student = s.id
				  inner join Subject sub on e.subject = sub.id
                  where sub.name = '역사';
                  
-- 4) 국어 과목을 듣는 서울 거주 학생 목록
select sub.name, stu.id, stu.name
from Enroll en inner join Subject sub on en.subject = sub.id
			   inner join Student stu on en.student = stu.id
where sub.name = '국어' and stu.address = '서울';

-- 5) 역사 과목을 수강중인 지역별 학생수
select stu.address, count(*)
from Enroll en inner join Subject sub on en.subject = sub.id
			   inner join Student stu on en.student = stu.id
where sub.name = '역사'
group by stu.address;

-- > join이 되면 테이블이 합쳐진다고 생각하면 됨.

-- 6) 과목별 수강중인 지역별 학생수
select sub.id, sub.name, stu.address, count(*)
from Enroll en inner join Subject sub on en.subject = sub.id
			   inner join Student stu on en.student = stu.id
group by sub.id, stu.address;



select * from Subject;
    