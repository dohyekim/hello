insert into Enroll(subject, student) values(3, 999);

select id, name, students from Subject; 

delete from Enroll where id = 3654;

select * from Enroll where subject = 3 and student = 999;

-- 학생테이블(Student)에 수강과목수(sbjects) 컬럼을 추가하고, 
-- sbjects 값을 기존 데이터로 모두 초기화(update) 한 후,
-- 수강 신청/취소시 sbjects를 증감 시키는 Trigger를 작성하시오.

ALTER table Student add column sbjects smallint default 0 not null;

 update Subject sub set students =
 (select count(*)
 from Enroll
 where subject = sub.id
 group by subject);
 
