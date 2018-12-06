create table Club(
	id smallint unsigned not null auto_increment primary key,
	name varchar(31) not null,
	createdata timestamp not null default current_timestamp,
	leader int(11),
	constraint foreign key fk_leader_student (leader) references Student (id) 
    on delete restrict
    on update restrict 
);

insert into Club(name, leader) values ('요트부', 100);
insert into Club(name, leader) values ('밴드부', 200);
insert into Club(name, leader) values ('봉사부', 300);

select c.*, s.name as 'student name' 
from Club as c inner join Student as s on c.leader = s.id;

insert into Prof(name, likecnt) select name, ceil(rand() * 100) 
from Student order by rand() limit 100;

select name, ceil(rand() * 100) 
from Student order by rand() limit 100;

insert into Subject(name, prof) select '국어', id from Prof order by rand() limit 10;
update Subject set name='물리' where id = 3;
update Subject set namename='미술' where name='국어' and id <> 10 limit 1;

select * from Subject;

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

CREATE TABLE `Student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `phone` varchar(45) NOT NULL,
  `birthday` date NOT NULL,
  `email` varchar(45) NOT NULL,
  `address` varchar(3) NOT NULL,
  `gender` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1002 DEFAULT CHARSET=utf8;


CREATE TABLE Enroll(
	id int not null auto_increment primary key,
    subject smallint(5) unsigned not null,
    student int(11) not null,
    constraint foreign key fk_student_student (student) references Student (id)
    on delete restrict,
	constraint foreign key fk_subject_subject (subject) references Subject (id)
    on delete restrict
);

-- 밑의 쿼리문은 cross join의 개념과 비슷
insert into Enroll(student, subject) select s1.id, s2.id 
from Student s1, Subject s2 where s1.id > 10 and s1.id <= 200 and s2.id <= 5;

-- subquery 규칙
-- 컴퓨터는 from 뒤부터 작업한다.
-- select a, b from A, B라고 한다면 a와 b의 개수는 같아야 한다. a가 1000, b가 10이면 만 개의 data가 나오게 된다.
-- select stu.id, sbj.id from Student stu, Subject sbj
-- from 뒤에 나오는 것은 파일(즉 파일에서 읽어오겠다).



select s.name, sbj.id from Student s, (select id from Subject order by rand() limit 3) sbj 
where s.id > 200 and s.id < 205;

-- select s.name, from Student s, 

-- not in (select subject from Enroll) ;

select id from Subject order by rand() limit 3;

select s.name, sbj1.id from Student s, (select id from Subject order by rand() limit 3) sbj1 
where s.id > 200 and s.id < 205;

select s.name, sbj2.id from Student s, 
(select id not in (select id from Subject order by rand() limit 3) 
from Subject order by rand() limit 3) sbj2 where s.id >= 205 and s.id < 210;

select id from Subject where Subject.id not in (select id from Subject order by rand() limit 3);

select s.name, sbj.id from Student s, (select id from Subject order by rand() limit 3) sbj 
where s.id > 200 and s.id < 205;



-- 과목별 학생수
select subject, count(*) from Enroll group by subject;
-- 한 과목에 중복 학생 존재 여부 체크
select subject, student, count(*) from Enroll group by subject, student having count(*) > 1;

select student from Enroll group by subject;


select id from Student where id <=10 order by rand();

select name from Student;
select * from Enroll;
select * from Subject;

desc Student;

desc Club;
select * from Club;
