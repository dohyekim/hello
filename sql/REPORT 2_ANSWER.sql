-- Report 2 (과목, 평균, 최고 득점자, 총 학생수 [정렬] 과목 (가나다 순))


select max(sub.name) '과목', cast(avg(g.midterm + g.final) / 2 as signed integer) '평균', 
	   (select ss.name
			from Grade gr inner join Enroll enr on gr.enroll = enr.id
						  inner join Subject subj on enr.subject = subj.id
                          inner join Student ss on enr.student = ss.id
			where enr.subject = sub.id
			order by (gr.midterm + gr.final) desc limit 1) 최고득점자
        
, count(*)
from Grade g inner join Enroll en on g.enroll = en.id
			 inner join Subject sub on en.subject = sub.id
             inner join Student stu on en.student = stu.id
group by sub.id
order by 과목;

-- 확인
select max(sub.name) '과목' , cast(avg(g.midterm + g.final) / 2 as signed integer) '평균', count(*)
from Grade g inner join Enroll en on g.enroll = en.id
			 inner join Subject sub on en.subject = sub.id
             group by sub.id;


select en.subject, g.id, g.midterm, g.final, (g.midterm + g.final) 
from Grade g inner join Enroll en on g.enroll = en.id
order by midterm + final desc; 

select subj.id, subj.name, (gr.midterm + gr.final)
	   from Grade gr inner join Enroll enr on gr.enroll = enr.id
				    inner join Subject subj on enr.subject = subj.id
		where subj.id = 1
		order by (gr.midterm + gr.final) desc limit 1