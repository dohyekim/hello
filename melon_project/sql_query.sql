
truncate Album;
truncate MS_Song;
truncate Singer;
truncate Song_Rank;
truncate SongSinger;

select * from Album;
select * from MS_Song;
select * from Singer;
select * from Song_Rank;
select * from SongSinger;

select * from MS_Song ms inner join Album a on ms.album_id = a.album_id;
select * from SongSinger ss inner join MS_Song ms on ss.song = ms.song_no
							inner join Singer s on ss.singer = s.artist_id;
Alter table Song_Rank add constraint foreign key fk_song_rank (song_no) references MS_Song(song_no);
Alter table MS_Song add constraint foreign key fk_song_album (album_id) references Album(album_id);

set time_zone = 'Asia/Seoul';
select now();


