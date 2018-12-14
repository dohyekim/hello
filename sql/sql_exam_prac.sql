-- 성적 테이블(Grade), 컬럼(중간고사, 기말고사)을 만들고 각 수강 과목에 대해 중간고사, 기말고사 점수를 sample로 채우고
-- 다음과 같은 Report를 작성하시오.
-- 같은 쿼리를 2번 실행하면 쿼리를 두 번 작성하기
-- 수강내역: 500명 * 수강과목 수
-- 점수: 0~100점
-- Grade는 A,B,C,D,F
-- REPORT1 모양은 과목, 학생명, 중간고사, 기말고사, 총점, 평균, (과목별)학점, 석차(option) 순으로. [정렬] 과목별 성적순으로
-- REPORT2 모양은 과목, 평균, 최고 득점자, 총 학생수 [정렬] 과목 (가나다 순)
-- REPORT3 모양은 학생명, 학교명, 과목수, 총점, 평균, 평점
START TRANSACTION;

CREATE TABLE `Grade` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `enroll` int(11) NOT NULL,
  `midterm` int(11) NOT NULL DEFAULT '0',
  `final` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `Grade_ibfk_1` (`enroll`),
  CONSTRAINT `Grade_ibfk_1` FOREIGN KEY (`enroll`) REFERENCES `Enroll` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4096 DEFAULT CHARSET=utf8;

-- insert into Grade(sub_stu) 

select * from Enroll;
select * from Grade;
insert into Grade(enroll) select id from Enroll;
update Grade set midterm = ceil((0.5 + rand()/2) * 100) where id > 0;
update Grade set final = ceil((0.5 + rand()/2) * 100) where id > 0;

-- Report 1
select sub.name as 과목명, 
s.name as 학생, 
gd.midterm 중간 , gd.final 기말 , 
(gd.midterm + gd.final) 총점, 
cast((gd.midterm + gd.final) / 2 as signed integer) 평균,
(case when cast((gd.midterm + gd.final) / 2 as signed integer)>= 90 then 'A'
	when cast((gd.midterm + gd.final ) / 2 as signed integer) >= 80 then 'B'
    when cast((gd.midterm + gd.final ) / 2 as signed integer) >= 70 then 'C'
    when cast((gd.midterm + gd.final ) / 2 as signed integer) >= 60 then 'D'
else 'F' end) 학점
from Enroll as en inner join Student s on en.student = s.id
                  inner join Subject sub on en.subject = sub.id
                  inner join Grade gd on gd.enroll = en.id
                  order by sub.name , 학점 asc;

START TRANSACTION;
-- Report 2 (과목, 평균, 최고 득점자, 총 학생수 [정렬] 과목 (가나다 순))

-- 최고 득점자 (서칭)

create table Temp(
select (midterm + final) total,
	   sub.name subject,
       s.name student
from Enroll as en inner join Student s on en.student = s.id
                  inner join Subject sub on en.subject = sub.id
                  inner join Grade gd on gd.enroll = en.id);
          
select Temp.student, Temp.subject, Temp.total from
(select subject, max(total) max
from Temp group by subject) a
inner join Temp on a.subject = Temp.subject and a.max = Temp.total;

select * from Subject;
select subject from Temp group by subject;
commit;
-- 서브쿼리
select max(sub.name) subject, s.name, max(midterm), max(final)
		from Enroll as en inner join Student s on en.student = s.id
						  inner join Subject sub on en.subject = sub.id
					      inner join Grade gd on gd.enroll = en.id
		group by en.subject, s.id;
-- 실패
select a.subject, a.name, max(a.m + a.f)
from (select max(sub.name) subject, s.name, max(midterm) m, max(final) f
		from Enroll as en inner join Student s on en.student = s.id
						  inner join Subject sub on en.subject = sub.id
					      inner join Grade gd on gd.enroll = en.id
		group by en.subject, s.id) a
	inner join Grade gd on a.m = gd.midterm and a.f = gd.final
    -- inner join Subject sub on a.subject = sub.name
    -- inner join Student s on a.name = s.name
group by a.subject;




select * from Grade;
-- 실패
select max(sub.name) subject, s.name, max(gd.midterm + gd.final) total
		from Enroll as en inner join Student s on en.student = s.id
						  inner join Subject sub on en.subject = sub.id
					      inner join Grade gd on gd.enroll = en.id
		group by en.subject, s.id;
        

select sub.name 과목, (select midterm + final from Grade order by midterm + final desc limit 1) 총점
from Enroll as en inner join Student s on en.student = s.id
                inner join Subject sub on en.subject = sub.id
                inner join Grade gd on gd.enroll = en.id     
                group by sub.name;

select sub.name 과목, s.name 학생명,  (midterm + final) 총점
from Enroll as en inner join Student s on en.student = s.id
                inner join Subject sub on en.subject = sub.id
                inner join Grade gd on gd.enroll = en.id
order by midterm + final desc;





start transaction;
-- 과목 이름, 평균, 총 학생수

select sub.name as 과목명, 
s.name as 학생, 
gd.midterm 중간 , gd.final 기말 , 
(gd.midterm + gd.final) 총점, 
cast((gd.midterm + gd.final) / 2 as signed integer) 평균,
(case when cast((gd.midterm + gd.final) / 2 as signed integer)>= 90 then 'A'
	when cast((gd.midterm + gd.final ) / 2 as signed integer) >= 80 then 'B'
    when cast((gd.midterm + gd.final ) / 2 as signed integer) >= 70 then 'C'
    when cast((gd.midterm + gd.final ) / 2 as signed integer) >= 60 then 'D'
else 'F' end) 학점,
select max(sub.name) 과목명, 
(sum(midterm) + sum(final)) / count(*) / 2 as 평균,
count(*) as '수강생 수'
from Enroll as en inner join Student s on en.student = s.id
                  inner join Subject sub on en.subject = sub.id
                  inner join Grade gd on gd.enroll = en.id
                  
                  group by sub.id
                  order by sub.name , 학점 asc;
                  
select max(sub.name) as 과목명, cast((sum(midterm) + sum(final)) / count(*) / 2 as signed integer ) as 평균,
count(*) as '총 학생수'
from Enroll as en inner join Student s on en.student = s.id
                  inner join Subject sub on en.subject = sub.id
                  inner join Grade gd on gd.enroll = en.id
group by sub.id;


COMMIT;
rollback;

-- Report 3 (학생명, 학교명, 과목수, 총점, 평균, 평점)
start transaction;

select min(s.name) as 학생명, 
count(*) as 과목수, 
sum(midterm + final) as 총점, 
cast(sum(gd.midterm + gd.final) / (count(en.subject) * 2) as signed integer) as 평균,
(case when 
cast(sum(gd.midterm + gd.final) / (count(en.subject) * 2) as signed integer) >= 90 then 'A'
when
cast(sum(gd.midterm + gd.final) / (count(en.subject) * 2) as signed integer) >= 80 then 'B'
when
cast(sum(gd.midterm + gd.final) / (count(en.subject) * 2) as signed integer) >= 70 then 'C'
when
cast(sum(gd.midterm + gd.final) / (count(en.subject) * 2) as signed integer) >= 60 then 'D'
else 'F' end) as 학점
from Enroll en inner join Grade gd on gd.enroll = en.id
			   inner join Student s on en.student = s.id
			   inner join Subject sub on en.subject = sub.id
group by en.student
order by 학점, 학생명;

commit;
            