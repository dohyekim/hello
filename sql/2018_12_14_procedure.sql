drop procedure if exists sp_stu_cnt;
delimiter //
CREATE Procedure sp_stu_cnt(sub_name varchar(31)) 
BEGIN
	declare sbj_id smallint default 0;
    
    select id into sbj_id from Subject where name= sub_name;
    
	select count(*) stu_cnt, avg((g.midterm + g.final) / 2) avr
      from Enroll e inner join Grade g on e.id = g.enroll
		where e.subject = sbj_id;
END //
DELIMITER ;

call sp_stu_cnt('국어');





select * from Club;
select * from ClubMember;