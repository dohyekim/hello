

show index from Student;
show create table Student;

desc Student;

create table t_student like Student;
select * from t_student;
  ' 
select * from Student;
insert into t_student select * from Student;





insert into Student(name, addr, birth, tel, email) 
			values('김t_studentStudentt_student김김', '서울시 안녕', '19761213', '+821054247836',
					'annyeong@gmail.com');

insert into Student(name, addr, birth, tel, email) 
			values('임임임', '아오시 안녕', '19761213', '+821054247836',
					'annyeong@gmail.com');

insert into Student(name, addr, birth, tel, email) 
			values('심심심', '대박시 안녕', '19761213', '+821054247836',
					'annyeong@gmail.com');

-- truncate table t_student;

select * from Student;


