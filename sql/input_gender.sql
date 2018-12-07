select count(*) from Student where phone like '010-5%' or phone like '010-2%' or phone like '010-6%' or phone like '010-4%' or phone like '010-8%';

UPDATE Student 
SET 
    gender = (CASE
        WHEN
            phone LIKE '010-5%'
                OR phone LIKE '010-2%'
                OR phone LIKE '010-6%'
                OR phone LIKE '010-4%'
                OR phone LIKE '010-8%'
        THEN
            1
        ELSE 0
    END);

select gender, count(*) from Student group by gender;
           
select gender from Student;