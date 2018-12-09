
create table Prof(
	id smallint unsigned not null auto_increment primary key,
	name varchar(31) not null,
    likecnt int default 0 not null
    );
    

    
CREATE TABLE Subject(
  id smallint(5) unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name varchar(31) NOT NULL,
  prof smallint unsigned not null,
  CONSTRAINT FOREIGN KEY fk_prof_prof (prof) references Prof (id)
  on delete restrict
  on update restrict
);

CREATE TABLE Enroll(
	id int not null auto_increment primary key,
    subject smallint(5) unsigned not null,
    student int(11) not null,
    constraint foreign key fk_student_student (student) references Student (id)
    on delete restrict,
	constraint foreign key fk_subject_subject (subject) references Subject (id)
    on delete restrict
);

insert into Prof(name, likecnt) select name, ceil(rand() * 100) from Student order by rand() limit 100;
select name, ceil(rand() * 100) from Student order by rand() limit 100;

insert into Subject(name, prof) select '국어', id from Prof order by rand() limit 10;
update Subject set name='물리' where id = 3;
update Subject set name='체육' where name='국어' and id <> 10 limit 1;

UPDATE Student 
SET 
    gender = (CASE
        WHEN
            phone LIKE '010-5%'
                OR phone LIKE '010-2%'
                OR phone LIKE '010-6%'
                OR phone LIKE '010-4%'
                OR phone LIKE '010-8%'
        THEN
            1
        ELSE 0
    END);

insert into Enroll(student, subject)
 select id, (select id from Subject order by rand() limit 1) sid from Student order by id;

insert into Enroll(student, subject)
 select id, (select id from Subject order by rand() limit 1) sid from Student order by rand() limit 500
 on duplicate key update student = student;
 
insert into Enroll(student, subject)
 select id, (select id from Subject order by rand() limit 1) sid from Student order by rand() limit 500
 on duplicate key update student = student;


select * from Grade;



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
select  sub.name as 'subject name', s.name as 'student name', gd.midterm, gd.final, (midterm + final) 합계, substring(((midterm + final) / 2),1,2) 평균,
(case when substring(((midterm + final) / 2),1,2) >= 90 then 'A'
	when substring(((midterm + final) / 2),1,2) >= 80 then 'B'
    when substring(((midterm + final) / 2),1,2) >= 70 then 'C'
    when substring(((midterm + final) / 2),1,2) >= 60 then 'D'
else 'F' end) 학점
from Enroll as en inner join Student s on en.student = s.id
                  inner join Subject sub on en.subject = sub.id
                  inner join Grade gd on gd.enroll = en.id;

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


commit;


start transaction;
-- 과목 이름, 평균, 총 학생수
select sub.name, (sum(midterm) + sum(final)) / count(*) / 2 as 'average',
count(*) as total
from Enroll as en inner join Student s on en.student = s.id
                  inner join Subject sub on en.subject = sub.id
                  inner join Grade gd on gd.enroll = en.id
group by sub.name;


COMMIT;
rollback;

-- Report 3 (학생명, 학교명, 과목수, 총점, 평균, 평점)
