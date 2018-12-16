
-- Try this 1 
-- 과목명을 주면, 해당 과목의 수강 학생수를 반환하는 함수를 만드시오.
-- 1) Query 작성
-- 2) 입력 파라미터 설정, 리턴 타입 정의
-- 3) BEGIN ~ END 사이에 Query 입력

delimiter //
create function fn(sub_name varchar(5))
returns smallint
begin
	return 
		(
        select count(*)
			from Enroll e inner join Subject sub where e.subject = sub.id
		group by sub.name
		having sub.name = sub_name
		);
end //

delimiter ;

-- 확인

select fn_student_count('생물');

-- 활용
select name, fn_student_count(name) from Subject;


desc Subject;

-- Query 1
select count(*) 
from Enroll e inner join Subject sub where e.subject = sub.id
group by sub.name;

-- Query 1과 같은 Query
select count(*) 
from Enroll
where subject = (select id from Subject where name = '역사');

select * from Student;
alter table Student add column regdt timestamp default current_timestamp not null;
