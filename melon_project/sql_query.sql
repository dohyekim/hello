/*
truncate Album;
truncate MS_Song;
truncate SongSinger;
truncate Singer;
truncate Song_Rank;
*/


select * from Album;
select * from MS_Song;
select * from Singer;
select * from Song_Rank;
select rank, genre from Song_Rank sr inner join MS_Song s on sr.song_no = s.song_no limit 99;
update Song_Rank set rankdt = "20190125";


CREATE TABLE `SongSinger` (
  `song_no` varchar(50) NOT NULL
  ,
  `artist_id` varchar(50) NOT NULL,
  PRIMARY KEY (`song_no`,`artist_id`),
  UNIQUE KEY `songsinger` (`song_no`,`artist_id`),
  KEY `fk_song_singer_idx` (`artist_id`),
  CONS
  
  TRAINT `fk_singer_song` FOREIGN KEY (`song_no`) REFERENCES `MS_Song` (`song_no`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_song_singer` FOREIGN KEY (`artist_id`) REFERENCES `Singer` (`artist_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


select * from SongSinger;

select * from MS_Song ms inner join Album a on ms.album_id = a.album_id;
select * from SongSinger ss inner join MS_Song ms on ss.song = ms.song_no
							inner join Singer s on ss.singer = s.artist_id;
Alter table Song_Rank add constraint foreign key fk_song_rank (song_no) references MS_Song(song_no);
Alter table MS_Song add constraint foreign key fk_song_album (album_id) references Album(album_id);

set time_zone = 'Asia/Seoul';
select now();


show processlist;

create table User(
id int unsigned not null auto_increment primary key,
passwd varchar(256),
email varchar(256) not null,
nickname varchar(33)
);

select * from User;

desc MS_Song;
desc Album;
desc SongSinger;
desc Singer;

select * from MS_Song;
select * from Singer;
select * from SongSinger;

select * from Album a inner join MS_Song s on a.album_id = s.album_id;

select * from blogdb.Post;
-- truncate Post;
select * from blogdb.User;
desc Post;
-- truncate User;
drop table User;

show processlist;

select