create table Test(
	id tinyint unsigned not null auto_increment,
    name char(5) not null,
    primary key(id)
);


desc Test;
show create table Test;

ALTER DATABASE dooodb DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;


insert into Test3(ttt) values('김일수');

select * from Test3;

show processlist;

show variables;

show variables like '%session%';

show table status;

select * from Student;