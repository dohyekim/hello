CREATE TABLE `dooodb`.`Classroom` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`id`));

start transaction;

truncate Classroom;

insert Classroom(name) value(101);
insert Classroom(name) value(102);
insert Classroom(name) value(103);
insert Classroom(name) value(104);
insert Classroom(name) value(105);
insert Classroom(name) value(106);
insert Classroom(name) value(107);
insert Classroom(name) value(108);
insert Classroom(name) value(109);
insert Classroom(name) value(110);

ALTER TABLE `dooodb`.`Subject` 
ADD COLUMN `classroom` INT(11) NULL AFTER `prof`;

commit;
start transaction;
rollback;


update Subject set classroom = id ;

select * from Subject;
commit;

ALTER TABLE `dooodb`.`Subject` 
ADD INDEX `fk_classroom_classroom_idx` (`classroom` ASC);
;
ALTER TABLE `dooodb`.`Subject` 
ADD CONSTRAINT `fk_classroom_classroom`
  FOREIGN KEY (`classroom`)
  REFERENCES `dooodb`.`Classroom` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

select * from Subject;
