update Departments d set emp_cnt = (select count(*) 
                                     from Employees e
                                     where d.department_id = e.department_id);


create or replace trigger tr_emp_cnt_delete before delete on Employees for each row
begin
    
    update Departments set emp_cnt = emp_cnt - 1
                        where department_id = :old.department_id;
end;

create or replace trigger tr_emp_cnt after insert on Employees for each row
begin
    update Departments set emp_cnt = emp_cnt + 1
                                        where department_id = :new.department_id;
end;
