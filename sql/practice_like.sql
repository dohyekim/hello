select * from Student;

select id, name from Student where id between 10 and 20;

select * from Student where id in (1,3,5,7,9);

select name from Student where name like '김%';

select id, name from Student where name like '__영';

select id, name from Student where name like '문_이';

select id, birthday from Student where birthday between 19700101 and 20001231 order by birthday;  

select id, name from Student where name between '가' and '깋';


select id, name from Student where name between '바' and '빟';

select * from Student where name >/ '바' and name <'사';

select * from Student where substring(name,3) >/ '바' and name <'사';

select * from Student where email like 'a%';

select * from Student where email like 'a%' and phone like '010-9%';

select email from Student where email like '%@gmail.com';

select count(distinct email) from Student where email like '%gmail.com';

select * from Student;