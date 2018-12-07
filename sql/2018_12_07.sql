show variables like '%commit%'; 
-- Transaction 필수!!
START TRANSACTION;

update Student set name = '111' where id = 1;
select name from Student where id = 1;


update Student set name = '강모현' where id = 1;
select name from Student where id = 1;


ROLLBACK;

START TRANSACTION;
-- 과목명을 가나다순으로 한 줄로
SELECT GROUP_CONCAT(name) FROM Subject;
select name from Subject order by name;

-- temporary table (local variable과 비슷한 개념), session이 끝나면 사라지는 table
create temporary table temp(
    name char(5) not null);

insert into temp(name) select name from Subject order by name;

select group_concat(name) from temp;

select name from temp;

drop temporary table temp;
-- --------------------------------------------------------------------------------

-- 7번 문제에서 과목을 한 줄로
select min(sub.name) subject_name, 
				 (case stu.gender
				  when 1 then '남자'
						 else '여자' end) as 'gender', count(*) as 'num of students'
from Enroll en inner join Student stu on en.student = stu.id
			   inner join Subject sub on en.subject = sub.id
where stu.address = '서울'
group by sub.id, stu.gender
order by subject_name asc, stu.gender desc;