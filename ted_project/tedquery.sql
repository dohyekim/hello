

drop table Talk;    
create table Talk(
	talk_id int not null primary key,
    title varchar(256),
    event varchar(125),
    talk_year smallint,
    tags varchar(256)
    );
drop table Speaker;    
create table Speaker(
	speaker_id int not null primary key,
    name varchar(50),
    field varchar(125)
    );
    
drop table Korean;

/* unique key: talk_id/korcue */
create table Korean(
	talk_id int not null,
    korcue smallint,
    kor text    
    );

drop table English;
/* unique key: talk_id/engcue */    
create table English(
	talk_id int not null,
    engcue smallint,
    eng text
   );
    
drop table TalkSpeaker;
create table TalkSpeaker(
	talk_id int not null,
    speaker_id int not null
    );
    

/*
truncate table Talk;
truncate table Speaker;
truncate table Korean;
truncate table English;
truncate table TalkSpeaker;
*/


select * from Talk;
select * from Speaker;
select * from Korean where talk_id = 1 and korcue = 1;
select * from English where talk_id = 1 and engcue = 1;
select * from English where talk_id = 9;
select * from Korean where talk_id = 1;
select * from Korean;
select * from English;
select * from English;
select * from TalkSpeaker;
