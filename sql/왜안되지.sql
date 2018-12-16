drop function if exists fn_sub_cnt;

delimiter //
create function fn_sub_cnt(sub_name varchar(5))
returns smallint
begin
return 
(select count(*)
from Enroll en inner join Subject sub
on en.subject = sub.id
group by sub.name
having sub.name = sub_name);
end //

delimiter ;

select fn_sub_cnt('역사');

select name, fn_sub_cnt(name) from Subject;

