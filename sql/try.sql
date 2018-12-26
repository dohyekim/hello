create temporary table temp_res(

	과목 varchar(5) default '0', 
	rank1 varchar(5) default '0', 
	score1 smallint default 0, 
	rank2 varchar(5) default '0',
    score2 smallint default 0,
    rank3 varchar(5) default '0',
    score3 smallint default 0
);

set i = 1;
 select (concat('rank' + i)) from temp_res;