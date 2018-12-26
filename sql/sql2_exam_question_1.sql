
-- view 생성

create view v_stu_name_subcnt_avg as
	select stu.id 학번, stu.name 학생명, count(*) 수강과목수,
		   cast((avg(g.midterm + g.final) / count(*)) as signed integer) 평균점수
    from Enroll en inner join Student stu on en.student = stu.id
                   inner join Grade g on g.enroll = en.id
	group by en.student;
    
-- view 확인
    
select * from v_stu_name_subcnt_avg;