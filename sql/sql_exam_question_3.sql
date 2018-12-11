select * from Club;

ALTER TABLE `dooodb`.`Club` 
DROP COLUMN `createdata`;
ALTER TABLE `dooodb`.`Club` 
DROP FOREIGN KEY `Club_ibfk_1`;
ALTER TABLE `dooodb`.`Club` 
DROP COLUMN `leader`,
DROP INDEX `Club_ibfk_1` ;

CREATE TABLE `dooodb`.`ClubMember` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `club` VARCHAR(45) NOT NULL DEFAULT '없음',
  `student` INT(11) NOT NULL DEFAULT '0',
  `level` TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`));

desc ClubMember;

select * from ClubMember;

START TRANSACTION;
ROLLBACK;
select * from Club;
select id from Student where id > 0 and id < 151; 
insert into ClubMember(student) select id from Student where id > 0 and id < 151; 

select * from ClubMember;

update ClubMember 
set club = (case 
when student < 51 then '요트부' 
when student >= 51 and student < 101 then '봉사부'
else '밴드부'
end);

select * from ClubMember;

select student from ClubMember where club = '요트부' order by rand() limit 1;

update ClubMember
set level = 2
where student = 49
;

select student from ClubMember where club = '봉사부' order by rand() limit 1;

update ClubMember
set level = 2
where student = 86
;

select student from ClubMember where club = '밴드부' order by rand() limit 1;

update ClubMember
set level = 2
where student = 102
;

select * from ClubMember where level = 2;

select student from ClubMember where club = '요트부' and level <>2 order by rand() limit 2; 

update ClubMember
set level = 1
where student = 10 or student = 41
;

select student from ClubMember where club = '봉사부' and level <>2 order by rand() limit 2;

update ClubMember
set level = 1
where student = 69 or student = 74
;

select student from ClubMember where club = '밴드부' and level <>2 order by rand() limit 2;

update ClubMember
set level = 1
where student = 146 or student = 125
;

select * from ClubMember where level = 1;

select * from ClubMember;

select c.id, c.club, s.name, c.level
from ClubMember c inner join Student s on c.student = s.id
order by level desc;

ALTER TABLE `dooodb`.`ClubMember` 
ADD INDEX `fk_student_student_idx` (`student` ASC);
;
ALTER TABLE `dooodb`.`ClubMember` 
ADD CONSTRAINT `fk_student_student`
  FOREIGN KEY (`student`)
  REFERENCES `dooodb`.`Student` (`id`)
  ON DELETE CASCADE
  ON UPDATE NO ACTION;


commit;