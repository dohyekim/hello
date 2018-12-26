drop procedure if exists sp_like_prof;

delimiter //

CREATE Procedure sp_like_prof() 
	BEGIN
		declare low_grade_avg smallint;
		declare prof_like_avg smallint;
		declare prof_like_max smallint;	
		declare prof_like_min smallint;	
		declare stu_cnt_avg smallint;	
		drop temporary table if exists temp;
		 
		create temporary table temp (
				id smallint auto_increment primary key,
				prof varchar(5), sub_id varchar(5), 
				stu_cnt int, ratio_1 smallint default 0, 
				low_grade float default 0, ratio_2 smallint default 0, 
				prof_like smallint default 0, ratio_3 smallint default 0
				); 

		insert into temp(prof, sub_id, stu_cnt, low_grade, prof_like)
					select max(p.name), max(sub.name), max(sub.students), 
						   min((g.midterm + g.final)/2), max(p.likecnt)
					from Enroll en inner join Subject sub on en.subject = sub.id
										   inner join Prof p on sub.prof = p.id
										   inner join Grade g on g.enroll = en.id
					group by sub.prof;
                    
		set stu_cnt_avg = (select avg(stu_cnt) from temp);	
        
		update temp set ratio_1 = case 
									when stu_cnt < stu_cnt_avg then 4 
									when stu_cnt >= stu_cnt_avg then 5 
										end;
			
			
		set low_grade_avg = (select avg(low_grade) from temp);

		update temp set ratio_2 = case 
									when low_grade > low_grade_avg then 5
									when low_grade = low_grade_avg then 4
									when low_grade < low_grade_avg then 3
									end;


		set prof_like_avg = (select avg(prof_like) from temp);
		set prof_like_max = (select max(prof_like) from temp);
		set prof_like_min = (select min(prof_like) from temp);

		update temp set ratio_3 = case
									when prof_like = prof_like_max then 5
									when prof_like > prof_like_avg then 4
									when prof_like = prof_like_avg then 3
									when prof_like < prof_like_avg then 2
									when prof_like = prof_like_min then 1
									end;

		select prof 교수, sub_id 과목, (ratio_1 * 0.2 + ratio_2 * 0.3 + ratio_3 * 0.5) 총점 from temp order by 총점 desc limit 3;

		
	END //
    
DELIMITER ;

call sp_like_prof();
