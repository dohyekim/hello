-- 같은 이름의 함수가 있으면 지운다.
drop function if exists f_student_avg ;

-- 함수 만들기
delimiter //
create function f_student_avg(stu_id int)
returns int
begin
return
(
select round(avg(midterm + final) / 2) 평균 
from Grade g inner join Enroll en on g.enroll =en.id
where en.student = stu_id
);
end //

delimiter ;

select * from v_stu_name_subcnt_avg;
-- 확인
select f_student_avg(198);

