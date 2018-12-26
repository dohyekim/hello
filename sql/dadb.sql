create table dadb.Subject like dooodb.Subject;

alter table dadb.Subject drop column students;

select * from dadb.Subject;