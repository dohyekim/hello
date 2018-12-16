-- Try this 1번 

 delimiter // 
CREATE trigger tr_enroll_student_sbjects
	after insert on Enroll for each row
begin
	update Student
    set sbjects = sbjects + 1
    where id = new.student;
end //
delimiter ;

-- Try this 2번

delimiter //
CREATE TRIGGER tr_enroll_student_sbjects_delete
 BEFORE DELETE ON `Enroll` FOR EACH ROW
BEGIN
delete from Grade where enroll = old.id;
update Student
set sbjects = sbjects - 1
where id = (select student from Enroll where id = old.id);
END //
delimiter ;

delimiter //
CREATE DEFINER=`dooo`@`172.17.0.1` trigger tr_enroll_subject_students_delete
    before delete on Enroll For Each Row
BEGIN
    delete from Grade
     where enroll = OLD.id;
     
    update Subject
       set students = 
           (
            select count(*) - 1 from Enroll
             where subject = (select subject from Enroll where id = OLD.id)
           )
     where id = (select subject from Enroll where id = OLD.id);
END //
delimiter ;

-- Try this 3번

delimiter //

create trigger tr_subject_prof
before insert
on Subject for each row
	begin
		if new.prof is null 
			then set new.prof = (select id from Prof order by rand() limit 1);
		end if;
	end //

delimiter ;

select * from Subject;
desc Subject;
insert into Subject (name, prof) values ('열역학', null);

select * from Student;

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
