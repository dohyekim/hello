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
select id from Enroll; 

select * from Enroll;
insert into Grade(midterm) select ceil(rand() * 100);
update Grade set midterm = ceil(rand() * 100);
update Grade set final = ceil(rand() * 100);



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

-- Report 2 (과목, 평균, 최고 득점자, 총 학생수 [정렬] 과목 (가나다 순))

-- 최고 득점자 (d앚직 못함........)
from Enroll as en inner join Student s on en.student = s.id
                  inner join Subject sub on en.subject = sub.id
                  inner join Grade gd on gd.enroll = en.id;

-- 평균
select sub.name, (sum(midterm) + sum(final)) / count(*) / 2 as 'average'
from Enroll as en inner join Student s on en.student = s.id
                  inner join Subject sub on en.subject = sub.id
                  inner join Grade gd on gd.enroll = en.id
group by sub.name;