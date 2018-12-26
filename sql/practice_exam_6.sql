
drop procedure if exists sp_try_new;
delimiter //
create procedure sp_try_new()

begin

declare try_end boolean default false;
declare res_subject smallint default 0;
declare res_sub_name varchar(5);
declare res_student varchar(5);
declare res_total int default 0;
declare i tinyint default 0;

declare res_cursor cursor for
	select t_subject, t_sub_name, t_student, t_total from temp_try;

declare continue handler for not found set try_end = TRUE;

drop table if exists res_new;
create temporary table res_new(

	과목 varchar(5) default '0', 
	rank1 varchar(5) default '0', 
	score1 smallint default 0, 
	rank2 varchar(5),
    score2 smallint,
    rank3 varchar(5) default '0',
    score3 smallint default 0
);

open res_cursor;
	res_loop: loop
		fetch res_cursor into res_subject, res_sub_name, res_student, res_total ;

	set i = 1;
    if not exists (select 과목 from res_new where 과목 = i) 
		then insert into res_new(과목, rank1, score1) value(res_subject, res_student, res_total);
	elseif not exists (select rank2from res_new where 과목 = i) 
		then
			 update res_new set rank2 = res_student, score2 = res_total;
	elseif exists (select rank2, score2 from res_new where 과목 = i)
		then
             update res_new set rank3 = res_student, score3 = res_total;
		END IF;
        	
     
     if try_end then
			leave res_loop;
		end if;

	end Loop res_loop;

close res_cursor;      

end //
delimiter ;

call sp_try_new();

select * from res_new;