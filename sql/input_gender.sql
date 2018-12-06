select count(*) from Student where phone like '010-5%' or phone like '010-2%' or phone like '010-6%' or phone like '010-4%' or phone like '010-8%';

update Student set gender =
(case when phone like '010-5%' or 
		   phone like '010-2%' or 
		   phone like '010-6%' or 
	       phone like '010-4%' or 
	       phone like '010-8%' then 1 else 0 end);

select gender, count(*) from Student group by gender;
           
