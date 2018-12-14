
CREATE TABLE `Student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL DEFAULT '0',
  `phone` varchar(45) NOT NULL DEFAULT '0',
  `birthday` date DEFAULT NULL,
  `email` varchar(45) NOT NULL DEFAULT '0',
  `address` varchar(3) NOT NULL DEFAULT '0',
  `gender` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `fk_dept-dept_idx` (`dept`),
  CONSTRAINT `fk_dept-dept` FOREIGN KEY (`dept`) REFERENCES `Dept` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=4073 DEFAULT CHARSET=utf8;


CREATE TABLE `dooodb`.`Dept` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL DEFAULT 0,
  `prof` INT NOT NULL DEFAULT 0,
  `student` INT NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`));

select * from Dept;
select * from Student;
desc Dept;

ALTER TABLE `dooodb`.`Student` 
ADD COLUMN `dept` INT NOT NULL AFTER `gender`;

select * from Student;
truncate Dept;
START TRANSACTION;

insert into Dept(name) value('English');
insert into Dept(name) value('Math');
insert into Dept(name) value('Korean');
insert into Dept(name) value('History');
insert into Dept(name) value('Education');
select * from Dept;

commit;
start transaction;

ALTER TABLE `dooodb`.`Student` 
ADD COLUMN `dept` INT(11) NOT NULL DEFAULT 0 AFTER `gender`;
 
update Student set dept = 
(select cast((abs(rand()-0.5) * 10) as signed integer) );

update Student set dept = 1
where dept = 0;

commit;

ALTER TABLE `dooodb`.`Student` 
ADD INDEX `fk_dept_dept_idx` (`dept` ASC);

ALTER TABLE `dooodb`.`Student` 
ADD CONSTRAINT `fk_dept_dept`
  FOREIGN KEY (`dept`)
  REFERENCES `dooodb`.`Dept` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
  
select * from Student;

start transaction;
         

update Subject set classroom =
(select id from Classroom order by rand() limit 1);

select ceil(rand() * 10);

select * from Subject;
rollback;
commit;

select s.id, d.name
from Student s inner join Dept d
on s.dept = d.id;

select * from Dept;

ALTER TABLE `dooodb`.`Dept` 
CHANGE COLUMN `prof` `prof` SMALLINT(5) UNSIGNED NOT NULL DEFAULT '0' ;


ALTER TABLE `dooodb`.`Dept` 
ADD INDEX `fk_prof_prof_idx` (`prof` ASC);



ALTER TABLE `dooodb`.`Dept` 
ADD CONSTRAINT `fk_prof_prof`
  FOREIGN KEY (`prof`)
  REFERENCES `dooodb`.`Prof` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `dooodb`.`Dept` 
ADD INDEX `fk_student_student_idx` (`student` ASC);

ALTER TABLE `dooodb`.`Dept` 
ADD CONSTRAINT `fk_stu_stu`
  FOREIGN KEY (`student`)
  REFERENCES `dooodb`.`Student` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

SELECT * from Classroom;
