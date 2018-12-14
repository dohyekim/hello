create view v_enroll_subject as
	select e.*, s.name, s.prof
		from Enroll e inner join Subject s on e.subject = s.id;
        
        
desc v_enroll_subject;

show create view v_enroll_subject;

select current_user();

select * from v_enroll_subject order by id;

select * from information_schema.views
        where table_schema='dooodb';
        
-- Try this 1번
create view v_grade_enroll as
	select g.*, e.subject, e.student
     from Grade g inner join Enroll e on g.enroll = e.id;
     
     
select subject, count(*)
from v_grade_enroll
group by subject;

-- Try this 2번
create view v_stu_sub_grade_enroll as
	select s.id 학번, s.name 학생명, sub.id 과목번호, sub.name 과목명, 
    g.midterm 중간, g.final 기말, (g.midterm + g.final) 총점, 
    cast(((g.midterm + g.final) / 2) as signed integer) 평균,
    (case when cast(((g.midterm + g.final) / 2) as signed integer) >= 90 then 'A'
		 when cast(((g.midterm + g.final) / 2) as signed integer) >= 80 then 'B'
		 when cast(((g.midterm + g.final) / 2) as signed integer) >= 70 then 'C'
         when cast(((g.midterm + g.final) / 2) as signed integer) >= 60 then 'D'
         else 'D' end) 학점
	 from Enroll en inner join Student s on en.student = s.id
				    inner join Subject sub on en.subject = sub.id
                    inner join Grade g on g.enroll = en. id;

-- 역사 과목의 수강 학생들을 성적순으로 출력하시오.
    
select 과목명, 학생명, 총점, 학점 
 from v_stu_sub_grade_enroll
 where 과목명 = '역사'
 order by 총점 DESC, 학점;    
 
 
 ALTER table Subject add column students smallint default 0 not null;
 desc Subject;
 
 update Subject sub set students =
 (select count(*)
 from Enroll
 where subject = sub.id
 group by subject);

delimiter // 
 create trigger tr_enroll_subject_students
	after insert on Enroll for each row
begin
end //
delimiter ;    

select * from Subject where id = 1;


insert into Enroll(subject, student) values(1,200);

select count(*) from Enroll where subject = (select subject from Enroll where id = old.id);


delete from Enroll where id = 1101;
select * from Student;
select * from Subject;
select * from Grade;
select * from Enroll;