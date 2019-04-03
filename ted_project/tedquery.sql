

drop table Talk;    
create table Talk(
	talk_id int not null primary key,
    title varchar(256),
    event varchar(125),
    talk_year smallint,
    tags varchar(1024),
    diff tinyint
    );
drop table Speaker;    
create table Speaker(
	speaker_id int not null primary key,
    name varchar(50),
    field varchar(256)
    );
    
drop table Korean;

/* unique key: talk_id/korcue */
create table Korean(
	talk_id int not null,
    korcue smallint,
    kor varchar(1024)    
    );

drop table English;
/* unique key: talk_id/engcue */    
create table English(
	talk_id int not null,
    engcue smallint,
    eng varchar(1024),
    isKorean tinyint
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





select * from Talk order by talk_id desc;
select * from Korean where talk_id = 3 and korcue = 3;
select * from English where talk_id = 4;


select * from English where eng regexp '([Tt]hank you)' and talk_id between 1 and 5;

select engcue from English
                        where eng regexp '([tT]hank you)'
                        and talk_id = 3;
                        
select talk_id from Talk where diff = 0;
select * from Speaker;
select k.kor from English e left outer join Korean k on e.talk_id = k.talk_id;

/*
update Talk t set isKorean = (select case when max(k.kor) is null then 0 else 1 end
                               from English e left outer join Korean k on e.talk_id = k.talk_id
							  where e.talk_id = t.talk_id)
where talk_id > 0;
*/


select * from Talk where talk_id = 3;
select * from Talk order by talk_id desc;
select engcue from English where talk_id = 578 order by engcue desc;
select korcue from Korean where talk_id = 578 order by korcue desc;

select talk_id from Talk where isKorean is null;
select eng from English where talk_id = 360;
select * from Talk order by talk_id desc;
select * from English where talk_id = 102;
select * from Korean where talk_id = 122;
select * from TalkSpeaker where talk_id = 122;

/*
update Talk t set diff = null;
*/

/*
delete from Talk where talk_id = ;
delete from English where talk_id = 24;
delete from Korean where talk_id = 6;
*/
select * from Talk t inner join TalkSpeaker ts on t.talk_id = ts.talk_id
		inner join Speaker s on ts.speaker_id = s.speaker_id
		where t.talk_id = 122;

select * from Korean where talk_id = 1;
select * from English where talk_id = 1;
select * from English where talk_id = 24;
select * from Korean where talk_id = 24;
select * from Korean order by talk_id desc;
select * from English where talk_id = 9;
select * from English order by talk_id desc;
select * from TalkSpeaker;
select * from Speaker where speaker_id = 24;


select * from English where talk_id = 4;

select talk_id, engcue 
	from English 
	where eng like '%Thank you%';
    
select talk_id, eng, engcue from English where talk_id = 6 and engcue = 357;

select talk_id, korcue, kor from Korean 
	where kor like '%감사합니다%';
    
select * from Korean where talk_id = 361;
select * from English where talk_id = 361;


select korcue, kor from Korean
	where talk_id =1 and
    korcue between 289 and 293;
    
select korcue, kor from Korean where talk_id = 4 and
korcue between 205 and 207;

select (@rownum := @rownum + 1) r
                        from Talk t, (select @rownum := 0) rn
                        order by r desc
                        limit 1;
                        
                        
select t.talk_id, t.field, max(engcue), max(eng) from English e inner join Talk t on t.talk_id = e.talk_id   
                        where eng like '%Thank you%'
                        and t.talk_id = 7
                        group by t.talk_id;
                        
select engcue from English where talk_id = 1 order by engcue desc limit 1;

select talk_id, korcue, kor from Korean 
                        where kor like '%비합리%'
                        and talk_id = 5;
                        
