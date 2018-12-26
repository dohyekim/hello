drop trigger if exists tr_club_leader;

delimiter //
create trigger tr_club_leader
after insert
on Club for each row
begin
	declare student_id int;

	set student_id = 
					(select stu.id 
					 from Student stu inner join ClubMember cm on stu.id = cm.student
					 where cm.student <> 1 and cm.student <> 2
					 order by rand()
					 limit 1);
					 
	insert into ClubMember(club, student, level) values(new.id, student_id, 1);

end //

delimiter ;

start transaction;
insert into Club(name) values('여행부');
select * from Club;
select * from ClubMember;
select student, count(*) from ClubMember
where level = 1 or level = 2
group by student
having count(*) > 1;
rollback;