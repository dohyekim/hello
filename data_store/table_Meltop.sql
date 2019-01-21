
-- utf-8(4byte) 설정
create table dadb.Meltop(
	id int not null auto_increment primary key,
    rank smallint not null,
    title varchar(1024),
    singer varchar(1024),
    likecnt int
    );
    
ALTER TABLE `dadb`.`Meltop` 
CHANGE COLUMN `title` `title` VARCHAR(1024) CHARACTER SET 'utf8mb4' NULL DEFAULT NULL ,
CHANGE COLUMN `singer` `singer` VARCHAR(1024) CHARACTER SET 'utf8mb4' NULL DEFAULT NULL ;

select * from dadb.Meltop;

truncate table dadb.Meltop;

select * from dadb.Meltop order by likecnt;

delete from dadb.Meltop;




