drop procedure if exists sp_res_cursor;
delimiter //
create procedure sp_res_cursor()

begin
declare try_end boolean default false;
declare res_subject smallint default 0;
declare res_student varchar(5);
declare res_total int default 0;
declare res_sub_name varchar(5);
declare n tinyint default 1;
declare i tinyint;

declare res_cursor cursor for
	select t_subject, t_sub_name, t_student, t_total from temp_try;

declare continue handler for not found set try_end = TRUE;

drop table if exists temp_res;
create temporary table temp_res(

	과목 varchar(5) default '0', 
	rank1 varchar(5) default '0', 
	score1 smallint default 0, 
	rank2 varchar(5) default '0',
    score2 smallint default 0,
    rank3 varchar(5) default '0',
    score3 smallint default 0
);

open res_cursor;
set n = 1;
set i = 1;
	res_loop: loop

		fetch res_cursor into res_subject, res_sub_name, res_student, res_total ;
		
	IF res_subject = n then set n = n + 1; 
		insert into temp_res set 과목 = res_sub_name, rank1 = res_student, score1 = (res_total / 2);
	
    ELSE 
		set i = i + 1;
        SET @sql = CONCAT('update temp_res set ', 'rank', i,' = "res_student" where 과목 = "res_sub_name"');
		PREPARE myQuery from @sql;
		EXECUTE myQuery;
        
        
		SET @sql2 = CONCAT('update temp_res set ','score', i,' = ("res_total" / 2) where 과목 = "res_sub_name"');
		PREPARE myQuery2 from @sql2;
		EXECUTE myQuery2;
		
        if i = 3 then set i = 1;
			end if;
		
	
		
	END IF;
        if try_end then
			leave res_loop;
		end if;

	end Loop res_loop;

close res_cursor;      

end //
delimiter ;

call sp_res_cursor();

select * from temp_res;