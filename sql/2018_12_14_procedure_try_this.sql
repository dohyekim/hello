drop procedure if exists sp_club_member;

delimiter //
create Procedure sp_club_member(club_name varchar(31))
begin

declare v_club_id varchar(5);

select id into v_club_id from Club where name = club_name;

select s.name '학생명', fn_clubmember_level(c.level) '등급'
from ClubMember c inner join Student s
					on c.student = s.id
where c.club = v_club_id;

end //
delimiter ;

call sp_club_member('요트부');

