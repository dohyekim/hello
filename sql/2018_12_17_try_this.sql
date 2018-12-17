/*
select 학생명,과목번호, 과목명, 총점
	from v_stu_sub_grade_enroll v_en
		inner join Subject sub on v_en.과목번호 = sub.id  order by 과목번호, 총점 desc;
  */
  
drop procedure if exists sp_try_cursor;
delimiter //
create procedure sp_try_cursor()

begin

declare _sbj smallint default 1;
declare try_end boolean default false;
declare try_total int default 0;
declare try_student varchar(5);
declare try_subject int default 0;
declare try_sub_name varchar(5);

declare try_cursor cursor for
	select 학생명, 과목번호, 과목명, 총점 from v_stu_sub_grade_enroll v
		inner join Subject sub on v.과목번호 = sub.id
	order by 과목번호, 총점 desc; 

declare continue handler for not found set try_end = TRUE;

drop table if exists temp_try;
create temporary table temp_try(

	t_student varchar(5) default '0', 
	t_subject smallint default 0, 
	t_sub_name varchar(5) default '0', 
	t_total int(11) default 0
);

open try_cursor;

	try_loop: loop

		fetch try_cursor into try_student, try_subject, try_sub_name, try_total ;
	        
	IF ((select count(*) from temp_try where t_subject = try_subject) < 3) then
		insert into temp_try value(try_student, try_subject, try_sub_name, try_total);

		
		END IF;
        if try_end then
			leave try_loop;
		end if;

	end Loop try_loop;

close try_cursor;      




end //
delimiter ;
