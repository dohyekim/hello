select gender, count(name) from Student group by gender;
select * from Student;

select name, count(*) from Student group by name having count(*) > 1;


-- COUNT(*) 는 ROW수를 반환한다
select count(*) from Student;

-- BIRTH 순서대로
select * from Student order by birthday limit 10;
select birthday from Student order by birthday;

-- 김씨 10명
select * from Student where name like '김%' order by name asc limit 10;

-- 서울 지역 학생, 학번 역순
select id, name, address from Student where address = '서울' order by id desc limit 10;

-- 서울 지역 학생 중 90년 이후 출생자
select * from Student where address = '서울' and birthday between '19900101' and '99991231' order by birthday asc; 
select * from Student where address = '서울' and birthday between '1990-01-01' and '9999-12-31' order by birthday asc;

-- subject테이블의 과목명과 담당 교수명을 join하기
select c.*, s.name as 'sub name' from Club as c inner join Student as s on sub.id = sub.name;

select phone from Student;
select * from Student;
select email from Student ;
select birthday from Student order by birthday;

-- outer join 대신에
select sbj.*, (select name from professor where id = sbj.prof) from Subject sbj;

-- inner join query
select sub.*, prof.name from Subject sub inner join Prof prof on sub.prof = prof.id;
select sub.name, prof.name from Subject sub inner join Prof prof on sub.prof = prof.id;







