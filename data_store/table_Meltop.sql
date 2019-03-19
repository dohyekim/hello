
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



create table dadb.Api(
id int not null auto_increment primary key,
title varchar(125),
link varchar(125),
description varchar(125),
bloggername varchar(125),
bloggerlink varchar(125),
postdate varchar(10)
);

drop table Blogger;
create table dadb.Blogger(
id int not null auto_increment primary key,
bloggerid varchar(256),
bloggername varchar(256),
bloggerlink varchar(256)
);

select * from dadb.Blogger;
truncate dadb.Blogger;

drop table BlogPost;
create table dadb.BlogPost(
id int not null auto_increment primary key,
title varchar(256),
link varchar(256),
bloggerid varchar(256),
postdate varchar(10)
);

select * from BlogPost;
truncate BlogPost;
-- Alter table Song_Rank add constraint foreign key fk_song_rank (song_no) references MS_Song(song_no);
alter table dadb.BlogPost add constraint foreign key fk_post_blogger(bloggerid) references dadb.Blogger(bloggerid);

create table AAA (
id int not null auto_increment primary key,
text1 text
);


select text1 from AAA;
truncate AAA;
